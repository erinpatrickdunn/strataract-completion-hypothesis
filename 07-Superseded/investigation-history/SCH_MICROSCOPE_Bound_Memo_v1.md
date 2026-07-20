# Memo: The Laboratory/Precision-Gravity Audit of SCH — MICROSCOPE Bound, Screening Escape Routes, and the Structural Conclusion

**Status: Working estimate, order-of-magnitude to low-precision on the numeric bound (§2); the structural arguments (§4–§7) are conclusions about what SCH's own stated action does and does not permit, not new experimental results. Not a substitute for a formal derivation at every step, but sufficient to answer the scoping questions the team raised: is there a real existing-data constraint, is the calibration story internally consistent, and does any screening/escape mechanism survive contact with the theory's own mathematics?**

*Prepared using SCH's own literal formulas (Paper A §2.3, §6.4; Paper B §6.2–6.3; Appendix P Theorem 0, §P.1.3, §P.11.2) and public data: MICROSCOPE final results and mission documentation, standard nuclear-structure values, and the published screened-scalar-field literature.*

---

## 1. Motivation

The team's calibration programme depends entirely on the Bi-209 → Pb-208 transmutation experiment (Paper A §5) to fix α and m_eff — a measurement that has not been run and that no one outside the project is likely to run. Before investing further theory effort gated on that experiment, this memo asks a narrower, answerable question:

**Does data that already exists already constrain α, using SCH's own stated formulas?**

The answer is yes. SCH's composition-dependent coupling η(Z,N) (built from nuclear deformation parameters β₂, β₄) is exactly the kind of quantity that Weak Equivalence Principle (WEP) tests are designed to catch. The MICROSCOPE satellite mission already ran the relevant experiment, to extraordinary precision, using two of the most common materials in modern precision metrology (Ti and Pt alloys) — and got a null result.

This memo has two tracks, run separately as requested:

- **Track 1** — take SCH's formulas literally and derive a numeric bound on α from MICROSCOPE's public result.
- **Track 2** — a separate audit of whether the Bi-209 calibration experiment's design rationale is even consistent with SCH's own definition of η(Z,N).

---

## 2. Track 1 — The MICROSCOPE Bound on α

### 2.1 Method and definitions (explicitly not given by SCH's own text — filled in here, flagged as such)

SCH defines η(Z,N) qualitatively as a nuclear "geometric coupling efficiency" that vanishes for spherical/doubly-magic nuclei and grows with deformation, via a formula built from β₂, β₄ (Paper A §2.3). No normalized functional form is given anywhere in the corpus. For this estimate we use the simplest reading consistent with the stated intent:

> **η(Z,N) ≡ β₂(Z,N)² / β₂(Bi-209)²** — i.e., deformation-squared, normalized so that η(Bi-209) ≡ 1, matching the framework's own claim that Bi-209 represents its calibration/maximum-contrast point.

The predicted MICROSCOPE (Eötvös parameter) signal is:

> **η_Eöt ≈ α · X · Δη(material A, material B)**

where X is the fraction of the coupling that actually tracks composition-dependent mass content — this is the mass-coupling ambiguity flagged previously in Paper C §2.1, never resolved in the source documents. Two branches are carried through in parallel:

- **Branch M (nucleon/atomic-mass coupling):** X = 1 — the correction scales with the full physical nucleon mass.
- **Branch q (quark-mass-content coupling):** X ≈ (2m_u+m_d)/m_nucleon ≈ 9 MeV / 938 MeV ≈ 0.0097 — the correction scales only with the current-quark mass actually carried inside the nucleon.

### 2.2 Reference point: Bi-209

Bi-209's measured deformation is <span title="cited">weakly oblate with near-constant deformation of β₂ ≈ -0.15</span> (ISOLDE Coulomb-excitation measurements). This gives the calibration point β₂²(Bi-209) = 0.0225.

**Note:** Bi-209's experimental selection in Paper A §5.1 is justified by its large nuclear *magnetic moment* (a single-particle spin effect from the unpaired h9/2 proton), not by its deformation. Its actual β₂ value is modest — see Track 2 below for why this matters.

### 2.3 Pass A — natural elements, order of magnitude

Using natural isotopic abundances and representative literature deformation values for Ti and Pt isotopes:

| Isotope mix | ⟨β₂²⟩ | η_eff (norm. to Bi-209) |
|---|---|---|
| Ti (natural) | ≈0.0184 | ≈0.82 |
| Pt (natural) | ≈0.0193 | ≈0.86 |

