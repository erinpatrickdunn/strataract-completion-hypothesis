"""
sigma_classification.py
=======================
Targeted three-way table to classify sigma_e's role relative to
the beta_z / Firefly RAR residual relationship.

Three quantities reported for all subsamples:
  1. rho(beta_z, sigma_e)                     -- shared variance check
  2. partial rho(beta_z, rar_FF) | Ms,Re,n,age        -- without sigma_e
  3. partial rho(beta_z, rar_FF) | Ms,Re,n,age,sigma  -- with sigma_e

Classification logic:
  rho(beta_z, sigma_e) small AND (2) ~ (3):
    -> sigma_e orthogonal to beta_z signal; independence supported;
       "leave Firefly untouched" position is defensible

  rho(beta_z, sigma_e) large AND (3) << (2):
    -> sigma_e and beta_z share substantial variance;
       could be confounder OR mediator; cannot distinguish from
       correlations alone; both specifications must be reported

  rho(beta_z, sigma_e) large AND (3) ~ (2):
    -> sigma_e carries separate information; beta_z signal is
       robust to sigma_e inclusion; strongest possible result

Input:  manga_enriched.csv
Output: sigma_classification_output.txt
"""

import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

DATA_PATH = "manga_enriched.csv"
OUT_PATH  = "sigma_classification_output.txt"

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

def classify(rho_bz_sig, rho_without, rho_with):
    """Plain-English classification of sigma_e's role."""
    if np.isnan(rho_bz_sig) or np.isnan(rho_without) or np.isnan(rho_with):
        return "insufficient data"
    shared = abs(rho_bz_sig)
    drop = (abs(rho_without) - abs(rho_with))
    pct  = drop / abs(rho_without) * 100 if abs(rho_without) > 0.01 else 0

    if shared < 0.10 and abs(pct) < 20:
        return "orthogonal — independence supported"
    elif shared >= 0.10 and pct > 30:
        return "shared variance — confounder or mediator (report both)"
    elif shared >= 0.10 and abs(pct) < 20:
        return "shared variance — beta_z robust to sigma inclusion"
    else:
        return f"mixed — pct drop={pct:.0f}%"

# ── load ───────────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH, low_memory=False)
fast = df["kin_class"] == "fast"
slow = df["kin_class"] == "slow"

sigma_col = "STELLAR_SIGMA_1RE" if "STELLAR_SIGMA_1RE" in df.columns \
            else "Sigma_Re"
print(f"Loaded {len(df)} rows  |  sigma: {sigma_col}")

# control sets
ctrl_joint = [c for c in ["log_Ms_Re_cyl","log_Re_kpc",
                           "nsa_sersic_n","LW_AGE_1Re"]
              if c in df.columns and df[c].notna().sum() > 50]
ctrl_sigma = ctrl_joint + [sigma_col]
print(f"Joint controls:        {ctrl_joint}")
print(f"Joint + sigma controls:{ctrl_sigma}")

subsamples = {
    "Full":      pd.Series(True, index=df.index),
    "Fast":      fast,
    "Slow":      slow,
    "Low":       df["mass_tertile"] == "Low",
    "Mid":       df["mass_tertile"] == "Mid",
    "High":      df["mass_tertile"] == "High",
    "Low_fast":  (df["mass_tertile"] == "Low")  & fast,
    "Low_slow":  (df["mass_tertile"] == "Low")  & slow,
    "Mid_fast":  (df["mass_tertile"] == "Mid")  & fast,
    "Mid_slow":  (df["mass_tertile"] == "Mid")  & slow,
    "High_fast": (df["mass_tertile"] == "High") & fast,
    "High_slow": (df["mass_tertile"] == "High") & slow,
}

lines = []
lines.append("=" * 72)
lines.append("SIGMA_E CLASSIFICATION — SCH Replication Study")
lines.append("=" * 72)
lines.append(f"\nSigma column: {sigma_col}")
lines.append(f"Joint controls: {ctrl_joint}")

# ══════════════════════════════════════════════════════════════════════════
# PART 1: rho(beta_z, sigma_e) — how much do they share?
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("PART 1: rho(beta_z, sigma_e)")
lines.append("  How much variance do beta_z and sigma_e share?")
lines.append("  Small rho -> orthogonal; large rho -> shared latent driver")
lines.append("=" * 72)
lines.append(f"\n  {'Subsample':<18} {'N':>5}  {'raw rho':>8}  {'p':>12}  "
             f"{'|Ms,Re,n,age':>8}  {'p':>12}  sig")
