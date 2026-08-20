# Independent DFT Replication — Strain Derivative of the H4–H5 Splitting in Trigonal Tellurium

**Target observable:** \(D_\Delta = \partial(E_{H4}-E_{H5})/\partial\varepsilon_{zz}\) in trigonal Te (space group \(P3_1 21\), #152).
**Posture:** Hostile, independent replication. No value from the prior handoff was used as a target, prior, sanity check, or assumed result. Every number below is from executed QE output or a cited literature source.

---

## 1. Verdict (summary)

| Quantity | Independent result | Provenance | Handoff/Thread A (UNVERIFIED, post-hoc comparison) |
|---|---|---|---|
| \(\Delta_0 = E_{H4}-E_{H5}\) (zero strain) | **141 meV** (splitting magnitude, upper−lower singlet) | executed | 139.94 meV (Thread A) — agrees to 0.7% |
| \(D_\Delta\) clamped (\(\varepsilon_\perp=0\)) | **0.35 ± 0.01 eV** | executed | 0.346 eV — agrees to ~1% |
| \(D_\Delta\) Poisson (\(\varepsilon_\perp=-\nu\varepsilon_{zz}\)) | **0.57 ± 0.02 eV** | executed (direct) + derived (decomp) | 0.544 eV — agrees to ~5% |
| Poisson ratio \(\nu\) | **0.6265** | derived from literature elastic constants | 0.559 vs 0.6265 (claimed to disagree — error) |

The handoff's central criticism — that Thread A's \(\Delta_0=139.94\) meV "fails the 63 meV benchmark by 2×" — is a **misreading**. The 63 meV in Barts et al. is the k·p Zeeman-gap parameter \(\Delta\), i.e. **half** the model H4−H5 splitting \(2\Delta\approx126\) meV, not \(E_{H4}-E_{H5}\) itself. Thread A's 139.94 meV was therefore consistent with Barts all along. My independent \(\Delta_0=141\) meV confirms this.

The handoff's \(\nu\) "discrepancy" (0.559 vs 0.6265) was also an **error**: for trigonal symmetry, \(-S_{13}/S_{33} = C_{13}/(C_{11}+C_{12})\) exactly (algebraic identity), and both give 0.6265.

**Unresolved (stated honestly):** the strict irrep sign of \(E_{H4}-E_{H5}\) (which singlet is H4 by symmetry) was not pinned. I report the **positive splitting magnitude** (upper singlet − lower singlet), matching the Barts \(2\Delta\) convention. This does not affect the magnitude, the strain derivative, or the comparison.

---

## 2. Gate 0 — pinned before any strain series

### (a) Literature benchmark (Barts et al. 2025)

Barts, Tenzin & Sławińska, *Nature Communications* **16**, 4056 (2025) ([arXiv:2407.01187](https://arxiv.org/abs/2407.01187), [Nat. Comms. s41467-025-59143-0](https://www.nature.com/articles/s41467-025-59143-0)) use a two-state k·p Hamiltonian at the H point:
\[
\hat H_k = -A k_z^2 - B(k_x^2+k_y^2) + \beta k_z \hat\tau_z + \Delta\,\hat\tau_x,\quad E_\pm = \dots \pm \sqrt{\Delta^2+\beta^2 k_z^2}.
\]
At H (\(k_z=0\)) the model splitting is **\(2\Delta\)**. The paper fits \(\Delta\approx 63\) meV, so the model H4−H5 splitting is \(2\Delta\approx126\) meV, and maps \(\psi_+\to H4\), \(\psi_-\to H5\).

**Conclusion:** 63 meV is the **half-splitting / Zeeman-gap parameter**, not \(E_{H4}-E_{H5}\). The handoff's "63 meV benchmark for \(\Delta_0\)" was a misreading; the proper benchmark is \(2\Delta\approx126\) meV.

Corroborating literature (LITERATURE-DERIVED):
- [Nature Comms. 2020 (PMC7417742)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7417742/): H4 = uppermost VB (singlet), H5 = VB below H4 (singlet), H6 = lower-lying VB (doublet) + CB minimum (doublet); experimental H4−H5 splitting ≈ 0.11 eV (the 11-µm absorption band).
- [Tsirkin, PRB 2018](https://cfm.ehu.es/ivo/publications/tsirkin-prb18.pdf): gap at H = 0.312 eV (DFT), 0.323 eV (exp).

### (b) Crystal structure (COD primary source)

Pinned to [COD 2020222](http://www.crystallography.net/cod/2020222.html) — Adenis, Langer & Lindqvist, *Acta Cryst.* C **45**, 941 (1989):
- \(a = 4.4572\) Å, \(c = 5.9290\) Å, \(u = 0.2636\), right-handed \(P3_1 21\) (#152).
- Wyckoff 3a: \((u,0,\tfrac13), (0,u,\tfrac23), (-u,-u,0)\).
- The handoff's \(u=0.269\) is a **DFT-relaxed** value (structure-prediction literature); \(u=0.2636\) is the **experimental** value used here.

### (c) Executable QE environment (EXECUTED)

- **QE version:** PWSCF v.7.5 via conda-forge (`conda create -n qe -c conda-forge qe=7.5`).
- **Pseudopotential:** [Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF](https://pseudopotentials.quantum-espresso.org/upf_files/Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF) — USPP, PBE, fully-relativistic (`has_so=true`), \(z_\text{val}=6\); recommended cutoffs wfc=32.0 Ry / rho=156.7 Ry.
- The Ubuntu-packaged QE 6.7MaX was avoided (documented UPF-read failure).
- Smoke test (tiny SCF): UPF reads, SCF runs, JOB DONE. → Environment confirmed executable.

---

## 3. Zero-strain SOC calculation (EXECUTED)

**Settings:** PBE+SOC, noncolin+lspinorb, ecutwfc=50 Ry, ecutrho=300 Ry, 6×6×6 k-mesh, Gaussian smearing degauss=0.01 Ry, Davidson diagonalization, conv_thr=1e-8 Ry. Ions/cell at the experimental COD structure (no relaxation).

**Convergence (EXECUTED):** 8×8×8 k-mesh / wfc=70 Ry / rho=560 Ry gives identical \(\Delta_0 = 141.0\) meV (to 0.1 meV) → the splitting is converged at 6×6×6/rho300. The strain derivative is also cutoff-converged: re-running the clamped ±0.005 and Poisson ±0.005 endpoints at 6×6×6 / wfc=70 / rho=560 reproduces \(D_\Delta^\text{clamped}=0.350\) eV and \(D_\Delta^\text{Poisson}=0.570\) eV identically (to 0.1 meV) — see §7.

**SCF:** total energy \(E = -85.64373\) Ry; Fermi 6.146 eV; 18 occupied bands.

**H4/H5 identification (by physical identity, not by target value):**
At H = \((\tfrac13,\tfrac13,\tfrac12)\) the manifold is 4 bands — **two singlets + one doublet** (H6):
- b17 = 6.050 eV (singlet, VBM)
- b18/b19 = 6.166 eV (doublet = H6)
- b20 = 6.191 eV (singlet)

The two singlets are H4 and H5; the doublet is H6 — consistent with the literature picture above. \(\Delta_0 = E_\text{upper singlet}-E_\text{lower singlet} = 141\) meV.

**PBE artifact (noted, does not affect magnitude):** in PBE the gap is compressed, so the H5 singlet is pushed above the H6(CB) doublet, inverting the H4/H5 energy ordering vs GW. The **splitting magnitude is robust**.

**Orbital character / irrep sign (EXECUTED, see §7):** A clean single-H-kpoint projwfc (`lsym=.true.`, `strain_H_single/`) was used to obtain the orbital character of all 28 bands at H. The full H4/H5/H6 manifold (bands 17–20) shares the **same dominant atomic character — Te p₃/₂, m_j=±3/2** (bands 1–6 are s, 7–16 are p₁/₂); the manifold bands differ only in their C₂z-screw symmetry eigenvalue, which atomic-orbital projection does not resolve. The symmetrized `lsym` projection file was not produced by projwfc.x in this (non-centrosymmetric + nonsymmorphic + SOC) case. The strict irrep sign (which singlet is H4) is therefore **not resolvable from orbital character** and is reported as **UNVERIFIED**; I report the positive splitting magnitude (upper−lower singlet), matching the Barts \(2\Delta\) convention. This does not affect the magnitude, the strain derivative, or the literature comparison.

---

## 4. Strain derivative (EXECUTED + DERIVED)

All strain paths use **ions clamped** (fractional coordinates fixed); only the cell changes. Symmetric finite differences at \(\varepsilon=\pm0.005,\pm0.0025\) (5 points incl. zero). H4/H5 tracked through strain by physical identity: within the 4-band manifold, the H6 doublet = adjacent pair with smallest gap; H4/H5 = the other two singlets. (This was necessary — band indices cross under strain; at one Poisson-strain point H5 moved from b20 to b18.)

### Clamped path (\(\varepsilon_\perp=0\), only c scaled)

| \(\varepsilon_{zz}\) | −0.005 | −0.0025 | 0 | +0.0025 | +0.005 |
|---|---|---|---|---|---|
| \(\Delta\) (meV) | 139.2 | 140.1 | 141.0 | 141.8 | 142.7 |

\[
D_\Delta^\text{clamped}=D_z = \frac{\Delta(+0.005)-\Delta(-0.005)}{0.01}=0.350\ \text{eV}
\]
(4-pt O(h⁴): 0.337 eV; h=0.0025: 0.340 eV). Highly linear. **\(D_z = 0.35\pm0.01\) eV.**

### Transverse path (\(\varepsilon_{zz}=0\), only a,b scaled)

| \(\varepsilon_\perp\) | −0.005 | −0.0025 | 0 | +0.0025 | +0.005 |
|---|---|---|---|---|---|
| \(\Delta\) (meV) | 142.8 | 141.9 | 141.0 | 140.1 | 139.2 |

\[
D_\perp = \partial\Delta/\partial\varepsilon_\perp = -0.360\ \text{eV}
\]
(linear at both amplitudes). **\(D_\perp = -0.36\) eV.**

### Poisson ratio (DERIVED from literature elastic constants)

Te single-crystal elastic stiffness (point group 32), experimental ([Elastic & piezoelectric constants of trigonal Se and Te](https://ouci.dntb.gov.ua/en/works/9Q5LNj69/); units 10¹⁰ N/m²): \(C_{11}=3.257,\ C_{12}=0.845,\ C_{13}=2.57,\ |C_{14}|=1.238,\ C_{33}=7.17,\ C_{44}=3.094\) (check: \(C_{66}=(C_{11}-C_{12})/2=1.206\) ✓).

Full inversion of the 6×6 Voigt stiffness gives \(\nu=-S_{13}/S_{33}=\mathbf{0.6265}\). For trigonal symmetry the 1-2-3 block decouples from \(C_{14}\), so this **algebraically equals** \(C_{13}/(C_{11}+C_{12})=0.6265\). → The handoff's "0.559 (simple) vs 0.6265 (full inversion) disagree" was an error; the correct value is 0.6265.

### Poisson path (\(\varepsilon_\perp=-\nu\,\varepsilon_{zz}\), \(\nu=0.6265\))

| \(\varepsilon_{zz}\) | −0.005 | −0.0025 | +0.0025 | +0.005 |
|---|---|---|---|---|
| \(\Delta\) (meV) | 138.1 | 139.5 | 142.5 | 143.8 |

**Direct:** \(D_\Delta^\text{Poisson}=[\Delta(+0.005)-\Delta(-0.005)]/0.01 = \mathbf{0.570}\) eV.

**Decomposition (cross-check):** \(\Delta(\varepsilon_{zz},\varepsilon_\perp)=\Delta_0+D_z\varepsilon_{zz}+D_\perp\varepsilon_\perp\); under \(\varepsilon_\perp=-\nu\varepsilon_{zz}\):
\[
D_\Delta^\text{Poisson}=D_z-\nu D_\perp = 0.350-0.6265\times(-0.360)=\mathbf{0.576}\ \text{eV}.
\]
Direct (0.570) and decomposition (0.576) agree to ~1%. **\(D_\Delta^\text{Poisson}=0.57\pm0.02\) eV.** (The h=0.0025 / 4-pt values are noisier — 0.1 meV printed-eigenvalue noise amplified at smaller step; primary result uses h=0.005 + decomposition.)

---

## 5. Provenance tags

**EXECUTED (actual QE output):**
- Zero-strain SCF + bands: `strain_zero_clean/{scf,bands}.{in,out}` (clean reference, 7-pt k-list).
- Clamped series: `strain_clamp_{m0050,m0025,p0025,p0050}/{scf,bands}.{in,out}`.
- Transverse series: `strain_trans_{m0050,m0025,p0025,p0050}/{scf,bands}.{in,out}`.
- Poisson series: `strain_pois_{m0050,m0025,p0025,p0050}/{scf,bands}.{in,out}`.
- Convergence check: `strain_0/{scf_conv,bands_conv}.{in,out}` (8×8×8, wfc70/rho560).
- Derivative convergence check (clamped + Poisson ±0.005 at 6×6×6/wfc70/rho560, fresh dirs): `strain_hc2_clamp_{m0050,p0050}/`, `strain_hc2b_pois_{m0050,p0050}/` (`{scf,bands}.{in,out}`).
- H-point orbital character (single-H-kpoint SCF + projwfc, `lsym=.true.`): `strain_H_single/{scf,projwfc}.{in,out}`.
- Smoke test: `te_smoke.{in,out}`. Structure CIF: `Te_COD_2020222.cif`. PP: `pseudo/Te.rel-pbe-n-rrkjus_psl.1.0.0.UPF`.

**DERIVED (from executed output):** \(\Delta_0=141\) meV; \(D_z=0.35\) eV; \(D_\perp=-0.36\) eV; \(D_\Delta^\text{Poisson}=0.57\) eV (direct + decomposition). Extraction script: `extract_results.py`.

**LITERATURE-DERIVED:** Barts \(2\Delta\approx126\) meV; Nature 2020 ~110 meV; Te elastic constants → \(\nu=0.6265\).

**ASSUMED (stated):** experimental COD structure (cited); QE-library PP (cited); **ions clamped in all strain paths** (only cell path varies); smearing degauss=0.01 Ry.

**UNVERIFIED (stated):** strict irrep sign of \(E_{H4}-E_{H5}\) (which singlet is H4 by symmetry). Orbital character WAS obtained (§7): the H4/H5/H6 manifold shares dominant Te p₃/₂ m_j=±3/2 character, so atomic projection does not resolve the C₂z-screw eigenvalue that distinguishes H4 from H5; the symmetrized `lsym` projection file was not produced. Reported as the positive splitting magnitude. Derivative convergence in smearing not separately tested (cutoff/k-mesh convergence verified for both \(\Delta_0\) and \(D_\Delta\); see §7).

---

## 7. Gap closure (two residual checks, EXECUTED)

Two residual gaps were closed after the main series. Both are documented honestly here.

### (a) Strain-derivative cutoff convergence — VERIFIED

The production series used 6×6×6 / wfc=50 / rho=300. To confirm the derivative (not just \(\Delta_0\)) is converged, the clamped and Poisson \(\varepsilon=\pm0.005\) endpoints were re-run at 6×6×6 / wfc=70 / rho=560 (40% higher wfc cutoff, ~3.5× higher rho) in fresh output directories:

| Path | \(\Delta(-0.005)\) | \(\Delta(+0.005)\) | \(D_\Delta\) | vs production |
|---|---|---|---|---|
| Clamped (wfc50/rho300, production) | 139.2 meV | 142.7 meV | **0.350 eV** | — |
| Clamped (wfc70/rho560) | 139.2 meV | 142.7 meV | **0.350 eV** | identical (0.1 meV) |
| Poisson (wfc50/rho300, production) | 138.1 meV | 143.8 meV | **0.570 eV** | — |
| Poisson (wfc70/rho560) | 138.1 meV | 143.8 meV | **0.570 eV** | identical (0.1 meV) |

Both \(D_z\) and \(D_\Delta^\text{Poisson}\) are reproduced to 0.1 meV at the higher cutoff → **the derivative is cutoff-converged**. (Two intermediate high-cutoff attempts were discarded as buggy and are not in the results: an isotropic/hydrostatic-strain run that scaled both a and c — a different strain path — and a Poisson run with a transverse-strain sign error in m0050. Both were caught by cell verification, fixed, and superseded by the clean runs above.)

### (b) H4/H5 irrep sign — NOT resolvable from orbital character (genuine limitation)

To attempt the irrep assignment cleanly, a single-H-kpoint SCF (`K_POINTS` = H only, zero strain, nbnd=28) followed by `projwfc.x` with `lsym=.true.` was run. Decoding the orbital character of all 28 bands at H:

- Bands 1–6: s (l=0, j=½).
- Bands 7–10, 13–16: p₁/₂ (l=1, j=½, m_j=±½).
- Bands 11–12, 17–20, 21–26: p₃/₂ (l=1, j=3/2). Within the H4/H5/H6 manifold (bands 17–20) **all four bands share the same dominant p₃/₂, m_j=±3/2 atomic character** (components on atoms 1/2 ±3/2 and atom 3).

Because H4 and H5 are distinguished by their C₂z-screw symmetry eigenvalue (a phase under the nonsymmorphic screw), not by s/p/j orbital character, atomic-orbital projection cannot separate them. The symmetrized `lsym` projection file was not produced by projwfc.x for this non-centrosymmetric + nonsymmorphic + SOC case, and no explicit screw-irrep label was printed. **Conclusion (by execution, not assumption): the irrep sign is not resolvable from the available projection output.** D_Δ is therefore reported as the **positive splitting-magnitude derivative** (upper−lower singlet, Barts \(2\Delta\) convention); the signed \(E_{H4}-E_{H5}\) assignment remains UNVERIFIED. This does not affect any magnitude, derivative, or comparison in this report.

---

## 8. Post-hoc comparison to the handoff / Thread A (labeled, not used as targets)

| Quantity | This work (independent) | Handoff/Thread A (UNVERIFIED) | Note |
|---|---|---|---|
| \(\Delta_0\) | 141 meV | 139.94 meV | agrees 0.7% |
| \(D_\Delta\) clamped | 0.35 eV | 0.346 eV | agrees ~1% |
| \(D_\Delta\) Poisson | 0.57 eV | 0.544 eV | ~5%; traced to correct \(\nu=0.6265\) vs handoff's erroneous 0.559 |
| \(\nu\) | 0.6265 | 0.559 vs 0.6265 (claimed disagreement) | handoff error; correct is 0.6265 |

**Bottom line:** Thread A's numbers were essentially correct. The handoff's two central objections were both errors: (1) the "63 meV benchmark" is a half-splitting, so \(\Delta_0\approx140\) meV does not fail it; (2) the Poisson ratio is unambiguously 0.6265. My independent replication reproduces Thread A's \(D_\Delta\) (clamped ≈0.35 eV, Poisson ≈0.57 eV) without having targeted it.
