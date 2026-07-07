"""
SCH Replication v5 - JAM anisotropy parameter inspection.

Checks the kappa and beta_z/beta_r columns from JAM v2 HDU4 (JAMcyl+NFW)
and HDU5 (JAMsph+NFW) as candidate intrinsic coherence proxies, before
committing to either as the primary binning variable.

Reports:
  1. Basic distributions (count, mean, std, percentiles, NaN fraction)
     for kappa, beta_z (cyl), beta_r (sph) across the full catalogue
     and after our quality cuts.
  2. Correlation of kappa/beta_z with Lambda_Re and Sigma_Re -- to
     understand how much these overlap with what we already measured.
  3. Distribution by rough morphological class using the Emsellem et al.
     2011 fast/slow rotator boundary in the (Lambda_Re, Eps_MGE) plane.
  4. Scatter plots reported as percentile tables (no matplotlib needed)
     so results are readable in terminal output.

Usage:
    python inspect_anisotropy.py
"""

import numpy as np
import pandas as pd
from astropy.io import fits
from astropy.table import Table
from scipy.stats import spearmanr

DATA_DIR = "data"
JAM_FILE = "SDSSDR17_MaNGA_JAM_v2.fits"

# Quality cuts matching build_sample.py
CHI2_DOF_MAX = 5.0
Z_MIN, Z_MAX = 0.01, 0.15
PRIMARY_TARGETS = {0, 2}


def flat_to_pandas(tbl):
    names = [name for name in tbl.colnames if len(tbl[name].shape) <= 1]
    return tbl[names].to_pandas()


def load_jam():
    path = f"{DATA_DIR}/{JAM_FILE}"
    with fits.open(path) as hdul:
        master = flat_to_pandas(Table(hdul[1].data))
        cyl    = flat_to_pandas(Table(hdul[4].data))
        sph    = flat_to_pandas(Table(hdul[5].data))
    return master, cyl, sph


def decode_bytes(df):
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].apply(
                lambda v: v.decode("utf-8").strip() if isinstance(v, bytes) else v
            )
            df[col] = df[col].astype(str).str.strip()
    return df


def apply_quality_cuts(master, cyl):
    df = master.copy()
    df["chi2_dof_cyl"] = cyl["chi2_dof"].values
    df["kappa"]        = cyl["kappa"].values
    df["beta_z"]       = cyl["beta_z"].values
    df["fdm_Re_cyl"]   = cyl["fdm_Re"].values
    df["log_Ms_Re_cyl"]= cyl["log_Ms_Re"].values

    df = df[df["Qual"] >= 1]
    df = df[df["drp3qual"] == 1]
    df = df[(df["Lambda_Re"] > 0) & (df["Sigma_Re"] > 0)]
    df = df[df["Re_arcsec_MGE"] > 0]
    df = df[(df["z"] > Z_MIN) & (df["z"] < Z_MAX)]
    df = df[df["target"].isin(PRIMARY_TARGETS)]
    df = df[df["chi2_dof_cyl"] < CHI2_DOF_MAX]
    return df.reset_index(drop=True)


def percentile_table(series, label):
    s = series.dropna()
    pcts = [1, 5, 10, 25, 50, 75, 90, 95, 99]
    vals = np.percentile(s, pcts)
    print(f"\n  {label}  (N={len(s)}, NaN={series.isna().sum()})")
    print(f"  mean={s.mean():.4f}  std={s.std():.4f}  "
          f"min={s.min():.4f}  max={s.max():.4f}")
    header = "  " + "  ".join(f"p{p:02d}" for p in pcts)
    values = "  " + "  ".join(f"{v:+.3f}" for v in vals)
    print(header)
    print(values)


def fast_slow_classification(df):
    """
    Emsellem et al. 2011 boundary: fast rotator if
    Lambda_Re >= 0.31 * sqrt(Eps_MGE).
    Returns a Series with 'fast', 'slow', or 'undefined'.
    """
    boundary = 0.31 * np.sqrt(df["Eps_MGE"].clip(lower=0))
    cls = np.where(df["Lambda_Re"] >= boundary, "fast",
          np.where(df["Eps_MGE"].isna(), "undefined", "slow"))
    return pd.Series(cls, index=df.index)


def report_corr(label, x, y):
    mask = ~np.isnan(x) & ~np.isnan(y)
    if mask.sum() < 10:
        print(f"  {label:50s}  N<10, skip")
        return
    rho, p = spearmanr(x[mask], y[mask])
    print(f"  {label:50s}  N={mask.sum():5d}   rho={rho:+.3f}   p={p:.2e}")