Δη(Pt, Ti) ≈ 0.042.

Combined with MICROSCOPE's measured null result, η_Eöt(Ti/Pt) = **(-1.5 ± 2.7) × 10⁻¹⁵**:

| Branch | Bound on α |
|---|---|
| M (nucleon-mass) | α ≲ 7 × 10⁻¹⁴ |
| q (quark-mass) | α ≲ 7 × 10⁻¹² |

### 2.4 Pass B — actual flown alloy compositions

Confirmed MICROSCOPE compositions (primary mission documentation):

- **PtRh10** (SUREF and the heavy SUEP mass): <span title="cited">90% Pt (A=195.1, Z=78), 10% Rh (A=102.9, Z=45) by mass</span>.
- **TA6V** (light SUEP mass): <span title="cited">90% Ti (A=47.9, Z=22), 6% Al (A=27.0, Z=13), 4% V (A=50.9, Z=23) by mass</span>.

Alloying-element deformation values used (mass-fraction weighted):

| Element | Mass fraction | β₂ used | Basis |
|---|---|---|---|
| Ti (natural) | 90% (TA6V) | ⟨β₂²⟩=0.0184 | natural-abundance weighted, literature |
| **Al-27** | 6% (TA6V) | β₂≈0.31, β₂²≈0.096 | derived from measured Q=0.14 barn via rotational-model conversion (see caveat below) |
| V-51 | 4% (TA6V) | β₂≈0.05, β₂²≈0.0025 | N=28 shell closure → expected weakly deformed; representative, not individually sourced |
| Pt (natural) | 90% (PtRh10) | ⟨β₂²⟩=0.0193 | natural-abundance weighted, literature |
| Rh-103 | 10% (PtRh10) | β₂≈0.20, β₂²≈0.04 | A~103 transitional region; representative, not individually sourced |

**Caveat on Al-27 (the single largest driver of the alloy-level result):** its β₂ is obtained by converting the *measured* electric quadrupole moment (Q = 0.14 barn, I=5/2 ground state) to an intrinsic deformation via the standard rotational-model (strong-coupling, K=I) relation. That model is well-justified for heavy collectively-deformed nuclei; it is a real stretch for Al-27, a light, single-particle sd-shell nucleus normally treated in shell-model terms. Treat β₂(Al-27)≈0.31 as an effective, model-dependent number, not a settled collective measurement — the softest input in this whole calculation.

**Alloy-level η_eff (mass-fraction weighted):**

- η_eff(TA6V) = 0.90(0.0184) + 0.06(0.096) + 0.04(0.0025) = 0.0224 → **≈1.00**
- η_eff(PtRh10) = 0.90(0.0193) + 0.10(0.04) = 0.0214 → **≈0.95**

Δη(TA6V, PtRh10) ≈ **0.05**

### 2.5 Final bound table

| Coupling reading | η_eff TA6V | η_eff PtRh10 | Δη | MICROSCOPE bound on α |
|---|---|---|---|---|
| Branch M (nucleon-mass) | 1.00 | 0.95 | 0.05 | **α ≲ 5 × 10⁻¹⁴** |
| Branch q (quark-mass) | 1.00 | 0.95 | 0.05 | **α ≲ 5 × 10⁻¹²** |

### 2.6 Robustness check

The bound was recomputed three times with successive refinements: naive natural elements → alloys with a placeholder Al-27 value → alloys with an Al-27 value derived from a real measured quadrupole moment. Across all three, the result stayed anchored between **~10⁻¹⁴ and ~10⁻¹² depending on the mass-coupling branch**, moving by at most a factor of ~4 at any step. This is not a fragile result hanging on one shaky input.

**Conclusion of Track 1:** Even under the more permissive branch (quark-mass coupling), MICROSCOPE's existing public data already constrains SCH's α to below ~10⁻¹². This is a real, order-of-magnitude-robust result using only public data and the framework's own stated formulas — no new experiment required, and no waiting on Bi-209.

**What this bound would need to be checked against:** whether α ~ 10⁻¹² (or 10⁻¹⁴) is still large enough to produce the galactic-scale phenomenology claimed in Papers A/B. That comparison has not yet been done and is a natural next step — see Section 4.

---

## 3. Track 2 — Bi-209 Calibration Consistency Audit

This is deliberately kept separate from the numeric bound, per the team's request, because it's a conceptual/definitional finding rather than a calculation.

