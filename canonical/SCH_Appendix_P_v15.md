**Appendix P — v15 | June 2026**

**Appendix P**

**Proof of Closure: The Strataract Completion Hypothesis**

**as a Closed Variational Theory**

**Working Proof Document — v15 | June 2026**

Revised from v14: **This revision incorporates the Theorem 4 split.**
Appendix P v14's Theorem 4 (Section P.5) asserted that Term 2 "persists
and diffuses after matter moves" with timescale $\tau_{\text{diff}}
\sim R^2m_{\text{eff}}/\hbar$, without ever exhibiting the linearized
field equation that formula was supposed to summarize. That formula is
now understood to have been an unexamined transplant of nonrelativistic
quantum wavepacket-spreading scaling onto a relativistic field, with no
derivation ever given for why that picture should apply. This revision
supplies the missing derivation, in a new **Section P.11**: linearizing
the condensate sector of $S_{\text{geo}}$ around $\eta_{\text{eq}}$
reveals that Term 2 is carried by **two** propagating fields, not one
— an amplitude channel $\delta\eta$ and a pseudoscalar channel
$\delta P$, related by the chiral rotation the condensate
spontaneously (and, because of the explicit mass term, only
approximately) breaks, with masses related by a Gell-Mann–Oakes–Renner-type
relation derived here for the first time. Each channel's transport is
then derived, not asserted: dissipationless ballistic propagation in
vacuum, crossing over to a diffusive regime with a Landau-damping rate
$\gamma_\phi(T,\rho)$ in a thermal medium — a genuine damped
relativistic wave (telegrapher) equation, replacing the retired
diffusion formula. Theorem 4 is superseded in full by two new theorems,
4a (carrier structure, CLOSED) and 4b (transport regimes, OPEN pending
three new CT-vii sub-targets). The black hole condensate frequency
table of Section P.7.5.2 — which was computed directly from the
retired formula — is retracted, not relabeled: its entries are void,
and its mass-scaling exponent is not currently established. This
propagates to a retraction/suspension of every downstream claim that
quoted a specific propagation timescale or frequency for Term 2,
tracked in Section P.11.5 and cross-referenced from the STATUS SUMMARY
table below. Section P.7.7's cosmological $(\eta,A^0,P)$ bilinear
system and Section P.10's Branch 1/Branch 2 dynamics are confirmed
**unaffected** — those concern the homogeneous cosmological background
values of the bilinears, evolving under the Cartan equation and the
cosmological Dirac equation; Section P.11 concerns local spatial
fluctuations around a fixed background value, a distinct (if related)
calculation. This document formalizes and supersedes the standalone
working paper `SCH_Theorem4_Split_CarrierStructure_v1.md`. Supersedes
v14.

Revised from v13.1: **This is the single-pass canonical rewrite the
v13.1 freeze notice reserved for once IVN-CT8-Dirac-1 closed.** It
closes. Summary of the resolution path, in full, since this document
supersedes several working papers whose findings are folded in here
rather than left as external references:

**IVN-CT8-Dirac-1a** (convention audit) closed first: the Hermiticity
assignment $\gamma^{0\dagger}=-\gamma^0$ in $(-,+,+,+)$ — equivalently
$(\gamma^0_D)^2=+1$ in the $(+,-,-,-)$ convention used throughout the
chirality sector — is forced, not one of several equally valid choices.
This settled that $\eta\equiv-i\bar\psi\psi$ is a labeling clarification
of Theorem 0, not a reopening of it (see the note at Theorem 0 below).

**IVN-CT8-Dirac-1b** (abstract-lemma route) found the general
Hermiticity-based protection argument correct for the mass and
quartic-$\eta$ sectors, but produced a manifestly imaginary residual in
$\dot P$ when applied to the self-sourced torsion term — a real bilinear
cannot have an imaginary source, so this signaled an unresolved error
rather than a physical result, and opened **1b-i**.

**IVN-CT8-Dirac-1b-i** (direct-bilinear route) resolved it: working
entirely in explicit 2-spinor components ($\psi=(\xi,\chi)^T$,
$u=\xi^\dagger\xi$, $v=\chi^\dagger\chi$, $w=\xi^\dagger\chi$, with
$\eta=u-v$, $J^0=-(u+v)$, $A^0=-(w+\bar w)$, $P=i(w-\bar w)$), the bug
was traced to a gamma-algebra slip in the abstract lemma's application
to the $\Gamma=\gamma^5$ bilinear. The direct-bilinear route gave a
corrected, self-consistent, fully real Branch 2 system with torsion
coefficient $-\tfrac{3\kappa\alpha}{2}$ in $\dot\eta$, and recommended
one further independent check — the 4D-first route, the one leg of the
original triangulation strategy not yet executed — before the freeze
could be lifted.

**The 4D-first route was attempted and initially erred.** A first pass
worked from the connection component $K_0^{\ ij}$ (sourced by the
*spatial* axial current $A^k$) and found an apparent factor-of-2
discrepancy against the direct-bilinear result. That pass was wrong: it
had selected the wrong contorsion component. $K_0^{\ ij}$ is sourced by
$A^k$, which vanishes identically on the homogeneous, isotropic
background — no combinatorics performed on a vanishing term produces a
physical contribution. A confirming pass, redone using the correct
component ($K_{ijk}$, fully spatial internal indices, sourced by $A^0$,
which does not vanish on the background), reproduced
$-\tfrac{3\kappa\alpha}{2}$ exactly, in full agreement with the
direct-bilinear route. **Three independent routes now converge on the
same coefficient**, satisfying the project's own bar for promotion from
Provisional to Canonical for the first time in this sector's five-version
history.

The freeze on P.7.7.3, P.7.7.3a, and CT-ix Section P.10 (Branch 2) is
**lifted**. This document is the single-pass rewrite: every frozen
section is rewritten in full below, not referenced. Gap 7 moves from
FROZEN to ESTABLISHED. Gap 16 moves from FROZEN (Branch 2) to CLOSED,
mechanism-established, with quantitative magnitude explicitly flagged
as still pending the Bi-209 calibration (which fixes $\alpha$) — this
is a distinct and narrower open item than "frozen," and is stated as
such throughout.

**Two items are explicitly out of scope of this rewrite and are not
silently resolved.** The clean-room package that originally triggered
the v13.1 freeze also flagged two defects unrelated to the chirality
sector: a claimed double-count in P.9.4.2 and a claimed sign error in
P.9.5.3's Hubble-friction coefficient. Neither claim has been
independently re-verified by any route in the IVN-CT8-Dirac-1 series —
all three of that series' documents worked with the reduced bilinear
system, not with re-deriving P.9.4.2/P.9.5.3 from scratch. Given that
the clean-room package's central claim (no Branch 2 sourcing at all)
did not survive independent scrutiny, its other claims are not treated
as established just because they came bundled with it. P.9 is carried
forward in this document exactly as in v12/v13, unedited. This is
flagged as a new, narrowly-scoped open item below (Section P.9, note at
end) rather than either silently fixed or silently ignored.

All content not touched by the above is carried forward in full below.
Nothing is elided with "unchanged from vX" — every section has its
complete text in this document.

---

**STATUS SUMMARY**

| **Gap** | **Status** | **Resolution / Reference** |
| --- | --- | --- |
| Gap 1 — Leading-order uniqueness of $Q_{\mu\nu}$ | **ESTABLISHED** | Fierz completeness, local EFT limit, explicit density hierarchy bound |
| Gap 2 — Four-velocity normalization | **ESTABLISHED** | Fierz + parity-preserving sector, regime-conditional |
| Gap 3 — Gamma_decoh, Gamma_recoh | **DERIVED** | Matsubara + EFT kinetics, no additional free parameters |
| Gap 4 — Torsion persistence | **RESOLVED** | Algebraic/field distinction |
| Gap 5 — Black hole bounce resonance (mechanism) | **ESTABLISHED** | Term 3 at Planck density, condensate propagation *mechanism* established (Theorem 4, now Theorem 4a). Unaffected by v15. |
| Gap 5a — Black hole bounce resonance (propagation frequency) | **OPEN (v15)** | The quantitative frequency table (P.7.5.2) computed the propagation *rate* from a formula (Theorem 4) now retracted and superseded by Theorem 4b. Frequency values are suspended pending CT-vii(a–c). See Section P.11. |
| Gap 6 — S³ spatial topology | **ESTABLISHED** | SU(2) group manifold identification, canonical spin structure |
| Gap 7 — Chirality inversion across bounce and sympathetic nucleation | **ESTABLISHED (mechanism); numerical evaluation pending Bi-209** | Resolved via the IVN-CT8-Dirac-1 series: convention fixed (1a), torsion coefficient triply confirmed at $-\tfrac{3\kappa\alpha}{2}$ (1b-i direct-bilinear, and 4D-first after correcting an initial wrong-component error). Chirality inversion per cycle is confirmed non-generic; the monodromy phase is calculable in form, pending $\alpha$, $m$ from Bi-209. See Section P.7.7 in full below. |
| Gap 8 — Photon-condensate coupling and CMB monopole | **OPEN TARGET** | CT-xiii identified. Prerequisites: CT-vii + CT-viii. |
| Gap 9 — Physical primitive: ψ as derived object, not ansatz | **ESTABLISHED** | P.0b: ψ is the unique minimal 4D rotational encoder; S_geo follows as consequence. Theorem 0. |
| Gap 10 — W-spin as mass: η as physical rotational departure | **ESTABLISHED** | Theorem 0: η = ψ̄ψ (up to the sign/factor clarification of IVN-CT8-Dirac-1d, non-substantive) is the w-spin magnitude of the 4D knot; bridges physical picture and formalism. |
| Gap 11 — c as tangential S³ velocity: speed of light derived | **ESTABLISHED** | Theorem 5: c(t) = ω(t) · R_cosmic(t). Photon as minimum-w-spin surface wave. Constancy of c derived from S³ geometry. Lensing confirms photon w-spin is nonzero. |
| Gap 12 — Matter-light phase transition: topological distinctness | **ESTABLISHED** | Theorem 6: η = 0 and η ≠ 0 are distinct phases separated by a topological boundary, not points on a speed continuum. Its chiral-symmetry-breaking content is now given explicit tree-level form in Section P.11. |
| Gap 13 — Antipodal condensate coupling: mechanism linking local BH emission to global $S^3$ modes | **OPEN TARGET** | CT-xix identified. Prerequisites: CT-vii + CT-viii. CT-viii closed. Physical motivation in *SCH_GalacticEngine_PhysicalPicture_v1*. Plausibly aided by the light $\delta P$ channel's ballistic propagation (Section P.11.3), pending CT-vii(c). |
| Gap 14 — Thermodynamic consistency of coherence-forcing: entropy accounting for galactic engine | **OPEN TARGET** | CT-xx identified. Prerequisites: CT-xix + Bi-209 calibration. |
| Gap 15 — FLRW reduction of $S_{\text{geo}}$: modified Friedmann equations and bounce condition | **CLOSED** | CT-viii: modified Friedmann equations derived, two-branch cosmology established, bounce existence condition proven, GR recovery confirmed. Section P.9. Two subsidiary claims from the clean-room package (P.9.4.2 double-count; P.9.5.3 sign) remain independently unverified — see note at end of P.9. |
| Gap 16 — Cosmological dynamics: solution structure of the modified Friedmann system | **CLOSED — Branch 1 fully; Branch 2 mechanism established, quantitative magnitude pending Bi-209** | CT-ix: Branch 1 two-phase dynamics, $R_{\text{universe}}$, CMB quadrupole constraint on $m\eta_0$, all unaffected throughout this sector's entire revision history. Branch 2 is now a genuinely coupled three-variable $(\eta,A^0,P)$ system with $\eta$ sourced by $\kappa\alpha A^0P$ at the confirmed coefficient; the late-time approach to Branch 1 behavior is a calculable oscillatory correction of fractional size set by $\kappa\alpha$, parametrically small in the weak-torsion-coupling regime already assumed generic, not yet numerically bounded pending $\alpha$. See Section P.10 in full below. |
| Gap 17 — Term 2 carrier structure | **CLOSED (v15)** | Theorem 4a: Term 2 is carried by two generically nondegenerate channels, $\delta\eta$ and $\delta P$, related by the chiral rotation the condensate breaks, satisfying a derived SCH Gell-Mann–Oakes–Renner relation. See Section P.11.1–P.11.2, P.11.4. |
| Gap 18 — Term 2 transport regime | **OPEN (v15)** | Theorem 4b: transport is a derived damped relativistic wave equation, dissipationless in vacuum, diffusive in dense media, with per-channel damping rates undetermined numerically. Supersedes the retired formula $\tau_{\text{diff}}\sim R^2m_{\text{eff}}/\hbar$ (Theorem 4). Gated on CT-vii(a–c). See Section P.11.3, P.11.4, P.11.6. |

The framework has a closed variational structure within its stated EFT
and mean-field condensate regime. All claims are regime-conditional. The
density hierarchy is explicit and bounded. Sections P.7.5, P.7.6 cover
black hole and topological predictions unaffected by any version of the
chirality-sector revision, except that P.7.5's quantitative frequency
table is retracted per Section P.11 (Gap 5a above). Section P.7.7 and
Section P.10 are rewritten in full below, closing the freeze opened in
v13.1, and are confirmed unaffected by the v15 Theorem 4 split. Section
P.11 (new in v15) supplies the carrier structure and transport
derivation that Theorem 4 never provided.

---

# **P.0 Preamble: From Consistency to Proof — and the Role of Regime Conditioning**

Paper A (Draft 2.3) presents the Strataract Completion Hypothesis (SCH) as a modified gravitational field equation:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa\left[T_{\mu\nu} + \alpha\,C_{\mu\nu}\right]$$

$$C_{\mu\nu} = Q_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu$$

This appendix resolves all formal gaps and establishes the framework as a closed variational theory rooted in the Einstein-Cartan-Dirac action with a geometric state spinor field. All leading-order claims hold in the low-density EFT limit ($\rho \ll \rho_c$) governing galactic-scale dynamics. Higher-order contributions (quartic in $\psi$) exist, are identified as Term 3, and dominate at high density.

**The derivation chain:**

**PRIMITIVE:** Rotation is fundamental

**OBJECT:** Spinor field $\psi$ in curved spacetime — covering group $\mathrm{SU}(2)\times\mathrm{SU}(2)$

**ACTION:** $S = S_{\text{EC}} + S_{\text{geo}} + S_{\text{GHY}} + S_{\text{matter}}$

- $S_{\text{EC}}$: Einstein–Cartan gravity (tetrad $e^a_{\mu}$ + spin connection $\omega^{ab}_{\mu}$)
- $S_{\text{geo}}$: Dirac-type spinor with quartic self-interaction ($\lambda > 0$)

**VARIATION:**

$$\frac{\delta}{\delta e^a_{\mu}} \;\Rightarrow\; G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa\left(T_{\mu\nu} + \alpha C_{\mu\nu}\right) + \text{Term}(3)$$

$$\frac{\delta}{\delta\omega^{ab}_{\mu}} \;\Rightarrow\; T_{\lambda\mu\nu} = \frac{\kappa\alpha}{2}\,\varepsilon_{\lambda\mu\nu\rho}\,A^\rho$$

**IDENTIFICATIONS** (leading order, $\rho \ll \rho_c$):

$$C_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu = Q_{\mu\nu}$$
$$\eta = \bar{\psi}\psi \quad (\text{Lorentz scalar by Theorem 2; w-spin magnitude by Theorem 0})$$
$$u^\mu = J^\mu / (\bar{\psi}\psi) \quad (\text{four-velocity from }\psi\text{ alone})$$

**LIMITS:**

- $A^\mu = 0$ (isotropic ground state) $\Rightarrow$ $\mathcal{T} = 0$, $C_{\mu\nu} = 0$ $\Rightarrow$ exact GR
- $A^\mu$ small $\Rightarrow$ Paper A weak-field equation
- $\rho \gg \rho_c$ $\Rightarrow$ Term(3) dominant $\Rightarrow$ neutron star / Planck regime

