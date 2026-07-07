# SCH — IVN-CT8-Dirac-1: Confirming Pass on the 4D-First $(\ast)$-to-$(A^0)^2$ Chain
## Second, Independent Execution — and a Correction to the First

**Status:** RESOLVED. Corrects `SCH_IVN-CT8-Dirac-1_4DFirst_v1.md`.
June 2026.

**Purpose.** Per the recommendation closing the prior document, this is
the one confirming re-derivation of Section 3 of
`SCH_IVN-CT8-Dirac-1_4DFirst_v1.md` — the only content in that document
not already twice-confirmed elsewhere. To be a genuine second route
rather than a repetition, this document works entirely in explicit
2-spinor components (no abstract $\gamma_{ab}$-antisymmetry lemma used
as a shortcut) and, critically, checks *which* contorsion component
actually survives on the homogeneous background before assembling
anything — a check the prior document skipped.

**Headline result: the prior document's Section 3 was wrong.** It used
the wrong contorsion component. Redone correctly, this pass does **not**
confirm the doubled coefficient $-3\kappa\alpha$. It reproduces the
original reduced-action/direct-bilinear coefficient, $-\tfrac{3\kappa\alpha}{2}$,
exactly.

---

## 1. Which Contorsion Component Actually Contributes?

Cartan's equation, $T_{abc}=\tfrac{\kappa\alpha}{2}\varepsilon_{abcd}A^d$
(all internal Lorentz indices), is only nonzero when $a,b,c,d$ are *all
four* distinct — a 4-index epsilon symbol in 4D vanishes unless every
index differs. This means $T_{abc}$ (and $K_{abc}=\tfrac12T_{abc}$)
splits into exactly two disjoint cases, according to which single index
is "left over" as $d$:

**Case 1 — fully spatial, $\{a,b,c\}=\{i,j,k\}$, left-over index $d=0$:**
$$K_{ijk} = \frac{\kappa\alpha}{4}\varepsilon_{ijk}A^0$$
Sourced by $A^0$. **Survives** on the homogeneous, isotropic background,
where $\langle A^0\rangle\neq0$ by construction (this is Branch 2).

**Case 2 — one temporal, two spatial, $\{a,b,c\}=\{0,i,j\}$, left-over $d=k$:**
$$K_{0ij} = \frac{\kappa\alpha}{4}\varepsilon_{ijk}A^k$$
Sourced by the *spatial* axial current $A^k$. On the homogeneous,
isotropic FLRW/S³ background there is no preferred spatial direction:
$A^k=0$ identically, not merely in expectation. **This term vanishes.**

`SCH_IVN-CT8-Dirac-1_4DFirst_v1.md`, Sections 2–3, used **only Case 2**
— the connection component $K_0^{\ ij}$, contracted against
$\gamma^0\gamma_{ij}$. That computation, and the antisymmetric-pair
counting identity within it, was arithmetically fine on its own terms.
But the object it was computing is exactly the piece that vanishes on
the physical background. The "factor of 2 the reduced-action route
missed" was found inside a term that does not contribute to the
self-coupling at all. **Case 1 was never examined in the prior
document.** This is the actual bug this confirming pass exists to catch.

## 2. Redoing It With the Correct Component (Case 1)

The relevant Lagrangian piece has *external* index $a=i$ (spatial), not
$a=0$:
$$\mathcal{L}_K = \frac{i}{8}\sum_i\sum_{j,k}K_{ijk}\,\bar\psi\gamma^i\gamma_{jk}\psi + \text{h.c.}$$

Using the established Dirac representation
($\gamma^0=\mathrm{diag}(I,-I)$, $\gamma^i=\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$,
$\psi=(\xi,\chi)^T$), direct multiplication gives, for spatial $j\neq k$:
$$\gamma_{jk} = \mathrm{diag}(-i\varepsilon_{jkl}\sigma^l,\,-i\varepsilon_{jkl}\sigma^l)$$
$$\gamma^i\gamma_{jk} = \begin{pmatrix}0 & \sigma^iM\\ -\sigma^iM & 0\end{pmatrix},\quad M\equiv-i\varepsilon_{jkl}\sigma^l$$
$$\bar\psi\gamma^i\gamma_{jk}\psi = \psi^\dagger\gamma^0\gamma^i\gamma_{jk}\psi = \xi^\dagger\sigma^iM\chi+\chi^\dagger\sigma^iM\xi = -i\varepsilon_{jkl}\big(\xi^\dagger\sigma^i\sigma^l\chi+\chi^\dagger\sigma^i\sigma^l\xi\big)$$

