# SCH — Theorem 4 Split: Carrier Structure and Transport Regimes of Term 2
## Retraction of the Diffusion Timescale; Two-Mode Condensate Structure; Suspension of the P.7.5.2 Frequency Table

*Working Paper | v1 | June 2026*

**Status:** SUPERSEDES Appendix P Theorem 4 (P.5) in full. Extends and
formalizes `SCH_Resolution2_GoldstoneMode_Investigation_v1.md`.
Retracts Appendix P Section P.7.5.2's numerical table. Not yet
incorporated into Appendix P proper — filed here as a standalone
working paper pending review, per the project's convention of keeping
resolution documents separate until a canonical revision folds them
in.

**What this document does.** Appendix P's Theorem 4 asserted, without
derivation, that Term 2 "persists and diffuses after matter moves"
with timescale $\tau_{\text{diff}} \sim R^2 m_{\text{eff}}/\hbar$. That
formula is now understood to be an unexamined transplant of
nonrelativistic quantum wavepacket-spreading scaling onto a
relativistic field with no justification given for why that scaling
should apply. This document does the derivation Theorem 4 skipped:
it linearizes the condensate sector of $S_{\text{geo}}$ around its
equilibrium value, identifies the actual propagating degrees of
freedom, and derives — rather than assumes — their transport
behavior in vacuum and in a thermal/dense medium. Theorem 4 is
retired and replaced by two theorems, 4a and 4b, described below.

---

## 1. Why Theorem 4 Needed Retraction, Restated Precisely

Appendix P, Section P.5, stated in full:

> "Theorem 4 (Term Distinction): Term 2 ($C_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu$) is a propagating field effect governed by the Dirac equation for $\psi$. It persists and diffuses after matter moves. Diffusion timescale: $\tau_{\text{diff}} \sim R^2 m_{\text{eff}}/\hbar$."

No linearized field equation was exhibited anywhere in Appendix P
between "governed by the Dirac equation" and the boxed timescale. The
closure table's parenthetical "(PDE)" beside Theorem 4 asserted the
existence of a differential equation that was never written down. The
specific scaling chosen, $\tau \sim R^2 m/\hbar$, is not the generic
signature of classical field diffusion (which would be written
$\tau \sim R^2/D$ for some diffusion constant $D$ with an identified
physical origin); it is the scaling of nonrelativistic quantum
wavepacket spreading, $\sigma_x(t) \sim \sigma_x(0)\sqrt{1+(\hbar
t/m\sigma_x(0)^2)^2}$, inverted for $t$. Nothing in the framework
establishes that this is the correct physical picture for a
relativistic field sourced by a cosmological or astrophysical bounce.

This substitution was never harmless bookkeeping. Every place in the
framework that quotes a specific propagation timescale or frequency
for Term 2 — the black hole condensate frequency table (P.7.5.2), the
NANOGrav interpretation (Paper B 7.1), the antipodal convergence
mechanism's implicit propagation-speed assumption (Paper A 2.11,
CT-xix), the rotation-curve-flattening wavelength
$\lambda_{\text{cond}} = c/f_{\text{cond}}$ (Paper A 2.11, Paper B
7.4), and the post-merger lensing diffusion test (Paper B 5) — inherits
this unjustified substitution. None of these are shown to be wrong by
what follows. All of them are shown to have been resting on a formula
that was never derived, and several are now shown to need specific,
identified revision.

---

## 2. Identifying the Actual Carriers

### 2.1 The Symmetry Structure (carried from Resolution 2)

$\eta = \bar\psi\psi$ is invariant under the vector phase rotation
$\psi \to e^{i\theta}\psi$; that is not the symmetry the condensate
breaks. The condensate breaks the chiral rotation $\psi \to
e^{i\alpha\gamma^5}\psi$, under which $\eta$ and $P = \bar\psi\gamma^5\psi$
rotate into one another as a two-component object:

$$\eta \to \eta\cos2\alpha - P\sin2\alpha, \qquad P \to \eta\sin2\alpha + P\cos2\alpha$$

This is the same structure as chiral symmetry breaking by the scalar
quark condensate in QCD, with $\eta$ playing the role of
$\langle\bar qq\rangle$ and $P$ playing the role of the pseudoscalar
direction whose fluctuation is the pion.