**The finding:** SCH's Bi-209 experimental design and SCH's theoretical definition of η(Z,N) are built from two different nuclear observables that do not track each other.

- The Bi-209 experiment is justified in Paper A §5.1–5.2 by Bi-209 having the largest nuclear magnetic moment of any stable nucleus — a single-particle effect from one unpaired proton in a high-j (h9/2) orbital outside the N=126 magic shell.
- SCH's actual formula for η(Z,N) (Paper A §2.3) is built from **collective deformation** parameters (β₂, β₄) — a different, unrelated nuclear property.
- Bi-209's real deformation is β₂ ≈ -0.15 (sourced above) — a modest, unremarkable value, **not** a "maximum contrast" configuration by the deformation metric.

**Consequence for the calibration logic:** on the literal deformation-based reading of η, Bi-209 is not uniquely large — it's comparable to, or in this analysis's Pass B result, slightly *smaller than*, ordinary lab alloys already flown in MICROSCOPE (η_eff(Bi-209)≡1.0 vs. η_eff(TA6V)≈1.00, η_eff(PtRh10)≈0.95). **This means MICROSCOPE is not an off-axis or tangential test relative to what the Bi-209 experiment probes — it is sampling essentially the same part of η-space.**

If the team's internal mental model has been "Bi-209/Pb-208 spans the interesting range of η, and ordinary lab materials sit near zero," that model is false under SCH's own stated formula. This needs to be resolved (or the η(Z,N) formula needs to be revised/re-specified) before the Bi-209 experimental design can be described as sound, independent of whether the experiment ever gets funded.

---

## 4. Does "Screening" Rescue SCH from the Track 1 Bound? (Reading 2 Audit)

The Track 1 bound only bites if SCH's coupling behaves the same way in dense terrestrial matter as it's assumed to elsewhere. A natural objection: what if the effect is environment-suppressed in ordinary lab-density matter (the same logic as chameleon/symmetron dark-energy screening), and only "turns on" in some other regime? This section tests that objection directly against SCH's own stated potential, rather than leaving it as an assertion.

### 4.1 Chameleon-style (linear density coupling)

Grafting the standard chameleon interaction β(ρ/M)η onto SCH's existing potential (Appendix P §P.11.2: V(η,P) = (μ²/2)(η²+P²) + (λ/4)(η²+P²)² − mη) only *tilts* the existing minimum — it doesn't reproduce the runaway-potential structure that gives real chameleon theories their many-orders-of-magnitude mass shift between vacuum and lab density. **Chameleon screening does not fall out of SCH's existing action.** Producing it would require replacing the quartic potential with a genuinely different (runaway) potential — a different theory, not a reading of the current one.

### 4.2 Symmetron-style (quadratic density coupling)

Replacing μ² → μ²_eff(ρ) = μ² + ρ/M² is a clean, structurally compatible modification of SCH's existing Mexican-hat potential: at low (galactic) density the field sits in its broken-symmetry vev; above a critical density ρ*, symmetry is restored and η_eq is driven toward zero. **This is mathematically viable** — unlike the chameleon case — but it requires introducing a wholly new coupling constant M that exists nowhere in S_geo or any version of Appendix P.

**The decisive problem:** Bi-209, in the proposed calibration experiment, is a solid metal target at ordinary terrestrial bulk density — the same order of magnitude as MICROSCOPE's Ti/Pt test masses. A single scalar critical density ρ* cannot distinguish "MICROSCOPE's alloy" from "the Bi-209 target": both are ordinary terrestrial solids. Whatever ρ* is tuned to suppress η enough to hide from MICROSCOPE necessarily suppresses η by the same factor at the Bi-209 target, directly from the same μ²_eff(ρ) formula — not as a numerical accident, but as a structural consequence of using density as the sole screening variable.

**Conclusion:** density-based screening (chameleon or symmetron) either doesn't emerge from SCH's action at all, or emerges but is self-defeating — it saves MICROSCOPE only by disabling SCH's own proposed calibration experiment at the same order of magnitude.

---

## 5. Does a Macroscopic Spin/Coherence Channel Survive Instead? (Channel 2 Audit)

A further objection: what if the relevant environmental variable for screening isn't density at all, but something more native to SCH's own vocabulary — "organized rotational coherence," i.e. the axial current A^μ — and Bi-209's spin structure (I=9/2, one unpaired proton) distinguishes it from MICROSCOPE's materials in a way density does not?

This requires first asking whether A^μ mediates any macroscopic long-range interaction at all, before comparing to any experimental bound.

