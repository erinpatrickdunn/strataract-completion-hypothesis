# SCH — CT-ix: Cosmological Dynamics from the Modified Friedmann System
## Working Derivation Document — v2 | June 2026

**Status:** OPEN TARGET → DERIVATION IN PROGRESS

**Revised from v1:** Section P.10.5 (Branch 2 analysis) is corrected following
IVN-I ("PT-1 Monodromy in the $(+,-,-,-)$ Convention," June 2026, incorporated
into Appendix P v13 Section P.7.7.3). The v1 Branch 2 system (Lemma P.10.5.1,
equations E2/E3) mixed metric-signature conventions in the same way the original
Appendix P v12 PT-1 calculation did. The corrected, convention-consistent
system is real rather than complex, drops the Hubble-friction term v1 carried
in the $(A^0,P)$ sector, and — most importantly — shows that $\eta$ is sourced
by $\kappa\alpha A^0 P$ in Branch 2 and does not dilute purely as $a^{-3}$,
contradicting the v1 assumption flagged (but not resolved) at P.10.5.2's
original IVN marker. This directly resolves OQ-CT-ix-3 in the sense of
confirming the effect is real; its quantitative size remains open pending
IVN-I-3 (CRITICAL, unresolved). Branch 1 (Sections P.10.1–P.10.4) is
**unaffected** — its derivation used only the $A^0=0$ reduction, which is
identical in both the old and corrected conventions. All Appendix P version
pointers below are updated from v11 to v13 (Section P.9 / CT-viii itself did
not change between those versions). See the boxed caveats in Section P.10.5
and the updated status tables in P.10.6 and P.10.9 for the full accounting.

**Prerequisite satisfied:** CT-viii (FLRW Reduction, Appendix P v13 Section P.9 — unchanged since v11)

**Prerequisite for:** PT-1 (chirality inversion — see Appendix P v13 P.7.7.3 for
the corrected calculation), CT-xix (antipodal condensate coupling),
quantitative bounce cosmology predictions, $R_{\text{universe}}$ constraint

**Verification status:** All steps in this document require independent verification.
Steps marked *(IVN)* are particularly sensitive to sign conventions or
integration constants and should be prioritised. Steps marked *(IVN-I)* refer
to the seven verification items opened by the v2 Branch 2 correction (see
Appendix P v13 Section P.7.7.9); IVN-I-3 is CRITICAL and gates Section P.10.5.

**Methodological principle (carried from CT-viii):** Carry all mathematically
allowed branches until the equations eliminate them. Do not impose simplifying
assumptions as starting points.

---

## Preamble: What CT-ix Must Deliver

CT-viii delivered the field equations on the $S^3 \times \mathbb{R}$ background:

- First Friedmann equation (Hamiltonian constraint)
- Raychaudhuri equation
- Cosmological Dirac equation governing $\psi(t)$
- Conservation law $a^3 J^0 = \mathcal{J}$
- Two-branch cosmological structure (torsion-free / torsion-active)
- Bounce existence condition and regularity

CT-viii did not deliver:

- The solution structure of the coupled ODE system
- The asymptotic behaviour in each cosmological phase
- The characteristic scales ($R_{\text{universe}}$, $\eta_{\text{bounce}}$, $a_{\text{bounce}}$) as functions of action parameters
- The connection between condensate evolution and observable $c(t) = \omega(t) R_{\text{cosmic}}(t)$
- A classification of cosmological fixed points and their stability
- The perturbative expansion around the matter-dominated epoch

CT-ix provides all of the above in Branch 1 (torsion-free) fully, and in Branch 2
(torsion-active) at the level of structure and fixed-point classification. Branch 2
quantitative solutions require PT-1 to establish which branch is physical before
full development is warranted.

---

## P.10.0 — Notation and Starting Equations

The starting system is taken directly from Appendix P v13 Section P.9.5
(unchanged from v11 — CT-viii itself was not touched by the v13 revision), with
$\rho_{\text{matter}} = 0$ for the condensate-only cosmology. Matter is reintroduced
in Section P.10.7.

**Modified First Friedmann Equation:**

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\left(m\eta + \frac{\lambda}{4}\eta^2
+ \frac{\kappa\alpha}{4}(A^0)^2\right) \tag{F1}$$

**Raychaudhuri Equation:**

$$\frac{\ddot{a}}{a} = -\frac{\kappa}{6}\left(-2m\eta - \frac{\lambda}{2}\eta^2
+ \kappa\alpha(A^0)^2\right) \tag{F2}$$

**Cosmological Dirac Equation:**

$$i\gamma^0\dot{\psi} = \frac{3H}{2}\gamma^0\psi + m\psi + \frac{\lambda}{2}\eta\psi
+ \frac{\kappa\alpha}{2}A^0\gamma^0\gamma^5\psi \tag{D}$$

**Conservation Law:**

$$a^3 J^0 = \mathcal{J} = \text{const} \tag{C}$$

**Branch conditions (from P.9.6.1):**

- Branch 1: $A^0 = 0$ throughout. Consistent with parity-preserving vacuum.
- Branch 2: $A^0 \neq 0$. Dynamically determined by (D).

**Notation:** $\kappa = 8\pi G/c^4$, $H = \dot{a}/a$, overdot = $d/dt$.

---

## P.10.1 — Branch 1 Analysis: Torsion-Free Cosmology

### P.10.1.1 — Reduction of the System

In Branch 1, $A^0 = 0$ identically. The Dirac equation (D) reduces to:

$$i\gamma^0\dot{\psi} = \frac{3H}{2}\gamma^0\psi + m\psi + \frac{\lambda}{2}\eta\psi \tag{D1}$$

The system (F1), (F2) becomes:

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\left(m\eta + \frac{\lambda}{4}\eta^2\right) \tag{F1a}$$

$$\frac{\ddot{a}}{a} = \frac{\kappa}{6}\left(2m\eta + \frac{\lambda}{2}\eta^2\right) \tag{F2a}$$

Note the sign in (F2a): $\ddot{a}/a > 0$ when $\eta > 0$. The condensate drives
accelerated expansion, not deceleration. This is the bounce mechanism operating
in the pre-bounce (collapsing) and post-bounce (expanding) phases.

### P.10.1.2 — The $\eta$ Equation from the Dirac Equation

To extract a scalar evolution equation for $\eta = \bar{\psi}\psi$, differentiate
with respect to $t$ and use (D1):

$$\dot{\eta} = \frac{d}{dt}(\bar{\psi}\psi) = \dot{\bar{\psi}}\psi + \bar{\psi}\dot{\psi}$$

From (D1):

$$\dot{\psi} = -i\gamma^0\left(\frac{3H}{2}\gamma^0\psi + m\psi
+ \frac{\lambda}{2}\eta\psi\right)$$

$$= -i\left(\frac{3H}{2}\psi - im\gamma^0\psi - i\frac{\lambda}{2}\eta\gamma^0\psi\right)$$

using $(\gamma^0)^2 = -\mathbf{1}$ in the $(-,+,+,+)$ metric signature. *(IVN: confirm
$(\gamma^0)^2$ sign in the convention used throughout.)*

Taking $\bar{\psi}(\cdot)$ and $(\cdot)\psi$ contractions and using the Dirac
representation bilinear structure:

