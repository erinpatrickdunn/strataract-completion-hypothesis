# SCH — Clean-Room Re-Derivation Package
## Steps 1–4: Torsion-Free and Torsion-Active FLRW Dirac Equations, Bilinear ODE System, and Comparison

**Status:** WORKING DOCUMENT — v1 | June 2026

**Purpose.** IVN-I-3 could not be resolved by patching the existing $(A^0,P)$
system in place: doing so surfaced an unresolved imaginary residual (see the
chat record immediately preceding this document) and, on inspection, an
apparent double-counting bug in Appendix P Section P.9.4.2. Rather than
patch further, this document re-derives the cosmological Dirac equation and
its bilinear consequences from scratch, in a single, explicitly audited
convention, following the five-step order specified for this package. Steps
1 through 4 are executed here. **Step 5 (updating CT-viii/CT-ix) is
deliberately not performed in this document** and should not be undertaken
until this package itself has been independently checked — see the
Verification Status section at the end.

**Headline finding.** The re-derivation does not merely resolve IVN-I-3. It
finds that IVN-I's own corrected system (Appendix P v13, Section P.7.7.3,
equations E1-new/E-A-new/E-P-new) does not survive a fully reality-audited
re-derivation. The apparent $\kappa\alpha A^0 P$ sourcing of $\eta$ in Branch
2 — the centerpiece of IVN-I's contribution — is not present in the
corrected system derived below. Its origin is traced to an unaudited
assumption about which fermion bilinears are real in the $(-,+,+,+)$
Clifford algebra, an assumption inherited (unexamined) by every version of
this calculation back through v12.

---

## Step 0 — Convention Fixing and Bilinear Reality Audit

*(Not one of the five requested steps, but a necessary prerequisite — see
Conclusion for why skipping this step is what caused every prior version of
this calculation to go wrong.)*

**Signature and Clifford algebra.** Metric signature $(-,+,+,+)$, matching
Appendix P Section P.9.1. Flat-frame gamma matrices satisfy
$\{\gamma^a,\gamma^b\}=2\eta^{ab}\mathbb{1}$, $\eta^{ab}=\mathrm{diag}(-1,1,1,1)$,
giving $(\gamma^0)^2=-\mathbb{1}$, $(\gamma^i)^2=+\mathbb{1}$ ($i=1,2,3$).

**Hermiticity assignment.** Consistency with a unitary representation in
this signature forces:
$$\gamma^{0\dagger}=-\gamma^0 \quad(\text{anti-Hermitian}), \qquad \gamma^{i\dagger}=+\gamma^i \quad(\text{Hermitian})$$
Define $\gamma^5\equiv i\gamma^0\gamma^1\gamma^2\gamma^3$, which is Hermitian,
satisfies $(\gamma^5)^2=+\mathbb{1}$, and anticommutes with every $\gamma^a$
(standard Clifford algebra facts, not re-derived here).

**Dirac adjoint.** Fixed once, used everywhere below without modification:
$$\bar\psi \equiv \psi^\dagger\gamma^0 \qquad(\text{bare — no compensating factor of } i)$$

**Reality audit of every bilinear used in this framework.** For a bilinear
$B_\Gamma\equiv\bar\psi\Gamma\psi=\psi^\dagger\gamma^0\Gamma\psi$, Hermiticity
gives $B_\Gamma^\dagger = \psi^\dagger\Gamma^\dagger\gamma^{0\dagger}\psi=
-\psi^\dagger\Gamma^\dagger\gamma^0\psi$. Direct computation, case by case:

| Bilinear | Definition | $B^\dagger$ vs. $B$ | Reality |
|---|---|---|---|
| $J^0$ | $\bar\psi\gamma^0\psi$ | $J^{0\dagger}=J^0$ | **Real** |
| $P$ | $\bar\psi\gamma^5\psi$ | $P^\dagger=P$ | **Real** |
| $A^0$ | $\bar\psi\gamma^0\gamma^5\psi$ | $A^{0\dagger}=A^0$ | **Real** |
| $\bar\psi\psi$ | $\bar\psi\cdot\mathbb{1}\cdot\psi$ | $(\bar\psi\psi)^\dagger=-\bar\psi\psi$ | **Imaginary** |

