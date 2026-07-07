"""
inclination_dissection.py
=========================
Focused audit of the inclination-RAR residual relationship.

Step 1: rho(inc_deg_cyl, rar_resid_firefly)
         Full, fast/slow, mass tertiles, mass x kin cross-cuts.
         This is the cleanest test: Firefly mass is photometric,
         knows nothing about JAM inclination fitting.

Step 2: Side-by-side comparison
         rho(inc, rar_JAM) vs rho(inc, rar_FF)
         for all subsamples, especially slow rotators.
         If FF shows similar rho to JAM: problem is in the
           acceleration estimate or sample selection, not JAM mass.
         If FF shows much smaller rho: problem is JAM-mass-specific,
           likely deprojection artifact.

Step 3 (CMB dipole): NOT run here. Conditional on Step 1 result.

Input:  manga_enriched.csv  (from enrich_and_audit.py)
Output: inclination_dissection_output.txt
"""

import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings("ignore")

DATA_PATH = "manga_enriched.csv"
OUT_PATH  = "inclination_dissection_output.txt"

# ── helpers ────────────────────────────────────────────────────────────────
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
    s = sig(p)
    if np.isnan(rho):
        return f"  {label:<{width}} {n:>5}  {'---':>7}  {'---':>12}"
    return (f"  {label:<{width}} {n:>5}  {rho:>+7.3f}  {p:>12.2e}  {s}")

# ── load ───────────────────────────────────────────────────────────────────
df = pd.read_csv(DATA_PATH, low_memory=False)
print(f"Loaded {len(df)} rows from {DATA_PATH}")

# Verify key columns
for col in ["inc_deg_cyl","rar_resid","rar_resid_firefly",
            "kin_class","mass_tertile","log_Ms_Re_cyl"]:
    n = df[col].notna().sum() if col in df.columns else 0
    print(f"  {col:<28}: {n} valid")

# ── subsamples ─────────────────────────────────────────────────────────────
fast = df["kin_class"] == "fast"
slow = df["kin_class"] == "slow"

