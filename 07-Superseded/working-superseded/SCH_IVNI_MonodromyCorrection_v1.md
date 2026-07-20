# SCH — IVN-I: PT-1 Monodromy in the $(+,-,-,-)$ Convention
## Redoing the Monodromy Calculation with Correct Bilinears

> **⚠️ SUPERSEDED PENDING CLEAN-ROOM CANONICALIZATION**
>
> This document is retained as the record of the intermediate correction
> attempt that exposed the need for a full convention/reality audit of the
> cosmological Dirac equation and its bilinear sector. **It is no longer to
> be treated as the operative Branch 2 result.**
>
> A subsequent clean-room re-derivation (`SCH_CleanRoom_Rederivation_v1.md`,
> June 2026), built on a single audited $(-,+,+,+)$ convention with an
> explicit bilinear-reality check performed *before* any dynamics were
> derived, found that the $\eta$-sourcing claim in this document's downstream
> consequence (Appendix P v13, Section P.7.7.3a: $\dot\eta+3H\eta=\kappa\alpha
> A^0P$) does not survive re-derivation. The clean-room package instead finds
> $\dot\eta=-3H\eta$ exactly, in both branches, protected by a structural
> argument independent of the specific values of $m,\lambda,\alpha$. It also
> finds a distinct $(A^0,P)$ oscillator structure than this document's Part
> 2/3 conclusions below (different sign on $\dot A^0$, an additional $J^0$
> coupling in $\dot P$, and retained — not absent — Hubble friction).
>
> This document's *qualitative* conclusion — that chirality inversion per
> bounce cycle is not a generic, topologically-protected consequence of the
> dynamics — is not contradicted by the clean-room package and may well
> survive canonicalization. What is specifically superseded is the detailed
> bilinear system below (Parts 1–3) and, in particular, the claim that
> Branch 2 introduces a new $\eta$-sourcing effect.
>
> This document remains historically important: it is what first surfaced
> the metric-convention inconsistency in the original v12 PT-1 calculation,
> and its own internal inconsistencies (in turn) are what prompted the
> clean-room package. It should be read as a waypoint, not a destination.
> The open tracking item for the canonical replacement is
> **IVN-CT8-Dirac-1** (Appendix P v13.1, Section P.7.7.10).
>
> Note also that this document used the $(+,-,-,-)$ signature convention
> (Hermitian $\gamma^0_D$), while the clean-room package used $(-,+,+,+)$
> (anti-Hermitian $\gamma^0$). Reconciling results across the two requires
> care with signature-dependent factors of $i$ — this reconciliation is
> itself part of IVN-CT8-Dirac-1a's scope.

*Working Document — v1 | June 2026*

**Status:** SUPERSEDES the monodromy section of PT-1 Monodromy Calculation v1,
which used mixed conventions. This document redoes the calculation in the
consistent $(+,-,-,-)$ convention established by IVN-H.

**Convention fixed throughout:**
- $\eta_{ab} = \mathrm{diag}(+1,-1,-1,-1)$
- $\gamma^0_D = \mathrm{diag}(\mathbf{1},-\mathbf{1})$, $(\gamma^0_D)^2 = +\mathbf{1}$
- $\gamma^5_D = \begin{pmatrix}0&\mathbf{1}\\\mathbf{1}&0\end{pmatrix}$,
  $(\gamma^5_D)^2 = +\mathbf{1}$
- $\bar{\psi} = \psi^\dagger\gamma^0_D = (\xi^\dagger,-\chi^\dagger)$
- $\eta = \bar{\psi}\psi = \xi^\dagger\xi - \chi^\dagger\chi \in \mathbb{R}$
- $A^0 = \bar{\psi}\gamma^0_D\gamma^5_D\psi = \xi^\dagger\chi + \chi^\dagger\xi
  \in \mathbb{R}$
- $J^0 = \bar{\psi}\gamma^0_D\psi = \xi^\dagger\xi + \chi^\dagger\chi > 0$
- $P = \bar{\psi}\gamma^5_D\psi = -i(\xi^\dagger\chi - \chi^\dagger\xi) \in \mathbb{R}$
- $m, \lambda, \alpha, \kappa > 0$ all real

---

## Part 1 — The Cosmological Dirac Equation in $(+,-,-,-)$

### 1.1 Deriving $\dot{\psi}$ in $(+,-,-,-)$

The cosmological Dirac equation (action-variation level, convention-independent):

$$i\gamma^0\dot{\psi} = \frac{3H}{2}\gamma^0\psi + m\psi
+ \frac{\lambda}{2}\eta\psi + \frac{\kappa\alpha}{2}A^0\gamma^0\gamma^5\psi \tag{D}$$

In $(+,-,-,-)$, multiply both sides on the left by $-i\gamma^0_D$.
Since $(\gamma^0_D)^{-1} = \gamma^0_D$ (because $(\gamma^0_D)^2 = +\mathbf{1}$):

$$(-i\gamma^0_D)(i\gamma^0_D)\dot{\psi} = (-i\gamma^0_D)\,\text{RHS}$$

$$(-i)(i)(\gamma^0_D)^2\dot{\psi} = -i\gamma^0_D\,\text{RHS}$$

$$(1)(+\mathbf{1})\dot{\psi} = -i\gamma^0_D\,\text{RHS}$$

