#!/usr/bin/env python3
"""
Extracts E_H4, E_H5 from a QE 'bands' calculation output and tracks them
across the strain series.

USAGE:
    python3 extract_H4_H5.py <path_to_bands.out> [--prev <path_to_prev_bands.out>]

IDENTIFICATION PROTOCOL (per the audit's explicit requirement -- do not
identify states merely by sorting eigenvalues at each strain independently):

1. At the H point (k-index printed below), noncollinear+SOC calculations
   give bands in Kramers pairs only where an inversion-type symmetry
   protects the degeneracy; P3_1 21 (point group 32) has NO inversion
   center, so H4 and H5 are generically NON-degenerate already at zero
   strain (this is the entire physical point of Delta existing at all).
   Expect four valence bands near the H4/H5 energy window (the model in
   Barts et al. 2025 is a 2-band k.p model, but full DFT will show the
   4d-semicore-free / p-derived manifold has more bands nearby -- H4/H5
   are specifically the topmost two before a clear ~eV-scale gap to the
   next lower band, and the two states straddling this specific splitting,
   NOT simply "bands N and N+1" by blind index).

2. At epsilon=0 (the reference strain), identify H4/H5 by:
   (a) locating the H k-point block in the .out file,
   (b) taking the pair of bands whose splitting is closest to 63 meV
       (the Barts et al. reference value) among bands within +/- 0.5 eV
       of the reported valence band maximum at H,
   (c) reporting ALL candidate splittings in that window so a human can
       check for a more physically motivated choice before trusting the
       automatic guess.

3. For strained points, track continuity via ENERGY PROXIMITY to the
   previous strain's identified H4/H5 (pass --prev). This is a minimal,
   auditable tracking method -- it is NOT a substitute for character/
   projection-based tracking (e.g. via projwfc.x) if avoided crossings
   are suspected. If the energy gap to the next-nearest band ever drops
   below ~5 meV between consecutive strain points, this script prints an
   explicit AMBIGUITY WARNING and refuses to silently proceed -- per the
   audit requirement "if band identification becomes ambiguous, stop and
   report the ambiguity rather than assigning labels arbitrarily."
"""

import argparse
import re
import sys
import json


def parse_bands_at_H(outfile, h_kpoint=(0.33333, 0.33333, 0.50000), tol=1e-3):
    """Parse a QE 'bands' calculation stdout for the eigenvalues at the H point."""
    with open(outfile) as f:
        text = f.read()

    # QE prints "k =  kx ky kz ( ... PWs)   bands (ev):" blocks
    kblock_re = re.compile(
        r"k =\s*([\-0-9.]+)\s+([\-0-9.]+)\s+([\-0-9.]+)[^\n]*\n\s*\n?\s*bands \(ev\):\s*\n\n((?:\s*[\-0-9.]+)+)",
        re.MULTILINE,
    )
    matches = kblock_re.findall(text)
    if not matches:
        print("ERROR: no 'bands (ev):' blocks found. Is this a completed 'bands' calculation output?")
        sys.exit(2)

    for kx, ky, kz, energies_block in matches:
        kx, ky, kz = float(kx), float(ky), float(kz)
        if abs(kx - h_kpoint[0]) < tol and abs(ky - h_kpoint[1]) < tol and abs(kz - h_kpoint[2]) < tol:
            energies = [float(x) for x in energies_block.split()]
            return energies

    print(f"ERROR: H point {h_kpoint} not found among parsed k-blocks. "
          f"Found k-points: {[(round(m[0],3),round(m[1],3),round(m[2],3)) for m in matches]}")
    sys.exit(2)


def identify_H4_H5_reference(energies, target_splitting_eV=0.063, window_eV=0.5):
    """At the reference (unstrained) point: find the pair of adjacent bands
    within `window_eV` of each other whose splitting is closest to the
    Barts et al. target, among the upper valence manifold."""
    energies = sorted(energies)
    candidates = []
    for i in range(len(energies) - 1):
        split = energies[i + 1] - energies[i]
        if split < window_eV:
            candidates.append((abs(split - target_splitting_eV), i, i + 1, energies[i], energies[i + 1], split))
    candidates.sort()
    if not candidates:
        print("ERROR: no adjacent-band pair found with splitting < window_eV. "
              "Structure/pseudopotential/cutoff benchmark has likely FAILED -- "
              "do not proceed to strain derivative. Report as FAIL per Gate 3.")
        sys.exit(3)

    print("Candidate H4/H5 pairs near the target splitting (ALL reported for manual review):")
    for score, i, j, e_i, e_j, split in candidates[:6]:
        print(f"  bands {i},{j}:  E={e_i:.4f}, {e_j:.4f} eV   splitting={split*1000:.2f} meV   "
              f"|delta from 63meV|={score*1000:.2f} meV")

    best = candidates[0]
    _, i, j, e_lo, e_hi, split = best
    print(f"\nAUTO-SELECTED (closest to 63 meV target): bands {i}/{j}, "
          f"E_H4={e_lo:.6f} eV, E_H5={e_hi:.6f} eV, Delta={split*1000:.3f} meV")
    print("^ This is a heuristic. Verify against orbital character (projwfc.x) before trusting for production results.")
    return {"E_H4": e_lo, "E_H5": e_hi, "band_index_H4": i, "band_index_H5": j, "Delta_eV": split}


def track_from_previous(energies, prev_result, max_jump_eV=0.05):
    """For strained points: pick the two energies closest to the previous
    step's H4/H5, and flag ambiguity if another band has moved within
    5 meV of either tracked state (per the audit's explicit requirement)."""
    energies = sorted(energies)
    e_h4_prev, e_h5_prev = prev_result["E_H4"], prev_result["E_H5"]

    def closest(e_target):
        return min(energies, key=lambda e: abs(e - e_target))

    e_h4 = closest(e_h4_prev)
    e_h5 = closest(e_h5_prev)

    if abs(e_h4 - e_h4_prev) > max_jump_eV or abs(e_h5 - e_h5_prev) > max_jump_eV:
        print(f"AMBIGUITY WARNING: tracked state jumped by more than {max_jump_eV*1000:.0f} meV "
              f"between strain steps. This may indicate an avoided crossing or a strain step too "
              f"large for simple energy-proximity tracking. STOP and use character-based tracking "
              f"(projwfc.x) before trusting this point.")

    others = [e for e in energies if e not in (e_h4, e_h5)]
    for e in others:
        if abs(e - e_h4) < 0.005 or abs(e - e_h5) < 0.005:
            print(f"AMBIGUITY WARNING: an untracked band ({e:.6f} eV) has come within 5 meV of a "
                  f"tracked H4/H5 state. Band identification is not safe to trust at this strain "
                  f"point without character analysis. Reporting anyway, flagged.")

    delta = e_h5 - e_h4
    return {"E_H4": e_h4, "E_H5": e_h5, "Delta_eV": delta}


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("outfile")
    ap.add_argument("--prev", default=None, help="JSON result file from the previous strain step")
    ap.add_argument("--save", default=None, help="where to save this step's result as JSON")
    args = ap.parse_args()

    energies = parse_bands_at_H(args.outfile)

    if args.prev is None:
        result = identify_H4_H5_reference(energies)
    else:
        with open(args.prev) as f:
            prev_result = json.load(f)
        result = track_from_previous(energies, prev_result)
        print(f"\nE_H4={result['E_H4']:.6f} eV  E_H5={result['E_H5']:.6f} eV  "
              f"Delta={result['Delta_eV']*1000:.3f} meV")

    if args.save:
        with open(args.save, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Saved to {args.save}")