**Finding: it does not, by the framework's own cited formalism.** Appendix P §P.1.3 states that torsion is *algebraically* determined by the Cartan equation — "there is no differential propagation equation for torsion" — a standard feature of Einstein-Cartan gravity (Hehl et al. 1976, cited elsewhere in the corpus) in which torsion has no kinetic term and is therefore non-dynamical. Solving the Cartan equation and substituting back into the Dirac equation produces a **contact** (zero-range) four-fermion interaction between spin densities at the same point, not a field that propagates between separated bodies. This is independently consistent with the corpus's own description of Term 3 elsewhere (§P.7.1): repulsive pressure "when matter with aligned chirality **overlaps**" — contact language, not long-range-force language. S_geo also contains no independent axial four-fermion self-interaction term that could carry a long-range signal by a different route; the only self-interaction present is the scalar quartic (λ/4)(ψ̄ψ)².

The one place A^0 does reach beyond a point is through κα(A^0)² sitting inside the ordinary stress-energy tensor, sourcing gravity via the standard Einstein equation — but this is gravitational-strength, inherits the same ε≤10⁻²³ density suppression already assigned to Term 3 at ordinary densities elsewhere in Appendix P, and is a Track-1-style question (not a new spin-force channel).

**Precise statement of the finding:** The current action does not derive a propagating axial interaction. Under the Einstein–Cartan structure explicitly cited by the framework, torsion is algebraically constrained to the local spin density and therefore does not mediate an independent long-range force. Consequently, **existing long-range spin-force experiments (Eöt-Wash, comagnetometers, SQUID searches) are not direct tests of the current SCH action** — not because SCH passes them, but because the current action does not make the kind of claim those experiments are built to test.

(Separately: the original Bi-209 proposal's Channels A–C are coincidence-triggered on individual transmutation events, not on bulk statistical polarization, so the question of whether ordinary bulk bismuth metal has net macroscopic polarization does not actually threaten the original local-event proposal — it only closes off the idea of comparing that proposal against archival bulk-matter spin-force data.)

---

## 6. Structural Clarification: Three Distinct Objects Being Conflated

Across the framework's revision history, three physically distinct objects have often been discussed as if interchangeable. This audit's process of elimination has separated them cleanly:

1. **Einstein-Cartan torsion** (the axial current sourcing the Cartan equation) — algebraic, local, non-propagating, contact-only. Established, per §5 above.
2. **The propagating Appendix P condensate fields** (η, P, δη, δP) — these have genuine wave equations, dispersion relations, and effective masses (Theorem 4a/4b), and are the only sector capable of carrying a signal beyond a point.
3. **The effective stress-energy tensor** (C_μν = ρηu_μu_ν, or the full T_μν^(η,P,A)) — affects physics only through the standard Einstein field equation, at ordinary gravitational strength.

The intuitive chain implicitly assumed in earlier drafts — spin → torsion → long-range effect → galactic phenomenology — breaks at the second step: local torsion is a contact interaction and stops there. Any long-range behavior in the framework comes only through the condensate sector (object 2) or through gravitational sourcing (object 3), never through torsion itself.

---

## 7. General Structural Conclusion

Throughout this audit, every proposed mechanism capable of generating cosmological or macroscopic laboratory signatures has reduced to one of three sectors: (i) local Einstein-Cartan torsion, which is algebraically constrained and non-propagating; (ii) propagating condensate modes, whose currently derived dynamics either dilute as matter or screen on laboratory/cosmological scales; or (iii) the effective gravitational stress-energy tensor, which contributes only through the standard Einstein equations. No additional propagating degree of freedom presently derivable from S_geo has been found. Consequently, every candidate route investigated to date — transport, background evolution, growth of structure, density screening, and macroscopic spin interactions — either terminates structurally or reduces to a previously analyzed sector. **The remaining untested prediction of the framework is therefore confined to the explicitly proposed local Bi-209 coincidence experiment, rather than any existing astrophysical or precision-gravity dataset.**

This is not a list of isolated negative results. It is the discovery of a single organizing fact about what the current action does and does not permit: the theory's propagating sector is far more restricted than earlier drafts assumed, and nearly every apparent "new route" investigated in this audit was, in one form or another, an attempt to promote a local object into a long-range one.

---

## 8. Resolving the Fork: Does the WEP Bound (Track 1) Even Apply?

Track 1's numeric bound assumed a falling test mass feels an extra acceleration proportional to α·∇η(x) — the standard scalar-tensor "fifth force" derivation. That derivation is only valid if η is a genuine background *field* with position dependence. Whether that's actually what SCH's η is turns out to be ambiguous in the corpus itself, and the ambiguity is load-bearing: it determines whether MICROSCOPE is even the correct comparator.

### 8.1 The parameter-vs-field distinction

Extremizing S = −∫m_eff(x)dτ with m_eff(x) = m(1+αη(x)) gives, to leading order:

**a^μ = −α(g^μν+u^μu^ν)∇_νη**

This term depends only on the *gradient* of an ambient field, not on the falling body's own mass or structure — i.e., it is automatically species-universal (a stronger version of the team's original "Case C," forced by the functional form itself rather than a coincidence).

