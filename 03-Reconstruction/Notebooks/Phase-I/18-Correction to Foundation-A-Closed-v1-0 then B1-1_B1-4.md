# Correction to `Foundation-A-Closed-v1.0`, then B1.1–B1.4

## An error found while trying to *use* the closed system, not while re-checking it

Building $\Gamma[\sigma,\pi,V,A,T]$ requires the closed Fierz system in a single, fully consistent real-field convention throughout — something the closure process itself never actually exercised (the involution check only needed $T^2$ and $F^2=\mathbb1$, not every pairwise relation). Redoing all four relations from their original raw-imaginary-$P$ derivations, substituting $P^2_{\rm raw}=-P^2_{\rm real}$ **consistently** throughout (dropping the tilde now — I'll write $P$ for the real field from here on):

$$\eta^2 = \tfrac15P^2-\tfrac15V^2+\tfrac15A^2-\tfrac1{10}T^2 \qquad P^2 = \tfrac15\eta^2-\tfrac15V^2+\tfrac15A^2+\tfrac1{10}T^2$$
$$A^2-V^2 = 2\eta^2+2P^2 \qquad\qquad T^2=-6\eta^2+6P^2$$

**Cross-check, redone independently:** $(1)+(2)$ gives $2(\eta^2+P^2)=A^2-V^2$, matching (3) exactly. $(1)-(2)$ gives $-6(\eta^2-P^2)\cdot(-1)=T^2$... i.e. $T^2=-6\eta^2+6P^2$, matching (4) exactly. **Self-consistent.**

**This differs from `Foundation-A-Closed-v1.0` in two signs**: the certificate's η² row (had $-\tfrac15P^2$, should be $+\tfrac15P^2$) and its $A^2-V^2$ row (had $-2P^2$, should be $+2P^2$). Tracing the source: the underlying step-by-step derivations in the original A4b2 notebook were actually done correctly at each line; the error is in how those results were transcribed into the certificate's compact summary — a genuine, if narrow, provenance failure of exactly the kind the certificate's own "immutable baseline" language was supposed to prevent. **This requires a `Foundation-A-Closed-v1.1` erratum**, not a silent fix — flagging per the provenance policy you specified.

## B1.1 — The bosonized action, before symmetry is invoked

**[C2]** Using a one-parameter Fierz interpolation (weight $t$ moved from the raw $\eta^2$ term into its Fierz-equivalent form via relation (1) above):
$$-\frac\lambda4\eta^2 = -\frac{\lambda(1-t)}{4}\eta^2 - \frac{\lambda t}{20}P^2+\frac{\lambda t}{20}V^2-\frac{\lambda t}{20}A^2+\frac{\lambda t}{40}T^2$$
exact for any $t$ (an identity, not an approximation, since relation (1) is exact). HS-transforming each surviving channel with its own auxiliary field ($\sigma\leftrightarrow\eta$, $\pi\leftrightarrow P$, $V_\mu^{\rm aux}\leftrightarrow V^\mu$, etc.) gives a generalized Dirac operator
$$D = i\partial\!\!\!/ - m - \sigma - i\gamma^5\pi - \gamma\!\cdot\!V^{\rm aux} - \gamma^5\gamma\!\cdot\!A^{\rm aux} - \sigma_{\mu\nu}T^{{\rm aux},\mu\nu}$$
and $\Gamma(t;\sigma,\pi,V^{\rm aux},A^{\rm aux},T^{\rm aux}) = [\text{quadratic HS terms, coefficients depending on }t] + i\,\mathrm{Tr}\ln D$. **Flagged, not resolved:** for $t$ such that a given channel's Fierz coefficient is negative, the naive per-channel Gaussian HS completion needs the opposite sign convention (or analytic continuation) to converge — a known subtlety in multi-channel bosonization I have not worked through here.

## B1.2 — Is $\Gamma$ exactly $SO(3)$-invariant?

**[C2]** Yes, and this is derivable rather than assumed. Under a spatial rotation $R\in SO(3)$, coordinates transform as $x^i\to R^i_{\ j}x^j$ and the spinor transforms in the corresponding spin representation $\psi\to S(R)\psi$ with $S(R)\gamma^\mu S(R)^{-1}=R^\mu_{\ \nu}\gamma^\nu$ (standard, and consistent with the explicit representation fixed in Foundation A). The auxiliary fields transform as their Lorentz type dictates ($\sigma,\pi$ scalars: invariant; $V^{\rm aux}_\mu,A^{\rm aux}_\mu$: rotate as vectors; $T^{\rm aux}_{\mu\nu}$: rotates as a tensor). Under the *simultaneous* transformation of coordinates, spinor basis, and auxiliary fields, $D\to S(R)DS(R)^{-1}$ by direct substitution (each term in $D$ built from covariant contractions of a $\gamma$-structure with the correspondingly-transforming field). Then $\mathrm{Tr}\ln D \to \mathrm{Tr}\ln[S(R)DS(R)^{-1}] = \mathrm{Tr}[S(R)\ln D\,S(R)^{-1}] = \mathrm{Tr}\ln D$ (trace is invariant under similarity transformation — a one-line linear-algebra fact, not assumed). The classical HS quadratic terms are manifestly invariant by construction (sums of Lorentz-index-contracted squares). **No anomaly concern**, per your note: spatial rotations are not chirally anomalous in 3+1D Dirac theory (the relevant anomaly is under $U(1)_A$, unrelated to $SO(3)$). **$\Gamma$ is exactly $SO(3)$-invariant.**

## B1.3 — Does the auxiliary-field variational problem carry constraints?

**[C2] — the key clean finding, using your own suggested angle.** Two independent facts, both checkable directly rather than inferred by analogy to Hawking's case:

1. **Gravity is not in play.** The Constitution's own Target 0 definition (§5) explicitly restricts to a **flat background with gravity decoupled**. Hawking's PSC exception concerns spatially-homogeneous *gravitational* (metric/lapse/shift) reductions specifically — that machinery, and its associated Hamiltonian constraint, is simply **absent from Target 0's scope by construction**. This directly answers your suggested check: there is no gravitational constraint to inherit, because there is no dynamical gravity here at all.

2. **The auxiliary fields themselves carry no constraint structure.** Every HS field introduced in B1.1 enters $\Gamma$'s classical piece with **no kinetic (derivative) term** — only algebraic mass-like terms ($\sigma^2/\lambda$, etc.). Constrained-system (Dirac–Bergmann) analysis produces Hamiltonian constraints from *degenerate momenta* — fields whose time-derivatives don't appear, or appear degenerately, in the Lagrangian. A field with **no derivative dependence at all** trivially has no canonical momentum to be degenerate: its Euler–Lagrange equation is purely algebraic ($\delta\Gamma/\delta\sigma=0$ at each point, no propagation). **There is no constrained-system structure in the auxiliary sector, independent of the gravity question.**

## B1.4 — Applying PSC

**[C2]** Both of PSC's obstruction routes are closed off within Target 0's actual scope: no gravitational constraint (point 1), no matter-sector constraint (point 2), and $\Gamma$ is confirmed $SO(3)$-invariant (B1.2) with $SO(3)$ compact and acting linearly on the field space (B1.1's construction). **PSC applies cleanly here: restricting to $V^{\rm aux}=A^{\rm aux}=T^{\rm aux}=0$ (mod $u^\mu$-aligned pieces) before extremizing is exact, not a truncation, within Target 0's flat-space scope.**

**Explicit scope limit, stated plainly so it isn't silently assumed later:** this resolution depends on point 1 — gravity's absence — which is a feature of *Target 0 specifically*, not of the corpus's actual cosmological application. The moment this machinery is pointed at §P.9's real FLRW system (which has its own explicit gravitational Hamiltonian constraint, §P.9.5.1, by name), point 1 no longer holds, and the Hawking-type caveat would need to be checked again from scratch on that system — this B1.3/B1.4 resolution does **not** transfer automatically to a future cosmological extension.

**Status: B1 resolved within Target 0's flat-space scope.** Reduced problem for B2 onward: $\sigma,\pi$ only (plus $u$-aligned $V^0,A^0$ if retained), with the Fierz-parameter $t$-dependence of B1.1 still the open, unresolved ambiguity — that's the next thing to pin down.
