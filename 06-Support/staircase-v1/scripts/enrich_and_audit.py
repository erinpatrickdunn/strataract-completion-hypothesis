"""
enrich_and_audit.py  (v2)
=========================
Fixed FITS loading strategy:
  - JAM:      HDU1 has plateifu, HDU2 has beta_z — join on row index
  - Firefly:  HDU1 has plateifu, HDU2 has LW_AGE_1Re — join on row index
  - DRP:      HDU1 has both; force float64 on sersic_n before merge
"""

import numpy as np
import pandas as pd
from scipy import stats
from astropy.io import fits
import warnings
warnings.filterwarnings("ignore")

CSV_PATH     = "manga_merged_with_rar.csv"
JAM_FITS     = "data/SDSSDR17_MaNGA_JAM_v2.fits"
FIREFLY_FITS = "data/manga-firefly-v3_1_1-mastar.fits"
DRP_FITS     = "data/drpall-v3_1_1.fits"
OUT_CSV      = "manga_enriched.csv"
OUT_TXT      = "joint_partial_audit_output.txt"

# ── stat helpers ───────────────────────────────────────────────────────────
def partial_spearman(df, x_col, y_col, control_cols):
    cols = [x_col, y_col] + control_cols
    sub = df[cols].dropna()
    n = len(sub)
    if n < 30:
        return np.nan, np.nan, n
    def rank(v): return stats.rankdata(v).astype(float)
    rx = rank(sub[x_col].values)
    ry = rank(sub[y_col].values)
    C  = np.column_stack([rank(sub[c].values) for c in control_cols])
    def resid(v, C_):
        A = np.column_stack([np.ones(len(v)), C_])
        coef, *_ = np.linalg.lstsq(A, v, rcond=None)
        return v - A @ coef
    rho, pval = stats.spearmanr(resid(rx, C), resid(ry, C))
    return rho, pval, n

def raw_spearman(df, x, y):
    sub = df[[x, y]].dropna()
    rho, p = stats.spearmanr(sub[x], sub[y])
    return rho, p, len(sub)

def sig_stars(p):
    if p is None or np.isnan(p): return ""
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else ""

def quintile_staircase(df, bin_col, signal_col, control_cols=None, label=""):
    cols = [bin_col, signal_col] + (control_cols or [])
    sub = df[cols].dropna().copy()
    if len(sub) < 100:
        return None
    if control_cols:
        def rank(v): return stats.rankdata(v).astype(float)
        ry = rank(sub[signal_col].values)
        C  = np.column_stack([np.ones(len(sub))] +
                             [rank(sub[c].values) for c in control_cols])
        coef, *_ = np.linalg.lstsq(C, ry, rcond=None)
        sub["_s"] = ry - C @ coef
    else:
        sub["_s"] = sub[signal_col]
    try:
        sub["_q"] = pd.qcut(sub[bin_col], 5,
                            labels=["Q1","Q2","Q3","Q4","Q5"],
                            duplicates="drop")
    except ValueError:
        return f"\n  Staircase: {label}  [SKIPPED — insufficient unique values in {bin_col}]"
    # re-check we still have 5 bins after drop
    n_bins = sub["_q"].nunique()
    if n_bins < 3:
        return f"\n  Staircase: {label}  [SKIPPED — only {n_bins} unique bins after dedup]"
    tbl = sub.groupby("_q", observed=True)["_s"].agg(["mean","sem","count"])
    means = tbl["mean"].values
    n_up = (np.diff(means) > 0).sum()
    mono = "MONOTONIC" if n_up == 4 else f"{n_up}/4 steps up"
    out = [f"\n  Staircase: {label}  [{mono}]",
           f"  {'Q':<4} {'N':>6} {'mean':>9} {'+-2SE':>9}"]
    for q, row in tbl.iterrows():
        out.append(f"  {q:<4} {int(row['count']):>6} {row['mean']:>9.4f} "
                   f"{2*row['sem']:>9.4f}")
    return "\n".join(out)

