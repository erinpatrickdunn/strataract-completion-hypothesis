# Reconstruction Master Report v1

## SCH Fermion Sector Reconstruction: Corpus Extraction, Effective Action Reconstruction, and Derivational Status Audit

*03-Reconstruction/Reconstruction_Master_Report_v1.md*

---

### Preface

This document is not a new theory. It is not a revision of SCH. It is a reconstruction of the frozen fermion sector of SCH — the action $S_{\rm geo}$ as stated in Appendix P §P.1.2 — whose purpose is to determine exactly what follows from that action, what the existing canonical documents (Appendix P, Papers A/B/C) actually document as derivation versus assertion, and what remains open. It does not determine whether SCH is physically correct or incorrect; it determines the derivational status of claims made within the frozen construction.

Every conclusion here is governed by the principles in `02-Methodology/`. Where a canonical document (04) is found to assert something not derivable from the stated action by the standards this reconstruction applies, that finding is reported as a provenance gap — not as an error in SCH's physics, and not as license to revise SCH. Revision, if warranted, is Phase II or later work, tracked separately in `05-Alternative-Constructions/`.

### Document Status

Canonical reference for Phase I of the SCH Fermion Sector Reconstruction. Editorial revision permitted without changing content; any change altering a derivation, scope statement, or conclusion is new research and belongs in a future version or in `05-Alternative-Constructions/`, not silently in this file.

---

## Part I — Reconstruction Charter

### I.1 Definition of reconstruction

**Reconstruction** is the process of recovering the minimum mathematical chain required for a claimed result from its stated foundational assumptions, while preserving every dependency, approximation, and choice encountered along that chain. Reconstruction does not mean rewriting the theory. It means making the existing derivation chain explicit enough that every claim can be traced to (a) a definition, (b) a derived step, or (c) an unlabeled assumption — and reporting honestly when the chain cannot be completed.

### I.2 Why reconstruction was performed

The SCH corpus (`04-Canonical-Theory`) makes claims of derivation — "Theorem," "Derived," "CLOSED" — about quantities built from the frozen action $S_{\rm geo}$. An audit beginning from Paper A's condensate claims repeatedly found that stated results depended on intermediate steps that were themselves unaudited: a potential form asserted without a shown Hubbard–Stratonovich transform, a Fierz completion applied silently, a regulator never specified. Each audit of a specific claim exposed a more primitive dependency. Reconstruction was undertaken to work upward from the frozen action itself, deriving what can be derived, documenting exactly what is and is not shown in the existing corpus, and reporting — rather than resolving by assumption — every point where the derivation cannot proceed without an unlabeled choice.

### I.3 Governing principles

Full texts in `02-Methodology/`. Summary:

- **Category Discipline.** Every equation is Definition (C1), Derived (C2, no skipped steps), or Hypothesis (C3, explicitly flagged).
- **Documentation Principle.** Distinguish mathematical existence, corpus documentation, and uniqueness of a derivation. Absence of documentation is not evidence of non-existence; presence of documentation is not evidence of uniqueness.
- **Scope Principle.** Every conclusion is scoped to its explicit construction. Extension to other constructions or documents requires a separate derivation, not analogy.
- **Comparability Protocol.** Before comparing two constructions: state what each computes, what is built in as definition versus approximation, and the domain on which comparison is licensed.
- **Reproducibility Standard.** Load-bearing numerical/algebraic results require a second, genuinely independent derivation route before certification.

### I.4 Scope limitations

This reconstruction covers: the frozen $S_{\rm geo}$ (Appendix P §P.1.2) in isolation, flat background, no coupling to $S_{\rm matter}$, zero temperature, homogeneous condensate ansatz. It does **not** cover: the cosmological (FLRW) reduction of §P.9 as an independent target (only its PSC-transferability is flagged as open), the chirality/Branch-2 sector of §P.7.7, or Paper C's particle-scale claims (audited only as a pass-through dependency). Governing action is frozen throughout; no revision to $S_{\rm geo}$ is proposed here.