$$\dot{\eta} = -3H\,\frac{\bar{\psi}\gamma^0\psi}{2} \cdot (\text{factor}) -
2m\,\text{Im}(\bar{\psi}\gamma^0\psi) \cdot \ldots$$

**This approach is algebraically unwieldy via direct differentiation. The cleaner
route is through the spinor equation of motion projected onto bilinears, which
yields the $\eta$ evolution equation directly.**

**Lemma P.10.1.2 (η evolution in Branch 1):**

From the Dirac equation (D1) and its conjugate, contracting with $\bar{\psi}$ and
$\psi$ respectively and combining:

$$\dot{\eta} + 3H\eta = 0 \tag{E1}$$

**Derivation:** The kinetic term $\frac{3H}{2}\gamma^0$ contributes a dilution factor
when contracted to form the scalar bilinear. The mass and quartic terms contribute
to $\bar{\psi}\psi = \eta$ but, being proportional to $\eta$ itself, do not alter
the dilution structure. The full contraction yields (E1). *(IVN: complete this
contraction explicitly, tracking every term in (D1).)*

**Immediate consequence of (E1):**

$$\eta(t) = \frac{\eta_0}{a(t)^3} \tag{E1-sol}$$

The condensate density dilutes as $a^{-3}$, exactly as pressureless dust.
This is not an accident: in Branch 1, the condensate scalar behaves as cold matter
from the perspective of its dilution law, even though its equation of state
$w = p/\rho = -1$ (cosmological constant character) differs. The two effects are
consistent: $\eta$ itself dilutes as $a^{-3}$, but each unit of $\eta$ sources
gravitational energy proportional to $m + (\lambda/4)\eta$, the latter of which
also dilutes. The combined sourcing is not simple dust.

### P.10.1.3 — Substitution into the First Friedmann Equation

Using (E1-sol) in (F1a):

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\left(\frac{m\eta_0}{a^3}
+ \frac{\lambda\eta_0^2}{4a^6}\right) \tag{F1b}$$

This is the modified Friedmann equation in Branch 1 as an explicit equation for
$a(t)$ alone. It has two source terms:

- **Term A:** $\frac{\kappa m \eta_0}{3} a^{-3}$ — scales as dust ($w=0$ from
  the perspective of $H^2$ sourcing).
- **Term B:** $\frac{\kappa\lambda\eta_0^2}{12} a^{-6}$ — scales as stiff
  radiation ($w=1$), or more precisely as the square of dust density.

Term B dominates at small $a$ (near the bounce). Term A dominates at large $a$
(in the expanding phase).

### P.10.1.4 — Phase Structure in Branch 1

Define the characteristic scale factors:

$$a_* \equiv \left(\frac{\lambda\eta_0}{4m}\right)^{1/3} \tag{scales}$$

At $a \ll a_*$: Term B $\gg$ Term A. The modified Friedmann equation becomes:

$$H^2 \approx \frac{\kappa\lambda\eta_0^2}{12}\,a^{-6} - \frac{1}{a^2}$$

At $a \gg a_*$: Term A $\gg$ Term B. The equation becomes:

$$H^2 \approx \frac{\kappa m\eta_0}{3}\,a^{-3} - \frac{1}{a^2}$$

which is the standard dust Friedmann equation on $S^3$. This is the GR recovery
at late times, now with an explicit scale $a_*$ at which the recovery becomes
operative.

**The three cosmological phases in Branch 1:**

| Phase | $a$ regime | Dominant source | $H^2$ scaling | Character |
|-------|------------|-----------------|---------------|-----------|
| I: Pre-bounce (condensate-dominated) | $a \ll a_*$ | Term B ($\lambda\eta^2$) | $a^{-6}$ | Stiff-condensate |
| II: Transition | $a \sim a_*$ | Both terms | mixed | $a_*$ is the transition scale |
| III: Late expansion | $a \gg a_*$ | Term A ($m\eta$) | $a^{-3}$ | Dust-like condensate |

### P.10.1.5 — The Bounce in Branch 1

The bounce occurs at $H = 0$, $\dot{a} = 0$. From (F1b):

$$\frac{1}{a_{\text{b}}^2} = \frac{\kappa m\eta_0}{3}\,a_{\text{b}}^{-3}
+ \frac{\kappa\lambda\eta_0^2}{12}\,a_{\text{b}}^{-6}$$

This is a quadratic in $a_{\text{b}}^{-3}$. Define $u \equiv a_{\text{b}}^{-3}$:

$$\frac{\kappa\lambda\eta_0^2}{12}\,u^2 + \frac{\kappa m\eta_0}{3}\,u - \frac{1}{a_{\text{b}}^2} = 0$$

*(IVN: note that $a_{\text{b}}$ appears on both sides — this equation implicitly
defines $a_{\text{b}}$ through $u = a_{\text{b}}^{-3}$; the $1/a_{\text{b}}^2$ term
is $u^{2/3}$. Rewrite as:)*

$$\frac{\kappa\lambda\eta_0^2}{12}\,u^2 + \frac{\kappa m\eta_0}{3}\,u
= u^{2/3} \tag{bounce-eq}$$

This is a transcendental equation in $u$. Two limits:

**Small-$\eta_0$ limit (Term A dominates):**

$$a_{\text{b}}^{\text{(A)}} = \frac{\kappa m\eta_0}{3} \tag{bounce-A}$$

**Large-$\eta_0$ limit (Term B dominates):**

$$a_{\text{b}}^{\text{(B)}} = \left(\frac{\kappa\lambda\eta_0^2}{12}\right)^{1/4}
\tag{bounce-B}$$

In both limits, $a_{\text{b}} > 0$. The bounce is non-singular.

The result from CT-viii (Appendix P v13, P.9.6.2 — unchanged from v11) stated:

$$\eta_{\text{bounce}} \approx \sqrt{\frac{12}{\kappa\lambda}}\,\frac{1}{a_{\text{bounce}}}$$

This is the high-condensate-density limit of (bounce-eq), consistent with
Term B dominance. *(IVN: verify consistency of (bounce-B) with the CT-viii result
by substituting $\eta = \eta_0/a^3$ at $a = a_{\text{b}}$.)*

### P.10.1.6 — The Expanding Phase and $R_{\text{universe}}$

In Phase III ($a \gg a_*$), the system approaches standard dust cosmology on $S^3$:

$$H^2 + \frac{1}{a^2} \approx \frac{\kappa m\eta_0}{3}\,a^{-3}$$

This is exactly the Friedmann equation for dust on a closed universe with
energy parameter $\Omega_{\text{dust}} = \frac{\kappa m\eta_0}{3H^2 a^3}$.
The universe reaches a maximum radius $a_{\text{max}}$ when $H = 0$ again
(the turnaround of the current expansion cycle):

$$\frac{1}{a_{\text{max}}} = \frac{\kappa m\eta_0}{3}\,a_{\text{max}}^{-3}$$

$$a_{\text{max}}^2 = \frac{\kappa m\eta_0}{3} \tag{amax}$$

The maximum radius of the $S^3$ is:

$$R_{\text{universe}} = a_{\text{max}} \cdot R_{\text{unit}}$$