The first three follow the naive expectation that physical bilinears built
this way are real. The fourth does not. This is a genuine, checkable fact
about the $(-,+,+,+)$ Clifford algebra with this Hermiticity assignment — it
is not an error of convention choice; the same conclusion follows for either
sign choice of the compensating factor discussed below.

**Consequence for $\eta$.** The framework's w-spin magnitude
$\eta=\bar\psi\psi$ (Appendix P, Theorem 0) is, under the bare adjoint above,
purely imaginary. Since $\eta$ is asserted throughout the framework to be a
real physical quantity (Theorem 0's entire content depends on it), the
correct definition compatible with both the Clifford algebra and the
intended physics is:
$$\eta \equiv -i\,\bar\psi\psi \qquad\Longleftrightarrow\qquad \bar\psi\psi \equiv i\eta \quad (\eta \text{ real})$$

**Consequence for the action.** Appendix P Section P.1.2 writes the mass and
quartic terms of $S_{\text{geo}}$ as $-m\bar\psi\psi-\frac{\lambda}{4}(\bar\psi\psi)^2$.
Substituting $\bar\psi\psi=i\eta$: $-m\bar\psi\psi=-im\eta$ (imaginary — the
term as literally written is not part of a real Lagrangian), while
$-\frac{\lambda}{4}(\bar\psi\psi)^2=-\frac{\lambda}{4}(i\eta)^2=+\frac{\lambda}{4}\eta^2$
(real, but with the *opposite* sign to what Theorem 0/6 intend). The
corrected, manifestly-real action terms that reproduce the intended physics
($\mathcal L\supset -m\eta-\frac{\lambda}{4}\eta^2$, i.e. mass costs energy,
quartic term has the sign needed for spontaneous condensation) are:
$$\mathcal{L}_{\text{geo}} \supset +im\,\bar\psi\psi \;+\; \frac{\lambda}{4}(\bar\psi\psi)^2$$
Check: $im\bar\psi\psi=im(i\eta)=-m\eta$ ✓. $\frac{\lambda}{4}(\bar\psi\psi)^2=\frac{\lambda}{4}(i\eta)^2=-\frac{\lambda}{4}\eta^2$ ✓.

The kinetic term $\frac{i}{2}(\bar\psi\gamma^aD_a\psi-\text{h.c.})$ requires no
correction — for any operator $X$, $\frac{i}{2}(X-X^\dagger)$ is automatically
real by construction, independent of signature. This is confirmed
explicitly below (Step 1) via the equation of motion it produces.

**Scope note.** This audit does not extend to re-examining Theorem 0's
derivation of $\eta$ as "w-spin magnitude" in light of the sign/definition
correction, nor to Theorem 6's potential $V_{\text{eff}}$, beyond confirming
that the corrected action reproduces the *sign structure* those sections
assume. A full audit of Theorems 0, 5, and 6 against this corrected
convention is out of scope for this package and is flagged as a follow-on
item at the end.

---

## Step 1 — 4D Torsion-Free FLRW Dirac Equation for Homogeneous $\psi(t)$

**Setup.** Metric and tetrad from Appendix P Sections P.9.1–P.9.2, unchanged:
$ds^2=-dt^2+a(t)^2 d\Omega_3^2$ on $S^3$, diagonal tetrad
$e^0_t=1,\,e^1_\chi=a,\,e^2_\theta=a\sin\chi,\,e^3_\phi=a\sin\chi\sin\theta$.
Homogeneous spinor ansatz $\psi=\psi(t)$ (P.9.3). Torsion-free: spin
connection is the Levi-Civita connection $\overset{\circ}{\omega}$ only (no
contorsion — either because torsion is genuinely absent, or because
$A^0=0$, which makes the Cartan-equation-sourced contorsion vanish
identically; both readings coincide in this section).

**Reduced Lagrangian** (per unit $V_{S^3}=2\pi^2$, using the corrected
action terms from Step 0, and the P.9.4.1 kinetic-integral result taken as
given for the spatial gamma-matrix bookkeeping, which does not involve
$\bar\psi\psi$ and is therefore unaffected by the Step 0 audit):

$$L = a^3\left[\frac{i}{2}\Big(\bar\psi\gamma^0\dot\psi - \dot{\bar\psi}\gamma^0\psi\Big) + im\,\bar\psi\psi + \frac{\lambda}{4}(\bar\psi\psi)^2\right]$$

**Note on the $P.9.4.2$ double-count.** The P.9.4.1 boxed kinetic integral is
$2\pi^2a^3\big(\bar\psi\gamma^0\dot\psi - \tfrac{3H}{2}\bar\psi\gamma^0\psi\big)$.
Substituting into $\frac{i}{2}(X-X^\dagger)$ with $X=\bar\psi\gamma^0\dot\psi-\tfrac{3H}2\bar\psi\gamma^0\psi$:
since $\bar\psi\gamma^0\psi=J^0$ is real (Step 0 table), the $-\tfrac{3H}2J^0$
piece is Hermitian and cancels against its own h.c. counterpart inside the
antisymmetrized bracket, leaving only
$\frac{i}{2}(\bar\psi\gamma^0\dot\psi-\dot{\bar\psi}\gamma^0\psi)$ — exactly
the kinetic term used above. P.9.4.2 instead retained the $-\tfrac{3H}2J^0$
piece as an *additional*, separate term in the assembled Lagrangian. That
is a double-count: the term is present once (and cancels) inside the
Hermitian kinetic construction, and was then written down a second time.
This is confirmed, not merely suspected — the cancellation follows directly
from $J^0$'s reality, established in Step 0.

**Euler-Lagrange variation**, treating $\psi,\bar\psi$ as independent fields
(standard for Dirac field theory), varying with respect to $\bar\psi$:

$$\frac{\partial L}{\partial\bar\psi} = a^3\left[\frac i2\gamma^0\dot\psi + im\psi + \frac\lambda2(\bar\psi\psi)\psi\right], \qquad \frac{\partial L}{\partial\dot{\bar\psi}} = -\frac i2 a^3\gamma^0\psi$$

$$\frac{d}{dt}\frac{\partial L}{\partial\dot{\bar\psi}} = -\frac i2 a^3\Big(3H\gamma^0\psi+\gamma^0\dot\psi\Big)$$

The Euler-Lagrange equation $\frac{\partial L}{\partial\bar\psi}-\frac{d}{dt}\frac{\partial L}{\partial\dot{\bar\psi}}=0$ gives, after dividing by $a^3$:

$$i\gamma^0\dot\psi + \frac{3iH}{2}\gamma^0\psi + im\psi + \frac{\lambda}{2}(\bar\psi\psi)\psi = 0$$

Left-multiplying by $\gamma^0$ (using $(\gamma^0)^2=-\mathbb 1$) and dividing
through by $-i$, using $\bar\psi\psi=i\eta$:

$$\boxed{\dot\psi = -\frac{3H}{2}\psi + \left(m+\frac{\lambda}{2}\eta\right)\gamma^0\psi} \tag{D1-clean}$$

**Verification.** Computing $\dot\eta=-i(\dot\psi^\dagger\gamma^0\psi+\psi^\dagger\gamma^0\dot\psi)$
directly from (D1-clean): the $\big(m+\tfrac\lambda2\eta\big)\gamma^0\psi$
terms contribute $\mp(m+\tfrac\lambda2\eta)|\psi|^2$ to the two halves of the
sum respectively and cancel exactly (phase-rotation terms never change a
$\gamma^0$-norm — see the general lemma in Step 3). Only the friction term
survives:

$$\dot\eta = -3H\eta$$

This is the required Branch 1 dilution law, recovered exactly, with no
residual of any kind. (D1-clean) is confirmed self-consistent.

---

## Step 2 — 4D Torsion-Active FLRW Dirac Equation with $A^0 \neq 0$

**The contorsion coupling.** Per Appendix P Section P.9.3, a nonzero
axial current sources contorsion via the Cartan equation,
$T_{\lambda\mu\nu}=\tfrac{\kappa\alpha}2\varepsilon_{\lambda\mu\nu\rho}A^\rho$,
modifying the spin connection $\omega=\overset\circ\omega+K$. The full
derivation of the resulting gamma-matrix structure in the covariant
derivative — repeating the P.9.4.1-style spatial integration on $S^3$ but
with $K$ included — is a comparable undertaking to P.9.4.1 itself and is
**not** re-derived from raw indices in this package (flagged explicitly as a
scope limit, not silently assumed). What *is* established here, and is
sufficient for Steps 3–4, is the reality character of the resulting term.

Since the contorsion enters through the covariant derivative $D_\mu\psi$
inside the kinetic sector $\frac i2(\bar\psi\gamma^aD_a\psi-\text{h.c.})$ —
the same manifestly-real construction responsible for the friction term in
Step 1 — any well-formed axial contribution it produces must, by the same
general argument, appear in the equation of motion with a **real**
coefficient (no compensating $i$ needed), exactly as the friction term
$-\tfrac{3H}2\psi$ did. Adopting the coefficient magnitude already fixed by
the Cartan-equation normalization (matching P.1.3 and the pre-existing
$\tfrac{\kappa\alpha}2$ appearing throughout P.9.5.3 and P.7.7.3), the
torsion-active equation of motion is:

$$\boxed{\dot\psi = -\frac{3H}{2}\psi + \left(m+\frac{\lambda}{2}\eta\right)\gamma^0\psi + \frac{\kappa\alpha}{2}A^0\,\gamma^0\gamma^5\psi} \tag{D2-clean}$$

**Explicit scope flag.** The *coefficient magnitude and operator structure*
$\tfrac{\kappa\alpha}2A^0\gamma^0\gamma^5$ is imported from the established
Cartan-equation normalization on the grounds of consistency and dimensional
analysis, not independently re-derived here from the full contorsion
tensor contraction. This is a distinct, narrower open item from IVN-I-3 and
should be logged separately (see Verification Status). What *is* fully
established in this package is that whatever the precise coefficient turns
out to be, it must be real — which is the property Steps 3–4 depend on.

**General structural form.** Write $\dot\psi=-\tfrac{3H}2\psi+X\psi$ with
$$X \equiv M\gamma^0+N\gamma^0\gamma^5, \qquad M\equiv m+\frac\lambda2\eta \ (\text{real}), \qquad N\equiv\frac{\kappa\alpha}2A^0\ (\text{real})$$
Note $X=\gamma^0(M+N\gamma^5)=\gamma^0W$ with $W\equiv M+N\gamma^5$
manifestly **Hermitian** ($M,N$ real, $\gamma^5$ Hermitian). This structural
fact — $X$ is $\gamma^0$ times a Hermitian operator — is the single
property Step 3 needs and is what any correctly-derived, real-Lagrangian
Dirac equation of this type will always produce.

---

## Step 3 — The Closed Bilinear ODE System $(\eta, J^0, P, A^0)$

**General lemma.** For any bilinear $B_\Gamma=\bar\psi\Gamma\psi$ and any
$X=\gamma^0W$ with $W$ Hermitian,
$$\dot B_\Gamma = -3HB_\Gamma + \psi^\dagger\big[\gamma^0\Gamma X + X^\dagger\gamma^0\Gamma\big]\psi, \qquad X^\dagger = -W\gamma^0 \text{ (since } X^\dagger=W^\dagger\gamma^{0\dagger}=-W\gamma^0\text{)}$$

**Protection of $\eta$ (the central result).** For $\Gamma=\mathbb 1$:
$$\gamma^0 X = \gamma^0(\gamma^0 W) = -W, \qquad X^\dagger\gamma^0 = (-W\gamma^0)\gamma^0 = -W(\gamma^0)^2 = +W$$
$$\Rightarrow\ \gamma^0X+X^\dagger\gamma^0 = -W+W = 0 \quad\text{identically, for any Hermitian } W$$

Therefore $\dot{(\bar\psi\psi)}=-3H(\bar\psi\psi)$ exactly, with **no source
term of any kind**, for *any* real mass, quartic, or axial coupling — this
is a structural consequence of $X$ having the form $\gamma^0\times\text{Hermitian}$,
which is guaranteed for any Dirac equation derived from a real Lagrangian of
this general type. In terms of the real $\eta=-i\bar\psi\psi$:

$$\boxed{\dot\eta = -3H\eta} \qquad (\text{exact, both branches, no } \kappa\alpha A^0P \text{ source term})$$

**The remaining three bilinears (full contraction, shown for completeness).**
Carrying out the same contraction for $\Gamma=\gamma^0$ (giving $J^0$),
$\Gamma=\gamma^5$ (giving $P$), and $\Gamma=\gamma^0\gamma^5$ (giving $A^0$),
using $\gamma^5\gamma^0=-\gamma^0\gamma^5$ and $(\gamma^5)^2=\mathbb 1$
throughout:

$$\dot J^0 = -3HJ^0 - \kappa\alpha\,A^0 P$$
$$\dot P = -3HP - (2m+\lambda\eta)\,A^0 - \kappa\alpha\, A^0 J^0$$
$$\dot A^0 = -3HA^0 + (2m+\lambda\eta)\,P$$

All four equations are manifestly real (every term is a product of real
quantities) with no residual imaginary pieces at any stage — a clean,
closed, self-consistent system. $J^0$, $P$, and $A^0$ are genuinely
sourced/coupled to one another; $\eta$ is not coupled to any of them.

**Consistency checks.**
(i) *Trivial limit:* setting $M=N=0$ (no mass, no axial coupling) reduces
every equation to pure dilution $\dot B=-3HB$, as required for a
free-streaming bilinear with $\psi\propto a^{-3/2}$.
(ii) *Oscillation frequency:* dropping Hubble friction and the
$\lambda\eta$, $\kappa\alpha A^0J^0$ corrections for a leading-order check,
$\dot A^0\approx 2mP$, $\dot P\approx -2mA^0$ gives
$\ddot A^0\approx -4m^2A^0$ — oscillation at frequency $2m$, matching the
physically expected chirality-oscillation scale used throughout Appendix P
Section P.7.7.5 and the CT-ix document's late-time analysis. This is a
reassuring cross-check against previously-established (and unaffected)
physical expectations.

---

## Step 4 — Comparison Against P.9.4.1, P.9.5.3, and P.7.7.3a

| Source | Claim | Comparison with clean-room result |
|---|---|---|
| **P.9.4.1** | Boxed kinetic integral $2\pi^2a^3(\bar\psi\gamma^0\dot\psi-\tfrac{3H}2\bar\psi\gamma^0\psi)$ | The integral itself is not disputed (it concerns only gamma-matrix/spatial bookkeeping, untouched by the Step 0 audit). **P.9.4.2's use of it is a double-count** (Step 1, "Note"): the $-\tfrac{3H}2J^0$ piece cancels inside the Hermitian kinetic construction and should not also appear as a standalone term. |
| **P.9.5.3** | $i\gamma^0\dot\psi=\tfrac{3H}2\gamma^0\psi+m\psi+\tfrac\lambda2\eta\psi+\tfrac{\kappa\alpha}2A^0\gamma^0\gamma^5\psi$ | **Does not match (D2-clean)**, even after algebraic rearrangement. The stated equation has the wrong sign on the Hubble term (solving it gives $\psi$ *growing* with $a$, not diluting) and implicitly assumes a reality structure for the mass term that Step 0 shows is not valid without a compensating $i$. (D2-clean) should replace it. |
| **P.7.7.3a (IVN-I)** | $\dot\eta+3H\eta=\kappa\alpha A^0P$ | **Contradicted.** The clean-room derivation finds $\dot\eta=-3H\eta$ exactly, with no source term, for the structural reason given in Step 3. This is the headline finding of this package: IVN-I's own corrected system does not survive re-derivation under a fully audited convention. |
| **P.7.7.3a (IVN-I)** | $\dot A^0=-(2m+\lambda\eta)P$, $\dot P=(2m+(\lambda-\kappa\alpha)\eta)A^0$, no Hubble friction in the $(A^0,P)$ sector | **Also does not match.** Clean-room result has the *opposite sign convention* on $\dot A^0$ relative to $P$ (compare $\dot A^0=+(2m+\lambda\eta)P$ here), an additional $\kappa\alpha A^0J^0$ term in $\dot P$ that IVN-I's system lacks (because IVN-I did not carry $J^0$ as part of the closed system), and **does** retain Hubble friction $-3H$ on both $A^0$ and $P$, contrary to IVN-I's claim that the corrected system has none. |

**Net assessment.** Every prior version of this calculation — the original
v5–v11 text, the v12 PT-1 calculation, and IVN-I's own correction of it —
shares the same unaudited assumption: that $\bar\psi\psi$ is real under the
adjoint convention in use. It is not, in the $(-,+,+,+)$ signature with the
Hermiticity assignment this framework has used throughout (P.9.2's tetrad
and Cartan-equation conventions). Once that is corrected, the entire
downstream calculation changes, and in this specific instance, changes in
the direction of *simplifying* the physics: $\eta$'s dilution law turns out
to be exact and unconditional, protected by a clean symmetry-type argument,
rather than being an approximation that breaks down in Branch 2.

---

## What This Package Does Not Do

Per the requested ordering, **Step 5 — updating CT-viii (Appendix P Section
P.9) and CT-ix (the companion working document) — is not performed here.**
Doing so is a substantial follow-on task: P.9.5.3 needs to be replaced with
(D2-clean), and every downstream consequence traced through — P.7.7
(monodromy/chirality), P.10.5 (CT-ix Branch 2, already flagged provisional
pending exactly this kind of result), and the numerical phase estimate in
P.7.7.5. The dilution-law simplification found here likely *simplifies*
that follow-on work relative to what P.7.7.3/P.7.7.3a anticipated (since
$\eta$ decouples from the chirality sector entirely, rather than requiring
a coupled three-variable treatment), but the $(A^0,P)$ oscillator itself
still needs the corrected sign/coupling structure carried through the
monodromy calculation from scratch.

---

## Verification Status

This package should be treated with exactly the same "provisional pending
independent check" status this project has applied to every prior version
of this calculation — the fact that this version resolves several previous
inconsistencies cleanly is encouraging but is not, by itself, proof of
correctness. Specific items for independent verification:

1. **(CR-1)** Confirm the Hermiticity assignment $\gamma^{0\dagger}=-\gamma^0$,
   $\gamma^{i\dagger}=+\gamma^i$ is the correct/unique one for a unitary
   representation in $(-,+,+,+)$, and that no alternative assignment
   restores $\bar\psi\psi$ to reality without breaking $J^\mu$'s reality
   instead (Step 0 found these two requirements to be in tension; confirm
   this tension is unavoidable rather than an artifact of a specific
   representation choice).
2. **(CR-2)** Independently verify the Step 1 Euler-Lagrange variation,
   particularly the treatment of $\psi,\bar\psi$ as independent fields and
   the product-rule differentiation of $a^3(t)$.
3. **(CR-3)** Independently re-derive the Step 2 contorsion-sourced term
   from the raw $K^{ab}_c$ contraction (the P.9.4.1-style spatial
   integration this package explicitly did not repeat), to confirm both the
   $\tfrac{\kappa\alpha}2$ coefficient and the $\gamma^0\gamma^5$ operator
   structure survive independently of the reality argument used to fix its
   sign here.
4. **(CR-4)** Independently verify the Step 3 bilinear contractions for
   $J^0$, $P$, $A^0$ (the $\eta$ contraction is simple enough to be
   low-risk; the other three involve more gamma-algebra and are more
   error-prone).
5. **(CR-5)** Reconcile this package's finding with Theorem 0's identification
   of $\eta=\bar\psi\psi$ as the physical w-spin magnitude, given that Step 0
   shows this identification requires an explicit sign/factor convention
   ($\eta\equiv-i\bar\psi\psi$) not stated in the original Theorem 0 text.
   Confirm this is a labeling clarification rather than a substantive change
   to Theorem 0's content.

Until CR-1 through CR-5 are addressed, this package's results should be
treated as the current best derivation, superseding P.9.5.3 and P.7.7.3a in
status, but not yet promoted to "established" — consistent with how this
project has handled every prior derivation in this sector.

---

*SCH Clean-Room Re-Derivation Package — v1 | June 2026*
*Steps 1–4 of the requested 5-step package. Step 5 deliberately deferred.*
*Not for citation without author approval. Requires independent verification at all CR-marked items.*