### 2.2 The Tree-Level Effective Potential and the GMOR Relation

Write the tree-level effective potential for the two-component object
$(\eta, P)$ as the chiral-invariant Mexican-hat potential plus the one
term that explicitly breaks the chiral symmetry — the mass term
$-m\bar\psi\psi = -m\eta$, exactly as it appears in $S_{\text{geo}}$
(P.1.2):

$$V(\eta, P) = \frac{\mu^2}{2}(\eta^2+P^2) + \frac{\lambda}{4}(\eta^2+P^2)^2 - m\,\eta$$

The first two terms are manifestly invariant under the $(\eta,P)$
rotation of Section 2.1; the last term is not — it picks out the
$\eta$ direction, exactly as $-m\bar\psi\psi$ picks out the scalar
channel in the action. In the chiral limit $m \to 0$, the minimum of
$V$ sits anywhere on the circle $\eta^2+P^2 = v^2$ (with $v^2 =
-\mu^2/\lambda$ for $\mu^2<0$); turning on $m \neq 0$ tilts the
potential and selects a unique minimum on the $\eta$ axis. This
reproduces, from the potential itself rather than by fiat, the
parity-preserving vacuum condition $P_{\text{eq}} = 0$ already assumed
in Theorem 2 (P.3) and used throughout Section P.7.7's bilinear
analysis.

Expanding to quadratic order around $(\eta_{\text{eq}}, 0)$, with
$\eta_{\text{eq}} = v + O(m)$:

$$m_\eta^2 \equiv \left.\frac{\partial^2 V}{\partial\eta^2}\right|_{\text{eq}} = 2\lambda\eta_{\text{eq}}^2 + O(m)$$

$$m_P^2 \equiv \left.\frac{\partial^2 V}{\partial P^2}\right|_{\text{eq}} = \frac{m}{\eta_{\text{eq}}}$$

The second relation is the SCH-specific Gell-Mann–Oakes–Renner (GMOR)
relation, structurally identical to $m_\pi^2 f_\pi^2 \propto
m_q\langle\bar qq\rangle$ in QCD: a mode that would be exactly
massless under a purely spontaneous breaking ($m=0$) acquires a mass
suppressed by the size of the explicit breaking. This is not an
analogy invoked for plausibility; it is a direct consequence of
expanding the same potential that already appears in $S_{\text{geo}}$
and that Theorem 0 Step 3 already partially expanded (that step
extracted $m_{\text{eff}}^2 = m^2 - \lambda\eta_{\text{eq}}^2/2$ for
the $\eta$-direction curvature under a slightly different
parameterization; the calculation here is the completion of that
expansion to include the previously-unexamined $P$-direction).

**Result — mass ratio:**

$$\frac{m_P^2}{m_\eta^2} = \frac{m}{2\lambda\eta_{\text{eq}}^3}$$

This is a genuine prediction of the framework, evaluable once Bi-209
fixes $\{m,\lambda,\eta_{\text{eq}}\}$. In the regime $m \ll
\lambda\eta_{\text{eq}}^3$ — the bare mass parameter small compared to
the condensate's own self-interaction scale — $m_P \ll m_\eta \sim
m_{\text{eff}}$, and the light mode is the pseudoscalar fluctuation
$\delta P$, not the amplitude fluctuation $\delta\eta$. Whether this
regime holds is not established here; only the mechanism and the
exact ratio to evaluate are established.

### 2.3 Consequence for "Term 2"

Term 2 is not carried by a single propagating object. It is carried by
(at least) two: the amplitude mode $\delta\eta$, with mass $m_\eta
\sim m_{\text{eff}}$, and the pseudoscalar mode $\delta P$, with mass
$m_P$ generically different from $m_\eta$ and parametrically smaller
in the natural regime identified above. Theorem 4's single-carrier
language is retired on this basis alone, independent of the transport
question addressed next.

---

## 3. Transport Behavior of Each Carrier

### 3.1 Vacuum (T = 0): Dissipationless Propagation

Integrating out the fundamental fermion around the condensate
background (Hubbard–Stratonovich plus the one-loop fermion
determinant — the same technique underlying the NJL/linear-sigma-model
treatment of chiral condensates, and the same technique Theorem 3
already uses for the effective potential, here evaluated at nonzero
external momentum rather than only at $\omega=k=0$) gives an inverse
propagator for each fluctuation channel, $\phi \in \{\delta\eta,
\delta P\}$:

