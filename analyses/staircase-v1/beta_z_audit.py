"""
SCH Replication v5 - beta_z structural audit.

Two questions, in order of importance:

1. MODEL-INTERNAL CIRCULARITY CHECK:
   beta_z and log_Ms_Re_cyl both come from the same JAM model.
   Does beta_z still predict rar_resid when we replace JAM stellar
   mass with Firefly photometric mass (independent of kinematics)?
   If yes: JAM-internal coupling is not the explanation.
   If no: the signal was model-internal circularity.

2. KNOWN STRUCTURAL RELATIONS:
   Does beta_z simply track known structural properties --
   ellipticity, Sersic index, age, metallicity -- that might
   independently predict the RAR residual?

Usage:
    python beta_z_audit.py
"""

import numpy as np
import pandas as pd
from scipy.stats import spearmanr, rankdata
from astropy.io import fits
from astropy.table import Table

CSV      = "manga_merged_with_rar.csv"
JAM_FILE = "data/SDSSDR17_MaNGA_JAM_v2.fits"
FF_FILE  = "data/manga-firefly-v3_1_1-mastar.fits"
DRP_FILE = "data/drpall-v3_1_1.fits"

G_SI   = 6.674e-11
MSUN_KG = 1.989e30
KPC_M   = 3.0857e19


def flat_to_pandas(hdu):
    tbl = Table(hdu.data)
    names = [n for n in tbl.colnames if len(tbl[n].shape) <= 1]
    return tbl[names].to_pandas()


def decode_plateifu(series):
    return series.apply(
        lambda v: v.decode().strip() if isinstance(v, bytes) else str(v).strip()
    )


def load_jam_extras():
    with fits.open(JAM_FILE) as hdul:
        master = flat_to_pandas(hdul[1])
        cyl    = flat_to_pandas(hdul[4])
    master["plateifu"] = decode_plateifu(master["plateifu"])
    return pd.DataFrame({
        "plateifu": master["plateifu"],
        "Eps_MGE":  master["Eps_MGE"],
        "beta_z":   cyl["beta_z"],
        # NOT loading log_Mt_Re here -- already in CSV as log_Mt_Re_cyl
    })


def load_firefly_pops():
    """
    Load stellar population parameters only (age, metallicity).
    PHOTOMETRIC_MASS already in the CSV from build_sample.py.
    """
    with fits.open(FF_FILE) as hdul:
        gi = flat_to_pandas(hdul["GALAXY_INFO"])
        gp = flat_to_pandas(hdul["GLOBAL_PARAMETERS"])
    gi["plateifu"] = decode_plateifu(gi["PLATEIFU"])
    return pd.DataFrame({
        "plateifu":   gi["plateifu"],
        "LW_AGE_1Re": gp["LW_AGE_1Re"].values,
        "LW_Z_1Re":   gp["LW_Z_1Re"].values,
        "MW_Z_1Re":   gp["MW_Z_1Re"].values,
    })


def load_sersic():
    with fits.open(DRP_FILE) as hdul:
        drp = flat_to_pandas(hdul["MANGA"])
    drp["plateifu"] = decode_plateifu(drp["plateifu"])
    return drp[["plateifu", "nsa_sersic_n"]].copy()


def partial_corr_spearman(x, y, controls):
    def resid(a, B):
        A = np.column_stack([B, np.ones(len(a))])
        coef, _, _, _ = np.linalg.lstsq(A, a, rcond=None)
        return a - A @ coef
    rx = rankdata(x)
    ry = rankdata(y)
    rc = np.column_stack([rankdata(c) for c in controls])
    return spearmanr(resid(rx, rc), resid(ry, rc))


def report(label, rho, p, n):
    print(f"  {label:56s}  N={n:5d}   rho={rho:+.3f}   p={p:.2e}")


def add_tertiles(df):
    df = df.copy()
    df["mass_tertile"] = pd.qcut(
        df["log_Ms_Re_cyl"], 3, labels=["Low", "Mid", "High"]
    )
    return df


