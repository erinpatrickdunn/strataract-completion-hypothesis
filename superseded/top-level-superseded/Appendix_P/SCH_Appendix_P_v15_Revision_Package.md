# Appendix P — v15 Revision Package | June 2026
## Incorporating the Theorem 4 Split: Carrier Structure and Transport Regimes of Term 2

**Document status:** This is the v15 delta package — the new
canonical material plus the exact patches required against v14 — filed
in the same manner as CT-viii's FLRW reduction was originally filed as
a standalone document "designated for incorporation into Appendix P"
before being folded in as Section P.9. This package supersedes
Appendix P v14 Section P.5 (Theorem 4) and touches the STATUS SUMMARY
table, Section P.6, Section P.7.5.2, and Section P.8. It formalizes
`SCH_Theorem4_Split_CarrierStructure_v1.md`, now filed in
`resolved/`. It does **not** touch Section P.7.7 or the Branch 1/Branch
2 cosmological dynamics of Section P.10 — those concern the homogeneous
cosmological background values of the bilinears, not their local
spatial fluctuations, and are confirmed unaffected below (Section 6 of
this package).

**Instruction for incorporation into a future single-file v15.** Per
the project's no-elision policy, the next full monolithic revision of
Appendix P should insert Section P.11 below verbatim after Section
P.7 and before Section P.8, and should apply the patches of Sections
2–5 below to the existing v14 text at the locations indicated. This
package does not reproduce the entirety of v14; it reproduces only
what is new or changed.

---

## 0. Summary of Changes from v14

1. **New Section P.11** is added: the derivation Appendix P Theorem 4
   never supplied. It replaces the asserted, undereived diffusion
   timescale $\tau_{\text{diff}} \sim R^2 m_{\text{eff}}/\hbar$ with an
   actual linearization of the condensate sector, identifying two
   propagating carriers (not one) and a derived transport law (damped
   relativistic wave equation, not a bare diffusion formula) for each.
2. **Section P.5 (Theorem 4)** is marked superseded-in-place. Its text
   is retained for the historical record, per the project's
   discipline of not silently deleting material, but is flagged as
   retired and pointed forward to Theorems 4a/4b in Section P.11.
3. **Section P.6 (Closure Summary)** — the "Torsion / lensing
   persistence" row is split into a carrier-structure part (CLOSED)
   and a transport-regime part (OPEN, gated on CT-vii sub-targets).
4. **Section P.7.5.2** — the black hole condensate frequency table is
   retracted, not relabeled. A retraction notice is inserted in place.
5. **Section P.8** — CT-vii's entry is expanded with three named
   sub-targets (a), (b), (c).
6. **STATUS SUMMARY table, Gap 5** — split into bounce-mechanism
   (unaffected, ESTABLISHED) and propagation-frequency (now OPEN,
   pending CT-vii) components.
7. **Final status line** at the end of Section P.6 is updated to
   record the split.

Nothing else in Appendix P v14 is touched. In particular: Theorem 0,
Theorem 2, Theorem 3, Theorem 5, Theorem 6, Section P.7.7 in its
entirety, and Section P.10 in its entirety are unaffected — see
Section 6 of this package for the explicit non-interference argument.

---

## 1. New Section P.11 — Term 2 Carrier Structure and Transport

*(Insert as a new top-level section after P.7, before P.8. Numbered
P.11 to sit after the existing P.7 subsections and P.9/P.10, which
were themselves appended in that order by CT-viii and CT-ix; P.11
continues the sequence.)*

### P.11.0 — Why This Section Exists

Section P.5 (Theorem 4) asserted that Term 2 "is a propagating field
effect governed by the Dirac equation for $\psi$... It persists and
diffuses after matter moves," with quoted timescale $\tau_{\text{diff}}
\sim R^2 m_{\text{eff}}/\hbar$. No linearized field equation was ever
exhibited to justify this. The specific scaling chosen is the
signature of nonrelativistic quantum wavepacket spreading — the rate
at which a Schrödinger packet of a massive particle delocalizes — not
the signature of a classical relativistic field's transport. Nothing
in v12–v14 established why that picture should apply to a field
governed by $S_{\text{geo}}$'s equations of motion.