$$D_\phi^{-1}(\omega,k) = \Pi_{\text{tree},\phi} + \Pi_{\text{loop},\phi}(\omega,k)$$

At $T=0$, $\Pi_{\text{loop},\phi}(\omega,k)$ is purely real for
$\omega^2 - k^2c^2 < 4M^2c^4/\hbar^2$, where $M$ is the mass of the
fundamental fermion running in the loop — distinct from, and much
larger than, either condensate-mode mass, which is precisely what
permits $\delta\eta$ and $\delta P$ to exist as light collective
excitations at all. Below this threshold, the derivative expansion of
the loop gives a clean second-order dispersion relation with no
imaginary part:

$$D_\phi^{-1}(\omega,k) = Z_\phi\left[\omega^2 - c^2k^2 - \left(\frac{m_\phi c^2}{\hbar}\right)^2\right] + O\!\left(\frac{\omega^2-c^2k^2}{M^2c^4/\hbar^2}\right)$$

**This is dissipationless.** Both channels obey an ordinary
Klein-Gordon equation with no friction term, and propagate ballistically
at group velocity $v_g = c\sqrt{1 - m_\phi^2c^2/(\hbar^2k^2+m_\phi^2c^2)} \to c$
for $k \gg m_\phi c/\hbar$. In vacuum, or in any environment too dilute
or too cold to populate real fermion pairs, Theorem 4's "diffuses"
language has no support whatsoever — not a revision, an outright
retraction for this regime.

### 3.2 Finite Temperature and Density: Landau Damping

In a medium with a real thermal population of the fundamental fermion
— exactly the situation inside a dense structured environment, and
one Theorem 3 already treats via the Matsubara formalism, here
evaluated at nonzero $(\omega,k)$ rather than only at the origin —
$\Pi_{\text{loop},\phi}(\omega,k;T,\rho)$ acquires an imaginary part
from Landau damping: on-shell thermal fermions scattering off the
fluctuation, a process available even below the $T=0$ pair-production
threshold. In the soft limit $\omega,k \ll M c/\hbar, k_BT/\hbar c$
relevant to condensate-scale physics, this appears generically as

$$\mathrm{Im}\,\Pi_{\text{loop},\phi}(\omega,k;T,\rho) \approx -Z_\phi\,\gamma_\phi(T,\rho)\,\omega + O(\omega^2)$$

Transforming back to position space, each channel now obeys a damped
relativistic wave equation — the telegrapher equation:

$$\ddot{\delta\phi} + \gamma_\phi(T,\rho)\,\dot{\delta\phi} - c^2\nabla^2\delta\phi + \left(\frac{m_\phi c^2}{\hbar}\right)^2\delta\phi = 0, \qquad \phi \in \{\eta, P\}$$

**Two damping rates, not one.** The amplitude channel couples to the
fermion loop through a scalar ($\mathbf{1}$) vertex; the pseudoscalar
channel couples through a $\gamma^5$ vertex. These are different Dirac
traces feeding different loop integrals. There is no a priori reason
$\gamma_\eta(T,\rho) = \gamma_P(T,\rho)$, and this document does not
assume it. Equality, if it ever holds, is a special-case result to be
checked, not a default.

**Relation to $\Gamma_{\text{decoh}}$ — corrected.** An earlier
working hypothesis proposed identifying the transport damping rate
with Theorem 3's $\Gamma_{\text{decoh}}$ directly. This is now
understood to be imprecise. $\Gamma_{\text{decoh}} \propto
\partial^2V_{\text{eff}}/\partial\eta^2$ evaluated at $\omega=k=0$ is
the curvature of the effective potential governing *homogeneous*
relaxation — it is precisely the quantity entering Paper A's $\eta$
evolution equation (Section 2.4a), which contains no spatial gradient
term at all. $\gamma_\eta(T,\rho)$, by contrast, is the $O(\omega)$
slope of the *imaginary part* of the same self-energy function,
evaluated at small but nonzero $(\omega,k)$. Both quantities come from
the same underlying loop integral and the same coupling constants
$\{\alpha,\lambda,\kappa(T)\}$, and are therefore parametrically
related — but they are not the same number, and no relation between
them is asserted here beyond "computable from the same integral by a
different extraction." This is confirmed to leave Theorem 3 and Paper
A Section 2.4a entirely untouched: the homogeneous relaxation equation
they describe is a different slice of the same self-energy function
and requires no revision.

