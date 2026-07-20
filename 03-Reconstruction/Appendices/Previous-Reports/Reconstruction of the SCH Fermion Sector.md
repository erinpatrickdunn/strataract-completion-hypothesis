# Reconstruction of the SCH Fermion Sector
## Version 2.0 — Consolidated Reference Document

*Supersedes the chronological notebook sequence (Foundations Notebooks 1–3, Notebooks A4a–A4e, B0–B2, C0–C2) as the canonical reference. Notebook history is preserved as Appendix D for provenance, not deleted. All future work cites this document by section, not by notebook number.*

---

## Part I — Constitution

**Purpose.** Fix, before any calculation, what is being derived, from what, under what approximation, and what counts as success or failure. This is Phase I: Reconstruction, not Phase II: Revision — $S_{\rm geo}$ is frozen as stated regardless of prior belief in its correctness; the goal is to test its consequences, not improve it.

**Frozen action.**
$$S_{\rm geo} = \int d^4x\, e\left[\frac i2\left(\bar\psi\gamma^ae^\mu_aD_\mu\psi-\text{h.c.}\right) - m\bar\psi\psi - \frac\lambda4(\bar\psi\psi)^2\right]$$
No other term. No $S_{\rm matter}$ coupling in this reconstruction. Gravity decoupled (flat background) unless a section states otherwise.

**Fundamental field.** The Dirac spinor $\psi(x)$ only. No internal index, no flavor/color multiplicity ($N=1$).

**Composite operators** (not fundamental, no independent meaning until derived): $\eta=\bar\psi\psi$, $P=\bar\psi\gamma^5\psi$, $A^\mu=\bar\psi\gamma^\mu\gamma^5\psi$, $J^\mu=\bar\psi\gamma^\mu\psi$.

**Category discipline.** Every equation is Category 1 (Definition), Category 2 (Derived — no skipped steps), or Category 3 (Hypothesis, explicitly flagged). Undefined status halts the derivation there.

**Documentation Principle.** Distinguish (1) mathematical existence of a derivation, (2) its explicit documentation in the corpus, (3) its uniqueness. Evidence for (2) is not evidence for (1); absence of (2) is not evidence against (1).

**Scope Principle.** Every conclusion is scoped to the explicit construction from which it was derived. Extension to other constructions, effective actions, or corpus documents requires a separate derivation, not analogy.

**Comparability Protocol** (operational corollary, governs any future cross-construction comparison). Before comparing two constructions: (i) state what object each computes; (ii) state what is built in as approximation vs. definition; (iii) establish the domain on which comparison is licensed — *before* interpreting agreement or disagreement as physics.

**Conventions.** Signature $(+,-,-,-)$; $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$; $\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3$; Dirac representation fixed explicitly (Part II); $\bar\psi=\psi^\dagger\gamma^0$; $\varepsilon_{0123}=+1$.

---

## Part II — Algebraic Foundation

**Explicit representation, Hermiticity, parity, chiral rotation:** derived directly from $2\times2$-block Dirac matrices, cross-checked in two independent ways at every step (algebraic conjugation and explicit matrix multiplication).

**Hermiticity table:**

| Bilinear | Type | Real/Imaginary |
|---|---|---|
| $\eta=\bar\psi\psi$ | scalar | Real |
| $P=\bar\psi\gamma^5\psi$ | pseudoscalar | Imaginary ($\tilde P\equiv iP$ real) |
| $V^\mu$ | vector | Real |
| $A^\mu$ | axial | Real |
| $T^{\mu\nu}$ | tensor | Real |

**Corpus flag:** Appendix P's own note ($\eta\equiv-i\bar\psi\psi$) contradicts this table's direct computation; the compensating $i$ belongs on $P$, not $\eta$. Located, not adjudicated further here.

**Parity:** $\eta$ even, $\tilde P$ odd — derived, and retroactively justifies Theorem 2's assumed parity-preserving vacuum ($\langle\tilde P\rangle=0$).

**Chiral $SO(2)$ rotation:** $(\eta,\tilde P)$ rotate as a block; $V^\mu,A^\mu$ invariant; $\eta^2+\tilde P^2$ is the invariant combination (not $\eta^2+P^2$).

**Closed Fierz system** (real fields, `Foundation-A-Closed-v1.1`, erratum applied):
$$\eta^2=\tfrac15P^2-\tfrac15V^2+\tfrac15A^2-\tfrac1{10}T^2 \qquad P^2=\tfrac15\eta^2-\tfrac15V^2+\tfrac15A^2+\tfrac1{10}T^2$$
$$A^2-V^2=2\eta^2+2P^2 \qquad\qquad T^2=-6\eta^2+6P^2$$
Verified: swap-operator formalism ($P=\frac14\sum\Gamma_A\otimes\Gamma^A$, $P^2=\mathbb1$ trivial); Clifford eigenvalues $(\mu_S,\mu_P,\mu_V,\mu_A,\mu_T)=(4,-4,-2,2,0)$; tensor sandwich eigenvalue $\lambda_T=-4$ (corrected from an initial sign error, confirmed by independent explicit-matrix computation); full involution $F^2=\mathbb1$ confirmed across all four relations simultaneously.