where $R_{\text{unit}}$ is the radius of the unit $S^3$ in the coordinate system
of Section P.9.1. The observable $R_{\text{universe}}$ is therefore:

$$R_{\text{universe}}^2 = \frac{\kappa m\eta_0}{3}\,R_{\text{unit}}^2 \tag{Runiv}$$

This is the leading-order derivation of $R_{\text{universe}}$ from action parameters.
It is conditional on Phase III being the appropriate regime for the current
cosmological epoch (i.e., $a_{\text{current}} \gg a_*$) and on the matter sector
$\rho_{\text{matter}}$ being subdominant to the condensate term at turnaround.

**Interpretation:** $R_{\text{universe}}$ is set by the product $m\eta_0$ — the
condensate mass parameter times the initial condensate amplitude. Neither alone
determines the universe's size; the product does. This product is constrained by
the CMB quadrupole suppression (requiring $R_{\text{universe}} \geq 3R_{\text{Hubble}}$,
from Appendix P Section P.7.6.4) and independently by the Bi-209 calibration
(which pins $m$ and $m_{\text{eff}}$, from which $\eta_0$ can be inferred via
the condensate equilibrium condition $\eta_{\text{eq}} = m^2/\lambda$).

**Note on the derivation brief's CT-ix scope:** The development brief designated
CT-ix as "$R_{\text{universe}}$ derivation." Equation (Runiv) delivers this
at leading order. The full derivation including matter sector and the complete
Phase III dynamics is in Section P.10.7 below.

---

## P.10.2 — Branch 1 Fixed-Point Analysis

### P.10.2.1 — The Autonomous System

Define the dimensionless variables:

$$x \equiv \sqrt{\frac{\kappa\lambda\eta_0^2}{12}}\,a^{-3}, \qquad
y \equiv \sqrt{\frac{\kappa m\eta_0}{3}}\,a^{-3/2}, \qquad
s \equiv \frac{1}{a}$$

The Friedmann equation (F1b) becomes:

$$H^2 = x^2 + y^2 - s^2 \tag{F1c}$$

The time derivatives of $(x, y, s)$ are determined by $\dot{a} = aH$:

$$\dot{x} = -3Hx, \qquad \dot{y} = -\frac{3}{2}Hy, \qquad \dot{s} = -Hs$$

**Fixed points** (where $H = 0$, $\dot{H} = 0$):

The only fixed point with $a$ finite and $\eta > 0$ is the bounce: $H = 0$,
$a = a_{\text{b}}$, corresponding to the maximum of the Friedmann constraint
surface in phase space. At the bounce, the system momentarily stalls and
reverses direction of $\dot{a}$.

The expanding phase has no finite fixed point in the condensate-only system:
$a$ grows until the curvature term $-1/a^2$ dominates and the expansion halts
at $a_{\text{max}}$.

**Stability of the bounce:** The bounce is a saddle point in the $(a, \dot{a})$
phase plane — it is attracting in the $\dot{a}$ direction (collapsing phase
approaches it) and repelling in the $a$ direction (expanding phase departs from
it). This is the correct behaviour for a regular turnaround. *(IVN: confirm
the Jacobian eigenvalues at the bounce from (F1b) and (F2a).)*

### P.10.2.2 — The de Sitter Attractor

In Phase III at late times, if $m > 0$ and $\eta$ dilutes as $a^{-3}$, the
source in (F1a) dies away and the system asymptotes toward $H^2 \to -1/a^2$,
which has no real solution — the expansion halts.

This is the closed-universe turnaround: the $S^3$ reaches $a_{\text{max}}$
and begins recollapsing. The recollapse is symmetric to the expansion phase
in the torsion-free branch.

There is no de Sitter attractor in the condensate-only Branch 1 system. A
cosmological constant term would be required to produce late-time acceleration,
and no such term appears in $S_{\text{geo}}$ independently of $\eta$.

**However:** If the condensate at late times has $\eta \to \eta_{\text{eq}} \neq 0$
(equilibrium value rather than diluting freely), the effective energy density
has a floor and the system does approach a de Sitter-like attractor. This requires
the matter sector to maintain $\eta_{\text{eq}}$ against dilution, which is the
recoherence mechanism of Paper A Section 2.4a. Full treatment requires
$\Gamma_{\text{recoh}} > 0$, deferred to Section P.10.7.

---

## P.10.3 — Branch 1: Analytic Solutions in Limiting Regimes

### P.10.3.1 — Phase I: Stiff-Condensate Regime ($a \ll a_*$)

Dropping Term A and the curvature term (valid at small $a$):

$$H^2 \approx \frac{\kappa\lambda\eta_0^2}{12}\,a^{-6}$$

$$\dot{a} \approx \pm\sqrt{\frac{\kappa\lambda\eta_0^2}{12}}\,a^{-2}$$

Separating variables and integrating:

$$\int a^2\,da = \pm\sqrt{\frac{\kappa\lambda\eta_0^2}{12}}\,\int dt$$

$$\frac{a^3}{3} = \pm\sqrt{\frac{\kappa\lambda\eta_0^2}{12}}\,(t - t_{\text{b}})$$

$$\boxed{a(t) = \left(3\sqrt{\frac{\kappa\lambda\eta_0^2}{12}}\right)^{1/3}
|t - t_{\text{b}}|^{1/3}} \tag{sol-I}$$

The scale factor grows as $|t - t_{\text{b}}|^{1/3}$ near the bounce.
The Hubble rate:

$$H = \frac{\dot{a}}{a} = \frac{1}{3(t - t_{\text{b}})}$$

This is the $a \propto t^{1/3}$ solution characteristic of a stiff-fluid
dominated cosmology. *(IVN: verify by substituting (sol-I) back into F1b
and checking both sides match in the Phase I limit.)*

### P.10.3.2 — Phase III: Dust-Condensate Regime ($a \gg a_*$)

Dropping Term B:

$$H^2 + \frac{1}{a^2} \approx \frac{\kappa m\eta_0}{3}\,a^{-3}$$

This is the standard closed dust Friedmann equation. The parametric solution
(standard cosmology result, included here for completeness and to establish
notation for downstream use):

$$a(\phi) = \frac{a_{\text{max}}}{2}(1 - \cos\phi), \qquad
t(\phi) = \frac{t_{\text{max}}}{\pi}\left(\phi - \sin\phi\right) \tag{sol-III}$$

where $\phi \in [0, 2\pi]$ is the development parameter, $\phi = 0$ at the
bounce (minimum $a$, but in Phase III we are identifying the transition from
Phase I as an effective initial condition), and $\phi = \pi$ at maximum expansion.

The maximum expansion radius:

$$a_{\text{max}} = \frac{\kappa m\eta_0}{3} \tag{amax-explicit}$$

The time to maximum expansion:

$$t_{\text{max}} = \frac{\pi}{2}\sqrt{\frac{a_{\text{max}}^3}{\kappa m\eta_0/3}}
= \frac{\pi}{2}\,a_{\text{max}} \tag{tmax}$$

*(IVN: verify (tmax) by substituting (sol-III) into the Phase III Friedmann
equation.)*

The Hubble time at the current epoch is $H_0^{-1}$. The requirement
$R_{\text{universe}} \geq 3R_{\text{Hubble}}$ translates to:

$$a_{\text{max}} \geq 3/H_0 \tag{constraint-amax}$$

From (amax-explicit):

$$m\eta_0 \geq \frac{9}{\kappa H_0^2} = \frac{9H_0^2}{8\pi G H_0^2 / c^4}
= \frac{9c^4}{8\pi G} \tag{constraint-meta0}$$

This is the CMB quadrupole suppression constraint expressed as a bound
on the product $m\eta_0$. It is a prediction of the framework once $m$
is fixed by the Bi-209 calibration, determining $\eta_0$.

---

## P.10.4 — Branch 1: The Full Cycle

The Branch 1 cosmology describes a closed cycle:

$$\underbrace{\text{Collapse}}_{\dot{a}<0,\, a \to a_{\text{b}}}
\;\xrightarrow{\text{bounce}}\;
\underbrace{\text{Phase I expansion}}_{\dot{a}>0,\, a \propto t^{1/3}}
\;\xrightarrow{a \sim a_*}\;
\underbrace{\text{Phase III expansion}}_{\dot{a}>0,\, a \to a_{\text{max}}}
\;\xrightarrow{\text{turnaround}}\;
\underbrace{\text{Recollapse}}_{\dot{a}<0}$$

The cycle is symmetric under time reversal about the bounce (assuming
symmetric initial conditions and ignoring entropy production, which is
addressed in CT-xx).

**The current epoch** sits in Phase III, somewhere between $a_*$ and $a_{\text{max}}$.
The observational constraints on $H_0$, $\Omega_k$, and the CMB quadrupole
suppression together constrain the position within this phase.

**Relation to $c(t) = \omega(t) R_{\text{cosmic}}(t)$ (Theorem 5):**

In the Phase III parametric solution (sol-III), $R_{\text{cosmic}}(t) = a(\phi)R_{\text{unit}}$.
The angular frequency $\omega(t)$ satisfies:

$$c = \omega(t)\,a(t)\,R_{\text{unit}} = \dot{\phi}(t)\,a(t)\,R_{\text{unit}}$$

where $\dot{\phi}$ is the rate of change of the development parameter.
From (sol-III):

$$\dot{\phi} = \frac{\pi}{t_{\text{max}}} \cdot \frac{1}{1 - \cos\phi}
\cdot \frac{1}{\sin\phi} \cdot \frac{a_{\text{max}}}{2}\sin\phi
= \frac{\pi}{t_{\text{max}}} \cdot \frac{a_{\text{max}}/2}{a(\phi)}$$

*(IVN: this derivation needs to be completed from the full (sol-III) time derivative.)*

The key qualitative result is that $\omega(t)$ is not constant — it varies with the
cosmological development parameter. $c(t) = \omega(t) R_{\text{cosmic}}(t)$ is
therefore a dynamical quantity, consistent with the physical picture of
Paper A Section 0.3, but approximately constant on timescales short compared to
$t_{\text{max}}$ — which is why local experiments measure a constant $c$.

---

## P.10.5 — Branch 2 Analysis: Torsion-Active Cosmology

> **⚠️ SUPERSEDED IN v2.** The derivation in this section (P.10.5.1–P.10.5.4)
> was written using a $(A^0,P)$ bilinear system that, per IVN-I (June 2026),
> mixed metric-signature conventions in the same way as the original Appendix
> P v12 PT-1 calculation. Section P.10.5.1's Lemma is retained below for the
> historical record and because its *qualitative* oscillator picture is
> structurally similar to the corrected one, but its specific equations (E2),
> (E3) should not be used for quantitative work. **Use the corrected system
> from Appendix P v13 Section P.7.7.3 instead** — reproduced in the new
> Section P.10.5.0a immediately below. The most consequential change is that
> the corrected system shows $\eta$ is *not* independent of the chirality
> sector in Branch 2 (Section P.10.5.2 flagged this as an open verification
> item in v1 and did not resolve it in either direction; IVN-I now resolves it
> in the negative — the independence assumption is false). Sections
> P.10.5.2–P.10.5.4 are annotated with caveats below rather than fully
> rewritten, since a complete Branch 2 re-derivation using the corrected
> system is a substantial undertaking properly scoped as its own follow-on
> document once IVN-I-3 is closed.

### P.10.5.0a — The Corrected $(A^0,\eta,P)$ System (from Appendix P v13 P.7.7.3)

For reference, the corrected, convention-consistent bilinear system is:

$$\dot{\eta} + 3H\eta = \kappa\alpha A^0 P \tag{E1-new}$$

$$\dot{A}^0 = -(2m + \lambda\eta)\,P \tag{E-A-new}$$

$$\dot{P} = \left(2m + (\lambda - \kappa\alpha)\eta\right) A^0 \tag{E-P-new}$$

$$\dot{J}^0 + 3H J^0 = 0 \quad \text{(tentative — see IVN-I-4, IVN-I-5)} \tag{E-J-new}$$

All four are real, with no Hubble-friction term in the $(A^0,P)$ sector
(unlike v1's E2/E3 below, which carried a $3H$ friction term inherited from
the mixed-convention derivation). Defining $\Omega_1 \equiv 2m+\lambda\eta$,
$\Omega_2 \equiv 2m+(\lambda-\kappa\alpha)\eta$, the $(A^0,P)$ pair oscillates
with adiabatic phase $\Phi_{\text{cycle}} = \int\sqrt{\Omega_1\Omega_2}\,dt$,
replacing this document's $\alpha_+ = \int \Omega_{\text{mix}}\,dt$ below
wherever it appears. See Appendix P v13 P.7.7.3 for the full derivation and
the corrected monodromy matrix $M_{\text{correct}}$.

### P.10.5.1 — The Additional Equation *(historical — see caveat above)*

In Branch 2, $A^0 \neq 0$. The Dirac equation (D) contains the additional term:

$$\frac{\kappa\alpha}{2}A^0\,\gamma^0\gamma^5\psi$$

This term couples $\eta$ and $A^0$ through the spinor equation of motion.
An evolution equation for $A^0$ must be derived analogously to the $\eta$
equation in Branch 1.

**Lemma P.10.5.1 (A⁰ evolution in Branch 2):**

From (D) and its conjugate, contracting to form the axial bilinear:

$$\dot{A}^0 + 3H\,A^0 = -2m\,P - \lambda\eta\,P \tag{E2}$$

where $P = \bar{\psi}\gamma^5\psi$ is the pseudoscalar bilinear.

*(IVN: derive (E2) explicitly from (D). The pseudoscalar $P$ is a new bilinear
that was zero in the parity-preserving vacuum of Branch 1. In Branch 2 it
may be nonzero. Determine the $P$ evolution equation from (D) to close the system.)*

**Closure issue:** The system (E1), (E2) involves $\eta$, $A^0$, and $P$. A third
equation for $P$ is needed. From the Dirac equation, contracting with $\bar{\psi}\gamma^5$:

$$\dot{P} + 3HP = 2m\,A^0 + \lambda\eta\,A^0 \tag{E3}$$

*(IVN: verify (E3).)*

The system (E1), (E2), (E3) is closed. It has the structure of coupled harmonic
oscillators in the $(\eta, A^0, P)$ space, with $a(t)$ providing the time-varying
environment. The coupling strength is set by $m$ and $\lambda\eta$.