### 3.3 The Two Regimes

The telegrapher equation of Section 3.2 has two limiting behaviors,
selected by the ratio of the propagation distance $R$ to the
damping-set length scale $c/\gamma_\phi$:

- **$R \ll c/\gamma_\phi$ (diffuse environments):** the friction term
  is negligible compared to the wave operator; propagation is
  ballistic, $\tau \sim R/c$ (up to a group-velocity factor for
  $m_\phi \neq 0$).
- **$R \gg c/\gamma_\phi$ (dense, structured environments):** the
  second time-derivative becomes negligible relative to the friction
  term, and the equation reduces to an ordinary diffusion equation,
  $\gamma_\phi\,\dot{\delta\phi} \approx c^2\nabla^2\delta\phi$, with
  diffusion constant $D_\phi = c^2/\gamma_\phi$ and timescale
  $\tau_{\text{diff},\phi} \sim R^2/D_\phi = R^2\gamma_\phi/c^2$.

This is the corrected form of a transport timescale — derived from an
actual field equation rather than borrowed from an unrelated physical
picture. It supersedes $\tau_{\text{diff}} \sim R^2m_{\text{eff}}/\hbar$
in every place that formula previously appeared.

Because $m_\eta \neq m_P$ generically, and $\gamma_\eta \neq \gamma_P$
generically, the two channels cross over from ballistic to diffusive
behavior at different distances in the same environment. A dense
region can plausibly diffuse the heavier, more strongly-coupled
$\eta$-channel while the lighter, more weakly-coupled $P$-channel
remains ballistic well past that point — see Section 5.3.

---

## 4. Theorem 4a — Persistence and Carrier Structure of Term 2

*(Supersedes the ontological content of Appendix P Theorem 4.)*

**Statement.** Term 2 is not a contact interaction; it is a
propagating field effect that persists after the matter source moves,
carried by fluctuations of the condensate sector around its
equilibrium value. Under the chiral decomposition of Section 2.1,
these fluctuations resolve into (at least) two channels: an amplitude
mode $\delta\eta$ and a pseudoscalar mode $\delta P$, related by the
chiral rotation the condensate spontaneously breaks. Because the
condensate's explicit chiral-breaking term ($-m\bar\psi\psi$ in
$S_{\text{geo}}$) is nonzero, the two channels are generically
nondegenerate, with tree-level masses

$$m_\eta^2 = 2\lambda\eta_{\text{eq}}^2 + O(m), \qquad m_P^2 = \frac{m}{\eta_{\text{eq}}}$$

satisfying the SCH GMOR relation $m_P^2/m_\eta^2 = m/(2\lambda\eta_{\text{eq}}^3)$.
This theorem makes no claim about transport, propagation speed, or the
relative magnitude of $m_\eta$ and $m_P$ beyond nondegeneracy; those
are the subject of Theorem 4b.

**Basis.** Section 2 above; consistent with, and completing, Theorem 0
Step 3 and Theorem 2's parity-preserving vacuum condition.

## 5. Theorem 4b — Transport Regimes of Term 2

*(Supersedes the transport-law content of Appendix P Theorem 4.)*

**Statement.** Each condensate fluctuation channel $\phi \in
\{\delta\eta,\delta P\}$ obeys, upon integrating out the fundamental
fermion, a damped relativistic wave equation

$$\ddot\phi + \gamma_\phi(T,\rho)\,\dot\phi - c^2\nabla^2\phi + (m_\phi c^2/\hbar)^2\phi = 0$$

with $\gamma_\phi(T,\rho) \to 0$ in vacuum or sufficiently dilute,
cold media, and $\gamma_\phi(T,\rho) > 0$ sourced by Landau damping off
a real thermal fermion population, computed from the same
finite-temperature self-energy underlying Theorem 3 but evaluated at
its $O(\omega)$ imaginary slope rather than at $\omega=k=0$. The two
channels have generically distinct damping rates $\gamma_\eta \neq
\gamma_P$, sourced by distinct (scalar vs. pseudoscalar) fermion loop
vertices.