**TOPOLOGY:** $\mathrm{SU}(2)$ as group manifold $= S^3$ $\Rightarrow$ spatial topology uniquely compatible with $S^3$ (P.7.6)

**GROUND FLOOR:** $\psi$ derived as minimal rotational encoder in 4D; $\eta$ identified as w-spin magnitude; $c$ derived as tangential S³ velocity; photon identified as minimum-w-spin surface wave (lensing confirms $\eta_{\text{photon}} > 0$); matter-light distinction derived as phase transition (P.0b, Theorems 0, 5, 6)

**CHIRALITY SECTOR** (closed in v14): the torsion-fermion self-coupling in Branch 2 is established at coefficient $-\tfrac{3\kappa\alpha}{2}$ in $\dot\eta$, confirmed by three independent derivation routes (Section P.7.7).

**CARRIER/TRANSPORT SECTOR** (new in v15): Term 2 is carried by two
generically nondegenerate condensate fluctuations, $\delta\eta$ and
$\delta P$, whose transport is a derived damped relativistic wave
equation rather than an asserted diffusion formula (Section P.11).

---

# **P.0a Conservation Architecture: The Global Energy-Momentum Accounting**

The modified field equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa(T_{\mu\nu} + \alpha C_{\mu\nu})$ introduces a second source term beyond standard stress-energy. Mathematical self-consistency requires a complete accounting of how energy-momentum is exchanged among all three terms on the right-hand side.

## **P.0a.1 The Required Conservation Statement**

The contracted Bianchi identity requires that the total source on the right-hand side of the field equation be divergence-free:

$$\nabla^\mu T_{\mu\nu}^{\text{total}} = \nabla^\mu\left[T_{\mu\nu}^{\text{matter}} + \alpha C_{\mu\nu} + T_{\mu\nu}^{\text{torsion}}\right] = 0$$

## **P.0a.2 Status of Each Term**

**Term 1 —** $T_{\mu\nu}^{\text{matter}}$: $\nabla^\mu T_{\mu\nu}^{\text{matter}} = 0$ holds independently when matter follows geodesics in the absence of condensate coupling. The geodesic condition is a derived consequence of $S_{\text{geo}}$ in the mean-field condensate regime (P.3, Step 5), not an independent assumption.

**Term 2 —** $\alpha C_{\mu\nu} = \alpha\rho\,\eta\,u_\mu u_\nu$: Divergence-free in the mean-field condensate regime by Theorem 1 (P.2). The $\eta$ evolution equation (Paper A Section 2.4a) is the explicit statement of the Term 1–Term 2 exchange channel.

**Term 3 —** $T_{\mu\nu}^{\text{torsion}} \sim A_\mu A_\nu - \tfrac{1}{2}A_\rho A^\rho g_{\mu\nu}$: Algebraically determined by the Cartan equation (P.1.3). Divergence-free in the parity-preserving vacuum sector (Theorem 2). Outside this sector — now including the resolved Branch 2 self-coupling of Section P.7.7 — the formal accounting at Planck density requires CT-viii.

## **P.0a.3 Exchange Channel Map**

Channel A (Term 1 ↔ Term 2): Condensate decoherence/recoherence. Governed by $u^\mu\nabla_\mu\eta = -\Gamma_{\text{decoh}}\,\eta + \Gamma_{\text{recoh}}\,(1-\eta)$. Rates derived (Theorem 3). Full $\nabla^\mu T_{\mu\nu}^{\text{total}} = 0$ verification: OPEN TARGET.

Channel B (Term 2 ↔ Term 3): Condensate-torsion coupling at high density. Algebraic at galactic densities (Term 3 suppressed by $\varepsilon \leq 10^{-23}$). At cosmological Branch 2 densities: now explicit — see Section P.7.7 — with the self-sourcing of $\eta$ by $\kappa\alpha A^0 P$ as the leading channel-B exchange term in that regime.

Channel C (Term 1 ↔ Term 3): Matter spin coupling to torsion via Papapetrou-Dixon equations. Subleading at galactic densities. Full accounting: OPEN TARGET (part of Gordon decomposition programme, CT-ii).

## **P.0a.4 What Is Closed and What Is Open**

Closed: $\nabla^\mu C_{\mu\nu} = 0$ at leading order (Theorem 1, Appendix A); $\nabla^\mu T_{\mu\nu}^{\text{torsion}} = 0$ in the parity-preserving vacuum (Theorem 2); the $\eta$ evolution equation (Theorem 3); the Branch 2 self-coupling channel (Section P.7.7, this version). Open channels are all in regimes beyond the galactic-scale observational programme and are identified calculational targets, not foundational gaps.

---

# **P.0b The Physical Primitive: ψ as Derived Object**

## **P.0b.1 The Starting Point**

All previous revisions of Appendix P began with the geometric state spinor field $\psi$ as a given object — introduced, identified with the covering group SU(2) × SU(2), and then subjected to variational analysis. This placement of $\psi$ as a starting assumption rather than a derived object left a logical gap at the ground floor of the framework: why this object, and why does it take this specific mathematical form?

Section P.0b fills that gap. The claim is that $\psi$ is not introduced as a mathematical convenience. It is the unique minimal mathematical object capable of encoding rotational state in four-dimensional curved spacetime, and its specific form — a Dirac spinor in the fundamental representation of Spin(1,3) — follows necessarily from that requirement.

The argument has four steps: (i) identify what a physical primitive of rotation requires a mathematical object to do; (ii) enumerate the candidate objects in 4D Riemannian geometry; (iii) show by elimination that the spinor field is the unique minimal candidate; (iv) show that $S_{\text{geo}}$ is the most general local action for that object consistent with the symmetries of the problem.

## **P.0b.2 What a Rotational Encoder Must Do**

The physical primitive is rotation. Not rotation as a phenomenon that emerges at some energy scale, but rotation as a substrate — the bedrock geometric property of a manifold with a metric. For a mathematical object to serve as a rotational encoder in 4D curved spacetime, it must satisfy four requirements:

**R1 — Local:** It must be defined at every point of the spacetime manifold independently of the properties of any other point.

**R2 — Lorentz-covariant:** It must transform in a definite representation of the local Lorentz group SO(1,3) at each point, so that rotational state has a consistent meaning in every local frame.

**R3 — Sensitive to all rotational degrees of freedom:** It must carry information about rotational departure from the isotropic ground state in all independent rotational directions. In four spacetime dimensions, the independent rotational planes are: three spatial rotations (SO(3) subgroup) and three boosts. The object must distinguish departure along each.

**R4 — Minimal:** Among all objects satisfying R1–R3, it should be the one with the fewest independent components, because the physical primitive is a single primitive, not a composite.

## **P.0b.3 Enumeration and Elimination**

The candidate objects in four-dimensional pseudo-Riemannian geometry, classified by their SO(1,3) representation content, are:

**Scalars** (representation: trivial, dimension 1): A scalar field at each point carries no directional information at all. It cannot distinguish the orientation of a rotation — R3 fails.

**Vectors** (representation: 4, dimension 4): A four-vector $V^\mu$ encodes a single preferred direction. In 3+1 dimensions, however, a single preferred direction determines only the axis of rotation, not the sense or magnitude of the rotational departure from isotropy in the transverse planes. For example, a vector pointing in the $x$-direction does not by itself encode the degree of rotation in the $yz$-plane. R3 fails: vectors cannot simultaneously encode departure in all six rotational planes of SO(1,3).

**Antisymmetric tensors** (representation: $6 = 3_+ \oplus 3_-$, dimension 6): The antisymmetric rank-2 tensor $F^{\mu\nu}$ decomposes into self-dual and anti-self-dual parts under the action of the Lorentz group. This object can encode rotation in all six planes. However, it is not minimal: its six independent components over-determine the rotational state, because the two SU(2) factors in SU(2) × SU(2) $\cong$ Spin(1,3) can be encoded in four complex components — two Weyl spinors — not six. The antisymmetric tensor is the square of the spinor in representation-theoretic language; it is not the minimal object. R4 fails.

**Symmetric traceless tensors** (representation: 9, dimension 9): These carry even more components and fail R4 for the same reason, compounded.

**Dirac spinors** (representation: $(\tfrac{1}{2},0) \oplus (0,\tfrac{1}{2})$, dimension 4 over $\mathbb{C}$, i.e., 8 real components): The Dirac spinor $\psi$ is the direct sum of the two fundamental representations of SU(2) × SU(2) $\cong$ Spin(1,3). The first SU(2) factor encodes left-handed rotational state; the second encodes right-handed rotational state. Together they encode the full rotational departure from isotropy in all six planes of SO(1,3), in the minimal representation that does so.

**Weyl spinors** (representation: $(\tfrac{1}{2},0)$ or $(0,\tfrac{1}{2})$, dimension 2 over $\mathbb{C}$): A single Weyl spinor encodes rotational state in only one SU(2) factor. It fails R3 because it is sensitive to rotations of definite handedness only and cannot encode the full parity-symmetric rotational ground state.

**Result of enumeration:** The Dirac spinor $\psi$ is the unique object satisfying R1–R4 simultaneously. Scalars and single vectors fail R3. Antisymmetric tensors fail R4. Weyl spinors fail R3. The Dirac spinor is the minimal complete rotational encoder in 4D curved spacetime.

## **P.0b.4 The Action as Consequence**

Given that $\psi$ is the minimal rotational encoder, the action $S_{\text{geo}}$ is the most general local, Lorentz-invariant, generally covariant action for $\psi$ that is at most quartic in the field and its first derivatives. The Dirac kinetic term $\bar{\psi}\gamma^a e^a_\mu D_\mu \psi$ is the unique kinetic term at quadratic order. The mass term $m\bar{\psi}\psi$ is the unique mass-dimension-4 quadratic interaction. The quartic self-coupling $(\lambda/4)(\bar{\psi}\psi)^2$ is the unique quartic scalar self-interaction consistent with the symmetries of the action. Higher powers of $\psi$ are suppressed by powers of the Planck mass in the EFT sense and are not included at leading order.

The action $S_{\text{geo}}$ is therefore not a freely chosen ansatz. It is the unique leading-order action for the unique minimal rotational encoder in 4D curved spacetime, written in terms of the tetrad $e^a_\mu$ and spin connection $\omega^{ab}_\mu$ that define the curved-spacetime geometry.

**Corollary P.0b.4:** The derivation chain of the framework is complete at the ground floor. The physical primitive (rotation is fundamental) uniquely determines the mathematical object ($\psi$ = Dirac spinor) which uniquely determines the action ($S_{\text{geo}}$ = leading-order action for $\psi$). No unjustified choices are made at any stage.

---

# **Theorem 0 — W-Spin as Mass**

*Note on the literal bilinear formula.* IVN-CT8-Dirac-1d found that a
fully audited convention requires the explicit statement
$\eta\equiv-i\bar\psi\psi$ rather than the bare $\eta=\bar\psi\psi$ used
in earlier drafts of this theorem — a labeling clarification of what the
convention always implied, not a substantive reopening. Theorem 0's
physical content (w-spin magnitude, mass as departure-from-isotropy
energy) is unaffected; the statement and proof below use $\eta=\bar\psi\psi$
as in all prior versions, with this note flagging the sign/factor
housekeeping item for the record.

## **Statement**

The Lorentz scalar bilinear $\eta = \bar{\psi}\psi$, previously established (Theorem 2) to be a genuine Lorentz scalar, is physically identified as the w-spin magnitude of the matter field — the degree to which the 4D rotational state of matter departs from the isotropic ground state along the w-axis of the embedding four-sphere. Specifically:

(i) $\eta = 0$ corresponds to the isotropic rotational ground state: the matter field is in the unique configuration in which its rotational state is spherically symmetric in all planes, including the $wx$, $wy$, and $wz$ planes that connect the three spatial dimensions to the compactified w-direction. This is the condensate vacuum, the state of minimum rotational departure.

(ii) $\eta \neq 0$ measures the magnitude of departure from this ground state specifically along the w-axis: the amount by which the spinor field has rotated out of the isotropic vacuum into a configuration with a net projection onto the w-direction.

(iii) The parameter $m$ in $S_{\text{geo}}$ is the restoring force scale for w-spin departure: it is the coefficient governing the energy cost of maintaining $\eta \neq 0$ in the absence of rotational coherence sources. In this sense, $m$ is the mass of the condensate field, and $\eta \neq 0$ is the physical meaning of rest mass for matter.

## **Proof**

**Step 1 — The geometry of the w-axis.** The S³ manifold identified in P.7.6 as the spatial topology of the universe is a three-sphere embedded in $\mathbb{R}^4$. The four coordinates of the embedding space are $(x, y, z, w)$. Three of these coordinates — $(x, y, z)$ — correspond to the three observable spatial dimensions. The fourth coordinate $w$ is the direction along which the S³ curves back on itself: for a point moving along S³ in what appears to be a spatial direction, the $w$-coordinate changes at a rate determined by the curvature $1/R_{\text{cosmic}}$.

The rotational planes of SO(4) acting on $\mathbb{R}^4$ include the three purely spatial planes $(xy, xz, yz)$, the three purely boost-like planes $(tx, ty, tz)$ in Lorentzian signature, and the three w-planes $(wx, wy, wz)$. The w-planes are the planes that connect the observable spatial dimensions to the compactified fourth dimension. Rotational departure along the w-axis means rotational departure in the three $w$-planes simultaneously.

**Step 2 — The scalar bilinear as w-plane projection.** The Dirac spinor $\psi$ in the representation $(\tfrac{1}{2},0) \oplus (0,\tfrac{1}{2})$ of SU(2) × SU(2) encodes the full rotational state of matter in all planes. Under the decomposition of SO(4) → SO(3) × U(1)$_w$, where SO(3) is the group of purely spatial rotations and U(1)$_w$ encodes the w-plane rotational content, the scalar bilinear $\eta = \bar{\psi}\psi$ projects onto the U(1)$_w$ component.

This follows from the Clifford algebra structure. The scalar bilinear $\bar{\psi}\psi = \psi^\dagger \gamma^0 \psi$ is constructed using the identity element of the Clifford algebra, $\mathbf{1}$. In the standard Dirac representation, $\mathbf{1}$ commutes with all generators of purely spatial SO(3) rotations (which are built from products of spatial gamma matrices $\gamma^i$). It does not commute with the boost generators $\gamma^0 \gamma^i$. In the context of the S³ embedding, the boost direction along the w-axis is the compactified direction; the scalar bilinear therefore measures specifically the departure from the isotropic state along the w-direction.

More concretely: in the rest frame of a matter element with four-velocity $u^\mu$, the spatial components of $\psi$ encode the three-dimensional rotational state (spin), while the scalar bilinear $\eta = \bar{\psi}\psi$ encodes the component of the rotational state that cannot be expressed as a purely spatial rotation — it encodes the w-spin, the rotational departure in the planes that connect the spatial dimensions to the w-direction.

**Step 3 — The mass term as w-spin restoring force.** The mass term in $S_{\text{geo}}$ is:

$$-m\bar{\psi}\psi = -m\,\eta$$

In the effective potential for the condensate field, this term contributes $+m\eta$ to the energy density when $\eta \neq 0$: maintaining w-spin departure costs energy proportional to the departure magnitude $\eta$ times the restoring force scale $m$. The quartic self-coupling $-(\lambda/4)(\bar{\psi}\psi)^2 = -(\lambda/4)\eta^2$ provides a negative-energy term that competes with the mass term and drives spontaneous condensation at $\eta_{\text{eq}} \neq 0$ when $\lambda > 0$. The balance between these two terms sets the equilibrium condensate value $\eta_{\text{eq}}$ and thereby sets the effective mass of matter in the condensate background: $m_{\text{eff}}^2 = m^2 - \lambda\eta_{\text{eq}}^2/2$.

*Note (v15).* Section P.11.2 completes this expansion by including the
previously-unexamined orthogonal direction $P = \bar\psi\gamma^5\psi$,
deriving $m_\eta^2 = 2\lambda\eta_{\text{eq}}^2$ (consistent with the
above to the order retained) and, new to this document, $m_P^2 =
m/\eta_{\text{eq}}$ — the SCH Gell-Mann–Oakes–Renner relation. This is a
completion of Theorem 0 Step 3, not a revision of it.

