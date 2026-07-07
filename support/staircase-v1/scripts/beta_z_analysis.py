"""
SCH Replication v5 - beta_z as independent coherence axis.

The question is NOT whether beta_z substitutes for lambda_r.
The question is whether beta_z carries independent gravitational
information that cannot be reduced to known structural relations.

Step 1: Basic SCH-relevant correlations (the ones we should have
        run before dismissing beta_z).
        rho(beta_z, log_excess) and rho(beta_z, rar_resid),
        full sample and by mass tertile, raw and partial
        controlling for log_Ms and log_Re_kpc.

Step 2: The beta_z floor question.
        Is beta_z = 0 a JAM model prior artefact or physical?
        Diagnose by checking whether floor galaxies (beta_z < 0.01)
        cluster in (lambda_r, sigma, mass) space or are uniform.

Step 3: Joint (lambda_r, beta_z) prediction of rar_resid.
        Is there an interaction -- does the combination predict
        excess gravity better than either alone?

Usage:
    python beta_z_analysis.py
"""

import numpy as np
import pandas as pd
from scipy.stats import spearmanr, rankdata
from astropy.io import fits
from astropy.table import Table

CSV        = "manga_merged_with_rar.csv"
JAM_FILE   = "data/SDSSDR17_MaNGA_JAM_v2.fits"
BETA_Z_FLOOR = 0.01


def load_jam_extras():
    """
    Load beta_z, kappa (HDU4) and Eps_MGE (HDU1) from JAM v2,
    aligned by row position, returned as a DataFrame with plateifu.
    """
    with fits.open(JAM_FILE) as hdul:
        def flat(hdu):
            tbl = Table(hdu.data)
            names = [n for n in tbl.colnames if len(tbl[n].shape) <= 1]
            return tbl[names].to_pandas()

        master = flat(hdul[1])   # plateifu, Eps_MGE, Lambda_Re
        cyl    = flat(hdul[4])   # beta_z, kappa

    master["plateifu"] = master["plateifu"].apply(
        lambda v: v.decode("utf-8").strip() if isinstance(v, bytes) else str(v).strip()
    )

    out = pd.DataFrame({
        "plateifu": master["plateifu"],
        "Eps_MGE":  master["Eps_MGE"],
        "beta_z":   cyl["beta_z"],
        "kappa":    cyl["kappa"],
    })
    return out


def add_tertiles(df, mass_col="log_Ms_Re_cyl"):
    df = df.copy()
    df["mass_tertile"] = pd.qcut(
        df[mass_col], 3, labels=["Low", "Mid", "High"]
    )
    return df


def partial_corr_spearman(x, y, controls):
    """
    Partial Spearman correlation of x and y, controlling for
    one or more variables in controls (list of arrays).
    Uses rank-based OLS residualization.
    """
    def resid(a, B):
        A = np.column_stack([B, np.ones(len(a))])
        coef, _, _, _ = np.linalg.lstsq(A, a, rcond=None)
        return a - A @ coef

    rx = rankdata(x)
    ry = rankdata(y)
    rcontrols = np.column_stack([rankdata(c) for c in controls])

    rx_resid = resid(rx, rcontrols)
    ry_resid = resid(ry, rcontrols)
    return spearmanr(rx_resid, ry_resid)


def report(label, rho, p, n):
    print(f"  {label:52s}  N={n:5d}   rho={rho:+.3f}   p={p:.2e}")


