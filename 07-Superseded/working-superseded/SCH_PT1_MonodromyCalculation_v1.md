# SCH — PT-1 Monodromy Calculation
## Does $A^0$ Change Sign Over One Cosmological Cycle?

*Working Document — v1 | June 2026*

**Status:** PROOF ATTEMPT — MONODROMY CALCULATION (IVN-18 from PT-1 v1)

**Input equations from IVN-16 Resolution:**

$$\dot{A}^0 = i(2m + \lambda\eta)P - i\kappa\alpha J^0 A^0 \tag{S1}$$

$$\dot{P} = i(2m + \lambda\eta)A^0 - i\kappa\alpha J^0 P \tag{S2}$$

with:
- $\eta(t) = \eta_0 / a(t)^3$ (from E1, confirmed by IVN-16)
- $J^0 = \mathcal{J} / a(t)^3$ (conservation law, P.9.5.4)
- $a(t)$ given by the Branch 1 parametric solution (CT-ix, sol-III)

**Claim to evaluate:** Whether the monodromy matrix $M$ of the system
(S1)-(S2) over one complete cosmological cycle satisfies $M = -\mathbf{1}$,
which would give $A^0 \to -A^0$ and $P \to -P$ per cycle.

---

## Section 1 — Preliminary Simplification

### 1.1 Substitution and Rescaling

Define the combined time-varying frequency:

$$\Omega(t) \equiv 2m + \lambda\eta(t) = 2m + \frac{\lambda\eta_0}{a(t)^3}
\tag{def-Omega}$$

And the damping coefficient:

$$\Gamma(t) \equiv \kappa\alpha J^0(t) = \frac{\kappa\alpha\mathcal{J}}{a(t)^3}
\tag{def-Gamma}$$

Both are positive (assuming $m, \lambda, \eta_0, \mathcal{J}, \kappa, \alpha > 0$)
and both decay as $a^{-3}$ at late times.

The system (S1)-(S2) becomes:

