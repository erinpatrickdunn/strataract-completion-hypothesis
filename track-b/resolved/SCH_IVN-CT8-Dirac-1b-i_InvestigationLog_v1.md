# SCH — IVN-CT8-Dirac-1b-i: Investigation Log
## Hunting the Imaginary Residual in $\dot P$

**Status:** OPEN — substantial partial progress, resolution not found.
June 2026

**Item under investigation:** Appendix P v13.3, Section P.7.7.10,
sub-item IVN-CT8-Dirac-1b-i, opened by
`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` Part C.

**Purpose of this document.** Report what was checked, what was ruled out,
and what remains genuinely unresolved, honestly and without manufacturing
a closure. This is a negative-and-partial result: several plausible bug
locations were checked and eliminated with reasonable confidence; the
actual source of the inconsistency was not found.

---

## 1. What Was Re-Checked

### 1.1 Independent re-verification: is the raw kinetic integral really imaginary?

Part A/B of the 1b document established that the raw spatial contorsion
contribution to the kinetic integral, $Y\propto(A^0)^2$ with an explicit
factor of $i$, is imaginary — requiring the standard antisymmetrization
$\frac{i}{2}(Y-Y^\dagger)$ to extract a real Lagrangian term — via the
specific chain of substitutions used there ($\gamma_j\gamma_k\to-i\gamma^0\gamma_i\gamma^5$,
then contraction with the outer $\gamma^i$).

This was re-checked here by an **independent route**: classifying the
bilinear covariant type of $\Gamma=\gamma^i\gamma^j\gamma^k$ (three
distinct spatial gamma matrices, no $\gamma^5$ substitution at all)
directly against the Step-0 reality rules. Result: $\Gamma^\dagger=-\Gamma$
(anti-Hermitian, via reversing the order of three mutually anticommuting
Hermitian matrices), and checking the full reality condition
($\Gamma$ must commute with $\gamma^0$ for $\bar\psi\Gamma\psi$ to be
real) shows $\Gamma$ anticommutes with $\gamma^0$ instead — confirming
$\bar\psi\gamma^i\gamma^j\gamma^k\psi$ is imaginary, independent of and
consistent with Part A/B's finding via the $\gamma^5$-substitution route.

**Conclusion: the raw-integral-is-imaginary, antisymmetrization-produces-a-real-quartic-term
step is confirmed correct via two independent methods. This is not the
source of the inconsistency.**

### 1.2 Independent re-verification: is $\dot P$'s imaginary residual a lemma-application error?

Part C derived $\dot P\big|_{\Delta X}=-\tfrac{3i\kappa\alpha}{2}A^0J^0$
using the general lemma $\dot B_\Gamma=-3HB_\Gamma+\psi^\dagger[\Delta X^\dagger\gamma^0\Gamma+\gamma^0\Gamma\Delta X]\psi$.
This was re-derived here **without using the lemma at all** — direct,
fully explicit computation of $\dot\psi^\dagger\gamma^0\gamma^5\psi+\psi^\dagger\gamma^0\gamma^5\dot\psi$
from the complete assembled $\dot\psi = -\tfrac{3H}2\psi+(m+\tfrac\lambda2\eta)\gamma^0\psi+\Delta X\psi$
and its conjugate, tracking every term:

$$\dot P = -3HP - 2\left(m+\frac\lambda2\eta\right)A^0 - \frac{3i\kappa\alpha}{2}A^0J^0$$

**Identical result.** The mass/quartic-$\eta$ contributions and the
Hubble friction reproduce exactly what the earlier, lemma-based
computation gave, and the imaginary residual reappears with the same
coefficient. This rules out "the general lemma was misapplied to a term
of unexpected structure" as the explanation — the direct computation,
which makes no structural assumption about $\Delta X$ at all, gives the
same answer.

### 1.3 Re-checked: does treating the Levi-Civita and contorsion pieces of $D_i\psi$ separately drop a cross-term?