def compute_rar_resid_firefly(df):
    """
    Recompute rar_resid using Firefly PHOTOMETRIC_MASS.
    Column is already in CSV as PHOTOMETRIC_MASS (log10 Msun units,
    confirmed from earlier inspection: mean=10.52, range 8.8-12.2).
    """
    pm = df["PHOTOMETRIC_MASS"]
    valid = pm.notna() & (pm > 0) & (pm < 15)

    re_m     = df["Re_kpc"].values * KPC_M
    sigma_ms = df["STELLAR_SIGMA_1RE"].values * 1000.0
    mstar_kg = np.where(valid, (10 ** pm.values) * MSUN_KG, np.nan)

    with np.errstate(divide="ignore", invalid="ignore"):
        g_obs = 5.0 * sigma_ms**2 / re_m
        g_bar = G_SI * mstar_kg / re_m**2
        resid = np.log10(g_obs / g_bar)

    resid[~valid] = np.nan
    return resid


def main():
    # ------------------------------------------------------------------
    # Load and merge
    # ------------------------------------------------------------------
    df = pd.read_csv(CSV)

    df = df.merge(load_jam_extras(),   on="plateifu", how="left")
    df = df.merge(load_firefly_pops(), on="plateifu", how="left")
    df = df.merge(load_sersic(),       on="plateifu", how="left")
    df = add_tertiles(df)

    df["kin_class"] = np.where(
        df["Lambda_Re"] >= 0.31 * np.sqrt(df["Eps_MGE"].clip(lower=0)),
        "fast", "slow"
    )

    with np.errstate(divide="ignore", invalid="ignore"):
        df["log_Re_kpc"] = np.log10(df["Re_kpc"])
        df["log_Ms"]     = df["log_Ms_Re_cyl"]

    # Sentinel cleanup
    sentinel = -9999.0
    for col in ["PHOTOMETRIC_MASS", "LW_AGE_1Re", "LW_Z_1Re", "MW_Z_1Re"]:
        if col in df.columns:
            df.loc[df[col] <= sentinel + 1, col] = np.nan

    df["rar_resid_firefly"] = compute_rar_resid_firefly(df)
    df["rar_resid_firefly"].replace([np.inf, -np.inf], np.nan, inplace=True)

    print(f"Sample N={len(df)}")
    print(f"PHOTOMETRIC_MASS valid: {df['PHOTOMETRIC_MASS'].notna().sum()}")
    print(f"rar_resid_firefly valid:{df['rar_resid_firefly'].notna().sum()}")
    print(f"LW_AGE_1Re valid:       {df['LW_AGE_1Re'].notna().sum()}")
    print(f"LW_Z_1Re valid:         {df['LW_Z_1Re'].notna().sum()}")
    print(f"nsa_sersic_n valid:     {df['nsa_sersic_n'].notna().sum()}")
    print(f"Eps_MGE valid:          {df['Eps_MGE'].notna().sum()}")
    print(f"Fast: {(df['kin_class']=='fast').sum()}  "
          f"Slow: {(df['kin_class']=='slow').sum()}\n")

    # ------------------------------------------------------------------
    # PART 1: Model-internal circularity check
    # ------------------------------------------------------------------
    print("=" * 70)
    print("PART 1: MODEL-INTERNAL CIRCULARITY CHECK")
    print("        beta_z vs rar_resid_JAM  (JAM mass in denominator)")
    print("        beta_z vs rar_resid_FIREFLY (photometric mass, independent)")
    print("=" * 70)

    groups = [
        ("Full",         pd.Series([True]*len(df), index=df.index)),
        ("fast",         df["kin_class"] == "fast"),
        ("slow",         df["kin_class"] == "slow"),
        ("Low",          df["mass_tertile"] == "Low"),
        ("Mid",          df["mass_tertile"] == "Mid"),
        ("High",         df["mass_tertile"] == "High"),
    ]

    for grp_label, mask in groups:
        sub = df[mask].dropna(
            subset=["beta_z", "rar_resid", "rar_resid_firefly",
                    "log_Ms", "log_Re_kpc"]
        )
        if len(sub) < 20:
            continue

        r1,  p1  = spearmanr(sub["beta_z"], sub["rar_resid"])
        r1p, p1p = partial_corr_spearman(
            sub["beta_z"].values, sub["rar_resid"].values,
            [sub["log_Ms"].values, sub["log_Re_kpc"].values]
        )
        r2,  p2  = spearmanr(sub["beta_z"], sub["rar_resid_firefly"])
        r2p, p2p = partial_corr_spearman(
            sub["beta_z"].values, sub["rar_resid_firefly"].values,
            [sub["log_Ms"].values, sub["log_Re_kpc"].values]
        )

        print(f"\n  --- {grp_label} (N={len(sub)}) ---")
        report("raw  rho(beta_z, rar_resid_JAM)",        r1,  p1,  len(sub))
        report("part rho(beta_z, rar_resid_JAM)|Ms,Re",  r1p, p1p, len(sub))
        report("raw  rho(beta_z, rar_resid_FIREFLY)",    r2,  p2,  len(sub))
        report("part rho(beta_z, rar_resid_FF)|Ms,Re",   r2p, p2p, len(sub))

    # ------------------------------------------------------------------
    # PART 2: Known structural relation audit
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("PART 2: KNOWN STRUCTURAL RELATIONS")
    print("        Does beta_z track structural properties that")
    print("        independently predict the RAR residual?")
    print("=" * 70)

    struct_vars = [
        ("Eps_MGE",      "ellipticity"),
        ("nsa_sersic_n", "Sersic n"),
        ("LW_AGE_1Re",   "LW age"),
        ("LW_Z_1Re",     "LW metallicity"),
        ("MW_Z_1Re",     "MW metallicity"),
    ]

    print("\n  2a. rho(beta_z, structural variable):")
    for var, label in struct_vars:
        for grp_label, mask in [
            ("Full", pd.Series([True]*len(df), index=df.index)),
            ("slow", df["kin_class"] == "slow"),
        ]:
            sub = df[mask].dropna(subset=["beta_z", var])
            if len(sub) < 20:
                continue
            rho, p = spearmanr(sub["beta_z"], sub[var])
            report(f"{grp_label:6s} rho(beta_z, {label})", rho, p, len(sub))

    print("\n  2b. rho(structural variable, rar_resid):")
    for var, label in struct_vars:
        for grp_label, mask in [
            ("Full", pd.Series([True]*len(df), index=df.index)),
            ("slow", df["kin_class"] == "slow"),
        ]:
            sub = df[mask].dropna(subset=[var, "rar_resid"])
            if len(sub) < 20:
                continue
            rho, p = spearmanr(sub[var], sub["rar_resid"])
            report(f"{grp_label:6s} rho({label}, rar_resid)", rho, p, len(sub))

    print("\n  2c. Partial rho(beta_z, rar_resid) additionally controlling")
    print("      for each structural variable in turn:")
    for var, label in struct_vars:
        for grp_label, mask in [
            ("Full", pd.Series([True]*len(df), index=df.index)),
            ("slow", df["kin_class"] == "slow"),
        ]:
            sub = df[mask].dropna(
                subset=["beta_z", "rar_resid", "log_Ms", "log_Re_kpc", var]
            )
            if len(sub) < 20:
                continue
            rho, p = partial_corr_spearman(
                sub["beta_z"].values,
                sub["rar_resid"].values,
                [sub["log_Ms"].values,
                 sub["log_Re_kpc"].values,
                 sub[var].values]
            )
            report(
                f"{grp_label:6s} partial|Ms,Re,{label[:12]}",
                rho, p, len(sub)
            )

    # ------------------------------------------------------------------
    # PART 3: Is beta_z absorbed into the JAM mass estimate?
    # ------------------------------------------------------------------
    print("\n" + "=" * 70)
    print("PART 3: IS beta_z ABSORBED INTO THE JAM MASS ESTIMATE?")
    print("        If beta_z drives the mass fit, its correlation with")
    print("        rar_resid could be a model tautology.")
    print("=" * 70)

    for grp_label, mask in [
        ("Full", pd.Series([True]*len(df), index=df.index)),
        ("fast", df["kin_class"] == "fast"),
        ("slow", df["kin_class"] == "slow"),
    ]:
        sub = df[mask].dropna(
            subset=["beta_z", "log_Ms_Re_cyl", "fdm_Re_cyl", "log_Mt_Re_cyl"]
        )
        if len(sub) < 20:
            continue
        r_ms,  p_ms  = spearmanr(sub["beta_z"], sub["log_Ms_Re_cyl"])
        r_fdm, p_fdm = spearmanr(sub["beta_z"], sub["fdm_Re_cyl"])
        r_tot, p_tot = spearmanr(sub["beta_z"], sub["log_Mt_Re_cyl"])
        print(f"\n  --- {grp_label} (N={len(sub)}) ---")
        report("rho(beta_z, log_Ms_Re_cyl)",  r_ms,  p_ms,  len(sub))
        report("rho(beta_z, log_Mt_Re_cyl)",  r_tot, p_tot, len(sub))
        report("rho(beta_z, fdm_Re_cyl)",     r_fdm, p_fdm, len(sub))


if __name__ == "__main__":
    main()
