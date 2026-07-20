# Foundation C — C0: Documenting the A→B→C Chain

*Adopting your Object A/B/C distinction as the organizing structure. This notebook constructs Object B explicitly (something no prior document in this reconstruction, or apparently the corpus, has done), and shows precisely where the corpus's A→C jumps occur.*

## Objective, stated per your proposed framing

Construct, from the frozen $S_{\rm geo}$, a documented derivation of an effective bosonic functional $\Gamma[\Phi]$, identifying explicitly: (1) every exact transformation, (2) every approximation, (3) every truncation, (4) every newly introduced assumption — so the provenance of any resulting effective potential can be audited independently of its physical interpretation.

## Object A → Object B: what's actually exact

**[C1]** Object A is $S_{\rm geo}$, frozen, unchanged since the original Constitution.

**[C2] — Object B, constructed with full bookkeeping.** Using the closed Foundation A Fierz system to write the *general* exact bosonization (not yet the restricted $t$-family — the full five-channel HS transform, exact for any choice of five coefficients $(c_S,c_P,c_V,c_A,c_T)$ satisfying the one Fierz constraint that they represent the same operator):
$$-\frac\lambda4\eta^2 \;=\; -\frac{\lambda c_S}4\eta^2 - \frac{\lambda c_P}{20}\cdot 5\,P^2 \cdots$$
More precisely, **[C2]**: the exact statement of Object B is
$$Z[J] = \mathcal N^{-1}\int\mathcal D\sigma\,\mathcal D\pi\,\mathcal D V_\mu\,\mathcal D A_\mu\,\mathcal D T_{\mu\nu}\;e^{i\int\left[\text{quadratic}(\sigma,\pi,V,A,T;\,c) \;+\;\bar\psi(i\partial\!\!\!/-m-\sigma-i\gamma^5\pi-\gamma\!\cdot\! V-\gamma^5\gamma\!\cdot\! A-\sigma_{\mu\nu}T^{\mu\nu})\psi\right]}$$
for **any** choice of coefficient set $c=(c_S,c_P,c_V,c_A,c_T)$ consistent with the single Fierz constraint linking them (the one-parameter $t$-family used in B1/B2 is a slice of this larger space, not its entirety — this is worth stating plainly since B1/B2 only ever explored one line through a larger space of exact representations). **This is Object B, and it is exact: no saddle point, no loop truncation, no regulator has entered yet.** Every member of this family, for every admissible $c$, computes the identical $Z[J]$ — this is guaranteed by construction, since each is a Gaussian completion of the same operator identity established in Foundation A, not by any new argument.

**Explicit flag, per your point 5:** Foundation B (B2) established that at least one member of this family exhibits mean-field representation-dependence. **It did not establish, and C0 does not now establish, that every member does.** This remains an open, larger question than B2 answered, and I am not treating it as settled.

## Object B → Object C: where the corpus actually is

**[C2] — Target 0 / B1–B2's own Object C.** Restricting to the $(\sigma,\pi)$ slice (justified via PSC in B1.3/B1.4) and taking the saddle point of the fermion determinant at one-loop, zero boson-loop order:
$$V_{\rm eff}^{(t)}(\sigma,\pi) = \frac{\sigma^2}{\lambda(1-t)}+\frac{5\pi^2}{\lambda t} + F\big((m+\sigma)^2+\pi^2\big)$$
This is a fully documented Object C — every step from A through B to here is shown in this reconstruction, with every truncation labeled (saddle point in $\sigma,\pi$; one fermion loop; zero boson loop; PSC-justified restriction to the scalar/pseudoscalar sector; UV divergence in $F$ still unregularized, per the original Target-0 halt).

**[C1, quoting] — Theorem 6's Object C**, by contrast: $V_{\rm eff}(\eta)=\frac{m^2}2\eta-\frac\lambda4\eta^2$. Checking this against the Object-B family: setting $t=0$ in the *classical* (no fermion loop) piece of the B1/B2 construction gives exactly $\sigma^2/\lambda$ as the auxiliary-field stiffness term, which on-shell ($\sigma=\lambda\eta/2$, from the original Target-0 Gaussian completion) reduces to $\lambda\eta^2/4$ — **matching Theorem 6's quartic term in form and sign**, but **only if the fermion-loop contribution $F(\cdot)$ is dropped entirely.** There is no documented step in Theorem 6 corresponding to "and then we neglect $F$," or any regularization of it — **Theorem 6's Object C is missing the entire B2 step (the fermion determinant) as a documented transformation.** This confirms, more precisely than the earlier audit could, exactly *where* the A→C jump occurs: Theorem 6 has effectively performed the classical piece of the $t=0$ HS completion and stopped, presenting the result as if it were the full mean-field potential.

**[C1, quoting] — §P.11.2's Object C:** $V(\eta,P)=\frac{\mu^2}2(\eta^2+P^2)+\frac\lambda4(\eta^2+P^2)^2-m\eta$. Checking against the Object-B family with the earlier caution in mind (I am not asserting this is *outside* the family, only that its membership is undemonstrated): the coefficient structure — equal weight on $\eta^2,P^2$ at quadratic order, an *additional* quartic-in-$(\eta^2+P^2)$ term not present anywhere in $S_{\rm geo}$ or in any Object-B member constructed here — **does not match any $c$ in the Object-B family as constructed in this notebook**, because Object B's quadratic-in-auxiliary-field terms are fixed by the Fierz coefficients times $1/\lambda$-type stiffnesses, with no independent quartic self-interaction of the auxiliary fields ever generated at *this* stage (a quartic-in-$\Phi$ term would only arise from higher-loop corrections to the auxiliary sector, i.e., from Object C's boson-loop content, not from Object B). **This is a stronger, more precise finding than the earlier audit's "not explicitly demonstrated": §P.11.2's potential has a term (the quartic $(\eta^2+P^2)^2$ piece) that cannot originate from Object B at all under the construction given here — it would have to come from somewhere else (a boson self-energy correction, a separately-introduced phenomenological term, or an error), and the corpus does not say which.**

## Summary — the provenance chain, made explicit

| Step | Documented in this reconstruction? | Documented in Theorem 6? | Documented in §P.11.2? |
|---|---|---|---|
| A: frozen action | ✓ | ✓ (cited) | ✓ (cited) |
| A→B: exact bosonization | ✓ (this notebook) | ✗ | ✗ |
| B→C: fermion loop / saddle point | ✓ (B1/B2) | ✗ — absent entirely | Partial — quadratic piece plausible, quartic piece unaccounted for |
| C: regulator / UV treatment | ✗ (flagged, open) | ✗ | ✗ |

## Status

C0's objective is met for the constructed line of the reconstruction (A→B→C fully documented through Target 0/B2, halting honestly at the UV regulator). It also sharpens, rather than merely repeats, the earlier audit: Theorem 6's gap is now identified specifically as *missing the B→C fermion-loop step*, and §P.11.2's gap is now identified specifically as *containing a term with no traceable origin in Object B at all*, not merely an unmotivated coefficient choice. Foundation B's caution stands unaltered: this shows the documented line is representation-dependent and that two corpus documents each skip or add an undocumented step; it does not show every possible bosonization behaves this way, and C0 does not close that broader question.

Ready for C1 (does the mean-field/one-loop order suffice, given this) whenever you'd like to proceed.