But this only applies if η(x) is a field with a value at every point in space. **Paper A §2.3 writes η = η(Z,N)** — a static coefficient computed from a specific nucleus's own deformation, not a function of position at all. Under that reading, ∇η is not defined; there is no force term in the falling body's equation of motion; the only place η(Z,N) enters physics is as a source term in Q_μν = ρηu_μu_ν, i.e., how strongly the body *sources* gravity for something else — not how it responds to an external field.

Paper C §2.1, by contrast, explicitly treats η as ⟨ψ̄ψ⟩, a condensate field with its own potential, equation of motion, and vacuum expectation value. The corpus uses both without ever stating that they're related, let alone how (this is the CT-xxv gap, now shown to be load-bearing rather than a documentation nicety).

### 8.2 If η is a field (Picture 2): the WKB force is universal, but P.12 already screens it out of range

Even granting the field reading, Appendix P's own P.12 calculation gives λ_coh = ħ/(m_eff c) ≈ 0.1 m at the framework's stated m_eff (~10⁻⁶ eV) — a number already used self-consistently throughout the corpus, not a new assumption. Outside its sources, a field of this mass falls off as e^(−r/λ)/r. At Earth's radius (~6.4×10⁶ m), r/λ ≈ 6.4×10⁷ — the field is suppressed by a factor of e^(−6.4×10⁷), i.e., completely absent at satellite altitude. **This is a different and more mundane mechanism than the chameleon/symmetron screening tested in §4 — it requires no new density-dependent physics, only the mass scale the corpus already committed to.**

Consequence: under Picture 2, MICROSCOPE genuinely doesn't apply — not because the force is screened by density, but because there's no residual field left at orbital separation at all. The correct comparator shifts to **short-range Yukawa / inverse-square-law tests** (Eöt-Wash-type torsion balances, sensitive from micrometers to ~meters), which is exactly the range λ_coh sits in. This has not been calculated in this memo; it is the natural next step if Picture 2 is judged the correct reading.

### 8.3 If η is a static parameter (Picture 1): the correct test isn't WEP at all — it's active/passive mass equivalence

