# SCH — IVN-CT8-Dirac-1b: Canonical Re-Derivation of the Torsion Coupling
## Under the Post-1a Convention Lock

**Status:** PARTIAL — operator structure confirmed; a genuine unresolved
inconsistency is surfaced and tracked as a new sub-item, not resolved.
June 2026

**Item under audit:** Appendix P v13.2, Section P.7.7.10, sub-item
IVN-CT8-Dirac-1b. Maps to CR-3 in `SCH_CleanRoom_Rederivation_v1.md`.

**Framing.** The clean-room package imported the axial coupling
$\tfrac{\kappa\alpha}{2}A^0\gamma^0\gamma^5\psi$ from the established Cartan
equation normalization, verifying only that it must carry a real
coefficient (from the general kinetic-sector reality argument) and not
re-deriving its magnitude or operator structure from the raw contorsion
tensor. This item does that re-derivation, under the convention locked by
1a. It should be read in two parts with different confidence levels: Part A
is a clean, verified derivation. Part B/C surfaces a genuine open problem
that this document does not resolve.

---

## Part A — The Raw Kinetic-Integral Contribution (Confirmed)

**Contorsion from the Cartan equation.** For totally antisymmetric torsion
(guaranteed here since $T_{\lambda\mu\nu}\propto\varepsilon_{\lambda\mu\nu\rho}A^\rho$
is manifestly totally antisymmetric), the standard Einstein-Cartan relation
between contorsion and torsion simplifies to $K_{abc}=\tfrac12T_{abc}$ (a
direct consequence of total antisymmetry combined with the general
formula $K_{abc}=\tfrac12(T_{abc}+T_{bca}-T_{cab})$, since cyclic
permutations of a totally antisymmetric rank-3 tensor are all equal). For
purely temporal $A^\mu=(A^0,0,0,0)$, this gives purely spatial contorsion
$K_{ijk}=\tfrac{\kappa\alpha}4\varepsilon_{ijk0}A^0$ (spatial frame indices
$i,j,k$), consistent with Appendix P Section P.9.3's stated purely-spatial
torsion structure. (The overall sign here depends on the $\varepsilon$-tensor
orientation convention and is flagged, not fully pinned down — see
Residual Items below; the magnitude and index structure are not affected
by this ambiguity.)

**Contribution to the covariant derivative.** For the homogeneous ansatz
$\psi=\psi(t)$, $D_i\psi \supset \tfrac14K_i{}^{jk}[\gamma_j,\gamma_k]\psi$.
Using the identity (derived directly from $\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3$
and the Clifford anticommutation relations, verified independently for
all three cyclic cases): for $(i,j,k)$ any cyclic permutation of $(1,2,3)$,
$$\gamma_j\gamma_k = -i\,\gamma^0\gamma_i\gamma^5$$
the contorsion contribution to $D_i\psi$ reduces, after the diagonal
tetrad factors $e_{(i)}$ cancel exactly against the inverse tetrad in the
kinetic integral $\bar\psi\gamma^ie^i{}_iD_i\psi$, to a **position-independent**
result (no residual $S^3$-angular dependence, as required for consistency
with the homogeneous ansatz). Using $\gamma^i\gamma^0\gamma_i\gamma^5=-\gamma^0\gamma^5$
(no sum; $(\gamma^i)^2=+1$) and summing the three spatial directions
(each contributing identically by the symmetric result above):

$$\sum_{i=1}^3\bar\psi\gamma^ie^i{}_iD_i\psi\Big|_{K\text{-piece}} = \frac{3i\kappa\alpha}{8}A^0\,\bar\psi\gamma^0\gamma^5\psi = \frac{3i\kappa\alpha}{8}(A^0)^2$$

using $\bar\psi\gamma^0\gamma^5\psi=A^0$ (the bilinear is built from the same
$\psi$ — see Part B).

**Confirmed: the operator structure is $\gamma^0\gamma^5$**, derived
directly from the index contraction rather than assumed, and the raw
magnitude traces consistently to the established $\kappa\alpha$
normalization (with an overall numerical factor of 3/8 from summing the
three spatial directions and the $\tfrac14[\gamma_j,\gamma_k]=\tfrac12\gamma_j\gamma_k$
prefactor — this factor is new information not previously stated
anywhere in the appendix, and should be independently re-checked, but
the derivation producing it is complete and internally consistent).

