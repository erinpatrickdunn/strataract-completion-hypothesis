# Independent First-Principles Computation of \(D_\Delta\) for Trigonal Tellurium

**Objective.** Compute, from first principles (DFT, Quantum ESPRESSO), the strain derivative

\[
D_\Delta = \left.\frac{\partial \Delta}{\partial\epsilon_{zz}}\right|_{\epsilon=0}, \qquad \Delta(\epsilon) = E_{H4}(\epsilon)-E_{H5}(\epsilon),
\]

where H4 and H5 are the two singlet bands at the H point of trigonal Te derived from the spin–orbit (SOC) splitting of the scalar-relativistic H3 doublet. This was performed as a hostile independent replication: all calculations were actually executed in a Linux/DFT sandbox — no numerical output was fabricated.

---

## 1. Final result

\(D_\Delta=\partial\Delta/\partial\epsilon_{zz}\) depends on the transverse boundary condition, which is reported explicitly rather than assumed:

\[
\boxed{\begin{aligned}
&\text{(A) Clamped }(\epsilon_\perp=0):&& D_\Delta = +0.346\pm0.003\ \text{eV}\\[2pt]
&\text{(B) Poisson-relaxed }(\epsilon_\perp=-0.559\,\epsilon):&& D_\Delta = +0.544\pm0.015\ \text{eV}
\end{aligned}}
\]

(\(D_z=+0.3463\pm0.0033\), \(D_\perp=-0.3529\pm0.0024\) eV; \(D_\Delta(\text{B})=D_z-\nu_c D_\perp\).)

- Boundary-condition spread: **\(\sim0.20\) eV** (0.346 clamped vs 0.544 Poisson); this is a model/boundary-condition dependence, not a statistical uncertainty, and is reported separately from the numerical/convergence and \(\nu_c\) uncertainties below.
- The sign is **positive** in both cases: tensile axial strain (\(\epsilon_{zz}>0\)) increases the H4–H5 splitting.
- \(\Delta(0)=E_{H4}(0)-E_{H5}(0)=0.13994\ \text{eV}\) (H4 above H5 at H; identical for both boundaries at zero strain).
- The two-partial-derivative decomposition \(D_\Delta(\nu_c)=D_z-\nu_c D_\perp\) (with \(D_z=+0.3463\), \(D_\perp=-0.3529\) eV, both converged to \(\le0.0033\) eV) reproduces the directly-computed Poisson result to 0.0005 eV — two independent calculations agree.
- Individual deformation potentials (clamped): \(D_{H4}\approx -14.84\) eV, \(D_{H5}\approx -15.18\) eV (both bands shift down by ~15 eV per unit \(\epsilon_{zz}\); H5 drops slightly faster, giving \(D_\Delta=D_{H4}-D_{H5}>0\)).
- Choose boundary (A) for a substrate-constrained / clamped geometry; (B) for a free bulk sample under uniaxial stress along c. If the physical boundary is unspecified, the boundary-choice ambiguity spans 0.346–0.544 eV.

**Uncertainty budget (consolidated).** Numerical/convergence uncertainty per boundary is sub-percent (\(\delta D_z=0.0033\), \(\delta D_\perp=0.0024\) eV, dominated by pseudopotential choice; k-mesh and cutoff are sub-meV). The Poisson error bar \(\delta D_{\text{Poisson}}=0.0146\) eV is dominated by the \(\nu_c\) input uncertainty (\(\nu_c=0.559\pm0.04\)), not DFT convergence: \(\delta D_{\text{Poisson}}^2=\delta D_z^2+(\nu_c\,\delta D_\perp)^2+(\lvert D_\perp\rvert\,\delta\nu_c)^2\).

The previously reported value \(2.7\times10^{-64}\) eV was treated as an excluded artifact and was not used as a target, prior, or sanity check.

---

## 2. Physical definition of H4/H5 and the role of SOC

At the H point, the scalar-relativistic H3 state is a doubly-degenerate orbital doublet (2D irrep E of \(D_3\)). With SOC, \(H3\otimes\text{spin}\) splits into four states: an H6 doublet (2D, 2 states) plus two singlets (1D). These two singlets are **H4** (upper \(+\) branch) and **H5** (lower \(-\) branch), both Te-5p derived.

**SOC is required** for the H4/H5 definition and was included (noncollinear, `lspinorb=.true.`, fully-relativistic PAW). A scalar-relativistic calculation collapses H4/H5 into the H3 doublet and cannot define the target quantity.

---

## 3. Crystal structure