### P.10.5.2 — The $\eta$-$A^0$ Coupling Structure *(historical — assumption resolved false by IVN-I)*

> **RESOLUTION (v2):** The IVN item below, left open in v1, is now resolved —
> in the negative. IVN-I's corrected system (P.10.5.0a, equation E1-new) shows
> $\dot\eta + 3H\eta = \kappa\alpha A^0 P \neq 0$ in Branch 2. The assumption
> that $\eta = \eta_0/a^3$ holds "regardless of $A^0$" is **false** whenever
> $A^0$ and $P$ are simultaneously nonzero, which is generically the case in
> Branch 2. This was OQ-CT-ix-3 (Section P.10.9.2) under a different name; it
> is now confirmed qualitatively, with quantitative size pending IVN-I-3
> (CRITICAL). Everything from "Assuming $\eta$-dilution is unmodified..."
> onward in this subsection, including (E2b), (E3b), and $\Omega_{\text{mix}}$,
> should be read as the superseded v1 approximation, not as a validated
> result. The corrected replacement quantities are $\Omega_1,\Omega_2$ from
> P.10.5.0a.

From (E1): $\eta = \eta_0 / a^3$ (same dilution as Branch 1, this is exact
regardless of $A^0$ because $\eta$-evolution involves only $H$ at leading order
before the $A^0$ coupling enters).

*(IVN: confirm this claim by checking whether the $A^0$ terms in (D) contribute
to $\dot{\eta}$ or only to $\dot{A}^0$ and $\dot{P}$. — **RESOLVED in v2, see
box above: the claim is false.**)*

Assuming $\eta$-dilution is unmodified by the $A^0$ terms, the $A^0$-$P$ system
becomes:

$$\dot{A}^0 + 3HA^0 = -(2m + \lambda\eta_0/a^3)\,P \tag{E2b}$$

$$\dot{P} + 3HP = (2m + \lambda\eta_0/a^3)\,A^0 \tag{E3b}$$

Define $\Omega_{\text{mix}}(t) \equiv 2m + \lambda\eta_0/a^3$. This is a
time-varying oscillation frequency. The system (E2b), (E3b) describes
oscillating mixing between $A^0$ and $P$ at frequency $\Omega_{\text{mix}}$,
damped by the Hubble friction term $3H$.

### P.10.5.3 — Late-Time Behaviour in Branch 2 *(historical — conclusion now provisional)*

> **CAVEAT (v2):** This subsection's asymptotes-to-Branch-1 conclusion rests
> on (E2b)/(E3b), which are superseded (P.10.5.2 box). The corrected system
> has no Hubble-friction term and $\Omega_1 \neq \Omega_2$; whether $(A^0)^2$
> still decays as $a^{-3}$ at late times under the corrected system, and
> whether the $\kappa\alpha A^0 P$ source keeps $\eta$ from diluting to zero
> as fast as assumed, are both open (IVN-I-3, IVN-I-6 in Appendix P v13
> P.7.7.9). The qualitative expectation that Branch 2 approaches Branch 1
> once $\eta \to 0$ is still plausible — a vanishing $\eta$ shuts off the new
> source term $\kappa\alpha A^0 P$ only if $A^0$ or $P$ also vanish, which is
> not obviously guaranteed — but this is now an open question rather than an
> establishing argument. Treat everything below as the v1 approximation.

At late times ($a \to \infty$, $\eta \to 0$):

$$\Omega_{\text{mix}} \to 2m = \text{const}$$

The $(A^0, P)$ system becomes:

$$\ddot{A}^0 + 3H\dot{A}^0 + (4m^2 + 9H^2/4)\,A^0 = 0 \tag{osc}$$

*(IVN: derive (osc) by differentiating (E2b) and substituting (E3b). — this
IVN item is now superseded; (E2b)/(E3b) themselves need re-derivation from
the corrected system before (osc) is trustworthy.)*

This is a damped oscillator equation. The oscillation frequency is $2m$ and
the damping is from Hubble friction $3H/2$. For $m \gg H$ (condensate mass
much larger than the Hubble rate, which holds generically since $m \sim 10^{-6}$
eV and $H_0 \sim 10^{-33}$ eV), the oscillation is underdamped.

At late times, $A^0$ oscillates at frequency $2m$ with amplitude decaying as
$a^{-3/2}$. The time-averaged $\langle (A^0)^2 \rangle$ decays as $a^{-3}$,
which sources an effective stiff-fluid contribution to (F1) that also dilutes.

**Consequence:** In Branch 2, the torsion-induced source term $\frac{\kappa\alpha}{4}(A^0)^2$
in (F1) oscillates and decays. The Branch 2 cosmology asymptotes toward the Branch 1
behavior at late times. The distinction between branches is most significant near
the bounce where $A^0$ is large. **(v2: this consequence paragraph is the
provisional v1 conclusion flagged above — not re-derived under the corrected
system.)**

### P.10.5.4 — The Modified Bounce Condition in Branch 2 *(historical — scaling argument likely survives, not yet reverified)*

> **CAVEAT (v2):** The bounce-existence inequality itself,
> $\frac{\lambda}{2}\eta^2+2m\eta>\kappa\alpha(A^0)^2$, is a CT-viii (P.9.6.2)
> result and is unaffected by IVN-I. What follows below — the specific claim
> that $(A^0_{\text{b}})^2 \sim a_{\text{b}}^{-3}$ near the bounce — used the
> superseded (E2b)/(E3b) oscillation-amplitude scaling. The power-counting
> argument (amplitude $\sim a^{-3/2}$ from an adiabatic oscillator with slowly
> varying frequency and $3H$ damping) may well survive under the corrected,
> frictionless system with a different but still power-law amplitude scaling
> — an undamped adiabatic oscillator's amplitude is set by the adiabatic
> invariant rather than by explicit Hubble friction, which typically gives a
> comparable but not necessarily identical scaling. This has not been
> reverified. The qualitative conclusion (bounce occurs generically in Branch
> 2, scalar condensate dominates near the bounce) is plausible on general
> grounds — $\eta_0/a_{\text{b}}^3$ diverges faster than any power-law-bounded
> $A^0$ amplitude as $a_{\text{b}}\to 0$ — but should be treated as
> provisional rather than established until redone with the corrected system.

From CT-viii (P.9.6.2), the bounce requires:

$$\frac{\lambda}{2}\eta^2 + 2m\eta > \kappa\alpha(A^0)^2$$

Substituting $\eta = \eta_0/a_{\text{b}}^3$:

$$\frac{\lambda\eta_0^2}{2a_{\text{b}}^6} + \frac{2m\eta_0}{a_{\text{b}}^3}
> \kappa\alpha(A^0_{\text{b}})^2 \tag{bounce-B2}$$

where $A^0_{\text{b}}$ is the value of $A^0$ at the bounce. Whether this condition
is satisfied depends on the amplitude of $A^0$ at the bounce, which is set by
the evolution from the pre-bounce initial conditions through the (E2b)-(E3b) system
**(v2: superseded — see corrected system, P.10.5.0a)**.

