# MANIFEST — Te D_Δ Replication Package

Independent DFT replication of \(D_\Delta=\partial(E_{H4}-E_{H5})/\partial\varepsilon_{zz}\) in trigonal Tellurium (\(P3_1 21\)).
All inputs/outputs are **executed** Quantum ESPRESSO v7.5 results. The full analysis and provenance tags are in `report/Te_DDelta_final_report.md`.

## Contents

```
report/                 Te_DDelta_final_report.md   — provenance-tagged final report
scripts/                extract_results.py          — H4/H5 extraction + finite differences (reproduces all tables)
                        gen_clamped.py              — generates clamped-strain scf/bands inputs
                        gen_trans_pois.py           — generates transverse + Poisson-strain inputs
structure/              Te_COD_2020222.cif          — COD primary structure (Adenis, Acta Cryst. C 45, 941 (1989))
pseudopotential/        Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF  — USPP, PBE, fully-relativistic (QE library)
smoke/                  te_smoke.{in,out}           — environment smoke test (UPF read + SCF)
runs/zero_strain/       zero_clean_{scf,bands}.{in,out}  — definitive zero-strain (7-pt k-list, Δ0=141 meV)
                        strain0_14pt_{scf,bands}.{in,out} — original 14-pt zero-strain calc
runs/clamped/           {m,p}{0025,0050}_{scf,bands}.{in,out}  — clamped path (ε_⊥=0), 4 strains
runs/transverse/        {m,p}{0025,0050}_{scf,bands}.{in,out}  — transverse path (ε_zz=0), 4 strains
runs/poisson/           {m,p}{0025,0050}_{scf,bands}.{in,out}  — Poisson path (ε_⊥=-ν·ε_zz, ν=0.6265), 4 strains
runs/convergence/       {scf,bands}_conv.{in,out}   — 8×8×8 / wfc70/rho560 convergence check
runs/projwfc/           projwfc{,_min,_sel}.{in,out} — orbital-character attempt (array-selection failed in QE 7.5)
```

Filename tags: `m` = compressive (negative ε), `p` = tensile (positive ε), 4-digit = strain×10⁴ (e.g. `p0050` = +0.005).

## Key results (reproduce via `python3 scripts/extract_results.py` from the `runs/` parent)

| Quantity | Value |
|---|---|
| Δ0 (zero strain) | 141 meV |
| D_Δ clamped (D_z) | 0.35 ± 0.01 eV |
| D_⊥ (transverse) | −0.36 eV |
| ν (Poisson) | 0.6265 |
| D_Δ Poisson | 0.57 ± 0.02 eV (direct 0.570 + decomp 0.576) |

## QE settings (all runs)
PBE+SOC, noncolin+lspinorb, ecutwfc=50 Ry, ecutrho=300 Ry, 6×6×6 k-mesh (SCF), 7-pt K–H–A k-list (bands at H), Gaussian smearing degauss=0.01 Ry, Davidson, conv_thr=1e-8. **Ions clamped** (fractional coords fixed) in all strain paths; only the cell path varies.

## Reproduce
```
conda create -n qe -c conda-forge qe=7.5
conda activate qe
export OMP_NUM_THREADS=1
# regenerate inputs:
python3 scripts/gen_clamped.py      ; python3 scripts/gen_trans_pois.py
# run each: mpirun -np 2 pw.x -in <dir>/scf.in > <dir>/scf.out ; ... bands.in > bands.out
# extract:
python3 scripts/extract_results.py
```
Note: `extract_results.py` reads `strain_*/bands.out` paths relative to a `qe_runs/` layout; adjust paths to match this package's `runs/<category>/<tag>_bands.out` if re-running standalone.

## Gap-closure files (see report §7)
- `runs/convergence/strain_hc2_clamp_{m0050,p0050}/` and `runs/convergence/strain_hc2b_pois_{m0050,p0050}/`: derivative cutoff-convergence checks — **6×6×6 k-mesh, ecutwfc=70 Ry, ecutrho=560 Ry** (higher than the production 50/300), clamped and Poisson ±0.005 endpoints in fresh dirs. Reproduce D_Δ(clamped)=0.350 eV and D_Δ(Poisson)=0.570 eV to 0.1 meV.
- `runs/projwfc/strain_H_single/{scf,projwfc}.{in,out}`: single-H-kpoint SCF + projwfc (`lsym=.true.`) for H4/H5 orbital character / irrep analysis. Shows the H4/H5/H6 manifold shares dominant Te p₃/₂ m_j=±3/2 character; the C₂z-screw-irrep sign is not resolvable from orbital projection.