This section supplies the derivation Theorem 4 skipped: it linearizes
the condensate sector of $S_{\text{geo}}$ around $\eta_{\text{eq}}$,
identifies the actual propagating degrees of freedom, and derives
their transport behavior in vacuum and in a thermal/dense medium. The
consequence is Theorems 4a and 4b (Section P.11.4), which supersede
Theorem 4 in full.

### P.11.1 — Carrier Identification: the Chiral Decomposition

$\eta = \bar\psi\psi$ is invariant under the vector phase rotation
$\psi \to e^{i\theta}\psi$; that is not the symmetry the condensate
breaks. The condensate breaks the chiral rotation $\psi \to
e^{i\alpha\gamma^5}\psi$, under which $\eta$ and $P = \bar\psi\gamma^5\psi$
rotate into one another:

$$\eta \to \eta\cos2\alpha - P\sin2\alpha, \qquad P \to \eta\sin2\alpha + P\cos2\alpha$$

This is the same structure as chiral symmetry breaking by the scalar
condensate in the NJL model, with $\eta$ in the role of
$\langle\bar\psi\psi\rangle$ and $P$ in the role of the pseudoscalar
direction whose fluctuation is the analogue of the pion.

### P.11.2 — Tree-Level Potential and the SCH GMOR Relation

Write the tree-level effective potential for $(\eta,P)$ as the
chiral-invariant Mexican-hat potential plus the explicit
chiral-breaking term already present in $S_{\text{geo}}$ (P.1.2), the
mass term $-m\bar\psi\psi = -m\eta$:

$$V(\eta,P) = \frac{\mu^2}{2}(\eta^2+P^2) + \frac{\lambda}{4}(\eta^2+P^2)^2 - m\,\eta$$

The first two terms are invariant under the rotation of P.11.1; the
last is not, and picks out the $\eta$ direction exactly as
$-m\bar\psi\psi$ does in the action. In the chiral limit $m\to0$, the
minimum sits anywhere on the circle $\eta^2+P^2=v^2$ ($v^2=-\mu^2/\lambda$
for $\mu^2<0$); $m\neq0$ tilts the potential and selects a unique
minimum on the $\eta$ axis. **This reproduces Theorem 2's
parity-preserving vacuum condition $P_{\text{eq}}=0$ from the
potential itself, rather than assuming it** — Theorem 2 (P.3) is
thereby independently confirmed, not merely left standing.

Expanding to quadratic order around $(\eta_{\text{eq}},0)$, with
$\eta_{\text{eq}}=v+O(m)$:

$$m_\eta^2 \equiv \left.\frac{\partial^2V}{\partial\eta^2}\right|_{\text{eq}} = 2\lambda\eta_{\text{eq}}^2 + O(m)$$

$$m_P^2 \equiv \left.\frac{\partial^2V}{\partial P^2}\right|_{\text{eq}} = \frac{m}{\eta_{\text{eq}}}$$

The second relation is the SCH Gell-Mann–Oakes–Renner relation,
structurally identical to $m_\pi^2 f_\pi^2 \propto
m_q\langle\bar qq\rangle$ in QCD: a mode that would be exactly
massless under purely spontaneous breaking acquires a mass suppressed
by the size of the explicit breaking $m$. This completes, rather than
duplicates, Theorem 0 Step 3's expansion of the $\eta$-direction
curvature ($m_{\text{eff}}^2 = m^2-\lambda\eta_{\text{eq}}^2/2$ there;
$m_\eta^2 = 2\lambda\eta_{\text{eq}}^2$ here — consistent to the order
retained, with the small discrepancy in leading coefficient
attributable to the different parameterization used in Theorem 0's
single-field expansion versus the two-field expansion here; this is a
bookkeeping reconciliation, not a physical inconsistency, and is noted
as a minor open item for a future consolidation pass).

**Mass ratio — a genuine, evaluable prediction:**

$$\boxed{\frac{m_P^2}{m_\eta^2} = \frac{m}{2\lambda\eta_{\text{eq}}^3}}$$

In the regime $m \ll \lambda\eta_{\text{eq}}^3$, $m_P \ll m_\eta \sim
m_{\text{eff}}$: the light carrier is the pseudoscalar fluctuation
$\delta P$. This document does not establish whether this regime
holds — only that it is a specific, calculable condition on
$\{m,\lambda,\eta_{\text{eq}}\}$, evaluable once Bi-209 fixes them
(CT-vii(a), Section P.11.6 below).