At the Planck-density bounce, $a_{\text{b}}$ is microscopically small and
$\eta_0/a_{\text{b}}^3$ is extremely large. The left side of (bounce-B2) grows
as $a_{\text{b}}^{-6}$, while $A^0$ is bounded by the oscillatory decay amplitude
which scales as $a_{\text{b}}^{-3/2}$, so $(A^0_{\text{b}})^2 \sim a_{\text{b}}^{-3}$.
The ratio is:

$$\frac{\kappa\alpha(A^0_{\text{b}})^2}{\lambda\eta_0^2/(2a_{\text{b}}^6)}
\sim a_{\text{b}}^3 \to 0 \text{ as } a_{\text{b}} \to 0$$

The bounce condition is satisfied generically in the small-$a_{\text{b}}$ limit,
confirming the CT-viii result that the bounce occurs in Branch 2 as well,
with the scalar condensate dominating over the torsion term at the bounce point.
**(v2: this numerical scaling argument should be rerun against the corrected
system before being cited as more than plausible; see caveat above.)**

---

## P.10.6 — Fixed Points, Stability, and Attractors: Summary

> **CAVEAT (v2):** The Branch 2 column below is carried from the superseded
> v1 derivation (Section P.10.5, historical). It should be read as "what v1
> argued," not as an established result. Branch 1 is unaffected.

| Phase | Branch 1 | Branch 2 (v1 argument — provisional, see caveat) |
|-------|----------|----------|
| Near bounce | Stiff-condensate: $a \propto t^{1/3}$ | Modified by $A^0$ oscillations; same asymptotic if $A^0$ amplitude bounded |
| Transition | $a \sim a_*$: Term A dominates | $\Omega_{\text{mix}}$ transitions from $\lambda\eta$-dominated to $2m$-dominated |
| Late expansion | Dust-condensate: closed universe | Asymptotes to Branch 1 (torsion dilutes) — **not yet reverified under the corrected $\eta$-sourcing (IVN-I-3)** |
| Maximum expansion | $a = a_{\text{max}} = \kappa m\eta_0/3$ | Modified $a_{\text{max}}$ if $A^0$ non-negligible at turnaround |
| Recollapse | Symmetric to expansion | Symmetric, with decaying $A^0$ oscillation amplitude (v1 argument) |

**The attractor structure:** Both branches have the same late-time attractor —
the standard closed dust cosmology. The condensate terms decay. The torsion
term decays faster (as $a^{-3}$ in amplitude vs $a^{-3}$ for the scalar condensate,
but the torsion energy as $a^{-6}$ in energy density vs. $a^{-3}$ for the scalar).
Branch 2 flows toward Branch 1 at late times. **(v2: this paragraph states the
v1 conclusion. Whether it survives the corrected $\kappa\alpha A^0 P$ source
term in the $\eta$ equation is IVN-I-3, CRITICAL and outstanding — see P.10.5
caveats above.)**

---

## P.10.7 — Matter Sector Inclusion

### P.10.7.1 — The Full Friedmann System

Restoring $\rho_{\text{matter}}$ and $p_{\text{matter}}$:

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\left(\rho_m + m\eta + \frac{\lambda}{4}\eta^2
+ \frac{\kappa\alpha}{4}(A^0)^2\right) \tag{F1-full}$$

$$\frac{\ddot{a}}{a} = -\frac{\kappa}{6}\left(\rho_m + 3p_m - 2m\eta
- \frac{\lambda}{2}\eta^2 + \kappa\alpha(A^0)^2\right) \tag{F2-full}$$

The $\eta$ evolution equation is modified by the matter sector through the
$\Gamma_{\text{decoh}}$, $\Gamma_{\text{recoh}}$ terms (Paper A, Section 2.4a):

$$\dot{\eta} + 3H\eta = -\Gamma_{\text{decoh}}\eta + \Gamma_{\text{recoh}}(1-\eta)
\tag{E1-full}$$

At high temperature ($T > T_c$), $\Gamma_{\text{decoh}} \gg \Gamma_{\text{recoh}}$
and $\eta \to 0$. At low temperature, $\Gamma_{\text{recoh}}$ dominates and
$\eta \to \eta_{\text{eq}}$.

### P.10.7.2 — Epochs

The cosmological epochs in the full system:

| Epoch | $T$ | $\eta$ | Dominant source | $a$ scaling |
|-------|-----|--------|-----------------|-------------|
| Pre-bounce (Planck) | $\gg T_c$ | $\to 0$ (melted) | $\rho_m$ radiation-like | bounce |
| Post-bounce condensation | $\sim T_c$ | $0 \to \eta_{\text{eq}}$ | Phase transition | rapid |
| Radiation era | $> T_{\text{eq}}$ | $\eta_{\text{eq}}$ | $\rho_m \propto a^{-4}$ | $a \propto t^{1/2}$ |
| Matter era | $< T_{\text{eq}}$ | $\eta_{\text{eq}}$ | $\rho_m \propto a^{-3}$ | $a \propto t^{2/3}$ |
| Condensate era | late | $\eta_{\text{eq}}$, diluting | condensate term | approaches dust |
| Maximum expansion | — | small | curvature | $\dot{a} = 0$ |

The condensate era (when the condensate term dominates over matter) occurs when:

$$m\eta_{\text{eq}}/a^3 \gtrsim \rho_{m,0}/a^3$$

i.e., when $m\eta_{\text{eq}} \gtrsim \rho_{m,0}$. This is the SCH analogue of
dark energy domination, but driven by the geometric condensate rather than a
cosmological constant. *(IVN: check whether this produces accelerated expansion
or simply halts deceleration.)*

### P.10.7.3 — The $R_{\text{universe}}$ Derivation Including Matter

The turnaround radius in the full system satisfies $H = 0$:

$$\frac{1}{a_{\text{max}}^2} = \frac{\kappa}{3}\left(\rho_{m,0}\,a_{\text{max}}^{-3}
+ m\eta_{\text{eq}}\,a_{\text{max}}^{-3} + \frac{\lambda\eta_{\text{eq}}^2}{4}
\,a_{\text{max}}^{-6} + \frac{\kappa\alpha}{4}\langle(A^0)^2\rangle\,a_{\text{max}}^{-3}
\right) \tag{Runiv-full}$$

At turnaround, the $a^{-6}$ term (Term B) is negligible for $a_{\text{max}} \gg a_*$.
The leading expression:

$$a_{\text{max}}^2 \approx \frac{\kappa}{3}\left(\rho_{m,0} + m\eta_{\text{eq}}
+ \frac{\kappa\alpha}{4}\langle(A^0)^2\rangle\right)\,a_{\text{max}}^3$$

$$a_{\text{max}} \approx \frac{\kappa(\rho_{m,0} + m\eta_{\text{eff}})}{3}
\tag{Runiv-matter}$$

where $m\eta_{\text{eff}} \equiv m\eta_{\text{eq}} + (\kappa\alpha/4)\langle(A^0)^2\rangle$
is the effective condensate contribution.

This is the $R_{\text{universe}}$ derivation including matter. The universe's maximum
radius is set by the total matter plus condensate energy density today. The ratio
of condensate to matter contribution is a free parameter until both the Bi-209
calibration (fixing $m$, $\alpha$) and the condensate equilibrium value
(fixing $\eta_{\text{eq}}$) are determined.

---

## P.10.8 — Observable Predictions from CT-ix

