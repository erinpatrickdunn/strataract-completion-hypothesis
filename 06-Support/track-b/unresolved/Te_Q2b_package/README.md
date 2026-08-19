# Q2b-3 Calculation Package: D_Delta for Trigonal Te

## What this answers

$$D_\Delta \equiv \left.\frac{\partial(E_{H_4}-E_{H_5})}{\partial\epsilon_{zz}}\right|_{\epsilon=0}$$

— the strain derivative of tellurium's H-point valence-band (H4–H5)
spin-orbit splitting, under uniaxial **stress** along the trigonal
($C_3$, $z$) axis, with the elastic boundary condition
$\epsilon_{xx}=\epsilon_{yy}=-0.6265\,\epsilon_{zz}$.

This is **not yet** the SCH/Term-3 answer. It is the first of two
missing inputs identified in the Ampère-anomaly Term-3 audit; the second
(how the CISP response $\chi_{zz}^{\rm spin}$ depends on $\Delta$) is a
separate, downstream calculation, not attempted here.

## Category discipline (per audit convention)

Every number in this package is one of:
- **DERIVED** — computed in this audit (e.g. $\nu=0.6265$, the strain series lattice parameters)
- **LITERATURE-VERIFIED** — taken directly from a cited, checked source ($a_0,c_0,u_0,\Delta_0=63$ meV, elastic constants)
- **ASSUMED/REQUIRED INPUT** — a modeling choice stated explicitly (exchange-correlation functional, cutoffs, k-mesh, smearing)

None of these categories has been silently promoted into another.

## Status of this package: NOT YET EXECUTED

$$\boxed{D_\Delta = \text{not yet measured/calculated}}$$

This package was built after three failed execution attempts in the
authoring environment (see "Known execution environment issues" below).
It is a complete, standalone specification — every input file, the
pseudopotential, and the analysis scripts are real and functional. It
requires a working Quantum ESPRESSO installation to produce a number.

## Directory contents

```
pseudopotentials/
  Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF   validated fully-relativistic Te pseudopotential (frozen, do not modify)
  Te.rel-pbe-n-rrkjus_psl.1.0.0.in    exact ld1.x input used to generate it
  generation.log                       ld1.x output, confirming Dirac-relativistic calculation
  PROVENANCE.md                        full generation/validation chain
  CHECKSUM.txt                         SHA-256 of the UPF file

structures/
  generate_strained_cells.py           regenerates every input file below (re-run if any parameter changes)
  strain_series.json                   computed lattice parameters for every strain point

inputs/
  scf_eps{+-N}_cut{1,2}.in             SCF, clamped ions, two independent cutoff/k-mesh sets
  relax_eps{+-N}_cut1.in               SCF with internal-coordinate relaxation (u free), primary cutoff only
  bands_eps{+-N}_cut{1,2}.in           band structure along Gamma-K-H-A-Gamma, explicit H point
  manifest.json                        machine-readable index of all of the above

analysis/
  extract_H4_H5.py                     parses a 'bands' output, identifies/tracks H4/H5, flags ambiguity
  fit_derivative.py                    fits D_Delta from collected results, cross-checks convergence

results_template.csv                   fill in E_H4_eV, E_H5_eV from your calculations here
```

## How to run

Requires: a **working** Quantum ESPRESSO installation (`pw.x`) with the
included pseudopotential readable, and Python 3 with `numpy`.

```bash
cd inputs/
mkdir -p tmp

# 1. MANDATORY zero-strain benchmark gate -- run this FIRST, alone
pw.x -in scf_eps+0.00000_cut1.in > scf_eps+0.00000_cut1.out
pw.x -in bands_eps+0.00000_cut1.in > bands_eps+0.00000_cut1.out
cd ../analysis
python3 extract_H4_H5.py ../inputs/bands_eps+0.00000_cut1.out --save eps0_cut1.json

# Compare the printed Delta against 63 meV (Barts et al. 2025).
# STOP HERE if the discrepancy is large and cannot be explained by a
# specific, identified cause (structure/pseudopotential/cutoff/k-mesh/
# XC functional). Do not proceed to the strain series from a failed
# benchmark.

# 2. If the benchmark passes: run the remaining strain points, tracking
#    continuity from the epsilon=0 result
for f in ../inputs/scf_eps-0.00250_cut1.in ../inputs/scf_eps-0.00500_cut1.in \
         ../inputs/scf_eps+0.00250_cut1.in ../inputs/scf_eps+0.00500_cut1.in; do
  pw.x -in $f > ${f%.in}.out
done
for f in ../inputs/bands_eps-0.00250_cut1.in ../inputs/bands_eps-0.00500_cut1.in \
         ../inputs/bands_eps+0.00250_cut1.in ../inputs/bands_eps+0.00500_cut1.in; do
  pw.x -in $f > ${f%.in}.out
done
# Extract each, tracking from the nearest already-identified strain point
# (e.g. eps=+0.0025 tracks from eps=0; eps=+0.0050 tracks from eps=+0.0025)
python3 extract_H4_H5.py ../inputs/bands_eps+0.00250_cut1.out --prev eps0_cut1.json --save eps+0.0025_cut1.json
# ... repeat for each strain in order, always tracking from its nearest neighbor

# 3. Repeat the entire series for cutset "cut2" (convergence check) and
#    for the relax_* inputs (clamped-vs-relaxed check)

# 4. Fill in results_template.csv from the saved JSON results, then:
python3 fit_derivative.py ../results_template.csv
```