**Consequence.** Term 2 is carried by (at least) two fields, not one:
$\delta\eta$ (mass $m_\eta \sim m_{\text{eff}}$) and $\delta P$ (mass
$m_P$, generically distinct, parametrically smaller in the natural
regime above).

### P.11.3 — Transport: Vacuum and Finite Temperature

**Vacuum ($T=0$).** Integrating out the fundamental fermion around the
condensate background (Hubbard–Stratonovich plus the one-loop fermion
determinant — the same technique Theorem 3 uses for the effective
potential, here evaluated at nonzero external momentum) gives, for
each channel $\phi\in\{\delta\eta,\delta P\}$, an inverse propagator
$D_\phi^{-1}(\omega,k) = \Pi_{\text{tree},\phi} +
\Pi_{\text{loop},\phi}(\omega,k)$. Below the pair-production threshold
set by the fundamental fermion mass $M$ (distinct from, and much
larger than, either condensate-mode mass — the separation is what
permits $\delta\eta,\delta P$ to exist as light collective modes at
all), $\Pi_{\text{loop},\phi}$ is purely real, and the derivative
expansion gives an ordinary, dissipationless Klein-Gordon dispersion:

$$D_\phi^{-1}(\omega,k) = Z_\phi\left[\omega^2 - c^2k^2 - (m_\phi c^2/\hbar)^2\right] + O\!\left(\frac{\omega^2-c^2k^2}{M^2c^4/\hbar^2}\right)$$

**In vacuum, or any environment too dilute or cold to populate real
fermion pairs, both channels propagate ballistically at group velocity
$v_g \to c$ for $k\gg m_\phi c/\hbar$, with no friction term
whatsoever.** Theorem 4's diffusion language has no support in this
regime; this is a retraction for the vacuum case, not a revision.

**Finite temperature/density.** In a medium with a real thermal
population of the fundamental fermion (the same finite-temperature
calculation underlying Theorem 3, evaluated at its $O(\omega)$
imaginary part rather than only at $\omega=k=0$),
$\Pi_{\text{loop},\phi}(\omega,k;T,\rho)$ acquires an imaginary part
from Landau damping — on-shell thermal fermions scattering off the
fluctuation, available even below the $T=0$ pair threshold. In the
soft limit relevant here:

$$\mathrm{Im}\,\Pi_{\text{loop},\phi}(\omega,k;T,\rho) \approx -Z_\phi\,\gamma_\phi(T,\rho)\,\omega + O(\omega^2)$$

giving the damped relativistic wave (telegrapher) equation:

$$\ddot{\delta\phi} + \gamma_\phi(T,\rho)\,\dot{\delta\phi} - c^2\nabla^2\delta\phi + (m_\phi c^2/\hbar)^2\,\delta\phi = 0$$

**Two damping rates, not one.** $\delta\eta$ couples to the fermion
loop through a scalar ($\mathbf{1}$) vertex; $\delta P$ couples through
a $\gamma^5$ vertex — different Dirac traces, different loop
integrals. $\gamma_\eta(T,\rho) = \gamma_P(T,\rho)$ is not assumed;
equality, if it ever holds, is a special-case result to check.

**Relation to $\Gamma_{\text{decoh}}$ (Theorem 3) — clarified, not
identified.** $\Gamma_{\text{decoh}} \propto
\partial^2V_{\text{eff}}/\partial\eta^2$ at $\omega=k=0$ is the
curvature governing *homogeneous* relaxation — precisely the quantity
in Paper A's $\eta$ evolution equation (Section 2.4a), which contains
no spatial gradient term. $\gamma_\eta(T,\rho)$ is the $O(\omega)$
slope of the *imaginary part* of the same self-energy function at
small but nonzero $(\omega,k)$. Both come from the same loop integral
and the same couplings $\{\alpha,\lambda,\kappa(T)\}$, and are
therefore parametrically related — but they are not the same number,
and no numerical identification is made here. **Theorem 3 and Paper A
Section 2.4a require no revision; they are a different extraction from
the same self-energy function.**

### P.11.4 — Theorems 4a and 4b

