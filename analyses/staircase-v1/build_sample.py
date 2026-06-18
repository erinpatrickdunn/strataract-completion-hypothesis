"""
SCH Replication v5 - Sample construction.

Merges:
  - SDSSDR17_MaNGA_JAM_v2.fits     (HDU1 master row + HDU4 JAMcyl+NFW
                                     primary + HDU5 JAMsph+NFW cross-check)
  - drpall-v3_1_1.fits              (HDU1 'MANGA': targeting bits, quality)
  - dapall-v3_1_1-3.1.0.fits        (HDU3 'HYB10-MILESHC-MASTARSSP':
                                     STELLAR_SIGMA_1RE, DAPDONE, DAPQUAL)
  - manga-firefly-v3_1_1-mastar.fits (GALAXY_INFO: PHOTOMETRIC_MASS)

Applies quality cuts, computes the log_excess proxy (cylindrical and
spherical), and writes manga_merged.csv for downstream staircase /
diagnostic analysis.

Usage:
    python build_sample.py
"""

import os
import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.table import Table

DATA_DIR = "data"
OUT_CSV = "manga_merged.csv"

JAM_FILE = "SDSSDR17_MaNGA_JAM_v2.fits"
DRPALL_FILE = "drpall-v3_1_1.fits"
DAPALL_FILE = "dapall-v3_1_1-3.1.0.fits"
FIREFLY_FILE = "manga-firefly-v3_1_1-mastar.fits"

CHI2_DOF_MAX = 5.0
SIGMA_MIN, SIGMA_MAX = 20.0, 400.0   # km/s, as in Paper B quality cuts
Z_MIN, Z_MAX = 0.01, 0.15
PRIMARY_TARGETS = {0, 2}             # JAM HDU1 'target' flag

# Alignment check threshold. inc_deg is a free fit parameter that differs
# slightly between model variants (NFW vs no-NFW, cyl vs sph) even for the
# same galaxy, so we check correlation rather than exact equality. A value
# this high can only happen if the rows are in the same order across HDUs.
ALIGNMENT_CORR_MIN = 0.7


def flat_to_pandas(tbl):
    """Convert an astropy Table to pandas, dropping multidimensional columns."""
    names = [name for name in tbl.colnames if len(tbl[name].shape) <= 1]
    dropped = [name for name in tbl.colnames if name not in names]
    if dropped:
        print(f"    (dropping multidimensional columns: {dropped})")
    return tbl[names].to_pandas()


def load_jam(path):
    with fits.open(path) as hdul:
        master_tbl = Table(hdul[1].data)
        cyl_tbl = Table(hdul[4].data)
        sph_tbl = Table(hdul[5].data)
        beta_z_only_tbl = Table(hdul[2].data)

    master = flat_to_pandas(master_tbl)
    cyl = flat_to_pandas(cyl_tbl)
    sph = flat_to_pandas(sph_tbl)
    beta_z_only = flat_to_pandas(beta_z_only_tbl)

    assert len(master) == len(cyl) == len(sph), (
        f"JAM HDU row counts differ: {len(master)}, {len(cyl)}, {len(sph)}"
    )

    # Alignment sanity check: HDU2 (beta_z, no NFW) and HDU4 (beta_z + NFW)
    # describe the same axisymmetric geometry for the same galaxy, so
    # inc_deg and chi2_dof should be highly correlated row-for-row if the
    # HDUs share row order, even though individual fit values differ
    # slightly between model variants.
    a = np.asarray(beta_z_only["inc_deg"], dtype=float)
    b = np.asarray(cyl["inc_deg"], dtype=float)
    valid = ~np.isnan(a) & ~np.isnan(b)
    corr = np.corrcoef(a[valid], b[valid])[0, 1]
    print(f"  JAM HDU alignment check: HDU2 vs HDU4 inc_deg correlation = {corr:.4f}")
    if corr < ALIGNMENT_CORR_MIN:
        raise RuntimeError(
            f"JAM HDU alignment check FAILED: HDU2 vs HDU4 inc_deg "
            f"correlation = {corr:.4f} (< {ALIGNMENT_CORR_MIN}). Do not "
            f"trust the row-position merge below until this is resolved."
        )
    print("  [ok] JAM HDU row-alignment check passed")

    # Suffix the model-dependent columns before concatenation
    cyl = cyl.add_suffix("_cyl")
    sph = sph.add_suffix("_sph")

    jam = pd.concat(
        [master.reset_index(drop=True),
         cyl.reset_index(drop=True),
         sph.reset_index(drop=True)],
        axis=1,
    )
    return jam


def load_drpall(path):
    with fits.open(path) as hdul:
        drp = flat_to_pandas(Table(hdul["MANGA"].data))
    keep = [
        "plateifu", "mangaid", "objra", "objdec", "nsa_z",
        "nsa_elpetro_th50_r", "nsa_elpetro_ba", "nsa_elpetro_mass",
        "drp3qual", "mngtarg1",
    ]
    return drp[keep].copy()


def load_dapall(path):
    with fits.open(path) as hdul:
        dap = flat_to_pandas(Table(hdul["HYB10-MILESHC-MASTARSSP"].data))
    keep = ["PLATEIFU", "DAPDONE", "DAPQUAL", "STELLAR_SIGMA_1RE",
            "STELLAR_RCHI2_1RE"]
    dap = dap[keep].copy()
    dap = dap.rename(columns={"PLATEIFU": "plateifu"})
    return dap