Propagation is ballistic ($\tau \sim R/c$) for $R \ll c/\gamma_\phi$
and diffusive ($\tau \sim R^2\gamma_\phi/c^2$) for $R \gg
c/\gamma_\phi$, for each channel independently. No universal, single
transport law applies across all environments or to both channels
simultaneously.

**Basis.** Section 3 above.

**Explicit non-claims.** Theorem 4b does not establish numerical
values for $\gamma_\eta$, $\gamma_P$, or $m_P/m_\eta$. It establishes
the functional form of the transport law and the physical origin of
the damping term, replacing an unjustified formula with a derived one
whose remaining free inputs are named explicitly in Section 6.

---

## 6. Retraction and Suspension of Downstream Claims

### 6.1 Appendix P Section P.7.5.2 — Retracted

The black hole condensate frequency table is defined via $f_{\text{cond}}
= 1/\tau_{\text{diff}}(R_s)$ using the retracted formula
$\tau_{\text{diff}} \sim R_s^2 m_{\text{eff}}/\hbar$. Every entry in
that table (0.5 Hz for 3 $M_\odot$; the NANOGrav-band entries for
intermediate-mass black holes; the Sgr A* and M87* periods) is void,
not merely relabeled. The Schwarzschild radius $R_s$ is, for every
astrophysical black hole, deep in the ballistic regime under Section
3.3's criterion — it is a propagation distance orders of magnitude
smaller than any plausible $c/\gamma_\phi$ — so the correct leading
estimate is $f_{\text{cond}} \sim c/(2\pi R_s)$ or similar, not the
retracted $M^{-2}$ scaling. This changes both the numerical values and
the mass-scaling of the entire table. **Status: SUSPENDED**, not
provisionally retained, pending recomputation once $\gamma_\phi$ and
$m_P$ are evaluated.

### 6.2 Cascading Suspensions

The following inherit Section 6.1's suspension directly and should be
treated as such in any document that cites them, pending recomputation:

- **Paper B Section 7.1** (NANOGrav condensate hum interpretation) —
  the entire frequency-band argument depends on the retracted
  $f_{\text{cond}} \sim M^{-2}$ table.
- **Paper A Section 2.11 / Paper B Section 7.4** (rotation curve
  flattening radius, $\lambda_{\text{cond}} = c/f_{\text{cond}} \sim
  M^2$) — the mass-scaling exponent itself is not established until
  the correct regime (ballistic vs. diffusive, and for which channel)
  is identified at galactic-halo scales.
- **Paper A Section 2.11 / CT-xix** (antipodal convergence mechanism)
  — likely *strengthened* rather than weakened, since $S^3$-crossing
  propagation is plausibly deep in the ballistic regime for the light
  $P$-channel, but the "likely" needs confirmation once $c/\gamma_P$
  is estimated against the relevant cosmological distance scale.
- **Paper B Section 5.2, Signature (ii)** ("heavier condensate diffuses
  more slowly") — does not survive as stated. A two-channel,
  environment-dependent picture replaces single-parameter
  mass-dependence; see Section 6.3 below for the replacement
  signature.

### 6.3 A New, More Specific Signature for Post-Merger Lensing

Section 3.3's regime structure predicts something Theorem 4's original
single-carrier picture could not: a **two-component broadening
signature**. If $\gamma_\eta > \gamma_P$ in the relevant post-merger
environment (plausible, though not established, given the amplitude
channel's larger tree-level mass and presumptively stronger coupling
to the thermal fermion background), the lighter $P$-channel should
remain closer to ballistic — producing a faster-moving, less-diffused
leading edge to the lensing excess — while the heavier $\eta$-channel
diffuses more classically behind it, producing a slower, more
broadened trailing component. This is a distinct, more falsifiable
prediction than a single universal diffusion curve, and is proposed
here as a candidate replacement for the retracted Signature (ii),
pending the same numerical inputs as everything else in this section.

### 6.4 Unaffected

Theorem 3 (P.4) and Paper A Section 2.4a's $\eta$ evolution equation
are confirmed unaffected — see Section 3.2's discussion of
$\Gamma_{\text{decoh}}$ versus $\gamma_\eta$. Theorem 2's
parity-preserving vacuum condition is confirmed rather than assumed,
via the tree-level potential minimization in Section 2.2. Nothing in
Section P.7.7's bilinear evolution system (the $(\eta,A^0,P)$
cosmological dynamics) is touched by this document — that system
concerns the homogeneous cosmological background values of the
bilinears, not their local spatial fluctuations, and uses a distinct
$P = \bar\psi\gamma^5\psi$ evolution driven by the axial current $A^0$
rather than the chiral-rotation fluctuation structure analyzed here.
The two uses of "$P$" — Section P.7.7's cosmological bilinear and this
document's fluctuation field $\delta P$ — denote the same operator
$\bar\psi\gamma^5\psi$ evaluated in different contexts (homogeneous
background vs. local perturbation); no conflict, but documents citing
both should distinguish them explicitly to avoid confusion in future
revisions.

