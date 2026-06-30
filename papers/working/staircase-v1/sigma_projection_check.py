"""
sigma_projection_check.py
=========================
Single targeted question:

  Does observed velocity dispersion (STELLAR_SIGMA_1RE) correlate
  with inclination in slow rotators?

If yes: g_obs is inclination-dependent in slow rotators, which
  propagates into the Firefly RAR residual even though the mass
  estimator is photometric. The inclination-RAR signal is a
  kinematic projection artifact, not a physical or SCH effect.

If no: the inclination-RAR correlation in slow rotators remains
  unexplained by any projection mechanism tested so far.
  Proceed to CMB dipole / sky position analysis.

Input:  manga_enriched.csv
Output: sigma_projection_output.txt
"""

import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

DATA_PATH = "manga_enriched.csv"
OUT_PATH  = "sigma_projection_output.txt"

def spearman(df, x, y, controls=None):
    cols = [x, y] + (controls or [])
    sub = df[cols].dropna()
    n = len(sub)
    if n < 20:
        return np.nan, np.nan, n
    if not controls:
        rho, p = stats.spearmanr(sub[x], sub[y])
        return rho, p, n
    def rank(v): return stats.rankdata(v).astype(float)
    rx, ry = rank(sub[x].values), rank(sub[y].values)
    C = np.column_stack([rank(sub[c].values) for c in controls])
    def resid(v):
        A = np.column_stack([np.ones(len(v)), C])
        coef, *_ = np.linalg.lstsq(A, v, rcond=None)
        return v - A @ coef
    rho, p = stats.spearmanr(resid(rx), resid(ry))
    return rho, p, n

def sig(p):
    if np.isnan(p): return "---"
    return "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"

def fmt(label, n, rho, p, width=42):
    if np.isnan(rho):
        return f"  {label:<{width}} {n:>5}  {'---':>7}  {'---':>12}  ---"
    return f"  {label:<{width}} {n:>5}  {rho:>+7.3f}  {p:>12.2e}  {sig(p)}"

# ── load ───────────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH, low_memory=False)
slow = df["kin_class"] == "slow"
fast = df["kin_class"] == "fast"

sigma_col = "STELLAR_SIGMA_1RE" if "STELLAR_SIGMA_1RE" in df.columns \
            else "Sigma_Re"
print(f"Loaded {len(df)} rows  |  sigma column: {sigma_col}")
print(f"Slow N={slow.sum()}  Fast N={fast.sum()}")
print(f"sigma valid (slow): {df.loc[slow, sigma_col].notna().sum()}")

lines = []
lines.append("=" * 72)
lines.append("SIGMA_E PROJECTION CHECK")
lines.append("=" * 72)
lines.append(f"""
Question: Does rho(inc_deg_cyl, {sigma_col}) differ between
fast and slow rotators?

Physical expectation:
  True sphere: sigma_e has no inclination dependence.
  Oblate slow rotator: sigma_e may vary with viewing angle
    if the system has residual anisotropy or flattening.

If rho(inc, sigma) is significant in slow rotators:
  -> g_obs is viewing-angle dependent
  -> Firefly RAR residual inherits inclination dependence
     through the kinematic channel, not the mass channel
  -> The inclination-RAR signal is a kinematic artifact

If rho(inc, sigma) is NOT significant in slow rotators:
  -> Projection of sigma_e is not the explanation
  -> Move to sky position / CMB dipole analysis
""")

# ── main test ──────────────────────────────────────────────────────────────
lines.append("=" * 72)
lines.append(f"rho(inc_deg_cyl, {sigma_col})")
lines.append("=" * 72)
lines.append(f"\n  {'Subsample':<42} {'N':>5}  {'rho':>7}  {'p':>12}  sig")
lines.append("  " + "-" * 70)

subsamples = {
    "Full":      pd.Series(True, index=df.index),
    "Fast":      fast,
    "Slow":      slow,
    "Low_slow":  (df["mass_tertile"] == "Low")  & slow,
    "Mid_slow":  (df["mass_tertile"] == "Mid")  & slow,
    "High_slow": (df["mass_tertile"] == "High") & slow,
    "Low_fast":  (df["mass_tertile"] == "Low")  & fast,
    "Mid_fast":  (df["mass_tertile"] == "Mid")  & fast,
    "High_fast": (df["mass_tertile"] == "High") & fast,
}

for name, mask in subsamples.items():
    sub = df[mask]
    rho, p, n = spearman(sub, "inc_deg_cyl", sigma_col)
    lines.append(fmt(name, n, rho, p))

# ── partial: controlling for mass ─────────────────────────────────────────
lines.append(f"\n  — Partial rho(inc, sigma) | log_Ms_Re_cyl —")
lines.append(f"  {'Subsample':<42} {'N':>5}  {'rho':>7}  {'p':>12}  sig")
lines.append("  " + "-" * 70)

for name, mask in subsamples.items():
    sub = df[mask]
    rho, p, n = spearman(sub, "inc_deg_cyl", sigma_col, ["log_Ms_Re_cyl"])
    lines.append(fmt(name, n, rho, p))

# ── chain: does sigma mediate inc -> rar_FF in slow rotators? ─────────────
lines.append(f"\n" + "=" * 72)
lines.append("MEDIATION TEST: does sigma_e carry inc -> rar_FF in slow rotators?")
lines.append("=" * 72)

sub_slow = df[slow]
r_is, p_is, n_is = spearman(sub_slow, "inc_deg_cyl", sigma_col)
r_sr, p_sr, n_sr = spearman(sub_slow, sigma_col, "rar_resid_firefly")
r_ir, p_ir, n_ir = spearman(sub_slow, "inc_deg_cyl", "rar_resid_firefly")
r_ctrl, p_ctrl, n_ctrl = spearman(sub_slow, "inc_deg_cyl",
                                   "rar_resid_firefly",
                                   ["log_Ms_Re_cyl", sigma_col])

lines.append(f"""
  Slow rotators (N={n_ir}):

  A: rho(inc, sigma_e)           = {r_is:>+7.3f}  p={p_is:.2e}  {sig(p_is)}
  B: rho(sigma_e, rar_FF)        = {r_sr:>+7.3f}  p={p_sr:.2e}  {sig(p_sr)}
  C: rho(inc, rar_FF)  raw       = {r_ir:>+7.3f}  p={p_ir:.2e}  {sig(p_ir)}
  D: rho(inc, rar_FF) |Ms,sigma  = {r_ctrl:>+7.3f}  p={p_ctrl:.2e}  {sig(p_ctrl)}

  Verdict:
    A significant + B significant + D collapses -> sigma mediates
    A not significant                           -> not this channel
    D remains large                             -> unexplained; go to sky position
""")

output = "\n".join(lines)
print(output)
with open(OUT_PATH, "w") as f:
    f.write(output)
print(f"Written to {OUT_PATH}")
