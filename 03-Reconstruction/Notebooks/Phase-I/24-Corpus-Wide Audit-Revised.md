# Corpus-Wide Audit — Revised, With Evidentiary Boundaries Made Explicit

*Adopting all three of your reclassifications and the reframed overall conclusion. This is `Foundation-B-Audit-v1.0`.*

## 1. Theorem 6

**Adopted verbatim:** Theorem 6 does not document the derivation of its stated mean-field effective potential from the frozen action $S_{\rm geo}$. Consequently, the provenance of that potential is incomplete within the current corpus.

This is the correct scope. What the audit can establish is a documentation gap in the corpus as written, not a claim about whether a valid derivation exists somewhere unstated. And per your later point, I'm replacing my earlier phrasing ("Theorem 6 never performed the calculation") with **"the current corpus does not document the derivation of Theorem 6's effective potential from the frozen action."**

## 2. §P.11 (GMOR)

**Adopted, with the overreach removed.** I had called $V(\eta,P)=\frac{\mu^2}2(\eta^2+P^2)+\frac\lambda4(\eta^2+P^2)^2-m\eta$ "a third representation," which implicitly asserted a specific relationship (inequivalence to both the raw action and the Fierz-forced form) that I have not actually proven — I only observed it *doesn't visually match* either. That's a weaker fact than "it's a distinct, unmotivated point," since I haven't ruled out it being, e.g., a phenomenological NJL-inspired ansatz introduced with a different justification never stated, or an effective potential arising after some other reduction not documented in §P.11 itself. Corrected conclusion, adopted as stated: **the relationship between the §P.11 effective potential and the frozen quartic interaction has not been explicitly demonstrated within the corpus.**

## 3. Paper C

Unchanged — this was already scoped correctly as a pass-through dependency, not an independent finding.

## Revised overall conclusion — the three-part decomposition

Replacing the compressed "the ambiguity propagates into the parts that matter most" with the unpacked version:

1. **B2 establishes that at least one legitimate mean-field realization of $S_{\rm geo}$'s quartic term is representation-dependent.** (Established directly, in this reconstruction.)
2. **Theorem 6 and §P.11 do not currently document why the particular effective potential they employ is the uniquely appropriate realization of the frozen interaction.** (Established as a documentation fact about the corpus, independent of whether B2's specific finding is what ultimately explains the gap.)
3. **Therefore the provenance linking $S_{\rm geo}$ to those downstream potentials is presently incomplete.** (Follows from 1+2 as a logical conclusion, without requiring the claim that Theorem 6 or §P.11 are wrong.)

This is the correct evidentiary structure: (1) and (2) are independently supported findings from different parts of this reconstruction; (3) is what follows from holding them together, and no stronger.

## Reorganizing Foundation C accordingly

Adopting your C0/C1/C2 ordering in place of my original "add bosonic fluctuations" framing:

**C0 — What is the correct effective bosonic theory implied by the frozen action?**
This is the provenance question directly raised by finding 2 above: attempt an honest derivation of *a* bosonized effective potential from $S_{\rm geo}$ (following Target 0/B0–B2's machinery, which is now solid), and compare what emerges against both Theorem 6's bare form and §P.11's symmetric-completion form — not to declare either right or wrong, but to establish, for the first time in this corpus, an actual documented derivation chain from action to potential that can be checked.

**C1 — What approximation should be applied?**
Only after C0 produces *a* candidate potential does it make sense to ask whether the mean-field/one-loop order used throughout this reconstruction is adequate, or whether B2's demonstrated representation-dependence means a boson-fluctuation correction (the original B3 idea) is actually necessary at this stage rather than optional refinement.

**C2 — What vacuum emerges?**
Only after C0 and C1 are settled does asking "does $\eta_{\rm eq}\ne0$, and does it look like Theorem 6's claimed condensate" become a well-posed question rather than a premature one.

## Status

`Foundation-B-Audit-v1.0` is frozen with the corrections above. The reframing you've proposed is accepted as the correct next organizational structure: **the central open question shifts from "how do we improve the mean-field calculation" to "what effective potential is actually implied by the frozen microscopic interaction, and what assumptions are required to obtain it" — and that question is now C0, the opening item of Foundation C, rather than a bosonic-loop extension of Foundation B.**

Ready to open C0 when you are.
