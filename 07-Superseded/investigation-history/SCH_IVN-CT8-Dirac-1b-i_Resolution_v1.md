# SCH — IVN-CT8-Dirac-1b-i: Resolution
## Found via the Direct-Bilinear (Explicit Component) Route

**Status:** RESOLVED. June 2026.

**Item resolved:** Appendix P v13.4, Section P.7.7.10, IVN-CT8-Dirac-1b-i
(the critical gating issue for the entire chirality/Branch-2 sector).

**Method.** Per the triangulation strategy specified in v13.4, this
document executes the **direct-bilinear route**: rather than working with
abstract $\bar\psi\Gamma\psi$ bilinears and the general Hermiticity-based
lemma (the method used in
`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` Part C, where the
inconsistency first appeared), every quantity is expressed in explicit
spinor components and differentiated directly. This removes every
opportunity for a gamma-algebra bookkeeping error to hide inside an
abstract manipulation.

---

## 1. Explicit Component Setup

Using $\gamma^5=\begin{pmatrix}0&I\\I&0\end{pmatrix}$ (derived explicitly
from $\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3$ in the established Dirac
representation) and $\psi=(\xi,\chi)^T$, direct computation gives every
bilinear in terms of $u\equiv\xi^\dagger\xi$, $v\equiv\chi^\dagger\chi$
(real, $\geq0$), and $w\equiv\xi^\dagger\chi$ (complex):

$$\eta = u-v, \qquad J^0=-(u+v), \qquad A^0=-(w+\bar w), \qquad P=i(w-\bar w)$$

All four manifestly real given $u,v$ real and $w,\bar w$ complex
conjugates, as required.

## 2. Cross-Check: the Doubled Coefficient Is Confirmed Correct

Before addressing $\dot P$, the doubled coefficient from
`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` Part B/C was independently
re-derived by varying the effective Lagrangian
$\mathcal L_{\text{eff}}=-\tfrac{3\kappa\alpha}{8}(\xi^\dagger\chi+\chi^\dagger\xi)^2$
directly with respect to $\xi^\dagger,\chi^\dagger$ as independent complex
fields (standard, unambiguous complex-field variational calculus, no
$\bar\psi/\gamma^0$ intermediary):

$$\frac{\partial\mathcal L_{\text{eff}}}{\partial\xi^\dagger} = \frac{3\kappa\alpha}{4}A^0\chi, \qquad \frac{\partial\mathcal L_{\text{eff}}}{\partial\chi^\dagger} = \frac{3\kappa\alpha}{4}A^0\xi$$

Carrying these through the same Euler-Lagrange procedure used for the
$\xi,\chi$ kinetic and mass/quartic sectors gives exactly the component
equations implied by $\Delta X\psi = -\tfrac{3i\kappa\alpha}{4}A^0\gamma^5\psi$
— matching the abstract-route result term for term. **This confirms the
doubling (from the auxiliary-field-elimination product rule) is correct.
The error is not in the coefficient magnitude.** The earlier suspicion
that Palatini-style "vary-then-substitute" logic might halve the
coefficient is ruled out.

## 3. The Full Component Equations

Assembling kinetic (friction), mass, quartic, and K-term contributions
for each component (all independently cross-checked against the abstract
$\dot\psi$ equation and found to match):

$$\dot\xi = -\frac{3H}{2}\xi + im\xi + \frac{i\lambda}{2}\eta\xi - \frac{3i\kappa\alpha}{4}A^0\chi$$

$$\dot\chi = -\frac{3H}{2}\chi - im\chi - \frac{i\lambda}{2}\eta\chi - \frac{3i\kappa\alpha}{4}A^0\xi$$

## 4. Direct Computation of $\dot P$ — Where the Bug Was

Computing $\dot w = \dot\xi^\dagger\chi+\xi^\dagger\dot\chi$ directly by
substituting the component equations and their conjugates, term by term:

$$\dot w = -3Hw - 2imw - i\lambda\eta w - \frac{3i\kappa\alpha}{4}A^0\eta$$

(using $v-u=-\eta$ to combine the cross terms $\chi^\dagger\chi$ and
$\xi^\dagger\xi$ that appear from the $K$-term pieces of $\dot\xi^\dagger\chi$
and $\xi^\dagger\dot\chi$ respectively). Taking $\dot P = i(\dot w-\dot{\bar w})$
and combining with the conjugate expression for $\dot{\bar w}$:

$$\dot P = -3HP - 2mA^0 - \lambda\eta A^0 + \frac{3\kappa\alpha}{2}\eta A^0$$

$$\boxed{\dot P = -3HP - \left(2m+\left(\lambda-\frac{3\kappa\alpha}{2}\right)\eta\right)A^0}$$

**This is manifestly real.** No residual. It also has a **different
structural form** than the abstract-lemma result in
`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` Part C, which claimed
$\dot P\big|_{\Delta X}=-\tfrac{3i\kappa\alpha}{2}A^0J^0$ — imaginary, and
dependent on $J^0$ rather than $\eta$. The dependence on $J^0$ in that
earlier result does not appear at all in the direct computation; it was
an artifact of a gamma-algebra error in that specific application of the
general lemma to the $\Gamma=\gamma^5$ case. The explicit component route,
having no abstract intermediate step where such an error could occur
unnoticed, is authoritative here.

## 5. The Remaining Two Bilinears (Confirmation, Not Correction)