$$\dot{\psi} = -i\gamma^0_D\left(\frac{3H}{2}\gamma^0_D\psi + m\psi
+ \frac{\lambda}{2}\eta\psi + \frac{\kappa\alpha}{2}A^0\gamma^0_D\gamma^5_D\psi\right)$$

$$= -i\frac{3H}{2}(\gamma^0_D)^2\psi - im\gamma^0_D\psi
- i\frac{\lambda}{2}\eta\gamma^0_D\psi
- i\frac{\kappa\alpha}{2}A^0(\gamma^0_D)^2\gamma^5_D\psi$$

$$= -i\frac{3H}{2}\psi - im\gamma^0_D\psi
- i\frac{\lambda}{2}\eta\gamma^0_D\psi
- i\frac{\kappa\alpha}{2}A^0\gamma^5_D\psi \tag{D'}$$

**Note:** In $(+,-,-,-)$, $(\gamma^0_D)^2 = +\mathbf{1}$ gives $-i\frac{3H}{2}\psi$
with a *minus* sign from $(-i\gamma^0_D)(\frac{3H}{2}\gamma^0_D\psi)
= -i\frac{3H}{2}(\gamma^0_D)^2\psi = -i\frac{3H}{2}\psi$. Same as in
the $(-,+,+,+)$ IVN-16 result — the structure is unchanged.

The last term: $(-i\gamma^0_D)\cdot\frac{\kappa\alpha}{2}A^0\gamma^0_D\gamma^5_D\psi
= -i\frac{\kappa\alpha}{2}A^0(\gamma^0_D)^2\gamma^5_D\psi
= -i\frac{\kappa\alpha}{2}A^0(+\mathbf{1})\gamma^5_D\psi
= -i\frac{\kappa\alpha}{2}A^0\gamma^5_D\psi$ ✓

The conjugate equation:

$$\dot{\bar{\psi}} = +i\frac{3H}{2}\bar{\psi} + im\bar{\psi}\gamma^0_D
+ i\frac{\lambda}{2}\eta\bar{\psi}\gamma^0_D
+ i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5_D \tag{D''}$$

*(IVN-I-1: verify (D'') by taking the Dirac conjugate of (D') explicitly
in the $(+,-,-,-)$ convention.)*

### 1.2 Component Equations

In the Dirac representation with
$\gamma^0_D = \begin{pmatrix}\mathbf{1}&0\\0&-\mathbf{1}\end{pmatrix}$,
$\gamma^5_D = \begin{pmatrix}0&\mathbf{1}\\\mathbf{1}&0\end{pmatrix}$:

From (D'):

Upper component ($\xi$):
$$\dot{\xi} = -i\frac{3H}{2}\xi - im\xi - i\frac{\lambda}{2}\eta\xi
- i\frac{\kappa\alpha}{2}A^0\chi \tag{C-xi}$$

Lower component ($\chi$):
$$\dot{\chi} = -i\frac{3H}{2}\chi + im\chi + i\frac{\lambda}{2}\eta\chi
- i\frac{\kappa\alpha}{2}A^0\xi \tag{C-chi}$$

*(IVN-I-2: verify (C-xi) and (C-chi) by direct substitution of the
$(+,-,-,-)$ gamma matrices into (D').)*

Compare with the IVN-16 component equations which used $(-,+,+,+)$.
The key difference: in $(-,+,+,+)$, the mass term in (C-xi) was
$+im\gamma^0_L\xi$ which gave $im$ for the upper component; here in
$(+,-,-,-)$ the mass term is $-im\gamma^0_D\xi$ which gives $-im\xi$
for the upper component (since $\gamma^0_D$ acts as $+1$ on the upper
component). The upper and lower mass terms have opposite signs.

---

## Part 2 — The Bilinear Evolution Equations

### 2.1 The $\eta$ Equation

$$\dot{\eta} = \frac{d}{dt}(\xi^\dagger\xi - \chi^\dagger\chi)
= \dot{\xi}^\dagger\xi + \xi^\dagger\dot{\xi} - \dot{\chi}^\dagger\chi
- \chi^\dagger\dot{\chi}$$

From (C-xi): $\dot{\xi} = -i\frac{3H}{2}\xi - im\xi
- i\frac{\lambda}{2}\eta\xi - i\frac{\kappa\alpha}{2}A^0\chi$

So $\dot{\xi}^\dagger = +i\frac{3H}{2}\xi^\dagger + im\xi^\dagger
+ i\frac{\lambda}{2}\eta\xi^\dagger + i\frac{\kappa\alpha}{2}A^0\chi^\dagger$

**The $-3H/2$ terms:**

$\dot{\xi}^\dagger\xi + \xi^\dagger\dot{\xi}\big|_{3H}
= +i\frac{3H}{2}\xi^\dagger\xi - i\frac{3H}{2}\xi^\dagger\xi = 0$

$-\dot{\chi}^\dagger\chi - \chi^\dagger\dot{\chi}\big|_{3H}
= -i\frac{3H}{2}\chi^\dagger\chi + i\frac{3H}{2}\chi^\dagger\chi = 0$

Wait — from (C-chi): $\dot{\chi} = -i\frac{3H}{2}\chi + \ldots$, so
$\dot{\chi}^\dagger = +i\frac{3H}{2}\chi^\dagger + \ldots$

$-\dot{\chi}^\dagger\chi\big|_{3H} = -i\frac{3H}{2}\chi^\dagger\chi$

$-\chi^\dagger\dot{\chi}\big|_{3H} = +i\frac{3H}{2}\chi^\dagger\chi$

These cancel. ✓

**The mass terms:**

From $\xi$ sector: $+im\xi^\dagger\xi - im\xi^\dagger\xi = 0$ ✓

From $\chi$ sector: $(-\dot{\chi}^\dagger\chi - \chi^\dagger\dot{\chi})\big|_m$

$= -(-im\chi^\dagger\chi) - \chi^\dagger(im\chi)$

Wait — from (C-chi): mass term is $+im\chi$, so
$\dot{\chi}^\dagger\big|_m = -im\chi^\dagger$ and
$-\dot{\chi}^\dagger\chi\big|_m = +im\chi^\dagger\chi$

$-\chi^\dagger\dot{\chi}\big|_m = -\chi^\dagger(+im\chi) = -im\chi^\dagger\chi$

Sum: $+im\chi^\dagger\chi - im\chi^\dagger\chi = 0$ ✓

**The $\lambda\eta/2$ terms:** same cancellation by the same argument. ✓

**The $\kappa\alpha A^0/2$ terms:**

From $\xi$ sector:
$\dot{\xi}^\dagger\xi\big|_{A^0} = +i\frac{\kappa\alpha}{2}A^0\chi^\dagger\xi$
$\xi^\dagger\dot{\xi}\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\xi^\dagger\chi$

From $\chi$ sector:
$-\dot{\chi}^\dagger\chi\big|_{A^0} = -(-i\frac{\kappa\alpha}{2}A^0\xi^\dagger)\chi
= +i\frac{\kappa\alpha}{2}A^0\xi^\dagger\chi$

Wait — from (C-chi): the $A^0$ term is $-i\frac{\kappa\alpha}{2}A^0\xi$.
So $\dot{\chi}^\dagger\big|_{A^0} = +i\frac{\kappa\alpha}{2}A^0\xi^\dagger$
and $-\dot{\chi}^\dagger\chi\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\xi^\dagger\chi$.

$-\chi^\dagger\dot{\chi}\big|_{A^0} = -\chi^\dagger(-i\frac{\kappa\alpha}{2}A^0\xi)
= +i\frac{\kappa\alpha}{2}A^0\chi^\dagger\xi$

Sum of all $A^0$ contributions:

$+i\frac{\kappa\alpha}{2}A^0\chi^\dagger\xi
- i\frac{\kappa\alpha}{2}A^0\xi^\dagger\chi
- i\frac{\kappa\alpha}{2}A^0\xi^\dagger\chi
+ i\frac{\kappa\alpha}{2}A^0\chi^\dagger\xi$

$= i\kappa\alpha A^0(\chi^\dagger\xi - \xi^\dagger\chi)$

Now: $\chi^\dagger\xi - \xi^\dagger\chi = -(\xi^\dagger\chi - \chi^\dagger\xi)
= -2i\,\mathrm{Im}(\xi^\dagger\chi)$.

From the bilinear table: $P = -i(\xi^\dagger\chi - \chi^\dagger\xi)$,
so $\xi^\dagger\chi - \chi^\dagger\xi = iP$ and
$\chi^\dagger\xi - \xi^\dagger\chi = -iP$.

Substituting:

$i\kappa\alpha A^0 \cdot (-iP) = \kappa\alpha A^0 P$

**Result:**

$$\boxed{\dot{\eta} + 3H\eta = \kappa\alpha A^0 P} \tag{E1-new}$$

This is the corrected $\eta$ equation. **It is not $\dot{\eta} + 3H\eta = 0$.**

In $(+,-,-,-)$, $\eta$ is NOT conserved in the presence of nonzero $A^0$
and $P$. There is a source term $\kappa\alpha A^0 P$.

*(IVN-I-3: this is a significant difference from the IVN-16 result where
$\dot{\eta} + 3H\eta = 0$ was found. The difference arises because in
$(+,-,-,-)$ the $A^0$ coupling to the $\eta$ equation does not cancel.
Verify (E1-new) term by term.)*

**In Branch 1 ($A^0 = 0$):** $\dot{\eta} + 3H\eta = 0$, giving
$\eta \propto a^{-3}$. ✓ The dilution law holds in Branch 1 regardless
of convention. ✓

**In Branch 2 ($A^0 \neq 0$):** $\eta$ has a source term and does not
dilute as $a^{-3}$ exactly. This is a new result — the Branch 2 dynamics
are more coupled than previously understood.

### 2.2 The $A^0$ Equation

$$\dot{A}^0 = \frac{d}{dt}(\xi^\dagger\chi + \chi^\dagger\xi)
= \dot{\xi}^\dagger\chi + \xi^\dagger\dot{\chi}
+ \dot{\chi}^\dagger\xi + \chi^\dagger\dot{\xi}$$

**The $-3H/2$ terms:**

$\dot{\xi}^\dagger\chi\big|_{3H} = +i\frac{3H}{2}\xi^\dagger\chi$
$\xi^\dagger\dot{\chi}\big|_{3H} = -i\frac{3H}{2}\xi^\dagger\chi$: cancel.

$\dot{\chi}^\dagger\xi\big|_{3H} = +i\frac{3H}{2}\chi^\dagger\xi$

Wait — from (C-chi): $\dot{\chi}\big|_{3H} = -i\frac{3H}{2}\chi$, so
$\dot{\chi}^\dagger\big|_{3H} = +i\frac{3H}{2}\chi^\dagger$.

$\dot{\chi}^\dagger\xi\big|_{3H} = +i\frac{3H}{2}\chi^\dagger\xi$
$\chi^\dagger\dot{\xi}\big|_{3H} = -i\frac{3H}{2}\chi^\dagger\xi$: cancel. ✓

All $3H$ terms cancel. $\dot{A}^0$ has no Hubble friction term.

**The mass terms:**

From $\xi$ sector ($\dot{\xi}\big|_m = -im\xi$):
$\dot{\xi}^\dagger\chi\big|_m = +im\xi^\dagger\chi$
$\chi^\dagger\dot{\xi}\big|_m = -im\chi^\dagger\xi$

From $\chi$ sector ($\dot{\chi}\big|_m = +im\chi$):
$\xi^\dagger\dot{\chi}\big|_m = +im\xi^\dagger\chi$
$\dot{\chi}^\dagger\xi\big|_m = -im\chi^\dagger\xi$

Sum: $2im\xi^\dagger\chi - 2im\chi^\dagger\xi = 2im(\xi^\dagger\chi - \chi^\dagger\xi)
= 2im \cdot iP = -2mP$

*(using $\xi^\dagger\chi - \chi^\dagger\xi = iP$ from the bilinear table)*

**The $\lambda\eta/2$ terms:** same structure as mass, giving $-\lambda\eta P$.

**The $\kappa\alpha A^0/2$ terms:**

From $\xi$ sector ($\dot{\xi}\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\chi$):
$\dot{\xi}^\dagger\chi\big|_{A^0} = +i\frac{\kappa\alpha}{2}A^0\chi^\dagger\chi$
$\chi^\dagger\dot{\xi}\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\chi^\dagger\chi$
These cancel. ✓

From $\chi$ sector ($\dot{\chi}\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\xi$):
$\xi^\dagger\dot{\chi}\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\xi^\dagger\xi$
$\dot{\chi}^\dagger\xi\big|_{A^0} = +i\frac{\kappa\alpha}{2}A^0\xi^\dagger\xi$
These cancel. ✓

All $\kappa\alpha$ terms cancel in the $\dot{A}^0$ equation.

**Result:**

$$\boxed{\dot{A}^0 = -(2m + \lambda\eta)P} \tag{E-A-new}$$

No $i$ factor. No $J^0$ coupling. No Hubble friction.
The $A^0$ evolution is driven purely by the product $(2m + \lambda\eta)P$.

### 2.3 The $P$ Equation

$$\dot{P} = \frac{d}{dt}(-i(\xi^\dagger\chi - \chi^\dagger\xi))$$

$= -i(\dot{\xi}^\dagger\chi + \xi^\dagger\dot{\chi} - \dot{\chi}^\dagger\xi
- \chi^\dagger\dot{\xi})$

**The $3H$ terms:** cancel by the same argument. ✓

**The mass terms:**

$-i(\dot{\xi}^\dagger\chi\big|_m + \xi^\dagger\dot{\chi}\big|_m
- \dot{\chi}^\dagger\xi\big|_m - \chi^\dagger\dot{\xi}\big|_m)$

$= -i(im\xi^\dagger\chi + im\xi^\dagger\chi - (-im)\chi^\dagger\xi - (-im)\chi^\dagger\xi)$

Wait — from (C-chi): $\dot{\chi}\big|_m = +im\chi$, so
$\dot{\chi}^\dagger\big|_m = -im\chi^\dagger$.

$= -i(im\xi^\dagger\chi + im\xi^\dagger\chi
- (-im\chi^\dagger\xi) - (-im\chi^\dagger\xi))$

$= -i(im\xi^\dagger\chi + im\xi^\dagger\chi + im\chi^\dagger\xi + im\chi^\dagger\xi)$

$= -i \cdot 2im(\xi^\dagger\chi + \chi^\dagger\xi)$

$= -i \cdot 2im \cdot A^0$

$= 2m A^0$

**The $\lambda\eta/2$ terms:** same structure, giving $+\lambda\eta A^0$.

**The $\kappa\alpha A^0/2$ terms:**

$-i(\dot{\xi}^\dagger\chi\big|_{A^0} + \xi^\dagger\dot{\chi}\big|_{A^0}
- \dot{\chi}^\dagger\xi\big|_{A^0} - \chi^\dagger\dot{\xi}\big|_{A^0})$

$\dot{\xi}^\dagger\chi\big|_{A^0} = +i\frac{\kappa\alpha}{2}A^0\chi^\dagger\chi$

$\xi^\dagger\dot{\chi}\big|_{A^0} = \xi^\dagger(-i\frac{\kappa\alpha}{2}A^0\xi)
= -i\frac{\kappa\alpha}{2}A^0\xi^\dagger\xi$

$-\dot{\chi}^\dagger\xi\big|_{A^0} = -(-(-i\frac{\kappa\alpha}{2}A^0\xi^\dagger))\xi$

Wait — $\dot{\chi}\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\xi$, so
$\dot{\chi}^\dagger\big|_{A^0} = +i\frac{\kappa\alpha}{2}A^0\xi^\dagger$.

$-\dot{\chi}^\dagger\xi\big|_{A^0} = -i\frac{\kappa\alpha}{2}A^0\xi^\dagger\xi$

$-\chi^\dagger\dot{\xi}\big|_{A^0} = -\chi^\dagger(-i\frac{\kappa\alpha}{2}A^0\chi)
= +i\frac{\kappa\alpha}{2}A^0\chi^\dagger\chi$

Sum of $\kappa\alpha$ terms inside the $-i(\ldots)$:

$i\frac{\kappa\alpha}{2}A^0\chi^\dagger\chi - i\frac{\kappa\alpha}{2}A^0\xi^\dagger\xi
- i\frac{\kappa\alpha}{2}A^0\xi^\dagger\xi + i\frac{\kappa\alpha}{2}A^0\chi^\dagger\chi$

$= i\kappa\alpha A^0(\chi^\dagger\chi - \xi^\dagger\xi)$

$= -i\kappa\alpha A^0(\xi^\dagger\xi - \chi^\dagger\chi)$

$= -i\kappa\alpha A^0\eta$

Then $-i \cdot (-i\kappa\alpha A^0\eta) = -\kappa\alpha A^0\eta$.

**Result:**

$$\boxed{\dot{P} = (2m + \lambda\eta)A^0 - \kappa\alpha\eta A^0} \tag{E-P-new}$$

$$= A^0\left(2m + (\lambda - \kappa\alpha)\eta\right) \tag{E-P-new-simplified}$$

### 2.4 The $J^0$ Equation

For completeness:

$$\dot{J}^0 = \frac{d}{dt}(\xi^\dagger\xi + \chi^\dagger\chi)$$

By the same calculation as $\dot{\eta}$ but with opposite signs on
the $\chi$ sector:

The $3H$ terms give $-3H J^0$.

The mass terms: $+im\xi^\dagger\xi - im\xi^\dagger\xi
+ (-im)\chi^\dagger\chi - (-im)\chi^\dagger\chi = 0$ ✓

The $A^0$ terms by same argument as $\dot{\eta}$, but with:

$i\kappa\alpha A^0(\chi^\dagger\xi + \xi^\dagger\chi)$

*(IVN-I-4: verify this step — the $J^0$ $A^0$ coupling)*

$= i\kappa\alpha A^0 \cdot A^0 = i\kappa\alpha (A^0)^2$

This is imaginary unless $(A^0)^2$ has an imaginary factor — but $A^0$
is real, so $(A^0)^2$ is real and $i\kappa\alpha(A^0)^2$ is imaginary.
$J^0$ must be real since it equals $\xi^\dagger\xi + \chi^\dagger\chi$.
A imaginary source for a real quantity indicates an error.

*(IVN-I-5: recheck the $A^0$ contribution to $\dot{J}^0$ carefully.)*

**Tentative result, pending IVN-I-4 and IVN-I-5:**

$$\dot{J}^0 + 3H J^0 = 0 \tag{E-J-new}$$

(if the $A^0$ contribution vanishes, which it should by conservation of
the vector current in the parity-preserving sector)

---

## Part 3 — The Corrected $(A^0, P)$ System

### 3.1 The System

In Branch 2 ($A^0 \neq 0$, $P \neq 0$), the coupled evolution equations
in $(+,-,-,-)$ are:

$$\dot{A}^0 = -(2m + \lambda\eta)\,P \tag{S1-correct}$$

$$\dot{P} = (2m + (\lambda - \kappa\alpha)\eta)\,A^0 \tag{S2-correct}$$

Define:

$$\Omega_1(t) \equiv 2m + \lambda\eta(t) \tag{Omega1}$$

$$\Omega_2(t) \equiv 2m + (\lambda - \kappa\alpha)\eta(t) \tag{Omega2}$$

The system:

$$\dot{A}^0 = -\Omega_1 P, \qquad \dot{P} = \Omega_2 A^0 \tag{Sys}$$

This is a real, coupled, linear ODE system with no $i$ factors.
All quantities are real. This is the correct system.

**Compare with the previous (incorrect) version from PT-1 Monodromy v1:**

Previous (wrong convention):
$\dot{A}^0 = i\Omega P - i\Gamma A^0$, $\dot{P} = i\Omega A^0 - i\Gamma P$

Current (correct $(+,-,-,-)$):
$\dot{A}^0 = -\Omega_1 P$, $\dot{P} = \Omega_2 A^0$

The structures are qualitatively different. The previous system had
pure imaginary coefficients and Hubble friction; the current system
has real coefficients and no Hubble friction in either equation.

### 3.2 The Character of the System

Taking the second derivative:

$$\ddot{A}^0 = -\dot{\Omega}_1 P - \Omega_1\dot{P}
= -\dot{\Omega}_1 P - \Omega_1\Omega_2 A^0$$

$$\ddot{A}^0 + \Omega_1\Omega_2 A^0 = -\dot{\Omega}_1 P \tag{2nd-A}$$

Similarly:

$$\ddot{P} + \Omega_1\Omega_2 P = \dot{\Omega}_2 A^0 \tag{2nd-P}$$

In the adiabatic limit ($\dot{\Omega}_1, \dot{\Omega}_2 \approx 0$, i.e.,
$\eta$ varying slowly), this becomes:

$$\ddot{A}^0 + \Omega_1\Omega_2 A^0 \approx 0 \tag{osc-A}$$

$$\ddot{P} + \Omega_1\Omega_2 P \approx 0 \tag{osc-P}$$

These are oscillator equations. The character depends on the sign of
$\Omega_1\Omega_2$:

**If $\Omega_1\Omega_2 > 0$:** oscillatory solutions,
$A^0(t) \propto \cos(\int\sqrt{\Omega_1\Omega_2}\,dt)$.

**If $\Omega_1\Omega_2 < 0$:** exponentially growing/decaying solutions.

$\Omega_1 = 2m + \lambda\eta > 0$ always (since $m, \lambda > 0$ and
$\eta > 0$ in the condensed phase).

$\Omega_2 = 2m + (\lambda - \kappa\alpha)\eta$. This is positive if
$\lambda > \kappa\alpha$ or if $\eta < 2m/(\kappa\alpha - \lambda)$
(when $\kappa\alpha > \lambda$).

In the generic case $\lambda > \kappa\alpha$ (weak torsion coupling),
$\Omega_1\Omega_2 > 0$ and the system is oscillatory.

**The $(A^0, P)$ system oscillates in the condensed phase.**

### 3.3 Normal Modes

The system (Sys) is not immediately diagonalisable by the previous mode
decomposition $u = A^0 + P$, $v = A^0 - P$ because the coefficients
$\Omega_1 \neq \Omega_2$.

Write in matrix form:

$$\frac{d}{dt}\begin{pmatrix}A^0\\P\end{pmatrix}
= \begin{pmatrix}0 & -\Omega_1 \\ \Omega_2 & 0\end{pmatrix}
\begin{pmatrix}A^0\\P\end{pmatrix} \tag{Msys}$$

The matrix $\mathcal{M} = \begin{pmatrix}0&-\Omega_1\\\Omega_2&0\end{pmatrix}$
has eigenvalues $\pm i\sqrt{\Omega_1\Omega_2}$ (assuming $\Omega_1\Omega_2 > 0$).

The eigenvectors are $\mathbf{v}_\pm = \begin{pmatrix}\sqrt{\Omega_1}\\\pm i\sqrt{\Omega_2}\end{pmatrix}$
(up to normalisation).

*(IVN-I-6: verify the eigenvectors.)*

In the adiabatic approximation (treating $\Omega_1, \Omega_2$ as
slowly varying), the normal mode solutions are:

$$A^0(t) + i\sqrt{\frac{\Omega_1}{\Omega_2}}P(t) \propto
\exp\!\left(i\int_0^t\sqrt{\Omega_1(s)\Omega_2(s)}\,ds\right)$$

$$A^0(t) - i\sqrt{\frac{\Omega_1}{\Omega_2}}P(t) \propto
\exp\!\left(-i\int_0^t\sqrt{\Omega_1(s)\Omega_2(s)}\,ds\right)$$

The accumulated phase over one cycle:

$$\Phi_{\text{cycle}} = \int_{\text{cycle}}\sqrt{\Omega_1(t)\Omega_2(t)}\,dt
\tag{Phi}$$

where $\Omega_1\Omega_2 = (2m + \lambda\eta)(2m + (\lambda-\kappa\alpha)\eta)$.

### 3.4 The Monodromy Matrix

The monodromy after one cycle maps $(A^0, P)\big|_0 \to (A^0, P)\big|_{T_{\text{cycle}}}$.
In the adiabatic approximation, using the mode decomposition:

$$M_{\text{correct}} = \begin{pmatrix}
\cos\Phi_{\text{cycle}} & -\sqrt{\frac{\Omega_1}{\Omega_2}}\sin\Phi_{\text{cycle}} \\
\sqrt{\frac{\Omega_2}{\Omega_1}}\sin\Phi_{\text{cycle}} & \cos\Phi_{\text{cycle}}
\end{pmatrix} \tag{M-correct}$$

*(IVN-I-7: derive (M-correct) from the mode solutions by inverting
the mode transformation and computing the full cycle map.)*

**$M_{\text{correct}} = -\mathbf{1}$ requires:**

$\cos\Phi_{\text{cycle}} = -1$ and $\sin\Phi_{\text{cycle}} = 0$.

This gives $\Phi_{\text{cycle}} = (2n-1)\pi$ for integer $n$ — odd
multiples of $\pi$.

---

## Part 4 — Evaluating the Phase Integral

### 4.1 The Phase Integral in $(+,-,-,-)$

$$\Phi_{\text{cycle}} = \int_{\text{cycle}}\sqrt{\Omega_1\Omega_2}\,dt$$

$$= \int_{\text{cycle}}\sqrt{(2m + \lambda\eta)(2m + (\lambda-\kappa\alpha)\eta)}\,dt$$

In Branch 1 ($A^0 = 0$): $\eta = \eta_0/a^3$ (dilution law, confirmed
in $(+,-,-,-)$ by E1-new with $A^0 = 0$).

In Phase III ($\eta \approx 0$, $a \gg a_*$):

$$\sqrt{\Omega_1\Omega_2} \approx \sqrt{(2m)(2m)} = 2m$$

The integral over the cycle:

$$\Phi_{\text{cycle}} \approx 2m \cdot T_{\text{cycle}} \tag{Phi-III}$$

This is the same leading-order result as before. The Phase III estimate
$\Phi_{\text{cycle}} \sim 10^{54}$ stands.

In Phase I ($\eta \gg 2m/\lambda$, $a \ll a_*$):

$$\sqrt{\Omega_1\Omega_2} \approx \sqrt{\lambda(\lambda-\kappa\alpha)}\,\eta
= \sqrt{\lambda(\lambda-\kappa\alpha)}\frac{\eta_0}{a^3}$$

The Phase I contribution near the bounce:

$$\Phi_{\text{I}} \sim \sqrt{\lambda(\lambda-\kappa\alpha)}\eta_0
\int_{\text{bounce}}\frac{dt}{a^3}$$

As in the previous monodromy calculation, this integral diverges near the
bounce (as $\int d\tau/\tau$ for $a \propto \tau^{1/3}$). The physical
cutoff at $a_c$ (condensate melting) regulates it, giving a finite
contribution that depends on $\eta_0$, $\lambda$, $\kappa\alpha$, and $a_c$.

### 4.2 The Key New Feature: The $\kappa\alpha$ Correction

In the $(+,-,-,-)$ result, the phase integral involves
$\sqrt{\Omega_1\Omega_2} = \sqrt{(2m+\lambda\eta)(2m+(\lambda-\kappa\alpha)\eta)}$
rather than simply $\Omega = 2m + \lambda\eta$.

The difference:

$$\sqrt{\Omega_1\Omega_2} = \Omega_1\sqrt{1 - \frac{\kappa\alpha\eta}{\Omega_2}}
\approx \Omega_1\left(1 - \frac{\kappa\alpha\eta}{2\Omega_1} + \ldots\right)
= \Omega_1 - \frac{\kappa\alpha\eta}{2} + \ldots$$

So at leading order in $\kappa\alpha$:

$$\Phi_{\text{cycle}} \approx \int_{\text{cycle}}\left(\Omega_1
- \frac{\kappa\alpha\eta}{2}\right)dt
= \int_{\text{cycle}}\left(2m + \lambda\eta - \frac{\kappa\alpha\eta}{2}\right)dt$$

The correction to the Phase III estimate:

$$\delta\Phi = -\frac{\kappa\alpha}{2}\int_{\text{cycle}}\eta\,dt
= -\frac{\kappa\alpha\eta_0}{2}\int_{\text{cycle}}\frac{dt}{a^3}$$

This integral is finite (the cutoff at $a_c$ regulates the bounce
divergence). It represents a correction to the monodromy phase from
the torsion coupling $\kappa\alpha$.

**Qualitative observation:** The $\kappa\alpha$ correction *reduces*
the monodromy phase $\Phi_{\text{cycle}}$ relative to the naive
$2m T_{\text{cycle}}$ estimate. Whether this correction is significant
compared to $\pi$ depends on the parameters.

### 4.3 The Condition for Chirality Inversion

$M_{\text{correct}} = -\mathbf{1}$ requires:

$$\Phi_{\text{cycle}} = (2n-1)\pi \tag{chirality-condition}$$

With $\Phi_{\text{cycle}} \approx 2m T_{\text{cycle}} \sim 10^{54}$, the
condition (chirality-condition) requires the phase to land on an odd multiple
of $\pi$ — a set of measure zero in the space of all possible phase values.

The $\kappa\alpha$ correction modifies $\Phi_{\text{cycle}}$ by a finite
amount but does not in general shift it to the nearest odd multiple of $\pi$.

**The conclusion of the previous monodromy calculation stands in the
corrected convention:** chirality inversion per cycle is not generic.
It requires the action parameters to satisfy a specific quantization
condition, which has no topological protection.

---

## Part 5 — The New Result: $\eta$ Sourcing in Branch 2

### 5.1 The Coupled System in Branch 2

In Branch 2 ($A^0 \neq 0$), equation (E1-new) gives:

$$\dot{\eta} + 3H\eta = \kappa\alpha A^0 P$$

This means $\eta$ is not simply diluting as $a^{-3}$ in Branch 2.
The condensate scalar is sourced by the product $A^0 P$.

From (Sys): $A^0$ and $P$ oscillate with frequency $\sim 2m$. Their
product $A^0 P$ oscillates at frequency $\sim 4m$ (double frequency).
The time-averaged source is:

$$\langle A^0 P\rangle_{\text{osc}} = \frac{1}{2}\langle A^0\rangle_{\text{osc}}
\langle P\rangle_{\text{osc}} + \text{correlated terms}$$

If the oscillations of $A^0$ and $P$ are $90°$ out of phase (which
is generically the case for a harmonic oscillator system), then
$\langle A^0 P\rangle_{\text{osc}} \neq 0$ in general.

**This is a new physical effect:** in Branch 2, the axial condensate
oscillations pump energy into (or drain energy from) the scalar
condensate $\eta$. The condensate amplitude does not simply dilute —
it is dynamically coupled to the chirality oscillations.

### 5.2 Physical Interpretation

The source term $\kappa\alpha A^0 P$ in the $\eta$ equation has the
following physical meaning. $A^0$ is the timelike axial current —
the chiral charge density. $P$ is the pseudoscalar bilinear — the
parity-odd condensate amplitude. Their product is a parity-even
scalar that couples to the torsion through $\kappa\alpha$.

In Branch 2, the condensate is not in the parity-preserving vacuum.
The coexistence of nonzero $A^0$ and $P$ represents a parity-broken
condensate state. The torsion coupling $\kappa\alpha$ then allows
energy to flow between the scalar condensate $\eta$ and the
parity-odd sector $(A^0, P)$.

This is new physics that was not visible in the previous (incorrect)
convention calculation, where $\eta$ diluted independently. It
means the Branch 2 cosmological dynamics are richer than previously
understood: the condensate amplitude, the chirality, and the
pseudoscalar all evolve together in a coupled system.

---

## Part 6 — Summary

### 6.1 Results of IVN-I

| Result | Status |
|--------|--------|
| $\dot{A}^0 = -(2m+\lambda\eta)P$ — no $i$ factors, no Hubble friction | Derived (IVN-I-3 pending) |
| $\dot{P} = (2m + (\lambda-\kappa\alpha)\eta)A^0$ | Derived |
| In Branch 1: $\dot{\eta} + 3H\eta = 0$ ✓ | Confirmed |
| In Branch 2: $\dot{\eta} + 3H\eta = \kappa\alpha A^0 P$ — new source term | **New result** |
| System is oscillatory with frequency $\sqrt{\Omega_1\Omega_2} \approx 2m$ | Established |
| Monodromy phase $\Phi_{\text{cycle}} \approx 2m T_{\text{cycle}} \sim 10^{54}$ | Confirmed (same order as before) |
| Chirality inversion condition: $\Phi_{\text{cycle}} = (2n-1)\pi$ — not generic | **Confirmed in correct convention** |
| $\kappa\alpha$ correction reduces $\Phi_{\text{cycle}}$ by a finite amount | New quantitative detail |
| Branch 2 $\eta$ sourcing by $A^0 P$ — new coupled dynamics | **New physical effect** |

### 6.2 What Changes and What Doesn't

**Unchanged from the previous monodromy analysis:**
- The qualitative conclusion that $M = -\mathbf{1}$ is not generic
- The order-of-magnitude estimate $\Phi_{\text{cycle}} \sim 10^{54}$
- The PT-1 claim revision in Appendix P v12

**Changed:**
- The bilinear evolution equations are now real with no spurious $i$ factors
- The monodromy matrix (M-correct) has a different structure from (M-final)
  in the previous document — $\Omega_1 \neq \Omega_2$ so the matrix is
  not simply $e^{i\alpha_-}\begin{pmatrix}\cos&i\sin\\i\sin&\cos\end{pmatrix}$
- Branch 2 has a new coupled $\eta$-sourcing effect
- The topological investigation conclusions are unaffected (the holonomy
  argument carries through with $\Phi_{\text{cycle}}$ replacing $\alpha_+$)

### 6.3 Remaining IVN Items

| IVN | Content | Priority |
|-----|---------|----------|
| IVN-I-1 | Verify (D'') by taking Dirac conjugate of (D') in $(+,-,-,-)$ | HIGH |
| IVN-I-2 | Verify component equations (C-xi) and (C-chi) | HIGH |
| IVN-I-3 | Verify $\dot{\eta} + 3H\eta = \kappa\alpha A^0 P$ term by term | CRITICAL |
| IVN-I-4 | Check $A^0$ contribution to $\dot{J}^0$ | HIGH |
| IVN-I-5 | Resolve apparent imaginary term in $\dot{J}^0$ | HIGH |
| IVN-I-6 | Verify eigenvectors of (Msys) | MEDIUM |
| IVN-I-7 | Derive monodromy matrix (M-correct) from mode solutions | HIGH |

### 6.4 Recommended Next Step

IVN-I-3 is the critical item — the $\eta$ sourcing in Branch 2 is a
new physical effect that was invisible in the wrong convention. If it
survives independent verification, it changes the Branch 2 cosmological
dynamics significantly and requires a revision of the CT-ix document's
Branch 2 analysis (Section P.10.5 of Appendix P v12).

After IVN-I-3 is verified, the natural next step is OQ-CT-ix-5: the
matter-creation epoch duration calculation, which now needs to account
for the coupled $(A^0, P, \eta)$ dynamics in Branch 2.

---

*SCH IVN-I: PT-1 Monodromy in $(+,-,-,-)$ — v1 | June 2026*
*Not for citation without author approval.*
*Main results: (1) Correct bilinear evolution equations derived with no
spurious $i$ factors. (2) Chirality inversion conclusion unchanged —
$\Phi_{\text{cycle}} \sim 10^{54}$, not generically $(2n-1)\pi$. (3) New
physical effect identified: in Branch 2, $\eta$ is sourced by $\kappa\alpha A^0 P$,
coupling the scalar condensate to the chiral oscillations.*