This is the physical meaning of rest mass in the SCH framework: rest mass is the energy cost of maintaining a nonzero w-spin departure from the isotropic ground state. A particle at rest is not moving through three-dimensional space but it is moving in the w-direction (it is tracing the S³ manifold as the universe rotates), and the energy required to maintain this w-directional rotational state is what we measure as rest mass energy $mc^2$.

**Step 4 — The GR limit as zero w-spin.** When $\eta \to 0$ — either because $T > T_c$ (thermal decoherence melts the condensate) or because the system is in the isotropic ground state $A^\mu = 0$ — there is no w-spin departure. The matter field rotates isotropically in all planes including the w-planes, and the geometric state tensor $C_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu \to 0$. The modified field equation reduces to the standard Einstein equation. GR is the exact limit of zero w-spin. This confirms that w-spin departure is the physical content of the condensate correction to gravity: matter with nonzero w-spin departs from the isotropic state that GR describes and sources additional gravitational effects through $C_{\mu\nu}$.

**Step 5 — Connection to the observational proxy.** The galactic-scale observational proxy $\lambda_R = \langle V \rangle / \sqrt{\langle V^2 \rangle + \langle \sigma^2 \rangle}$ measures the degree to which stellar orbits are coherently rotating rather than isotropically distributed. High $\lambda_R$ corresponds to high w-spin: the stellar matter is in a state of organized rotational departure from isotropy. Low $\lambda_R$ corresponds to low w-spin: the stellar matter is near the isotropic ground state. The prediction of the SCH framework — that higher $\lambda_R$ corresponds to more gravitational excess at fixed stellar mass — is the direct observational signature of higher w-spin sourcing larger $C_{\mu\nu}$.

**Conclusion:** $\eta = \bar{\psi}\psi$ is the w-spin magnitude of the 4D rotational field. It measures the degree of departure from the isotropic gravitational ground state along the compactified w-direction of the S³ manifold. Rest mass is the energy of w-spin departure. GR is the zero-w-spin limit. ∎

---

# **Theorem 5 — c as Tangential S³ Velocity**

## **Statement**

The speed of light $c$ is derived as the tangential surface velocity of the S³ manifold: $c(t) = \omega(t) \cdot R_{\text{cosmic}}(t)$, where $\omega(t)$ is the angular frequency of the S³ at cosmic time $t$ and $R_{\text{cosmic}}(t)$ is its radius. Photons are identified as minimum-w-spin ($\eta \to \eta_{\min} > 0$) surface waves propagating along the three-sphere. They are not zero-w-spin objects — observational evidence from gravitational lensing directly establishes that photons couple to the condensate field: light is deflected by massive bodies. Zero-w-spin would preclude this coupling entirely. The correct identification is minimum nonzero w-spin, not zero w-spin. The constancy of $c$ in local experiments is a consequence of the S³ geometry rather than a postulate.

## **Proof**

**Step 1 — Photons as minimum-w-spin excitations.** The photon, as a massless gauge boson, has rest mass $m_\gamma = 0$. In the SCH framework, rest mass is the energy cost of maintaining w-spin departure against the restoring force scale $m$ (Theorem 0, Step 3). A particle with $m_\gamma = 0$ therefore has a w-spin departure that costs zero energy to maintain — it sits at the minimum of the effective potential for $\eta$ rather than at $\eta = 0$. This minimum is $\eta_{\min}$, the lowest nonzero value of the condensate order parameter consistent with the field equations. The photon's w-spin is minimum but nonzero: it couples to the condensate field weakly but measurably. This is directly confirmed by gravitational lensing: light is deflected by massive condensate concentrations, which requires a nonzero photon-condensate coupling, which requires $\eta_{\text{photon}} > 0$. The identification $\eta_{\text{photon}} = 0$ is falsified by every lensing observation ever made. The correct identification is $\eta_{\text{photon}} = \eta_{\min}$, the minimum nonzero w-spin state.

**Step 2 — The constraint surface for minimum-w-spin objects.** A particle with $\eta = \eta_{\min}$ has a w-spin component that is nonzero but minimal. Its w-directional motion is therefore minimal — approaching zero but not reaching it. In the limit $\eta_{\min} \to 0$, the particle is confined increasingly tightly to the surface of S³: it propagates predominantly tangentially, with only a vanishingly small component of its motion directed inward or outward along the w-axis. In this limit, the tangential speed approaches the full surface velocity of the S³.

The three-sphere S³ of radius $R_{\text{cosmic}}$ rotates with angular frequency $\omega = \dot{\phi}$, where $\phi$ is the angular coordinate around the S³. For an object with $\eta \to \eta_{\min}$ (minimum w-spin, minimum w-directional motion), its speed in the embedding space approaches the tangential velocity of the surface:

$$v_{\text{tangential}} = \omega \cdot R_{\text{cosmic}}$$

This is the speed at which the surface of the S³ is moving in the embedding $\mathbb{R}^4$ at that radius. Massive particles, with $\eta \gg \eta_{\min}$, have substantial w-directional motion and therefore travel at speeds strictly less than $v_{\text{tangential}}$. Photons, with $\eta = \eta_{\min}$, approach the tangential surface velocity asymptotically. In the idealized $\eta_{\min} \to 0$ limit, photons travel exactly at $c = \omega R_{\text{cosmic}}$. The deviation from this for physical photons is of order $\eta_{\min}/\eta_{\text{matter}}$ — unmeasurably small and consistent with all precision measurements of the constancy of $c$.

**Step 3 — Identification with c.** The speed of light is the maximum speed of signal propagation. In the SCH framework, signals propagate either as massive particles (w-spin $\eta \gg \eta_{\min}$, mass $> 0$, speed $< c$) or as photons (minimum w-spin $\eta = \eta_{\min}$, approaching the S³ surface tangential velocity). The tangential surface velocity is the maximum speed because no physical signal can propagate faster than the surface of the manifold on which all physics occurs. Therefore:

$$c(t) = \omega(t) \cdot R_{\text{cosmic}}(t)$$

**Step 4 — Constancy of c in local experiments.** The apparent constancy of $c$ follows from the relationship between $\omega(t)$ and $R_{\text{cosmic}}(t)$. In the cosmological expansion governed by the modified Friedmann equations (CT-viii), $\omega$ and $R_{\text{cosmic}}$ are related by the dynamics of the S³ manifold. In the current epoch, $R_{\text{cosmic}} \sim 4 \times 10^{26}$ m and $\omega \sim c / R_{\text{cosmic}} \sim 7 \times 10^{-19}$ rad/s. The product $\omega \cdot R_{\text{cosmic}}$ is maintained at the constant value $c = 3 \times 10^8$ m/s by the dynamics of the expansion.

For local experiments conducted over timescales $\Delta t \ll H_0^{-1}$ (short compared to the Hubble time), the change in $c(t)$ due to cosmological evolution is:

$$\frac{\Delta c}{c} \sim H_0 \Delta t \sim 10^{-18} \left(\frac{\Delta t}{\text{s}}\right)$$

This is far below the precision of any measurement currently achievable on human timescales. Within any local experiment, $c$ is constant to better than any measurable precision. The apparent constancy is not a postulate but a consequence of the ratio $\omega/R_{\text{cosmic}}$ being stable over the timescales of local physics.

**Step 5 — The photon dispersion relation.** For a minimum-w-spin surface wave on S³, the dispersion relation follows from the wave equation on S³ with $m_\gamma = 0$. In the limit of small wavelength compared to $R_{\text{cosmic}}$ (the geometric optics limit, valid for all photons observed in laboratory and astrophysical settings), the dispersion relation reduces to:

$$E = pc$$

exactly, with $c = \omega R_{\text{cosmic}}$ as derived above. The full dispersion relation on S³ includes curvature corrections of order $(1/k R_{\text{cosmic}})^2$, where $k$ is the wave number. These corrections are entirely negligible for any photon with wavelength much less than the Hubble radius. The standard result $E = pc$ is recovered in the local limit.

**Step 6 — The photon-condensate coupling.** The derivation in Steps 1–5 establishes that photons carry minimum nonzero w-spin $\eta_{\min}$. This has a specific consequence for the interaction of photons with the condensate: photons do couple to $C_{\mu\nu}$, but weakly, in proportion to $\eta_{\min}$. The coupling is not zero — gravitational lensing directly establishes this — but it is suppressed relative to the coupling of massive matter by the ratio $\eta_{\min}/\eta_{\text{matter}}$. This suppression explains why it takes the condensate concentration of a star or galaxy to produce a measurable photon deflection, while the same condensate produces large effects on massive matter at much lower concentrations. The photon-condensate cross section $\sigma(\omega)$ governing this coupling is derived in CT-xiii. The coupling also produces a cumulative strataract drag on photons traversing cosmological distances, contributing to the observed redshift of distant sources (Paper A Section 6.9.0) and to the Olbers mechanism and CMB monopole conjectures (Paper A Sections 6.9.1 and 6.9.2). ∎

## **Corollary 5.1 — Massive particles move at speeds less than c**

A particle with w-spin $\eta \gg \eta_{\min}$ has a substantial component of its state along the w-direction. This component is not tangential to the S³ surface; it is directed inward along the w-axis. An object with significant w-directional motion cannot simultaneously travel at the full tangential surface velocity $c$, because its total four-velocity must be normalized: $u^\mu u_\mu = -c^2$. Splitting the motion between tangential (spatial) and w-directional (rest mass) components means the tangential speed is strictly less than $c$. The maximum tangential speed approaches $c$ only in the limit $\eta \to \eta_{\min}$ — the photon limit of minimum w-spin and zero rest mass. This is the derivation of the speed limit $v < c$ for massive particles from S³ geometry and Theorem 0. The photon is not an exception to this limit; it is the limit itself.

---

# **Theorem 6 — The Matter-Light Phase Transition**

## **Statement**

The states $\eta = \eta_{\min}$ (minimum w-spin; photons, massless particles) and $\eta \gg \eta_{\min}$ (substantial w-spin; massive matter) are not points on a smooth continuum of rotational states. They are topologically distinct phases of the rotational field, separated by a phase boundary that is stable under perturbations. The transition between the matter phase ($\eta \gg \eta_{\min}$) and the light phase ($\eta \to \eta_{\min}$) is a first-order phase transition in the condensate order parameter $\eta$. The phase boundary is not at $\eta = 0$ exactly — the photon's minimum nonzero w-spin places it just above the boundary — but the boundary itself is at $\eta = 0$, the true isotropic ground state that no physical particle occupies.

## **Proof**

**Step 1 — The effective potential for η.** From the action $S_{\text{geo}}$, the effective potential for the condensate order parameter $\eta$ in the mean-field approximation is:

$$V_{\text{eff}}(\eta) = \frac{m^2}{2}\eta - \frac{\lambda}{4}\eta^2 + \text{higher order}$$

(written in terms of $\eta = \bar{\psi}\psi$ rather than $|\psi|^2$, so $\eta$ ranges over $\mathbb{R}$). The quartic coupling $\lambda > 0$ ensures that $V_{\text{eff}}$ has a nontrivial minimum at $\eta_{\text{eq}} = m^2/\lambda > 0$ for $T < T_c$. The potential is not symmetric in $\eta \to -\eta$ at the physical level (negative $\eta$ corresponds to a chirality-reversed condensate, addressed in P.7.7). At $T > T_c$, the only minimum is $\eta = 0$.

*Note (v15).* Section P.11.2 exhibits the full $(\eta,P)$-plane
potential of which this is the $\eta$-axis restriction, and identifies
the symmetry this section's spontaneous breaking actually corresponds
to: the chiral rotation $\psi\to e^{i\alpha\gamma^5}\psi$, under which
$(\eta,P)$ rotate into each other. The mass term $-m\eta$ that breaks
the $\eta\to-\eta$ symmetry referenced above is the same term that
explicitly (not just spontaneously) breaks this chiral symmetry,
producing a pseudo-Goldstone rather than an exact Goldstone mode in the
$P$ direction — see Section P.11 for the consequences.

**Step 2 — The barrier at η = 0.** Consider the effective potential as a function of temperature $T$. At $T < T_c$:

- The global minimum is at $\eta = \eta_{\text{eq}}(T) > 0$ (the condensate phase — matter).
- The local extremum at $\eta = 0$ is not a minimum but a saddle point of $V_{\text{eff}}$: $\partial^2 V_{\text{eff}}/\partial\eta^2|_{\eta=0} = m^2 > 0$ at one-loop order but the potential curves toward $-\infty$ as $|\eta|$ increases until the quartic term dominates. The energy barrier between $\eta = 0$ and $\eta = \eta_{\text{eq}}$ is the condensation energy $\Delta F = V_{\text{eff}}(0) - V_{\text{eff}}(\eta_{\text{eq}}) > 0$.

At $T > T_c$:

- The only minimum is $\eta = 0$ (the decoherent phase — light/photons and thermalized matter).
- The condensate is melted; all matter fields are in the zero-w-spin decoherent phase.

**Step 3 — The phase boundary is topologically stable.** The matter phase ($\eta = \eta_{\text{eq}} \neq 0$) and the light phase ($\eta = 0$) are separated not merely by an energy barrier but by a topological distinction. The matter phase spontaneously breaks the U(1) symmetry $\psi \to e^{i\theta}\psi$ of $S_{\text{geo}}$ (corresponding to w-spin orientation), while the light phase preserves this symmetry. The order parameter $\eta = \bar{\psi}\psi$ is nonzero in the broken phase and zero in the symmetric phase. By Landau's theorem on symmetry-breaking phase transitions, the broken-symmetry phase and the symmetric phase are separated by a genuine phase transition at $T = T_c$ rather than a smooth crossover. The two phases are topologically distinct in the sense that no continuous deformation of the order parameter can connect them without crossing $\eta = 0$.

*Note (v15).* As Section P.11.1 makes explicit, $\eta=\bar\psi\psi$ is
in fact invariant under this vector phase rotation $\psi\to
e^{i\theta}\psi$ ($\bar\psi\to\bar\psi e^{-i\theta}$ leaves
$\bar\psi\psi$ unchanged); the symmetry the condensate actually breaks
is the chiral rotation $\psi\to e^{i\alpha\gamma^5}\psi$ acting on the
$(\eta,P)$ pair. This is a precision correction to the symmetry
identification in this step; the topological conclusion of Step 3
(broken phase and symmetric phase separated by a genuine transition,
not a crossover) is unaffected, since the chiral rotation is likewise
spontaneously broken by $\eta_{\text{eq}}\neq0$ and explicitly broken by
$m\neq0$, and the same Landau argument applies to it directly.

**Step 4 — First-order character of the transition.** The Matsubara analysis (Theorem 3, P.4) establishes that $V_{\text{eff}}(\eta, T)$ has a first-order structure at the transition: both the condensate phase ($\eta = \eta_{\text{eq}}$) and the decoherent phase ($\eta = 0$) coexist at $T = T_c$ before the first-order jump occurs. The latent heat of the transition is $L = T_c \cdot \partial\eta_{\text{eq}}/\partial T|_{T_c}$. The first-order character is a consequence of the cubic term generated in $V_{\text{eff}}(\eta, T)$ by thermal fluctuations at one loop, which preempts the continuous second-order transition that would be predicted by the tree-level potential alone.

The first-order character is physically significant: the transition between matter and light is not a smooth process but a sudden jump. A photon cannot gradually acquire rest mass by a smooth increase in $\eta$; it must cross the phase boundary discontinuously. This is the mechanism behind pair production (matter-antimatter pairs created from photon energy) and annihilation (matter-antimatter pairs converting to photons): these are first-order phase transitions at the level of the individual quantum field, mediated by the condensate.