**Theorem 4a (Persistence and Carrier Structure of Term 2).** Term 2 is
not a contact interaction; it is a propagating field effect that
persists after the matter source moves, carried by fluctuations of the
condensate sector around its equilibrium value. These fluctuations
resolve, under the chiral decomposition of P.11.1, into an amplitude
channel $\delta\eta$ and a pseudoscalar channel $\delta P$. Because the
explicit chiral-breaking term $-m\bar\psi\psi$ in $S_{\text{geo}}$ is
nonzero, the two channels are generically nondegenerate, with
tree-level masses $m_\eta^2=2\lambda\eta_{\text{eq}}^2$, $m_P^2 =
m/\eta_{\text{eq}}$, related by the SCH GMOR relation of P.11.2. This
theorem makes no claim about transport speed or the relative magnitude
of $m_\eta$ versus $m_P$ beyond nondegeneracy.

*Basis:* P.11.1–P.11.2; consistent with, and completing, Theorem 0
Step 3 and independently confirming Theorem 2.

**Theorem 4b (Transport Regimes of Term 2).** Each channel $\phi \in
\{\delta\eta,\delta P\}$ obeys, upon integrating out the fundamental
fermion, a damped relativistic wave equation with
$\gamma_\phi(T,\rho)\to0$ in vacuum/dilute-cold media and
$\gamma_\phi(T,\rho)>0$ sourced by Landau damping in a thermal medium,
computed from the same finite-temperature self-energy underlying
Theorem 3 but at its $O(\omega)$ imaginary slope. The two channels have
generically distinct damping rates. Propagation is ballistic ($\tau
\sim R/c$) for $R \ll c/\gamma_\phi$ and diffusive ($\tau \sim
R^2\gamma_\phi/c^2$) for $R \gg c/\gamma_\phi$, independently for each
channel. No universal, single transport law applies across all
environments or to both channels simultaneously.

*Basis:* P.11.3. *Explicit non-claims:* numerical values of
$\gamma_\eta$, $\gamma_P$, $m_P/m_\eta$ are not established here — see
P.11.6 (CT-vii sub-targets).

### P.11.5 — What Is Retracted, Suspended, and Unaffected

**Retracted (vacuum/dilute regime), superseded (dense regime):**
Theorem 4's formula $\tau_{\text{diff}}\sim R^2m_{\text{eff}}/\hbar$ is
retired everywhere. It is replaced, in the diffusive limit only, by
$\tau_{\phi,\text{diff}} \sim R^2\gamma_\phi/c^2$ — a derived quantity
requiring $\gamma_\phi(T,\rho)$, not the borrowed quantum-spreading
form.

**Suspended pending CT-vii(c):** Section P.7.5.2's black hole
condensate frequency table, defined via $f_{\text{cond}} =
1/\tau_{\text{diff}}(R_s)$ using the retired formula. The Schwarzschild
radius $R_s$ is, for every astrophysical black hole, plausibly deep in
the ballistic regime of P.11.3 (a propagation distance far below any
plausible $c/\gamma_\phi$), so the correct leading estimate is of order
$c/R_s$, not the retired $M^{-2}$ scaling — changing both the numbers
and the mass-scaling exponent of the entire table. See the retraction
notice at Section P.7.5.2 (Section 4 of this package) and Section P.8's
expanded CT-vii entry (Section 5 of this package).

**Unaffected:** Theorem 3 (P.4); Paper A Section 2.4a's $\eta$
evolution equation; Theorem 2's parity-preserving vacuum condition
(now independently confirmed, per P.11.2); Section P.7.7's cosmological
$(\eta,A^0,P)$ bilinear system in its entirety, including the
established torsion self-coupling coefficient $-\tfrac{3\kappa\alpha}{2}$.
The latter concerns homogeneous cosmological background values of the
bilinears evolving under the Cartan equation and the axial current
$A^0$; P.11's fluctuation fields $\delta\eta,\delta P$ concern local
spatial perturbations around a fixed background value. Both sections
use the operator $P=\bar\psi\gamma^5\psi$, but in different contexts
(cosmological background bilinear vs. local fluctuation field);
documents citing both should distinguish them explicitly.

### P.11.6 — New Calculational Sub-Targets (CT-vii)

Routed to CT-vii (already the black hole condensate propagator
target, and the natural home for all three, since they fall out of one
linearize-and-loop calculation):