The full spatial covariant derivative is $D_i\psi = D_i\psi\big|_{\text{LC}} + D_i\psi\big|_K$
(linear sum). The kinetic Lagrangian contribution is
$\bar\psi\gamma^ie^i{}_iD_i\psi = \bar\psi\gamma^ie^i{}_iD_i\psi\big|_{\text{LC}} + \bar\psi\gamma^ie^i{}_iD_i\psi\big|_K$,
and the antisymmetrization $X\mapsto\frac i2(X-X^\dagger)$ is linear in
$X$, so it distributes over this sum with no cross-terms. This is a basic
property of Hermitian conjugation and addition, not an assumption specific
to this calculation, and was re-confirmed by explicitly writing out the
distribution. **Ruled out as the source.**

---

## 2. What Remains Unresolved

None of the checks above located the missing piece. The imaginary
residual in $\dot P$ is robust across three independent computational
routes (the original lemma-based derivation, the from-scratch direct
computation, and cross-checking the antecedent steps that feed into
both). This strongly suggests the problem is not a mechanical slip in
Part C's arithmetic, nor in how the general lemma is applied — it is
either (a) a genuine conceptual gap in how the self-sourced (quartic)
contorsion term should be incorporated into the antisymmetrized kinetic
construction, not yet identified, or (b) an error further upstream in
Part A's derivation of the raw coupling that survives the two independent
checks performed so far because those checks tested internal consistency
of what was derived, not whether the underlying physical setup (e.g., the
choice to treat *only* the spatial covariant derivative as contorsion-bearing,
per P.9.3's "purely spatial" torsion, or the specific way the algebraic
torsion solution was substituted) is complete.

**Best remaining hypothesis (unconfirmed):** the antisymmetrization
prescription $\frac{i}{2}(X-X^\dagger)$, as used throughout this
framework, was originally justified and verified only for $X$ linear in
$\psi$ (ordinary kinetic and mass-type terms, where $\bar\psi\Gamma\psi$
is genuinely bilinear in the field). The contorsion-sourced piece is
quartic in $\psi$ (since it is built from $\bar\psi\gamma^ie^i{}_iD_i\psi$
where $D_i\psi$ itself contains a bilinear-in-$\psi$ coefficient). While
the algebraic identity $\frac i2(X-X^\dagger)=i\,\mathrm{Im}(X)$ is
degree-independent as a statement about complex numbers, it is not yet
established here that treating the quartic term as an ordinary additive
Lagrangian piece — to be varied by the standard product rule exactly as
if it were any other potential term — is the complete and correct
treatment for a term that arose via auxiliary-field elimination
specifically. This is a real possibility that has not been checked, only
flagged.

This hypothesis is not verified. It is reported as the most promising
remaining direction, not as a finding.

---

## 3. Disposition

**IVN-CT8-Dirac-1b-i remains OPEN.** This document adds genuine value —
three candidate error locations are now ruled out with reasonable
confidence — but does not close the item. The recommended next step is
not further re-derivation along the same lines (which has now been
tried three ways with consistent results) but a more fundamental check
of whether the standard antisymmetrized-kinetic-term construction, as
used throughout this framework since v8, actually generalizes correctly
to self-sourced (auxiliary-field-eliminated) quartic terms — possibly
requiring consultation of the broader Einstein-Cartan-Dirac literature's
treatment of this specific point (how the four-fermion term's variation
should be normalized relative to the original antisymmetrized kinetic
prescription), rather than a re-derivation internal to this framework's
own conventions.

**Consequence for the freeze.** No change. The freeze on P.9.4.2,
P.9.5.3, P.7.7.3, P.7.7.3a, and CT-ix Section P.10.5 remains in effect.
Whether $\eta$ is protected in Branch 2 remains reopened, not confirmed,
exactly as stated in Appendix P v13.3. This investigation neither
strengthens nor weakens that status — it narrows the search for the
answer without providing it.

---

*SCH IVN-CT8-Dirac-1b-i Investigation Log — v1 | June 2026*
*Partial progress; item remains open. Three candidate error locations
ruled out. Not for citation without author approval.*
