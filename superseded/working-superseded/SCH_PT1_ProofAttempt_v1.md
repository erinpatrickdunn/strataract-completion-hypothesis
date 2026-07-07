# SCH — PT-1: Chirality Transformation Through the Bounce
## Proof Attempt — v1 | June 2026

**Status:** PROOF ATTEMPT. This document carries through the calculation
identified in the PT-1 Problem Specification (v1) as the recommended proof
strategy. All steps requiring independent verification are marked *(IVN)*.

**Claim to be established:**
$$A^0 = \bar{\psi}\gamma^0\gamma^5\psi \quad \text{satisfies} \quad
A^0(t_{\text{b}}^+) = -A^0(t_{\text{b}}^-) \tag{PT-1 claim}$$

where $t_{\text{b}}$ is the bounce time, and the superscripts $\pm$ denote
the post- and pre-bounce values in the limit as $t \to t_{\text{b}}$ from
each side.

**Prerequisite inputs used:**
- Cosmological Dirac equation (D) from CT-viii / Appendix P v11, P.9.5.3
- Bounce regularity: $\psi(t)$ continuous through $t_{\text{b}}$, P.9.6.3
- Branch 2 self-consistency: $A^0 \neq 0$ consistent with the field equations
- Conservation law $a^3 J^0 = \mathcal{J}$ from P.9.5.4
- Bilinear transformation table from PT-1 Problem Specification Section 6

---

## Section 1 — Setup: The Bilinear System Near the Bounce

### 1.1 The Cosmological Dirac Equation

From Appendix P v11, equation P.9.5.3:

$$i\gamma^0\dot{\psi} = \frac{3H}{2}\gamma^0\psi + m\psi
+ \frac{\lambda}{2}\eta\psi + \frac{\kappa\alpha}{2}A^0\gamma^0\gamma^5\psi
\tag{D}$$

Multiply on the left by $-i\gamma^0$ (using $(\gamma^0)^2 = -\mathbf{1}$ in
the $(-,+,+,+)$ signature): *(IVN-1: confirm $(\gamma^0)^2 = -\mathbf{1}$
in the convention of Appendix P.)*

$$\dot{\psi} = -i\gamma^0\left(\frac{3H}{2}\gamma^0\psi + m\psi
+ \frac{\lambda}{2}\eta\psi + \frac{\kappa\alpha}{2}A^0\gamma^0\gamma^5\psi\right)$$