---

## 7. New Calculational Sub-Targets (routed to CT-vii)

Per the routing already established in
`SCH_Resolution2_GoldstoneMode_Investigation_v1.md` Section 7, the
following are named sub-targets of CT-vii (black hole condensate
propagator), since all three fall out of the same linearize-and-loop
calculation begun here:

**CT-vii(a).** Complete the GMOR ratio $m_P^2/m_\eta^2 =
m/(2\lambda\eta_{\text{eq}}^3)$ numerically once Bi-209 fixes
$\{m,\lambda,\eta_{\text{eq}}\}$. Determines whether the natural
light-mode regime of Section 2.2 is realized.

**CT-vii(b).** Compute $\gamma_\eta(T,\rho)$ and $\gamma_P(T,\rho)$
from the $O(\omega)$ imaginary slope of the finite-temperature
self-energy, for both the scalar and pseudoscalar vertices, as
functions of the ambient thermal fermion density. This is the
Landau-damping calculation referenced in Section 3.2 and is a
genuinely new computation, not a lookup from Theorem 3.

**CT-vii(c).** Using (a) and (b), recompute the black hole condensate
frequency table of the (retracted) Section P.7.5.2, determining for
each mass scale which channel dominates and which regime
(ballistic/diffusive/crossover) applies at $R = R_s$, and separately at
the galactic and cosmological distance scales relevant to Sections
6.2–6.3.

---

## 8. Summary Table

| Item | Prior status | Status after this document |
|---|---|---|
| Term 2 carrier | Single object ($\eta$) | Two channels, $\delta\eta$ and $\delta P$, generically nondegenerate (Thm 4a) |
| Transport law | Asserted, undereived: $\tau\sim R^2m_{\text{eff}}/\hbar$ | Derived: damped KG / telegrapher equation per channel, with ballistic and diffusive limiting regimes (Thm 4b) |
| Vacuum propagation | Unclear / conflated with diffusion | Dissipationless, ballistic near $c$ (Sec. 3.1) |
| Dense-medium propagation | Universal quantum-spreading diffusion | Channel-dependent diffusion, $D_\phi = c^2/\gamma_\phi$, from Landau damping (Sec. 3.2–3.3) |
| $\Gamma_{\text{decoh}}$ vs. transport damping | Treated as candidate identity | Distinct slices of the same self-energy; not identical (Sec. 3.2) |
| P.7.5.2 frequency table | Canonical | **Retracted / suspended** pending CT-vii(c) |
| NANOGrav, rotation-curve-flattening $\lambda_{\text{cond}}$ | Canonical, quantitative | Suspended pending CT-vii(c) |
| Antipodal convergence mechanism | Assumed near-$c$ propagation | Plausibly supported by ballistic $P$-channel; not yet confirmed |
| Post-merger lensing Signature (ii) | Mass-dependent diffusion rate | Retired; replaced by candidate two-component (ballistic edge + diffusive trail) signature (Sec. 6.3) |
| Theorem 3, Paper A §2.4a | Canonical | Unaffected |
| Theorem 2 (parity-preserving vacuum) | Assumed | Independently confirmed at tree level (Sec. 2.2) |

---

*SCH Theorem 4 Split — v1 | June 2026*
*Working paper. Not yet incorporated into a revised Appendix P.
Numerical evaluation of $\gamma_\eta$, $\gamma_P$, and $m_P/m_\eta$
(CT-vii sub-targets a–c) is the required next step before any
suspended downstream claim can be reinstated, revised, or confirmed
retracted. Not for citation without author approval.*
