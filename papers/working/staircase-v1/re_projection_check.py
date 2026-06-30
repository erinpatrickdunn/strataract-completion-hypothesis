"""
re_projection_check.py
======================
Tests whether the inclination-RAR residual correlation in slow rotators
is driven by a projection effect on the effective radius estimate.

Hypothesis: face-on slow rotators appear more extended (larger Re),
which inflates g_bar denominator, deflates g_bar, and inflates RAR residual.

If rho(inc, Re) is negative in slow rotators (face-on = larger Re),
this is the mechanism behind the inclination-RAR correlation.

Input:  manga_enriched.csv
Output: re_projection_output.txt
"""

import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

DATA_PATH = "manga_enriched.csv"
OUT_PATH  = "re_projection_output.txt"

def raw_spearman(df, x, y):
    sub = df[[x, y]].dropna()
    if len(sub) < 20:
        return np.nan, np.nan, len(sub)
    rho, p = stats.spearmanr(sub[x], sub[y])
    return rho, p, len(sub)

def partial_spearman(df, x_col, y_col, control_cols):
    cols = [x_col, y_col] + control_cols
    sub = df[cols].dropna()
    n = len(sub)
    if n < 20:
        return np.nan, np.nan, n
    def rank(v): return stats.rankdata(v).astype(float)
    rx = rank(sub[x_col].values)
    ry = rank(sub[y_col].values)
    C  = np.column_stack([rank(sub[c].values) for c in control_cols])
    def resid(v, C_):
        A = np.column_stack([np.ones(len(v)), C_])
        coef, *_ = np.linalg.lstsq(A, v, rcond=None)
        return v - A @ coef
    rho, p = stats.spearmanr(resid(rx, C), resid(ry, C))
    return rho, p, n

def sig(p):
    if p is None or np.isnan(p): return ""
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"

def row(label, n, rho, p, width=38):
    if np.isnan(rho):
        return f"  {label:<{width}} {n:>5}  {'---':>7}  {'---':>12}  ---"
    return f"  {label:<{width}} {n:>5}  {rho:>+7.3f}  {p:>12.2e}  {sig(p)}"

# ── load ───────────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH, low_memory=False)
print(f"Loaded {len(df)} rows")

fast = df["kin_class"] == "fast"
slow = df["kin_class"] == "slow"

masks = {
    "Full":      pd.Series(True, index=df.index),
    "Fast":      fast,
    "Slow":      slow,
    "Low_fast":  (df["mass_tertile"] == "Low")  & fast,
    "Low_slow":  (df["mass_tertile"] == "Low")  & slow,
    "Mid_fast":  (df["mass_tertile"] == "Mid")  & fast,
    "Mid_slow":  (df["mass_tertile"] == "Mid")  & slow,
    "High_fast": (df["mass_tertile"] == "High") & fast,
    "High_slow": (df["mass_tertile"] == "High") & slow,
}

lines = []
lines.append("=" * 72)
lines.append("Re PROJECTION CHECK — SCH Replication Study")
lines.append("=" * 72)
lines.append("""
Hypothesis:
  Face-on slow rotators appear more extended (larger apparent Re).
  Larger Re -> smaller g_bar -> inflated RAR residual.
  This would make the inclination-RAR correlation a pure projection
  artifact with no physical content.

Expected signature if hypothesis is true:
  rho(inc_deg_cyl, Re_kpc)       NEGATIVE in slow rotators
  rho(inc_deg_cyl, Re_arcsec)    NEGATIVE in slow rotators
  (low inclination = face-on = larger apparent size)

  After controlling for Re, rho(inc, rar_resid_FF) should shrink
  substantially in slow rotators.
""")

# ══════════════════════════════════════════════════════════════════════════
# SECTION 1: rho(inc, Re) — does inclination predict apparent size?
# ══════════════════════════════════════════════════════════════════════════
lines.append("=" * 72)
lines.append("SECTION 1: rho(inc_deg_cyl, Re)")
lines.append("  Negative rho = face-on galaxies appear larger.")
lines.append("=" * 72)

for re_col in ["Re_kpc", "Re_arcsec_MGE", "log_Re_kpc"]:
    if re_col not in df.columns:
        continue
    lines.append(f"\n  Re measure: {re_col}")
    lines.append(f"  {'Subsample':<38} {'N':>5}  {'rho':>7}  {'p':>12}  sig")
    lines.append("  " + "-" * 68)
    for name, mask in masks.items():
        sub = df[mask]
        rho, p, n = raw_spearman(sub, "inc_deg_cyl", re_col)
        lines.append(row(name, n, rho, p))

# ══════════════════════════════════════════════════════════════════════════
# SECTION 2: does controlling for Re reduce rho(inc, rar_FF)?
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("SECTION 2: rho(inc, rar_FF) before and after controlling for Re")
lines.append("  If Re mediates the inclination effect, partial rho should")
lines.append("  drop substantially after adding Re to the control set.")
lines.append("=" * 72)