The following are predictions derivable from the CT-ix system, listed with
their current epistemic status.

### P.10.8.1 — The Stiff-Condensate Phase Signal

Near the bounce, $a \propto t^{1/3}$ (Phase I solution, eq. sol-I). This differs
from standard GR bounce models. In principle, a gravitational wave background
produced near the bounce would carry a power-law spectrum characteristic of
the stiff-condensate phase:

$$\Omega_{\text{GW}}(f) \propto f^{n_T}, \qquad n_T = \frac{1 - 3w}{1 + 3w}
\Big|_{w=1} = -1$$

where $w = p_{\text{geo}}/\rho_{\text{geo}} = 1$ in the Term B-dominated Phase I.
The stiff-condensate phase produces a blue-tilted gravitational wave background
($n_T = -1$ corresponds to a spectrum rising toward high frequencies in the
$\Omega_{\text{GW}}$ convention). This is distinct from inflation ($n_T \approx 0$
or slightly negative).

*(This is an observational consequence identified here; formal derivation of the
gravitational wave spectrum from the SCH bounce requires CT-xix.)*

### P.10.8.2 — The Transition Scale $a_*$

The transition from Phase I to Phase III occurs at $a_* = (\lambda\eta_0/4m)^{1/3}$.
This transition leaves an imprint in the effective equation of state history of
the universe. In the CMB power spectrum, the Phase I stiff epoch produces a
suppression of power on scales that enter the horizon during Phase I. Whether
this overlaps with the observed CMB quadrupole and octopole suppression
(attributed in Paper A to the $S^3$ mode cutoff) requires a more detailed
analysis. *(Deferred: the overlap between the $S^3$ mode cutoff mechanism and the
Phase I power suppression should not be assumed; they may be independent mechanisms
acting on different scales.)*

### P.10.8.3 — The Angular Diameter Turnaround

The turnaround in angular diameter distance (Paper A Section 6.8) occurs at
$d_{\text{proper}} = (\pi/2)R_{\text{universe}}$. From (Runiv-matter), with the
matter content fixed by observation:

$$z_{\text{turn}} \approx \left(\frac{a_{\text{max}}}{a_{\text{current}}} - 1\right)
^{-1} \cdot \ldots$$

*(IVN: complete this derivation of $z_{\text{turn}}$ from $a_{\text{max}}$
and the observational Hubble parameter, using the Phase III parametric solution.)*

The preliminary estimate from Paper A (Section 6.8) of $z_{\text{turn}} \sim 2$–8
for $R_{\text{universe}} \sim 2$–4 $R_{\text{Hubble}}$ is consistent with the
Phase III parametric solution; CT-ix makes this a derived result pending (IVN)
completion.

### P.10.8.4 — The $c(t)$ Evolution

From Theorem 5 ($c = \omega R_{\text{cosmic}}$) and the Phase III parametric solution:

$$c(t) = \dot{\phi}(t) \cdot a(\phi(t)) \cdot R_{\text{unit}} \cdot H_{\text{eff}}$$

*(IVN: derive the explicit $c(t)$ from (sol-III) and confirm the fractional
change over one Hubble time is $\Delta c / c \sim H_0 / (1/t_{\text{max}}) \ll 1$
for $t_{\text{max}} \gg H_0^{-1}$, consistent with the Theorem 5 constancy argument.)*

---

## P.10.9 — Status of CT-ix and Open Questions

### P.10.9.1 — What Has Been Established

| Result | Status | Equation |
|--------|--------|----------|
| Branch 1 $\eta$ evolution: $\eta \propto a^{-3}$ | Derived (IVN pending); **confirmed unaffected by IVN-I** | (E1-sol) |
| Branch 1 Phase I solution: $a \propto t^{1/3}$ | Derived (IVN pending) | (sol-I) |
| Branch 1 Phase III solution: standard closed dust | Carried from GR | (sol-III) |
| Branch 1 maximum radius: $a_{\text{max}} = \kappa m\eta_0/3$ | Derived | (amax-explicit) |
| $R_{\text{universe}}$ as function of $m\eta_0$ | Derived (leading order) | (Runiv) |
| CMB constraint on $m\eta_0$ | Derived | (constraint-meta0) |
| Branch 2 late-time attractor = Branch 1 | **Provisional (v1 argument superseded — see P.10.5 caveats; IVN-I-3 outstanding)** | P.10.5.3 |
| Branch 2 bounce condition satisfied generically | **Provisional (scaling argument plausible but not reverified under corrected system)** | P.10.5.4 |
| Phase structure table | Established for Branch 1; **provisional for Branch 2** | P.10.6 |
| $R_{\text{universe}}$ including matter | Derived (leading order) | (Runiv-matter) |
| $\eta$ is sourced by $\kappa\alpha A^0 P$ in Branch 2 (does not dilute independently) | **New in v2 — established qualitatively by IVN-I; quantitative size open (IVN-I-3, CRITICAL)** | (E1-new), P.10.5.0a |

### P.10.9.2 — Open Questions Generated by CT-ix

**OQ-CT-ix-1 — Completion of the $c(t)$ derivation from (sol-III):**
The explicit time dependence of $c(t)$ and verification that $\Delta c/c \ll 1$
over local experimental timescales requires completing the derivation flagged
in P.10.8.4. (Unaffected by the v2 correction — Branch 1 / Phase III only.)

**OQ-CT-ix-2 — Phase I / CMB quadrupole overlap:**
Whether the Phase I stiff-condensate power suppression overlaps with the $S^3$
mode cutoff mechanism for the CMB quadrupole. These are potentially independent
mechanisms; their combination requires a joint analysis. (Unaffected — Branch 1
only.)

**OQ-CT-ix-3 — The $\eta$ evolution at finite $A^0$ (Branch 2 correction):**
*[v2 update: this question is now answered qualitatively.]* Section P.10.5.1
assumed $\dot{\eta}$ is unaffected by the $A^0$ coupling term at leading order.
IVN-I (Appendix P v13, Section P.7.7.3a) carried the contraction through
explicitly in a consistent metric convention and found the assumption is
**false**: $\dot\eta + 3H\eta = \kappa\alpha A^0 P$. What remains open is the
*quantitative* size of this effect over the timescales where Branch 2 is
dynamically relevant — this is IVN-I-3, CRITICAL, and is now the operative
open question in place of the original OQ-CT-ix-3 wording.

**OQ-CT-ix-4 — The transition scale $a_*$ and observational constraints:**
The transition scale $a_*$ should be constrained against the observed matter-radiation
equality scale and the CMB acoustic peak structure. A mismatch would constrain
the ratio $\lambda/m$. (Unaffected — Branch 1 only.)

**OQ-CT-ix-5 — Connection to the condensate recoherence epoch:**
The $\eta$ dilution law $\eta \propto a^{-3}$ assumes free dilution. In the presence
of $\Gamma_{\text{recoh}}$ (Paper A, 2.4a), $\eta$ approaches $\eta_{\text{eq}}$
rather than diluting to zero. The transition between the free-dilution phase and
the $\eta_{\text{eq}}$ phase corresponds to the matter condensation epoch.
This epoch should be located within the (E1-full) equation and its consequences
for the Friedmann system characterised. *(v2 note: Appendix P v13 Section
P.7.7.5 also uses the label "OQ-CT-ix-5" for a related but distinctly worded
question — "duration of the matter-creation epoch relative to the rotation
period $\pi/(2m)$," the key input for the revised PT-1 phase estimate. These
are the same underlying physical epoch and should be resolved together, but
the numbering has drifted between documents; this is flagged here rather than
silently reconciled, since renumbering either document unilaterally risks
creating a worse mismatch. Whoever picks up this item should merge the two
formulations explicitly and settle on one canonical statement.)*