---

## Part II — Corpus Extraction

*What the canonical documents (04) explicitly state, quoted or closely paraphrased, prior to any reconstruction judgment. Throughout this Part: "no X is derived" is avoided in favor of "no X derivation is documented within the cited proof" — the distinction this report exists to preserve.*

### II.1 Appendix P §P.1.2 — the frozen action
$$S_{\rm geo} = \int d^4x\,e\left[\frac i2\left(\bar\psi\gamma^ae^\mu_aD_\mu\psi-\text{h.c.}\right)-m\bar\psi\psi-\frac\lambda4(\bar\psi\psi)^2\right]$$
Stated without a documented derivation of the quartic coefficient's sign or magnitude beyond "$\lambda>0$ is the necessary and sufficient condition for a first-order matter-light phase transition" (Theorem 6 statement, §P.1.2 gloss).

### II.2 Theorem 0 (Appendix P) — $\eta$ as w-spin magnitude
Asserts $\eta=\bar\psi\psi$ is real and identifies it physically as w-spin magnitude. States $m_{\rm eff}^2=m^2-\lambda\eta_{\rm eq}^2/2$ "in the effective potential for the condensate field" — no effective-potential derivation is documented within Theorem 0's own proof; the formula appears at Step 3 of the stated proof with no HS transform or loop calculation shown.

### II.3 Theorem 6 (Appendix P) — matter-light phase transition
States $V_{\rm eff}(\eta)=\frac{m^2}2\eta-\frac\lambda4\eta^2+\text{higher order}$ "from the action $S_{\rm geo}$," calling this "the effective potential for the condensate order parameter $\eta$ in the mean-field approximation" (§P.1.2/Theorem 6 Step 1). No Hubbard–Stratonovich field, no fermion determinant, and no regularization scheme appear anywhere in the stated proof — none of these steps is documented within it.

### II.4 §P.11.2 (Appendix P) — tree-level potential and GMOR relation
States $V(\eta,P)=\frac{\mu^2}2(\eta^2+P^2)+\frac\lambda4(\eta^2+P^2)^2-m\eta$, "the chiral-invariant Mexican-hat potential plus the explicit chiral-breaking term already present in $S_{\rm geo}$." Derives $m_\eta^2=2\lambda\eta_{\rm eq}^2$, $m_P^2=m/\eta_{\rm eq}$ (the "SCH GMOR relation") by extremizing this stated potential. The potential's origin from $S_{\rm geo}$ is asserted; no HS transform, loop calculation, or Fierz justification for the $(\eta^2+P^2)$ completion is documented within the cited derivation.

### II.5 Paper A §2.10a / Appendix P §P.7.7 — chirality sector
States the cosmological Dirac equation "defines the transformation of $A^\mu$... as the holonomy of a connection," with the torsion self-coupling coefficient "$-\frac{3\kappa\alpha}2$" confirmed by three routes. This sector uses the *cosmological background* bilinear system (§P.9.3/§P.9.5), a separate construction from the flat-space $(\eta,P)$ potential of §P.11.2 — the two are explicitly noted (§P.7.7.3a, §P.11.5) as non-interfering, per the corpus's own statement.

### II.6 Paper C §2.1 — leptonic mass shift
Takes $\eta=\langle\bar\psi\psi\rangle$ as "the condensate vacuum expectation value" — an external input, sourced from "the mean-field condensate limit" without re-deriving $\eta_{\rm eq}$. Depends entirely on whichever value Theorem 6/§P.11.2 supply, via $m_{\rm eff}$.

### II.7 Summary of extraction
Every quantitative downstream claim in Papers A/B/C that depends on $\eta_{\rm eq}\ne0$ traces back to Theorem 6 or §P.11.2's *stated*, not *documented-as-derived*, potential forms. This is the precise target for Parts III–V.

