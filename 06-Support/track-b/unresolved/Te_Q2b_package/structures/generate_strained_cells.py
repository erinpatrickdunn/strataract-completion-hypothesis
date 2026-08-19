#!/usr/bin/env python3
"""
Generates strained trigonal-Te QE input files (SCF + bands) for the Q2b-3
deformation-potential calculation: D_Delta = d(E_H4 - E_H5)/d(eps_zz).

Loading condition: uniaxial STRESS along the trigonal (C3, z) axis.
Elastic boundary condition: eps_xx = eps_yy = -nu * eps_zz,
  nu = 0.6265, derived in this audit from Royer & Dieulesaint (1979)
  trigonal elastic constants via full compliance-matrix inversion
  (nu = -S13/S33, NOT the simplified -c13/(c11+c12) stiffness-ratio
  shortcut, which is only exact for isotropic media).

Structure: trigonal Te, space group P3_1 21 (No. 152), ibrav=4 (hexagonal
cell) is exactly equivalent here because the imposed strain is isotropic
in the (x,y) plane -- both in-plane hexagonal lattice vectors scale by
the same factor (1+eps_xx), preserving their 120-degree relationship,
so ibrav=4 with strain-adjusted celldm(1), celldm(3) is rigorous, not
an approximation.

a0 = 4.456 Ang, c0 = 5.927 Ang, u = 0.269 (Wyckoff 3a, P3_1 21 setting):
  Te1: (u, 0, 2/3)
  Te2: (0, u, 1/3)
  Te3: (-u, -u, 0)

H point (hexagonal BZ, crystal/reciprocal coordinates): (1/3, 1/3, 1/2).

Two internal-coordinate protocols are generated, per the audit's own
"do not silently mix clamped-ion and relaxed-ion deformation potentials"
requirement:
  - clamped: u fixed at 0.269 for all strains (primary/default)
  - relaxed: 'relax' calculation type, ions free to move along the
    strain-preserved symmetry directions (u is the only free internal
    coordinate for this Wyckoff position under this strain symmetry)
"""

import json
import os

A0, C0 = 4.456, 5.927          # Angstrom, LITERATURE-VERIFIED (see PROVENANCE)
U0 = 0.269                     # LITERATURE-VERIFIED (see PROVENANCE)
NU = 0.6265                    # DERIVED this audit (Royer & Dieulesaint 1979 -> full compliance inversion)
BOHR = 0.52917721067

PSEUDO = "Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF"

# Convergence pair: primary + a tighter set, both must be run to satisfy
# the spec's "converge the derivative, not just the total energy" requirement
CUTOFF_SETS = [
    {"tag": "cut1", "ecutwfc": 60, "ecutrho": 480, "kmesh": (6, 6, 4)},
    {"tag": "cut2", "ecutwfc": 80, "ecutrho": 640, "kmesh": (8, 8, 6)},
]

# Primary strain series (local derivative) + wider points for linearity check
STRAINS = [-0.0050, -0.0025, 0.0, 0.0025, 0.0050]

OUTDIR = os.path.join(os.path.dirname(__file__), "..", "inputs")
os.makedirs(OUTDIR, exist_ok=True)