masks = {
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
lines.append("INCLINATION DISSECTION — SCH Replication Study")
lines.append("=" * 72)
lines.append(f"\nN = {len(df)}  |  Fast: {fast.sum()}  Slow: {slow.sum()}")
lines.append(f"inc_deg_cyl range: "
             f"{df['inc_deg_cyl'].min():.1f} – {df['inc_deg_cyl'].max():.1f} deg")

# ══════════════════════════════════════════════════════════════════════════
# STEP 1: rho(inc_deg_cyl, rar_resid_FIREFLY)
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("STEP 1: rho(inc_deg_cyl, rar_resid_FIREFLY)")
lines.append("  Firefly mass is photometric — independent of JAM inclination fit.")
lines.append("  A large rho here means the problem is in the acceleration")
lines.append("  estimate or sample geometry, NOT in the JAM mass deprojection.")
lines.append("=" * 72)
lines.append(f"\n  {'Subsample':<38} {'N':>5}  {'rho':>7}  {'p':>12}  sig")
lines.append("  " + "-" * 70)

for name, mask in masks.items():
    sub = df[mask]
    rho, p, n = raw_spearman(sub, "inc_deg_cyl", "rar_resid_firefly")
    lines.append(row(name, n, rho, p))

# Also: partial controlling for log_Ms_Re_cyl (mass-controlled)
lines.append(f"\n  — Partial rho(inc, rar_FF) | log_Ms_Re_cyl —")
lines.append(f"  {'Subsample':<38} {'N':>5}  {'rho':>7}  {'p':>12}  sig")
lines.append("  " + "-" * 70)
for name, mask in masks.items():
    sub = df[mask]
    rho, p, n = partial_spearman(
        sub, "inc_deg_cyl", "rar_resid_firefly", ["log_Ms_Re_cyl"])
    lines.append(row(name, n, rho, p))

# ══════════════════════════════════════════════════════════════════════════
# STEP 2: JAM vs FF side-by-side
# ══════════════════════════════════════════════════════════════════════════
lines.append("\n" + "=" * 72)
lines.append("STEP 2: rho(inc_deg_cyl, rar_JAM) vs rho(inc_deg_cyl, rar_FF)")
lines.append("  Side-by-side comparison across all subsamples.")
lines.append("  Key diagnostic:")
lines.append("    FF >> JAM  -> artifact is in JAM mass deprojection")
lines.append("    FF ~ JAM   -> artifact is in g_obs or sample geometry")
lines.append("    FF << JAM  -> unexpected; investigate further")
lines.append("=" * 72)
lines.append(f"\n  {'Subsample':<18} {'N':>5}  "
             f"{'rho_JAM':>8}  {'p_JAM':>10}  "
             f"{'rho_FF':>8}  {'p_FF':>10}  "
             f"{'delta':>7}  interpretation")
lines.append("  " + "-" * 90)

for name, mask in masks.items():
    sub = df[mask]
    rj, pj, nj = raw_spearman(sub, "inc_deg_cyl", "rar_resid")
    rf, pf, nf = raw_spearman(sub, "inc_deg_cyl", "rar_resid_firefly")

    if np.isnan(rj) or np.isnan(rf):
        lines.append(f"  {name:<18} {nj:>5}  {'---':>8}  {'---':>10}  "
                     f"{'---':>8}  {'---':>10}  {'---':>7}")
        continue

    delta = rf - rj
    # Interpretation
    if abs(rf) < 0.05 and abs(rj) > 0.1:
        interp = "JAM artifact (FF clean)"
    elif abs(rf) > 0.1 and abs(rj) > 0.1 and abs(delta) < 0.05:
        interp = "shared — geometry or g_obs"
    elif abs(rf) > 0.1 and abs(rj) > 0.1 and delta > 0.05:
        interp = "FF > JAM — check photom"
    elif abs(rf) < 0.05 and abs(rj) < 0.05:
        interp = "clean in both"
    else:
        interp = "mixed"

    sj = sig(pj)
    sf = sig(pf)
    lines.append(
        f"  {name:<18} {nj:>5}  "
        f"{rj:>+8.3f}{sj:<3}  {pj:>10.2e}  "
        f"{rf:>+8.3f}{sf:<3}  {pf:>10.2e}  "
        f"{delta:>+7.3f}  {interp}")

# ── additional: partial versions for slow rotators specifically ───────────
lines.append(f"\n  — Slow rotators: partial rho(inc, rar) | log_Ms_Re_cyl —")
lines.append(f"  {'Residual':<20} {'N':>5}  {'rho':>7}  {'p':>12}  sig")
lines.append("  " + "-" * 55)
sub_slow = df[slow]
for resid_col, label in [("rar_resid",         "JAM  residual"),
                          ("rar_resid_firefly", "FF   residual"),
                          ("rar_resid_nsa",     "NSA  residual"),
                          ("rar_resid_sph",     "SPH  residual")]:
    if resid_col not in df.columns:
        continue
    rho, p, n = partial_spearman(
        sub_slow, "inc_deg_cyl", resid_col, ["log_Ms_Re_cyl"])
    lines.append(row(label, n, rho, p, width=20))

# ── summary interpretation ─────────────────────────────────────────────────
lines.append("\n" + "=" * 72)
lines.append("INTERPRETATION GUIDE")
lines.append("=" * 72)
lines.append("""
  The 0.465 rho(inc, rar_JAM) in slow rotators raised three hypotheses:

  H1 — JAM deprojection artifact
       JAM fits inclination as free parameter for slow rotators.
       Inclination uncertainty -> mass uncertainty -> RAR residual.
       SIGNATURE: rho_FF << rho_JAM for slow rotators.

  H2 — Acceleration estimate artifact (viewing angle in g_obs)
       The dynamical g_obs itself depends on inclination via
       projected velocity dispersion or surface brightness.
       SIGNATURE: rho_FF ~ rho_JAM (both large).

  H3 — Genuine physical signal
       Face-on vs edge-on slow rotators genuinely differ in
       their dark matter content or geometric coupling.
       SIGNATURE: signal survives all mass and size controls,
       consistent sign across all residual estimators.

  Decision tree after seeing these results:
    If H1: the beta_z signal in slow rotators (JAM residual) is
            suspect. Focus on Firefly residual for main claim.
    If H2: need to revisit how g_obs is estimated for slow rotators.
            May need JAM sigma_e-based acceleration instead.
    If H3: genuinely interesting but needs physical explanation.
""")

output = "\n".join(lines)
print(output)
with open(OUT_PATH, "w") as f:
    f.write(output)
print(f"\nWritten to {OUT_PATH}")