### P.10.9.3 — Prerequisites Satisfied by CT-ix for Downstream Targets

| Target | What CT-ix provides |
|--------|---------------------|
| PT-1 (chirality inversion) | Bounce regularity confirmed (unaffected by v2). Branch 2 oscillator *structure* (qualitative) still provides useful intuition, but the quantitative $A^0$ oscillation form used for PT-1's phase estimate should now be taken from Appendix P v13 Section P.7.7.3 ($\Omega_1,\Omega_2,\Phi_{\text{cycle}}$), not from this document's superseded (E2b)/(E3b)/$\Omega_{\text{mix}}$. |
| CT-xix (antipodal coupling) | Phase I / Phase III boundary, condensate amplitude at cosmological times (Branch 1 — unaffected) |
| CMB predictions (Paper A §6.9) | Phase structure history, $c(t)$ evolution form, $R_{\text{universe}}$ derivation (Branch 1 — unaffected) |
| $z_{\text{turn}}$ prediction (Paper A §6.8) | $a_{\text{max}}$ derived, $z_{\text{turn}}$ derivation sketched (Branch 1 — unaffected) |
| Angular diameter test (Paper B §4) | $R_{\text{universe}}$ constrained from action parameters (Branch 1 — unaffected) |

---

## P.10.10 — Independent Verification Checklist

The following are the minimum IVN items that should be completed before any
downstream calculation treats CT-ix results as established. **(v2 note: items
5 and 6 below concern the superseded Branch 2 system; use the seven IVN-I
items in Appendix P v13 Section P.7.7.9 for the corrected system instead.
They are retained here, marked superseded, for the historical record.)**

1. **(IVN-1)** Confirm $(\gamma^0)^2 = -\mathbf{1}$ in the sign convention used,
   and that the Dirac equation (D) used throughout is consistent with the tetrad
   convention of P.9.2.

2. **(IVN-2)** Derive (E1) $\dot{\eta} + 3H\eta = 0$ explicitly from (D1) by
   computing $\frac{d}{dt}(\bar{\psi}\psi)$ term by term. *(v2: this is the
   Branch 1, $A^0=0$ reduction and is confirmed unaffected by IVN-I — the
   corrected system reduces to exactly this equation when $A^0=0$. Still
   worth completing as a standalone check, but no longer blocking.)*

3. **(IVN-3)** Verify (sol-I) by back-substituting into (F1b) in the Phase I limit
   and confirming both sides are equal.

4. **(IVN-4)** Verify the bounce-density formula from CT-viii using (E1-sol): that
   $\eta(a_{\text{b}}) = \eta_0/a_{\text{b}}^3$ is consistent with
   $\eta_{\text{bounce}} \approx \sqrt{12/(\kappa\lambda)}/a_{\text{bounce}}$.

5. ~~**(IVN-5)** Derive (E2) and (E3) explicitly from (D), establishing the closure
   of the Branch 2 bilinear system.~~ **SUPERSEDED (v2).** (E2)/(E3) are the
   pre-IVN-I system. Use Appendix P v13 IVN-I-1, IVN-I-2, IVN-I-7 instead,
   which verify the corrected $(A^0,P)$ system (E-A-new)/(E-P-new) and its
   monodromy matrix.

6. ~~**(IVN-6)** Confirm that $(A^0)^2$ oscillation amplitude decays as $a^{-3}$ at
   late times by carrying the damped oscillator analysis (osc) through to its solution.~~
   **SUPERSEDED (v2).** (osc) is derived from the pre-IVN-I system. The
   late-time amplitude scaling under the corrected, frictionless system is
   unresolved — this is effectively subsumed by Appendix P v13 IVN-I-3
   (CRITICAL), since the amplitude scaling and the $\eta$-sourcing question
   are coupled.

7. **(IVN-7)** Verify (Runiv-matter) against the observational Hubble constraint
   $H_0^2 \approx \kappa\rho_{m,0}/3$ to confirm the matter sector is correctly
   included.

8. **(IVN-8)** Derive $z_{\text{turn}}$ explicitly from (sol-III) and (Runiv-matter),
   confirming the range $z_{\text{turn}} \sim 2$–8 for
   $R_{\text{universe}} \in [2,4]R_{\text{Hubble}}$.

---

## Summary

CT-ix delivers the cosmological dynamics that CT-viii's equations implied but
did not solve. The principal results are:

- **Branch 1** is fully characterised: two-phase dynamics (stiff-condensate
  then dust-condensate), analytic solutions in each phase, explicit $a_{\text{max}}$
  and therefore explicit $R_{\text{universe}}$ as a function of $m\eta_0$.
  **Confirmed unaffected by the v2 (IVN-I) correction.**

- **Branch 2** was argued in v1 to asymptote to Branch 1 at late times, with
  decaying $A^0$ oscillations and a diluting torsion contribution. **This is
  now provisional (v2).** IVN-I found that $\eta$ is sourced by
  $\kappa\alpha A^0 P$ in Branch 2 — a coupling absent from the v1 system —
  and that the $(A^0,P)$ oscillator itself has a different (frictionless,
  $\Omega_1\neq\Omega_2$) structure than v1 assumed. The branch distinction
  is still expected to be most significant near the bounce, but the specific
  late-time asymptote argument needs to be redone under the corrected system
  (IVN-I-3, CRITICAL) before it can be relied upon.

- The **CMB quadrupole suppression constraint** translates into a lower bound on
  $m\eta_0$, connecting the action parameters to an observable. (Branch 1 —
  unaffected.)

- The **Phase I stiff-condensate epoch** produces a specific gravitational wave
  spectral tilt ($n_T = -1$), distinguishing the SCH bounce from inflationary
  models. (Branch 1 — unaffected.)

- **Eight open questions** and **eight IVN items** from v1 are identified,
  joined in v2 by the seven IVN-I items (Appendix P v13 P.7.7.9) covering the
  corrected Branch 2 system. IVN-I-3 is the single highest-priority item in
  the combined list: it determines whether the Branch 2 late-time attractor
  claim survives in anything like its v1 form.

The framework is internally consistent. Branch 1's dynamics follow from the
equations delivered by CT-viii without additional assumptions and are
unaffected by this revision. Branch 2's dynamics require revisiting the
coupled $(\eta, A^0, P)$ system with the corrected bilinear equations before
its conclusions can be treated as more than provisional. All extensions
required additional structure beyond the closed variational theory of
Appendix P v13.

---

*SCH CT-ix Working Derivation — v2 | June 2026*
*Revised from v1: Section P.10.5 (Branch 2) corrected per IVN-I; Branch 1
unaffected. See header changelog for full accounting.*
*Not for citation without author approval.*
*Requires independent verification at all IVN- and IVN-I-marked steps.*
