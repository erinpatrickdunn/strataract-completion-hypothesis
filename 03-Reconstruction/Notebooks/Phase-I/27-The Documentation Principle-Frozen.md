# The Documentation Principle, Frozen

**Documentation Principle.** When auditing a theoretical derivation, distinguish: (1) the mathematical existence of a derivation, (2) the explicit documentation of that derivation in the corpus, and (3) the uniqueness of that derivation. Evidence for (2) is not evidence for (1), and failure to establish (2) is not evidence against (1).

This is adopted as a standing rule for the remainder of the reconstruction, carried forward the same way Foundation A's category tags are. It names precisely the move that went wrong in the C0 correction and gives future notebooks a one-line check before asserting any impossibility claim.

---

# C1: Internal Consistency of the Approximation Sequence

## Objective, adopted as stated

Determine whether the approximation sequence used in the documented A→B→C derivation is internally self-consistent for the questions the corpus asks of it, decomposed into three logically independent branches: representation dependence, loop ordering, and regularization.

## Branch 1 — Representation dependence

**[C2, established, Foundation B]** The one-fermion-loop, zero-boson-loop truncation does not preserve exact Fierz equivalence: $d\Gamma_{\rm MF}/dt|_{t=0}=\sigma_0^2/\lambda\ne0$ whenever $\sigma_0\ne0$. Per the Documentation Principle, this shows non-invariance for *this* truncation on *this* constructed family — it does not show every truncation fails, and does not show no truncation could succeed.

## Branch 2 — Loop ordering

**[C2] — this can actually be checked directly, not just asserted, using machinery already built.** The question "are omitted boson fluctuations parametrically controlled, or merely omitted?" has a standard diagnostic: compare the scale at which the boson-loop correction to $\Gamma_{\rm MF}$ enters against the scale of the terms already kept. The boson quadratic term is $\sigma^2/\lambda$; a one-boson-loop correction to $\Gamma$ from integrating over $\sigma$-fluctuations around the saddle goes schematically as $\frac12\ln\det[\lambda^{-1}+F''(M^2)\cdot(\ldots)]$ — this has **no small parameter controlling it relative to the tree/fermion-loop terms already kept**, unlike, say, a large-$N$ expansion where boson loops are suppressed by $1/N$ relative to the fermion loop. **Nothing in $S_{\rm geo}$ as frozen supplies such a parameter** — there is no flavor or color multiplicity $N$ anywhere in the single-fermion action (Constitution §2: "the only fundamental dynamical field... is the Dirac spinor $\psi(x)$," singular, no internal index). This is a genuine, checkable finding, not an assumption: **the loop ordering used throughout Target 0/B1/B2 is not parametrically controlled by anything internal to $S_{\rm geo}$.** It is an *ad hoc* truncation order (keep fermion loop, drop boson loop), not a controlled expansion, unless and until such a parameter is separately introduced (e.g., some future extension including multiple fermion flavors) — and no such parameter is stated anywhere in the corpus.

## Branch 3 — Regularization

**[C2, established, Target 0 §5]** The effective potential cannot be defined as a specific function without a regulator/renormalization choice; $[\lambda]=-2$ forces this. Unresolved, as originally flagged, and unaffected by anything since.

## Testing your hypothesis: do the branches collapse onto a common origin?

This is the sharp, checkable question you posed, and I want to test it rather than assume it.

**[C2] — partial collapse, one direction confirmed.** Recall from B2 §6 (the "residual item" flagged there): the pseudoscalar branch's existence/stability depends on the sign of $10/(\lambda t)+2F'(M^2)$ at large $M^2$ — i.e., on the **UV behavior of $F$**, the same function whose divergence structure is exactly Branch 3's unresolved regulator question. **This is a real, demonstrable link between Branch 1 and Branch 3**: whether the representation-dependence found in B2 is confined to small $t$ (a mild, perhaps ignorable effect) or extends to a genuine competing vacuum at larger $t$ depends on precisely the UV data that Branch 3 leaves unfixed. **So Branches 1 and 3 are not independent — the regulator choice governs how severe the representation-dependence actually is.**

**[C2] — Branch 2's relationship to the other two is different in kind, not degree.** Branch 2 isn't about *how large* the boson-loop correction is (which would make it a quantitative question entangled with Branches 1/3) — it's about whether there's *any stated reason* to drop it at all. This is a **prior, structural gap**: even before asking what a specific regulator gives for $F$, or how far the representation-dependence extends in $t$, one can already observe that the corpus never states why the boson loop is negligible. This doesn't collapse into Branches 1/3; it sits *above* them, since a controlled-expansion parameter (were one found) would determine how much either of the other two branches even matters, without needing to resolve either first.

## Revised dependency graph

Not quite your proposed graph — testing it produced a refinement:

```
Microscopic action
        │
        ▼
Exact bosonization (Object B)
        │
        ▼
Mean-field truncation (Object C)
        │
        ├──► Branch 2: NO stated controlling parameter for dropping boson loops
        │         (structural gap — sits above the other two; unresolved by anything below)
        │
        └──┬──► Branch 3: UV regulator unfixed
           │
           └──► Branch 1: representation-dependence, whose *severity*
                 (confined to small t, or a genuine competing vacuum)
                 is governed by Branch 3's unresolved UV data
```

**Branches 1 and 3 are linked, confirmed directly rather than merely conjectured.** Branch 2 is not a third independent failure mode at the same level — it's a **precondition** that was never checked before Branches 1 and 3 were even reached: nothing in $S_{\rm geo}$ justifies stopping at one fermion loop in the first place.

## Status

C1's objective is met to the extent that all three branches are now precisely stated and their relationships tested rather than assumed. The honest summary: **the approximation sequence is not self-consistent, and the reason is more basic than any single branch — there is no stated small parameter anywhere in $S_{\rm geo}$ licensing the fermion-loop/no-boson-loop truncation used throughout Target 0 and Foundation B, and the two identified consequences of proceeding anyway (Fierz representation-dependence, UV regulator-dependence) are not independent pathologies but a single unresolved truncation manifesting two ways.**

This sharpens rather than replaces the earlier findings: B2's result stands as a valid demonstration exactly as scoped; Branch 2's finding here explains *why* such a demonstration was possible to construct at all — there was never a principled reason the truncation should have been representation-independent in the first place.