---

## Part III — Potential Reconstruction

*[Foundation A in full — algebraic substrate — precedes this and is presented in `Notebooks/Phase-I/Fermion-Sector/` as the prerequisite Fierz system; summarized here for the potential-specific question.]*

### III.1 $V(\eta,P)$: the closed Fierz system

$$\eta^2=\tfrac15P^2-\tfrac15V^2+\tfrac15A^2-\tfrac1{10}T^2 \qquad P^2=\tfrac15\eta^2-\tfrac15V^2+\tfrac15A^2+\tfrac1{10}T^2$$
$$A^2-V^2=2\eta^2+2P^2 \qquad T^2=-6\eta^2+6P^2$$
(`Foundation-A-Closed-v1.1`; real-field convention, $\tilde P$ written $P$ throughout.)

**Scope statement:** Within the constructed Fierz-consistent bilinear system, $\eta^2+P^2$ emerges as the invariant combination under the identified chiral $SO(2)$ rotation block. This is a property of the constructed system, not an unconditional statement about every possible representation of the chiral symmetry.

### III.2 Constraints

On a homogeneous, isotropic background: $V^\mu,A^\mu$ reduce to their $u^\mu$-aligned components (only $V^0,A^0$ survive); $T^{\mu\nu}\equiv0$ (no nonzero $SO(3)$-invariant antisymmetric tensor constructible from a single vector). Parity forces $\langle P\rangle=0$ in a parity-symmetric vacuum (derived, `Notebooks/Phase-I/Fermion-Sector/`).

### III.3 Contradictions located

§P.11.2's potential imposes **equal** coefficients on $\eta^2$ and $P^2$ at quadratic order, plus an *additional* quartic term $\frac\lambda4(\eta^2+P^2)^2$ absent from $S_{\rm geo}$ and absent from the exact bosonization constructed in Part IV. This is neither the raw action ($\eta^2$ alone) nor any point on the Fierz-forced interpolation family (Part IV). Its provenance is undocumented (Documentation Principle) — not shown impossible (Scope Principle).

### III.4 Unresolved choices

Which of (at least) three inequivalent representations of the quartic term — raw ($t=0$), Fierz-forced ($t=1$ along the constructed family), or §P.11.2's symmetric completion (off the constructed family entirely) — should be extremized has never been fixed by an argument internal to $S_{\rm geo}$ anywhere in the corpus.

---

## Part IV — Fermion Sector Reconstruction

### IV.1 Hubbard–Stratonovich transformation
Exact Gaussian completion; single field $\sigma\leftrightarrow\eta$ suffices for the exact path integral. General five-channel family (any Fierz-consistent coefficient set) equally exact at the level of $Z[J]$.

### IV.2 Effective action and determinant
$D=i\partial\!\!\!/-(m+\sigma)-i\gamma^5\pi$; with $\bar M=(m+\sigma)-i\gamma^5\pi$, derived directly (not imported) that $\mathrm{Tr}\ln D=F\big((m+\sigma)^2+\pi^2\big)$, confirmed by independent explicit-matrix computation.

### IV.3 Reconstruction Finding 1 — Mean-Field Fierz Dependence
$$\left.\frac{d\Gamma_{\rm MF}}{dt}\right|_{t=0}=\frac{\sigma_0^2}\lambda \;\ne 0 \text{ whenever } \sigma_0\ne0$$
The Target-0 mean-field object is demonstrably Fierz-non-invariant. Scoped strictly to this construction (Scope Principle) — not a claim about the exact theory or about every possible bosonization. Formal claim classification (per the forthcoming `SCH_Claim_Status_Framework_v1`) to be assigned once that framework exists; provisionally: **established, construction-scoped.**

### IV.4 UV issue / cutoff requirement
$[\lambda]=-2$; $F$ is UV-divergent; no regulator is specified by $S_{\rm geo}$ or fixed uniquely by $\lambda$. This is the original, still-unresolved Target-0 halt point.