def main():
    # ----------------------------------------------------------------
    # Load and merge
    # ----------------------------------------------------------------
    df = pd.read_csv(CSV)
    jam_extras = load_jam_extras()

    df = df.merge(jam_extras, on="plateifu", how="left")

    print(f"Merged sample: N={len(df)}")
    print(f"beta_z NaN after merge: {df['beta_z'].isna().sum()}")
    print(f"Eps_MGE NaN after merge: {df['Eps_MGE'].isna().sum()}")

    with np.errstate(divide="ignore", invalid="ignore"):
        df["log_Re_kpc"] = np.log10(df["Re_kpc"])
        df["log_Ms"]     = df["log_Ms_Re_cyl"]
        df["log_sigma"]  = np.log10(df["STELLAR_SIGMA_1RE"])

    df = add_tertiles(df, "log_Ms_Re_cyl")

    # Emsellem et al. 2011 fast/slow boundary
    df["kin_class"] = np.where(
        df["Lambda_Re"] >= 0.31 * np.sqrt(df["Eps_MGE"].clip(lower=0)),
        "fast", "slow"
    )
    print(f"Fast: {(df['kin_class']=='fast').sum()}  "
          f"Slow: {(df['kin_class']=='slow').sum()}\n")

    # ----------------------------------------------------------------
    # STEP 1: SCH-relevant correlations for beta_z
    # ----------------------------------------------------------------
    print("=" * 70)
    print("STEP 1: rho(beta_z, log_excess) and rho(beta_z, rar_resid)")
    print("        raw, and partial controlling for log_Ms + log_Re_kpc")
    print("=" * 70)

    for outcome, label in [("log_excess", "log_excess (proxy)"),
                            ("rar_resid",  "rar_resid  (proper)")]:
        print(f"\n  --- Outcome: {label} ---")
        groups = (
            [("Full",  df)] +
            [(t, df[df["mass_tertile"] == t]) for t in ["Low","Mid","High"]] +
            [(c, df[df["kin_class"] == c]) for c in ["fast","slow"]]
        )
        for grp_label, sub in groups:
            sub = sub.dropna(
                subset=["beta_z", outcome, "log_Ms", "log_Re_kpc"]
            )
            if len(sub) < 20:
                continue
            rho_raw, p_raw = spearmanr(sub["beta_z"], sub[outcome])
            rho_part, p_part = partial_corr_spearman(
                sub["beta_z"].values,
                sub[outcome].values,
                [sub["log_Ms"].values, sub["log_Re_kpc"].values]
            )
            report(f"{grp_label:8s} raw  rho(beta_z, {outcome})",
                   rho_raw, p_raw, len(sub))
            report(f"{grp_label:8s} part rho(beta_z, {outcome}) | Ms,Re",
                   rho_part, p_part, len(sub))

    # ----------------------------------------------------------------
    # STEP 2: Is the beta_z floor a model artefact or physical?
    # ----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("STEP 2: The beta_z floor -- artefact or physical?")
    print(f"        Floor defined as beta_z < {BETA_Z_FLOOR}")
    print("=" * 70)

    df["at_floor"] = df["beta_z"] < BETA_Z_FLOOR

    floor_frac = df["at_floor"].mean()
    print(f"\n  Floor fraction (full sample): "
          f"{floor_frac:.3f} ({df['at_floor'].sum()} of {len(df)})")

    print("\n  Floor fraction by mass tertile:")
    for t in ["Low", "Mid", "High"]:
        sub = df[df["mass_tertile"] == t]
        print(f"    {t}: {sub['at_floor'].mean():.3f} "
              f"(N_floor={sub['at_floor'].sum()}, N={len(sub)})")

    print("\n  Floor fraction by kinematic class:")
    for c in ["fast", "slow"]:
        sub = df[df["kin_class"] == c]
        print(f"    {c}: {sub['at_floor'].mean():.3f} "
              f"(N_floor={sub['at_floor'].sum()}, N={len(sub)})")

    print("\n  Distribution of lambda_r, sigma, log_Ms "
          "for floor vs non-floor:")
    for var, lbl in [("Lambda_Re",         "Lambda_Re"),
                     ("STELLAR_SIGMA_1RE",  "sigma"),
                     ("log_Ms",             "log_Ms")]:
        floor_v    = df.loc[df["at_floor"],  var].dropna()
        nonfloor_v = df.loc[~df["at_floor"], var].dropna()
        valid = df[[var, "beta_z"]].dropna()
        rho, p = spearmanr(valid[var], valid["beta_z"])
        print(f"\n    {lbl}:")
        print(f"      floor     mean={floor_v.mean():.3f}  "
              f"median={floor_v.median():.3f}  std={floor_v.std():.3f}")
        print(f"      non-floor mean={nonfloor_v.mean():.3f}  "
              f"median={nonfloor_v.median():.3f}  std={nonfloor_v.std():.3f}")
        print(f"      rho(beta_z, {lbl}) = {rho:+.3f}  p={p:.2e}")

    print("\n  Floor fraction by lambda_r quintile (full sample):")
    df["lr_quintile"] = pd.qcut(
        df["Lambda_Re"], 5, labels=[f"Q{i+1}" for i in range(5)]
    )
    g = df.groupby("lr_quintile", observed=False)
    floor_by_q = g.agg(
        N=("beta_z", "size"),
        floor_frac=("at_floor", "mean"),
        beta_z_mean=("beta_z", "mean"),
        beta_z_median=("beta_z", "median"),
        lambda_r_mean=("Lambda_Re", "mean"),
        sigma_mean=("STELLAR_SIGMA_1RE", "mean"),
    )
    print(floor_by_q)

    # ----------------------------------------------------------------
    # STEP 3: Joint (lambda_r, beta_z) prediction of rar_resid
    # ----------------------------------------------------------------
    print("\n" + "=" * 70)
    print("STEP 3: Joint (lambda_r, beta_z) prediction of rar_resid")
    print("        Does the combination predict better than either alone?")
    print("=" * 70)

    groups = (
        [("Full",  df)] +
        [(t, df[df["mass_tertile"] == t]) for t in ["Low","Mid","High"]]
    )
    for grp_label, sub in groups:
        sub = sub.dropna(
            subset=["lambda_r","beta_z","rar_resid",
                    "log_Ms","log_Re_kpc"]
        ).copy()
        if len(sub) < 20:
            continue

        rho_lr,  p_lr  = spearmanr(sub["lambda_r"], sub["rar_resid"])
        rho_bz,  p_bz  = spearmanr(sub["beta_z"],   sub["rar_resid"])

        rho_lr_bz, p_lr_bz = partial_corr_spearman(
            sub["lambda_r"].values, sub["rar_resid"].values,
            [sub["beta_z"].values]
        )
        rho_bz_lr, p_bz_lr = partial_corr_spearman(
            sub["beta_z"].values, sub["rar_resid"].values,
            [sub["lambda_r"].values]
        )
        rho_lr_all, p_lr_all = partial_corr_spearman(
            sub["lambda_r"].values, sub["rar_resid"].values,
            [sub["beta_z"].values,
             sub["log_Ms"].values,
             sub["log_Re_kpc"].values]
        )
        rho_bz_all, p_bz_all = partial_corr_spearman(
            sub["beta_z"].values, sub["rar_resid"].values,
            [sub["lambda_r"].values,
             sub["log_Ms"].values,
             sub["log_Re_kpc"].values]
        )

        print(f"\n  --- {grp_label} (N={len(sub)}) ---")
        report("raw rho(lambda_r,  rar_resid)",     rho_lr,     p_lr,     len(sub))
        report("raw rho(beta_z,    rar_resid)",     rho_bz,     p_bz,     len(sub))
        report("partial rho(lambda_r | beta_z)",    rho_lr_bz,  p_lr_bz,  len(sub))
        report("partial rho(beta_z  | lambda_r)",   rho_bz_lr,  p_bz_lr,  len(sub))
        report("partial rho(lambda_r | bz+Ms+Re)",  rho_lr_all, p_lr_all, len(sub))
        report("partial rho(beta_z  | lr+Ms+Re)",   rho_bz_all, p_bz_all, len(sub))

    print("\n  --- By kinematic class (full sample) ---")
    for c in ["fast", "slow"]:
        sub = df[df["kin_class"] == c].dropna(
            subset=["lambda_r","beta_z","rar_resid",
                    "log_Ms","log_Re_kpc"]
        ).copy()
        if len(sub) < 20:
            continue
        rho_lr, p_lr = spearmanr(sub["lambda_r"], sub["rar_resid"])
        rho_bz, p_bz = spearmanr(sub["beta_z"],   sub["rar_resid"])
        rho_bz_all, p_bz_all = partial_corr_spearman(
            sub["beta_z"].values, sub["rar_resid"].values,
            [sub["lambda_r"].values,
             sub["log_Ms"].values,
             sub["log_Re_kpc"].values]
        )
        print(f"\n  {c} rotators (N={len(sub)}):")
        report("  raw rho(lambda_r,  rar_resid)",     rho_lr,    p_lr,    len(sub))
        report("  raw rho(beta_z,    rar_resid)",     rho_bz,    p_bz,    len(sub))
        report("  partial rho(beta_z | lr+Ms+Re)",    rho_bz_all,p_bz_all,len(sub))


if __name__ == "__main__":
    main()