**Step 5 — The bounce as epoch-boundary phase transition.** The cosmological bounce (P.7.4, P.7.5) reaches Planck densities at which Term 3 dominates and the condensate is driven to extreme values. The collapse phase drives $\eta \to 0$ at the bounce point (maximum compression, maximum thermalization, condensate melted by $T \gg T_c$), followed by re-expansion during which the condensate reconstitutes ($\eta$ grows from 0 to $\eta_{\text{eq}}$) as the temperature falls below $T_c$. The matter-creation epoch of the early universe — the epoch in which matter separates from light — is identified with the phase transition $\eta: 0 \to \eta_{\text{eq}}$ during cosmic cooling after the bounce. This is not a gradual separation of matter from radiation but a phase transition at a definite epoch $T = T_c$.

**Step 6 — Implications for the contrast class.** The first-order phase transition between matter and light provides the formal underpinning for the contrast class established in Papers A and B. Systems in the matter phase ($\eta \neq 0$) participate in the condensate sourcing of gravity through $C_{\mu\nu}$. Systems in the light phase ($\eta = 0$, or thermalized matter at $T > T_c$) do not. The intracluster gas in the Bullet Cluster is driven toward the $\eta \approx 0$ phase by shock heating ($T \gg T_c$); the stellar matter remains in the $\eta \neq 0$ phase (thermally isolated from the ICM on relevant timescales). The lensing offset between gas and galaxies is a direct consequence of the phase distinction established in this theorem. ∎

## **Corollary 6.1 — The matter-light distinction is not a speed continuum**

It follows from Theorem 6 that the distinction between matter and light is not that matter moves slowly and light moves fast, or that matter has a small $\eta$ and light has a slightly smaller one. Matter and light are in different phases of the condensate field, separated by a topological boundary. The speed-of-light limit for matter (Corollary 5.1) is a consequence of this phase distinction, not the definition of it. A particle moves at $v < c$ not because of a cosmic speed limit but because it is in the $\eta \neq 0$ phase, which means it has a w-spin component that occupies part of its four-velocity, leaving a spatial speed strictly below $c$.

---

# **P.1 The Fundamental Action and Lagrangian Density**

## **P.1.1 Total Action**

The total action on spacetime manifold M, in terms of the tetrad $e^a_{\mu}$ and spin connection $\omega^{ab}_{\mu}$, is:

$$S_{\text{total}} = S_{\text{EC}}[e,\omega] + S_{\text{geo}}[e,\omega,\psi] + S_{\text{GHY}}[e] + S_{\text{matter}}[e,\psi]$$

where:

- $S_{\text{EC}} = \dfrac{1}{2\kappa}\int d^4x\,e\,R(e,\omega)$ — Einstein–Cartan gravity; tetrad + spin connection
- $S_{\text{geo}} = \int d^4x\,e\left[\tfrac{i}{2}(\bar{\psi}\gamma^a e^a_{\mu} D_\mu\psi - \text{h.c.}) - m\bar{\psi}\psi - \tfrac{\lambda}{4}(\bar{\psi}\psi)^2\right]$ — Geometric state spinor; Dirac + quartic self-coupling
- $S_{\text{GHY}} = \dfrac{1}{\kappa}\int d^3x\,\sqrt{h}\,K$ — Gibbons–Hawking–York boundary term
- $S_{\text{matter}}$: Standard Model fields, minimally coupled — Ordinary matter; $T_{\mu\nu}$ source

By P.0b, $S_{\text{geo}}$ is the unique leading-order action for the unique minimal rotational encoder $\psi$ in 4D curved spacetime. By Theorem 0, the mass parameter $m$ is the w-spin restoring force scale. By Theorems 5 and 6, the action admits two phases of its condensate solution: the matter phase $(\eta \neq 0)$ and the light phase $(\eta = 0)$.

## **P.1.2 Explicit Lagrangian for $S_{\text{geo}}$**

$$S_{\text{geo}} = \int_M d^4x\,e\left[\frac{i}{2}\left(\bar{\psi}\gamma^a e^a_{\mu} D_\mu\psi - D_\mu\bar{\psi}\gamma^a e^a_{\mu}\psi\right) - m\bar{\psi}\psi - \frac{\lambda}{4}(\bar{\psi}\psi)^2\right]$$

where the Fock–Weyl covariant derivative is $D_\mu\psi = \partial_\mu\psi + \tfrac{1}{4}\omega_\mu^{ab}[\gamma_a,\gamma_b]\psi$. The parameter $\lambda > 0$ governs the quartic self-interaction and sets the condensate scale. By Theorem 6, $\lambda > 0$ is the necessary and sufficient condition for a first-order matter-light phase transition; $\lambda \leq 0$ would give no condensate and no matter phase, only the light phase everywhere.

## **P.1.3 Variational Equations**

Variation with respect to the tetrad $e^a_{\mu}$ yields:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa\left[T_{\mu\nu}^{\text{matter}} + \alpha C_{\mu\nu} + T_{\mu\nu}^{\text{torsion}}\right]$$

where $C_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu$ is the leading-order geometric state tensor (w-spin sourcing) and $T_{\mu\nu}^{\text{torsion}} \sim A_\mu A_\nu - \tfrac{1}{2}A_\rho A^\rho g_{\mu\nu}$.

Variation with respect to the spin connection $\omega^{ab}_{\mu}$ gives the Cartan equation:

$$T_{\lambda\mu\nu} = \frac{\kappa\alpha}{2}\,\varepsilon_{\lambda\mu\nu\rho}\,A^\rho$$

This is an algebraic equation: torsion is instantaneously determined by the local axial current. There is no differential propagation equation for torsion. This distinction is the foundation of Theorem 4 (P.5, now Theorem 4a/4b — Section P.11) and the black hole bounce analysis of P.7.5. It is also the starting point for the entire chirality-sector derivation of Section P.7.7 below, where $T_{\lambda\mu\nu}$ is a totally antisymmetric rank-3 tensor in all four internal Lorentz indices taken together with $\varepsilon_{\lambda\mu\nu\rho}A^\rho$.

---

# **P.2 Gap 1 — Leading-Order Uniqueness of $Q_{\mu\nu}$**

**Theorem 1 (Leading-Order Uniqueness)**

At quadratic order in $\psi$, in the low-density EFT regime ($\rho \ll \rho_c$), subject to the symmetries of $S_{\text{geo}}$, $Q_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu$ is the unique rank-2 symmetric divergence-free tensor constructible from local spinor bilinears of $\psi$. Uniqueness holds modulo: (i) an overall coupling constant $\alpha$; (ii) subleading higher-order corrections suppressed by $\varepsilon(\rho) \leq 10^{-23}$ at galactic densities.

Three sequential filters — rank-2 symmetry (F1), divergence-free (F2), quadratic in $\psi$ (F3) — reduce the complete Fierz bilinear basis of ten candidates to the unique survivor: $C_3 = \rho(\bar{\psi}\psi)u_\mu u_\nu = Q_{\mu\nu}$. The overall coupling constant $\alpha$ must be determined experimentally (the Bi-209 calibration).

---

# **P.2a The Density Hierarchy: Bounding Higher-Order Contributions**

The expansion parameter $\varepsilon(\rho) = \rho/\rho_c$ is bounded as follows:

$$\varepsilon(\rho_{\text{galactic}}) = \frac{\rho_{\text{galactic}}}{\rho_c} \leq \frac{10^{-23}}{10^{-1}} = 10^{-23}$$

At galactic densities, quartic corrections to $Q_{\mu\nu}$ are suppressed by a factor of $10^{-23}$. Term 3 becomes competitive at $\rho \sim \rho_c \sim 10^{-1}$ g/cm$^3$, encompassing neutron star cores and Planck-scale cosmology.

---

# **P.3 Gap 2 — Four-Velocity Normalization**

**Theorem 2 (Regime-Conditional Normalization)**

For the geometric state spinor $\psi$ satisfying the field equations of $S_{\text{geo}}$, the normalized current $u^\mu = J^\mu/(\bar{\psi}\psi)$ satisfies $u^\mu u_\mu = -c^2$ in the parity-preserving vacuum sector of $S_{\text{geo}}$, for all spinor configurations satisfying the equations of motion in that sector, within the low-density regime ($\rho \ll \rho_c$).

Proof via Fierz identity: $J^\mu J_\mu = -S^2 - P^2$. Parity symmetry enforces $P = \bar{\psi}\gamma^5\psi = 0$, giving $u^\mu u_\mu = -c^2$.

*Note (v15).* The parity-preserving condition $P=0$ assumed here is now
independently derived, rather than merely assumed, in Section P.11.2:
the tree-level effective potential's minimum sits at $P_{\text{eq}}=0$
precisely because the explicit chiral-breaking term $-m\eta$ tilts the
$(\eta,P)$-plane potential onto the $\eta$ axis. Theorem 2 is thereby
strengthened, not altered.

---

# **P.4 Gap 3 — Derivation of $\Gamma_{\text{decoh}}$ and $\Gamma_{\text{recoh}}$**

**Theorem 3 (Rate Derivation)**

$\Gamma_{\text{decoh}} = (\alpha/m^2)(\lambda\rho)^2\kappa(T)$ and $\Gamma_{\text{recoh}} = (\alpha/m^2)(\lambda\rho)^2\kappa(T)f(T)$, where $\kappa(T) = d^2V_{\text{eff}}/d\eta^2$ evaluated at $\eta_{\text{eq}}(T)$ and $f(T) = \eta_{\text{eq}}(T)/\eta_{\text{max}}$. Both rates are fixed by action parameters $\{\alpha, \lambda, m\}$ and temperature $T$. No free parameters remain.

Derived from $S_{\text{geo}}$ via the finite-temperature effective potential computed by the Matsubara formalism.

*Note (v15).* $\Gamma_{\text{decoh}}$ is evaluated at $\omega=k=0$ — the
homogeneous relaxation rate entering Paper A's $\eta$ evolution
equation (Section 2.4a), which has no spatial gradient term. Section
P.11.3 evaluates the same finite-temperature self-energy at its
$O(\omega)$ imaginary slope, giving the distinct (though
parametrically related) transport damping rates $\gamma_\eta,\gamma_P$
relevant to spatial propagation of Term 2. Theorem 3 itself requires no
revision; it is one extraction of the underlying self-energy function
among several now identified.

---

# **P.5 Gap 4 — Torsion Persistence and Post-Merger Lensing**

**Superseded notice (v15).** Theorem 4's transport claim — the
formula $\tau_{\text{diff}}\sim R^2m_{\text{eff}}/\hbar$ — was never
derived from a linearized field equation and is retracted. Its
ontological claim (Term 2 is propagating, not a contact interaction) is
retained and independently re-derived with additional structure in
**Section P.11**, as **Theorem 4a** (carrier structure: two channels,
not one) and **Theorem 4b** (transport regimes: derived damped-wave
equation, not an asserted diffusion formula). Theorem 4 is superseded
in full by Theorems 4a and 4b. The original text is retained below for
the historical record.

**Theorem 4 (Term Distinction)**

Term 2 ($C_{\mu\nu} = \rho\,\eta\,u_\mu u_\nu$) is a propagating field effect governed by the Dirac equation for $\psi$. It persists and diffuses after matter moves. Diffusion timescale: $\tau_{\text{diff}} \sim R^2 m_{\text{eff}}/\hbar$. Term 3 ($\sim A_\mu A_\nu - \tfrac{1}{2}A_\rho A^\rho g_{\mu\nu}$) is a contact interaction. Torsion is algebraically determined by the Cartan equation and does not propagate.

---

# **P.6 Closure Summary**

| **Challenge** | **Status** | **Resolution / Reference** |
| --- | --- | --- |
| Lagrangian architecture | **CLOSED** | $S_{\text{geo}}$ is the Einstein-Cartan-Dirac action with quartic spinor coupling. Metric variation gives the field equation exactly. (P.1) |
| Tensor emergence ($Q_{\mu\nu}$) | **CLOSED (leading order)** | Theorem 1: $Q_{\mu\nu}$ unique at quadratic order via Fierz completeness + three filters. Density hierarchy bound $\varepsilon \leq 10^{-23}$. (P.2, P.2a) |
| $\eta$ scalar nature | **CLOSED** | $\eta = \bar{\psi}\psi$ is a Lorentz scalar bilinear; proven from spinor transformation law under SL(2,C). (P.3 — Theorem 2) |
| GR recovery | **CLOSED** | $A^\mu = 0$ in isotropic ground state makes torsion vanish algebraically. Exact GR. (P.1) |
| Geometric Resonance Postulate | **CLOSED** | Ground state = spinor vacuum = $A^\mu = 0$ = zero net chirality. Derived from SU(2) × SU(2) covering group. (P.1) |
| $\Gamma_{\text{decoh}}$, $\Gamma_{\text{recoh}}$ | **CLOSED (regime-conditional)** | Theorem 3: both rates derived from $S_{\text{geo}}$ via Matsubara + EFT kinetics. Fixed by $\{\alpha, \lambda, m, T\}$. (P.4) |
| $u^\mu$ normalization | **CLOSED (regime-conditional)** | Theorem 2: $u^\mu u_\mu = -c^2$ in parity-preserving vacuum sector, $S \neq 0$, $\rho \ll \rho_c$. Parity-preserving condition now independently derived (P.11.2). (P.3) |
| Torsion / lensing persistence — carrier structure | **CLOSED** | Theorem 4a: Term 2 carried by two generically nondegenerate channels ($\delta\eta$, $\delta P$), related by the chiral rotation the condensate breaks, satisfying the SCH GMOR relation. (P.11.1–P.11.2, P.11.4) |
| Torsion / lensing persistence — transport regime | **OPEN** | Theorem 4b: transport is a derived damped relativistic wave equation, dissipationless in vacuum, diffusive in dense media, with per-channel damping rates $\gamma_\eta,\gamma_P$ undetermined numerically. Superseded formula: $\tau_{\text{diff}}\sim R^2m_{\text{eff}}/\hbar$ (Theorem 4, retracted). Gated on CT-vii(a–c). (P.11.3–P.11.6) |
| Density hierarchy | **CLOSED** | $\varepsilon(\rho) = \rho/\rho_c \leq 10^{-23}$ at galactic scales. Quartic corrections negligible. (P.2a) |
| BH bounce resonance (mechanism) | **CLOSED** | Term 3 at Planck density → bounce. Term 2 propagates outward — mechanism established (Theorem 4a). Q effectively infinite. (P.7.5) |
| BH bounce resonance (propagation frequency) | **OPEN (v15)** | The quantitative frequency table (P.7.5.2) used the retracted formula; suspended pending CT-vii(a–c). (P.11.5) |
| S³ topology | **CLOSED** | SU(2) group manifold = S³. Spinor field on SU(2) × SU(2) selects S³ canonically via spin structure. (P.7.6) |
| Chirality inversion across bounce / sympathetic nucleation | **CLOSED (mechanism); numerical evaluation pending Bi-209** | Confirmed non-generic across three independent derivation routes at coefficient $-\tfrac{3\kappa\alpha}{2}$. (P.7.7) |
| Photon-condensate coupling / CMB monopole | **OPEN TARGET** | CT-xiii identified. Prerequisites: CT-vii + CT-viii. (P.8) |
| Physical primitive: $\psi$ as derived object, not ansatz | **CLOSED** | P.0b: $\psi$ is the unique minimal 4D rotational encoder (enumeration + elimination). $S_{\text{geo}}$ follows as consequence. |
| W-spin as mass: $\eta$ as physical rotational departure | **CLOSED** | Theorem 0: $\eta = \bar{\psi}\psi$ is the w-spin magnitude; rest mass is the energy cost of w-spin departure from the isotropic ground state. Completed by the two-field expansion of P.11.2. |
| $c$ as tangential S³ velocity: speed of light derived | **CLOSED** | Theorem 5: $c(t) = \omega(t) \cdot R_{\text{cosmic}}(t)$. Photon as minimum-w-spin surface wave. Constancy of $c$ from S³ geometry. |
| Matter-light phase transition: topological distinctness | **CLOSED** | Theorem 6: $\eta = 0$ and $\eta \neq 0$ are phases separated by a first-order topological boundary, not points on a speed continuum. Symmetry identification precision-corrected in P.11.1 (chiral, not vector, rotation). |
| FLRW reduction: modified Friedmann equations and bounce | **CLOSED** | CT-viii: Friedmann equations derived, two-branch cosmology, bounce condition, GR recovery, kinetic coefficient corrected. See P.9. Two clean-room-flagged subsidiary claims (P.9.4.2, P.9.5.3) remain independently unverified — see note at end of P.9. |
| Antipodal condensate coupling: local BH emission → global $S^3$ modes | **OPEN TARGET** | CT-xix identified. Prerequisites: CT-vii + CT-viii. CT-viii closed; CT-vii open. Plausibly aided by ballistic light-channel propagation (P.11.3), unconfirmed. (P.8) |
| Thermodynamic consistency of coherence-forcing mechanism | **OPEN TARGET** | CT-xx identified. Prerequisites: CT-xix + Bi-209 calibration. |
| Cosmological dynamics: Branch 1 and Branch 2 solution structure | **CLOSED (Branch 1 full; Branch 2 mechanism established, magnitude pending Bi-209)** | CT-ix: Branch 1 two-phase dynamics, $R_{\text{universe}}$, CMB constraint. Branch 2 now a coupled three-variable system with confirmed self-sourcing coefficient. Confirmed unaffected by the v15 Theorem 4 split — homogeneous-background dynamics, not local fluctuation transport. (P.10) |
| Term 2 carrier structure | **CLOSED (v15)** | Theorem 4a. Two nondegenerate channels, SCH GMOR relation derived. (P.11.1, P.11.2, P.11.4) |
| Term 2 transport regime | **OPEN (v15)** | Theorem 4b. Derived damped relativistic wave equation; numerical damping rates and mass ratio pending CT-vii(a–c). (P.11.3, P.11.4, P.11.6) |