If η(Z,N) only modifies how strongly a nucleus sources gravity without a matching change to how it responds to gravity, that is precisely a violation of the **equivalence of active and passive gravitational mass** (Bondi's distinction) — a principle distinct from WEP, with its own dedicated experimental lineage:

- **Kreuzer (1968):** Cavendish-type torsion balance, Teflon (F) vs. density-matched dibromomethane/trichloroethylene (Br) — bound of **5×10⁻⁵** on the active/passive mass ratio difference.
- **Bartlett & Van Buren (1986):** lunar orbit asymmetry (Fe-rich core vs. Al-rich crust) — bound of **~4×10⁻¹²**.
- **Singh et al. (2023):** full modern lunar-laser-ranging dataset — bound of **3.9×10⁻¹⁴**, ~100× tighter than 1986.

**Running the same style of calculation as Track 1** (representative β₂-derived η(Z,N) for F, Br, Fe, Al — flagged as softer-sourced than Ti/Pt, since F-19 (I=1/2) and Fe-56 (I=0) have no measurable static quadrupole moment by angular-momentum selection rules, and would properly require B(E2)-systematics rather than the static-moment method used elsewhere in this memo):

| Test | Δη (representative) | Experimental bound | Branch M (α≲) | Branch q (α≲) |
|---|---|---|---|---|
| Kreuzer (F/Br) | ≈3.0 | 5×10⁻⁵ | 1.7×10⁻⁵ | 1.7×10⁻³ |
| Lunar (Fe/Al, 2023) | ≈2.5 | 3.9×10⁻¹⁴ | 1.6×10⁻¹⁴ | 1.6×10⁻¹² |

**Notable cross-check:** the modern lunar bound lands at essentially the same order of magnitude as the Track 1 MICROSCOPE bound (10⁻¹⁴/10⁻¹² across both mass-coupling branches), despite using entirely different elements, a different underlying principle, and a different measurement technique across independent decades-long programs. Picture 1 is constrained just as hard as Picture 2 was — by a completely separate line of public evidence.

### 8.4 Summary table

| Reading | What η is | Force on falling body | Correct comparator | Outcome |
|---|---|---|---|---|
| Picture 1 | static η(Z,N), source-only | none (no ∇η) — but sources Q_μν asymmetrically | Kreuzer / lunar-laser-ranging (active-passive mass) | **Constrained to α≲10⁻¹²–10⁻¹⁴, same order as Track 1** |
| Picture 2 (as P.12's m_eff implies) | dynamical field, λ_coh≈0.1 m | universal, but field vanishes beyond ~0.1 m | short-range Yukawa/torsion-balance tests, not MICROSCOPE | MICROSCOPE inapplicable; different existing constraint applies instead, not yet computed here |
| Picture 2 with much lighter m_eff | dynamical field, long-range | universal, MICROSCOPE-scale | MICROSCOPE | Would require contradicting P.12's own adopted number |

**The upshot:** there is no reading of η — field or parameter — that escapes a tight, existing, public constraint. The two live branches (Picture 1 via Kreuzer/LLR, Picture 2 via MICROSCOPE at face value) both land in the same α≲10⁻¹²–10⁻¹⁴ range; the one branch that would evade MICROSCOPE specifically (Picture 2 at short range) still needs to be checked against short-range Yukawa tests before it can be called safe.

---

## 9. Recommended Next Steps

1. **Settle whether η is Picture 1 or Picture 2 as an explicit modeling decision** (the CT-xxv gap) — this determines which of the two branches in §8.4 is the operative one, though both are already tightly constrained.
2. **Compare whichever bound applies (≲10⁻¹² to 10⁻¹⁴) against what α would need to be** to produce the claimed galactic-scale gravitational phenomenology (C_μν sourcing, Papers A/B). If the galactic phenomenology requires α orders of magnitude larger than any of these bounds allow, that is a direct tension the team needs to confront regardless of which picture is chosen.
3. **If Picture 2 is chosen, run the short-range Yukawa/torsion-balance comparison** (§8.2) rather than treating MICROSCOPE as dispositive — this has not yet been done.
4. **If Picture 1 is chosen and a tighter number is wanted for the Kreuzer/lunar test**, pull B(E2)-derived deformation values for F-19 and Fe-56 rather than the representative values used in §8.3, since the static-quadrupole-moment method doesn't apply to either nucleus.
5. **Resolve the mass-coupling ambiguity (Branch M vs. Branch q)** as an actual modeling decision internal to SCH — this changes every bound in this memo by roughly two orders of magnitude and is currently unspecified in Paper C §2.1.
6. **Either fix or reconcile the η(Z,N) definition** given the Track 2 finding — if Bi-209 is meant to represent a true "maximum contrast" configuration, the formula needs to reflect the single-particle/spin structure that actually motivated its selection, not collective deformation.
7. **If SCH wants to keep a screening escape route alive**, it must be built from the condensate sector rather than from torsion or an imported chameleon/symmetron density term — and must independently satisfy Bi-209 survival, existing atom-interferometry bounds, and galactic-scale un-screening simultaneously (§4, §7). This is a substantial new-physics proposal, not a reading of the current text.
8. **If a tighter Track 1 number is wanted:** pull primary-source β₂ values for V-51 and Rh-103 (currently representative, not individually sourced) — though the sensitivity analysis suggests this is unlikely to move the final bound by more than a factor of a few.

---

*Memo prepared from public data: MICROSCOPE final WEP test results; MICROSCOPE mission design/composition documentation (PtRh10, TA6V); ISOLDE Coulomb-excitation measurement of Bi-209 deformation; standard nuclear data for Ti, Pt, Al-27 isotopes; the chameleon/symmetron screened-scalar literature (Hamilton et al. 2015; Burrage & Sakstein reviews) used only to check whether SCH's action can reproduce these mechanisms, not as a claim that SCH is such a theory; Kreuzer (1968), Bartlett & Van Buren (1986), and Singh et al. (2023) on active/passive gravitational mass equivalence. All SCH-side formulas and parameters as stated in Paper A, Paper B, Paper C, and Appendix P v15/v16.*