$$\dot{A}^0 = i\Omega P - i\Gamma A^0 \tag{S1'}$$

$$\dot{P} = i\Omega A^0 - i\Gamma P \tag{S2'}$$

This is a $2\times 2$ linear ODE system. Write it in matrix form:

$$\frac{d}{dt}\begin{pmatrix}A^0\\P\end{pmatrix}
= i\begin{pmatrix}-\Gamma & \Omega \\ \Omega & -\Gamma\end{pmatrix}
\begin{pmatrix}A^0\\P\end{pmatrix} \tag{matrix}$$

### 1.2 Diagonalisation

The matrix $\mathcal{M}(t) = i\begin{pmatrix}-\Gamma & \Omega \\ \Omega & -\Gamma\end{pmatrix}$
has eigenvalues:

$$\mu_\pm = i(-\Gamma \pm \Omega) \tag{eigenvalues}$$

with eigenvectors $\mathbf{v}_+ = \begin{pmatrix}1\\1\end{pmatrix}$
and $\mathbf{v}_- = \begin{pmatrix}1\\-1\end{pmatrix}$.

Define normal modes:

$$u \equiv A^0 + P, \qquad v \equiv A^0 - P \tag{modes}$$

The decoupled equations:

$$\dot{u} = i(-\Gamma + \Omega)u = i(\Omega - \Gamma)u \tag{u-eq}$$

$$\dot{v} = i(-\Gamma - \Omega)v = -i(\Omega + \Gamma)v \tag{v-eq}$$

These are first-order linear ODEs with time-varying coefficients.

### 1.3 Formal Solutions

$$u(t) = u(t_0)\exp\left(i\int_{t_0}^t (\Omega(s) - \Gamma(s))\,ds\right)
\tag{u-sol}$$

$$v(t) = v(t_0)\exp\left(-i\int_{t_0}^t (\Omega(s) + \Gamma(s))\,ds\right)
\tag{v-sol}$$

The monodromy over one full cycle $[t_{\text{b}}, t_{\text{b}} + T_{\text{cycle}}]$
(where $T_{\text{cycle}}$ is the period of the cosmological cycle) is:

$$u \to u \cdot e^{i\Phi_-}, \qquad v \to v \cdot e^{-i\Phi_+}$$

where:

$$\Phi_- \equiv \int_{\text{cycle}} (\Omega - \Gamma)\,dt
= \int_{\text{cycle}} \left(2m + \frac{\lambda\eta_0}{a^3}
- \frac{\kappa\alpha\mathcal{J}}{a^3}\right)dt \tag{Phi-minus}$$

$$\Phi_+ \equiv \int_{\text{cycle}} (\Omega + \Gamma)\,dt
= \int_{\text{cycle}} \left(2m + \frac{\lambda\eta_0}{a^3}
+ \frac{\kappa\alpha\mathcal{J}}{a^3}\right)dt \tag{Phi-plus}$$

---

## Section 2 — The Monodromy Matrix

### 2.1 The Monodromy in $(A^0, P)$ Basis

Inverting the mode definition:
$A^0 = (u+v)/2$, $P = (u-v)/2$.

After one cycle:
$$u \to e^{i\Phi_-}u, \quad v \to e^{-i\Phi_+}v$$

So:
$$A^0 \to \frac{e^{i\Phi_-}u + e^{-i\Phi_+}v}{2}
= \frac{e^{i\Phi_-}(A^0+P) + e^{-i\Phi_+}(A^0-P)}{2}$$

$$= \frac{e^{i\Phi_-}+e^{-i\Phi_+}}{2}A^0
+ \frac{e^{i\Phi_-}-e^{-i\Phi_+}}{2}P$$

$$P \to \frac{e^{i\Phi_-}u - e^{-i\Phi_+}v}{2}
= \frac{e^{i\Phi_-}-e^{-i\Phi_+}}{2}A^0
+ \frac{e^{i\Phi_-}+e^{-i\Phi_+}}{2}P$$

The monodromy matrix in the $(A^0, P)$ basis:

$$M = \begin{pmatrix}
\cos\Phi_{\text{avg}} e^{i\Phi_{\text{diff}}} &
i\sin\Phi_{\text{avg}} e^{i\Phi_{\text{diff}}} \\
i\sin\Phi_{\text{avg}} e^{i\Phi_{\text{diff}}} &
\cos\Phi_{\text{avg}} e^{i\Phi_{\text{diff}}}
\end{pmatrix} \tag{M-matrix}$$

where $\Phi_{\text{avg}} \equiv (\Phi_- + \Phi_+)/2$ and
$\Phi_{\text{diff}} \equiv (\Phi_- - \Phi_+)/2$.

*(IVN-M1: verify the algebra leading to M-matrix by explicit
substitution of the mode solutions back into $(A^0, P)$.)*

More explicitly:

$$\frac{e^{i\Phi_-}+e^{-i\Phi_+}}{2}
= e^{i(\Phi_- - \Phi_+)/2}\cos\!\left(\frac{\Phi_-+\Phi_+}{2}\right)$$

Wait — let me be more careful. Define:

$$\alpha_+ \equiv \frac{\Phi_- + \Phi_+}{2} = \int_{\text{cycle}}
\left(2m + \frac{\lambda\eta_0}{a^3}\right)dt = \int_{\text{cycle}}\Omega\,dt$$

$$\alpha_- \equiv \frac{\Phi_- - \Phi_+}{2} = -\int_{\text{cycle}}
\frac{\kappa\alpha\mathcal{J}}{a^3}\,dt = -\int_{\text{cycle}}\Gamma\,dt$$

Then $\Phi_- = \alpha_+ + \alpha_-$ and $\Phi_+ = \alpha_+ - \alpha_-$,
giving $e^{i\Phi_-} = e^{i\alpha_+}e^{i\alpha_-}$ and
$e^{-i\Phi_+} = e^{-i\alpha_+}e^{i\alpha_-}$.

So:

$$\frac{e^{i\Phi_-}+e^{-i\Phi_+}}{2}
= e^{i\alpha_-}\cdot\frac{e^{i\alpha_+}+e^{-i\alpha_+}}{2}
= e^{i\alpha_-}\cos\alpha_+$$

$$\frac{e^{i\Phi_-}-e^{-i\Phi_+}}{2}
= e^{i\alpha_-}\cdot\frac{e^{i\alpha_+}-e^{-i\alpha_+}}{2}
= ie^{i\alpha_-}\sin\alpha_+$$

Therefore the monodromy matrix is:

$$\boxed{M = e^{i\alpha_-}
\begin{pmatrix}\cos\alpha_+ & i\sin\alpha_+ \\
i\sin\alpha_+ & \cos\alpha_+\end{pmatrix}}
\tag{M-final}$$

where:

$$\alpha_+ = \int_{\text{cycle}}\Omega(t)\,dt
= \int_{\text{cycle}}\left(2m + \frac{\lambda\eta_0}{a^3}\right)dt
\tag{alpha-plus}$$

$$\alpha_- = -\int_{\text{cycle}}\Gamma(t)\,dt
= -\int_{\text{cycle}}\frac{\kappa\alpha\mathcal{J}}{a^3}\,dt
\tag{alpha-minus}$$

### 2.2 When Does $M = -\mathbf{1}$?

$M = -\mathbf{1}$ requires:

$$e^{i\alpha_-}\cos\alpha_+ = -1 \quad \text{and} \quad
e^{i\alpha_-}\sin\alpha_+ = 0$$

From the second condition: $\sin\alpha_+ = 0$, so $\alpha_+ = n\pi$
for integer $n$.

From the first condition with $\sin\alpha_+ = 0$:
$e^{i\alpha_-}\cos(n\pi) = -1$, so $e^{i\alpha_-}(\pm 1) = -1$.

**Case $n$ odd** ($\cos\alpha_+ = -1$): $e^{i\alpha_-}(-1) = -1$,
so $e^{i\alpha_-} = +1$, requiring $\alpha_- = 2k\pi$ for integer $k$.

**Case $n$ even** ($\cos\alpha_+ = +1$): $e^{i\alpha_-}(+1) = -1$,
so $e^{i\alpha_-} = -1$, requiring $\alpha_- = (2k+1)\pi$.

**Summary:** $M = -\mathbf{1}$ if and only if:

$$\alpha_+ = (2n-1)\pi \text{ and } \alpha_- = 2k\pi
\quad \text{(case A)}$$

or

$$\alpha_+ = 2n\pi \text{ and } \alpha_- = (2k+1)\pi
\quad \text{(case B)}$$

for integers $n, k$.

---

## Section 3 — Evaluating the Phase Integrals

### 3.1 The Cycle and the Integration Variable

Use the parametric solution from CT-ix (sol-III):

$$a(\phi) = \frac{a_{\text{max}}}{2}(1 - \cos\phi), \qquad
t(\phi) = \frac{t_{\text{max}}}{\pi}(\phi - \sin\phi)$$

$$\dot{\phi} = \frac{dt}{d\phi}^{-1} = \frac{\pi}{t_{\text{max}}}
\cdot \frac{1}{1 - \cos\phi} \tag{phi-dot}$$

One full cycle runs $\phi \in [0, 2\pi]$ (from bounce to bounce).
$dt = d\phi/\dot{\phi} = \frac{t_{\text{max}}}{\pi}(1-\cos\phi)\,d\phi$.

**Note on the bounce:** Near $\phi = 0$ and $\phi = 2\pi$, $a \to 0$
and $\Omega, \Gamma \to \infty$. The Phase I (stiff-condensate) regime
from CT-ix governs this neighbourhood. The Phase III parametric solution
is an approximation valid for $a \gg a_*$. The integrals must include
the Phase I regime near the bounce.

For the purpose of this calculation, work in the Phase III approximation
($a \gg a_*$, $\lambda\eta_0/a^3 \ll 2m$) first, then assess the Phase I
contribution separately.

### 3.2 The $\alpha_+$ Integral in Phase III

In Phase III ($\lambda\eta_0/a^3 \ll 2m$), $\Omega \approx 2m$:

$$\alpha_+ \approx 2m \cdot T_{\text{cycle}} = 2m \cdot 2t_{\text{max}}$$

From CT-ix equation (tmax): $t_{\text{max}} = (\pi/2)a_{\text{max}}$.

$$\alpha_+ \approx 4m \cdot \frac{\pi}{2}a_{\text{max}} = 2\pi m\,a_{\text{max}}
\tag{alpha-plus-III}$$

The condition $\alpha_+ = n\pi$ (for $M = -\mathbf{1}$) becomes:

$$2\pi m\,a_{\text{max}} = n\pi \quad \Rightarrow \quad
m\,a_{\text{max}} = \frac{n}{2} \tag{quantization-A}$$

From CT-ix equation (amax-explicit): $a_{\text{max}} = \kappa m\eta_0/3$.

$$m \cdot \frac{\kappa m\eta_0}{3} = \frac{n}{2}
\quad \Rightarrow \quad
m^2\eta_0 = \frac{3n}{2\kappa} \tag{quantization-B}$$

**This is a quantization condition on the action parameters.** Whether it
is satisfied depends on the values of $m$, $\eta_0$, and $\kappa = 8\pi G/c^4$.

The condition is not automatically satisfied for all parameter values.
This is a key finding: $M = -\mathbf{1}$ is not generic. It holds only
when the action parameters satisfy (quantization-B).

### 3.3 The $\alpha_-$ Integral in Phase III

$$\alpha_- = -\int_{\text{cycle}}\Gamma\,dt
= -\kappa\alpha\mathcal{J}\int_{\text{cycle}}\frac{dt}{a^3}$$

Using the parametric solution:

$$\int_{\text{cycle}}\frac{dt}{a^3}
= \int_0^{2\pi}\frac{1}{a(\phi)^3}\cdot\frac{t_{\text{max}}}{\pi}(1-\cos\phi)\,d\phi$$

$$= \frac{t_{\text{max}}}{\pi}\int_0^{2\pi}
\frac{1-\cos\phi}{\left(\frac{a_{\text{max}}}{2}\right)^3(1-\cos\phi)^3}\,d\phi$$

$$= \frac{t_{\text{max}}}{\pi}\cdot\frac{8}{a_{\text{max}}^3}
\int_0^{2\pi}\frac{d\phi}{(1-\cos\phi)^2} \tag{integral-a3}$$

The integral $\int_0^{2\pi}\frac{d\phi}{(1-\cos\phi)^2}$ diverges at
$\phi = 0$ and $\phi = 2\pi$ (where $1 - \cos\phi \to 0$).

**The integral diverges.** This means $\alpha_-$ diverges in the Phase III
approximation, which breaks down near the bounce ($\phi \to 0, 2\pi$).

This divergence is physical: near the bounce, $a \to 0$ and
$J^0/a^3 = \mathcal{J}/a^6 \to \infty$. The Phase III approximation
is not valid here. The Phase I solution must be used near the bounce.

### 3.4 Phase I Contribution Near the Bounce

From CT-ix equation (sol-I): near the bounce, $a(\tau) = C|\tau|^{1/3}$
where $C = (3\sqrt{\kappa\lambda\eta_0^2/12})^{1/3}$ and $\tau = t - t_{\text{b}}$.

In Phase I:
$$\frac{1}{a^3} = \frac{1}{C^3|\tau|} \quad \Rightarrow \quad
\int_{\text{Phase I}}\frac{dt}{a^3} \propto \int_\epsilon^{\tau_*}\frac{d\tau}{\tau}
= \ln(\tau_*/\epsilon) \tag{log-diverge}$$

This logarithmic divergence in $\tau$ as $\epsilon \to 0$ (approaching
the bounce) means $\alpha_-$ is logarithmically divergent as the bounce
is approached.

**Physical interpretation:** The $\Gamma$ term in the ODE represents
coupling of the $(A^0, P)$ system to $J^0$ — the vector current density.
Near the bounce, the matter density diverges (all matter is compressed
into a small $a$), making $J^0/a^3$ diverge. The $(A^0, P)$ system
rotates infinitely fast near the bounce in the normal-mode decomposition.

The total accumulated phase $\alpha_-$ is formally infinite. This does
not mean the monodromy is undefined — it means the normal-mode phases
$\Phi_\pm$ both diverge, but their combination in the monodromy matrix
may still be well-defined if the divergences cancel.

### 3.5 Cancellation Analysis

$$\Phi_- = \alpha_+ + \alpha_- = \int_{\text{cycle}}(\Omega - \Gamma)\,dt$$

$$\Phi_+ = \alpha_+ - \alpha_- = \int_{\text{cycle}}(\Omega + \Gamma)\,dt$$

Near the bounce, $\Omega \approx \lambda\eta_0/a^3$ and
$\Gamma = \kappa\alpha\mathcal{J}/a^3$. Their difference:

$$\Omega - \Gamma = \frac{\lambda\eta_0 - \kappa\alpha\mathcal{J}}{a^3}$$

If $\lambda\eta_0 = \kappa\alpha\mathcal{J}$ exactly, then $\Omega - \Gamma = 0$
near the bounce and $\Phi_-$ is finite. But $\Phi_+$ still diverges.

If $\lambda\eta_0 \neq \kappa\alpha\mathcal{J}$, both $\Phi_-$ and $\Phi_+$
diverge logarithmically near the bounce.

The monodromy matrix (M-final) involves $e^{i\alpha_-}$ and $\cos\alpha_+$,
$\sin\alpha_+$. With $\alpha_-$ logarithmically divergent:

$$e^{i\alpha_-} = e^{-i\int\Gamma dt}$$

is a pure phase that rotates by an infinite amount as the bounce is
approached. This means the monodromy is not well-defined in the
naive Phase III + Phase I decomposition.

---

## Section 4 — The Regularisation Question

### 4.1 Physical Regularisation

The logarithmic divergence of $\alpha_-$ near the bounce arises because
the cosmological Dirac equation (S1)-(S2) is being applied all the way
to $a \to 0$, where the matter density diverges.

In the physical picture, the condensate melts before the bounce:
$T > T_c$ drives $\eta \to 0$ and consequently $J^0 \to 0$ (since
$J^0$ is the conserved current of the same spinor field). The bilinears
$A^0$ and $P$ are also driven to zero as $\eta \to 0$.

This means the $(A^0, P)$ system **shuts off** before the bounce
is reached, not at it. The logarithmic divergence in $\int dt/a^3$
is cut off by the condensate melting at $T = T_c$, which occurs at
some finite $a = a_c > 0$.

The physical monodromy should therefore be computed over the interval
$[t_c^{\text{pre}}, t_c^{\text{post}}]$ — from the pre-bounce condensation
epoch through the post-bounce condensation epoch — not from bounce to bounce.

### 4.2 The Regulated System

The condensate melts at $T = T_c$, corresponding to scale factor $a_c$
determined by $T_c \sim m_{\text{eff}}/k_B$ and the thermal history.
At $a < a_c$, $\eta = 0$ and $A^0 = P = 0$ (the bilinears vanish with
the condensate).

The effective integration domain for the monodromy is:

$$[a_c, a_{\text{max}}, a_c] \quad
\text{(expansion from } a_c \text{ to } a_{\text{max}} \text{ and back)}$$

In this domain, $a \geq a_c > 0$, and both $\Omega$ and $\Gamma$ are bounded.
The integrals $\alpha_\pm$ are finite.

With the cutoff at $a_c$:

$$\alpha_+ = \int_{a_c\text{ epoch}} \Omega\,dt
\approx 2m \cdot T_{\text{effective}} + \frac{\lambda\eta_0}{a_c^3}
\cdot \delta t_c \tag{alpha-plus-reg}$$

where $T_{\text{effective}}$ is the time spent with $a > a_c$ and
$\delta t_c$ is the time near $a_c$.

$$\alpha_- = -\kappa\alpha\mathcal{J}\int_{a_c\text{ epoch}}\frac{dt}{a^3}
\tag{alpha-minus-reg}$$

Both are now finite. Their values depend on $a_c$, which depends on
$m_{\text{eff}}$ (from the Bi-209 calibration) and the thermal history.

### 4.3 The Monodromy Is Parameter-Dependent

The regulated monodromy matrix is:

$$M_{\text{reg}} = e^{i\alpha_-^{\text{reg}}}
\begin{pmatrix}\cos\alpha_+^{\text{reg}} & i\sin\alpha_+^{\text{reg}} \\
i\sin\alpha_+^{\text{reg}} & \cos\alpha_+^{\text{reg}}\end{pmatrix}$$

Whether $M_{\text{reg}} = -\mathbf{1}$ depends on the numerical values
of $\alpha_+^{\text{reg}}$ and $\alpha_-^{\text{reg}}$, which depend on:

- $m$ (condensate mass parameter, fixed by Bi-209)
- $\lambda$ (quartic coupling, constrained from condensate density)
- $\alpha$ (geometric coupling, fixed by Bi-209)
- $\eta_0$ (initial condensate amplitude, from $a_{\text{max}}$ constraint)
- $\mathcal{J}$ (conserved vector current, an initial condition)
- $a_c$ (condensate melting scale, from $m_{\text{eff}}$ and thermal history)

**The monodromy is not universally $-\mathbf{1}$. It depends on the
action parameters and initial conditions of the cosmological solution.**

---

## Section 5 — What This Means for PT-1

### 5.1 The Result

The monodromy calculation produces the following definite result:

> **The sign of $A^0$ after one cosmological cycle is determined by the
> monodromy matrix $M_{\text{reg}}$, which is a function of the action
> parameters $\{m, \lambda, \alpha, \kappa\}$, the initial conditions
> $\{\eta_0, \mathcal{J}\}$, and the condensate melting scale $a_c$.
> Whether $M_{\text{reg}} = -\mathbf{1}$ (chirality inversion) is not
> a universal consequence of the SCH dynamics. It holds if and only if
> the action parameters satisfy the quantization-like conditions derived
> in Section 2.2.**

This is a significant revision of the PT-1 claim as stated in P.7.7.2.

### 5.2 Three Possible Outcomes

The monodromy matrix $M_{\text{reg}}$ belongs to $U(2)$ (unitary $2\times 2$
matrices, since the system is linear with imaginary coefficients). Its
eigenvalues are $e^{i\Phi_-}$ and $e^{-i\Phi_+}$, both pure phases.

**Outcome A: $M_{\text{reg}} = -\mathbf{1}$** (PT-1 claim confirmed)

Requires the specific parameter conditions of Section 2.2. If the
physical parameters happen to satisfy these conditions, then $A^0$
inverts sign every cycle and the matter/antimatter alternation holds.
This is a fine-tuning unless a principle selects these parameter values.

**Outcome B: $M_{\text{reg}} \neq \pm\mathbf{1}$** (PT-1 claim fails)

$A^0$ rotates in the $(A^0, P)$ plane by an angle that is not a multiple
of $\pi$. The sign of $A^0$ after each cycle depends on the accumulated
rotation angle modulo $2\pi$. After many cycles, $A^0$ cycles through
positive and negative values with a period determined by the rotation angle.
The matter/antimatter alternation holds on average but not strictly
cycle-by-cycle.

**Outcome C: The rotation is ergodic** 

If $\Phi_- / (2\pi)$ and $\Phi_+ / (2\pi)$ are irrational, the
trajectory in $(A^0, P)$ space fills a torus ergodically. The long-run
average of $A^0$ over many cycles is zero. There is no systematic
chirality preference. The matter/antimatter asymmetry averages out.

### 5.3 Which Outcome Is Physically Selected?

Without the Bi-209 calibration fixing $m$ and $\alpha$, and without
the computation of $a_c$, the question cannot be answered numerically.

However, a qualitative argument can be made. In Phase III (late expansion,
$a \gg a_*$), $\Omega \approx 2m$ is approximately constant. The
dominant contribution to $\alpha_+$ is:

$$\alpha_+ \approx 2m \cdot T_{\text{eff}}$$

where $T_{\text{eff}}$ is the effective duration of the condensate epoch.
$T_{\text{eff}} \sim t_{\text{max}} = (\pi/2)a_{\text{max}}$.

The parameter $m$ is estimated at $m \sim m_{\text{eff}} \sim 10^{-6}$ eV
(Paper A Section 6.6a). In natural units, $a_{\text{max}} \sim R_{\text{universe}}
\sim 10^{26}$ m $\sim 10^{60}$ eV$^{-1}$.

$$\alpha_+ \sim 2 \times 10^{-6} \times \frac{\pi}{2} \times 10^{60}
\sim 10^{54} \gg 1$$

The phase $\alpha_+$ is astronomically large. It accumulates $\sim 10^{54}/\pi$
half-cycles during one cosmological epoch. The question of whether
$\alpha_+ = n\pi$ (an integer multiple of $\pi$) reduces to whether
the parameters conspire to make $2m \cdot t_{\text{max}}$ exactly a
multiple of $\pi$.

There is no reason from the action $S_{\text{geo}}$ why this should hold.
The value $\alpha_+ \mod \pi$ is generically nonzero and depends
sensitively on the precise values of $m$ and $a_{\text{max}}$.

**This strongly suggests Outcome B or C is generic, not Outcome A.**

### 5.4 A Reframing That May Rescue the Physical Prediction

The physical prediction of matter/antimatter alternation does not strictly
require $M = -\mathbf{1}$. It requires that the sign of $\langle A^0 \rangle$
— averaged over the condensate epoch of each cycle — alternates between
cycles.

The monodromy $M_{\text{reg}}$ rotates $(A^0, P)$ by some angle $\theta$
per cycle. The time-averaged value of $A^0$ over one cycle is:

$$\langle A^0 \rangle_{\text{cycle}} = A^0(0)\cos(\theta/2)\cos(\theta/2)
+ \ldots$$

*(this needs to be worked out from the rotation structure of M-final)*

A weaker sufficient condition for the physical prediction: if $\theta$ is
close to $\pi$ (i.e., $\alpha_+ \approx (2n-1)\pi$), then $A^0$ spends
approximately half its time positive and half negative within each cycle,
and the net chirality produced by sympathetic nucleation (which requires
$\langle A^0 \rangle \neq 0$ averaged over the matter-creation epoch)
could still be nonzero if the matter-creation epoch is brief compared to
the rotation period.

Whether the matter-creation epoch is brief enough to capture a definite
sign of $A^0$ is a quantitative question requiring:
1. The duration of the $T < T_c$ epoch in units of $1/(2m)$
2. The value of $\theta = \alpha_+$ modulo $\pi$

This brings us back to the Bi-209 calibration as the essential input.

---

## Section 6 — Summary and Revised PT-1 Status

### 6.1 What the Monodromy Calculation Established

| Result | Status |
|--------|--------|
| The $(A^0, P)$ system decouples into normal modes $u = A^0+P$, $v = A^0-P$ | Established |
| Normal modes evolve as $u \to e^{i\Phi_-}u$, $v \to e^{-i\Phi_+}v$ per cycle | Established |
| Monodromy matrix $M_{\text{reg}} = e^{i\alpha_-}\begin{pmatrix}\cos\alpha_+ & i\sin\alpha_+ \\ i\sin\alpha_+ & \cos\alpha_+\end{pmatrix}$ | Derived |
| $M = -\mathbf{1}$ requires $\alpha_+ = n\pi$ AND specific $\alpha_-$ conditions | Established |
| $\alpha_+$ is generically $\sim 10^{54}$ and not constrained to be $n\pi$ | Estimated |
| The naive integral diverges near the bounce; physical cutoff at $a_c$ regulates it | Identified |
| The result depends on $m$, $\alpha$, $\eta_0$, $\mathcal{J}$, $a_c$ | Established |
| $M = -\mathbf{1}$ is not a universal consequence of SCH dynamics | Established |

### 6.2 Revised Statement of the PT-1 Result

**What is established:** The sign of $A^0$ after one cosmological cycle
is governed by the monodromy phase $\alpha_+ = \int_{\text{cycle}}\Omega\,dt
\approx 2m T_{\text{eff}}$. This phase is generically large ($\sim 10^{54}$)
and not constrained to be a multiple of $\pi$ by any principle identified
in the current framework.

**What is not established:** That $A^0 \to -A^0$ per cycle as a universal
or even generic consequence of the SCH dynamics.

**What is open:** Whether the matter-creation epoch is short enough
relative to the rotation period $\pi/\Omega \sim \pi/(2m)$ that the sign
of $A^0$ is approximately constant during nucleation. If so, the chirality
of each cycle's matter content is set by the phase of $A^0$ at the start
of the matter-creation epoch, which depends on the accumulated rotation
from all previous cycles.

**The physical prediction is not ruled out.** The chirality of the current
cycle's matter is some definite value, set by the accumulated rotation
history. Whether it alternates strictly cycle-by-cycle, or follows a
more complex pattern, depends on parameter values not yet determined.

### 6.3 Implications for Appendix P

The entry for Gap 7 / PT-1 in the status table should be updated:

**Current entry:**
> *Chirality inversion across bounce / sympathetic nucleation:
> PREDICTION (proof outstanding). Standard spin representation on $S^3$
> predicts $A^\mu \to -A^\mu$. PT-1 is the formal confirmatory proof target.*

**Revised entry:**
> *Chirality inversion across bounce / sympathetic nucleation:
> OPEN QUESTION — CLAIM REQUIRES REVISION. The local bounce analysis
> (PT-1 v1) shows $A^0$ is continuous through the bounce with no local
> sign flip. The monodromy calculation shows $A^0$ rotates in the $(A^0,P)$
> plane with phase $\alpha_+ \approx 2m T_{\text{eff}} \sim 10^{54}$.
> Whether this produces sign inversion per cycle is not a universal
> consequence of the dynamics and depends on parameter values requiring
> the Bi-209 calibration. The sympathetic nucleation mechanism is not
> ruled out but is not established. Downgraded from PREDICTION to
> OPEN QUESTION pending numerical evaluation of the monodromy phase
> with calibrated parameters.*

### 6.4 What Comes Next

**Immediate:** The Appendix P status table update (Section 6.3 above).
This is a documentation task that can be done now and should be done
before further work builds on PT-1.

**After Bi-209 calibration:** With $m$ and $\alpha$ fixed, compute
$\alpha_+^{\text{reg}}$ and $\alpha_-^{\text{reg}}$ numerically.
Determine whether $\alpha_+ \mod \pi$ is close to $0$ or $\pi$,
and whether the matter-creation epoch is short enough to capture
a definite chirality sign.

**Structural:** The argument that the spin representation on $S^3$
selects $A^\mu \to -A^\mu$ (P.7.7.1) should be examined for what it
actually computes. As the PT-1 problem specification showed, the
spatial antipodal map gives $\psi \to -\psi$ but $A^\mu \to +A^\mu$
(bilinear). The argument in P.7.7.1 contains a gap that the monodromy
calculation has now replaced with a concrete framework.

---

## Section 7 — IVN Items for This Document

| IVN | Content | Priority |
|-----|---------|----------|
| IVN-M1 | Verify algebra for M-matrix derivation | HIGH |
| IVN-M2 | Confirm $\alpha_\pm$ sign conventions in (alpha-plus), (alpha-minus) | HIGH |
| IVN-M3 | Verify $t_{\text{max}} = (\pi/2)a_{\text{max}}$ from CT-ix and that the cycle period is $2t_{\text{max}}$ | MEDIUM |
| IVN-M4 | Estimate $\alpha_+^{\text{reg}}$ numerically with the preliminary $m \sim 10^{-6}$ eV and $R_{\text{universe}} \sim 3R_{\text{Hubble}}$ | MEDIUM |
| IVN-M5 | Derive the time-average of $A^0$ over one rotation at angle $\theta$ | MEDIUM |
| IVN-M6 | Compare duration of matter-creation epoch with rotation period $\pi/(2m)$ | LOW (needs Bi-209) |

---

*SCH PT-1 Monodromy Calculation — v1 | June 2026*
*Not for citation without author approval.*
*Main result: $M = -\mathbf{1}$ is not a universal consequence of SCH
dynamics. The chirality transformation per cycle is governed by a
parameter-dependent phase. Downgrade of PT-1 claim recommended.*
