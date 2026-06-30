"""
SCH Replication v5 - Proper RAR residual.

Computes the actual Radial Acceleration Relation residual

    rar_resid = log10(g_obs / g_bar)

    g_obs = 5 * sigma_star^2 / R_e      (spherical Jeans, Paper B definition)
    g_bar = G * M_star / R_e^2

using DAPall STELLAR_SIGMA_1RE for sigma_star and JAM log_Ms_Re_cyl for
M_star, with R_e converted from Re_arcsec_MGE to physical kpc via the
angular diameter distance at each galaxy's redshift (Planck18 cosmology).

Then:
  - Re-runs the mass-tertile x lambda_r-quintile staircase on rar_resid
    (replacing the log_excess proxy).
  - Checks whether the High-tertile censoring artifact (fdm_Re_cyl floor)
    survives on rar_resid, since rar_resid does not mechanically involve
    log_Mt_Re or fdm_Re_cyl.
  - Repeats the floor check for Low and Mid tertiles for completeness.
  - Compares M_star estimators: JAM (cyl), JAM (sph), NSA photometric,
    Firefly photometric -- as an estimator-bias cross-check analogous to
    the original Paper B Section 2.3.

Usage:
    python rar_residual_analysis.py
"""

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from astropy.cosmology import Planck18
import astropy.units as u
import astropy.constants as const

CSV = "manga_merged.csv"
SENTINEL = -9999.0
FLOOR_FDM_THRESH = 0.05

ARCSEC_TO_RAD = np.pi / (180.0 * 3600.0)


def mask_sentinels(df, cols):
    for c in cols:
        df.loc[df[c] <= SENTINEL + 1, c] = np.nan
    return df


def compute_re_kpc(df):
    """Convert Re_arcsec_MGE -> physical kpc using angular diameter distance."""
    d_a = Planck18.angular_diameter_distance(df["z"].values)  # Mpc, vectorized
    re_kpc = (df["Re_arcsec_MGE"].values * ARCSEC_TO_RAD) * (d_a.to(u.kpc).value)
    return re_kpc


def compute_rar_residual(df, log_mstar_col, re_kpc_col="Re_kpc",
                          sigma_col="STELLAR_SIGMA_1RE"):
    """
    Returns rar_resid = log10(g_obs / g_bar) for the given stellar-mass
    column, in SI units throughout.
    """
    re_m = (df[re_kpc_col].values * u.kpc).to(u.m).value
    sigma_ms = (df[sigma_col].values * u.km / u.s).to(u.m / u.s).value
    mstar_kg = (10 ** df[log_mstar_col].values * u.Msun).to(u.kg).value

    g_obs = 5.0 * sigma_ms**2 / re_m
    g_bar = const.G.value * mstar_kg / re_m**2

    with np.errstate(divide="ignore", invalid="ignore"):
        resid = np.log10(g_obs / g_bar)
    return resid


def add_tertiles(df, mass_col="log_Ms_Re_cyl"):
    df = df.copy()
    df["mass_tertile"] = pd.qcut(df[mass_col], 3, labels=["Low", "Mid", "High"])
    return df


def report_staircase(df, label, value_col):
    sub = df[["lambda_r", value_col]].dropna()
    rho, p = spearmanr(sub["lambda_r"], sub[value_col])
    print(f"  {label:14s}  N={len(sub):5d}   Spearman rho={rho:+.3f}   p={p:.2e}")
    return rho, p