**FINAL STATUS (v15):** A self-consistent variational closure has been
established within the stated EFT and mean-field condensate regime. All
leading-order claims are regime-conditional on $\rho \ll \rho_c$ and
$T < T_c$. The Strataract Completion Hypothesis is a self-consistent
variational EFT rooted in the Einstein-Cartan-Dirac action. GR is the
exact torsion-free limit ($\eta = 0$, $A^\mu = 0$). All galactic-scale
claims hold in the regime $\rho \ll \rho_c$. The ground-floor derivation
(P.0b, Theorems 0, 5, 6) establishes $\psi$ as a derived necessary
object, $\eta$ as w-spin magnitude, $c$ as the S³ surface velocity, and
matter-light as a first-order phase distinction. The chirality/Branch-2
sector, frozen since v13.1, was closed in v14: the torsion self-coupling
coefficient is triply confirmed at $-\tfrac{3\kappa\alpha}{2}$,
chirality inversion per cycle remains confirmed non-generic, and the
Branch 2 late-time approach to Branch 1 behavior is a calculable
(though not yet numerically evaluated) correction rather than an open
question of unknown size. **New in v15:** the Theorem 4 split
establishes that Term 2's carrier structure is closed (two
nondegenerate channels, GMOR relation derived) while its transport
regime is reopened as a distinct, better-posed question — a derived
damped relativistic wave equation replacing an unjustified diffusion
formula — pending CT-vii(a–c). No numerical transport claim from any
prior version of Appendix P (in particular, the black hole condensate
frequency table of P.7.5.2) should be treated as established until
those sub-targets are complete. CT-xix and CT-xx remain open targets,
unaffected by either closure.

---

# **P.7 New Predictions from the Torsion Route**

The quadratic torsion term (Term 3), absent from GR, generates predictions that distinguish Einstein-Cartan-SCH from both GR and the Paper A weak-field formulation. All Term 3 predictions operate in the high-density regime $\rho \sim \rho_c$, consistent with the density hierarchy of P.2a.

## **P.7.1 Spin-Spin Repulsion at High Density**

The term $2A_\mu A_\nu - A_\rho A^\rho g_{\mu\nu}$ acts as repulsive pressure when matter with aligned chirality overlaps. At neutron star densities ($\rho \sim 10^{14}$ g/cm$^3 \gg \rho_c$) this becomes significant, providing a natural upper bound on compactness. At galactic densities this term is suppressed by $\varepsilon \leq 10^{-23}$ and does not contaminate the galactic-scale observational programme.

## **P.7.2 Parity-Dependent Lensing Asymmetry**

Two otherwise identical galaxies with opposite orbital angular momentum generate identical $C_{\mu\nu}$ (since $\eta = \bar{\psi}\psi$ is parity-even) but opposite torsion. Their Term 2 lensing signals are equal; their Term 3 contributions differ. Chirality-dependent lensing asymmetry between mirror-image galaxy pairs is a clean prediction with no analogue in standard GR.

## **P.7.3 Bismuth-209: Second Measurement Channel**

The transmutation Bi-209 → Pb-208 involves nuclear spin collapse from $I = 9/2$ to $I = 0$. The spin-9/2 state has $A^\mu \neq 0$; the spin-0 state has $A^\mu = 0$. Both $\eta$ (Term 2 channel, calorimetrically accessible) and torsion (Term 3 channel, distinct timing signature) change at the transmutation. The two signals have different temporal profiles separable by high-resolution coincidence timing.

In the language of Theorem 0: the transmutation event is a reduction of w-spin from maximum (Bi-209, one unpaired proton at the nuclear geometric tension point) toward minimum (Pb-208, doubly magic, near-isotropic). The w-spin energy released at the transition is the signal measured in Channels A and B of the calibration experiment.

## **P.7.4 Big Bounce Cosmology**

At Planck-scale densities, Term 3 $\sim \kappa^2\alpha^2 A^2/4$ grows as $\rho^2$ and becomes cosmologically significant. The spin-spin repulsion provides a candidate bounce mechanism avoiding the Big Bang singularity. In the language of Theorem 6, the bounce drives the condensate through the $\eta = 0$ phase boundary: at the moment of maximum compression, $T \gg T_c$ and the condensate melts ($\eta \to 0$); during re-expansion, $T$ falls below $T_c$ and the condensate reconstitutes ($\eta \to \eta_{\text{eq}}$) through the first-order phase transition. The matter-creation epoch is this re-condensation event. Full demonstration requires the FLRW reduction (CT-viii).

## **P.7.5 Black Hole Bounce Resonance and Condensate Propagation Frequency**

### **P.7.5.1 The Two-Frequency Structure**

A black hole interior reaching Planck density sits firmly in the Term 3 dominant regime ($\rho \sim 10^{96}$ g/cm$^3 \gg \rho_c$). Term 3 spin-spin repulsion grows as $\rho^2$, reversing the collapse when the Planck threshold is reached. Since the collapsed matter remains gravitationally bound within the event horizon, it re-collapses and the process repeats. Two physically distinct frequencies characterize this system.

The internal bounce frequency is set by the Planck time:

$$f_{\text{internal}} \sim \frac{1}{t_{\text{Planck}}} \sim \frac{1}{5.4\times10^{-44}\text{ s}} \sim 10^{43}\text{ Hz}$$

This frequency is entirely inaccessible to external observers due to gravitational time dilation at the Schwarzschild radius. The black hole presents a static surface to any external measurement.

The condensate propagation frequency is set by the diffusion timescale of the spinor condensate Term 2 field propagating outward from the Schwarzschild radius $R_s = 2GM/c^2$:

$$\tau_{\text{diff}}(R_s) = \frac{R_s^2\,m_{\text{eff}}}{\hbar} = \frac{4G^2M^2\,m_{\text{eff}}}{\hbar c^4}$$

$$f_{\text{cond}} = \frac{1}{\tau_{\text{diff}}} = \frac{\hbar c^4}{4G^2\,m_{\text{eff}}\,M^2}$$

This scales as $M^{-2}$: larger black holes drive slower condensate waves.

*Note (v15).* This subsection's formula for $\tau_{\text{diff}}$ is the
retired Theorem 4 formula; see the retraction notice at P.7.5.2 below
and Section P.11.5. The internal bounce frequency $f_{\text{internal}}$
above is unaffected — it is a distinct quantity, defined independently
of Term 2's transport law.

### **P.7.5.2 Numerical Evaluation**

**Retraction notice (v15).** This table was computed via
$f_{\text{cond}} = 1/\tau_{\text{diff}}(R_s)$ using Theorem 4's formula
$\tau_{\text{diff}} \sim R_s^2m_{\text{eff}}/\hbar$, now retracted
(Section P.11). The Schwarzschild radius $R_s$ is, for every
astrophysical black hole, plausibly deep in the ballistic propagation
regime of Theorem 4b — a distance far below any plausible
$c/\gamma_\phi$ — meaning the correct scaling law is of order $c/R_s$,
not $M^{-2}$. **Every entry in the table below is void, not merely
mislabeled, and the mass-scaling exponent itself is not currently
established.** Recomputation is CT-vii(c) (P.11.6). Downstream claims
depending on this table — Paper B Section 7.1 (NANOGrav), Paper A
Section 2.11 and Paper B Section 7.4 (rotation curve flattening
wavelength $\lambda_{\text{cond}} \sim M^2$) — are suspended pending
recomputation, not provisionally retained. The table is retained below
unedited, for the historical record only.

Using the estimate $m_{\text{eff}} \sim \hbar/(\tau_{\text{coh}}\,c^2)$ with $\tau_{\text{coh}} \sim 400$ ps (Pb-208 first excited state lifetime):

$m_{\text{eff}} \sim 1.6\times10^{-6}$ eV$/c^2$ (sub-meV, consistent with long-range condensate)

| **Black hole mass** | **$f_{\text{cond}}$ (dimensional estimate)** | **Frequency band** |
| --- | --- | --- |
| 3 $M_\odot$ (stellar) | ~0.5 Hz | LIGO band |
| 30 $M_\odot$ (stellar) | ~$5 \times 10^{-3}$ Hz | Below LIGO, above NANOGrav |
| $10^4$ $M_\odot$ (intermediate) | ~$5 \times 10^{-9}$ Hz | NANOGrav nHz band |
| $4 \times 10^6$ $M_\odot$ (Sgr A*) | ~$10^{-13}$ Hz | Period ~$3 \times 10^5$ yr |
| $6.5 \times 10^9$ $M_\odot$ (M87*) | ~$4 \times 10^{-20}$ Hz | Cosmological timescale |

All numerical values are provisional and scale with $m_{\text{eff}}$. The Bi-209 calibration pins $m_{\text{eff}}$. **(v15: and, per the retraction above, the table additionally awaits CT-vii(a–c) before any of its entries can be trusted at all, independent of the Bi-209 value of $m_{\text{eff}}$.)**

### **P.7.5.3 The Quality Factor**

$$Q \sim \exp\!\left(\frac{m_{\text{eff}}\,c^2}{k_B\,T_{\text{Hawking}}}\right)$$

For all astrophysical black holes, $Q$ is effectively infinite. Black holes are the most perfect condensate resonators in the universe by many orders of magnitude.

Open stability question: backreaction and self-excitation. A full perturbative stability analysis of the condensate field around a Schwarzschild background is CT-vii.

### **P.7.5.4 Galactic Structure Implications**

At scales much smaller than the condensate wavelength $\lambda_{\text{cond}} = c/f_{\text{cond}}$, the oscillation appears as an enhanced static $C_{\mu\nu}$. This is the mechanism behind the anomalous gravitational sourcing described in Paper A Sections 1.1 and 1.2. The prediction distinguishing condensate-driven $C_{\mu\nu}$ from smooth dark matter halos: the anomalous sourcing profile should show non-monotonic radial structure correlated with the central black hole mass, rather than smooth NFW or Einasto profiles. *(v15: the specific wavelength scaling $\lambda_{\text{cond}}\sim M^2$ inherits the retraction of P.7.5.2; the qualitative non-monotonic-structure prediction is unaffected.)*

### **P.7.5.5 The NANOGrav Connection**

The condensate hum interpretation of the NANOGrav 2023 background is developed in Paper B Section 7.1. The condensate hum predicts persistent coherent sources at frequencies $f_{\text{cond}} \sim M^{-2}$, distinguishable from stochastic merger backgrounds by their coherence time. *(v15: the frequency-band placement is suspended pending CT-vii(c); the coherence-time discriminator itself, being independent of the specific frequency value, is unaffected.)*

---

## **P.7.6 S³ Spatial Topology: Derivation from the Spinor Covering Group**

### **P.7.6.1 The Group Manifold Identification**

**Lemma P.7.6.1** ($\mathrm{SU}(2) \cong S^3$): $\mathrm{SU}(2)$ is diffeomorphic to the three-sphere $S^3$ as a smooth manifold. Explicitly: $\mathrm{SU}(2) = \{(a,b)\in\mathbb{C}^2 : |a|^2 + |b|^2 = 1\}$, homeomorphic to the unit sphere in $\mathbb{R}^4$.

### **P.7.6.2 The Spin Structure Argument**

$S^3$ is the unique compact topology on which the spin structure canonically determined by the $\mathrm{SU}(2)\times\mathrm{SU}(2)$ covering group is already present without additional input. This is a compatibility and uniqueness argument within the class of compact orientable three-manifolds admitting spin structures. The physical claim: the correct topology is the one that requires no additional structure beyond what $S_{\text{geo}}$ already provides.

The connection to Theorem 5 is direct: $S^3$ is also the manifold on which $c(t) = \omega(t) R_{\text{cosmic}}(t)$ is the natural velocity scale, confirming that the speed of light is a property of the S³ geometry rather than an independent postulate.

### **P.7.6.3 Physical Consequences**

(1) Quantized condensate modes: the mode spectrum on S³ has a topological cutoff at wavelength $\sim 2\pi R_{\text{universe}}$, explaining the CMB quadrupole and octopole suppression.

(2) Angular diameter distance turnaround: $d_A = R_{\text{universe}} \sin(d_{\text{proper}}/R_{\text{universe}})/(1+z)$, with maximum at $d_{\text{proper}} = (\pi/2)R_{\text{universe}}$.

(3) Condensate resonant cavity: condensate waves cannot dissipate to infinity; the universe is a resonant cavity for the condensate field.

(4) Antipodal correlation signature: positive correlation between antipodal sky pixel pairs $T(\mathbf{n}) \times T(-\mathbf{n})$ above the ΛCDM baseline (Paper B Section 7.2).

### **P.7.6.4 Constraint on $R_{\text{universe}}$**

CMB quadrupole suppression: $R_{\text{universe}} \geq 3 \times R_{\text{Hubble}}$. Angular diameter distance turnaround at $z_{\text{turn}} \sim 2$–8: $R_{\text{universe}} \sim 1.5$–$3 \times R_{\text{Hubble}}$. Jointly: $R_{\text{universe}} \in [2, 4] \times R_{\text{Hubble}}$.

---

# **P.7.7 Chirality Across the Bounce and Sympathetic Nucleation**

