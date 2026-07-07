"""
joint_partial_audit.py
======================
Next-wall analysis for the SCH replication study.

Central question:
    Does beta_z carry independent information about rar_resid
    beyond what Sersic n, LW age, stellar mass, and Re already predict?

If the partial rho(beta_z, rar_resid | Ms_Re, Re, Sersic_n, LW_age) collapses,
the signal is the morphology/age axis in disguise.
If it holds, we have a genuinely independent dynamical variable.

Subsamples tested:
    - Full, Fast, Slow
    - Low / Mid / High mass tertile
    - Each mass tertile split by fast/slow

Additional attacks:
    - Add ellipticity to the control set
    - Check whether JAM inclination (inc_deg_cyl) mediates beta_z signal
    - Sersic n alone vs joint control (to see how much n absorbs)
    - Staircase table (quintile bins) for the surviving partials

Output:
    joint_partial_audit_output.txt
"""

import numpy as np
import pandas as pd
from scipy import stats
from itertools import combinations
import warnings
warnings.filterwarnings("ignore")

# ── paths ──────────────────────────────────────────────────────────────────
DATA_PATH = "manga_merged_with_rar.csv"
OUT_PATH  = "joint_partial_audit_output.txt"

# ── partial correlation (Spearman via residuals) ───────────────────────────
def partial_spearman(df, x_col, y_col, control_cols):
    """
    Spearman partial correlation of x and y controlling for controls.
    Uses the residual-on-ranks approach:
        rank(x) ~ controls  ->  rx
        rank(y) ~ controls  ->  ry
        rho(rx, ry)
    Returns (rho, pvalue, n).
    """
    cols = [x_col, y_col] + control_cols
    sub = df[cols].dropna()
    n = len(sub)
    if n < 30:
        return np.nan, np.nan, n

    rx = stats.rankdata(sub[x_col].values).astype(float)
    ry = stats.rankdata(sub[y_col].values).astype(float)
    controls = sub[control_cols].values.astype(float)

    # rank each control too for a fully nonparametric partial
    controls_r = np.column_stack([stats.rankdata(controls[:, i])
                                  for i in range(controls.shape[1])])

    def residualise(v, C):
        C_ = np.column_stack([np.ones(len(v)), C])
        coef, *_ = np.linalg.lstsq(C_, v, rcond=None)
        return v - C_ @ coef

    rx_res = residualise(rx, controls_r)
    ry_res = residualise(ry, controls_r)

    rho, pval = stats.spearmanr(rx_res, ry_res)
    return rho, pval, n


def raw_spearman(df, x_col, y_col):
    sub = df[[x_col, y_col]].dropna()
    rho, pval = stats.spearmanr(sub[x_col], sub[y_col])
    return rho, pval, len(sub)


# ── quintile staircase helper ──────────────────────────────────────────────
def quintile_staircase(df, bin_col, signal_col, control_cols=None, label=""):
    """
    Bin bin_col into 5 equal-count quintiles; report mean signal_col per bin.
    If control_cols supplied, signal is the partial-residual of signal_col
    on control_cols (so the staircase is confound-adjusted).
    """
    sub = df[[bin_col, signal_col] + (control_cols or [])].dropna()
    if len(sub) < 100:
        return None

    if control_cols:
        cols_r = pd.DataFrame(
            {c: stats.rankdata(sub[c]) for c in [signal_col] + control_cols}
        )
        C = np.column_stack([np.ones(len(sub))] +
                            [cols_r[c].values for c in control_cols])
        ry = cols_r[signal_col].values
        coef, *_ = np.linalg.lstsq(C, ry, rcond=None)
        sub = sub.copy()
        sub["_resid"] = ry - C @ coef
        signal_col_use = "_resid"
    else:
        signal_col_use = signal_col

    sub["_q"] = pd.qcut(sub[bin_col], 5,
                        labels=["Q1","Q2","Q3","Q4","Q5"])
    tbl = sub.groupby("_q", observed=True)[signal_col_use].agg(
        ["mean","sem","count"])
    tbl.columns = ["mean","sem","n"]

    # monotonicity check
    means = tbl["mean"].values
    diffs = np.diff(means)
    n_up = (diffs > 0).sum()
    mono = "MONOTONIC" if n_up == 4 else f"{n_up}/4 steps up"

    lines = [f"\n  Quintile staircase: {label}  [{mono}]"]
    lines.append(f"  {'Quintile':<8} {'N':>6} {'mean':>9} {'±2SE':>9}")
    for q, row in tbl.iterrows():
        lines.append(f"  {q:<8} {int(row['n']):>6} {row['mean']:>9.4f}"
                     f" {2*row['sem']:>9.4f}")
    return "\n".join(lines)