lines.append("  " + "-" * 78)

for name, mask in subsamples.items():
    sub = df[mask]
    r0, p0, n0 = spearman(sub, "beta_z", sigma_col)
    r1, p1, n1 = spearman(sub, "beta_z", sigma_col, ctrl_joint)
    lines.append(
        f"  {name:<18} {n0:>5}  {r0:>+8.3f}  {p0:>12.2e}  "
        f"{r1:>+8.3f}  {p1:>12.2e}  {sig(p1)}")

# ══════════════════════════════════════════════════════════════════════════
# PART 2: three-way table
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("PART 2: THREE-WAY TABLE")
lines.append("  Col A: rho(beta_z, sigma_e)  [shared variance]")
lines.append("  Col B: partial rho(beta_z, rar_FF) | joint controls")
lines.append("  Col C: partial rho(beta_z, rar_FF) | joint + sigma_e")
lines.append("  Drop%: (|B| - |C|) / |B| * 100")
lines.append("=" * 72)
lines.append(
    f"\n  {'Subsample':<14} {'N':>5}  "
    f"{'A: rho_bz_sig':>14}  "
    f"{'B: |joint':>10}  {'p_B':>10}  "
    f"{'C: |joint+sig':>13}  {'p_C':>10}  "
    f"{'Drop%':>6}  Classification")
lines.append("  " + "-" * 110)

results = {}
for name, mask in subsamples.items():
    sub = df[mask]
    ra, pa, na = spearman(sub, "beta_z", sigma_col)
    rb, pb, nb = spearman(sub, "beta_z", "rar_resid_firefly", ctrl_joint)
    rc, pc, nc = spearman(sub, "beta_z", "rar_resid_firefly", ctrl_sigma)

    if np.isnan(rb) or abs(rb) < 0.001:
        drop_pct = np.nan
        drop_str = "  ---"
    else:
        drop_pct = (abs(rb) - abs(rc)) / abs(rb) * 100
        drop_str = f"{drop_pct:>+5.0f}%"

    label = classify(ra, rb, rc)
    results[name] = (ra, rb, rc, drop_pct, label, na)

    sa, sb, sc = sig(pa), sig(pb), sig(pc)
    lines.append(
        f"  {name:<14} {na:>5}  "
        f"{ra:>+12.3f}{sa:<2}  "
        f"{rb:>+8.3f}{sb:<2}  {pb:>10.2e}  "
        f"{rc:>+11.3f}{sc:<2}  {pc:>10.2e}  "
        f"{drop_str}  {label}")

# ══════════════════════════════════════════════════════════════════════════
# PART 3: narrative summary
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("PART 3: NARRATIVE SUMMARY")
lines.append("=" * 72)
lines.append("""
  The classification of sigma_e's role determines the reporting strategy:

  SCENARIO A — orthogonal across all subsamples:
    sigma_e carries no shared variance with beta_z.
    The Firefly beta_z result stands as-is.
    Sigma_e documented as separate finding (inclination artifact).
    Report: primary result = Col B. Sigma robustness check = footnote.

  SCENARIO B — shared variance, signal drops substantially with sigma:
    Beta_z and sigma_e are measuring overlapping dynamical information.
    Cannot determine confounder vs mediator from correlations alone.
    Both specifications must be reported.
    Report: Col B and Col C side by side. Interpret difference honestly.

  SCENARIO C — shared variance, signal survives sigma inclusion:
    Beta_z carries information beyond sigma_e.
    Strongest possible result — robust to the hardest control.
    Report: Col C as primary. Col B as comparison.
    Clearly state: beta_z signal is not a sigma_e proxy.
""")

# print which scenario applies to key subsamples
lines.append("  Key subsample verdicts:")
for name in ["Full","Fast","Slow","Mid","Mid_fast","Mid_slow"]:
    if name in results:
        ra, rb, rc, dp, label, n = results[name]
        lines.append(f"    {name:<12}: {label}")

output = "\n".join(lines)
print(output)
with open(OUT_PATH, "w") as f:
    f.write(output)
print(f"\nWritten to {OUT_PATH}")