def load_firefly(path):
    with fits.open(path) as hdul:
        gi = flat_to_pandas(Table(hdul["GALAXY_INFO"].data))
    keep = ["PLATEIFU", "PHOTOMETRIC_MASS"]
    gi = gi[keep].copy()
    gi = gi.rename(columns={"PLATEIFU": "plateifu"})
    return gi


def decode_bytes(df):
    """astropy->pandas sometimes leaves bytes objects for string columns."""
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].apply(
                lambda v: v.decode("utf-8").strip() if isinstance(v, bytes) else v
            )
            if df[col].dtype == object:
                df[col] = df[col].astype(str).str.strip()
    return df


def main():
    print("Loading JAM v2 ...")
    jam = load_jam(os.path.join(DATA_DIR, JAM_FILE))
    jam = decode_bytes(jam)
    print(f"  {len(jam)} rows")

    print("Loading DRPall ...")
    drp = decode_bytes(load_drpall(os.path.join(DATA_DIR, DRPALL_FILE)))
    print(f"  {len(drp)} rows")

    print("Loading DAPall ...")
    dap = decode_bytes(load_dapall(os.path.join(DATA_DIR, DAPALL_FILE)))
    print(f"  {len(dap)} rows")

    print("Loading Firefly ...")
    ff = decode_bytes(load_firefly(os.path.join(DATA_DIR, FIREFLY_FILE)))
    print(f"  {len(ff)} rows")

    n0 = len(jam)
    print(f"\nStarting sample: {n0}")

    df = jam.copy()

    # --- JAM-internal quality cuts ---
    df = df[df["Qual"] >= 1]
    print(f"  after Qual >= 1: {len(df)}  (removed {n0 - len(df)})")
    n1 = len(df)

    df = df[df["drp3qual"] == 1]
    print(f"  after drp3qual == 1: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    df = df[(df["Lambda_Re"] > 0) & (df["Sigma_Re"] > 0)]
    print(f"  after Lambda_Re>0 & Sigma_Re>0: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    df = df[df["Re_arcsec_MGE"] > 0]
    print(f"  after Re_arcsec_MGE > 0: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    df = df[(df["z"] > Z_MIN) & (df["z"] < Z_MAX)]
    print(f"  after {Z_MIN} < z < {Z_MAX}: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    df = df[df["target"].isin(PRIMARY_TARGETS)]
    print(f"  after target in {PRIMARY_TARGETS} (primary sample): {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    df = df[df["chi2_dof_cyl"] < CHI2_DOF_MAX]
    print(f"  after chi2_dof_cyl < {CHI2_DOF_MAX}: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    # --- Cross-match with Firefly (inner join) ---
    df = df.merge(ff, on="plateifu", how="inner")
    print(f"  after Firefly inner join: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    # --- Cross-match with DAPall, require DAPDONE and clean DAPQUAL ---
    df = df.merge(dap, on="plateifu", how="inner")
    print(f"  after DAPall inner join: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    df = df[df["DAPDONE"] == 1]
    print(f"  after DAPDONE == 1: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    # DAPQUAL bit 30 = CRITICAL
    critical_bit = 1 << 30
    df = df[(df["DAPQUAL"].astype(np.int64) & critical_bit) == 0]
    print(f"  after DAPQUAL CRITICAL bit clear: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    df = df[(df["STELLAR_SIGMA_1RE"] > SIGMA_MIN) & (df["STELLAR_SIGMA_1RE"] < SIGMA_MAX)]
    print(f"  after {SIGMA_MIN} < STELLAR_SIGMA_1RE < {SIGMA_MAX}: {len(df)}  (removed {n1 - len(df)})")
    n1 = len(df)

    # --- DRPall merge for inclination / targeting cross-checks ---
    drp_renamed = drp.rename(columns={c: f"drp_{c}" for c in drp.columns if c != "plateifu"})
    df = df.merge(drp_renamed, on="plateifu", how="left")
    print(f"  after DRPall left join (for inc/targeting checks): {len(df)}")

    # --- Derived quantities ---
    df["log_excess"] = df["log_Mt_Re_cyl"] - df["log_Ms_Re_cyl"]
    df["log_excess_sph"] = df["log_Mt_Re_sph"] - df["log_Ms_Re_sph"]
    df["lambda_r"] = df["Lambda_Re"]

    print(f"\nFinal sample: {len(df)} galaxies (started from {n0})")

    out_cols = [
        "plateifu", "mangaid", "z", "Lambda_Re", "lambda_r", "Sigma_Re",
        "Re_arcsec_MGE", "Qual", "drp3qual", "target",
        # cylindrical (primary)
        "log_Ms_Re_cyl", "log_Mt_Re_cyl", "fdm_Re_cyl", "chi2_dof_cyl",
        "inc_deg_cyl", "log_excess",
        # spherical (cross-check)
        "log_Ms_Re_sph", "log_Mt_Re_sph", "fdm_Re_sph", "chi2_dof_sph",
        "inc_deg_sph", "log_excess_sph",
        # mass estimator controls
        "nsa_elpetro_mass", "PHOTOMETRIC_MASS",
        # DAP for proper RAR residual (next step)
        "STELLAR_SIGMA_1RE", "STELLAR_RCHI2_1RE",
        # DRPall cross-checks
        "drp_nsa_elpetro_ba", "drp_nsa_elpetro_th50_r", "drp_mngtarg1",
    ]
    missing = [c for c in out_cols if c not in df.columns]
    if missing:
        raise RuntimeError(f"Missing expected columns: {missing}")

    df[out_cols].to_csv(OUT_CSV, index=False)
    print(f"\nWrote {OUT_CSV} ({len(df)} rows, {len(out_cols)} columns)")


if __name__ == "__main__":
    main()