### Status

**Established**
✓ Clifford algebra, explicit representation, Levi-Civita convention
✓ Hermiticity table (matrix + algebraic, independently confirmed)
✓ Parity table (single derivation)
✓ Chiral $SO(2)$ block structure (single derivation)
✓ Complete Fierz system, $F^2=\mathbb1$ (double- or matrix-confirmed for every row)

**Deferred, non-blocking**
✗ Charge conjugation, time reversal (all bilinear classes)
✗ Tensor chiral-dual reality condition
✗ Canonical identities appendix (Gordon/trace compilation)

**Tag: `Foundation-A-Closed-v1.1`**

---

## Part III — Explicit Mean-Field Construction (One Scoped Object)

**Target 0** (as originally scoped): the zero-temperature, homogeneous, one-particle-irreducible effective potential $\Gamma[\eta_{\rm cl}]$, at one fermion loop, **by explicit definition — not as an approximation to a larger object.**

**HS transform:** exact Gaussian identity, single field $\sigma\leftrightarrow\eta$ suffices for the exact path integral. A general five-channel HS family (coefficients $c_S,c_P,c_V,c_A,c_T$ consistent with the Fierz constraint) is likewise exact at the level of $Z[J]$ — this is Object B, and every member computes the same partition function by construction.

**Fermion determinant, derived from $S_{\rm geo}$'s own operator** (not imported): with $\bar M=(m+\sigma)-i\gamma^5\pi$, $p\!\!\!/\bar M=Mp\!\!\!/$ exactly, giving $(p\!\!\!/-M)(p\!\!\!/+\bar M)=p^2-(m+\sigma)^2-\pi^2$. Confirmed independently by explicit rest-frame block-determinant computation. $\mathrm{Tr}\ln D=F\big((m+\sigma)^2+\pi^2\big)$.

**Symmetry reduction (PSC):** $\Gamma$ exactly $SO(3)$-invariant (trace-under-similarity argument). Auxiliary fields carry only algebraic second-class constraints (no kinetic term $\Rightarrow$ no gauge/Hamiltonian constraint). Target 0's flat-background scope removes the gravitational sector entirely, closing off the Hawking-type PSC exception. **Restricting to $V^{\rm aux}=A^{\rm aux}=T^{\rm aux}=0$ before extremizing is exact within this flat-space scope** — explicitly not shown to transfer to §P.9's constrained cosmological system.

**Central theorem (Fierz-parameter dependence):** with $\Gamma_t(\sigma,\pi)=\frac{\sigma^2}{\lambda(1-t)}+\frac{5\pi^2}{\lambda t}+F\big((m+\sigma)^2+\pi^2\big)$, exact evenness in $\pi$ makes $\pi=0$ an exact stationary point (and exact minimum for $t<t_*$) at every $t$. Envelope theorem gives, with no asymptotic gap:
$$\left.\frac{d\Gamma_{\rm MF}}{dt}\right|_{t=0} = \frac{\sigma_0^2}{\lambda}$$

**Statement, final scope:** *For the explicit Target-0 object (fermion-loop, zero-boson-loop, PSC-reduced to $(\sigma,\pi)$), a legitimate one-parameter family of exact bosonizations of the identical operator yields a stationary effective potential with nonzero leading dependence on the decoupling parameter whenever $\sigma_0\ne0$.* This is a positive counterexample to representation-independence for this specific, narrowly-scoped object — not a claim about every possible mean-field realization, nor about $S_{\rm geo}$'s exact theory.

### Status

**Established**
✓ Exact HS identity (single field, and general multi-channel family)
✓ Fermion determinant reduction, doubly derived
✓ PSC applicability, within flat-space Target-0 scope
✓ Nonzero $d\Gamma_{\rm MF}/dt|_{t=0}=\sigma_0^2/\lambda$ when $\sigma_0\ne0$

**Not established**
✗ That every legitimate bosonization exhibits this dependence
✗ That the exact (untruncated) theory is Fierz-dependent
✗ Any UV-regularized, finite value of $\Gamma_{\rm MF}$ itself

**Tag: `Foundation-B-Result-B2-v1.2`**

---

## Part IV — Provenance Audit

**Objects distinguished:** A (microscopic action) → B (exact bosonized functional) → C (truncated effective potential).

**Provenance Theorem.** For the explicit A→B→C chain constructed in this document (Parts II–III), every approximation and truncation is documented through the mean-field fermion determinant; the chain halts only at the unresolved UV regularization step. **Theorem 6 and §P.11 (Appendix P) currently do not contain a documented derivation establishing that their effective potentials arise from this same A→B→C chain.**