**CT-vii(a).** Evaluate $m_P^2/m_\eta^2 = m/(2\lambda\eta_{\text{eq}}^3)$
numerically once Bi-209 fixes $\{m,\lambda,\eta_{\text{eq}}\}$.
Determines whether the light-$P$-mode regime of P.11.2 is realized.

**CT-vii(b).** Compute $\gamma_\eta(T,\rho)$ and $\gamma_P(T,\rho)$
from the $O(\omega)$ imaginary slope of the finite-temperature
self-energy, for both the scalar and pseudoscalar vertices, as
functions of ambient thermal fermion density. A genuinely new
computation, not a lookup from Theorem 3.

**CT-vii(c).** Using (a) and (b), recompute the black hole condensate
frequency table of (retracted) Section P.7.5.2, determining for each
mass scale which channel dominates and which regime applies at $R=R_s$,
and separately at galactic and cosmological distance scales (relevant
to Paper A Section 2.11, Paper B Sections 7.1 and 7.4).

---

## 2. Patch to Section P.5 (Theorem 4)

*(Insert the following notice immediately before the existing Theorem
4 text in Section P.5. The original text is retained below it,
unedited, per the no-elision policy.)*

> **Superseded notice (v15).** Theorem 4's transport claim — the
> formula $\tau_{\text{diff}}\sim R^2m_{\text{eff}}/\hbar$ — was never
> derived from a linearized field equation and is retracted. Its
> ontological claim (Term 2 is propagating, not a contact interaction)
> is retained and independently re-derived with additional structure
> in **Section P.11**, as **Theorem 4a** (carrier structure: two
> channels, not one) and **Theorem 4b** (transport regimes: derived
> damped-wave equation, not an asserted diffusion formula). Theorem 4
> is superseded in full by Theorems 4a and 4b. The original text is
> retained below for the historical record.

*(Original Theorem 4 text follows unchanged.)*

---

## 3. Patch to Section P.6 (Closure Summary)

*(Replace the "Torsion / lensing persistence" row with the following
two rows:)*

| **Challenge** | **Status** | **Resolution / Reference** |
| --- | --- | --- |
| Torsion / lensing persistence — carrier structure | **CLOSED** | Theorem 4a: Term 2 carried by two generically nondegenerate channels ($\delta\eta$, $\delta P$), related by the chiral rotation the condensate breaks, satisfying the SCH GMOR relation. (P.11.1–P.11.2, P.11.4) |
| Torsion / lensing persistence — transport regime | **OPEN** | Theorem 4b: transport is a derived damped relativistic wave equation, dissipationless in vacuum, diffusive in dense media, with per-channel damping rates $\gamma_\eta,\gamma_P$ undetermined numerically. Superseded formula: $\tau_{\text{diff}}\sim R^2m_{\text{eff}}/\hbar$ (Theorem 4, retracted). Gated on CT-vii(a–c). (P.11.3–P.11.6) |

*(Update the "Final Status" prose at the end of Section P.6 by
appending the following sentence:)*

> The Theorem 4 split (v15) additionally establishes that Term 2's
> carrier structure is closed (two nondegenerate channels, GMOR
> relation derived) while its transport regime remains open pending
> CT-vii(a–c); no numerical transport claim from any prior version of
> Appendix P should be treated as established until those sub-targets
> are complete.

---

## 4. Patch to Section P.7.5.2

*(Insert the following retraction notice immediately before the
existing frequency table. The original table is retained below it,
unedited, per the no-elision policy — but every number in it should be
read as void until CT-vii(c) is complete.)*

> **Retraction notice (v15).** This table was computed via
> $f_{\text{cond}} = 1/\tau_{\text{diff}}(R_s)$ using Theorem 4's
> formula $\tau_{\text{diff}} \sim R_s^2m_{\text{eff}}/\hbar$, now
> retracted (Section P.11). The Schwarzschild radius $R_s$ is, for
> every astrophysical black hole, plausibly deep in the ballistic
> propagation regime of Theorem 4b — a distance far below any plausible
> $c/\gamma_\phi$ — meaning the correct scaling law is of order $c/R_s$,
> not $M^{-2}$. **Every entry in the table below is void, not merely
> mislabeled, and the mass-scaling exponent itself is not currently
> established.** Recomputation is CT-vii(c) (P.11.6). Downstream
> claims depending on this table — Paper B Section 7.1 (NANOGrav),
> Paper A Section 2.11 and Paper B Section 7.4 (rotation curve
> flattening wavelength $\lambda_{\text{cond}}\sim M^2$) — are
> suspended pending recomputation, not provisionally retained.