def scf_input(eps_zz, cutset, relax=False):
    exx = -NU * eps_zz
    a = A0 * (1 + exx)
    c = C0 * (1 + eps_zz)
    celldm1 = a / BOHR
    ca = c / a
    calc = "relax" if relax else "scf"
    ions_block = ""
    if relax:
        ions_block = "&ions\n  ion_dynamics = 'bfgs'\n/\n"

    return f"""&control
  calculation = '{calc}'
  prefix = 'te_eps{eps_zz:+.5f}_{cutset['tag']}{'_relax' if relax else ''}'
  pseudo_dir = '../pseudopotentials/'
  outdir = './tmp'
  verbosity = 'high'
  tstress = .true.
  tprnfor = .true.
/
&system
  ibrav = 4
  celldm(1) = {celldm1:.8f}
  celldm(3) = {ca:.8f}
  nat = 3
  ntyp = 1
  ecutwfc = {cutset['ecutwfc']}
  ecutrho = {cutset['ecutrho']}
  noncolin = .true.
  lspinorb = .true.
  occupations = 'smearing'
  smearing = 'gaussian'
  degauss = 0.005
/
&electrons
  conv_thr = 1.0d-9
  mixing_beta = 0.3
/
{ions_block}ATOMIC_SPECIES
  Te  127.60  {PSEUDO}
ATOMIC_POSITIONS crystal
  Te   {U0:.4f}   0.0000   0.6667
  Te   0.0000   {U0:.4f}   0.3333
  Te  -{U0:.4f}  -{U0:.4f}   0.0000
K_POINTS automatic
  {cutset['kmesh'][0]} {cutset['kmesh'][1]} {cutset['kmesh'][2]} 0 0 0
"""


def bands_input(eps_zz, cutset):
    exx = -NU * eps_zz
    a = A0 * (1 + exx)
    c = C0 * (1 + eps_zz)
    celldm1 = a / BOHR
    ca = c / a
    return f"""&control
  calculation = 'bands'
  prefix = 'te_eps{eps_zz:+.5f}_{cutset['tag']}'
  pseudo_dir = '../pseudopotentials/'
  outdir = './tmp'
  verbosity = 'high'
/
&system
  ibrav = 4
  celldm(1) = {celldm1:.8f}
  celldm(3) = {ca:.8f}
  nat = 3
  ntyp = 1
  ecutwfc = {cutset['ecutwfc']}
  ecutrho = {cutset['ecutrho']}
  noncolin = .true.
  lspinorb = .true.
  occupations = 'smearing'
  smearing = 'gaussian'
  degauss = 0.005
  nbnd = 24
/
&electrons
  conv_thr = 1.0d-9
/
ATOMIC_SPECIES
  Te  127.60  {PSEUDO}
ATOMIC_POSITIONS crystal
  Te   {U0:.4f}   0.0000   0.6667
  Te   0.0000   {U0:.4f}   0.3333
  Te  -{U0:.4f}  -{U0:.4f}   0.0000
K_POINTS crystal_b
  5
  0.00000  0.00000  0.00000  20   ! Gamma
  0.33333  0.33333  0.00000  20   ! K
  0.33333  0.33333  0.50000   5   ! H  <-- state of interest
  0.00000  0.00000  0.50000  20   ! A
  0.00000  0.00000  0.00000   1   ! Gamma
"""


def main():
    manifest = []
    for cutset in CUTOFF_SETS:
        for eps in STRAINS:
            scf_name = f"scf_eps{eps:+.5f}_{cutset['tag']}.in"
            bands_name = f"bands_eps{eps:+.5f}_{cutset['tag']}.in"
            with open(os.path.join(OUTDIR, scf_name), "w") as f:
                f.write(scf_input(eps, cutset, relax=False))
            with open(os.path.join(OUTDIR, bands_name), "w") as f:
                f.write(bands_input(eps, cutset))
            manifest.append({"eps_zz": eps, "cutset": cutset["tag"],
                              "scf": scf_name, "bands": bands_name, "relax": False})
            # relaxed-ion companion, primary cutoff set only (cut1), to bound
            # the clamped-vs-relaxed difference without doubling the whole grid
            if cutset["tag"] == "cut1":
                relax_name = f"relax_eps{eps:+.5f}_{cutset['tag']}.in"
                with open(os.path.join(OUTDIR, relax_name), "w") as f:
                    f.write(scf_input(eps, cutset, relax=True))
                manifest.append({"eps_zz": eps, "cutset": cutset["tag"],
                                  "scf": relax_name, "bands": None, "relax": True})

    with open(os.path.join(OUTDIR, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Wrote {len(manifest)} input-file entries to {OUTDIR}")


if __name__ == "__main__":
    main()