# ── main ───────────────────────────────────────────────────────────────────
def main():
    df = pd.read_csv(DATA_PATH, low_memory=False)
    print(f"Loaded {len(df)} rows")

    # ── variable availability check ────────────────────────────────────────
    needed = ["beta_z", "rar_resid", "rar_resid_firefly",
              "log_Ms_Re_cyl", "log_Re_kpc", "nsa_sersic_n",
              "LW_AGE_1Re", "Eps_MGE", "inc_deg_cyl",
              "kin_class", "mass_tertile"]
    missing = [c for c in needed if c not in df.columns]
    if missing:
        print(f"WARNING — missing columns: {missing}")

    lines = []
    lines.append("=" * 72)
    lines.append("JOINT PARTIAL AUDIT — SCH Replication Study")
    lines.append("=" * 72)
    lines.append(f"\nSample N = {len(df)}")
    for col in ["beta_z","rar_resid","rar_resid_firefly",
                "nsa_sersic_n","LW_AGE_1Re","Eps_MGE","inc_deg_cyl"]:
        if col in df.columns:
            n_valid = df[col].notna().sum()
            lines.append(f"  {col:<28} valid: {n_valid}")

    # ── define subsamples ──────────────────────────────────────────────────
    fast_mask = df["kin_class"] == "fast" if "kin_class" in df.columns else \
                df["Lambda_Re"] >= 0.31 if "Lambda_Re" in df.columns else \
                pd.Series(True, index=df.index)
    slow_mask = ~fast_mask

    mass_masks = {}
    if "mass_tertile" in df.columns:
        for t in ["Low", "Mid", "High"]:
            mass_masks[t] = df["mass_tertile"] == t
    elif "log_Ms_Re_cyl" in df.columns:
        terciles = df["log_Ms_Re_cyl"].quantile([1/3, 2/3])
        mass_masks["Low"]  = df["log_Ms_Re_cyl"] <  terciles.iloc[0]
        mass_masks["Mid"]  = (df["log_Ms_Re_cyl"] >= terciles.iloc[0]) & \
                             (df["log_Ms_Re_cyl"] <  terciles.iloc[1])
        mass_masks["High"] = df["log_Ms_Re_cyl"] >= terciles.iloc[1]

    subsamples = {"Full": pd.Series(True, index=df.index),
                  "Fast": fast_mask,
                  "Slow": slow_mask}
    for t, m in mass_masks.items():
        subsamples[t] = m
    # mass x kinematic cross-cuts
    for t, m in mass_masks.items():
        subsamples[f"{t}_fast"] = m & fast_mask
        subsamples[f"{t}_slow"] = m & slow_mask

    # ── control sets ──────────────────────────────────────────────────────
    base    = ["log_Ms_Re_cyl", "log_Re_kpc"]
    joint   = ["log_Ms_Re_cyl", "log_Re_kpc", "nsa_sersic_n", "LW_AGE_1Re"]
    maximal = ["log_Ms_Re_cyl", "log_Re_kpc", "nsa_sersic_n",
               "LW_AGE_1Re", "Eps_MGE"]

    # strip controls that aren't in df
    def avail(clist):
        return [c for c in clist if c in df.columns]

    # ── PART A: progressive control sets ──────────────────────────────────
    lines.append("\n" + "=" * 72)
    lines.append("PART A — PROGRESSIVE CONTROL SETS")
    lines.append("  Key question: does beta_z survive joint control for")
    lines.append("  Sersic n and LW age on top of Ms and Re?")
    lines.append("=" * 72)

    for resid_col, resid_label in [("rar_resid",         "JAM  "),
                                   ("rar_resid_firefly", "FF   ")]:
        if resid_col not in df.columns:
            continue
        lines.append(f"\n  Residual: {resid_label}")
        lines.append(f"  {'Subsample':<14} {'Controls':<36} "
                     f"{'N':>5} {'rho':>7} {'p':>12}")
        lines.append("  " + "-" * 72)

        for ss_name, ss_mask in subsamples.items():
            sub = df[ss_mask]
            for ctrl_label, ctrl in [
                ("raw",         []),
                ("|Ms,Re",      avail(base)),
                ("|Ms,Re,n,age",avail(joint)),
                ("|Ms,Re,n,age,eps", avail(maximal)),
            ]:
                if ctrl:
                    rho, pval, n = partial_spearman(
                        sub, "beta_z", resid_col, ctrl)
                else:
                    rho, pval, n = raw_spearman(sub, "beta_z", resid_col)
                if np.isnan(rho):
                    continue
                sig = ("***" if pval < 0.001 else
                       "**"  if pval < 0.01  else
                       "*"   if pval < 0.05  else "")
                lines.append(
                    f"  {ss_name:<14} {ctrl_label:<36} "
                    f"{n:>5} {rho:>+7.3f} {pval:>12.2e} {sig}")

    # ── PART B: incl mediation — does JAM inclination absorb beta_z? ──────
    lines.append("\n" + "=" * 72)
    lines.append("PART B — INCLINATION MEDIATION CHECK")
    lines.append("  If beta_z tracks inc_deg_cyl and inc_deg_cyl drives")
    lines.append("  rar_resid, the signal may be a JAM model artifact.")
    lines.append("=" * 72)

    if "inc_deg_cyl" in df.columns:
        lines.append(f"\n  {'Var pair':<45} {'N':>5} {'rho':>7} {'p':>12}")
        lines.append("  " + "-" * 60)

        for ss_name, ss_mask in [("Full", pd.Series(True, index=df.index)),
                                  ("Fast", fast_mask),
                                  ("Slow", slow_mask)]:
            sub = df[ss_mask]
            r1, p1, n1 = raw_spearman(sub, "beta_z", "inc_deg_cyl")
            r2, p2, n2 = raw_spearman(sub, "inc_deg_cyl", "rar_resid")
            r3, p3, n3 = partial_spearman(
                sub, "beta_z", "rar_resid",
                avail(joint + ["inc_deg_cyl"]))

            lines.append(f"\n  [{ss_name}]")
            lines.append(f"  {'rho(beta_z, inc_deg_cyl)':<45} "
                         f"{n1:>5} {r1:>+7.3f} {p1:>12.2e}")
            lines.append(f"  {'rho(inc_deg_cyl, rar_resid)':<45} "
                         f"{n2:>5} {r2:>+7.3f} {p2:>12.2e}")
            lines.append(f"  {'partial rho(beta_z,rar)|joint+inc':<45} "
                         f"{n3:>5} {r3:>+7.3f} {p3:>12.2e}")
    else:
        lines.append("\n  inc_deg_cyl not available — skipping")

    # ── PART C: quintile staircases ───────────────────────────────────────
    lines.append("\n" + "=" * 72)
    lines.append("PART C — QUINTILE STAIRCASES (confound-adjusted)")
    lines.append("  Staircase on partial residual of rar_resid on joint")
    lines.append("  control set. Monotonicity is the key diagnostic.")
    lines.append("=" * 72)

    ctrl_for_staircase = avail(joint)
    for ss_name, ss_mask in [("Full",  pd.Series(True, index=df.index)),
                              ("Fast",  fast_mask),
                              ("Slow",  slow_mask),
                              ("Mid",   mass_masks.get("Mid",
                               pd.Series(False, index=df.index)))]:
        sub = df[ss_mask]
        result = quintile_staircase(
            sub, "beta_z", "rar_resid",
            control_cols=ctrl_for_staircase,
            label=f"{ss_name} | controlled for {ctrl_for_staircase}")
        if result:
            lines.append(result)

    # ── PART D: Sersic n as sole control vs joint ─────────────────────────
    lines.append("\n" + "=" * 72)
    lines.append("PART D — HOW MUCH DOES SERSIC N ALONE ABSORB?")
    lines.append("  Compare |Ms,Re,n  vs  |Ms,Re,n,age to isolate")
    lines.append("  what age adds beyond morphology.")
    lines.append("=" * 72)

    if "nsa_sersic_n" in df.columns:
        lines.append(f"\n  {'Subsample':<10} {'Controls':<28} "
                     f"{'N':>5} {'rho(JAM)':>10} {'rho(FF)':>10}")
        lines.append("  " + "-" * 65)

        ctrl_n_only  = avail(["log_Ms_Re_cyl","log_Re_kpc","nsa_sersic_n"])
        ctrl_n_age   = avail(joint)

        for ss_name, ss_mask in [("Full", pd.Series(True, index=df.index)),
                                  ("Slow", slow_mask)]:
            sub = df[ss_mask]
            for ctrl_label, ctrl in [
                ("|Ms,Re,n",     ctrl_n_only),
                ("|Ms,Re,n,age", ctrl_n_age),
            ]:
                r_j, p_j, n_j = partial_spearman(
                    sub, "beta_z", "rar_resid", ctrl)
                r_f, p_f, n_f = partial_spearman(
                    sub, "beta_z", "rar_resid_firefly", ctrl) \
                    if "rar_resid_firefly" in df.columns \
                    else (np.nan, np.nan, 0)

                sig_j = ("***" if p_j < 0.001 else "**" if p_j < 0.01
                         else "*" if p_j < 0.05 else "")
                sig_f = ("***" if p_f < 0.001 else "**" if p_f < 0.01
                         else "*" if p_f < 0.05 else "") \
                        if not np.isnan(p_f) else ""

                lines.append(
                    f"  {ss_name:<10} {ctrl_label:<28} {n_j:>5} "
                    f"{r_j:>+7.3f}{sig_j:<3}  {r_f:>+7.3f}{sig_f:<3}")

    # ── write output ───────────────────────────────────────────────────────
    output = "\n".join(lines)
    print(output)
    with open(OUT_PATH, "w") as f:
        f.write(output)
    print(f"\nResults written to {OUT_PATH}")


if __name__ == "__main__":
    main()