### IV.5 Link between IV.3 and IV.4
The severity of the Fierz-dependence (confined to small $t$ vs. a genuine competing vacuum) depends on $F$'s UV behavior — the two open issues are not independent.

### IV.6 Control-criterion finding
No documented control criterion for the fermion-loop/zero-boson-loop truncation exists in the audited derivation. Five candidates checked against $S_{\rm geo}$'s actual content (large $N$, weak coupling, $\hbar$/semiclassical, gradient expansion, density hierarchy) — none found to organize this specific truncation, among those examined. Target 0 never claimed one; the truncation was a scope declaration, not an approximation presented as controlled.

---

## Part V — Effective Theory Status

| Result | Reconstruction Status | Dependency |
|---|---|---|
| Closed Fierz system ($\eta,P,V,A,T$) | **Established** | Clifford algebra, explicit matrix verification |
| Exact HS bosonization (any channel) | **Established** | Gaussian completion of the frozen quartic term |
| Fermion determinant reduction | **Established**, doubly derived | HS construction + explicit-matrix cross-check |
| PSC-justified symmetric reduction (flat space) | **Established**, scope-limited | Flat-background restriction; no gravitational constraint |
| $t$-dependence of $\Gamma_{\rm MF}$ at $\sigma_0\ne0$ | **Established**, for this construction | IV.1–IV.2, envelope theorem |
| Documented control criterion for the truncation | **Not established** — none found among five checked | Search against $S_{\rm geo}$'s stated content only |
| UV-finite $\Gamma_{\rm MF}$ | **Not established** — regulator unspecified | Original Target-0 dimensional analysis |
| Theorem 6's stated potential, derived from $S_{\rm geo}$ | **Conditional / provenance undocumented** | Corpus extraction (Part II) vs. Part IV construction |
| §P.11.2's stated potential, derived from $S_{\rm geo}$ | **Conditional / provenance undocumented** — quartic term unaccounted for | Same |
| Exact theory's Fierz-invariance | **Open** | Not addressed by this reconstruction |
| Alternative construction reproducing Appendix P | **Open** | Not attempted (Phase II) |

---

## Part VI — Consequences for Canonical Documents

**Recommendation for Appendix P, Theorem 6:** Reclassify from CLOSED to **CONDITIONAL — provenance undocumented**, per `SCH_Claim_Status_Framework_v1`. This reclassification reflects that the stated label does not accurately represent the documented derivation state within the corpus, not a judgment on the underlying physics. Either supply the missing HS/determinant/regularization steps explicitly, or relabel as a phenomenological ansatz rather than a derived theorem.

**Recommendation for Appendix P §P.11.2 (GMOR):** Same reclassification. The quartic $(\eta^2+P^2)^2$ term specifically requires either a documented derivation (boson self-energy correction? separate phenomenological input?) or explicit acknowledgment that it is not obtained from $S_{\rm geo}$ by the route this reconstruction constructed.

**Recommendation for Paper A §2.10a / §P.7.7:** No change required — confirmed as a separate construction (cosmological background bilinears, not the flat-space potential), unaffected by Parts III–V's findings, consistent with the corpus's own non-interference note.

**Recommendation for Paper C §2.1:** Flag $\eta_{\rm eq}$ and $m_{\rm eff}$ as inheriting Theorem 6/§P.11.2's conditional status; no independent finding against Paper C's own derivation structure.

**General recommendation:** Adopt `SCH_Claim_Status_Framework_v1` project-wide, replacing ad hoc THEOREM/DERIVED/CLOSED labels with a vocabulary that distinguishes documented derivation from physical assertion, consistent with this reconstruction's findings.

---

*Notebook history, errata, and abandoned derivation routes filed under `03-Reconstruction/Notebooks/Phase-I/` and `03-Reconstruction/Appendices/` per project structure; not duplicated here.*

---