---

## Part B — The Self-Sourcing Problem

The result above already reveals $\bar\psi\gamma^0\gamma^5\psi=A^0$
appearing where a supposedly *external* background field was expected.
This is the crux of what 1b needed to check and the clean-room package
did not: **$A^0$ is not an external field.** It is a bilinear of the same
$\psi$ whose equation of motion is being derived. Torsion in
Einstein-Cartan theory has no independent kinetic term — it is fixed
algebraically by the Cartan equation (P.1.3), which is exactly why
Appendix P Theorem 4 describes Term 3 as a "contact interaction." The
textbook-correct way to handle a non-dynamical (auxiliary) field sourced
by the dynamical field itself is to substitute its algebraic solution
into the action *before* varying with respect to the dynamical field —
not to treat it as fixed background during that variation. This is a
standard field-theory technique (integrating out a non-propagating
auxiliary field), and it is the mechanism, well documented in the
Einstein-Cartan-Dirac literature (Hehl et al. 1976, already cited in this
framework), by which spin-torsion coupling generically produces an
effective four-fermion self-interaction rather than a simple linear
coupling to a background.

Applying this correctly: the raw result above, treated as a term in the
**Lagrangian** rather than prematurely read off as a term in the equation
of motion, is

$$\mathcal L_{\text{eff,torsion}} = -\frac{3\kappa\alpha}{8}(A^0)^2$$

after the standard $\tfrac{i}{2}(X-\text{h.c.})$ antisymmetrization (the
term is real, so this antisymmetrization doubles rather than cancels it —
confirmed by direct computation, and consistent with $(A^0)^2$ being one
of the "good," already-real bilinear-squared combinations per the Step 0
classification). This is a genuine quartic self-interaction term, and its
structural form — quadratic in the axial current — is a good consistency
check: it matches the pre-existing "Term 3 $\sim A_\mu A^\mu$" language
already used elsewhere in Appendix P and Paper A (Section 2.1, "Term 3").

---

## Part C — Where the Derivation Breaks, and Why This Item Is Not Closed

Varying $\mathcal L_{\text{eff,torsion}}$ with respect to $\bar\psi$ using
the ordinary product rule (the same rule already validated, in the
clean-room package, for the structurally identical $\tfrac\lambda4(\bar\psi\psi)^2$
term) gives $\tfrac{\partial}{\partial\bar\psi}\mathcal L_{\text{eff,torsion}} =
-\tfrac{3\kappa\alpha}{4}A^0\gamma^0\gamma^5\psi$. This was independently
cross-checked via the chain rule through $\psi^\dagger$ rather than
$\bar\psi$ directly, and the two methods agree exactly — this specific
step is not in question.

Carrying this term through the full Euler-Lagrange procedure (the same
$\gamma^0$-multiplication-and-division sequence used throughout the
clean-room package, re-verified three times independently here after an
initial sign-tracking slip was caught and corrected) yields an additional
term in $\dot\psi$:

$$\Delta X\,\psi = -\frac{3i\kappa\alpha}{4}A^0\,\gamma^5\,\psi$$

**This term does not have the protected $\gamma^0\times\text{Hermitian}$
form** that 1a's audit showed is required of any term consistent with a
real action (checking directly: $\Delta X=\gamma^0 W$ requires
$W=-i\cdot\tfrac{3\kappa\alpha}{4}A^0\cdot\gamma^0\gamma^5$, and $i\times$Hermitian
is anti-Hermitian, not Hermitian, for any nonzero real coefficient). This
by itself would be a red flag suggesting an arithmetic error — except
that computing this term's *direct* contribution to $\dot\eta$
(bypassing the general lemma, which assumed the protected form and does
not directly apply here) gives a clean, fully real result:

$$\dot\eta\Big|_{\Delta X} = -\frac{3\kappa\alpha}{2}A^0P$$

— tantalizingly close in form to IVN-I's original (superseded) claim,
though via an entirely different mechanism (self-sourced torsion quartic
term, not a linear $(A^0,P)$ mixing system) and a different numerical
coefficient. This is a real, self-consistent partial result.

**However**, applying the identical procedure to compute this same term's
contribution to $\dot P$ produces:

