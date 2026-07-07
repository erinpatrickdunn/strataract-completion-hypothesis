# SCH — IVN-CT8-Dirac-1a: Formal Convention Audit
## Is the Bare-γ⁰ Adjoint Forced, or Merely Convenient?

**Status:** CLOSED | June 2026

**Item under audit:** Appendix P v13.1, Section P.7.7.10, sub-item
IVN-CT8-Dirac-1a — the gating item for IVN-CT8-Dirac-1. Maps to CR-1 in
`SCH_CleanRoom_Rederivation_v1.md`.

**Question.** The clean-room package derived $\eta$'s protection theorem
using a specific adjoint convention, $\bar\psi\equiv\psi^\dagger\gamma^0$
(bare, no compensating factor), under which $\eta=\bar\psi\psi$ came out
*imaginary* and required an explicit corrective definition
$\eta\equiv-i\bar\psi\psi$ to be made real, while $J^\mu=\bar\psi\gamma^\mu\psi$
required no such correction. Before trusting any dynamics built on this
choice, this audit asks: is that choice forced, or is there some other
Hermitian, invertible intertwiner $A$ under which $\eta$ and $J^\mu$ are
*both* real without an asymmetric compensating factor? If such an
alternative exists, the protection theorem needs to be rechecked under it
before IVN-CT8-Dirac-1b/1c proceed.

This audit is deliberately self-contained: no dynamics, no equations of
motion, no Lagrangian — a pure question about the Clifford algebra and its
admissible adjoints, answered before any further physics is built on top
of it, per the instruction that this be "a formal convention audit before
any further dynamics."

---

## 1. The General Reality Condition

For a bilinear $B_\Gamma \equiv \bar\psi\Gamma\psi = \psi^\dagger A\Gamma\psi$
(with $\bar\psi\equiv\psi^\dagger A$ for some fixed invertible matrix $A$),
Hermitian conjugation gives $B_\Gamma^\dagger = \psi^\dagger\Gamma^\dagger
A^\dagger\psi$. For $B_\Gamma$ to be real for every spinor $\psi$, the
matrix $A\Gamma$ must itself be Hermitian:
$$(A\Gamma)^\dagger = A\Gamma \quad\Longleftrightarrow\quad \Gamma^\dagger A^\dagger = A\Gamma$$

This is representation-complete: since the sixteen basis elements
$\{\mathbb 1,\gamma^\mu,\gamma^{\mu\nu},\gamma^\mu\gamma^5,\gamma^5\}$ span the
full space of $4\times4$ matrices, any candidate $A$ is reachable by this
kind of analysis without loss of generality; no ansatz is being smuggled
in by restricting to "matrices built from gammas."

**Requiring reality for $\Gamma=\mathbb 1$:** $A^\dagger=A$ — $A$ must be
Hermitian.

**Requiring reality for $\Gamma=\gamma^a$ ($a=0,1,2,3$), given $A$ Hermitian:**
$$\gamma^{a\dagger}A = A\gamma^a \quad\Longleftrightarrow\quad A\gamma^aA^{-1}=\gamma^{a\dagger}$$

Using the Hermiticity assignment established in the clean-room package's
Step 0 ($\gamma^{0\dagger}=-\gamma^0$, $\gamma^{i\dagger}=+\gamma^i$ for
$i=1,2,3$, forced by $(\gamma^0)^2=-\mathbb1$, $(\gamma^i)^2=+\mathbb1$ in the
$(-,+,+,+)$ signature), this becomes two separate conditions:

$$A\gamma^0A^{-1} = -\gamma^0 \quad(\text{i.e. } A \text{ anticommutes with } \gamma^0)$$
$$A\gamma^iA^{-1} = +\gamma^i \quad(\text{i.e. } A \text{ commutes with each } \gamma^i,\ i=1,2,3)$$

**The question reduces to:** find all Hermitian, invertible $4\times4$
matrices $A$ that commute with $\gamma^1,\gamma^2,\gamma^3$ and anticommute
with $\gamma^0$.

---

## 2. Solving the Constraint System

Working in the standard Dirac representation (mostly-plus, via
$\gamma^a_{\text{mp}}=i\gamma^a_{\text{mm}}$ rescaling of the standard
mostly-minus matrices, as in the clean-room package):
$$\gamma^0 = \begin{pmatrix}iI&0\\0&-iI\end{pmatrix}, \qquad \gamma^i = \begin{pmatrix}0&i\sigma^i\\-i\sigma^i&0\end{pmatrix}$$

Write $A$ in $2\times2$ block form, $A=\begin{pmatrix}A_{11}&A_{12}\\A_{21}&A_{22}\end{pmatrix}$.