*This section closes the freeze opened in v13.1. It is written in full,
incorporating the confirmed torsion coefficient from the IVN-CT8-Dirac-1
series in place of every prior provisional value (v12's $\kappa\alpha$;
v13/IVN-I's differently-structured $\Omega_1\neq\Omega_2$ system built on
a since-superseded convention correction; the clean-room package's "no
sourcing" claim, itself superseded). Confirmed unaffected by the v15
Theorem 4 split — see Section P.11.5.*

## **P.7.7.1 The Question**

Does the condensate axial current $A^0 = \bar{\psi}\gamma^0\gamma^5\psi$
change sign over one complete cosmological cycle (from one bounce through
maximum expansion to the next bounce)?

If yes: successive cycles alternate between matter-dominated and
antimatter-dominated, and the sympathetic nucleation mechanism produces
a within-cycle matter surplus whose sign is set by the cycle's chirality
phase.

If no (or if the answer is parameter-dependent): the chirality structure
of successive cycles is more complex, and the matter/antimatter asymmetry
must be understood through a different mechanism or through the specific
numerical value of the holonomy phase.

## **P.7.7.2 The Original Claim and Why It Fails**

Previous versions of this section (v5–v11) stated that spinors on $S^3$
acquire a sign change under the antipodal map, $A^\mu \to -A^\mu$, as
"the default consequence of the standard spin representation on $S^3$."
This is incorrect for two reasons. First, the spatial antipodal map
sends $\psi \to -\psi$, but $A^\mu$ is bilinear, so
$A^\mu \to (-1)^2 A^\mu = +A^\mu$ — the spatial antipodal map gives the
wrong sign. Second, the bounce is not a spatial antipodal map; it is a
continuous temporal event governed by the cosmological Dirac equation
(CT-viii), and $A^0$ is continuous through it with no local sign flip.

## **P.7.7.3 The Corrected Monodromy Calculation (Confirmed System)**

**Convention and bilinears.** Following the resolved
IVN-CT8-Dirac-1a convention audit: $\eta_{ab} = \mathrm{diag}(+1,-1,-1,-1)$;
$(\gamma^0_D)^2 = +\mathbf{1}$. In explicit 2-spinor components
$\psi=(\xi,\chi)^T$, with $u\equiv\xi^\dagger\xi$, $v\equiv\chi^\dagger\chi$
(real, $\geq0$), $w\equiv\xi^\dagger\chi$ (complex):

$$\eta = u-v, \qquad J^0=-(u+v), \qquad A^0=-(w+\bar w), \qquad P=i(w-\bar w)$$

**The confirmed bilinear evolution equations.** Three independent
derivation routes — direct-bilinear (component-by-component Euler-Lagrange
on $\xi,\chi$), and 4D-first (Cartan equation solved in the full,
un-reduced action using the fully-spatial contorsion component
$K_{ijk}=\tfrac{\kappa\alpha}{4}\varepsilon_{ijk}A^0$, the component
actually sourced by $A^0$ and surviving on the homogeneous background,
as opposed to the vanishing electric-type $K_0^{\ ij}$ component
initially and mistakenly used in an earlier attempt at this same route)
— converge on:

$$\dot{\eta} + 3H\eta = \kappa\alpha A^0 P \tag{E1}$$

$$\dot{A}^0 = -(2m + \lambda\eta)\,P \tag{E-A}$$

$$\dot{P} = \left(2m + \left(\lambda - \frac{3\kappa\alpha}{2}\right)\eta\right) A^0 \tag{E-P}$$

$$\dot{J}^0 + 3H J^0 = 0 \tag{E-J}$$

Written with explicit Hubble friction on every bilinear (matching the
component-level equations from which these were derived, not the
literal box of P.9.5.3 — see the note at the end of P.9):

$$\dot\eta = -3H\eta - \frac{3\kappa\alpha}{2}A^0P$$
$$\dot J^0 = -3HJ^0$$
$$\dot P = -3HP - \left(2m+\left(\lambda-\frac{3\kappa\alpha}{2}\right)\eta\right)A^0$$
$$\dot A^0 = -3HA^0 + (2m+\lambda\eta)P$$

All four real. All four independently confirmed by every route that
reached the correct physical contorsion component. The mass/quartic
sector coefficients ($2m$, $\lambda\eta$) were never in dispute across
any version of this derivation; only the torsion-sourced coefficient
($\kappa\alpha$ vs. $\tfrac{3\kappa\alpha}{2}$ vs. $3\kappa\alpha$, at
various points in this sector's revision history) required resolution,
and is now fixed.

**In Branch 1** ($A^0=0$), (E1) reduces to $\dot\eta+3H\eta=0$,
recovering the familiar dilution law $\eta\propto a^{-3}$ exactly.
Branch 1 is, and always was, unaffected by any version of this
derivation.

**In Branch 2** ($A^0\neq0$), (E1) has the nonzero source term
$\kappa\alpha A^0P$ at the confirmed coefficient. This is genuine new
physics, absent from every version of this section prior to v13, and
now established rather than provisional.

**The $(A^0,P)$ sub-system.** Equations (E-A) and (E-P) form a coupled
linear system for fixed (slowly-varying) $\eta$:

$$\dot A^0 = -\Omega_1 P, \qquad \dot P = \Omega_2 A^0$$

$$\Omega_1 \equiv 2m+\lambda\eta, \qquad \Omega_2 \equiv 2m+\left(\lambda-\frac{3\kappa\alpha}{2}\right)\eta$$

$\Omega_1\neq\Omega_2$ whenever $\kappa\alpha\neq0$. For $\Omega_1\Omega_2>0$
— the generic case when $\lambda>\tfrac{3\kappa\alpha}{2}$, i.e. weak
torsion coupling relative to the quartic self-coupling — the system is
oscillatory with adiabatic phase

$$\Phi_{\text{cycle}} = \int_{\text{cycle}}\sqrt{\Omega_1(t)\Omega_2(t)}\,dt$$

and monodromy matrix, in the adiabatic approximation,

$$M = \begin{pmatrix}
\cos\Phi_{\text{cycle}} & -\sqrt{\Omega_1/\Omega_2}\sin\Phi_{\text{cycle}} \\
\sqrt{\Omega_2/\Omega_1}\sin\Phi_{\text{cycle}} & \cos\Phi_{\text{cycle}}
\end{pmatrix}$$

$M=-\mathbf{1}$ (full chirality inversion) requires
$\Phi_{\text{cycle}}=(2n-1)\pi$, an odd multiple of $\pi$ — a
quantization condition on the action parameters with no topological
protection (Section P.7.7.4).

**The phase estimate.** In Phase III (near $\eta\approx0$, late time,
large $a$), $\sqrt{\Omega_1\Omega_2}\to2m$ and

$$\Phi_{\text{cycle}} \approx 2m\,T_{\text{cycle}} \sim 10^{54}$$

using the preliminary estimate $m\sim m_{\text{eff}}\sim10^{-6}$ eV,
$T_{\text{cycle}}\sim10^{60}\,\text{eV}^{-1}$. In Phase I (near the
bounce, $\eta\gg2m/\lambda$), the torsion coupling introduces a finite
shift

$$\delta\Phi = -\frac{3\kappa\alpha}{4}\int_{\text{cycle}}\eta\,dt$$

which reduces $\Phi_{\text{cycle}}$ relative to the naive
$2m\,T_{\text{cycle}}$ estimate by a finite, calculable amount once
$\alpha$ is fixed by the Bi-209 calibration. This shift does not, in
general, land $\Phi_{\text{cycle}}$ on the nearest odd multiple of
$\pi$ — that remains a set of measure zero in the space of possible
action-parameter values, with no topological mechanism forcing it
(P.7.7.4).

**Conclusion of P.7.7.3.** Chirality inversion per cycle
($M=-\mathbf{1}$) is not a generic consequence of the dynamics. It
requires the action parameters to satisfy a non-topologically-protected
quantization condition. This conclusion is unchanged across every
version of this section since v12 — what has changed, and is now
settled, is the coefficient of the torsion-sourced terms feeding into
$\Omega_2$ and into (E1).

## **P.7.7.3a Branch 2 $\eta$-Sourcing by the Chiral Sector — Confirmed**

Equation (E1), $\dot\eta+3H\eta=\kappa\alpha A^0P$ (with
$\kappa\alpha\to\tfrac{3\kappa\alpha}{2}$ understood in the sign
convention used throughout this document), means that in Branch 2 the
scalar condensate is not simply diluting under expansion — it is
dynamically driven by the product of the axial current and the
pseudoscalar bilinear. Since $A^0$ and $P$ oscillate (P.7.7.3, adiabatic
solution) at frequency $\sim\sqrt{\Omega_1\Omega_2}\approx2m$, their
product oscillates at roughly double this frequency, and in general
$\langle A^0P\rangle_{\text{osc}}\neq0$ once the phase relationship
between the two oscillators is accounted for: a generic $90°$ phase
offset for a coupled linear oscillator pair does not guarantee the
time-averaged product vanishes when $\Omega_1\neq\Omega_2$.

**Physical interpretation.** $A^0$ is the chiral charge density; $P$ is
the parity-odd pseudoscalar amplitude. Their product is parity-even and
couples to $\eta$ through the torsion coupling $\kappa\alpha$. In
Branch 2, the condensate is not in the parity-preserving vacuum; the
coexistence of nonzero $A^0$ and $P$ is itself a parity-broken state,
and the torsion coupling allows energy to flow between the scalar
condensate and the parity-odd sector.

**Status: no longer an open item.** Prior versions of this section
(v13, v13.1) carried this as CRITICAL and outstanding, pending
verification of the sourcing term itself. That verification is now
complete: three independent routes agree on both the existence and the
magnitude of the sourcing term. What remains open is not whether $\eta$
is sourced in Branch 2, but how large the effect is relative to the
leading $a^{-3}$ dilution — which depends on $\alpha$, still pending
Bi-209.

**Consequence for CT-ix.** See Section P.10 below, rewritten in full.
**Note (v15):** the homogeneous background bilinear $P(t)$ analyzed
throughout this section is the same operator $\bar\psi\gamma^5\psi$ as
the local fluctuation field $\delta P$ of Section P.11, evaluated in a
different context (spatially constant cosmological background versus
local spatial perturbation). No conflict between the two analyses; see
Section P.11.5 for the explicit non-interference statement.

## **P.7.7.4 Is the Phase Topologically Quantized?**

A systematic investigation (carried unchanged from v12, and unaffected
by the coefficient resolution — this investigation concerns the
structural question of whether *any* phase of this general type can be
topologically pinned, independent of its numerical value or coupling
strength) checked all candidate mechanisms for topological quantization
of $\Phi_{\text{cycle}}$:

**Spin structure on the temporal $S^1$:** The cosmological cycle
compactifies to $S^1$, which has two spin structures. The spin-statistics
theorem selects the antiperiodic spin structure (antiperiodic boundary
conditions on $\psi$). This forces $\psi(T_{\text{cycle}}) = -\psi(0)$.
However, the bilinears $(A^0, P)$ are quadratic in $\psi$: under
$\psi \to -\psi$ both bilinears are unchanged. The antiperiodic
spin structure gives periodic boundary conditions on the bilinears,
implying $M = +\mathbf{1}$, not $-\mathbf{1}$.

**Aharonov-Bohm effect:** Requires enclosed curvature flux in the
interior of the loop. The base manifold (time interval) is
one-dimensional; no two-forms exist and no flux is enclosed.
Result: inapplicable.

**Berry phase:** For the symmetric Branch 1 cycle, the parameter-space
path retraces itself (expanding phase = time-reverse of contracting
phase). A retraced path encloses zero area and gives zero Berry phase.
For Branch 2 (asymmetric), the Berry phase may be nonzero, but the
degeneracy point $\Omega_1=\Omega_2$ (equivalently $\kappa\alpha=0$) is
not enclosed for the physical case $\kappa\alpha\neq0$.
Result: zero for Branch 1; zero for Branch 2 with $\kappa\alpha\neq0$
held fixed around the cycle.

**Global $S^3$ mode coupling:** The spatial modes of $\psi$ on $S^3$
decouple from the zero mode at quadratic order. Nonlinear corrections
from the quartic term are suppressed in the mean-field approximation.
Result: no quantization from global $S^3$ modes at this order.

**Conclusion:** No topological mechanism quantizes $\Phi_{\text{cycle}}$.
The holonomy is a continuous, parameter-dependent element of
$\mathrm{SO}(2)$ (real orthogonal, per the corrected real bilinear
system — not $\mathrm{U}(1)$ as in the pre-IVN-I v12 treatment, which
worked with a complex-valued system that has since been superseded, but
the conclusion of no topological protection carries over unchanged).

## **P.7.7.5 The Physical Situation**

With the preliminary estimate $m \sim m_{\text{eff}} \sim 10^{-6}$ eV
and $T_{\text{eff}} \sim t_{\text{max}} \sim (\pi/2)R_{\text{universe}}
\sim 10^{60}$ eV$^{-1}$:

$$\Phi_{\text{cycle}} \approx 2m \cdot T_{\text{eff}} \sim 10^{54}$$

The phase is astronomically large and exquisitely sensitive to $m$ and
$R_{\text{universe}}$; it cannot be determined without the Bi-209
calibration. The matter-creation epoch (the $T<T_c$ window following the
bounce during which sympathetic nucleation operates) has a duration
$\delta t_c\sim H_c^{-1}$ where $H_c$ is the Hubble rate at $T=T_c$.
During this epoch, $A^0$ rotates by an angle $\delta\Phi\sim\sqrt{\Omega_1\Omega_2}\cdot\delta t_c$.

If $\delta\Phi\ll\pi$ — i.e., if the matter-creation epoch is short
compared to one half-rotation period — then $A^0$ has an approximately
definite sign during nucleation regardless of whether $M=-\mathbf{1}$
over the full cycle. The chirality of each cycle's matter content is
set by the sign of $A^0$ at the start of the matter-creation epoch,
which is determined by the accumulated holonomy phase from all previous
cycles. Whether $\delta\Phi\ll\pi$ is now a fully well-posed numerical
question — the system that determines it is established — awaiting
only the two numbers ($m$, $\alpha$) that Bi-209 provides. This
sub-calculation is identified as a sub-target of CT-ix (OQ-CT-ix-5,
Section P.10) and should be performed once the calibration is available.

## **P.7.7.6 The Sympathetic Nucleation Mechanism: Preserved**

The physical mechanism for within-cycle matter surplus is unaffected by
any version of the coefficient resolution: standard vacuum pair
creation gives net baryon number 0; in the presence of a condensate
with $\langle A^0\rangle \neq 0$, two same-chirality particles are
produced with net baryon number $+2$, at probability ratio
$\sim |\langle A^0\rangle|^2/m_{\text{eff}}^2$. What is preserved
is the mechanism and the existence of a chirality bias; what is now
established, rather than merely argued, is that this bias does not
necessarily invert sign at each bounce, and its value is set by the
accumulated (confirmed) holonomy from all previous cycles.

## **P.7.7.7 Relationship to the JWST Anomaly**

The interpretive link to the JWST early massive galaxy anomaly is
unaffected: sympathetic nucleation being active (nonzero $\langle A^0
\rangle$ at the matter-creation epoch) is required for any matter to
exist at all, and the magnitude of the within-cycle surplus depends on
$|\langle A^0\rangle|/m_{\text{eff}}$, computable after Bi-209
calibration.

## **P.7.7.8 Relationship to the Sakharov Conditions**

The condensate structure continues to provide structural correspondences
to all three Sakharov conditions (baryon number violation via Type 2
nucleation; CP violation via $\langle A^0 \rangle \neq 0$; departure
from equilibrium via the first-order bounce transition of Theorem 6).
Quantitative demonstration still requires PT-2 and the Bi-209
calibration.

## **P.7.7.9 Proof Target Structure**

**PT-1** [Status: numerical calculation, system now fully established]:

Compute the monodromy phase $\Phi_{\text{cycle}}$ and matrix $M$
numerically for the physical action parameters fixed by the Bi-209
calibration, using the confirmed system of P.7.7.3. Determine whether
the matter-creation epoch duration $\delta t_c$ satisfies
$\delta\Phi\ll\pi$ (P.7.7.5). Report $\langle A^0\rangle$ at the start
of the current cycle's matter-creation epoch. This proof target is no
longer gated on any convention or coefficient question — it is gated
only on the Bi-209 calibration itself.

*Prerequisite:* Bi-209 calibration.
*Expected result:* A specific numerical value for the holonomy phase
and a quantitative prediction for the within-cycle matter surplus.
*Nature of result:* Numerical, not topological.

**PT-2:** Bogoliubov analysis of pair creation in chiral condensate
background. Full computation of $P(\text{Type 2})/P(\text{Type 1})$ as
a function of $\{\alpha, \lambda, m, \langle A^0\rangle\}$.
*Prerequisite:* PT-1, for the value of $\langle A^0\rangle$.

**PT-3:** Self-consistent evolution equation for $\langle A^0\rangle$
across $N$ bounce cycles, using the monodromy matrix $M$ established by
PT-1. Determine whether the long-run sequence of $\langle A^0\rangle$
values is periodic, quasi-periodic, or ergodic.
*Prerequisite:* PT-1.

**PT-4:** Formal derivation of Sakharov conditions from $S_{\text{geo}}$.

## **P.7.7.10 Resolution Record: The IVN-CT8-Dirac-1 Series**

*This section replaces the v13.1 freeze notice. The freeze it announced
is lifted as of this document. The record below is retained in full for
audit purposes, since this sector has now been revised five times and
the discipline of showing the full path — not just the endpoint — is
what the project's governance charter identifies as the fix for that
pattern.*

**IVN-CT8-Dirac-1a** (convention audit) — CLOSED. Confirmed the
Hermiticity assignment $(\gamma^0_D)^2=+1$ in the $(+,-,-,-)$ convention
is forced, ruling out an alternative representation that would have
made both $\bar\psi\psi$ and $J^\mu$ simultaneously real without the
compensating structure this framework uses.

**IVN-CT8-Dirac-1b** (abstract-lemma route, reduced action) —
superseded in its Part C. Correctly established the operator structure
and overall magnitude class (Parts A, B) but produced an imaginary
residual in $\dot P$ from a gamma-algebra slip in applying the general
Hermiticity lemma to the $\Gamma=\gamma^5$ bilinear specifically. This
signaled an error (a real bilinear cannot have an imaginary source), not
a physical result, and opened 1b-i.

**IVN-CT8-Dirac-1b-i** (direct-bilinear route, reduced action) —
CLOSED. Working in explicit 2-spinor components with no abstract
lemma, located the bug and derived the corrected system at coefficient
$-\tfrac{3\kappa\alpha}{2}$ in $\dot\eta$. Recommended one further
independent check (the 4D-first route, the untried leg of the original
triangulation strategy) before the freeze could be lifted.

**4D-first, first attempt** — erred, and was itself corrected rather
than accepted. Worked from the connection component $K_0^{\ ij}$,
sourced by the spatial axial current $A^k$, which vanishes identically
on the homogeneous isotropic background. Found a real combinatorial
identity (an antisymmetric-index-pair double-count) but applied it to a
term with no physical contribution, producing a spurious apparent
doubling of the coefficient.

**4D-first, confirming pass** — CLOSED. Identified that the fully
spatial contorsion component $K_{ijk}$, sourced by $A^0$ itself, is the
one that survives on the background and was the omission in the first
attempt. Redone with every step multiplied out explicitly in 2-spinor
components, reproduced $-\tfrac{3\kappa\alpha}{2}$ exactly — agreeing
with, not doubling, the direct-bilinear result.

**Net result:** three independent derivation routes (reduced-action /
direct-bilinear, and 4D-first after its own internal correction) now
converge on the same coefficient. This is the first point in this
sector's revision history where a result has been independently
reproduced by a genuinely distinct method rather than asserted,
partially checked, or found internally consistent by a single route.
The freeze is lifted on that basis. Gap 7 moves to ESTABLISHED; Gap 16
moves to CLOSED for the mechanism, with numerical evaluation explicitly
flagged as pending Bi-209 throughout this document rather than treated
as settled.

**What remains genuinely open, stated plainly:** the clean-room
package's other two claims (P.9.4.2 double-count; P.9.5.3 sign error)
were never independently re-derived by any document in this series and
are not resolved by this rewrite — see the note at the end of Section
P.9. IVN-CT8-Dirac-1d (the $\eta\equiv-i\bar\psi\psi$ labeling question)
remains a non-blocking housekeeping item, noted at Theorem 0 above. The
quantitative size of the Branch 2 correction to the $a^{-3}$ dilution
law, and the numerical monodromy phase, both require Bi-209 and are not
evaluated here. **(v15: nor are the numerical values of $\gamma_\eta$,
$\gamma_P$, and $m_P/m_\eta$ from Section P.11 — a distinct set of
open numbers, gated on CT-vii rather than Bi-209 alone.)**

---

# **P.8 Remaining Calculational Programme**

The following items are calculational targets within the closed theory — well-defined computations, not foundational gaps.

**CT-i.** Numerical evaluation of $\kappa(T)$ across intermediate temperatures (stellar interior and galactic-scale regime). Analytic high-T and low-T limits are closed; intermediate regime requires numerical Matsubara integration.

**CT-ii.** Quantitative Gordon decomposition corrections. The full spinor vector current contains spin-orbit cross terms that modify $Q_{\mu\nu}$ at second order, generating predictions at nuclear scales relevant to the Bi-209 Channel C measurement.

**CT-iii.** Lensing diffusion timescale measurement. The spinor field diffusion prediction $\tau_{\text{diff}} \sim R^2 m_{\text{eff}}/\hbar$ is testable from time-resolved post-merger lensing imaging. *(v15: this dimensional prediction is the retired Theorem 4 formula; CT-iii should now be understood as testing the derived transport law of Theorem 4b — ballistic-to-diffusive crossover with channel-dependent $\gamma_\phi$ — once CT-vii(b) supplies numerical damping rates, per the two-component signature proposed in Section P.11.5 and Paper B Section 5.)*

**CT-iv.** Uniqueness at higher order in $\psi$. Theorem 1 establishes uniqueness at quadratic order. Quartic corrections are identified as Term 3; their full characterisation as a tensor source is pending.

**CT-v.** Equivalence principle formal bound. Quantitative suppression of $\eta$ differential at laboratory scales from the condensate temperature structure, compared against Eötvös bounds.

**CT-vi.** Quantitative evaluation of $m_{\text{eff}}$ from action parameters $\{\alpha, \lambda, m\}$ and comparison against the Pb-208 coherence timescale estimate. The Bi-209 calibration provides an independent experimental determination.

**CT-vii.** Black hole condensate propagator: full perturbative mode analysis of the spinor condensate field around a Schwarzschild background. Prerequisite for converting the dimensional estimate $f_{\text{cond}} \sim M^{-2}$ into a quantitative prediction (now understood to require re-derivation from first principles rather than confirmation — see Section P.11), and for establishing whether condensate propagation couples to pulsar timing. Also prerequisite for CT-xiii, CT-xix, and CT-xx. **Expanded (v15) with three named sub-targets, per the Theorem 4 split:**

- *CT-vii(a)* — numerical evaluation of the SCH GMOR ratio
  $m_P^2/m_\eta^2 = m/(2\lambda\eta_{\text{eq}}^3)$ once Bi-209 fixes
  $\{m,\lambda,\eta_{\text{eq}}\}$. Determines whether the light-$P$-mode
  regime of P.11.2 is realized.
- *CT-vii(b)* — computation of the per-channel Landau-damping rates
  $\gamma_\eta(T,\rho)$, $\gamma_P(T,\rho)$ from the finite-temperature
  self-energy's $O(\omega)$ imaginary slope. A genuinely new
  computation, not a lookup from Theorem 3.
- *CT-vii(c)* — recomputation of the black hole condensate frequency
  table (P.7.5.2, retracted) using (a) and (b), determining the
  dominant channel and propagation regime at each relevant distance
  scale (horizon, galactic, cosmological).

See Section P.11 for full derivation and motivation.

**CT-viii.** FLRW reduction and modified Friedmann equations. **CLOSED — see Section P.9.**

**CT-ix.** Derivation of $R_{\text{universe}}$ from action parameters and initial conditions, and full cosmological dynamics of the modified Friedmann system. **CLOSED for Branch 1; Branch 2 mechanism now established, magnitude pending Bi-209 — see Section P.10, rewritten in full this version. Confirmed unaffected by the v15 Theorem 4 split.**

**CT-x.** Bogoliubov analysis of sympathetic nucleation (Proof Target PT-2). Now proceeds from the confirmed $(\eta,A^0,P)$ system of Section P.7.7.3 above rather than any prior provisional system; its input $\langle A^0\rangle$ is the accumulated holonomy value discussed in P.7.7.5, not a value fixed by an assumed per-cycle sign inversion.

**CT-xi.** Perturbative vacuum stability, ghost analysis, and Hamiltonian boundedness of $S_{\text{geo}}$. Required for full formal closure at the quantum field theory level.

**CT-xii.** Hyperbolicity and causal propagation verification for the full Einstein-Cartan-SCH system.

**CT-xiii.** Photon–condensate coupling cross section $\sigma(\omega)$ as a function of photon frequency $\omega$, and derivation of the CMB monopole temperature from the condensate scrambling integral. Required to elevate the Olbers mechanism and CMB-as-condensate-scrambled-light conjectures (Paper A Section 6.9) from conjecture to theorem.

Physical content: The propagating spinor condensate $C_{\mu\nu}$ couples to photons via the photon-condensate interaction term in the full action. By Theorem 5, photons carry minimum nonzero w-spin $\eta_{\min}$ and therefore couple to the condensate weakly but measurably — gravitational lensing is direct observational confirmation of this coupling. The photon-condensate cross section $\sigma(\omega)$ governs both the lensing deflection (at short path lengths through concentrated condensate) and the cumulative strataract drag (at cosmological path lengths through the diffuse intergalactic condensate). The coherence damping length $L_{\text{coh}}(\omega) = 1/(n_{\text{condensate}}\,\sigma(\omega))$ determines the transition redshift $z_{\text{flip}}$ above which accumulated drag is sufficient to randomize photon directional and spectral coherence. The CMB monopole temperature $T_{\text{CMB}}$ emerges from the total energy density of this drag-randomized flux as a maximum-entropy (Planck) spectrum. The strataract drag also contributes an additive component to the cosmological redshift of all distant sources, separable in principle by its correlation with integrated line-of-sight matter density (Paper A Section 6.9.0).

Sub-targets: (a) Derive the photon-condensate vertex from $S_{\text{geo}} + S_{\text{matter}}$ (minimal coupling at order $\eta_{\min}$). (b) Compute $\sigma(\omega)$ at one loop in the condensate background. (c) Evaluate the coherence damping integral over all sources as a function of $z_{\text{flip}}$. (d) Derive $T_{\text{CMB}}$ from the total drag-randomized energy density. (e) Verify consistency with the measured 2.725 K. (f) Compute the line-of-sight strataract drag contribution to source redshift as a function of integrated matter density.

Prerequisites: CT-vii (open) and CT-viii (closed).

Falsification conditions carried in from Paper A Section 6.9: (i) $\sigma(\omega) = 0$ for all $\omega$ falsifies both the Olbers and CMB conjectures simultaneously; (ii) $\sigma(\omega)$ nonzero but $T_{\text{CMB}}$ inconsistent with 2.725 K falsifies the CMB origin conjecture; (iii) resolved-source count showing no suppression below $z_{\text{flip}}$ falsifies the Olbers mechanism conjecture.

**CT-xix.** Antipodal condensate coupling and global mode contribution — formal derivation of the mechanism by which condensate waves on $S^3$ couple into global rotational modes at their antipodal convergence points, closing the bounce cosmology energy cycle. Prerequisites: CT-vii, CT-viii (closed). **OPEN.** *(v15: plausibly aided by the light $\delta P$-channel's ballistic propagation identified in Section P.11.3 — an $S^3$-crossing distance is a natural candidate for the vacuum/dilute regime — but this is unconfirmed pending CT-vii(c).)*

**CT-xx.** Thermodynamic consistency of the coherence-forcing mechanism — entropy accounting for the galactic engine. Prerequisites: CT-xix, Bi-209 calibration. **OPEN.**

Full specifications for CT-xix and CT-xx in the galactic engine physical picture document and Paper A Section 2.11.

---

# **P.9 CT-viii: FLRW Reduction and Modified Friedmann Equations**

**Verification status:** This section requires independent expert verification. The gamma matrix calculations in P.9.4.1 and the bounce condition in P.9.6.2 are the steps most sensitive to sign conventions and should be prioritised for verification.

**Prerequisite for:** PT-1, CT-ix, CT-xiii, CT-xix, CT-xx.

**Methodological note:** Variation is performed before reduction (vary-then-reduce) rather than reduce-then-vary, to avoid missing boundary terms on $S^3$. The GHY term handles the timelike boundary; spatial boundary terms on the closed $S^3$ vanish automatically.

**Key dynamical choice:** The timelike axial current $A^0(t)$ is carried as an unconstrained dynamical quantity throughout. It is neither set to zero nor assumed nonzero. The field equations determine which branch is realised.

## P.9.1 — The Metric Ansatz

The universe has spatial topology $S^3$. The metric on $S^3 \times \mathbb{R}$ with scale factor $a(t)$:

$$ds^2 = -dt^2 + a(t)^2\,\gamma_{ij}\,dx^i dx^j$$

$$\gamma_{ij}\,dx^i dx^j = d\chi^2 + \sin^2\!\chi\left(d\theta^2 + \sin^2\!\theta\,d\phi^2\right)$$

$$g_{\mu\nu} = \mathrm{diag}\!\left(-1,\;a^2,\;a^2\sin^2\!\chi,\;a^2\sin^2\!\chi\sin^2\!\theta\right)$$

## P.9.2 — Tetrad and Levi-Civita Spin Connection

$$e^a_\mu = \mathrm{diag}\!\left(1,\;a,\;a\sin\chi,\;a\sin\chi\sin\theta\right)$$

$$e^\mu_a = \mathrm{diag}\!\left(1,\;\frac{1}{a},\;\frac{1}{a\sin\chi},\;\frac{1}{a\sin\chi\sin\theta}\right)$$

$$e = a^3\sin^2\!\chi\sin\theta = \sqrt{-g}$$

$$\overset{\circ}{\omega}{}^{01}{}_{\mu=1} = \dot{a}, \quad \overset{\circ}{\omega}{}^{02}{}_{\mu=2} = \dot{a}\sin\chi, \quad \overset{\circ}{\omega}{}^{03}{}_{\mu=3} = \dot{a}\sin\chi\sin\theta$$

$$\overset{\circ}{\omega}{}^{12}{}_{\mu=2} = -\cos\chi, \quad \overset{\circ}{\omega}{}^{13}{}_{\mu=3} = -\cos\chi\sin\theta, \quad \overset{\circ}{\omega}{}^{23}{}_{\mu=3} = -\cos\theta$$

$$R = 6\!\left(\ddot{a}/a + \dot{a}^2/a^2 + 1/a^2\right)$$

## P.9.3 — The Cosmological Spinor Ansatz and Bilinear Analysis

$\psi=\psi(t)$, spatially homogeneous in the local orthonormal frame.

$$\eta = \bar\psi\psi, \quad A^0 = \bar\psi\gamma^0\gamma^5\psi, \quad A^i = \bar\psi\gamma^i\gamma^5\psi=0 \text{ by isotropy}$$

Isotropy forces $A^i=0$ but does not force $A^0=0$; a purely timelike axial current is fully compatible with homogeneity and isotropy.

Torsion from nonzero $A^0$: $T_{ijk}=\tfrac{\kappa\alpha}{2}\varepsilon_{ijk0}A^0$, purely spatial. Contorsion: $K^{ab}_{\ c}=-(\kappa\alpha/4)\varepsilon^{ab}_{\ c0}A^0$.

## P.9.4 — Reduction of $S_{\text{geo}}$

### P.9.4.1 — Explicit Reduction of the Dirac Kinetic Term

Temporal piece ($\mu=0$): $D_0\psi=\dot\psi$.

Spatial covariant derivatives:

$$D_1\psi = \frac{\dot{a}}{4}[\gamma_0,\gamma_1]\psi$$

$$D_2\psi = \frac{1}{4}\left(\dot{a}\sin\chi\,[\gamma_0,\gamma_2] - \cos\chi\,[\gamma_1,\gamma_2]\right)\psi$$

$$D_3\psi = \frac{1}{4}\left(\dot{a}\sin\chi\sin\theta\,[\gamma_0,\gamma_3] - \cos\chi\sin\theta\,[\gamma_1,\gamma_3] - \cos\theta\,[\gamma_2,\gamma_3]\right)\psi$$

Integrating over $S^3$: the $\gamma_0$ terms survive; the $\gamma_1$ and $\gamma_2$ terms vanish (topological consequence of closed $S^3$).

$$\int_{S^3} e\,\bar{\psi}\gamma^a e^\mu_a D_\mu\psi\,d^3x = 2\pi^2 a^3\!\left(\bar{\psi}\gamma^0\dot{\psi} - \frac{3H}{2}\bar{\psi}\gamma^0\psi\right)$$

Coefficient of $H\bar\psi\gamma^0\psi$: $-3/2$, derived, not assumed.

### P.9.4.2 — The Full Reduced Lagrangian

$$L_{\text{EC}} = -\frac{3V_{S^3}}{\kappa}\,a\!\left(\dot{a}^2 + 1\right)$$

$$L_{\text{geo}} = V_{S^3}\,a^3\!\left[\frac{i}{2}\!\left(\bar{\psi}\gamma^0\dot{\psi} - \dot{\bar{\psi}}\gamma^0\psi\right) - \frac{3H}{2}\bar{\psi}\gamma^0\psi - m\eta - \frac{\lambda}{4}\eta^2 - \frac{\kappa\alpha}{4}(A^0)^2\right]$$

$$\rho_{\text{geo}} = m\eta + \frac{\lambda}{4}\eta^2 + \frac{\kappa\alpha}{4}(A^0)^2, \qquad p_{\text{geo}} = -m\eta - \frac{\lambda}{4}\eta^2 + \frac{\kappa\alpha}{4}(A^0)^2$$

## P.9.5 — The Modified Friedmann Equations

### P.9.5.1 — First Friedmann Equation

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\!\left(\rho_{\text{matter}} + m\eta + \frac{\lambda}{4}\eta^2 + \frac{\kappa\alpha}{4}(A^0)^2\right)$$

### P.9.5.2 — Second Friedmann Equation (Raychaudhuri)

$$\frac{\ddot{a}}{a} = -\frac{\kappa}{6}\!\left(\rho_{\text{matter}} + 3p_{\text{matter}} - 2m\eta - \frac{\lambda}{2}\eta^2 + \kappa\alpha(A^0)^2\right)$$

### P.9.5.3 — Cosmological Dirac Equation

$$i\gamma^0\dot{\psi} = \frac{3H}{2}\gamma^0\psi + m\psi + \frac{\lambda}{2}\eta\psi + \frac{\kappa\alpha}{2}A^0\gamma^0\gamma^5\psi$$

*Note carried forward, not resolved by this rewrite:* a literal solve of
this equation for $\dot\psi$ gives a purely imaginary coefficient on the
Hubble term, in apparent tension with the manifestly real $-3H/2$
damping used throughout the explicit component equations of Section
P.7.7.3 (which are independently confirmed by three routes and are not
in question). The clean-room package flagged this same equation as
carrying a sign error. Neither claim has been independently
re-verified by re-deriving this box from $\delta S_{\text{geo}}/\delta\bar\psi=0$
in the reduced action from scratch. This is out of scope for the
present rewrite (which resolves Gap 7 and Gap 16, not Gap 15) and is
listed here as an explicit, narrowly-defined open item rather than
silently carried forward as settled or silently corrected without its
own independent check.

### P.9.5.4 — Conservation Law

$$\frac{d}{dt}\!\left(a^3\bar{\psi}\gamma^0\psi\right) = 0 \qquad \Rightarrow \qquad a^3 J^0 = \mathcal{J} = \text{const}$$

### P.9.5.5 — GR Recovery

$\eta \to 0$, $A^0 \to 0$: standard $k=+1$ Friedmann equations recovered exactly.

## P.9.6 — Bounce Condition Analysis and PT-1 Prerequisites

### P.9.6.1 — Two-Branch Structure

**Branch 1** ($A^0=0$): bounce driven purely by $\lambda\eta^2$. Self-consistent.

**Branch 2** ($A^0\neq0$): both quartic condensate and torsion contribute. Equally self-consistent.

### P.9.6.2 — Bounce Existence Condition

$$\frac{\lambda}{2}\eta^2 + 2m\eta > \kappa\alpha(A^0)^2$$

Branch 1: reduces to $(\lambda/2)\eta^2+2m\eta>0$, satisfied for all $\eta>0$. Bounce always occurs.

Branch 2: condition satisfied when the scalar condensate dominates at maximum compression, generic at Planck-scale densities.

$$\eta_{\text{bounce}} \approx \sqrt{\frac{12}{\kappa\lambda}}\frac{1}{a_{\text{bounce}}}$$

### P.9.6.3 — Bounce Regularity

At the bounce, $H=0$, not infinite. The cosmological Dirac equation is first-order with no singularity at $t=t_{\text{bounce}}$. The bounce is a regular point.

### P.9.6.4 — PT-1 Prerequisites Delivered

Delivered: cosmological Dirac equation through the bounce; bounce regularity; two-branch structure; conservation law $a^3J^0=\mathcal{J}$; formal framework for spinor transformation under the bounce. All used, and confirmed consistent with, the P.7.7.3 derivation above.

## P.9.7 — Note on Unverified Subsidiary Claims (New in v14)

The clean-room re-derivation that triggered the v13.1 freeze (`SCH_CleanRoom_Rederivation_v1.md`) made three claims: (i) no Branch 2 sourcing of $\eta$ — **superseded**, definitively, by the confirmed sourcing at $-\tfrac{3\kappa\alpha}{2}$ established in Section P.7.7.3 above; (ii) a double-count in P.9.4.2; (iii) a sign error in P.9.5.3. Because claim (i) — the package's central claim — did not survive independent scrutiny, claims (ii) and (iii) are not treated as established merely because they arrived alongside it. Neither has been independently re-derived by any document in the IVN-CT8-Dirac-1 series, all of which worked with the reduced bilinear system rather than re-deriving P.9.4.1/P.9.4.2/P.9.5.3 from the action. P.9.4.1, P.9.4.2, and P.9.5.3 above are therefore carried forward exactly as in v12/v13, unedited, with claim (iii) flagged explicitly at P.9.5.3 above. This is a distinct, narrower, and newly-opened item — not part of the Gap 7/Gap 16 closure of this document, and not silently resolved by it. **(v15: unaffected by the Theorem 4 split; a wholly separate open item.)**

---

## P.10 CT-ix: Cosmological Dynamics from the Modified Friedmann System

*This section closes the freeze on Branch 2 opened in v13.1 and refined
in v13. Branch 1 has been correct and unaffected throughout this
sector's entire revision history; it is repeated here in full per this
document's no-elision policy. Branch 2 is rewritten to reflect the
confirmed three-variable system. Confirmed unaffected by the v15
Theorem 4 split — see Section P.11.5.*

CT-ix delivers the solution structure of the modified Friedmann system
established by CT-viii.

### Branch 1 (torsion-free, $A^0 = 0$)

The condensate scalar satisfies $\dot{\eta} + 3H\eta = 0$, giving
$\eta(t) = \eta_0/a(t)^3$. Substituting into the modified Friedmann
equation:

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\left(\frac{m\eta_0}{a^3}
+ \frac{\lambda\eta_0^2}{4a^6}\right)$$

**Phase I (stiff-condensate, $a \ll a_*$):**
$a(t) \propto |t - t_{\text{b}}|^{1/3}$. Stiff-fluid equation of state.
Predicted gravitational wave spectral tilt: $n_T = -1$ (blue-tilted,
distinct from inflationary models).

**Phase III (dust-condensate, $a \gg a_*$):**
Standard closed-universe parametric solution. Maximum expansion radius:
$a_{\text{max}} = \kappa m\eta_0/3$, giving:

$$R_{\text{universe}} = \frac{\kappa m\eta_0}{3}\,R_{\text{unit}}$$

CMB quadrupole suppression constraint ($R_{\text{universe}} \geq
3R_{\text{Hubble}}$) translates to:

$$m\eta_0 \geq \frac{9c^4}{8\pi G}$$

Branch 1 is unaffected by every version of the chirality-sector
revision: (E1) reduces exactly to $\dot\eta+3H\eta=0$ when $A^0=0$,
matching what CT-ix has always assumed. All Branch 1 results stand
without qualification, as they have since v12.

### Branch 2 (torsion-active, $A^0 \neq 0$) — Rewritten

The confirmed system, carried directly from Section P.7.7.3:

$$\dot\eta = -3H\eta - \frac{3\kappa\alpha}{2}A^0P$$
$$\dot J^0 = -3HJ^0$$
$$\dot P = -3HP - \left(2m+\left(\lambda-\frac{3\kappa\alpha}{2}\right)\eta\right)A^0$$
$$\dot A^0 = -3HA^0 + (2m+\lambda\eta)P$$

**This is a genuinely coupled three-variable system** — $\eta$, $A^0$,
and $P$ evolve together, with $\eta$ sourced by the oscillating product
$A^0P$ and $A^0$, $P$ each carrying an $\eta$-dependent frequency. This
is qualitatively different from the picture assumed by every version of
CT-ix prior to v13 (a single $\Omega_{\text{mix}}$ oscillator for
$(A^0,P)$ with $\eta$ decaying independently as $a^{-3}$), and different
again from the clean-room package's claim (a fully decoupled $\eta$,
requiring only the $(A^0,P)$ oscillator to be rebuilt). Neither simpler
picture survives; the coupled three-variable system is what is
established.

**Leading-order behavior.** In the weak-torsion-coupling regime already
identified as generic in P.7.7.3 ($\lambda\gg\tfrac{3\kappa\alpha}{2}$),
the $A^0P$ source term in $\dot\eta$ is a perturbation on top of the
dominant $-3H\eta$ dilution. Writing $\eta=\eta^{(0)}+\eta^{(1)}$ with
$\eta^{(0)}=\eta_0/a^3$ the unperturbed Branch 1-like solution, the
correction $\eta^{(1)}$ is sourced by
$-\tfrac{3\kappa\alpha}{2}A^0P$ evaluated on the zeroth-order $(A^0,P)$
oscillator solution of P.7.7.3 (frequencies $\Omega_1,\Omega_2$
evaluated at $\eta=\eta^{(0)}$). Because $A^0,P$ each decay as
$a^{-3/2}$ under Hubble friction in the adiabatic approximation
(standard damped-oscillator behavior), their product — and hence the
source term — decays as $a^{-3}$, the **same power of $a$** as the
unperturbed dilution term itself. The correction is therefore not
negligible at late times relative to $\eta^{(0)}$ merely by virtue of
cosmic expansion; whether it is small depends on the ratio of
amplitudes,

$$\frac{\eta^{(1)}}{\eta^{(0)}} \sim \frac{\kappa\alpha}{H}\cdot\frac{|A^0_0P_0|}{\eta_0} \times (\text{oscillating factor of order unity})$$

which is a genuinely calculable number once $\alpha$, $m$ (hence $H$ at
the relevant epoch), and the initial $(A^0_0,P_0,\eta_0)$ are fixed by
the Bi-209 calibration and the matter-creation-epoch initial conditions
identified in P.7.7.5. It is parametrically small in the weak-coupling
regime ($\kappa\alpha\ll\lambda$, already the generic assumption
underpinning the whole monodromy analysis), but "parametrically small
in a generic regime" is not the same statement as "shown to be
numerically small" — that requires the number, not yet available.

**Revised late-time-attractor statement.** Branch 2 approaches Branch 1
behavior at late times up to this calculable oscillatory correction of
fractional size $\sim\kappa\alpha/H$ (times order-unity oscillating
factors). This supersedes both the pre-v13 claim (clean asymptote, no
correction — incomplete, as v13 first noted) and the v13/clean-room
back-and-forth (source term present but of unknown, possibly
order-unity, size — now resolved to be parametrically small in the
regime already assumed generic elsewhere in this section, though not
yet numerically bounded).

**Open questions generated by CT-ix, updated:**

OQ-CT-ix-1: Explicit $c(t)$ derivation from the Phase III solution. Unaffected, still open.

OQ-CT-ix-2: Overlap between Phase I power suppression and CMB quadrupole. Unaffected, still open.

OQ-CT-ix-3: $\eta$ evolution correction at finite $A^0$ in Branch 2. **Closed as a question of mechanism and coefficient by Section P.7.7.3 above; open only as a question of numerical magnitude, pending Bi-209.**

OQ-CT-ix-4: Transition scale $a_*$ vs. observed matter-radiation equality. Unaffected, still open.

OQ-CT-ix-5: Duration of the matter-creation epoch relative to the rotation period $\pi/(2m)$ — the key input for the PT-1 numerical calculation (P.7.7.5, P.7.7.9). Now fully well-posed given the confirmed system; awaits Bi-209 for the numbers.

**IVN items:** The eight original CT-ix verification items and the
IVN-CT8-Dirac-1 series (1a–1d, plus the 4D-first confirming pass) are
now resolved or explicitly scoped as described in Section P.7.7.10.
Results from Branch 1 and from the confirmed Branch 2 system above may
be used downstream. The two unrelated clean-room claims about P.9.4.2
and P.9.5.3 (Section P.9.7) remain unverified and are not endorsed by
this closure.

---

# **P.11 Term 2 Carrier Structure and Transport (Theorem 4 Split)**

*New in v15. Supersedes Theorem 4 (Section P.5) in full. Formalizes
`SCH_Theorem4_Split_CarrierStructure_v1.md`.*

## **P.11.0 — Why This Section Exists**

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
consequence is Theorems 4a and 4b (P.11.4), which supersede Theorem 4
in full.

## **P.11.1 — Carrier Identification: the Chiral Decomposition**

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

## **P.11.2 — Tree-Level Potential and the SCH GMOR Relation**

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
(CT-vii(a), P.11.6 below).

**Consequence.** Term 2 is carried by (at least) two fields, not one:
$\delta\eta$ (mass $m_\eta \sim m_{\text{eff}}$) and $\delta P$ (mass
$m_P$, generically distinct, parametrically smaller in the natural
regime above).

## **P.11.3 — Transport: Vacuum and Finite Temperature**

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

## **P.11.4 — Theorems 4a and 4b**

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

## **P.11.5 — What Is Retracted, Suspended, and Unaffected**

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
notice at P.7.5.2 and P.8's expanded CT-vii entry.

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

## **P.11.6 — New Calculational Sub-Targets (CT-vii)**

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

*End of Appendix P — v15*

*June 2026 | Incorporates the Theorem 4 split in full.*

*Summary of v15 changes relative to v14: (1) New Section P.11 supplies
the linearized derivation Theorem 4 never provided, identifying two
condensate carriers ($\delta\eta$, $\delta P$) related by a derived SCH
Gell-Mann–Oakes–Renner relation, and deriving their transport as a
damped relativistic wave equation (dissipationless in vacuum, diffusive
in dense media with channel-dependent Landau-damping rates) rather than
asserting a diffusion formula. (2) Theorem 4 (P.5) is marked
superseded-in-place by Theorems 4a and 4b; its original text is
retained unedited for the historical record. (3) The black hole
condensate frequency table (P.7.5.2) is retracted — every entry void,
mass-scaling exponent unestablished — pending recomputation as CT-vii(c).
(4) CT-vii (P.8) is expanded with three named sub-targets: (a) GMOR
ratio, (b) Landau-damping rates, (c) frequency-table recomputation.
(5) The STATUS SUMMARY table's Gap 5 is split into a mechanism component
(unaffected, ESTABLISHED) and a propagation-frequency component (OPEN,
new Gap 5a); two new rows (Gap 17, Gap 18) record the carrier-structure
closure and transport-regime reopening. (6) Section P.6's closure table
is updated correspondingly, with a new FINAL STATUS (v15) paragraph.
(7) Theorem 2's parity-preserving vacuum condition is noted as
independently confirmed (not merely assumed) by the tree-level
potential of P.11.2. (8) Precision notes are added at Theorem 0 Step 3
and Theorem 6 Steps 1–3 cross-referencing the completed two-field
expansion and the corrected symmetry identification (chiral, not
vector, rotation), without altering either theorem's conclusions.
(9) Section P.7.7 and Section P.10 (the entire chirality/Branch-2
sector closed in v14) are confirmed unaffected and are reproduced in
full, unedited, per the no-elision policy; an explicit non-interference
note is added at P.7.7.3a and P.11.5 distinguishing the cosmological
background bilinear $P(t)$ from the local fluctuation field $\delta P$.
Every other section — P.0 through P.6, P.7.1–P.7.6, P.8, P.9, P.10 — is
reproduced in full, not referenced, per this revision's no-elision
policy, with inline notes at the specific points the Theorem 4 split
touches.*