every step multiplied out explicitly, no lemma invoked.

## 3. Assembling and Contracting the Sums

Substituting $K_{ijk}=\tfrac{\kappa\alpha}{4}\varepsilon_{ijk}A^0$:

$$\mathcal{L}_K = \frac{i}{8}\cdot\frac{\kappa\alpha}{4}A^0\cdot(-i)\sum_{i,j,k,l}\varepsilon_{ijk}\varepsilon_{jkl}\big(\xi^\dagger\sigma^i\sigma^l\chi+\chi^\dagger\sigma^i\sigma^l\xi\big) + \text{h.c.}$$

The double sum $\sum_{j,k}\varepsilon_{ijk}\varepsilon_{jkl}=\sum_{j,k}\varepsilon_{ijk}\varepsilon_{ljk}=2\delta_{il}$
(using the cyclic identity $\varepsilon_{jkl}=\varepsilon_{ljk}$, then the
standard two-index contraction — verified by direct enumeration, e.g.
$i=l=1$: only $(j,k)=(2,3),(3,2)$ contribute, giving
$\varepsilon_{123}\varepsilon_{231}+\varepsilon_{132}\varepsilon_{321}=(1)(1)+(-1)(-1)=2$;
$i=1,l=2$ gives $0$ by identical direct check). Collapsing $i=l$:

$$\mathcal{L}_K = \frac{i\cdot(-i)\kappa\alpha}{32}A^0\cdot2\sum_i\big(\xi^\dagger\sigma^i\sigma^i\chi+\chi^\dagger\sigma^i\sigma^i\xi\big)+\text{h.c.}$$

$i\cdot(-i)=1$; $\sum_i\sigma^i\sigma^i = 3I$ (each Pauli matrix squares to
$I$, three terms):

$$\mathcal{L}_K = \frac{\kappa\alpha}{32}A^0\cdot2\cdot3\,(\xi^\dagger\chi+\chi^\dagger\xi)+\text{h.c.} = \frac{6\kappa\alpha}{32}A^0\,(w+\bar w)+\text{h.c.}$$

Using $w+\bar w=-A^0$ (established convention, `SCH_IVN-CT8-Dirac-1b-i_Resolution_v1.md`
Section 1):

$$\mathcal{L}_K = -\frac{6\kappa\alpha}{32}(A^0)^2+\text{h.c.} = -\frac{3\kappa\alpha}{16}(A^0)^2+\text{h.c.}$$

This is already manifestly real, so the h.c. doubles it:

$$\boxed{\mathcal{L}_{\text{eff}} = -\frac{3\kappa\alpha}{8}(A^0)^2}$$

## 4. Comparison

$$-\frac{3\kappa\alpha}{8}(A^0)^2 \quad \text{— exactly the reduced-action/direct-bilinear coefficient.}$$

Not doubled. This second, independent, fully-explicit derivation agrees
with `SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` Part B/C and
`SCH_IVN-CT8-Dirac-1b-i_Resolution_v1.md` Sections 2 and 6, term for
term. **Three independent routes now converge on the same coefficient.**

## 5. What Went Wrong in the Prior Document, Precisely

`SCH_IVN-CT8-Dirac-1_4DFirst_v1.md` computed a real and correct
combinatorial identity — $\sum_{i,j}K_{0ij}\gamma_{ij}=2\sum_{i<j}K_{0ij}\gamma_{ij}$
— attached to the wrong physical object. $K_0^{\ ij}$ is sourced by the
spatial axial current $A^k$, which is exactly zero on a homogeneous,
isotropic background by symmetry, not merely small. No amount of correct
combinatorics on a vanishing term produces a nonzero contribution. The
actual self-sourcing term comes from $K_{ijk}$ (Case 1 above, external
index also spatial), which that document never considered. This is a
"right calculation on the wrong object" error, not a subtler version of
the same bug — the prior document's diagnosis of *why* three routes
might disagree was itself the source of a fourth, spurious disagreement.