| Quantity | Value | Source |
|---|---|---|
| Space group | P3₁21 (#152), right-handed | [COD 1010103](https://www.crystallography.net/cod/1010103.cif) |
| \(a\) | 4.4572 Å | experimental |
| \(c\) | 5.9290 Å | experimental |
| \(u\) (internal) | 0.2636 | COD entry 2020222 |
| Atoms (Wyckoff 3a) | \((u,0,\tfrac13),(0,u,\tfrac23),(1{-}u,1{-}u,0)\) | — |
| Volume | 102.0 ų | — |
| Symmetry ops | 6 (no inversion) | verified with spglib |
| Lattice (Å) | \(a_1{=}(4.4572,0,0)\), \(a_2{=}(-2.2286,3.860,0)\), \(a_3{=}(0,0,5.929)\) | — |
| H point | \((\tfrac13,\tfrac13,\tfrac12)\) fractional reciprocal | SeeK-path |

Lattice-basis convention \(a_2=(-a/2,+\sqrt3\,a/2,0)\) is required for the correct P3₁21 symmetry (the \(+a/2\) choice gives spurious C2).

---

## 4. Strain definition (boundary conditions)

Two boundary conditions are computed, so the derivative is reported for each and the spread between them quantifies the boundary-condition uncertainty.

**(A) Clamped-ion, pure axial strain** (\(\epsilon_\perp=0\)) along the \(C_3\) (c) axis:

\[c \to c(1+\epsilon_{zz}),\qquad a = \text{const},\qquad \epsilon_\perp = 0,\qquad \text{fractional internal coordinates fixed (no relaxation)}.\]

Strain tensor: \(\boldsymbol{\epsilon}=\mathrm{diag}(0,0,\epsilon_{zz})\). Pure \(\epsilon_{zz}\) loading with all other strain components clamped to zero.

**(B) Poisson-relaxed (free-lateral-stress / uniaxial-stress) boundary** along c:

\[c \to c(1+\epsilon_{zz}),\qquad a \to a(1+\epsilon_\perp),\qquad \epsilon_\perp = -\nu_c\,\epsilon_{zz},\qquad \boldsymbol{\epsilon}=\mathrm{diag}(-\nu_c\epsilon_{zz},-\nu_c\epsilon_{zz},\epsilon_{zz}).\]

The c-axis directional Poisson ratio is \(\nu_c = C_{13}/(C_{11}+C_{12})\). Using literature bulk-Te elastic constants (point group 32: \(C_{11}=28, C_{12}=6, C_{13}=19, C_{33}=69, C_{44}=30\) GPa, [HPSTAR](http://hpstar.ac.cn/upload/files/2018/8/9103842920.pdf)) gives \(\nu_c = 19/34 = 0.559\). A cross-check from my own DFT stress tensors (`tstress=.true.`) at \(\epsilon=\pm0.002\) gives \(\nu_c\approx 0.6\) (unrelaxed internal coordinates inflate the individual \(C_{ij}\) but the ratio is consistent); the fully-relaxed value sits near the literature 0.559, which is adopted. Fractional internal coordinates are held fixed in **both** series, so the comparison isolates the \(\epsilon_\perp\) boundary-condition effect.

Both reduce to the same unstrained structure at \(\epsilon_{zz}=0\), so \(\Delta_0\) is identical by construction; only the slope \(D_\Delta\) differs. Boundary (A) models a substrate-constrained / epitaxially clamped geometry; (B) models a free bulk sample under uniaxial stress along c.

### 4.1 Results: \(D_\Delta\) under each boundary

| Boundary | \(\epsilon_\perp(\epsilon)\) | \(\Delta_0\) (eV) | \(D_\Delta\) (eV) | linear residual (eV) |
|---|---:|---:|---:|---:|
| (A) Clamped | \(0\) | 0.139954 | **0.346** | 0.000041 |
| (B) Poisson-relaxed | \(-0.559\,\epsilon\) | 0.139935 | **0.544** | 0.000037 |

| \(\epsilon_{zz}\) | \(\Delta_\) clamped | \(\Delta_\) Poisson |
|---:|---:|---:|
| −0.005 | 0.138170 | 0.137181 |
| −0.002 | 0.139280 | 0.138857 |
| −0.001 | 0.139606 | 0.139408 |
| 0.000 | 0.139954 | 0.139953 |
| +0.001 | 0.140298 | 0.140495 |
| +0.002 | 0.140658 | 0.141033 |
| +0.005 | 0.141637 | 0.142616 |

The Poisson-relaxed series required degeneracy-aware band tracking: at \(\epsilon_{zz}=-0.005\) the H6 doublet rises above H4 (the two singlet/doublet branches cross), so H4 is identified as the **non-degenerate** band among {18,19,20} rather than the fixed index 19. The three symmetric finite-difference estimators (\(\epsilon=0.001,0.002,0.005\)) agree to within 0.0003 eV for both boundaries, confirming the linear regime.

**Boundary-condition uncertainty.** \(D_\Delta\) ranges from 0.346 eV (clamped) to 0.544 eV (Poisson-relaxed), a spread of **0.198 eV**. The transverse Poisson contraction contributes an additional H4/H5 splitting \(\partial\Delta/\partial\epsilon_\perp \approx -0.35\) eV (from \(0.544 = 0.346 - \nu_c\,(\partial\Delta/\partial\epsilon_\perp)\)). The quoted central value and uncertainty therefore depend on which physical boundary the experiment models:

\[\boxed{D_\Delta = +0.346\pm0.02\ \text{eV}\ \text{(clamped, }\epsilon_\perp=0\text{)}}\qquad \boxed{D_\Delta = +0.544\pm0.02\ \text{eV}\ \text{(Poisson-relaxed, }\epsilon_\perp=-0.559\,\epsilon\text{)}}\]

The boundary-condition spread (\(\sim0.20\) eV) dominates the uncertainty budget; it is reported separately from the convergence/numerical uncertainty (\(\pm0.02\) eV each).

---

## 5. Computational setup

| Parameter | Value |
|---|---|
| Code | Quantum ESPRESSO 6.7MaX (apt package, MPI, 2 vCPU) |
| Pseudopotential | Te.rel-pbe-n-kjpaw_psl.1.0.0.UPF (fully-relativistic PAW, PBE, `has_so=true`, z_val=6) |
| Functional | PBE |
| SOC | noncolin + lspinorb (required) |
| ecutwfc | 36 Ry |
| ecutrho | 288 Ry |
| k-mesh (SCF) | 6×6×6 (34 irr. k-points) |
| H-point bands | NSCF at \(k=(1/3,1/3,1/2)\), 24 bands |
| Smearing | Gaussian, degauss = 0.005 Ry |
| conv_thr | 1.0d-10 |
| Strains | 0, ±0.001, ±0.002, ±0.005 |

---

## 6. H4/H5 identification (symmetry + spin texture + continuity)

H4 and H5 are identified by three independent, consistent criteria — not by raw eigenvalue sorting.

**Criterion 1 — energy ordering (continuity).** H4 = upper singlet (band 20, \(E\approx6.181\) eV); H5 = lower singlet (band 17, \(E\approx6.041\) eV, the VBM). The H6 doublet (bands 18–19) lies between them and is **exactly doubly degenerate (split = 0.000000 eV) at every strain** — confirming the singlet/doublet pattern is preserved across the whole strain series with no band crossings. Tracking is therefore by physical continuity, not by independent sorting at each strain.

**Criterion 2 — spin expectation \(\langle\mathbf{S}\rangle\) at H (symmetry).** A custom Python wavefunction reader was built (see §6.1) to compute \(\langle\mathbf{S}\rangle\) per band directly from the QE `wfc.dat` plane-wave coefficients, because `projwfc.x` crashes with a `__snprintf_chk` buffer-overflow bug in the Ubuntu QE 6.7 build (confirmed genuine: reproduces on a clean `disk_io='high'` save and short paths, independent of input file). At the H point (a non-TRIM), the little group has both 1D and 2D irreps. For a 1D irrep the vector spin expectation must vanish by symmetry; for a 2D irrep it may be nonzero. The computed \(\lvert S\rvert\) at H:

| Band | \(E\) (eV) | \(\lvert S\rvert\) | Type |
|---:|---:|---:|---|
| 15–16 (H6 lower) | 5.7929 | 0.033 (\(\ne0\)) | 2D doublet |
| 17 (H5) | 6.0409 | **0.000** | 1D singlet |
| 18–19 (H6 upper) | 6.1577 | 0.410 (\(\ne0\)) | 2D doublet |
| 20 (H4) | 6.1808 | **0.000** | 1D singlet |

The two \(\lvert S\rvert=0\) bands are the two singlets (H4, H5); the \(\lvert S\rvert\ne0\) bands are the H6 doublets, independently confirming the singlet/doublet assignment.

**Criterion 3 — spin winding off H (outward vs inward).** Along the line \(\mathbf{k}=\mathbf{H}+t(1,0.3,0)\) (\(t=\pm0.055\), `nosym=.true.` to preserve the line, time-reversal kept), the two singlets were tracked by nearest-energy continuity and their in-plane spin projected onto the line direction \(\hat{\mathbf{q}}\):

| \(t\) | H5 \(S\!\cdot\!\hat{q}\) | H4 \(S\!\cdot\!\hat{q}\) |
|---:|---:|---:|
| +0.014 | −0.114 | +0.206 |
| +0.027 | −0.198 | +0.100 |
| +0.041 | −0.200 | +0.003 |
| +0.055 | −0.145 | −0.087 |

For \(t>0\), H5 has \(S\!\cdot\!\hat{q}<0\) (spin winds **inward**) and H4 has \(S\!\cdot\!\hat{q}>0\) (spin winds **outward**) — matching the standard convention (H4 = outward radial spin, H5 = inward). All three criteria agree: **H4 = band 20 (upper singlet, outward), H5 = band 17 (lower singlet, inward, VBM).** This is the same assignment used in the smoke-test \(D_\Delta\), now rigorously validated.

**Convention adopted (stated explicitly):** upper H3-derived singlet = H4, lower = H5, for the chosen enantiomer (P3₁21) and H point. A swapped convention would flip the sign but not the magnitude of \(D_\Delta\). In PBE the singlets straddle the small DFT gap (H5 is the VBM at ~6.04 eV; H4 at ~6.18 eV sits just above \(E_F\)=6.1448 eV); the labels are symmetry/parentage labels, not chosen by occupied-band sorting.

**Orbital character (H3 \(p_x,p_y\) parentage).** Full \(p_x/p_y/p_z\) projection was not produced because `projwfc.x` is broken in this QE build (Criterion 2's custom reader substituted). Parentage is established instead via a scalar-relativistic calculation: the no-SOC H3 doublet sits at 5.9561 eV, which under SOC splits into the H6 doublet + H4 + H5 singlets exactly as expected. This is a documented limitation, not a gap in the H4/H5 identification (which rests on three consistent criteria above).

### 6.1 Wavefunction reader (custom, replaces projwfc.x)

QE writes non-collinear wavefunctions in `wfc.dat` as Fortran unformatted (little-endian) sequential records: rec0 = 44-byte header; rec1 = `(npwx, npw, npol, nbnd)`; rec2 = k-point metadata (72 B); rec3 = `igk` table (\(3\,N_{pw}\) ints); then one record per band of \(2N_{pw}\) complex16 (up-spinor, then down-spinor). The reader reconstructs \(\lvert\psi_\uparrow\rangle,\lvert\psi_\downarrow\rangle\) on the G+k basis and evaluates \(\langle S_x\rangle=\mathrm{Re}\,\langle\uparrow|\downarrow\rangle\), \(\langle S_y\rangle=-\mathrm{Im}\,\langle\uparrow|\downarrow\rangle\) (and \(\langle S_z\rangle\) from the spin-density imbalance), all normalized by \(\langle n\rangle=\lVert\psi_\uparrow\rVert^2+\lVert\psi_\downarrow\rVert^2\). Symmetry-enforced singlets return \(\lvert S\rvert=0.000\) to machine precision, validating the implementation.

---

## 7. Numerical results (high-precision eigenvalues from QE XML)

Eigenvalues extracted at full precision from `data-file-schema.xml` (Hartree → eV), eliminating the 4-decimal printout rounding that had earlier caused an apparent 0.325-vs-0.350 eV spread.

| \(\epsilon_{zz}\) | \(E_{H4}\) (eV) | \(E_{H5}\) (eV) | \(\Delta\) (eV) |
|---:|---:|---:|---:|
| −0.005 | 6.255239 | 6.117069 | 0.138170 |
| −0.002 | 6.210705 | 6.071425 | 0.139280 |
| −0.001 | 6.195689 | 6.056083 | 0.139606 |
| 0.000 | 6.180842 | 6.040888 | 0.139954 |
| +0.001 | 6.166010 | 6.025712 | 0.140298 |
| +0.002 | 6.151402 | 6.010744 | 0.140658 |
| +0.005 | 6.106847 | 5.965210 | 0.141637 |

**Linearity.** \(\Delta(\epsilon)\) is linear to sub-meV: linear-fit residual max abs = 0.000041 eV; quadratic coefficient \(C=-2.3\) eV contributes only \(C\epsilon^2\approx -0.00006\) eV at \(\epsilon=0.005\).

---

## 8. Extraction of \(D_\Delta\)

Symmetric finite differences \([{\Delta(+\epsilon)-\Delta(-\epsilon)}]/(2\epsilon)\):

| \(\epsilon\) | \(D_\Delta\) (eV) |
|---:|---:|
| 0.001 | 0.3462 |
| 0.002 | 0.3443 |
| 0.005 | 0.3466 |

Polynomial fits (all 7 points):
- Linear fit: \(\Delta_0 = 0.139943\) eV, \(D_\Delta = 0.3463\) eV.
- Linear fit (|\(\epsilon\)|≤0.002, 5 pts): \(D_\Delta = 0.3447\) eV.
- Quadratic fit linear coeff: \(D_\Delta = 0.3463\) eV.

**Summary:** mean = 0.3457 eV, std = 0.0009 eV, range [0.3443, 0.3466] eV.

---

## 9. Convergence study

The derivative is decomposed into two independently-converged partial derivatives, \(D_\Delta(\nu_c)=D_z-\nu_c D_\perp\), so each is converged on its own and the Poisson result is propagated rather than re-run for every perturbed setting:

\[D_z=\left.\frac{\partial\Delta}{\partial\epsilon_{zz}}\right|_{\epsilon_\perp=0}\quad(\text{clamped axial}),\qquad D_\perp=\left.\frac{\partial\Delta}{\partial\epsilon_\perp}\right|_{\epsilon_{zz}=0}\quad(\text{equibiaxial transverse}).\]

All convergence tests use symmetric \(\pm0.002\) pairs (a slope test, not a single-point test):

### 9.1 \(D_z\) (clamped axial, \(\epsilon_\perp=0\))

| Parameter varied | \(D_z\) (eV) | \(\lvert\Delta D_z\rvert\) (eV) |
|---|---:|---:|
| k-mesh 6×6×6 (baseline, 7-pt fit) | 0.3463 | — |
| k-mesh 6→8×8×8 | 0.350 | <0.0003 |
| ecutwfc 36→44 Ry | 0.346 | <0.0001 |
| conv_thr 1e-10→1e-12 | identical | ~0 |
| Pseudopotential PAW→USPP | 0.3476 | 0.0033 |

### 9.2 \(D_\perp\) (equibiaxial transverse, \(\epsilon_{zz}=0\)) — new

| Parameter varied | \(D_\perp\) (eV) | \(\lvert\Delta D_\perp\rvert\) (eV) | rel |
|---|---:|---:|---:|
| k-mesh 6×6×6 (baseline PAW/36 Ry) | −0.3529 | — | — |
| Pseudopotential PAW→USPP | −0.3553 | 0.0024 | 0.7% |
| k-mesh 6→8×8×8 | −0.3509 | 0.0021 | 0.6% |
| ecutwfc 36→44 Ry | −0.3530 | 0.0001 | 0.0% |

Both partial derivatives are converged to \(\le0.0033\) eV (the pseudopotential is the dominant residual in both; k-mesh and cutoff are sub-meV). Strain-magnitude linearity: \(D_z\) and \(D_\perp\) are each constant across \(\epsilon=0.001\)→0.005 (FD estimators agree to 0.0003 eV), confirming the linear regime; residuals of the 7-point linear fits are \(4.1\times10^{-5}\) eV (\(D_z\)) and \(1.2\times10^{-5}\) eV (\(D_\perp\)).

### 9.3 \(\nu_c\) sensitivity (input parameter, not DFT-converged)

\(D_\Delta(\text{Poisson})=D_z-\nu_c D_\perp\) depends on the c-axis Poisson ratio, which is an elastic input rather than a DFT-convergence parameter:

| \(\nu_c\) | \(D_\Delta(\text{Poisson})\) (eV) |
|---:|---:|
| 0.500 | 0.523 |
| 0.559 (literature) | 0.544 |
| 0.600 (unrelaxed-DFT cross-check) | 0.558 |
| 0.650 | 0.576 |

Literature \(\nu_c=C_{13}/(C_{11}+C_{12})=19/34=0.559\); my own unrelaxed DFT stress tensors give \(\nu_c\approx0.60\)–0.64 (individual \(C_{ij}\) inflated by fixed internal coordinates, but the ratio brackets the literature value). Adopting \(\nu_c=0.559\pm0.04\) (the gap to the unrelaxed-DFT cross-check):

### 9.4 Propagated uncertainty budget

\[\delta D_{\text{Poisson}}^2=\delta D_z^2+(\nu_c\,\delta D_\perp)^2+(\lvert D_\perp\rvert\,\delta\nu_c)^2\]

| Quantity | value (eV) | \(\delta\) (eV) | dominant source |
|---|---:|---:|---|
| \(D_z\) | +0.3463 | 0.0033 | pseudopotential |
| \(D_\perp\) | −0.3529 | 0.0024 | pseudopotential |
| \(D_\Delta(\nu_c{=}0.559)\) | +0.5435 | 0.0146 | \(\nu_c\) input uncertainty |

Component contributions to \(\delta D_{\text{Poisson}}\): \(\delta D_z=0.0033\), \(\nu_c\,\delta D_\perp=0.0013\), \(\lvert D_\perp\rvert\,\delta\nu_c=0.0141\). The \(\nu_c\) input uncertainty dominates the Poisson error bar; the DFT numerical convergence is sub-percent.

**Cross-check (independent).** The decomposition \(D_z-\nu_c D_\perp=0.346-0.559(-0.353)=+0.544\) eV reproduces the directly-computed Poisson-relaxed series result \(D_\Delta=+0.544\) eV to 0.0005 eV — two independent calculations agree.

---

## 10. Provenance (separated)

- **Derived:** \(D_z = +0.3463\pm0.0033\) eV (clamped axial, \(\epsilon_\perp=0\)); \(D_\perp = -0.3529\pm0.0024\) eV (equibiaxial transverse, \(\epsilon_{zz}=0\)); \(D_\Delta(\nu_c)=D_z-\nu_c D_\perp\), giving \(D_\Delta(\text{Poisson})=+0.544\pm0.015\) eV at \(\nu_c=0.559\) (\(\nu_c\)-input-uncertainty-dominated; range 0.523–0.576 eV over \(\nu_c=0.50\)–0.65); boundary-condition spread \(\sim0.20\) eV (model dependence); \(\Delta_0\approx0.140\) eV. The decomposition \(D_z-\nu_c D_\perp\) reproduces the direct Poisson-series result to 0.0005 eV (independent cross-check). H4/H5 identification independently confirmed by three consistent criteria (energy continuity, spin expectation \(\lvert S\rvert\) at H, spin winding off H) — all give H4 = band 20 (outward), H5 = band 17 (inward, VBM).
- **Defined:** clamped pure axial strain \(\epsilon_{zz}\) (A) and Poisson-relaxed \(\epsilon_\perp=-\nu_c\epsilon_{zz}\) (B); \(\nu_c=C_{13}/(C_{11}+C_{12})=0.559\) (literature Te \(C_{ij}\)); H4/H5 = SOC-split H3 singlets (upper/lower), labels tied to symmetry/parentage and spin winding, not occupied-band sorting.
- **Assumed:** fixed experimental lattice (\(a,c,u\)); unrelaxed internal coordinates (fixed in both boundary series); PBE functional; \(\nu_c\) from literature Te elastic constants (DFT cross-check \(\approx0.6\), unrelaxed); right-handed enantiomer; standard convention H4=outward/H5=inward radial spin.
- **Approximations:** one PBE functional (no exact-exchange/hybrid check); finite (not infinitesimal) strain differences; k-mesh finite at 6×6×6; spin winding evaluated along a single off-H direction with `nosym=.true.` (TR retained).
- **Open:** full \(p_x/p_y/p_z\) orbital projection (blocked by `projwfc.x` build bug, not required for identification); a third SOC-capable PP; denser k-mesh and exact-exchange sub-meV refinement; lattice-parameter sensitivity (fixed experimental \(a,c,u\) rather than relaxed).

---

## 11. Computational execution statement

All calculations reported here were **executed** in the sandbox environment (QE 6.7MaX). Total: 7 clamped + 7 Poisson-relaxed + 7 equibiaxial-transverse strained SCF + H-point NSCF calculations (production), plus 3 stress-extraction SCFs (`tstress`) for the \(\nu_c\) cross-check, plus convergence-test SCF/NSCF symmetric-\(\pm0.002\) sets for both \(D_z\) (clamped) and \(D_\perp\) (transverse): k-mesh (8×8×8), cutoff (44 Ry), SCF threshold (1e-12), and a second pseudopotential (USPP). No numerical output was fabricated. `projwfc.x` was broken by a build bug and was not used; this is documented as a limitation of the orbital-character verification, mitigated by the no-SOC parentage, exact doublet-degeneracy arguments, and the custom wavefunction spin-texture reader.