def floor_check(df, label, value_col):
    sub = df.dropna(subset=["lambda_r", value_col, "fdm_Re_cyl"]).copy()
    sub["lambda_r_quintile"] = pd.qcut(sub["lambda_r"], 5, labels=[f"Q{i+1}" for i in range(5)])

    print(f"\n  --- {label}: N={len(sub)} ---")
    report_staircase(sub, "all", value_col)
    nofloor = sub[sub["fdm_Re_cyl"] >= FLOOR_FDM_THRESH]
    report_staircase(nofloor, f"fdm>={FLOOR_FDM_THRESH}", value_col)
    print(f"    (excluded {len(sub) - len(nofloor)} of {len(sub)})")

    g = sub.groupby("lambda_r_quintile")
    summary = g.agg(
        N=("lambda_r", "size"),
        value_mean=(value_col, "mean"),
        value_median=(value_col, "median"),
        fdm_mean=("fdm_Re_cyl", "mean"),
    )
    floor_frac = g.apply(lambda d: (d["fdm_Re_cyl"] < FLOOR_FDM_THRESH).mean())
    summary["floor_frac"] = floor_frac
    # correlation between the value and fdm itself, within this tertile
    rho_fdm, p_fdm = spearmanr(sub[value_col], sub["fdm_Re_cyl"])
    print(f"    Spearman rho({value_col}, fdm_Re_cyl) = {rho_fdm:+.3f}  p={p_fdm:.2e}")
    print(summary)


def main():
    df = pd.read_csv(CSV)
    df = mask_sentinels(df, ["PHOTOMETRIC_MASS", "drp_nsa_elpetro_ba", "drp_nsa_elpetro_th50_r"])

    print("=" * 70)
    print("Computing physical R_e and RAR residual")
    print("=" * 70)

    df["Re_kpc"] = compute_re_kpc(df)
    print(f"\nRe_kpc summary:\n{df['Re_kpc'].describe()}")

    # Primary residual: JAM cylindrical stellar mass
    df["rar_resid"] = compute_rar_residual(df, "log_Ms_Re_cyl")
    print(f"\nrar_resid (JAMcyl M_star) summary:\n{df['rar_resid'].describe()}")

    # Cross-check estimators
    df["rar_resid_sph"] = compute_rar_residual(df, "log_Ms_Re_sph")
    df["rar_resid_nsa"] = compute_rar_residual(df, "nsa_elpetro_mass")
    # Firefly PHOTOMETRIC_MASS: check units/sentinel before use
    valid_ff = df["PHOTOMETRIC_MASS"].notna() & (df["PHOTOMETRIC_MASS"] > 0)
    print(f"\nPHOTOMETRIC_MASS valid (non-sentinel, >0): {valid_ff.sum()} / {len(df)}")
    print(df.loc[valid_ff, "PHOTOMETRIC_MASS"].describe())
    df["rar_resid_firefly"] = np.nan
    df.loc[valid_ff, "rar_resid_firefly"] = compute_rar_residual(
        df.loc[valid_ff], "PHOTOMETRIC_MASS"
    )

    df = add_tertiles(df, "log_Ms_Re_cyl")

    print("\n" + "=" * 70)
    print("STAIRCASE on proper RAR residual (rar_resid, JAMcyl M_star)")
    print("=" * 70)
    report_staircase(df, "Full", "rar_resid")
    for tert in ["Low", "Mid", "High"]:
        report_staircase(df[df["mass_tertile"] == tert], tert, "rar_resid")

    print("\n" + "=" * 70)
    print("Floor/censoring check on rar_resid, by mass tertile")
    print("(does the fdm_Re_cyl floor artifact survive on the proper residual?)")
    print("=" * 70)
    for tert in ["Low", "Mid", "High"]:
        floor_check(df[df["mass_tertile"] == tert], f"{tert} tertile (rar_resid)", "rar_resid")

    print("\n" + "=" * 70)
    print("For comparison: same floor check on the log_excess proxy")
    print("=" * 70)
    for tert in ["Low", "Mid", "High"]:
        floor_check(df[df["mass_tertile"] == tert], f"{tert} tertile (log_excess)", "log_excess")

    print("\n" + "=" * 70)
    print("Estimator comparison (Full sample, rar_resid under each M_star)")
    print("=" * 70)
    report_staircase(df, "JAMcyl", "rar_resid")
    report_staircase(df, "JAMsph", "rar_resid_sph")
    report_staircase(df, "NSA photo", "rar_resid_nsa")
    report_staircase(df.loc[valid_ff], "Firefly photo", "rar_resid_firefly")

    df.to_csv("manga_merged_with_rar.csv", index=False)
    print("\nWrote manga_merged_with_rar.csv")


if __name__ == "__main__":
    main()