Expected runtime: each SCF/bands pair is a 3-atom unit cell with a
moderate k-mesh — should be minutes, not hours, on an ordinary
workstation. The full package (2 cutoff sets x 5 strains + 5 relaxed
points) is ~25 total `pw.x` runs.

## Known execution environment issues (so the next person doesn't re-diagnose these)

Three execution attempts were made in the authoring environment, all
blocked for reasons **unrelated to this calculation's physics or inputs**:

1. **Ubuntu-packaged QE 6.7MaX** (`quantum-espresso` 6.7-2build4): fails
   to read the pseudopotential with `xmlr_opentag: severe error, line
   too long`. Diagnosed precisely: 2 lines out of ~49,700 in the UPF
   file (pure numeric radial-function data) exceed this build's XML
   line-length buffer (2600 characters found; buffer limit lower than
   that). A content-preserving fix (inserting line breaks at whitespace
   token boundaries within the two offending lines only, never touching
   any tagged/attributed line) gets past this specific error but
   surfaces a second, deeper `SIGABRT` from a buffer-overflow check
   elsewhere in the same reader — not safely patchable without visibility
   into the compiled reader's internal buffer sizes.
2. **Source-built QE 6.8 and 7.3.1** (from `github.com/QEF/q-e`, tags
   `qe-6.8` and `qe-7.3.1`): both compile toolchains are fine (gfortran +
   BLAS/LAPACK), but `upflib`'s GPU-stub source files (e.g.
   `init_us_2_base_gpu.f90`) unconditionally `USE device_fbuff_m` /
   `device_memcpy_m`, regardless of whether CUDA is requested, in both
   versions. That module is provided by an external library,
   `devicexlib`, hosted **exclusively** at
   `gitlab.com/max-centre/components/devicexlib.git` (confirmed via the
   pinned submodule commit hash in `external/submodule_commit_hash_records`).
   No GitHub mirror was found after checking seven plausible locations.
3. **Conclusion**: a working execution environment needs either (a) a
   QE build with network access to `gitlab.com` at compile time, or (b)
   a different, already-working QE installation (any reasonably modern
   version — the bug in (1) appears specific to this exact Ubuntu
   packaging) with this pseudopotential file, untouched, simply dropped in.

If you have access to a normal HPC/workstation QE installation, none of
the above should be an obstacle — these are specific to the sandboxed,
network-restricted environment this package was built in, not to the
calculation itself.

## Physics specification (frozen, do not change without updating provenance)

| Quantity | Value | Category |
|---|---|---|
| $a_0$ | 4.456 Å | LITERATURE-VERIFIED |
| $c_0$ | 5.927 Å | LITERATURE-VERIFIED |
| $u_0$ (Wyckoff 3a internal coordinate) | 0.269 | LITERATURE-VERIFIED |
| Space group | $P3_121$ (No. 152) | LITERATURE-VERIFIED |
| $\nu = -S_{13}/S_{33}$ (transverse response) | 0.6265 | DERIVED (full compliance-matrix inversion of Royer & Dieulesaint 1979 elastic constants) |
| $\Delta_0$ benchmark target | 63 meV | LITERATURE-VERIFIED (Barts, Tenzin & Sławińska 2025, citing Furukawa 2017 / Shalygin 2012) |
| Exchange-correlation | PBE | ASSUMED (matches the pseudopotential and the Barts et al. model) |
| $E_{\rm cut}^{\rm wfc}$ | 60 / 80 Ry (two sets) | ASSUMED, convergence-tested by design |
| $k$-mesh | 6×6×4 / 8×8×6 | ASSUMED, convergence-tested by design |
| H point | $(1/3,1/3,1/2)$, crystal coords | LITERATURE-VERIFIED (standard hexagonal BZ convention) |