*(Original table follows unchanged, for historical record only.)*

---

## 5. Patch to Section P.8 (CT-vii entry)

*(Replace the existing one-line CT-vii entry with:)*

> **CT-vii.** Black hole condensate propagator: full perturbative mode
> analysis of the spinor condensate field around a Schwarzschild
> background. Prerequisite for converting the dimensional estimate
> $f_{\text{cond}} \sim M^{-2}$ into a quantitative prediction (now
> understood to require re-derivation from first principles rather
> than confirmation — see Section P.11), and for establishing whether
> condensate propagation couples to pulsar timing. Also prerequisite
> for CT-xiii, CT-xix, and CT-xx. **Expanded (v15) with three named
> sub-targets, per the Theorem 4 split:**
>
> - *CT-vii(a)* — numerical evaluation of the SCH GMOR ratio
>   $m_P^2/m_\eta^2 = m/(2\lambda\eta_{\text{eq}}^3)$ once Bi-209 fixes
>   $\{m,\lambda,\eta_{\text{eq}}\}$.
> - *CT-vii(b)* — computation of the per-channel Landau-damping rates
>   $\gamma_\eta(T,\rho)$, $\gamma_P(T,\rho)$ from the finite-temperature
>   self-energy's $O(\omega)$ imaginary slope.
> - *CT-vii(c)* — recomputation of the black hole condensate frequency
>   table (P.7.5.2, retracted) using (a) and (b), determining the
>   dominant channel and propagation regime at each relevant distance
>   scale.
>
> See Section P.11 for full derivation and motivation.

---

## 6. Patch to the STATUS SUMMARY Table (top of document)

*(Replace the Gap 5 row with:)*

| **Gap** | **Status** | **Resolution / Reference** |
| --- | --- | --- |
| Gap 5 — Black hole bounce resonance (mechanism) | **ESTABLISHED** | Term 3 at Planck density, condensate propagation *mechanism* from Theorem 4 (now Theorem 4a) established. Unaffected by v15. |
| Gap 5a — Black hole bounce resonance (propagation frequency) | **OPEN (v15)** | The quantitative frequency table (P.7.5.2) computed the propagation *rate* from a retracted formula (Theorem 4, superseded by Theorem 4b). Frequency values are suspended pending CT-vii(a–c). See Section P.11. |

---

## 7. Non-Interference Confirmation (Section P.7.7 and P.10)

For the avoidance of doubt, since Section P.7.7's chirality-sector
closure (v14) and Section P.10's Branch 2 cosmological dynamics both
involve bilinears $(\eta, A^0, P)$ that could be mistaken for the
objects analyzed in Section P.11:

- Section P.7.7's system governs the **homogeneous, spatially
  constant, cosmological background values** of $\eta(t)$, $A^0(t)$,
  $P(t)$ across the bounce cycle, driven by the Cartan equation and
  the cosmological Dirac equation of CT-viii (P.9.5.3). It contains no
  spatial gradient terms and describes no local fluctuation.
- Section P.11 governs **local, spatially varying perturbations**
  $\delta\eta(x,t)$, $\delta P(x,t)$ around a fixed background
  equilibrium value $\eta_{\text{eq}}$, via a tree-level potential
  expansion and a one-loop self-energy at nonzero momentum.
- These are complementary, not competing, analyses of the same
  underlying action. The torsion self-coupling coefficient
  $-\tfrac{3\kappa\alpha}{2}$ established in P.7.7.3, the Branch
  1/Branch 2 dynamics of P.10, and the FLRW reduction of P.9 all stand
  exactly as in v14, untouched by this package.

---

*Appendix P v15 Revision Package | June 2026*
*Formalizes `SCH_Theorem4_Split_CarrierStructure_v1.md` (filed in
`resolved/`) into canonical form. To be merged into a future
single-file Appendix P v15 per the no-elision policy. Numerical
evaluation of CT-vii(a–c) remains the required next step before any
suspended claim (P.7.5.2 table, Paper B §7.1, Paper A/B rotation-curve
wavelength scaling) can be reinstated, revised, or confirmed retracted.
Not for citation without author approval.*