$$= -\frac{3H}{2}\psi + i m\gamma^0\psi
+ i\frac{\lambda}{2}\eta\gamma^0\psi
+ i\frac{\kappa\alpha}{2}A^0\gamma^5\psi \tag{D'}$$

using $(\gamma^0)^2 = -\mathbf{1}$ in the first term and $-i\gamma^0 \cdot
\gamma^0\gamma^5 = -i(\gamma^0)^2\gamma^5 = i\gamma^5$ in the last.

The conjugate equation for $\dot{\bar{\psi}} = \frac{d}{dt}(\psi^\dagger\gamma^0)$:

$$\dot{\bar{\psi}} = -\frac{3H}{2}\bar{\psi}
- im\bar{\psi}\gamma^0
- i\frac{\lambda}{2}\eta\bar{\psi}\gamma^0
- i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5 \tag{D''}$$

*(IVN-2: derive (D'') by taking $\dagger$ of (D') and right-multiplying
by $\gamma^0$, tracking all signs.)*

### 1.2 The Four Bilinears

The relevant bilinears are:

$$\eta \equiv \bar{\psi}\psi, \quad
J^0 \equiv \bar{\psi}\gamma^0\psi, \quad
P \equiv \bar{\psi}\gamma^5\psi, \quad
A^0 \equiv \bar{\psi}\gamma^0\gamma^5\psi$$

These are the four Lorentz-scalar and Lorentz-vector-temporal bilinears
available in the homogeneous (spatially constant) cosmological ansatz.
All spatial bilinears vanish by the $S^3$ integration (P.9.4.1).

The Fierz identity in 4D relates these bilinears. In particular:

$$(\bar{\psi}\psi)^2 + (\bar{\psi}\gamma^5\psi)^2
= (\bar{\psi}\gamma^0\psi)^2 - (\bar{\psi}\gamma^0\gamma^5\psi)^2$$

i.e., $\eta^2 + P^2 = (J^0)^2 - (A^0)^2$, which is the norm relation
for the spinor in the cosmological reduction. *(IVN-3: verify this Fierz
identity in 4D Minkowski signature.)*

### 1.3 The Bounce Environment

At the bounce $t = t_{\text{b}}$: $H(t_{\text{b}}) = 0$, $\dot{a}(t_{\text{b}}) = 0$.

In the neighbourhood of the bounce, $H(t)$ passes through zero:

$$H(t) = \dot{H}(t_{\text{b}})\,(t - t_{\text{b}}) + O((t-t_{\text{b}})^2)$$

From the Raychaudhuri equation P.9.5.2 at the bounce ($H = 0$):

$$\dot{H}\big|_{t_{\text{b}}} = \frac{\ddot{a}}{a}\bigg|_{t_{\text{b}}}
= \frac{\kappa}{6}\left(2m\eta_{\text{b}}
+ \frac{\lambda}{2}\eta_{\text{b}}^2 - \kappa\alpha(A^0_{\text{b}})^2\right) > 0$$

where $\eta_{\text{b}} \equiv \eta(t_{\text{b}})$, $A^0_{\text{b}} \equiv
A^0(t_{\text{b}})$, and the inequality holds by the bounce existence condition
(P.9.6.2). So $\dot{H}(t_{\text{b}}) > 0$: $H$ passes through zero from
negative (pre-bounce collapse) to positive (post-bounce expansion).

Near the bounce, to leading order in $(t - t_{\text{b}})$:

$$H(t) \approx \dot{H}_{\text{b}}\,(t - t_{\text{b}}) \equiv h\,(t - t_{\text{b}})$$

where $h \equiv \dot{H}(t_{\text{b}}) > 0$ is a positive constant. *(IVN-4:
verify $h > 0$ from the bounce existence condition.)*

---

## Section 2 — Derivation of the Bilinear Evolution Equations

### 2.1 The $\eta$ Equation

$$\dot{\eta} = \dot{\bar{\psi}}\psi + \bar{\psi}\dot{\psi}$$

Substituting (D') and (D''):

$$\dot{\eta} = \left(-\frac{3H}{2}\bar{\psi} - im\bar{\psi}\gamma^0
- i\frac{\lambda}{2}\eta\bar{\psi}\gamma^0
- i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5\right)\psi$$

$$+ \bar{\psi}\left(-\frac{3H}{2}\psi + im\gamma^0\psi
+ i\frac{\lambda}{2}\eta\gamma^0\psi
+ i\frac{\kappa\alpha}{2}A^0\gamma^5\psi\right)$$

The $-3H/2$ terms give $-3H\eta$.

The $\pm im\bar{\psi}\gamma^0\psi$ terms: $-im\bar{\psi}\gamma^0\psi
+ im\bar{\psi}\gamma^0\psi = 0$. Cancel.

The $\pm i(\lambda/2)\eta\bar{\psi}\gamma^0\psi$ terms: cancel similarly.

The $\pm i(\kappa\alpha/2)A^0$ terms: $-i\frac{\kappa\alpha}{2}A^0\bar{\psi}
\gamma^5\psi + i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5\psi = 0$. Cancel.

**Result:**

$$\boxed{\dot{\eta} + 3H\eta = 0} \tag{E1}$$

This confirms the CT-ix result (E1) by explicit derivation from (D'') and (D').
*(IVN-5: this is IVN-2 from CT-ix — now completed here. Verify sign by
carrying each term through.)*

### 2.2 The $J^0$ Equation

$$\dot{J}^0 = \frac{d}{dt}(\bar{\psi}\gamma^0\psi)
= \dot{\bar{\psi}}\gamma^0\psi + \bar{\psi}\gamma^0\dot{\psi}$$

Substituting:

The $-3H/2$ terms: $-\frac{3H}{2}\bar{\psi}\gamma^0\psi
- \frac{3H}{2}\bar{\psi}\gamma^0\psi = -3H J^0$.

The $\pm im$ terms: $-im\bar{\psi}\gamma^0\gamma^0\psi
+ im\bar{\psi}\gamma^0\gamma^0\psi$. Since $(\gamma^0)^2 = -\mathbf{1}$:
$-im\bar{\psi}(-\mathbf{1})\psi + im\bar{\psi}(-\mathbf{1})\psi = 0$. Cancel.

The $\pm i(\lambda/2)\eta$ terms: same structure, cancel.

The $\pm i(\kappa\alpha/2)A^0$ terms:
$-i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5\gamma^0\psi
+ i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^0\gamma^5\psi$.

Using $\gamma^5\gamma^0 = -\gamma^0\gamma^5$ (since $\{\gamma^5,\gamma^\mu\}=0$):

$= +i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^0\gamma^5\psi
+ i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^0\gamma^5\psi
= i\kappa\alpha (A^0)^2 \cdot \frac{\bar{\psi}\gamma^0\gamma^5\psi}{A^0}$

Wait — this needs care. The term is:

$-i\frac{\kappa\alpha}{2}A^0(\bar{\psi}\gamma^5\gamma^0\psi)
+ i\frac{\kappa\alpha}{2}A^0(\bar{\psi}\gamma^0\gamma^5\psi)$

$= -i\frac{\kappa\alpha}{2}A^0(-A^0) + i\frac{\kappa\alpha}{2}A^0(A^0)$

$= i\frac{\kappa\alpha}{2}(A^0)^2 + i\frac{\kappa\alpha}{2}(A^0)^2
= i\kappa\alpha(A^0)^2$

But $i$ times a real quantity is imaginary, and $J^0$ must be real. 

*(IVN-6: resolve the apparent imaginary term in the $J^0$ equation. The
resolution is likely that $\bar{\psi}\gamma^5\gamma^0\psi$ is purely
imaginary, so the product with $i$ is real. Alternatively, in the
Dirac representation with $\psi$ a Dirac spinor, $A^0 = \bar{\psi}
\gamma^0\gamma^5\psi$ is real, but $\bar{\psi}\gamma^5\gamma^0\psi =
-\bar{\psi}\gamma^0\gamma^5\psi = -A^0$ is also real, making the sum
$i\kappa\alpha(A^0)^2$ imaginary. Check whether this term actually
vanishes by Hermiticity.)*

**Tentative result, pending IVN-6:**

$$\dot{J}^0 + 3H J^0 = 0 \tag{E-J}$$

which gives $J^0 \propto a^{-3}$, consistent with the conservation law
$a^3 J^0 = \mathcal{J}$ from P.9.5.4. The $A^0$ terms should cancel
or vanish by Hermiticity; IVN-6 must confirm this.

### 2.3 The $P$ Equation

$$\dot{P} = \frac{d}{dt}(\bar{\psi}\gamma^5\psi)
= \dot{\bar{\psi}}\gamma^5\psi + \bar{\psi}\gamma^5\dot{\psi}$$

The $-3H/2$ terms: $-3HP$.

The $\pm im$ terms: $-im\bar{\psi}\gamma^0\gamma^5\psi
+ im\bar{\psi}\gamma^5\gamma^0\psi$.

Using $\gamma^5\gamma^0 = -\gamma^0\gamma^5$:

$= -imA^0 + im(-A^0) = -2imA^0$

The $\pm i(\lambda/2)\eta$ terms: same structure as the mass terms,
giving $-2i(\lambda/2)\eta A^0 = -i\lambda\eta A^0$.

The $\pm i(\kappa\alpha/2)A^0$ terms:
$-i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5\gamma^5\psi
+ i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5\gamma^5\psi$

Since $(\gamma^5)^2 = +\mathbf{1}$: these reduce to
$-i\frac{\kappa\alpha}{2}A^0\eta + i\frac{\kappa\alpha}{2}A^0\eta = 0$. Cancel.

**Result:**

$$\boxed{\dot{P} + 3HP = -2i\left(m + \frac{\lambda}{2}\eta\right)A^0}
\tag{E-P}$$

*(IVN-7: the factor of $i$ on the right side requires examination.
In the Dirac representation, $P = \bar{\psi}\gamma^5\psi$ is
pseudo-scalar. If $A^0$ is real and $P$ is real, then the right side
must be real, which requires $(m + \lambda\eta/2)$ to be purely
imaginary or $A^0$ to be purely imaginary. In the condensate vacuum
the bilinears are typically real. Verify whether $P$ is real or
imaginary in the SCH cosmological context, and resolve the factor
of $i$.)*

**Note on the $i$ factor:** In the standard Dirac representation,
$\bar{\psi}\gamma^5\psi$ is *anti-Hermitian* as an operator but can
have real expectation values depending on the spinor. For the
cosmological spinor $\psi(t)$, the Wick-rotated or real-time
behaviour of $P$ should be determined from the ansatz. This is
not a sign error — it is a reality condition on the spinor
components that must be tracked.

### 2.4 The $A^0$ Equation

$$\dot{A}^0 = \frac{d}{dt}(\bar{\psi}\gamma^0\gamma^5\psi)
= \dot{\bar{\psi}}\gamma^0\gamma^5\psi + \bar{\psi}\gamma^0\gamma^5\dot{\psi}$$

The $-3H/2$ terms: $-3H A^0$.

The $\pm im$ terms:
$-im\bar{\psi}\gamma^0\gamma^0\gamma^5\psi
+ im\bar{\psi}\gamma^0\gamma^5\gamma^0\psi$

$= -im\bar{\psi}(-\mathbf{1})\gamma^5\psi
+ im\bar{\psi}\gamma^0\gamma^5\gamma^0\psi$

$= im\bar{\psi}\gamma^5\psi
+ im\bar{\psi}\gamma^0\gamma^5\gamma^0\psi$

For the second term: $\gamma^0\gamma^5\gamma^0 = -\gamma^0\gamma^0\gamma^5
= -(\gamma^0)^2\gamma^5 = -(-\mathbf{1})\gamma^5 = +\gamma^5$.

So: $imP + imP = 2imP$.

The $\pm i(\lambda/2)\eta$ terms: same structure, giving $2i(\lambda/2)\eta P
= i\lambda\eta P$.

The $\pm i(\kappa\alpha/2)A^0$ terms:
$-i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5\gamma^0\gamma^5\psi
+ i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^0\gamma^5\gamma^5\psi$

$= -i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^5\gamma^0\gamma^5\psi
+ i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^0\psi$

For the first term: $\gamma^5\gamma^0\gamma^5 = -\gamma^0\gamma^5\gamma^5
= -\gamma^0(\mathbf{1}) = -\gamma^0$. So this is
$+i\frac{\kappa\alpha}{2}A^0\bar{\psi}\gamma^0\psi
= +i\frac{\kappa\alpha}{2}A^0 J^0$.

Second term: $+i\frac{\kappa\alpha}{2}A^0 J^0$.

Sum: $i\kappa\alpha A^0 J^0$.

**Result:**

$$\boxed{\dot{A}^0 + 3H A^0 = 2i\left(m + \frac{\lambda}{2}\eta\right)P
+ i\kappa\alpha A^0 J^0} \tag{E-A}$$

*(IVN-8: verify the gamma matrix products step by step, especially
$\gamma^0\gamma^5\gamma^0 = +\gamma^5$ and $\gamma^5\gamma^0\gamma^5
= -\gamma^0$.)*

*(IVN-9: same $i$ factor issue as in (E-P). If $A^0$ and $P$ are both
real bilinears, the right side of (E-A) appears imaginary. The
coupling $J^0$ is real. Resolve the reality conditions on $P$ and
$A^0$ in the SCH cosmological context.)*

---

## Section 3 — The Bilinear System and Reality Conditions

### 3.1 Identifying the Reality Issue

Equations (E-P) and (E-A) both have factors of $i$ on the right side.
This is not a sign error. It reflects a structural property of the
spinor bilinears that must be addressed before the system can be
integrated through the bounce.

Define the real and imaginary parts of the spinor components. In the
Dirac representation with $\gamma^0 = \mathrm{diag}(\mathbf{1},-\mathbf{1})$,
write $\psi = (\xi, \chi)^T$ where $\xi, \chi$ are two-component spinors.

Then (from Appendix P v11, P.9.3):

$$\eta = \bar{\psi}\psi = i(\xi^\dagger\chi + \chi^\dagger\xi) \in \mathbb{R}$$

$$A^0 = \bar{\psi}\gamma^0\gamma^5\psi = -(\xi^\dagger\xi - \chi^\dagger\chi) \in \mathbb{R}$$

And by similar computation:

$$J^0 = \bar{\psi}\gamma^0\psi = \xi^\dagger\xi + \chi^\dagger\chi \in \mathbb{R}$$

$$P = \bar{\psi}\gamma^5\psi = i(\xi^\dagger\chi - \chi^\dagger\xi)$$

The expression for $P$ involves $i(\xi^\dagger\chi - \chi^\dagger\xi)$.
If $\xi^\dagger\chi$ is real, then $\xi^\dagger\chi - \chi^\dagger\xi =
\xi^\dagger\chi - (\xi^\dagger\chi)^* = 2i\,\mathrm{Im}(\xi^\dagger\chi)$,
making $P = -2\,\mathrm{Im}(\xi^\dagger\chi) \in \mathbb{R}$.

**So $P$ is real.** The factor of $i$ in (E-P) and (E-A) then requires
$(m + \lambda\eta/2)A^0$ and $(m + \lambda\eta/2)P$ to be imaginary for
the right sides to be real — but both are products of real quantities.

**Resolution:** The factor of $i$ is not an error in the algebra. It
indicates that equations (E-P) and (E-A) as written mix the real bilinears
$\{A^0, P\}$ with an imaginary driving term. The correct interpretation
is that in the cosmological context, the physical degrees of freedom in
$\psi$ are not all independently real.

The cosmological Dirac equation (D) is a complex ODE. The spinor $\psi$
has complex components. The bilinears $\eta$, $J^0$, $P$, $A^0$ are real
numbers (as shown above), but they are constructed from complex spinor
components. The equations (E-P) and (E-A) are therefore equations for
real quantities driven by terms that *appear* to have factors of $i$
but resolve to real quantities when the complex spinor components are
written out.

**Explicit resolution:** Define $\xi^\dagger\chi = u + iv$ where $u, v \in \mathbb{R}$.
Then:

$$\eta = 2u, \quad P = -2v, \quad J^0 = \xi^\dagger\xi + \chi^\dagger\chi,
\quad A^0 = \chi^\dagger\chi - \xi^\dagger\xi$$

The factor of $i$ in (E-P) then gives, for the mass term:

$$2i\left(m + \frac{\lambda}{2}\eta\right)A^0 = 2i\left(m + \lambda u\right)
(\chi^\dagger\chi - \xi^\dagger\xi)$$

This is imaginary times real, which is imaginary. But $\dot{P} + 3HP$
must be real since $P$ is real. This means the $\pm im$ terms in $\dot{P}$
must produce a real quantity despite the $i$ factor.

*(IVN-10: resolve by writing $\psi = (\xi,\chi)^T$ with complex components
and computing (E-P) directly in components. The factor of $i$ should
cancel against imaginary parts of the spinor components. This calculation
is essential before integrating the system through the bounce.)*

### 3.2 Alternative Approach: Work Directly in Components

Given the $i$ factor issue, the cleanest path forward is to bypass the
bilinear equations (E-P) and (E-A) and work directly with the cosmological
Dirac equation (D) in component form.

Write $\psi = (\xi,\chi)^T$ in the Dirac representation. Then (D) becomes
two coupled equations for $\xi(t)$ and $\chi(t)$.

In the Dirac representation:
$$\gamma^0 = \begin{pmatrix}\mathbf{1} & 0 \\ 0 & -\mathbf{1}\end{pmatrix},
\quad \gamma^5 = \begin{pmatrix}0 & \mathbf{1} \\ \mathbf{1} & 0\end{pmatrix},
\quad \gamma^0\gamma^5 = \begin{pmatrix}0 & \mathbf{1} \\ -\mathbf{1} & 0\end{pmatrix}$$

*(IVN-11: verify these matrix forms in the sign convention of Appendix P.)*

Substituting into (D) with $\psi = (\xi,\chi)^T$, and using $A^0 =
\bar{\psi}\gamma^0\gamma^5\psi = \chi^\dagger\chi - \xi^\dagger\xi$:

$$i\begin{pmatrix}\mathbf{1} & 0 \\ 0 & -\mathbf{1}\end{pmatrix}
\begin{pmatrix}\dot{\xi} \\ \dot{\chi}\end{pmatrix}
= \frac{3H}{2}\begin{pmatrix}\mathbf{1} & 0 \\ 0 & -\mathbf{1}\end{pmatrix}
\begin{pmatrix}\xi \\ \chi\end{pmatrix}
+ (m + \frac{\lambda}{2}\eta)\begin{pmatrix}\xi \\ \chi\end{pmatrix}
+ \frac{\kappa\alpha}{2}A^0
\begin{pmatrix}0 & \mathbf{1} \\ -\mathbf{1} & 0\end{pmatrix}
\begin{pmatrix}\xi \\ \chi\end{pmatrix}$$

Upper component ($\xi$):
$$i\dot{\xi} = \frac{3H}{2}\xi + \left(m + \frac{\lambda}{2}\eta\right)\xi
+ \frac{\kappa\alpha}{2}A^0\chi \tag{C-$\xi$}$$

Lower component ($\chi$):
$$-i\dot{\chi} = -\frac{3H}{2}\chi + \left(m + \frac{\lambda}{2}\eta\right)\chi
- \frac{\kappa\alpha}{2}A^0\xi$$

i.e.,
$$i\dot{\chi} = \frac{3H}{2}\chi - \left(m + \frac{\lambda}{2}\eta\right)\chi
+ \frac{\kappa\alpha}{2}A^0\xi \tag{C-$\chi$}$$

*(IVN-12: verify (C-$\xi$) and (C-$\chi$) by direct substitution into (D).)*

These are two coupled complex ODEs for the two-component spinors $\xi(t)$
and $\chi(t)$.

---

## Section 4 — Integration Through the Bounce

### 4.1 The Bounce as a Transition in $H$

At the bounce, $H$ passes through zero linearly:
$$H(t) = h(t - t_{\text{b}}) + O((t-t_{\text{b}})^2), \quad h > 0$$

Define $\tau \equiv t - t_{\text{b}}$, so $\tau < 0$ pre-bounce,
$\tau > 0$ post-bounce, $\tau = 0$ at the bounce.

In the neighbourhood of the bounce, $(m + \lambda\eta/2)$ and $A^0$
are approximately constant at their bounce values $\mu_{\text{b}} \equiv
m + \lambda\eta_{\text{b}}/2$ and $A^0_{\text{b}}$, since $\psi$ is
continuous (P.9.6.3) and the bilinears are continuous functions of $\psi$.

The component equations near the bounce become:

$$i\dot{\xi} = \frac{3h\tau}{2}\xi + \mu_{\text{b}}\xi
+ \frac{\kappa\alpha}{2}A^0_{\text{b}}\chi \tag{B-$\xi$}$$

$$i\dot{\chi} = \frac{3h\tau}{2}\chi - \mu_{\text{b}}\chi
+ \frac{\kappa\alpha}{2}A^0_{\text{b}}\xi \tag{B-$\chi$}$$

### 4.2 The Decoupled System at $\tau = 0$

At the bounce point itself ($\tau = 0$, $H = 0$), the $H$-dependent
terms vanish and the equations reduce to:

$$i\dot{\xi}\big|_{\tau=0} = \mu_{\text{b}}\xi_{\text{b}}
+ \frac{\kappa\alpha}{2}A^0_{\text{b}}\chi_{\text{b}} \tag{B0-$\xi$}$$

$$i\dot{\chi}\big|_{\tau=0} = -\mu_{\text{b}}\chi_{\text{b}}
+ \frac{\kappa\alpha}{2}A^0_{\text{b}}\xi_{\text{b}} \tag{B0-$\chi$}$$

These determine $\dot{\xi}$ and $\dot{\chi}$ at the bounce in terms of
$\xi_{\text{b}}$ and $\chi_{\text{b}}$.

### 4.3 Symmetry Analysis: The Key Observation

Examine the transformation $(\xi, \chi) \to (\chi, -\xi)$ applied to
(B-$\xi$) and (B-$\chi$):

Under $(\xi, \chi) \to (\chi, -\xi)$:
- (B-$\xi$) becomes: $i\dot{\chi} = \frac{3h\tau}{2}\chi + \mu_{\text{b}}\chi
  + \frac{\kappa\alpha}{2}A^0_{\text{b}}(-\xi)$
  $= \frac{3h\tau}{2}\chi + \mu_{\text{b}}\chi - \frac{\kappa\alpha}{2}A^0_{\text{b}}\xi$

Compare with (B-$\chi$): $i\dot{\chi} = \frac{3h\tau}{2}\chi - \mu_{\text{b}}\chi
+ \frac{\kappa\alpha}{2}A^0_{\text{b}}\xi$.

These differ in the sign of $\mu_{\text{b}}$ and the sign of the $A^0$
coupling. The transformation $(\xi,\chi) \to (\chi,-\xi)$ is not a
symmetry of the system — it changes $\mu_{\text{b}} \to -\mu_{\text{b}}$.

Now examine the transformation $(\xi,\chi) \to (\chi^*, -\xi^*)$
(complex conjugation composed with the above):

Under $t \to -\tau$ (time reversal at the bounce) and
$(\xi,\chi) \to (\chi^*,-\xi^*)$:

The time-reversed equation for $\xi$, with $H \to -H$ (i.e.,
$h\tau \to -h\tau$, since reversing time reverses the sign of $H$):

$$i(-\dot{\chi}^*) = \frac{3h\tau}{2}\chi^* + \mu_{\text{b}}\chi^*
- \frac{\kappa\alpha}{2}A^0_{\text{b}}\xi^*$$

Taking complex conjugate (since $\mu_{\text{b}}, h, A^0_{\text{b}}$
are all real):

$$-i\dot{\chi} = \frac{3h\tau}{2}\chi + \mu_{\text{b}}\chi
- \frac{\kappa\alpha}{2}A^0_{\text{b}}\xi$$

which gives $i\dot{\chi} = -\frac{3h\tau}{2}\chi - \mu_{\text{b}}\chi
+ \frac{\kappa\alpha}{2}A^0_{\text{b}}\xi$.

This matches (B-$\chi$) in the reversed-time regime ($\tau \to -\tau$,
so $3h\tau \to -3h\tau$). *(IVN-13: carry this symmetry analysis through
more carefully, tracking the sign of $\tau$ on both sides.)*

### 4.4 Direct Computation of $A^0$ Through the Bounce

Rather than relying on the symmetry argument, compute $A^0(\tau)$ directly
for small $|\tau|$.

At $\tau = 0$, $A^0_{\text{b}} = \chi_{\text{b}}^\dagger\chi_{\text{b}}
- \xi_{\text{b}}^\dagger\xi_{\text{b}}$.

Differentiate $A^0 = \chi^\dagger\chi - \xi^\dagger\xi$ with respect to $t$:

$$\dot{A}^0 = \dot{\chi}^\dagger\chi + \chi^\dagger\dot{\chi}
- \dot{\xi}^\dagger\xi - \xi^\dagger\dot{\xi}$$

From (C-$\xi$): $i\dot{\xi} = \frac{3H}{2}\xi + \mu\xi
+ \frac{\kappa\alpha}{2}A^0\chi$, so
$\dot{\xi} = -i\frac{3H}{2}\xi - i\mu\xi - i\frac{\kappa\alpha}{2}A^0\chi$

where $\mu \equiv m + \lambda\eta/2$.

And $\dot{\xi}^\dagger = +i\frac{3H}{2}\xi^\dagger + i\mu\xi^\dagger
+ i\frac{\kappa\alpha}{2}A^0\chi^\dagger$.

From (C-$\chi$): $\dot{\chi} = -i\frac{3H}{2}\chi + i\mu\chi
- i\frac{\kappa\alpha}{2}A^0\xi$

and $\dot{\chi}^\dagger = +i\frac{3H}{2}\chi^\dagger - i\mu\chi^\dagger
+ i\frac{\kappa\alpha}{2}A^0\xi^\dagger$.

Substituting:

$$\dot{A}^0 = \left(+i\frac{3H}{2}\chi^\dagger - i\mu\chi^\dagger
+ i\frac{\kappa\alpha}{2}A^0\xi^\dagger\right)\chi$$

$$+ \chi^\dagger\left(-i\frac{3H}{2}\chi + i\mu\chi
- i\frac{\kappa\alpha}{2}A^0\xi\right)$$

$$- \left(+i\frac{3H}{2}\xi^\dagger + i\mu\xi^\dagger
+ i\frac{\kappa\alpha}{2}A^0\chi^\dagger\right)\xi$$

$$- \xi^\dagger\left(-i\frac{3H}{2}\xi - i\mu\xi
- i\frac{\kappa\alpha}{2}A^0\chi\right)$$

The $3H/2$ terms:

$+i\frac{3H}{2}\chi^\dagger\chi - i\frac{3H}{2}\chi^\dagger\chi
- i\frac{3H}{2}\xi^\dagger\xi + i\frac{3H}{2}\xi^\dagger\xi = 0$

Wait — let me recount. From the $\dot{\chi}^\dagger\chi$ term:
$+i\frac{3H}{2}\chi^\dagger\chi$. From the $\chi^\dagger\dot{\chi}$ term:
$-i\frac{3H}{2}\chi^\dagger\chi$. These cancel.

From the $-\dot{\xi}^\dagger\xi$ term: $-i\frac{3H}{2}\xi^\dagger\xi$.
From the $-\xi^\dagger\dot{\xi}$ term: $+i\frac{3H}{2}\xi^\dagger\xi$.
These cancel.

All $3H/2$ terms cancel. $\checkmark$

The $\pm i\mu$ terms:

From $\dot{\chi}^\dagger\chi$: $-i\mu\chi^\dagger\chi$.
From $\chi^\dagger\dot{\chi}$: $+i\mu\chi^\dagger\chi$. Cancel.

From $-\dot{\xi}^\dagger\xi$: $-i\mu\xi^\dagger\xi$.
From $-\xi^\dagger\dot{\xi}$: $+i\mu\xi^\dagger\xi$. Cancel.

All $\mu$ terms cancel. $\checkmark$

The $\kappa\alpha A^0/2$ terms:

From $\dot{\chi}^\dagger\chi$: $+i\frac{\kappa\alpha}{2}A^0\xi^\dagger\chi$.
From $\chi^\dagger\dot{\chi}$: $-i\frac{\kappa\alpha}{2}A^0\chi^\dagger\xi$.
From $-\dot{\xi}^\dagger\xi$: $-i\frac{\kappa\alpha}{2}A^0\chi^\dagger\xi$.
From $-\xi^\dagger\dot{\xi}$: $+i\frac{\kappa\alpha}{2}A^0\xi^\dagger\chi$.

*(IVN-14: recheck the sign of the last two terms — $-\dot{\xi}^\dagger\xi$
and $-\xi^\dagger\dot{\xi}$ from the definition $\dot{A}^0 = -\dot{\xi}^\dagger\xi
- \xi^\dagger\dot{\xi} + \ldots$; confirm whether the signs as written
are correct.)*

Sum: $+i\frac{\kappa\alpha}{2}A^0(\xi^\dagger\chi - \chi^\dagger\xi)
+ i\frac{\kappa\alpha}{2}A^0(\xi^\dagger\chi - \chi^\dagger\xi)$

$= i\kappa\alpha A^0(\xi^\dagger\chi - \chi^\dagger\xi)$

Now $\xi^\dagger\chi - \chi^\dagger\xi = \xi^\dagger\chi - (\xi^\dagger\chi)^*
= 2i\,\mathrm{Im}(\xi^\dagger\chi)$.

And from the bilinear expressions: $P = i(\xi^\dagger\chi - \chi^\dagger\xi)
= i \cdot 2i\,\mathrm{Im}(\xi^\dagger\chi) = -2\,\mathrm{Im}(\xi^\dagger\chi)$.

So $\xi^\dagger\chi - \chi^\dagger\xi = iP$ *(using $P = -2\,\mathrm{Im}(\xi^\dagger\chi)$,
so $\mathrm{Im}(\xi^\dagger\chi) = -P/2$, giving $2i\,\mathrm{Im}(\xi^\dagger\chi)
= -iP$, so $\xi^\dagger\chi - \chi^\dagger\xi = -iP$)*.

*(IVN-15: confirm the sign: $\xi^\dagger\chi - \chi^\dagger\xi =
-iP$ given $P = i(\xi^\dagger\chi - \chi^\dagger\xi)$.)*

Substituting: the $\kappa\alpha$ contribution to $\dot{A}^0$ is:

$i\kappa\alpha A^0 \cdot (-iP) = \kappa\alpha A^0 P$

**Result:**

$$\boxed{\dot{A}^0 = \kappa\alpha A^0 P} \tag{E-A-explicit}$$

The Hubble friction term $-3H A^0$ is absent — the $3H/2$ terms all cancelled.
The $\mu$ terms all cancelled. The $A^0$ evolution is driven purely by the
product $\kappa\alpha A^0 P$.

*(IVN-16: confirm equation (E-A-explicit) is consistent with the general
form (E-A) derived earlier. The $3H$ dilution term vanishing here may
indicate an error in (E-A) — the general form should reduce to (E-A-explicit)
when computed directly in components. This is the critical verification.)*

---

## Section 5 — Interpretation of (E-A-explicit) and the Bounce

### 5.1 The System Near the Bounce

The coupled system for $(A^0, P)$ near the bounce, using the full
bilinear evolution:

From (E-A-explicit): $\dot{A}^0 = \kappa\alpha A^0 P$

From (E-P) (accepting the structure pending IVN-7 and IVN-10 resolution,
and taking the component-level result analogously):

$$\dot{P} = -3HP - 2\mu A^0 \tag{E-P-explicit}$$

*(IVN-17: derive (E-P-explicit) directly from components, analogously
to the $\dot{A}^0$ calculation above.)*

Near the bounce, $H = h\tau$:

$$\dot{A}^0 = \kappa\alpha A^0 P \tag{S1}$$

$$\dot{P} = -3h\tau P - 2\mu_{\text{b}} A^0 \tag{S2}$$

where $\mu_{\text{b}} = m + \lambda\eta_{\text{b}}/2 > 0$.

### 5.2 Behaviour at the Bounce Point

At $\tau = 0$ exactly:

$$\dot{A}^0\big|_{\tau=0} = \kappa\alpha A^0_{\text{b}} P_{\text{b}} \tag{S1-b}$$

$$\dot{P}\big|_{\tau=0} = -2\mu_{\text{b}} A^0_{\text{b}} \tag{S2-b}$$

From (S2-b): $P$ is changing at the bounce, driven by $A^0_{\text{b}}$.

From (S1-b): $A^0$ is changing at the bounce, driven by $A^0_{\text{b}} P_{\text{b}}$.

### 5.3 The Sign of $A^0$ Through the Bounce

Consider the second derivative of $A^0$:

$$\ddot{A}^0 = \kappa\alpha(\dot{A}^0 P + A^0\dot{P})
= \kappa\alpha(\kappa\alpha A^0 P^2 + A^0(-3h\tau P - 2\mu_{\text{b}} A^0))$$

$= \kappa\alpha A^0(\kappa\alpha P^2 - 3h\tau P - 2\mu_{\text{b}} A^0)$

At $\tau = 0$:

$$\ddot{A}^0\big|_{\tau=0} = \kappa\alpha A^0_{\text{b}}(\kappa\alpha P_{\text{b}}^2
- 2\mu_{\text{b}} A^0_{\text{b}}) \tag{2deriv}$$

The Taylor expansion of $A^0(\tau)$ around $\tau = 0$:

$$A^0(\tau) = A^0_{\text{b}} + \tau\,\kappa\alpha A^0_{\text{b}} P_{\text{b}}
+ \frac{\tau^2}{2}\kappa\alpha A^0_{\text{b}}(\kappa\alpha P_{\text{b}}^2
- 2\mu_{\text{b}} A^0_{\text{b}}) + O(\tau^3)$$

$$= A^0_{\text{b}}\left[1 + \tau\,\kappa\alpha P_{\text{b}}
+ \frac{\tau^2}{2}\kappa\alpha(\kappa\alpha P_{\text{b}}^2
- 2\mu_{\text{b}} A^0_{\text{b}}) + O(\tau^3)\right] \tag{Taylor-A}$$

**This does not show $A^0$ changing sign near the bounce.** The leading
correction is $+\tau\,\kappa\alpha A^0_{\text{b}} P_{\text{b}}$, which is
linear in $\tau$ and therefore changes sign across $\tau = 0$, but $A^0$
itself does not change sign unless the Taylor series drives it through zero.

### 5.4 When Does $A^0$ Change Sign?

From (Taylor-A), $A^0(\tau) = 0$ when:

$$1 + \tau\,\kappa\alpha P_{\text{b}} + O(\tau^2) = 0$$

$$\tau_0 \approx -\frac{1}{\kappa\alpha P_{\text{b}}}$$

This is a zero of $A^0$ at time $\tau_0 \neq 0$ — not at the bounce itself.
$A^0$ would change sign at $t = t_{\text{b}} + \tau_0$, which is either before
or after the bounce depending on the sign of $P_{\text{b}}$.

**This is a significant finding.** The cosmological Dirac equation does not
generically produce $A^0(t_{\text{b}}^+) = -A^0(t_{\text{b}}^-)$. That is:

> *$A^0$ is continuous through the bounce (as required by the regularity
> of the ODE), and whether it subsequently changes sign depends on the
> dynamics over a timescale $|\tau_0| \sim 1/(\kappa\alpha|P_{\text{b}}|)$
> rather than instantaneously at the bounce.*

---

## Section 6 — What This Means for PT-1

### 6.1 The Result

The direct ODE analysis produces the following:

1. $A^0$ is **continuous** through the bounce. This follows from P.9.6.3
   (bounce regularity) and is confirmed by (E-A-explicit) having no singularity
   at $H = 0$.

2. $A^0$ does **not** instantaneously change sign at the bounce. There is no
   discontinuity, no operator insertion, no automatic sign flip at $t = t_{\text{b}}$.

3. Whether $A^0$ changes sign over a bounce cycle depends on whether the
   trajectory in $(A^0, P)$ space encircles the origin between one bounce and
   the next. This is a global property of the solution over the full cosmological
   cycle, not a local property of the bounce point.

4. The relevant timescale for $A^0$ evolution is $|\tau_0| \sim 1/(\kappa\alpha
   |P_{\text{b}}|)$. Whether this timescale is short compared to the cosmological
   cycle period determines whether sign inversion occurs before or after the
   next bounce.

### 6.2 The Corrected Claim

The PT-1 claim as stated in P.7.7.2 — *"the antipodal map of $S^3$ acts
non-trivially on the global section of the spinor field $\psi$ through the
bounce, inducing $A^\mu \to -A^\mu$"* — requires revision.

The correct statement, supported by this analysis, is:

> **$A^0$ does not change sign instantaneously at the bounce. Whether $A^0$
> changes sign over one complete cosmological cycle depends on the global
> trajectory of the $(A^0, P)$ dynamical system over that cycle. Sign
> inversion per cycle is a sufficient but not necessary consequence of the
> dynamics, and whether it occurs requires analysis of the full-cycle solution
> of equations (S1) and (S2).**

This is a strictly weaker and more accurate claim than P.7.7.2.

### 6.3 Can the Weaker Claim Still Support the Physical Prediction?

The physical prediction — that successive cycles alternate matter/antimatter
dominance — does not require $A^0$ to change sign *at* the bounce. It requires
$A^0$ to have opposite sign in the post-bounce condensate compared to the
pre-bounce condensate, integrated over the matter-creation epoch. This is a
statement about the net chirality of the condensate averaged over the epoch
$T < T_c$ during which matter forms, not a statement about the instantaneous
value at the bounce point (where the condensate is melted, $\eta = 0$,
and $A^0$ is not directly physically meaningful for matter creation).

The question becomes: does the $(A^0, P)$ system, evolved through one
cosmological cycle, return with $A^0$ having the opposite sign? This is
a global question about the ODE system (S1)-(S2) over the full development
parameter $\phi \in [0, 2\pi]$ of the parametric solution (sol-III) from CT-ix.

### 6.4 The Global Cycle Analysis

The system (S1)-(S2) on the full cosmological cycle:

$$\frac{dA^0}{d\phi} = \frac{\kappa\alpha A^0 P}{\dot{\phi}}$$

$$\frac{dP}{d\phi} = \frac{-3H P - 2\mu A^0}{\dot{\phi}}$$

where $\phi$ is the development parameter from (sol-III) and $\dot{\phi}
= d\phi/dt > 0$ throughout the expanding phase.

On the contracting phase ($\phi \in (\pi, 2\pi)$), $\dot{a} < 0$ and
the equations run in reverse. The full cycle maps $(A^0, P)$ at $\phi = 0$
to $(A^0, P)$ at $\phi = 2\pi$.

Whether the map $(A^0, P)|_{\phi=0} \to (A^0, P)|_{\phi=2\pi}$ sends
$A^0 \to -A^0$ is determined by the monodromy of the linear system
(S1)-(S2) around the cycle.

**The monodromy of a non-autonomous linear ODE system** is a matrix
$M \in \mathrm{GL}(2,\mathbb{R})$ (for a 2D real system) such that
$(A^0, P)|_{\phi=2\pi} = M\,(A^0, P)|_{\phi=0}$.

If $\det(M) > 0$ and $M = -\mathbf{1}$ (up to rotation), then $A^0 \to -A^0$
and $P \to -P$ after one cycle. Whether $M = -\mathbf{1}$ is a quantitative
question that requires integrating the system (S1)-(S2) over the full cycle.

*(IVN-18: this is the key calculation that PT-1 must complete. It requires
numerical integration of (S1)-(S2) over the parametric solution (sol-III)
for generic parameter values, and possibly an analytic argument for why the
monodromy matrix takes the value $-\mathbf{1}$ rather than some other
$\mathrm{GL}(2,\mathbb{R})$ matrix.)*

---

## Section 7 — Summary and Revised Status

### 7.1 What This Calculation Established

| Result | Status |
|--------|--------|
| $\dot{\eta} + 3H\eta = 0$ confirmed by explicit derivation | Established (pending IVN-5) |
| $\dot{A}^0 = \kappa\alpha A^0 P$ (no Hubble friction) | Established (pending IVN-14–16) |
| $A^0$ is continuous through the bounce | Established (from regularity) |
| $A^0$ does not instantaneously change sign at the bounce | Established |
| $A^0$ sign change depends on global cycle monodromy | Identified — not yet computed |
| $P$ equation: $\dot{P} = -3HP - 2\mu A^0$ | Tentative (pending IVN-17) |
| PT-1 claim as stated in P.7.7.2 requires revision | Established |

### 7.2 What Remains for PT-1

**Required for PT-1 completion:**

1. Resolve all IVN items in Section 2–4 (IVN-6 through IVN-17).

2. Confirm the component equations (C-$\xi$) and (C-$\chi$) (IVN-12).

3. Compute the monodromy matrix $M$ for the $(A^0, P)$ system over one
   full cosmological cycle. This is the key calculation (IVN-18).

4. Determine whether $M = -\mathbf{1}$ (chirality inversion), $M = +\mathbf{1}$
   (chirality preservation), or $M$ is some other matrix (mixed outcome).

5. If $M$ depends on the action parameters $\{m, \lambda, \alpha, \kappa, \eta_0\}$,
   determine the parameter conditions under which $M = -\mathbf{1}$.

6. If $M \neq \pm\mathbf{1}$ for generic parameters, the PT-1 claim as stated
   does not follow from the dynamics and must be revised.

### 7.3 Revised Epistemic Status of PT-1 Claim

The claim in P.7.7.2 that the bounce induces $A^\mu \to -A^\mu$ is:

- **Not established** as a local result at the bounce point. The ODE analysis
  shows $A^0$ is continuous through the bounce with no local sign change.

- **Potentially established** as a global result over one cosmological cycle,
  if the monodromy matrix of the $(A^0, P)$ system is $M = -\mathbf{1}$.

- **Dependent on parameter values** in general. The monodromy calculation
  (IVN-18) must be completed to determine whether $M = -\mathbf{1}$ holds
  generically, conditionally, or not at all.

The physical prediction — alternating matter/antimatter cycles — is not
ruled out. But it is not established by this analysis. It is reframed as
a question about the monodromy of the bilinear ODE system, which is
a well-defined calculation.

---

## Section 8 — IVN Checklist

| IVN | Content | Priority |
|-----|---------|----------|
| IVN-1 | Confirm $(\gamma^0)^2 = -\mathbf{1}$ in Appendix P convention | HIGH |
| IVN-2 | Derive (D'') from (D') explicitly | HIGH |
| IVN-3 | Verify Fierz norm relation $\eta^2 + P^2 = (J^0)^2 - (A^0)^2$ | MEDIUM |
| IVN-4 | Confirm $h = \dot{H}(t_{\text{b}}) > 0$ from bounce condition | HIGH |
| IVN-5 | Full derivation of $\dot{\eta} + 3H\eta = 0$ term by term | HIGH |
| IVN-6 | Resolve apparent imaginary term in $\dot{J}^0$ equation | HIGH |
| IVN-7 | Resolve $i$ factor in (E-P); establish reality of $P$ | HIGH |
| IVN-8 | Verify $\gamma^0\gamma^5\gamma^0 = +\gamma^5$ and $\gamma^5\gamma^0\gamma^5 = -\gamma^0$ | HIGH |
| IVN-9 | Resolve $i$ factor in (E-A) | HIGH |
| IVN-10 | Full component derivation of (E-P) | HIGH |
| IVN-11 | Verify gamma matrix forms in Dirac representation | HIGH |
| IVN-12 | Verify (C-$\xi$) and (C-$\chi$) by direct substitution | HIGH |
| IVN-13 | Complete the symmetry analysis in Section 4.3 | MEDIUM |
| IVN-14 | Recheck signs in $\dot{A}^0$ component calculation | HIGH |
| IVN-15 | Confirm $\xi^\dagger\chi - \chi^\dagger\xi = -iP$ | HIGH |
| IVN-16 | Verify consistency of (E-A-explicit) with (E-A) | CRITICAL |
| IVN-17 | Derive (E-P-explicit) directly from components | HIGH |
| IVN-18 | Compute monodromy matrix $M$ for $(A^0,P)$ over one cycle | CRITICAL |

---

*SCH PT-1 Proof Attempt — v1 | June 2026*
*Not for citation without author approval.*
*This document reports an attempt, not a completed proof. The main result
is that the claim requires revision: $A^0$ does not change sign locally
at the bounce, and whether it changes sign globally over one cycle depends
on the monodromy of the $(A^0, P)$ system — a calculation identified but
not yet completed.*