$$\dot P\Big|_{\Delta X} = -\frac{3i\kappa\alpha}{2}A^0J^0$$

**— an explicit, unremoved factor of $i$.** Since $P$, $\kappa$, $\alpha$,
$A^0$, and $J^0$ are all real, this cannot be correct: $\dot P$ must be
real. This was re-derived from the general lemma
$\dot B_\Gamma=-3HB_\Gamma+\psi^\dagger[\Delta X^\dagger\gamma^0\Gamma+\gamma^0\Gamma\Delta X]\psi$
with $\Gamma=\gamma^5$, checked twice, and the imaginary residual persists.

**This is a genuine, unresolved inconsistency, not a typo to be patched.**
The most likely diagnosis: something about how the antisymmetrized
kinetic-term construction interacts with substituting a *self-referential*
background (as opposed to a genuinely external one) before varying is not
being handled completely correctly here — possibly an additional term
from properly antisymmetrizing the *full* self-consistent kinetic
integral (not just the derived effective Lagrangian piece) that has not
been accounted for. This document does not identify the missing piece.

**IVN-CT8-Dirac-1b is therefore NOT CLOSED.** What is established:

1. The raw (linear, external-field-treated) operator structure is
   $\gamma^0\gamma^5$, confirmed by direct index contraction (Part A —
   solid).
2. The coupling is genuinely self-sourced and requires auxiliary-field
   elimination treatment, producing a real quartic effective Lagrangian
   term matching the expected $A_\mu A^\mu$ structure (Part B — solid).
3. Varying that term correctly produces an internally inconsistent
   result (an imaginary residual in $\dot P$) that this document could
   not resolve (Part C — **open**).

**New sub-item opened: IVN-CT8-Dirac-1b-i** — identify and fix whatever is
missing in the self-consistent (auxiliary-field-elimination) treatment of
the torsion-sourced quartic term, such that all four resulting bilinear
equations ($\dot\eta$, $\dot J^0$, $\dot P$, $\dot A^0$) come out
simultaneously real. Until this closes, **the $\dot\eta=-3H\eta$ protection
result from the clean-room package's Steps 1–3 should be understood as
established only for the mass/quartic-$\eta$ sector in isolation** — i.e.,
Branch 1 (where $A^0=0$ identically and this entire question is moot) is
unaffected, but the question of whether $\eta$ is exactly protected in
Branch 2 is **reopened**, not confirmed, pending 1b-i.

---

## Residual Items (Lower Priority, Noted for Completeness)

- The overall sign of the $\varepsilon_{ijk0}$ contraction (Part A) depends
  on an orientation convention for the 4D Levi-Civita symbol not
  independently fixed in this document; it affects only the sign of the
  raw coupling, not the operator structure or the Part B/C findings.
- The factor of 3/8 (from summing three spatial directions) in the raw
  Part A result is new and has not been cross-checked against any
  existing statement in the appendix (no prior document gave this
  magnitude explicitly) — recommend independent re-verification alongside
  1c.

---

## Consequence for Sequencing

Per Appendix P v13.2 Section P.7.7.10, 1b and 1c were unblocked to proceed
in parallel following 1a's closure. **1b is now partially complete and has
generated a new blocking sub-item, 1b-i, which should be prioritized
alongside — not after — 1c**, since 1c (re-verifying the clean-room
package's $J^0$/$P$/$A^0$ contractions) and 1b-i (fixing the self-sourcing
treatment) both bear directly on whether the Branch 2 bilinear system is
even internally consistent, and are likely easier to resolve together
than in isolation. **The freeze on P.9.4.2, P.9.5.3, P.7.7.3, P.7.7.3a, and
CT-ix Section P.10.5 remains firmly in effect** — if anything, this
finding strengthens the case for the freeze, since it shows the Branch 2
question is more unsettled than even the v13.2 status suggested.

---

*SCH IVN-CT8-Dirac-1b — v1 | June 2026*
*Partial result. Opens IVN-CT8-Dirac-1b-i as a new tracked sub-item.*
*Not for citation without author approval. Do not treat the $-\tfrac{3\kappa\alpha}2A^0P$*
*figure in Part C as established — it is reported as a waypoint alongside*
*an unresolved inconsistency, not as a validated correction to Appendix P.*
