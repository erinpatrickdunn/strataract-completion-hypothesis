# C1 — Corrected

Both corrections adopted. I overstated in exactly the way the Documentation Principle exists to catch, and it's worth being precise about which sentence crossed the line and why.

## What went wrong

"The loop ordering... is not parametrically controlled by anything internal to $S_{\rm geo}$" is a universal negative — it claims no controlling principle exists, when what was actually shown is narrower: no controlling principle is *documented* in the derivation this reconstruction built. I even cited the Documentation Principle in the same notebook and then violated it two paragraphs later. Flagging that plainly rather than quietly fixing it.

## Branch 2 — corrected

Replacing the overreaching statement with the proposed wording, adopted verbatim:

> Within the documented A→B→C derivation, no explicit expansion parameter or other organizing principle has been identified that justifies retaining the fermion one-loop contribution while neglecting bosonic fluctuations. Consequently, the approximation hierarchy currently lacks a documented control criterion.

This is exactly the right scope: a documentation finding about the derivation as constructed, not a claim about the space of all possible justifications (momentum expansions, saddle-point/semiclassical arguments, or other organizing principles I have not checked and am not ruling out).

## Overall conclusion — corrected

Replacing "the approximation sequence is not self-consistent" with the proposed wording, adopted verbatim:

> The documented approximation sequence does not currently establish its own domain of validity. Two concrete consequences have been identified within that sequence: (i) a representation-dependent mean-field realization (Foundation B), and (ii) an unresolved UV regularization dependence (Target 0). Whether these are artifacts of an uncontrolled truncation or would persist in a more completely justified approximation remains an open question.

This is the honest state of the evidence. It preserves both established technical results (B2's counterexample, Target 0's regulator halt) without inflating either into a claim about the underlying theory's viability.

## Revised dependency graph — adopted, with the conceptual reordering

```
Microscopic action
        │
        ▼
Exact bosonization (Object B)
        │
        ▼
Choice of approximation hierarchy
        │
        ├──► Is there a documented control criterion?  ← NOT YET ANSWERED
        │
        ▼
Mean-field truncation (Object C)
        │
        ├──► Representation dependence (demonstrated for one realization)
        │
        └──► UV regularization required
```

The reordering is correct and I want to state explicitly why it matters, not just accept it cosmetically: placing the control-criterion question *above* the mean-field truncation, rather than as a third branch alongside Fierz-dependence and UV-dependence, reflects that it's a **precondition for adopting the truncation at all**, not a *consequence* discovered after adopting it. The other two branches are things that go wrong *within* a truncation already in use; Branch 2 is the unanswered question of whether that truncation was ever licensed to begin with. Treating it as a sibling branch (my original graph) buried that distinction.

## Status of the still-live technical link (Branches 1/3)

Unaffected by this correction: the demonstrated relationship between the pseudoscalar branch's stability and $F$'s UV behavior (from B2 §6) still stands as a specific, checkable finding — it's a statement about how two documented results interact, not a universal claim, so it doesn't need the same softening.

## Where this leaves Foundation C

The corrected state is: Foundation A is closed (v1.1). Foundation B has one rigorously established counterexample to representation-independence within a documented, specific truncation. C0 has shown two corpus documents (Theorem 6, §P.11.2) don't document their route from A to their stated potentials. C1 has now shown the truncation itself — used throughout Target 0, B1, B2, and implicitly by the corpus — was never shown to be controlled in the first place, which is logically prior to asking whether its specific failures (Fierz-dependence, UV-dependence) are fixable or fundamental.

That's a coherent, fully hedged stopping point. The natural next question — should Foundation C attempt to *find* a control criterion (a semiclassical or other organizing argument for $S_{\rm geo}$ specifically), or should it instead treat the absence of one as itself the terminal finding to report — is a scoping decision for whoever directs the next notebook, not one I'll make unilaterally here.