**Theorem 6:** asserts $V_{\rm eff}(\eta)=\frac{m^2}2\eta-\frac\lambda4\eta^2$ with no HS transform, no fermion determinant, no regularization shown — the entire B→C step is absent from its stated derivation.

**§P.11.2 (GMOR):** uses $V(\eta,P)=\frac{\mu^2}2(\eta^2+P^2)+\frac\lambda4(\eta^2+P^2)^2-m\eta$, a specific quadratic completion plus an additional quartic-in-$(\eta^2+P^2)$ term. The quartic piece is not produced by the explicit HS construction documented in Part III prior to any boson-loop approximation; its provenance within the current documented derivation remains unidentified (not: it cannot arise in any construction — only: it does not arise in this one).

**Paper C §2.1:** takes $\eta_{\rm eq}$ as external input; inherits Theorem 6/§P.11's provenance gap secondhand, introduces no independent instance.

### Status

**Established**
✓ One fully documented A→B→C chain (Parts II–III)
✓ Theorem 6 lacks a documented B→C step
✓ §P.11.2's quartic term unaccounted for within the constructed Object B

**Not established**
✗ That no construction could produce §P.11.2's potential
✗ That Theorem 6's asserted form is wrong (only: undocumented)

---

## Part V — Approximation Audit

**C1 finding:** within the documented A→B→C derivation, no explicit expansion parameter or organizing principle has been identified that justifies retaining the fermion one-loop term while neglecting boson fluctuations. The approximation hierarchy currently lacks a documented control criterion.

**C2 refinement (not an overturning of C1):** tracing the origin shows Target 0 never claimed such a criterion — its Constitution defined the fermion-loop object as the target *by declaration*, not as a truncation of a larger controlled expansion. Five candidates checked against $S_{\rm geo}$'s actual content:

| Candidate | Result |
|---|---|
| Large $N$ | Absent — $S_{\rm geo}$ has $N=1$, no internal index |
| Weak coupling in $\lambda$ | Fails — boson/fermion loop ratio doesn't organize in powers of $\lambda$ as constructed |
| $\hbar$/semiclassical | Standard mechanism requires the same $N$-suppression absent above |
| Gradient expansion | Addresses a different question (field homogeneity), not loop ordering |
| Density hierarchy ($\varepsilon(\rho)\le10^{-23}$) | Genuine, present in corpus, but controls Term 3 vs. Term 2, not boson vs. fermion loops |

**Two notions of completeness**, introduced as reusable vocabulary: (1) complete effective action (all orders/all fluctuations), (2) complete within declared scope. Much of the apparent tension between this reconstruction and the corpus arises from checking documents built for notion (2) against the standard of notion (1).

### Status

**Established**
✓ No documented control criterion in the audited derivation (C1)
✓ Target 0 never claimed one — declared scope, not truncated approximation (C2)
✓ Five standard organizing principles checked and found inapplicable, among those examined

**Not established**
✗ That no organizing principle exists for $S_{\rm geo}$
✗ Whether Fierz/UV pathologies are fundamental or truncation artifacts (explicitly open)

---

## Part VI — Established Foundations (Summary)

| Foundation | Core result | Status |
|---|---|---|
| A | Algebraic substrate for the SCH fermion sector | **Closed** (`v1.1`) |
| B | Target-0's scoped object is Fierz-non-invariant | **Closed for this construction** |
| C0 | One documented A→B→C chain; corpus provenance gaps located | **Established** |
| C1 | No documented control criterion in the audited derivation | **Established** |
| C2 | Target 0 never claimed one; five candidates checked and found inapplicable | **Established** |

---

## Part VII — Open Questions (Roadmap)

1. **Alternative A→B→C chain** (Path 2): CJT/2PI, large-$N$ generalization, or other construction — to be compared against Part III's object only via the Comparability Protocol.
2. **UV completion / regulator choice**: unresolved since Target 0's original halt (Constitution §5).
3. **Fierz restoration**: does including boson fluctuations (a genuinely different approximation order, not attempted here) restore representation-independence?
4. **Corpus repair**: Theorem 6 and §P.11 require either a documented derivation from $S_{\rm geo}$ or explicit relabeling as phenomenological ansätze.
5. **Foundation A residuals**: C/T classification, tensor chiral-dual reality, canonical identities appendix.
6. **Cosmological transfer**: whether Part III's PSC argument (flat-space-dependent) can be redone for §P.9's actual constrained FLRW system.

---

## Appendix D — Notebook History

Preserved in full as the chronological lab record (Foundations Notebooks 1–3; A4a–A4e; B0–B2; C0–C2; all errata and corrections, including `Foundation-A-Closed-v1.0`→`v1.1`). This document (v2.0) is the canonical reference; the notebooks are retained for provenance and are not to be cited in place of the corresponding sections above.