def avail(df, clist):
    return [c for c in clist if c in df.columns and df[c].notna().sum() > 50]

# ══════════════════════════════════════════════════════════════════════════
# STEP 1 — ENRICH
# ══════════════════════════════════════════════════════════════════════════
def enrich():
    print("=" * 60)
    print("STEP 1: Enriching CSV with missing FITS columns")
    print("=" * 60)

    base = pd.read_csv(CSV_PATH, low_memory=False)
    base["plateifu"] = base["plateifu"].astype(str).str.strip()
    print(f"Base CSV: {len(base)} rows, {len(base.columns)} columns")

    # ── JAM FITS ─────────────────────────────────────────────────────────
    # HDU1 has plateifu (38 cols), HDU2 has beta_z (11 cols, no plateifu).
    # The HDUs are paired by row index — same galaxy, different model outputs.
    # Strategy: load HDU1 plateifu + any cols we want, load HDU2 beta_z,
    # concatenate by position, then merge on plateifu.
    print("\n--- JAM FITS ---")
    with fits.open(JAM_FITS, memmap=True) as hdul:
        print(f"  Total HDUs: {len(hdul)}")

        # HDU1: plateifu key table
        hdu1 = hdul[1]
        h1_cols = [c.name for c in hdu1.columns]
        print(f"  HDU1 cols: {h1_cols}")

        # Find plateifu col name
        plate_col = next((c for c in h1_cols
                          if "plateifu" in c.lower()), None)
        if plate_col is None:
            print("  ERROR: no plateifu in HDU1"); return base

        df_key = pd.DataFrame({"plateifu":
                                hdu1.data[plate_col].astype(str)})
        df_key["plateifu"] = df_key["plateifu"].str.strip()
        n_key = len(df_key)
        print(f"  HDU1 plateifu: {n_key} rows")

        # Grab Eps_MGE from HDU1 if present
        for eps_cand in ["EPS_MGE","eps_mge","EPS"]:
            if eps_cand in [c.upper() for c in h1_cols]:
                real = next(c for c in h1_cols if c.upper()==eps_cand)
                df_key["Eps_MGE"] = hdu1.data[real].astype(float)
                print(f"  Eps_MGE found in HDU1 as '{real}'")
                break

        # HDU2: beta_z (cylindrical model results, no plateifu key)
        hdu2 = hdul[2]
        h2_cols = [c.name for c in hdu2.columns]
        print(f"  HDU2 cols: {h2_cols}")
        beta_col = next((c for c in h2_cols
                         if "beta_z" in c.lower()), None)
        if beta_col:
            n2 = len(hdu2.data)
            print(f"  HDU2 rows: {n2}  (HDU1 rows: {n_key})")
            if n2 == n_key:
                df_key["beta_z"] = hdu2.data[beta_col].astype(float)
                print(f"  beta_z loaded from HDU2 col '{beta_col}'")
            else:
                print(f"  WARNING: HDU1/HDU2 row count mismatch "
                      f"({n_key} vs {n2}) — cannot join by index")
                # Try HDU4 (next cylindrical model)
                for alt_hdu in [4, 6, 8, 10]:
                    if alt_hdu >= len(hdul): continue
                    h_alt = hdul[alt_hdu]
                    alt_cols = [c.name for c in h_alt.columns]
                    beta_alt = next((c for c in alt_cols
                                     if "beta_z" in c.lower()), None)
                    if beta_alt and len(h_alt.data) == n_key:
                        df_key["beta_z"] = h_alt.data[beta_alt].astype(float)
                        print(f"  beta_z loaded from HDU{alt_hdu}")
                        break
        else:
            print("  beta_z not in HDU2 col list")
            # scan remaining HDUs for beta_z at matching row count
            for alt_idx in range(2, len(hdul)):
                h_alt = hdul[alt_idx]
                if not hasattr(h_alt, 'columns'): continue
                alt_cols = [c.name for c in h_alt.columns]
                beta_alt = next((c for c in alt_cols
                                 if "beta_z" in c.lower()), None)
                if beta_alt and len(h_alt.data) == n_key:
                    df_key["beta_z"] = h_alt.data[beta_alt].astype(float)
                    print(f"  beta_z found in HDU{alt_idx} as '{beta_alt}'")
                    break

        df_key = df_key.drop_duplicates("plateifu")
        base = base.merge(df_key, on="plateifu", how="left")
        n_beta = base["beta_z"].notna().sum() if "beta_z" in base.columns else 0
        print(f"  beta_z matched: {n_beta}/{len(base)}")

    # ── FIREFLY FITS ──────────────────────────────────────────────────────
    # HDU1 (GALAXY_INFO) has plateifu, HDU2 (GLOBAL_PARAMETERS) has LW_AGE_1Re
    # Join by row index (same ordering guaranteed by MaNGA pipeline)
    print("\n--- FIREFLY FITS ---")
    with fits.open(FIREFLY_FITS, memmap=True) as hdul:
        hdu_names = [h.name for h in hdul]
        print(f"  HDUs: {hdu_names}")

        # Find plateifu HDU
        plate_hdu = None
        plate_col = None
        for idx, hdu in enumerate(hdul[1:], 1):
            if not hasattr(hdu, 'columns'): continue
            cols = [c.name for c in hdu.columns]
            pc = next((c for c in cols if "plateifu" in c.lower()), None)
            if pc:
                plate_hdu = idx
                plate_col = pc
                print(f"  plateifu in HDU{idx} ({hdu.name}) as '{pc}'")
                break

        # Find LW_AGE HDU
        age_hdu = None
        age_col = None
        for idx, hdu in enumerate(hdul[1:], 1):
            if not hasattr(hdu, 'columns'): continue
            cols = [c.name for c in hdu.columns]
            ac = next((c for c in cols
                        if c.upper() in ["LW_AGE_1RE","LW_AGE_RE"]), None)
            if ac:
                age_hdu = idx
                age_col = ac
                print(f"  LW_AGE_1Re in HDU{idx} ({hdu.name}) as '{ac}'")
                break
            # also check for generic age
            ac2 = next((c for c in cols if "age" in c.lower()), None)
            if ac2:
                print(f"  Age candidate in HDU{idx}: {ac2} "
                      f"(cols: {cols[:8]})")

        if plate_hdu is not None and age_hdu is not None:
            with fits.open(FIREFLY_FITS, memmap=True) as hdul2:
                n_plate = len(hdul2[plate_hdu].data)
                n_age   = len(hdul2[age_hdu].data)
                print(f"  plate HDU rows: {n_plate}, age HDU rows: {n_age}")

                df_plate = pd.DataFrame({
                    "plateifu": hdul2[plate_hdu].data[plate_col].astype(str)})
                df_plate["plateifu"] = df_plate["plateifu"].str.strip()

                age_vals = hdul2[age_hdu].data[age_col].astype(float)

                # Find LW_Z too
                z_col = None
                z_vals = None
                z_hdu_cols = [c.name for c in hdul2[age_hdu].columns]
                zc = next((c for c in z_hdu_cols
                            if c.upper() in ["LW_Z_1RE","LW_Z_RE"]), None)
                if zc:
                    z_col = zc
                    z_vals = hdul2[age_hdu].data[zc].astype(float)

                if n_plate == n_age:
                    df_plate["LW_AGE_1Re"] = age_vals
                    if z_vals is not None:
                        df_plate["LW_Z_1Re"] = z_vals
                    df_plate = df_plate.drop_duplicates("plateifu")
                    base = base.merge(df_plate, on="plateifu", how="left")
                    print(f"  LW_AGE_1Re matched: "
                          f"{base['LW_AGE_1Re'].notna().sum()}/{len(base)}")
                else:
                    # mismatched — try direct plateifu join on age HDU
                    pc2 = next((c.name for c in hdul2[age_hdu].columns
                                 if "plateifu" in c.name.lower()), None)
                    if pc2:
                        df_age = pd.DataFrame({
                            "plateifu": hdul2[age_hdu].data[pc2].astype(str),
                            "LW_AGE_1Re": age_vals})
                        if z_vals is not None:
                            df_age["LW_Z_1Re"] = z_vals
                        df_age["plateifu"] = df_age["plateifu"].str.strip()
                        df_age = df_age.drop_duplicates("plateifu")
                        base = base.merge(df_age, on="plateifu", how="left")
                        print(f"  LW_AGE_1Re matched (direct): "
                              f"{base['LW_AGE_1Re'].notna().sum()}/{len(base)}")
                    else:
                        print("  WARNING: row count mismatch and no plateifu "
                              "in age HDU — LW_AGE_1Re not loaded")
                        base["LW_AGE_1Re"] = np.nan
        else:
            print("  WARNING: could not locate both plateifu and LW_AGE_1Re")
            base["LW_AGE_1Re"] = np.nan

    # ── DRP FITS ─────────────────────────────────────────────────────────
    print("\n--- DRP FITS ---")
    with fits.open(DRP_FITS, memmap=True) as hdul:
        hdu = hdul[1]  # MANGA HDU has both plateifu and nsa_sersic_n
        h_cols = [c.name for c in hdu.columns]
        plate_col = next((c for c in h_cols
                          if "plateifu" in c.lower()), None)
        sersic_col = next((c for c in h_cols
                           if "sersic_n" in c.lower()), None)
        print(f"  plate_col='{plate_col}', sersic_col='{sersic_col}'")

        if plate_col and sersic_col:
            plateifus = hdu.data[plate_col].astype(str)
            # Force to Python float to avoid FITS byteorder issues
            sersic_vals = np.array(hdu.data[sersic_col],
                                   dtype=np.float64)
            df_drp = pd.DataFrame({
                "plateifu":    plateifus,
                "nsa_sersic_n": sersic_vals
            })
            df_drp["plateifu"] = df_drp["plateifu"].str.strip()
            df_drp = df_drp.drop_duplicates("plateifu")
            base = base.merge(df_drp, on="plateifu", how="left")
            print(f"  nsa_sersic_n matched: "
                  f"{base['nsa_sersic_n'].notna().sum()}/{len(base)}")
        else:
            print("  nsa_sersic_n or plateifu not found")
            base["nsa_sersic_n"] = np.nan

    # ── derived columns ───────────────────────────────────────────────────
    if "log_Re_kpc" not in base.columns and "Re_kpc" in base.columns:
        base["log_Re_kpc"] = np.log10(
            base["Re_kpc"].replace(0, np.nan))

    if "kin_class" not in base.columns and "Lambda_Re" in base.columns:
        base["kin_class"] = np.where(
            base["Lambda_Re"] >= 0.31, "fast", "slow")

    # ── summary ───────────────────────────────────────────────────────────
    print(f"\nEnriched: {len(base)} rows, {len(base.columns)} cols")
    for col in ["beta_z","LW_AGE_1Re","LW_Z_1Re","nsa_sersic_n",
                "Eps_MGE","log_Re_kpc","kin_class"]:
        n = base[col].notna().sum() if col in base.columns else "MISSING"
        print(f"  {col:<20}: {n}")

    base.to_csv(OUT_CSV, index=False)
    print(f"\nSaved enriched CSV -> {OUT_CSV}")
    return base