re_col = "Re_kpc" if "Re_kpc" in df.columns else "Re_arcsec_MGE"
lines.append(f"\n  Using Re measure: {re_col}")
lines.append(f"\n  {'Subsample':<18} {'N':>5}  "
             f"{'raw rho':>8}  {'p':>10}  "
             f"{'|Ms':>8}  {'p':>10}  "
             f"{'|Ms,Re':>8}  {'p':>10}  "
             f"drop?")
lines.append("  " + "-" * 95)

for name, mask in masks.items():
    sub = df[mask]
    r0, p0, n0 = raw_spearman(sub, "inc_deg_cyl", "rar_resid_firefly")
    r1, p1, n1 = partial_spearman(sub, "inc_deg_cyl", "rar_resid_firefly",
                                  ["log_Ms_Re_cyl"])
    r2, p2, n2 = partial_spearman(sub, "inc_deg_cyl", "rar_resid_firefly",
                                  ["log_Ms_Re_cyl", re_col])

    if np.isnan(r0):
        lines.append(f"  {name:<18} {n0:>5}  ---")
        continue

    # assess drop
    if not np.isnan(r2) and not np.isnan(r0) and abs(r0) > 0.05:
        pct_drop = (abs(r0) - abs(r2)) / abs(r0) * 100
        drop_str = f"{pct_drop:>+5.0f}% drop"
    else:
        drop_str = "---"

    s0, s1, s2 = sig(p0), sig(p1), sig(p2)
    lines.append(
        f"  {name:<18} {n0:>5}  "
        f"{r0:>+8.3f}{s0:<2}  {p0:>10.2e}  "
        f"{r1:>+8.3f}{s1:<2}  {p1:>10.2e}  "
        f"{r2:>+8.3f}{s2:<2}  {p2:>10.2e}  "
        f"{drop_str}")

# ══════════════════════════════════════════════════════════════════════════
# SECTION 3: the chain — does inc -> Re -> rar_FF hold?
# Check whether rho(Re, rar_FF) is itself significant in slow rotators
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("SECTION 3: rho(Re, rar_resid_FF) — is Re itself predictive?")
lines.append("  If Re drives the chain, Re should predict rar_FF")
lines.append("  independently of inclination.")
lines.append("=" * 72)

for re_col in ["Re_kpc", "Re_arcsec_MGE", "log_Re_kpc"]:
    if re_col not in df.columns:
        continue
    lines.append(f"\n  Re measure: {re_col}")
    lines.append(f"  {'Subsample':<38} {'N':>5}  {'rho':>7}  {'p':>12}  sig")
    lines.append("  " + "-" * 68)
    for name, mask in masks.items():
        sub = df[mask]
        rho, p, n = raw_spearman(sub, re_col, "rar_resid_firefly")
        lines.append(row(name, n, rho, p))

# ══════════════════════════════════════════════════════════════════════════
# SECTION 4: summary — what does the chain look like?
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("SECTION 4: CHAIN SUMMARY for slow rotators")
lines.append("=" * 72)

sub_slow = df[slow]
re_col = "Re_kpc" if "Re_kpc" in df.columns else "Re_arcsec_MGE"

r_ir, p_ir, n_ir = raw_spearman(sub_slow, "inc_deg_cyl", re_col)
r_rr, p_rr, n_rr = raw_spearman(sub_slow, re_col, "rar_resid_firefly")
r_ii, p_ii, n_ii = raw_spearman(sub_slow, "inc_deg_cyl", "rar_resid_firefly")
r_pi, p_pi, n_pi = partial_spearman(sub_slow, "inc_deg_cyl",
                                     "rar_resid_firefly",
                                     ["log_Ms_Re_cyl", re_col])

lines.append(f"""
  Slow rotators (N={n_ii}):

  Step A:  rho(inc, {re_col:<12})     = {r_ir:>+7.3f}  p={p_ir:.2e}  {sig(p_ir)}
  Step B:  rho({re_col:<12}, rar_FF)  = {r_rr:>+7.3f}  p={p_rr:.2e}  {sig(p_rr)}
  Step C:  rho(inc, rar_FF) raw       = {r_ii:>+7.3f}  p={p_ii:.2e}  {sig(p_ii)}
  Step D:  rho(inc, rar_FF)|Ms,Re     = {r_pi:>+7.3f}  p={p_pi:.2e}  {sig(p_pi)}

  If Steps A and B are both significant and Step D is near zero:
    -> Re fully mediates the inc-rar_FF relationship.
    -> The inclination effect is a size projection artifact.

  If Step D remains large after controlling for Re:
    -> Something else is driving the inclination-RAR correlation.
    -> Consider: dust attenuation, sigma_e projection, sky position.
""")

output = "\n".join(lines)
print(output)
with open(OUT_PATH, "w") as f:
    f.write(output)
print(f"\nWritten to {OUT_PATH}")
