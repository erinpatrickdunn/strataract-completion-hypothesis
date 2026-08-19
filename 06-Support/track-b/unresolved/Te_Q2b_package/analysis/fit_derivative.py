#!/usr/bin/env python3
"""
Fits Delta(eps_zz) = Delta_0 + D_Delta * eps_zz + C_Delta * eps_zz^2 + ...
from the collected per-strain results, and performs the convergence and
clamped-vs-relaxed cross-checks required by the audit.

INPUT: a CSV with columns eps_zz, cutset, relax, E_H4_eV, E_H5_eV
       (see ../results_template.csv for the exact expected format)

OUTPUT: D_Delta in meV per unit strain and meV per 1% strain, with an
        uncertainty estimated from the linear-fit residuals AND from the
        spread between the two independent cutoff sets (whichever is
        larger is reported -- do not understate uncertainty by only
        using the fit residual when the real systematic uncertainty is
        the cutoff-to-cutoff spread).
"""

import argparse
import csv
import numpy as np


def load(path):
    rows = []
    with open(path) as f:
        for r in csv.DictReader(f):
            rows.append({
                "eps_zz": float(r["eps_zz"]),
                "cutset": r["cutset"],
                "relax": r["relax"].strip().lower() in ("true", "1", "yes"),
                "E_H4_eV": float(r["E_H4_eV"]),
                "E_H5_eV": float(r["E_H5_eV"]),
            })
    return rows


def fit_D_Delta(rows, cutset, relax=False):
    subset = [r for r in rows if r["cutset"] == cutset and r["relax"] == relax]
    if len(subset) < 3:
        return None
    subset.sort(key=lambda r: r["eps_zz"])
    eps = np.array([r["eps_zz"] for r in subset])
    delta = np.array([r["E_H5_eV"] - r["E_H4_eV"] for r in subset])  # eV

    # Linear fit
    A = np.vstack([eps, np.ones_like(eps)]).T
    (slope, intercept), residuals, rank, sv = np.linalg.lstsq(A, delta, rcond=None)

    # Quadratic fit, to check whether linear regime is justified
    A2 = np.vstack([eps**2, eps, np.ones_like(eps)]).T
    coeffs2, res2, rank2, sv2 = np.linalg.lstsq(A2, delta, rcond=None)
    quad_coeff = coeffs2[0]

    # Central finite difference at the smallest available |eps| pair, as an
    # independent cross-check of the polynomial fit
    fd = None
    zero_idx = np.argmin(np.abs(eps))
    if len(eps) >= 3 and abs(eps[zero_idx]) < 1e-8:
        # use the smallest nonzero +/- pair
        pos = eps[eps > 0]
        neg = eps[eps < 0]
        if len(pos) and len(neg):
            e_p = pos.min()
            e_n = neg.max()
            d_p = delta[np.where(eps == e_p)[0][0]]
            d_n = delta[np.where(eps == e_n)[0][0]]
            fd = (d_p - d_n) / (e_p - e_n)

    fit_residual_std = np.std(delta - (slope * eps + intercept)) if len(eps) > 2 else float("nan")

    return {
        "cutset": cutset, "relax": relax,
        "D_Delta_eV_per_strain": slope,
        "D_Delta_meV_per_percent": slope * 1000 * 0.01,
        "Delta_0_fit_eV": intercept,
        "Delta_0_fit_meV": intercept * 1000,
        "quadratic_coeff_eV": quad_coeff,
        "finite_diff_check_eV_per_strain": fd,
        "fit_residual_std_eV": fit_residual_std,
        "n_points": len(subset),
        "raw_points": list(zip(eps.tolist(), delta.tolist())),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_path")
    args = ap.parse_args()

    rows = load(args.csv_path)
    cutsets = sorted(set(r["cutset"] for r in rows))

    results = []
    for cs in cutsets:
        r = fit_D_Delta(rows, cs, relax=False)
        if r:
            results.append(r)
    r_relax = fit_D_Delta(rows, cutsets[0], relax=True) if any(r["relax"] for r in rows) else None

    print("=" * 70)
    print("D_Delta results by cutoff set (clamped ions):")
    for r in results:
        print(f"\n  [{r['cutset']}]  n={r['n_points']} points")
        print(f"    D_Delta = {r['D_Delta_eV_per_strain']*1000:.3f} meV/unit strain "
              f"= {r['D_Delta_meV_per_percent']:.4f} meV/%")
        print(f"    Delta_0 (fit intercept) = {r['Delta_0_fit_meV']:.3f} meV")
        print(f"    quadratic coefficient = {r['quadratic_coeff_eV']*1000:.4f} meV "
              f"(should be << linear term if strain range is in the linear regime)")
        if r["finite_diff_check_eV_per_strain"] is not None:
            print(f"    central-finite-difference cross-check = "
                  f"{r['finite_diff_check_eV_per_strain']*1000:.3f} meV/unit strain")
        print(f"    fit residual std = {r['fit_residual_std_eV']*1000:.4f} meV")

    if len(results) == 2:
        spread = abs(results[0]["D_Delta_eV_per_strain"] - results[1]["D_Delta_eV_per_strain"])
        print(f"\n  CONVERGENCE CHECK (cutset-to-cutset spread): {spread*1000:.4f} meV/unit strain")
        print(f"  -> report this as the uncertainty on D_Delta if it exceeds the fit residual.")

    if r_relax:
        primary = next((r for r in results if r["cutset"] == cutsets[0]), None)
        if primary:
            diff = abs(primary["D_Delta_eV_per_strain"] - r_relax["D_Delta_eV_per_strain"])
            print(f"\n  CLAMPED vs RELAXED ION comparison ({cutsets[0]}):")
            print(f"    clamped D_Delta = {primary['D_Delta_eV_per_strain']*1000:.3f} meV/unit strain")
            print(f"    relaxed D_Delta = {r_relax['D_Delta_eV_per_strain']*1000:.3f} meV/unit strain")
            print(f"    difference      = {diff*1000:.3f} meV/unit strain")
            print(f"    -> report BOTH per the audit's explicit instruction not to silently mix protocols.")

    print("=" * 70)
    print("\nFINAL REPORTING RULE: take D_Delta from the tightest converged cutoff set.")
    print("Uncertainty = max(fit_residual_std, cutset-to-cutset spread).")
    print("If |D_Delta| < 2*uncertainty: classify as Outcome A (zero/numerically consistent with zero).")
    print("If |D_Delta| >= 2*uncertainty: classify as Outcome B (nonzero) and proceed to Q2b next gate.")


if __name__ == "__main__":
    main()
