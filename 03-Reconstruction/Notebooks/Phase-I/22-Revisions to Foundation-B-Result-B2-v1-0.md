# Revisions to `Foundation-B-Result-B2-v1.0`

## Addressing point 1: is $t$ a genuine family of HS truncations, or just relabeling?

This can be settled by a logical point rather than a further technical derivation, and I think it fully answers the concern.

**[C2]** For every $t\in[0,1)$, §2 of the frozen result shows $-\frac\lambda4\eta^2$ equals the same operator, written via a different linear combination of bilinears. Consequently, the *exact* path integral $Z[J]$, computed with no truncation, is manifestly $t$-independent — it's the same interaction, so of course the exact partition function built from it doesn't care how it's algebraically decomposed before HS transformation. **This is precisely why $t$-dependence appearing after mean-field truncation is diagnostic rather than incidental**: I do not need to argue that my particular one-parameter family is *the* canonical or unique realization of "the Fierz ambiguity" in some abstract sense. I only need **one** legitimate family of exact bosonizations of the same operator along which the mean-field extremum changes, to establish by direct counterexample that mean-field extremization does not commute with the (exact, operator-level) Fierz identity. That is a logically sufficient disproof of representation-independence at this order, regardless of whether some other parametrization would show a different quantitative slope, a different threshold $t_*$, or even a differently-shaped dependence. **The claim "representation independence has not been established at this approximation order" therefore does not rest on my interpolation being uniquely privileged — only on its being valid, which §2's operator identity establishes directly.**

This resolves the concern without needing an additional proof that my $t$ is "the" realization — it was never necessary to show that, only sufficient to exhibit one.

## Addressing point 2: does $d\Gamma_{\rm MF}/dt$ have independent physical meaning?

I accept this correction and think it sharpens the result rather than weakens it. **$t$ is not a physical parameter of the theory** — it's an internal bookkeeping label for how the exact quartic operator is split before linearization, and nothing in $S_{\rm geo}$ singles out a value of $t$. Consequently $d\Gamma_{\rm MF}/dt$ is **not an observable** and I should not have implied otherwise. What it *is*: a direct, quantitative measure that the one-fermion-loop/zero-boson-loop truncation fails to preserve an exact symmetry of the underlying operator identity (representation-independence under Fierz rearrangement). Its nonvanishing at $t=0$ is the precise sense in which the truncation, not the theory, is representation-dependent — this is a statement about the *approximation scheme's* validity, not a new physical prediction of $S_{\rm geo}$ itself.

## Addressing point 3: the corpus-wide interpretive note

Accepted as stated, replacing the overreaching paragraph verbatim with your proposed wording:

> Within the scalar-only Hubbard–Stratonovich mean-field truncation used in Target 0, the stationary effective potential is not demonstrated to be Fierz invariant. The explicit interpolation constructed here shows local dependence on the chosen decoupling parameter $t$, indicating that representation independence has not been established at this approximation order.

And correspondingly, the corpus-wide remark is downgraded from a claim to a conditional, exactly as you framed it:

> *If* Theorem 6, §P.11's GMOR relation, or Paper C's leptonic-mass program rely on the same scalar-only mean-field truncation used in Target 0, *then* they inherit this same undemonstrated-invariance issue unless an independent argument in those documents fixes the decoupling channel or otherwise restores representation-independence. This has not been checked against those documents and is not asserted here as established for any of them.

---

## `Foundation-B-Result-B2-v1.1`

All technical content (the corrected Fierz system, the exact HS identity, the PSC scope argument, the determinant reduction, the envelope-theorem computation and its $\sigma_0^2/\lambda$ result) is unchanged and stands as derived. What changes in v1.1 is exclusively the interpretive framing: the central claim is downgraded from "the condensate potential is definitively Fierz ambiguous" to **"representation-independence of the mean-field condensate potential has not been established at this approximation order, and an explicit, valid counterexample family shows the extremum's leading dependence on the decoupling choice is generically nonzero."** This is a narrower, more defensible statement, and per the point on logical sufficiency above, it does not require any further work to certify — the counterexample stands regardless of whether other parametrizations would look different.

**Frozen as `Foundation-B-Result-B2-v1.1`.** Awaiting direction on B3 (boson-fluctuation corrections) versus turning to the corpus-wide conditional check (whether Theorem 6/§P.11/Paper C actually do rely on this exact truncation, which hasn't been verified, only flagged as a live possibility).