def main():
    print("Loading JAM v2 ...")
    master, cyl, sph = load_jam()
    master = decode_bytes(master)

    print("=" * 70)
    print("1. Full catalogue distributions (before quality cuts)")
    print("=" * 70)

    percentile_table(cyl["kappa"],  "kappa  (JAMcyl+NFW, HDU4)")
    percentile_table(cyl["beta_z"], "beta_z (JAMcyl+NFW, HDU4)")
    percentile_table(sph["beta_r"], "beta_r (JAMsph+NFW, HDU5)")
    percentile_table(master["Lambda_Re"], "Lambda_Re (HDU1, for reference)")

    print("\n" + "=" * 70)
    print("2. After quality cuts")
    print("=" * 70)
    df = apply_quality_cuts(master, cyl)
    df["beta_r"] = sph["beta_r"].values[:len(df)]  # same row order confirmed
    print(f"  N after cuts: {len(df)}")

    percentile_table(df["kappa"],   "kappa  (post-cut)")
    percentile_table(df["beta_z"],  "beta_z (post-cut)")
    percentile_table(df["beta_r"],  "beta_r (post-cut)")

    print("\n" + "=" * 70)
    print("3. Correlations with Lambda_Re and Sigma_Re")
    print("   (how much do these overlap with what we already measured?)")
    print("=" * 70)
    report_corr("rho(kappa,  Lambda_Re)", df["kappa"].values,   df["Lambda_Re"].values)
    report_corr("rho(beta_z, Lambda_Re)", df["beta_z"].values,  df["Lambda_Re"].values)
    report_corr("rho(beta_r, Lambda_Re)", df["beta_r"].values,  df["Lambda_Re"].values)
    print()
    report_corr("rho(kappa,  Sigma_Re)",  df["kappa"].values,   df["Sigma_Re"].values)
    report_corr("rho(beta_z, Sigma_Re)",  df["beta_z"].values,  df["Sigma_Re"].values)
    report_corr("rho(beta_r, Sigma_Re)",  df["beta_r"].values,  df["Sigma_Re"].values)
    print()
    report_corr("rho(kappa,  fdm_Re_cyl)",df["kappa"].values,   df["fdm_Re_cyl"].values)
    report_corr("rho(beta_z, fdm_Re_cyl)",df["beta_z"].values,  df["fdm_Re_cyl"].values)

    print("\n" + "=" * 70)
    print("4. Fast / slow rotator classification (Emsellem et al. 2011)")
    print("   Lambda_Re >= 0.31 * sqrt(Eps_MGE)")
    print("=" * 70)
    df["kin_class"] = fast_slow_classification(df)
    counts = df["kin_class"].value_counts()
    print(f"\n  Classification breakdown (N={len(df)}):")
    for cls, n in counts.items():
        print(f"    {cls:12s}: {n:5d}  ({100*n/len(df):.1f}%)")

    for cls in ["fast", "slow"]:
        sub = df[df["kin_class"] == cls]
        print(f"\n  --- {cls} rotators (N={len(sub)}) ---")
        percentile_table(sub["kappa"],  "kappa")
        percentile_table(sub["beta_z"], "beta_z")
        percentile_table(sub["Lambda_Re"], "Lambda_Re")
        percentile_table(sub["Sigma_Re"],  "Sigma_Re")

    print("\n" + "=" * 70)
    print("5. kappa and beta_z: are they defined / well-behaved for")
    print("   slow rotators specifically?")
    print("=" * 70)
    slow = df[df["kin_class"] == "slow"]
    print(f"\n  Slow rotators: N={len(slow)}")
    print(f"  kappa  NaN fraction: {slow['kappa'].isna().mean():.3f}")
    print(f"  beta_z NaN fraction: {slow['beta_z'].isna().mean():.3f}")
    print(f"  chi2_dof_cyl mean:   {slow['chi2_dof_cyl'].mean():.4f}")
    print(f"  chi2_dof_cyl > 2:    {(slow['chi2_dof_cyl'] > 2).sum()} "
          f"({100*(slow['chi2_dof_cyl'] > 2).mean():.1f}%)")

    print("\n  kappa distribution within slow rotators:")
    percentile_table(slow["kappa"], "kappa (slow rotators)")
    percentile_table(slow["beta_z"], "beta_z (slow rotators)")

    print("\n  Correlation between kappa and Lambda_Re within slow rotators:")
    report_corr("rho(kappa, Lambda_Re) [slow only]",
                slow["kappa"].values, slow["Lambda_Re"].values)
    report_corr("rho(beta_z, Lambda_Re) [slow only]",
                slow["beta_z"].values, slow["Lambda_Re"].values)
    report_corr("rho(kappa, Sigma_Re) [slow only]",
                slow["kappa"].values, slow["Sigma_Re"].values)


if __name__ == "__main__":
    main()
