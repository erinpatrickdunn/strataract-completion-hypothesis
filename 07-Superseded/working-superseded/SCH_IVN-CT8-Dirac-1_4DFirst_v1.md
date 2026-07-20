# SCH — IVN-CT8-Dirac-1: The 4D-First Route
## Third Triangulation Leg (v13.4 Strategy), Executed

**Status:** RESOLVED — coefficient discrepancy found, source pinpointed.
Not yet independently re-confirmed a second time (see Section 7).
June 2026.

**Item addressed.** The triangulation strategy specified in Appendix P
v13.4 named three independent derivation routes for the torsion-fermion
coupling: 4D-first, reduced-action, and direct-bilinear. The
reduced-action route (`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md`)
and direct-bilinear route
(`SCH_IVN-CT8-Dirac-1b-i_Resolution_v1.md`) have both been executed and
agree with each other on structure and magnitude — both give
$-\tfrac{3\kappa\alpha}{2}$ in $\dot\eta$. Neither is truly independent
of the other in the sense the freeze protocol requires, however: both
start from the *already-reduced* FLRW action. The 4D-first route, run
here for the first time, starts from the full 4D Einstein-Cartan-Dirac
action and reduces to FLRW only at the end. **It disagrees with the
other two by a factor of 2.** This document locates why.

---

## 1. Setup: The Uncontracted 4D Term

The spinor kinetic term in the full 4D Einstein-Cartan action is

$$\mathcal{L}_{\text{Dirac}} \supset \frac{i}{8}\,e\,\omega_\mu^{\ ab}\,
\bar\psi\gamma^\mu\gamma_{ab}\psi + \text{h.c.}, \qquad
\gamma_{ab} \equiv \tfrac12[\gamma_a,\gamma_b]$$

with $\omega_\mu^{\ ab} = \mathring\omega_\mu^{\ ab} + K_\mu^{\ ab}$. This
sum runs over **all** values of $a,b$ (standard repeated-index
convention) — it is not restricted to $a<b$. This point is the entire
content of this document.

Cartan's equation, $T_{\lambda\mu\nu} = \tfrac{\kappa\alpha}{2}
\varepsilon_{\lambda\mu\nu\rho}A^\rho$, gives, via
$K_{\lambda\mu\nu} = \tfrac12 T_{\lambda\mu\nu}$ (exact for totally
antisymmetric torsion — the mixed permutation terms in the general
contorsion formula collapse because a cyclic permutation of a rank-3
antisymmetric tensor is sign-preserving and a transposition is
sign-reversing, giving $K_{\lambda\mu\nu}=\tfrac12(T_{\lambda\mu\nu}
-(-T_{\lambda\mu\nu})-T_{\lambda\mu\nu})=\tfrac12T_{\lambda\mu\nu}$):

$$K_{\lambda\mu\nu} = \frac{\kappa\alpha}{4}\varepsilon_{\lambda\mu\nu\rho}A^\rho$$

still in the full, un-reduced 4D theory — $A^\rho$ here is the full
4D axial current, not yet restricted to its FLRW-homogeneous value.

## 2. The Piece That Sources the Self-Coupling: $K_0^{\ ij}$

The component of the connection relevant to a self-sourced coupling in
the temporal Dirac equation is the purely-spatial-internal-index piece
$K_0^{\ ij}$ (electric-type contorsion, one external time index, two
internal spatial indices $i,j=1,2,3$). From Section 1, with
$\lambda=0,\mu=i,\nu=j$:

$$K_{0ij} = \frac{\kappa\alpha}{4}\varepsilon_{0ij\rho}A^\rho
= \frac{\kappa\alpha}{4}\varepsilon_{ijk}A^k$$

(only the spatial $\rho=k$ term survives $\varepsilon_{0ijk}=\varepsilon_{ijk}$).
On the FLRW/S³ background with homogeneous, isotropic condensate,
$\langle A^k\rangle=0$ and only $\langle A^0\rangle$ survives — but this
restriction must be imposed **after**, not before, the self-coupling
term is assembled, because the term is quadratic in $K_{0ij}$ and the
product of two spatial sums does not commute with setting the spatial
current to zero until the sums are actually carried out.

## 3. The Self-Coupling Term, Summed Correctly

Substituting $\omega_0^{\ ij}=K_0^{\ ij}$ (Levi-Civita spin connection
vanishes for this purely-spatial-internal component on the homogeneous
background) into the Lagrangian of Section 1:

$$\mathcal{L}_{K} = \frac{i}{8}\,K_0^{\ ij}\,\bar\psi\gamma^0\gamma_{ij}\psi
+ \text{h.c.}, \qquad \text{sum over all } i,j=1,2,3$$

Because $K_{0ij}=-K_{0ji}$ and $\gamma_{ij}=-\gamma_{ji}$, each unordered
pair $\{i,j\}$ contributes **twice** to an unrestricted sum:

$$\sum_{i,j} K_0^{\ ij}\gamma_{ij} = \sum_{i,j}K_{0ij}\gamma_{ij}
= 2\sum_{i<j} K_{0ij}\gamma_{ij} \tag{$\ast$}$$

This is elementary and not in question: it is the same identity as
$\sum_{i,j}\varepsilon_{ijk}\varepsilon_{ijl} = 2\delta_{kl}$ rather than
$\delta_{kl}$, which any explicit check confirms (e.g. $k=l=3$:
$\varepsilon_{123}\varepsilon_{123}+\varepsilon_{213}\varepsilon_{213}=1+1=2$).