For completeness, $\dot\eta$, $\dot J^0$, and $\dot A^0$ were also
recomputed via the identical explicit method:

$$\dot\eta = \dot u - \dot v = -3H\eta - \frac{3\kappa\alpha}{2}A^0P$$

$$\dot J^0 = -(\dot u+\dot v) = -3HJ^0 \quad(\text{the }A^0P\text{ terms cancel exactly between }\dot u\text{ and }\dot v)$$

$$\dot A^0 = -(\dot w+\dot{\bar w}) = -3HA^0 + (2m+\lambda\eta)P$$

These **match** what the abstract-lemma method (Part C) found for these
three quantities. Only $\dot P$ was wrong there. This is consistent with
the earlier investigation log's finding that the bug survived several
structural checks — because those checks (reality of the raw integral,
antisymmetrization linearity) were correct; the actual error was a
localized arithmetic slip in one specific gamma-matrix contraction
($\Gamma=\gamma^5$), not a conceptual flaw in the overall framework.

---

## 6. The Corrected, Fully Self-Consistent Branch 2 System

$$\dot\eta = -3H\eta - \frac{3\kappa\alpha}{2}A^0P$$
$$\dot J^0 = -3HJ^0$$
$$\dot P = -3HP - \left(2m+\left(\lambda-\frac{3\kappa\alpha}{2}\right)\eta\right)A^0$$
$$\dot A^0 = -3HA^0+(2m+\lambda\eta)P$$

All four real. All four independently derived via explicit component
computation with no abstract intermediate steps. This is offered as the
corrected canonical system for Branch 2, superseding every prior version
(v12, IVN-I, the clean-room package, and
`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` Part C).

---

## 7. The Headline Finding

**$\eta$ is sourced in Branch 2.** The clean-room package's central claim
— $\dot\eta=-3H\eta$ exactly, no sourcing, protected by the
$\gamma^0\times\text{Hermitian}$ structural argument — **does not survive**.
The general protection argument itself was not wrong for the terms it was
originally checked against (mass, quartic-$\eta$); it simply does not
extend to the self-sourced torsion term, whose contribution to $\dot\psi$
is of the anti-Hermitian-adjacent form flagged (but not resolved) at the
time.

**This differs from every prior claim about Branch 2 sourcing:**

| Source | Claimed $\dot\eta$ | Status |
|---|---|---|
| v12 / IVN-I (pre-clean-room) | $-3H\eta+\kappa\alpha A^0P$ | Superseded (convention error) |
| Clean-room package | $-3H\eta$ (no sourcing) | Superseded (missed the self-sourced torsion term entirely) |
| This document | $-3H\eta - \tfrac{3\kappa\alpha}{2}A^0P$ | Current best result |

The sign and coefficient here are new — not a confirmation of the
original IVN-I claim (different mechanism: self-sourced quartic torsion
term, not linear $(A^0,P)$ mixing) and not a confirmation of the
clean-room package's "no sourcing" claim either. This is a third,
independently-derived answer.

---

## 8. Consequences

**IVN-CT8-Dirac-1b-i is CLOSED.** The bug — a gamma-algebra error in the
abstract lemma's application to the $\Gamma=\gamma^5$ bilinear — is
identified, and the corrected system is derived and internally
consistent.

**IVN-CT8-Dirac-1b is upgraded from "internally inconsistent" to
resolved**, with the caveat that its Part A/B (operator structure,
magnitude, and the decision to treat the coupling via auxiliary-field
elimination) are all confirmed correct; only Part C's specific
$\dot P$ computation required correction, now superseded by Section 4
above.

**1c (independent re-verification of the clean-room package's $J^0,P,A^0$
contractions) should now be re-scoped**: those contractions were for the
*mass/quartic sector only* (where the clean-room package was correct) and
do not need re-verification; what does need independent re-verification
is the *torsion sector* result derived in this document — recommend a
fresh 1c pass specifically targeting Section 4 and 6 above.

**Freeze status.** The freeze on P.9.4.2, P.9.5.3, P.7.7.3, P.7.7.3a, and
CT-ix Section P.10.5 should be **maintained until this document itself is
independently verified** — it resolves the internal-inconsistency problem
that triggered the freeze, but a single successful derivation, however
carefully cross-checked internally, is not yet "independently verified"
in the sense the freeze protocol requires. Recommend: one independent
re-derivation via the **4D-first route** (the one triangulation leg not
yet attempted) before lifting the freeze and performing the single-pass
canonical rewrite of the frozen sections.

**Physical consequence, pending the freeze lift.** If this result holds,
Branch 2 is not the simple "$\eta$ decouples, only rebuild the $(A^0,P)$
oscillator" picture anticipated after 1a closed — nor is it the fully
decoupled system the clean-room package claimed. It is a genuinely
coupled three-variable $(\eta,P,A^0)$ system (with $J^0$ decoupling
cleanly, diluting as pure $a^{-3}$ throughout). The CT-ix Branch 2
late-time-attractor analysis, the bounce-condition scaling argument, and
the PT-1 monodromy phase estimate all need to be rebuilt from this
corrected three-variable system once independently verified.

---

*SCH IVN-CT8-Dirac-1b-i Resolution — v1 | June 2026*
*Closes IVN-CT8-Dirac-1b-i. Recommends one further independent check
(4D-first route) before the freeze is lifted. Not for citation without
author approval pending that check.*