This also retroactively clarifies the b/b-i documents: they were correct
in the reduced-variable framing not because they got lucky, but because
working directly in $A^0$ from the outset makes it structurally
impossible to accidentally introduce a Case-2-type vanishing term — the
reduction already discards the spatial-current-sourced piece before any
combinatorics is done. There was no missing factor of 2 in that route to
begin with.

## 6. Consequences

**`SCH_IVN-CT8-Dirac-1_4DFirst_v1.md` is superseded by this document.**
Its Sections 1–6 identified a real mathematical identity but misapplied
it to a term that vanishes identically on the physical background,
producing a spurious factor-of-2 discrepancy where none exists. Its
"corrected Branch 2 system" (Section 6 of that document, coefficient
$-3\kappa\alpha$) should not be used.

**The corrected — and now triply-confirmed — Branch 2 system:**

$$\dot\eta = -3H\eta - \frac{3\kappa\alpha}{2}A^0P$$
$$\dot J^0 = -3HJ^0$$
$$\dot P = -3HP - \left(2m+\left(\lambda-\frac{3\kappa\alpha}{2}\right)\eta\right)A^0$$
$$\dot A^0 = -3HA^0 + (2m+\lambda\eta)P$$

Identical to `SCH_IVN-CT8-Dirac-1b-i_Resolution_v1.md` Section 6.

**Per the project's Four-Question Rule:** exact equations, above; route,
direct-explicit-component 4D-first (Case-1 contorsion, external+internal
spatial indices, contracted with no abstract lemma); independent routes
now agreeing, three (reduced-action, direct-bilinear, this document);
downstream dependency map, unchanged in which sections are exposed
(Appendix P §P.7.7.3/P.7.7.3a, CT-ix §P.10.5, Paper A §2.10a/epistemic
table/§6.6 CT-x note), but the coefficient they should eventually carry
reverts to $-\tfrac{3\kappa\alpha}{2}$, not $-3\kappa\alpha$.

**This changes the governance charter's status, not just Appendix P's.**
The charter (Section 2, current classification table) lists the doubled
coefficient as "Provisional — leading candidate" and attributes the
factor-of-2 finding to "the 4D-first route['s] ... judged correct."
That attribution traces to the now-superseded prior document. The
charter's own B3 dependency table and Section 2 table should be updated
to reflect: three independent routes converge on $-\tfrac{3\kappa\alpha}{2}$;
the doubled candidate is not supported by any surviving derivation.

**Tier recommendation.** With three independently-derived, mutually
agreeing routes (reduced-action, direct-bilinear, direct-explicit
4D-first), this result satisfies the charter's own B2 completion
criterion more fully than the doubled candidate ever did — the doubled
candidate had exactly one derivation behind it, never independently
reproduced, before this pass. Recommend: **promote $-\tfrac{3\kappa\alpha}{2}$
to Tier 1 (Canonical)**, lift the freeze on P.9.4.2, P.9.5.3, P.7.7.3,
P.7.7.3a, and CT-ix §P.10.5, and perform the single-pass canonical
rewrite using this coefficient. This recommendation is offered here,
not executed — the actual rewrite is a separate, deliberate step per
the freeze-and-annotate discipline, and should wait for explicit
sign-off given how many times this exact sector has been prematurely
migrated before.

---

*SCH IVN-CT8-Dirac-1 Confirming Pass — v1 | June 2026*
*Supersedes `SCH_IVN-CT8-Dirac-1_4DFirst_v1.md`. Restores
$-\tfrac{3\kappa\alpha}{2}$ as the triply-confirmed Branch 2 coefficient.
Recommends Tier 1 promotion and freeze lift, pending sign-off.*