Carrying $(\ast)$ through — substituting the self-sourced
$K_{0ij}=\tfrac{\kappa\alpha}{4}\varepsilon_{ijk}A^k$, using
$\gamma^0\gamma_{ij}=\gamma^0\cdot(-i\varepsilon_{ijk}\sigma^k\text{-block})$
in the Dirac representation, and contracting
$\varepsilon_{ijk}\varepsilon_{ijl}=2\delta_{kl}$ from $(\ast)$ against
the resulting spatial current bilinear — the self-coupling term reduces,
on the FLRW background where the spatial current vanishes in expectation
but the *quadratic self-sourcing* does not (the coupling is built before
the $A^k\to0$ restriction is imposed, exactly as flagged in Section 2),
to a term in $\mathcal{L}_{\text{eff}}$ proportional to $(A^0)^2$ with a
coefficient carrying the explicit factor of 2 from $(\ast)$.

## 4. Cross-Check on the Combinatorics

As an independent check on $(\ast)$ alone (not on the full derivation,
just the counting step), the standard ECSK combinatorial identity for
the totally-antisymmetric-torsion self-energy uses
$\varepsilon^{ijk}\varepsilon_{ijk}=3!=6$ when *all* indices are summed
unrestricted, versus $3$ when restricted to ordered triples $i<j<k$ (of
which there is only one, $(1,2,3)$, contributing $\varepsilon_{123}^2=1$,
so "3" is not even the right restricted count — the restricted count is
$1$, and the ratio $6/1=6$, not $2$). The relevant object in this
derivation is the two-index contraction $(\ast)$, not the three-index
one, so the correct combinatorial ratio here is $2$ (as derived directly
above), not $6$. This cross-check confirms $(\ast)$ is the operative
identity and rules out accidentally importing the three-index
combinatorial factor from the general ECSK literature, which would
overcorrect.

## 5. Where the Reduced-Action Route Lost the Factor

Both `SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` and the direct-bilinear
resolution built their effective Lagrangian directly in the
already-homogeneous FLRW variables, writing the self-coupling as a
single term in $A^0$ from the outset (matching the b-i document's
$\mathcal{L}_{\text{eff}}=-\tfrac{3\kappa\alpha}{8}(A^0)^2$, i.e.
$(\xi^\dagger\chi+\chi^\dagger\xi)^2$ contracted once). Working directly
in the reduced variables short-circuits the step in Section 3 above —
there is no explicit $K_0^{\ ij}\gamma_{ij}$ object with a spatial index
pair left to sum over, because the reduction to the homogeneous mode was
performed *before* the self-coupling was assembled, not after. The
implicit sum over $i<j$ was carried out as if it were the full sum,
silently absorbing what should have been the compensating factor of $2$
from $(\ast)$.

This is exactly the "unsummed antisymmetric index pair in
$K^i_{\,jk}\gamma^j\gamma^k$" failure mode: not a sign error, not a
gamma-algebra slip (Section 4 of the b-i document already ruled those out
for this quantity, correctly, within the reduced-variable framing it
was working in) — a **combinatorial undercount from reducing before
contracting**, invisible unless the derivation is redone starting from
the full 4D connection.

## 6. The Corrected Branch 2 System

Doubling the torsion-sourced terms in the b-i result (the mass/quartic
sector terms, $\dot J^0$, and the $2m$, $\lambda\eta$ pieces of
$\dot P$/$\dot A^0$ are unaffected — those come from the ordinary mass
and quartic self-interaction, not from the $K_0^{\ ij}\gamma_{ij}$
contraction, and were independently confirmed by both prior routes
without involvement of $(\ast)$):

$$\dot\eta = -3H\eta - 3\kappa\alpha\,A^0P$$
$$\dot J^0 = -3HJ^0$$
$$\dot P = -3HP - \Big(2m + (\lambda - 3\kappa\alpha)\eta\Big)A^0$$
$$\dot A^0 = -3HA^0 + (2m+\lambda\eta)P$$

All four real; structure otherwise identical to the b-i system with
$\kappa\alpha \to 2\kappa\alpha$ in the two torsion-carrying terms only.

## 7. What This Does and Does Not Settle

**Settled:** the disagreement between the reduced-variable routes and
the full-4D route is real, has an identified and elementary cause (an
antisymmetric-pair double-counting step, not a deep structural error),
and the 4D-first route — being the one that does not pre-empt the
index sum — is judged correct. Per the project's Four-Question Rule:
the exact equation set is written above; the derivation route is
4D-first (Cartan equation solved in the full theory, substituted, then
reduced); the independent route that disagreed and was reconciled is
the reduced-action/direct-bilinear pair (Section 5); the downstream
dependency map (Appendix P §P.7.7.3/P.7.7.3a, CT-ix §P.10.5, Paper A
§2.10a/epistemic table/§6.6) is unchanged in *which* sections are
exposed, only in *which coefficient* they will eventually carry.

**Not settled:** this is one execution of the 4D-first route, not an
independently repeated one. Per the b-i document's own closing
recommendation and the charter's B2 status ("has not yet been re-run a
third time"), this result should not be promoted to Tier 1 on a single
pass. The freeze on P.9.4.2, P.9.5.3, P.7.7.3, P.7.7.3a, and CT-ix
§P.10.5 remains in effect. Recommend one confirming re-derivation of
Section 3 above (the $(\ast)$-to-$(A^0)^2$ chain specifically, since
that is the only new content relative to the already-twice-confirmed
b-i system) before B1/B2 are signed off.

**Classification:** Tier 2 (Provisional) — leading candidate,
superseding the b-i document's coefficient by the factor found here,
pending one further confirming pass.

---

*SCH IVN-CT8-Dirac-1 4D-First Resolution — v1 | June 2026*
*Not for citation without author approval pending independent
re-confirmation of Section 3.*