# ══════════════════════════════════════════════════════════════════════════
# STEP 2 — AUDIT
# ══════════════════════════════════════════════════════════════════════════
def audit(df):
    print("\n" + "=" * 60)
    print("STEP 2: Joint Partial Audit")
    print("=" * 60)

    lines = []
    lines.append("=" * 72)
    lines.append("JOINT PARTIAL AUDIT — SCH Replication Study")
    lines.append("=" * 72)
    lines.append(f"\nSample N = {len(df)}")
    for col in ["beta_z","rar_resid","rar_resid_firefly",
                "nsa_sersic_n","LW_AGE_1Re","Eps_MGE",
                "inc_deg_cyl","log_Re_kpc","kin_class"]:
        n = df[col].notna().sum() if col in df.columns else "MISSING"
        lines.append(f"  {col:<28} valid: {n}")

    base_ctrl    = avail(df, ["log_Ms_Re_cyl","log_Re_kpc"])
    joint_ctrl   = avail(df, ["log_Ms_Re_cyl","log_Re_kpc",
                               "nsa_sersic_n","LW_AGE_1Re"])
    maximal_ctrl = avail(df, ["log_Ms_Re_cyl","log_Re_kpc",
                               "nsa_sersic_n","LW_AGE_1Re","Eps_MGE"])
    lines.append(f"\n  base    controls: {base_ctrl}")
    lines.append(f"  joint   controls: {joint_ctrl}")
    lines.append(f"  maximal controls: {maximal_ctrl}")

    fast_mask = (df["kin_class"] == "fast") if "kin_class" in df.columns \
                else pd.Series(True, index=df.index)
    slow_mask = ~fast_mask

    mass_masks = {}
    if "mass_tertile" in df.columns:
        for t in ["Low","Mid","High"]:
            mass_masks[t] = df["mass_tertile"] == t

    subsamples = {"Full": pd.Series(True, index=df.index),
                  "Fast": fast_mask, "Slow": slow_mask}
    for t, m in mass_masks.items():
        subsamples[t] = m
        subsamples[f"{t}_fast"] = m & fast_mask
        subsamples[f"{t}_slow"] = m & slow_mask

    # ── PART A ────────────────────────────────────────────────────────────
    lines.append("\n" + "=" * 72)
    lines.append("PART A — PROGRESSIVE CONTROL SETS")
    lines.append("=" * 72)

    for resid_col, rlabel in [("rar_resid","JAM"),
                               ("rar_resid_firefly","FF")]:
        if resid_col not in df.columns: continue
        lines.append(f"\n  Residual: {rlabel}")
        lines.append(f"  {'Sample':<14} {'Controls':<34} "
                     f"{'N':>5} {'rho':>7} {'p':>12}")
        lines.append("  " + "-" * 72)
        for ss_name, ss_mask in subsamples.items():
            sub = df[ss_mask]
            for ctrl_label, ctrl in [
                ("raw",               []),
                ("|Ms,Re",            base_ctrl),
                ("|Ms,Re,n,age",      joint_ctrl),
                ("|Ms,Re,n,age,eps",  maximal_ctrl),
            ]:
                if not ctrl:
                    rho, p, n = raw_spearman(sub, "beta_z", resid_col)
                else:
                    rho, p, n = partial_spearman(
                        sub, "beta_z", resid_col, ctrl)
                if np.isnan(rho): continue
                lines.append(
                    f"  {ss_name:<14} {ctrl_label:<34} "
                    f"{n:>5} {rho:>+7.3f} {p:>12.2e} {sig_stars(p)}")

    # ── PART B — inclination ──────────────────────────────────────────────
    lines.append("\n" + "=" * 72)
    lines.append("PART B — INCLINATION MEDIATION")
    lines.append("=" * 72)
    if "inc_deg_cyl" in df.columns:
        inc_ctrl = avail(df, joint_ctrl + ["inc_deg_cyl"])
        lines.append(f"\n  {'Sample':<8} {'Pair':<44} "
                     f"{'N':>5} {'rho':>7} {'p':>12}")
        lines.append("  " + "-" * 70)
        for ss_name, ss_mask in [
            ("Full", pd.Series(True,index=df.index)),
            ("Fast", fast_mask), ("Slow", slow_mask)]:
            sub = df[ss_mask]
            r1,p1,n1 = raw_spearman(sub,"beta_z","inc_deg_cyl")
            r2,p2,n2 = raw_spearman(sub,"inc_deg_cyl","rar_resid")
            r3,p3,n3 = partial_spearman(
                sub,"beta_z","rar_resid", inc_ctrl)
            lines.append(f"\n  [{ss_name}]")
            lines.append(
                f"  {'':8} {'rho(beta_z, inc_deg_cyl)':<44} "
                f"{n1:>5} {r1:>+7.3f} {p1:>12.2e} {sig_stars(p1)}")
            lines.append(
                f"  {'':8} {'rho(inc_deg_cyl, rar_resid)':<44} "
                f"{n2:>5} {r2:>+7.3f} {p2:>12.2e} {sig_stars(p2)}")
            lines.append(
                f"  {'':8} {'partial rho(beta_z,rar)|joint+inc':<44} "
                f"{n3:>5} {r3:>+7.3f} {p3:>12.2e} {sig_stars(p3)}")

    # ── PART C — staircases ───────────────────────────────────────────────
    lines.append("\n" + "=" * 72)
    lines.append("PART C — QUINTILE STAIRCASES (confound-adjusted)")
    lines.append("=" * 72)
    for ss_name, ss_mask in [
        ("Full",  pd.Series(True,index=df.index)),
        ("Fast",  fast_mask),
        ("Slow",  slow_mask),
        ("Mid",   mass_masks.get("Mid",
                  pd.Series(False,index=df.index)))]:
        sub = df[ss_mask]
        r = quintile_staircase(sub,"beta_z","rar_resid",
                               joint_ctrl, f"{ss_name}")
        if r: lines.append(r)

    # ── PART D — Sersic n isolation ───────────────────────────────────────
    lines.append("\n" + "=" * 72)
    lines.append("PART D — SERSIC N ALONE vs JOINT CONTROL")
    lines.append("=" * 72)
    if "nsa_sersic_n" in df.columns and \
       df["nsa_sersic_n"].notna().sum() > 100:
        ctrl_n   = avail(df,["log_Ms_Re_cyl","log_Re_kpc","nsa_sersic_n"])
        ctrl_na  = joint_ctrl
        lines.append(f"\n  {'Sample':<8} {'Controls':<26} "
                     f"{'N':>5} {'rho_JAM':>9} {'rho_FF':>9}")
        lines.append("  " + "-" * 62)
        for ss_name, ss_mask in [
            ("Full", pd.Series(True,index=df.index)),
            ("Slow", slow_mask)]:
            sub = df[ss_mask]
            for ctrl_label, ctrl in [
                ("|Ms,Re,n",     ctrl_n),
                ("|Ms,Re,n,age", ctrl_na),
            ]:
                rj,pj,nj = partial_spearman(
                    sub,"beta_z","rar_resid",ctrl)
                rf,pf,nf = partial_spearman(
                    sub,"beta_z","rar_resid_firefly",ctrl) \
                    if "rar_resid_firefly" in df.columns \
                    else (np.nan,np.nan,0)
                lines.append(
                    f"  {ss_name:<8} {ctrl_label:<26} {nj:>5} "
                    f"{rj:>+7.3f}{sig_stars(pj):<3}  "
                    f"{rf:>+7.3f}{sig_stars(pf):<3}")
    else:
        lines.append("\n  nsa_sersic_n not available")

    out = "\n".join(lines)
    print(out)
    with open(OUT_TXT,"w") as f:
        f.write(out)
    print(f"\nResults written to {OUT_TXT}")


# ══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    df = enrich()
    n_beta = df["beta_z"].notna().sum() if "beta_z" in df.columns else 0
    if n_beta > 100:
        audit(df)
    else:
        print(f"\nERROR: beta_z has only {n_beta} valid values after enrichment.")
        print("The JAM FITS HDU structure is unusual — here is what we know:")
        print("  HDU1: plateifu present, beta_z absent")
        print("  HDU2: beta_z present, plateifu absent")
        print("  Row counts must match for index-join to work.")
        print("  Check the row counts printed above and report back.")