**Step 2.1 — Commutation with $\gamma^1,\gamma^2,\gamma^3$.** Expanding
$A\gamma^i=\gamma^iA$ block-by-block and matching coefficients gives four
matrix equations. Two of them, $A_{11}\sigma^i=\sigma^iA_{22}$ (for all
$i=1,2,3$), force $A_{11}=A_{22}=c\,I$ for a scalar $c$: this is a direct
consequence of the Pauli matrices generating an *irreducible* action on
$\mathbb C^2$ (Schur's lemma) — no non-scalar $2\times2$ matrix can
intertwine all three simultaneously.

The remaining two equations, $A_{12}\sigma^i=-\sigma^iA_{21}$ for all $i$,
are solved by decomposing $A_{12}=a_0\mathbb1+\vec a\cdot\vec\sigma$,
$A_{21}=b_0\mathbb1+\vec b\cdot\vec\sigma$ and matching coefficients of
$\mathbb1$ and each $\sigma^k$ using $\sigma^i\sigma^j=\delta^{ij}\mathbb1+i\epsilon^{ijk}\sigma^k$.
This forces $\vec a=\vec b=0$ (the cross-product terms must vanish in every
direction simultaneously, which only a zero vector satisfies) and
$b_0=-a_0$. So:

$$A_{11}=A_{22}=c\,I, \qquad A_{12}=a_0 I,\qquad A_{21}=-a_0 I$$

for free complex scalars $c,a_0$ — the full centralizer of the spatial
Clifford subalgebra in this representation, as expected.

**Step 2.2 — Anticommutation with $\gamma^0$.** Substituting the block form
above into $A\gamma^0=-\gamma^0A$ and comparing diagonal blocks forces
$c=0$; the off-diagonal blocks are automatically consistent for any $a_0$.

**Step 2.3 — Hermiticity.** With $c=0$, $A=\begin{pmatrix}0&a_0I\\-a_0I&0\end{pmatrix}$.
Requiring $A^\dagger=A$ forces $a_0=-\bar a_0$, i.e. $a_0$ purely imaginary:
$a_0=ir$ for real $r$.

**Result:**
$$\boxed{A = r\,\begin{pmatrix}0&iI\\-iI&0\end{pmatrix}, \qquad r\in\mathbb R\setminus\{0\}}$$

a one-real-parameter family, unique up to overall real rescaling — not a
richer family of genuinely inequivalent choices.

---

## 3. Identifying the Solution

Direct computation identifies this matrix: $\gamma^0_{\text{mm}}\gamma^5 =
\mathrm{diag}(I,-I)\begin{pmatrix}0&I\\I&0\end{pmatrix} = \begin{pmatrix}0&I\\-I&0\end{pmatrix}$
(using the standard chiral $\gamma^5=\begin{pmatrix}0&I\\I&0\end{pmatrix}$ in
this representation). Since $\gamma^0_{\text{mp}}=i\gamma^0_{\text{mm}}$:

$$A = r\,\gamma^0\gamma^5$$

**The unique alternative intertwiner (up to real scaling) is $\gamma^0\gamma^5$.**
There is no third option, and bare $\gamma^0$ itself is not a solution to
this combined system (consistent with it being exactly the source of the
original problem: bare $\gamma^0$ satisfies the vector-reality requirement
alone, not the combined scalar+vector requirement).

---

## 4. What the Alternative Actually Means Physically

Adopting $A=\gamma^0\gamma^5$ as the adjoint (setting $r=1$ without loss of
generality) and evaluating what the resulting "scalar" and "current"
bilinears are, expressed back in terms of the *original*, bare-$\gamma^0$
bilinear vocabulary already established in the clean-room package:

$$\text{"new scalar"} = \bar\psi'\psi = \psi^\dagger\gamma^0\gamma^5\psi = \psi^\dagger\gamma^0\cdot\gamma^5\psi = \bar\psi\gamma^5\psi \Big|_{\text{bare}} = P$$

$$\text{"new current, time component"} = \bar\psi'\gamma^0\psi = \psi^\dagger\gamma^0\gamma^5\gamma^0\psi = \psi^\dagger\gamma^5\psi \quad(\text{using } \gamma^5\gamma^0=-\gamma^0\gamma^5,\ (\gamma^0)^2=-1)$$

The second quantity is (up to the sign convention already fixed in the
clean-room package) the **axial charge** $A^0$, not a probability density.

**The alternative intertwiner does not rescue $\eta$ and $J^\mu$ in their
intended physical roles — it exists mathematically, but achieves
simultaneous reality only by exchanging labels:**

| Under bare $\gamma^0$ (clean-room choice) | Under $\gamma^0\gamma^5$ (alternative) |
|---|---|
| $\eta=\bar\psi\psi$ — imaginary, needs $-i$ correction | "new scalar" $=P$ — real, no correction needed |
| $J^0=\bar\psi\gamma^0\psi$ — real, $\propto -\vert\psi\vert^2$ (fixed sign) | "new $J^0$" $=\psi^\dagger\gamma^5\psi$ — **no fixed sign relative to $\vert\psi\vert^2$** ($\gamma^5$ has eigenvalues $\pm1$) |

The second row is the decisive physical disqualifier. The ordinary,
non-negotiable requirement on a Dirac current's time component is that it
track $\vert\psi\vert^2$ with a fixed sign — this is what makes $J^0$
interpretable as a probability/charge density in the first place. The
alternative intertwiner's "current" fails this outright: $\psi^\dagger\gamma^5\psi$
can take either sign depending on the spinor's chirality content, exactly
as expected for an axial rather than a vector-type quantity. It is not a
viable substitute for $J^0$ under any relabeling.

---

## 5. Conclusion

**IVN-CT8-Dirac-1a is CLOSED.** The audit is complete and admits no loose
ends: the constraint system was solved exactly (not approximately or
perturbatively), the solution set is a one-parameter family unique up to
real rescaling, and that unique alternative was checked and found to fail
the minimal physical requirement on $J^0$.

**Finding:** Once the standard requirement that $J^0$ retain a fixed sign
relative to $\vert\psi\vert^2$ (the ordinary probability/charge-density
role) is imposed, the bare-$\gamma^0$ adjoint is the *unique* viable
choice among Hermitian intertwiners achieving simultaneous scalar+vector
reality by any means. Consequently, $\eta$'s compensating factor
$\eta\equiv-i\bar\psi\psi$ is **forced by the physics, not an artifact of
an arbitrary convention choice.** The clean-room package's central
protection theorem for $\eta$ ($\dot\eta=-3H\eta$ exactly, no
$\kappa\alpha A^0P$ source term) does not need to be rechecked under a
different representation, because no viable different representation
exists.

**Consequence for sequencing.** Per Appendix P v13.1 Section P.7.7.10,
IVN-CT8-Dirac-1a was the gating item for 1b and 1c. It is now closed in
favor of the clean-room package's original convention. **IVN-CT8-Dirac-1b
(contorsion coefficient re-derivation) and IVN-CT8-Dirac-1c (independent
re-verification of the $J^0,P,A^0$ bilinear contractions) may now proceed
in parallel**, as originally sequenced. IVN-CT8-Dirac-1d (reconciling
$\eta\equiv-i\bar\psi\psi$ with Theorem 0's literal statement) is also
unblocked and is, in light of this audit, now a purely notational
reconciliation rather than an open physics question — Theorem 0's content
is confirmed unaffected.

**One remaining curiosity, noted but out of scope here.** This audit does
not check whether "$P$" (the quantity that *would* play the "new scalar"
role under the alternative adjoint) itself satisfies an analogous
protection theorem under its own natural dynamics. That would require
re-deriving the equation of motion's structure relative to the
$\gamma^0\gamma^5$ adjoint — a distinct, parallel exercise, not required to
close 1a, since 1a's purpose was only to check whether the *original*
choice was forced. It is noted here in case it becomes relevant to later
work on $P$'s own dynamics (already derived, under the bare adjoint, in
the clean-room package's Step 3).

---

## Status Update for Appendix P v13.1 / Tracking

This closes IVN-CT8-Dirac-1a with the following disposition, to be
reflected in Appendix P Section P.7.7.10's tracking table:

| Item | Status | Disposition |
|---|---|---|
| IVN-CT8-Dirac-1a | **CLOSED** | Bare-$\gamma^0$ adjoint confirmed forced (unique viable choice given $J^0$'s required fixed-sign character). Clean-room protection theorem for $\eta$ validated, not merely assumed. |
| IVN-CT8-Dirac-1b | **UNBLOCKED** | May proceed. |
| IVN-CT8-Dirac-1c | **UNBLOCKED** | May proceed, in parallel with 1b. |
| IVN-CT8-Dirac-1d | **UNBLOCKED, DOWNGRADED TO NOTATIONAL** | Theorem 0's content confirmed unaffected; only the literal formula needs the explicit $-i$ made visible. |

---

*SCH IVN-CT8-Dirac-1a Convention Audit — v1 | June 2026*
*Closes the gating item for IVN-CT8-Dirac-1 (Appendix P v13.1, Section P.7.7.10).*
*Not for citation without author approval. No further verification items opened by this audit.*
