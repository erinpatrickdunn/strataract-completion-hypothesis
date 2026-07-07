# Paper A — Draft 2.4 | June 2026

# Geometric State as a Gravitational Source Variable:
## A Multi-Scale Framework and Falsifiable Test Program

**Draft 2.4 | June 2026**

Revised from Draft 2.3: Section 2.10a and the CT-x entry in Section 6.6 are updated to reflect Appendix P v14 (the single-pass canonical rewrite closing the freeze that Draft 2.3 could only gesture at). Where Draft 2.3 reported the chirality-inversion question as an open, IVN-I-flagged item whose supporting calculation had itself been superseded twice over (first by a clean-room re-derivation, then by that re-derivation's own supersession), Appendix P v14 reports a resolution: three independent derivation routes — the direct-bilinear route and a twice-attempted, self-correcting 4D-first route — now converge on the same torsion self-coupling coefficient. Chirality inversion per cosmological cycle remains confirmed non-generic, as it has been since Draft 2.2; what changes in this revision is that the underlying mechanism is now established rather than provisional, with only its numerical magnitude (requiring the Bi-209 calibration) left open. The footer pointer to Appendix P is updated from v13 to v14. Supersedes Draft 2.3.

Revised from Draft 2.2: Section 2.10a and the CT-x entry in Section 6.6 are updated to reflect IVN-I ("PT-1 Monodromy in the $(+,-,-,-)$ Convention", June 2026), which redid the Appendix P PT-1 monodromy calculation in a consistent metric-signature convention. The chirality-inversion claim in this section already carried CONJECTURE/PREDICTION status pending PT-1 in Draft 2.2; that pending status is now updated to reflect what PT-1 actually found once the convention error was corrected — chirality inversion per cycle is confirmed non-generic, and a previously unknown Branch 2 coupling between the scalar condensate and the chirality sector is identified as a new open item. The footer pointer to Appendix P is updated from v9 to v13. Supersedes Draft 2.2.

Revised from Draft 2.1: Corrections to photon w-spin description, Eötvös typo, Sciama reference page number, rotation curve flattening data availability claim, and epistemic status table entry. Supersedes Draft 2.1.

Revised from Draft 2.0: Targeted extension. The galactic engine physical picture — developed in the companion document *SCH_GalacticEngine_PhysicalPicture_v1* — is incorporated. Section 2.10 is extended to describe what happens to condensate waves after black hole emission. New Section 2.11 introduces the galactic engine mechanism: antipodal convergence on $S^3$ as the link between local black hole emission and global $\omega(t)$, and coherence-forced halos as the physical origin of what appears as dark matter. The epistemic status table, Section 6.3, Section 6.6, and the Conclusion are updated accordingly. Appendix P is updated to v9 with CT-xix and CT-xx formally specified. All content from Draft 2.0 is carried forward unchanged. Supersedes Draft 2.0.

---

## Prefatory Note — Draft 2.1

Draft 2.0 established the correct logical order: physical picture first, mathematics as encoding. It left one physical question incompletely answered. Section 2.10 described black hole bounce resonance and the emission of condensate waves at frequency $f_{\text{cond}} \sim M^{-2}$. It did not describe where those waves go or what they do after emission. On a flat infinite manifold the answer would be: they disperse. On a closed $S^3$ the answer is different and the difference matters.

Draft 2.1 answers that question. Condensate waves on $S^3$ converge at their antipodal point. The nonlinear coupling in $S_{\text{geo}}$ converts the arriving wave energy into excitation of global $S^3$ modes. This is the mechanism that couples local black hole emission to the global rotation rate $\omega(t)$ — the previously unspecified link in the bounce cosmology energy cycle. It also drives a second consequence at galactic scales: the outward-propagating condensate hum from a galactic centre's black hole population maintains rotational coherence in halo matter beyond what thermal decoherence would otherwise allow. The region of maintained coherence is the dark matter halo. It is not a population of particles. It is the acoustic shadow of the galactic engine.

These two consequences — the antipodal energy cycle closure and the coherence-forced halo — were parallel, unconnected predictions in Draft 2.0. They are now mechanistically linked through the same condensate wave propagation physics.

Nothing in the mathematical content of Draft 2.0 is retracted. Two new calculational targets (CT-xix and CT-xx) are added. The epistemic status of the new claims is PREDICTION and CONJECTURE respectively, reflecting that the formal derivations are identified targets rather than completed theorems.

---

## Framework Epistemic Status: Reader Roadmap

| **Claim** | **Section** | **Status** | **Epistemic basis** |
|---|---|---|---|
| Time is flat — absolute background parameter | 0.1 | **AXIOM** | Foundational. Not derived. All other claims are consistent with it. |
| Space is flat — Euclidean 3D background | 0.1 | **AXIOM** | Foundational. Gravity is a field effect, not spatial curvature. |
| Matter is a Localized Topological Soliton with w-axis spin | 0.2 | **AXIOM** | Foundational. Physical basis for all derived results. |
| Mass = w-axis spin magnitude | 0.2 | **DERIVED** | Falls out of soliton geometry. Zero w-spin = zero mass = light. |
| $c$ = tangential velocity of $S^3$ surface | 0.3 | **DERIVED** | Photon as minimum-w-spin ($\eta \approx \eta_{\min} > 0$) surface wave. $c$ is a cosmic readout, not a constant. |
| W-pressure is the origin of inertia | 0.3 | **DERIVED** | Resistance to soliton reorientation in rising slice-attachment pressure. |
| $c$ asymptote = escape velocity from $S^3$ slice | 0.3 | **DERIVED** | W-pressure rises without bound as soliton approaches tangential velocity. |
| Modified field equation derived from $S_{\text{geo}}$ | 2.1 | **THEOREM** | Metric variation of Einstein-Cartan-Dirac action. Appendix P, derivation chain. |
| $Q_{\mu\nu}$ unique at quadratic order in $\psi$ | 2.1, 2.5 | **THEOREM** | Fierz completeness + three filters. Regime-conditional. Appendix P, Theorem 1. |
| $\eta = \bar{\psi}\psi$ is w-spin magnitude | 2.3 | **THEOREM** | Lorentz scalar bilinear = geometric measure of soliton w-rotation. Appendix P, Theorem 2. |
| GR exact recovery when $A_\mu = 0$ | 2.1, 6.1 | **THEOREM** | W-spin $\to$ 0 limit. Torsion vanishes algebraically. Appendix P, Step 16. |
| Spin quantization from $S^3$ closure | 0.4 | **DERIVED** | $S^3 \cong \mathrm{SU}(2)$. Closure condition gives integer and half-integer naturally. |
| Uncertainty principle is geometric | 0.5 | **DERIVED** | 3D cross-section of Localized Topological Soliton is a region, not a point. |
| Orbital shapes from w-axis excursions | 0.5 | **DERIVED** | Interference pattern of soliton excursion re-entry points. |
| Light predominates at epoch boundaries | 0.6 | **DERIVED** | W-pressure $\to$ 0 as $c(t) \to$ 0. Matter dissolves to light phase. |
| Bounce = matter-light-matter phase transition | 0.6 | **DERIVED** | No singularity possible — matter phase ends before turnaround. |
| $S^3$ topology compatible with spinor field | 2.9 | **COMPATIBILITY** | $\mathrm{SU}(2)$ group manifold = $S^3$. Appendix P, P.7.6. |
| BH bounce condensate frequency $f_{\text{cond}} \sim M^{-2}$ | 2.10 | **DIM. ESTIMATE** | From Theorem 4 diffusion timescale. Appendix P, P.7.5. |
| Chirality inversion per cosmological cycle ($A^\mu \to -A^\mu$) | 2.10a | **ESTABLISHED — CONFIRMED NON-GENERIC; MAGNITUDE PENDING BI-209** | Appendix P v14 (June 2026) closes the derivation: three independent routes (direct-bilinear; a twice-attempted, self-correcting 4D-first route) converge on the torsion self-coupling coefficient. Chirality inversion is confirmed non-generic — it requires a non-topologically-protected fine-tuning of action parameters, not a default consequence of $S^3$ geometry. The monodromy phase and within-cycle matter surplus are now fully well-posed numerically, pending only the Bi-209 calibration. See Section 2.10a. |
| Sympathetic nucleation produces net matter | App. C | **CONJECTURE** | Bogoliubov analysis required (PT-2). Structural correspondence established. Independent of whether chirality inverts per cycle — see Section 2.10a. |
| Angular diameter turnaround on $S^3$ | 6.8 | **PREDICTION** | Follows from $S^3$ geometry. Single free parameter $R_{\text{universe}}$. |
| Two-tax redshift: expansion + strataract drag | 6.9.0 | **DERIVED** | Follows from Theorem 5 + minimum-nonzero photon w-spin. Separating signature identified. |
| Olbers mechanism via strataract drag | 6.9.1 | **CONJECTURE** | CT-xiii required. Proof target identified. |
| CMB monopole as accumulated drag-randomized flux | 6.9.2 | **CONJECTURE** | CT-xiii required. Separable from acoustic anisotropy structure. |
| Black holes are rotational processors, not sinks | 2.11 | **DERIVED** | Follows from Term 3 bounce + Term 2 propagation. Appendix P P.7.5. |
| Antipodal convergence couples BH emission to global $\omega(t)$ | 2.11 | **PREDICTION** | Follows from $S^3$ topology + condensate propagation. CT-xix required for formal derivation. |
| Dark matter halo = coherence-forced region of galactic engine | 2.11 | **CONJECTURE** | Reframing of anomalous gravitational sourcing. Requires CT-vii, CT-xix, CT-xx. |
| Rotation curve flattening radius correlates with central BH mass | 2.11 | **PREDICTION** | Derivable from $f_{\text{cond}} \sim M^{-2}$ once condensate propagator known. CT-vii prerequisite. Falsifiable once direct dynamical BH mass sample for late-type spirals reaches N ≥ 30 (data gap confirmed June 2026; see Paper B Section 7.4). |

---

# 0. The Physical Picture

*This section states the ground floor of the framework in plain language. No equations appear here. The equations in Sections 1–6 and Appendix P are the mathematical encoding of what is said here — not its logical source. A reader who understands Section 0 understands the framework. The rest is precision.*

## 0.1 The Background Architecture: Absolute Parameterized Time and Euclidean Space

The foundational bedrock of this multi-scale framework rests upon two invariant geometric constraints. Every subsequent field equation and cosmological derivation proceeds from this rigid coordinate architecture in tandem with the intrinsic topology of matter.

**I. Absolute Parameterized Time**
Time is defined strictly as a rigid, one-dimensional, monotonically increasing parameterizing variable ($t$). It is fundamentally decoupled from localized matter-energy distributions and is incapable of metric curvature, warping, or localized dilation. The framework establishes a strict global foliation of the cosmos, wherein all observers—regardless of kinematic state or gravitational potential—share an identical, absolute present moment.

Consequently, the phenomenon traditionally interpreted as "time dilation" is recast not as a deformation of the temporal metric, but as a localized dynamic constraint on the internal state evolution of matter distributions. Kinematic and gravitational redshifting are manifestations of physical throttling on a system's internal mechanisms; clocks slow, but the underlying temporal parameter remains uniformly invariant.

**II. Euclidean Spatial Background**
Spatial geometry is modeled exclusively as a flat, three-dimensional Euclidean manifold ($\mathbf{R}^3$) possessing no intrinsic elasticity or autonomous degrees of freedom. The mechanical interactions traditionally attributed to the curvature of a spacetime fabric are generated instead by gradients within a ubiquitous physical field—the strataract—that pervades this rigid background.

The pseudo-Riemannian metric formulation of General Relativity ($g_{\mu\nu}$) is understood here as a highly successful effective field theory that mathematically correlates gravitational phenomenology by mapping the strataract gradient onto a fictitious, over-parameterized curved background. This geometric description is a phenomenological proxy rather than an ontological reality. A flat spatial background coupled to the dynamics of the strataract field is mathematically and physically sufficient to reproduce all observed gravitational behavior without requiring space itself to bend.

## 0.2 Matter is a Localized Topological Soliton. Mass is W-Axis Spin.

Every subatomic particle is a localized topological soliton — a self-consistent configuration of field energy with extent in all four spatial dimensions. Three of those dimensions are the familiar spatial dimensions of our observable universe. The fourth — call it the w-axis — is perpendicular to our three-dimensional slice of the cosmos.

The solitonic configuration rotates on the w-axis. This rotation is not a metaphor or an analogy. It is the actual physical motion of the soliton's structure in the fourth spatial dimension. And this rotation is mass.

**Mass is w-axis spin magnitude.** More w-spin = more mass. A particle with no w-spin has no mass. It is light.

This identification — mass as w-axis spin - is not postulated to fit observations. It falls out of the geometry. If a soliton rotates on the w-axis, it has angular momentum in 4D. Redirecting that angular momentum requires force. That resistance to redirection is what we measure as inertia. Inertia and mass are the same thing, and both are the resistance of a spinning 4D soliton to reorientation. The equivalence of inertial and gravitational mass - long treated as a mysterious coincidence requiring the equivalence principle - is a direct geometric consequence of this picture.

The particle zoo follows from this. Massive particles differ in the magnitude and closure topology of their w-axis spin — the proton, electron, and neutrino are solitons of different spin magnitude and different closure type threading the same S³ slice. The photon is the limiting case: a minimum-w-spin surface wave on the S³, not a bound soliton, but sharing the same underlying rotational geometry at its minimum nonzero coupling.

## 0.3 The S³ Cosmos, the Strataract, and the Speed of Light

The universe is an S³ — a three-sphere, a closed hyperspherical manifold — rotating on the w-axis. Every particle's w-spin is sympathetically coupled to this cosmic rotation. The local and the cosmological are not separate: the same rotation that spins a quark also rotates the cosmos. They are the same phenomenon at different scales.

The strataract is the rotational pressure field of the S³ slice, felt locally by every soliton embedded in it. It exerts symmetric pressure on every soliton from both sides in the w-direction — holding matter to the three-dimensional slice. Where the strataract field is uniform, space behaves as flat vacuum. Where massive concentrations of w-spinning solitons depress the field locally, neighboring matter falls along the resulting gradient. This is gravity — not curved space, but a strataract gradient.

Light is a surface wave on the S³ — not a soliton, not localized, not bound to any specific 3D position. A photon has minimum nonzero w-spin ($\eta \approx \eta_{\min} > 0$). This minimum coupling is confirmed by gravitational lensing: a truly zero-w-spin object would be completely decoupled from the condensate field and could not be deflected by massive bodies. Light bends, therefore photons couple, therefore their w-spin is nonzero. It is minimum — not zero. Without meaningful w-spin there is no soliton structure, no slice-binding pressure, no inertia in the matter sense. The photon propagates tangentially to the S³ surface at the tangential surface velocity of the cosmos.

**C is that tangential velocity:**

$$c(t) = \omega(t) \cdot R_{\text{cosmic}}(t)$$

C is not a universal constant. It is a live readout of the cosmic rotation rate ω(t). It is the speed at which the S³ surface moves. Light travels at c because light is a tangential surface wave — not because c is an externally imposed speed limit.

**The C asymptote falls out of this immediately.** As a soliton accelerates through the 3D slice, the strataract's resistance to w-axis tipping rises exponentially. The faster the bulk motion, the harder the slice pushes back to maintain the soliton's orientation. Reaching c would require infinite energy because the w-pressure resisting exit grows without bound. C is the escape velocity from the S³ slice, and it is geometrically infinite. You cannot exceed c not because of a law but because the cosmos will not release you.

**Relativistic effects are consequences of this geometry, not separate postulates:**

- *Length contraction* — the soliton's 3D cross-section narrows as it tips toward the w-axis. The object has not compressed; its slice intersection has narrowed.
- *Clock slowing* — internal atomic processes run at c. Bulk translation consumes a share of this budget. What remains for internal cycling is reduced. Clocks slow because the c-budget is partially spent on motion, not because time dilates.
- *Relativistic mass increase* — the soliton tips further into w as speed increases. Redirecting a more w-tilted soliton requires more force. Inertia rises with speed for geometric reasons.
- *The Twin Paradox* — both twins experience identical absolute time. The traveling twin's atoms record different histories because bulk acceleration tilted their solitons, throttling internal processes. The watches agree. The atomic records diverge.
- *Simultaneity* — two simultaneous events are simultaneously real. Apparent disagreements between observers are bookkeeping errors arising from not accounting for w-axis orientation when predicting signal arrival times. Relativity of simultaneity is not a feature of spacetime — it is a navigational artifact.

## 0.4 Spin Quantization from S³ Closure

The quantization of particle spin — why only integer and half-integer values are observed — is not postulated. It falls out of the S³ geometry.

A soliton threading a closed S³ must close back on itself after traversing the manifold. The w-axis rotation angle of the soliton must satisfy a closure condition: after going around the S³ once, the soliton's phase must return to its starting configuration. This is the same mathematics that quantizes electron orbitals, generalized to S³ geometry.

S³ is isomorphic to SU(2) as a manifold. SU(2) is the double cover of SO(3). This double cover structure means the closure condition admits both integer and half-integer solutions:

- **Integer closure** — soliton returns after one full rotation. **Bosons.** Photon, gluon, W/Z, graviton.
- **Half-integer closure** — soliton requires two full rotations to return. **Fermions.** Electron, quark, neutrino.

The Pauli exclusion principle follows: two solitons cannot occupy the same w-rotational state at the same location — topological exclusion, not an external rule. The spin-statistics theorem follows: integer-closure solitons commute, half-integer-closure solitons anti-commute — a consequence of closure type, not a separate postulate. The discrete mass spectrum follows: since mass = w-spin magnitude and w-spin is quantized, particle masses come in discrete values. The mass spectrum is a geometric spectrum.

**The key insight:** S³ ≅ SU(2) as a manifold. The cosmos IS the spin group. The quantization of particle spin and the topology of the universe are the same geometric fact, not two separate things that happen to share mathematics.

## 0.5 Quantum Effects as Geometry

Several results that have resisted physical interpretation in standard quantum mechanics become transparent in the soliton picture.

**The uncertainty principle** is not an epistemic limit on measurement. Every particle is a soliton with genuine w-axis extent. Its observable 3D properties are the cross-section of that 4D structure with our slice. A cross-section of a 4D object is inherently a region, not a point. Position uncertainty is the genuine 3D footprint of a 4D object intersecting a 3D slice. It is ontological, not epistemic.

**Electron orbital shapes** — the s, p, d, f geometries — are not arbitrary solutions to a wave equation imposed from outside. Electrons have relatively loose w-spin coupling and can undergo brief w-axis excursions: the soliton tilts asymmetrically, one side of its w-extent temporarily protrudes beyond the slice, and the electron's cross-section with the slice shifts. The probability cloud is the time-averaged distribution of these excursion re-entry points. Node lines where electron density is zero are directions in which the soliton's excursion geometry produces no slice intersection — not regions the electron avoids, but directions in which it is momentarily outside the slice entirely.

Ground state is the closest approach to a symmetric 4D sphere — minimum perturbation from the isotropic ground configuration. Excited states are perturbations from that symmetry. This is why the universe preferentially produces spherical and hyperspherical structures at every scale: the symmetric 4D sphere is the lowest energy configuration of a w-spinning soliton in a symmetric pressure field.

**The double slit** has resisted classical explanation because it demands light behave simultaneously as a wave and a particle. In 3D this is contradictory. In SCH it is not. Light is a surface wave on the S³ — not a soliton, not localized, not bound to any 3D coordinate. It propagates through both slits simultaneously because it is a wave on a surface, and waves do this. When a detector forces a coupling with matter — a soliton — the surface wave gets pinned to the slice at that interaction point. The interference pattern disappears not because of observation in any philosophical sense but because the wave coupled to a w-spinning soliton and was localized by it. Wavefunction collapse is a soliton-coupling event.

**Quantum entanglement** appears to require faster-than-light communication in 3D. In SCH no superluminal signaling is required. Entangled particles share a topological relationship in 4D — their soliton structures are linked through the w-axis. The 3D distance between them is irrelevant because the connection was never through 3D space. Measuring one particle's w-state resolves the shared 4D topology simultaneously. No signal travels through 3D space. The 3D separation between entangled particles is a red herring — they were never separated in the dimension that matters.

## 0.6 Cosmic Epoch Dynamics

The cosmos rotates on the w-axis. As it expands, matter condenses into complex structures — galaxies, stars, atomic configurations — each consuming rotational energy from the free pool. The cosmic rotation rate ω(t) drops. C(t) drops. The w-pressure holding matter to the slice drops.

**Matter stability is a function of cosmic epoch.** At peak rotation, solitons are tightly bound. At low rotation, they are loosely held. The energy threshold required to strip w-spin from a soliton and convert matter to light drops as c(t) drops.

This gives a unified physical explanation for why light predominates at both boundaries of a cosmic epoch:

*At the beginning:* The cosmos has just reversed rotation direction after the previous epoch's turnaround. ω(t) is rising from near zero. C is low. W-pressure is low. The threshold to form a stable soliton is high relative to available energy. The threshold to unwind a soliton is low. Photons predominate because the slice is not yet gripping hard enough to maintain stable soliton structures. The early universe radiation dominance era is not simply because it was hot — it is because the cosmos had not yet spun up enough for matter to stabilize.

*At the end:* ω(t) has been declining as matter consumes the rotational pool. C is dropping. W-pressure is dropping. Soliton structures at the margins begin to unwind spontaneously. Light production increases as the slice releases its grip on matter.

**The turnaround — the bounce — is a matter-light-matter phase transition, not a singularity:**

At maximum expansion, ω(t) → 0, c(t) → 0, w-pressure → 0. With w-pressure at zero, no soliton is held to the slice with meaningful force. The energy threshold for matter-to-light conversion approaches zero. Essentially all matter dissolves toward the photon phase. The universe at turnaround is predominantly photonic.

Absolute time continues through this moment without interruption. The S³ reverses rotation direction. ω(t) rises again. C rises. W-pressure rises. The photons that survived the turnaround now exist in a rising-pressure environment. As w-pressure increases, some surface wave configurations acquire sufficient rotational coupling to begin forming soliton structures. Light condenses back into matter.

```
Matter → Light → [Turnaround] → Light → Matter
```

There is no singularity at the bounce because there is no matter at the bounce. Matter has already dissolved into light before the turnaround. A matter singularity is geometrically impossible when the matter phase has already ended. The bounce is not matter collapsing to infinite density — it is a photon-dominated S³ reversing rotation direction.

---

# 1. The Anomaly Cluster: Predicted Consequences of the Physical Picture

*In previous drafts this section presented a collection of observational anomalies as motivating puzzles for a new framework. That framing is inverted here. The physical picture of Section 0 makes specific predictions. The following observations are where those predictions are confirmed.*

The physical picture of Section 0 predicts that the geometric organizational state of matter — specifically the coherence of w-axis spin across a system — independently sources gravitational effects beyond what mass-energy alone would produce. Systems with high rotational coherence produce stronger gravitational signatures at fixed baryonic mass. Systems with randomized orbital orientations and minimal geometric coherence do not.

This prediction has a well-defined contrast class. Globular clusters, dwarf irregular galaxies, pressure-supported ellipticals, and laboratory systems are all characterized by randomized orbital orientations and minimal w-spin coherence. They should not show anomalous gravitational signatures. They do not. The contrast class is as important as the signal class — both are predicted, and both are observed.

## 1.1 Galactic Rotation Curves

Stars at the outer edges of coherently rotating spiral galaxies orbit at velocities incompatible with the gravitational influence of visible mass alone. The anomaly is strongest in fast-rotating disc galaxies and weakest or absent in dispersion-dominated systems and globular clusters. This is the predicted pattern: organized w-spin coherence sources additional gravitational coupling beyond the baryonic mass.

The Milky Way exhibits rotation velocities of approximately 220 km/s at 50 kpc against a Newtonian prediction of approximately 100 km/s from visible mass. NGC 3198, NGC 6503, and Andromeda show similar factors. The anomaly tracks morphological coherence, not total mass. This is not explained by dark matter models, which predict mass-dependent but not coherence-dependent effects.

## 1.2 Elliptical Morphology-Lensing Correlation

A published correlation exists between elliptical galaxy morphology and inferred dark matter content, independent of total stellar mass: rounder ellipticals show stronger coupling to the geometric field and more anomalous lensing than elongated ones at equivalent mass. This is a direct prediction of the w-spin picture — a more spherically symmetric mass distribution has higher 4D rotational symmetry, which maps to different strataract coupling than an elongated system of the same total mass. Standard dark matter models have no mechanism to produce shape-dependence.

## 1.3 The Bullet Cluster and Geometric Stripping

The Bullet Cluster observation spatially separates dominant baryonic mass — hot intracluster gas — from the gravitational lensing signal, which follows the galaxy distributions. The standard interpretation requires collisionless dark matter particles.

The physical picture of Section 0 provides an alternative: Geometric Stripping. During the cluster collision, the hot intracluster gas undergoes violent shock-heating and phase randomization — the atomic and nuclear soliton structures are thermally disrupted, their w-spin coherence collapses toward the isotropic ground state. The stellar components retain rotational coherence through the collision because their internal geometric organization is thermally isolated from the intracluster medium. Enhanced gravitational sourcing therefore remains aligned with the geometrically coherent galaxy distributions.

The strataract condensate is a propagating field — it travels with the stellar matter and diffuses beyond it on timescale $\tau_{\text{diff}} \sim R^2 m_{\text{eff}}/\hbar$ (Theorem 4, Appendix P). The lensing follows the condensate. The gas has no condensate to contribute. The offset is geometric stripping, not dark matter.

## 1.4 Supporting Patterns

**JWST early massive galaxies.** JWST has identified galaxies at $z \sim 10\text{-}16$ that are anomalously massive, anomalously compact, and anomalously early relative to $\Lambda$CDM predictions. The bounce cosmology of Section 0.6 provides the explanation: each prior cycle deposits more net baryonic matter into the current cycle's initial conditions than a single-origin Big Bang would produce. Galaxies forming early in the current cycle did so in a matter-richer environment than $\Lambda$CDM assumes. Full treatment in Appendix C.

**NANOGrav gravitational wave background.** The 2023 NANOGrav detection of a stochastic background in the nHz range is conventionally attributed to supermassive black hole binary mergers. The black hole bounce resonance of Section 2.10 provides an alternative contribution: individual black holes driving condensate propagation at frequencies scaling as M⁻², which for intermediate-mass black holes falls in the nHz range. Full treatment in Section 2.10 and Paper B Section 7.1.

**Pioneer and Earth flyby anomalies.** Anomalous accelerations in spacecraft trajectories show sign and magnitude consistent with geometric coupling from the solar system's rotational organizational state. Supporting patterns only — full analysis in Paper B Section 3.

## 1.5 The Contrast Class

The physical picture predicts anomalous effects in systems with high geometric coherence and predicts their absence in systems with randomized orbital configurations. Globular clusters show no rotation curve anomaly. Dwarf irregular galaxies — with chaotic, non-coherent stellar orbits — show weak or absent anomalous lensing. Pressure-supported ellipticals show reduced geometric coupling. Laboratory systems show no anomalous gravitational effects.

This contrast class discipline is not optional — it is the primary guard against the framework absorbing every anomaly as evidence. The systems that should not show the signal do not show it. Both the presence and absence of the signal are predicted, and both are observed.

---

# 2. The Mathematical Framework

*The equations in this section are the mathematical encoding of the physical picture stated in Section 0. They do not introduce new physics — they give precision to what was said there in words. A reader who understood Section 0 should recognize each equation as a formal statement of something already physically clear.*

## 2.1 The Modified Field Equation

The physical picture of Section 0 states that the geometric organizational state of matter — the coherence of w-axis spin — sources gravitational effects beyond mass-energy alone. In the language of general relativity, this means the right-hand side of the Einstein field equation is incomplete. It contains the stress-energy tensor T_μν, which encodes what matter is — its mass, momentum, pressure. It does not contain any term encoding how matter is organized — its rotational coherence structure.

The complete field equation is:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa\left[T_{\mu\nu} + \alpha C_{\mu\nu}\right]$$

where C_μν is the geometric state tensor encoding the organizational state of matter beyond its mass-energy content, α is the dimensionless coupling constant, and κ = 8πG/c⁴ is the standard Einstein gravitational constant.

This equation is derived from the Einstein-Cartan-Dirac action with a geometric state spinor field ψ. The spinor field ψ is the mathematical representation of the soliton structure described in Section 0.2. The action S_geo is the formal encoding of the soliton's w-axis dynamics. Full derivation in Appendix P, Theorems 1-4.

The framework produces three source terms beyond standard GR:

- **Term 1:** κT_μν — standard GR stress-energy. Unchanged.
- **Term 2:** καC_μν — geometric organizational state. The propagating strataract condensate term. Primary new source at galactic scales. This is the w-pressure field described in Section 0.3, expressed as a tensor.
- **Term 3:** Quadratic torsion — spin-spin contact interaction. Negligible at galactic densities (suppressed by ε ≤ 10⁻²³). Dominant at neutron star and Planck-scale densities. The bounce mechanism of Section 0.6.

## 2.2 The Geometric Resonance Postulate — Now a Derived Theorem

In previous drafts this was presented as a postulate — an assumption that the geometric field couples to matter in proportion to its departure from the isotropic ground state. In the physical picture of Section 0 it is a derived consequence.

The isotropic ground state is the state of zero net w-spin — A_μ = 0, where A_μ = ψ̄γ_μγ⁵ψ is the axial current. This is the symmetric 4D sphere configuration of Section 0.5 — the lowest energy soliton configuration, the configuration to which matter naturally tends. Departure from this state is what sources C_μν.

**The Geometric Resonance Theorem:** The geometric field couples to matter in proportion to the geometric overlap between the local matter configuration and the field's preferred eigenstate geometry. The field's preferred eigenstate is the maximally symmetric isotropic configuration — the 4D spherical ground state at every scale. This follows from the vacuum structure of the SU(2) × SU(2) spinor covering group. Full proof in Appendix P, Step 11.

## 2.3 The Coupling Efficiency η — W-Spin Magnitude

At nuclear scales, geometric organizational state is encoded in the coupling efficiency η, identified as the spinor scalar bilinear:

$$\eta = \bar{\psi}\psi$$

This is the w-spin magnitude described in Section 0.2 — the degree to which the local matter configuration departs from the isotropic zero-spin ground state. It is a Lorentz scalar by theorem (Appendix P, Theorem 2), which is the formal expression of the fact that w-spin magnitude is a physical property of the soliton independent of the observer's orientation.

η = 0 corresponds to the isotropic ground state — zero net w-spin, zero geometric coupling, exact GR recovery.
η = 1 corresponds to maximum geometric coupling — maximum departure from isotropy, maximum strataract sourcing.

The phenomenological form $\eta(Z,N) = \left|\int\psi_{\text{nuclear}}(r) Y_{00}(\theta,\phi) dV\right|^2 f(\beta_2, \beta_4, \ldots)$ remains valid as a computational tool for nuclear calculations. The spinor bilinear is the underlying physical definition.

## 2.4 Thermal Decoherence

Geometric coupling efficiency degrades under environmental disruption. When a system is thermally agitated — collisions randomizing the w-spin orientations of individual solitons — the net geometric coherence of the ensemble drops toward zero. This is thermal decoherence. It is the same process that dissolves matter toward light at epoch boundaries (Section 0.6), operating at the atomic and nuclear scale rather than the cosmic scale.

The suppression function $f(\tau) = \tau_{\text{coll}}/(\tau_{\text{coll}} + \tau_{\text{coh}})$ approaches 1 when the collision timescale greatly exceeds the coherence recovery timescale and approaches 0 in the reverse limit.

## 2.4a The η Evolution Equation

$$u^\mu \nabla_\mu \eta = -\Gamma_{\text{decoh}} \eta + \Gamma_{\text{recoh}}(1 - \eta)$$

Both rates are derived from $S_{\text{geo}}$ via the finite-temperature effective potential (Appendix P, Theorem 3):

$$\Gamma_{\text{decoh}} = \frac{\alpha}{m^2}(\lambda\rho)^2\kappa(T)$$
$$\Gamma_{\text{recoh}} = \frac{\alpha}{m^2}(\lambda\rho)^2\kappa(T)f(T)$$

No free parameters remain. In the limit T → 0: Γ_decoh → 0, η → 1, maximum geometric coupling. In the limit T >> T_c: η → 0, C_μν → 0, exact GR recovered. The critical temperature T_c ~ m_eff/k_B is the temperature above which the cosmos is too hot to sustain w-spin coherence — the condensate melts.

Note that this galactic/nuclear-scale η evolution equation is distinct from the cosmological η evolution law of Section 2.10a and Appendix P Section P.7.7 — the latter concerns how the cosmological background value of η evolves across a bounce cycle in the presence of a nonzero axial current, and is a separate (and separately revised) calculation from the thermal decoherence law here.

## 2.5 Galactic Scale: The Rotational Coherence Tensor C_μν

At galactic scales, geometric organizational state is expressed through the rotational coherence tensor:

$$C_{\mu\nu} = Q_{\mu\nu} = \rho\eta u_\mu u_\nu$$

This is proven in Appendix P (Theorem 1) to be the unique rank-2 symmetric divergence-free tensor at quadratic order in ψ given the symmetries of S_geo. In the physical language of Section 0, this tensor encodes the w-spin density (ρη) flowing with the matter's bulk four-velocity (u_μu_ν). It is the strataract pressure field expressed as a gravitational source term.

The observational proxy at galactic scales is $\lambda_R = \langle V \rangle/\sqrt{\langle V^2 \rangle + \langle \sigma^2 \rangle}$ — the projected stellar spin parameter from IFU kinematics. This measures the degree to which stellar orbits are coherently rotating rather than randomly dispersed, which is the galactic-scale expression of w-spin coherence.

## 2.6 The Scale Bridge

The minimal phenomenological bridge connecting nuclear and galactic scale expressions is:

$$\nabla^2\phi = \rho\eta_{\text{eff}} + \lambda(\rho\eta_{\text{eff}})^2$$

The linear term governs long-range behavior at galactic densities. The quadratic term dominates at nuclear densities and becomes cosmologically significant at Planck densities — this is the Term 3 that drives the bounce mechanism of Section 0.6.

## 2.7 Why the Field Equation Cannot Be Reproduced by ΛCDM

Four $\Lambda$CDM mechanisms are considered and found insufficient to produce the predicted monotonic $\lambda_R$-lensing dependence at fixed stellar mass:

Halo assembly history predicts weaker lensing for dispersion-dominated systems at fixed mass — opposite to the prediction. Baryon feedback has no mechanism to couple specifically to orbital coherence rather than total mass. IMF variation is captured in stellar mass estimates and does not produce morphology-dependent residuals at fixed mass. Structural non-homology does not produce the predicted sign or monotonicity across the full distribution.

None of these mechanisms produces all four properties of the predicted signal simultaneously: monotonicity across the full λ_R distribution, survival under photometric mass replacement, persistence in all three mass tertiles, and steepest slope in the low-mass bin. The full discussion is in Paper B Section 2.5.

## 2.8 GR Recovery

General Relativity is recovered exactly when $A_\mu = 0$ — the isotropic ground state of the spinor field, corresponding to zero net w-spin. In this limit, torsion vanishes algebraically, $C_{\mu\nu} = 0$, and the field equation reduces to:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$$

All confirmed GR predictions occur where A_μ ≈ 0: solar system precision tests, binary pulsar orbital decay, gravitational wave production, the Eddington deflection. The framework contains GR as an exact limiting case — not an approximation, not a regime, but an exact algebraic limit when the w-spin of matter is negligible.

In the physical language of Section 0: when matter's w-spin coherence is zero, the strataract field is in its ground state everywhere, there is no geometric coupling beyond mass-energy, and Einstein's equations hold exactly.

## 2.9 S³ Spatial Topology

The spatial topology of the universe is not assumed. It is derived from the algebraic structure of the spinor field.

The geometric state spinor $\psi$ is defined on a curved spacetime manifold with covering group $\mathrm{SU}(2) \times \mathrm{SU}(2)$. The group manifold of SU(2) is, as a smooth manifold, the three-sphere $S^3$. SU(2) and $S^3$ are the same object — not a coincidence of notation but a mathematical identity. A spinor field whose symmetry group is $\mathrm{SU}(2) \times \mathrm{SU}(2)$ is most naturally and consistently defined on a spatial topology that is itself $S^3$.

This was stated in Section 0.6 in physical terms: the cosmos is an $S^3$ rotating on the w-axis. The mathematical statement is: $S^3$ is the unique compact topology on which the spin structure canonically determined by the $\mathrm{SU}(2) \times \mathrm{SU}(2)$ covering group is already present without additional input. Full argument in Appendix P, Section P.7.6.

Physical consequences: (1) quantized global condensate modes explain CMB quadrupole and octopole suppression; (2) the universe is a resonant cavity for the condensate field; (3) the angular diameter distance formula predicts a turnaround redshift z_turn (Section 6.8); (4) antipodal CMB correlation signature (Paper B Section 7.2).

## 2.10 Black Hole Bounce Resonance

The quadratic torsion term — Term 3 — dominates at Planck-scale densities. Black hole interiors reaching Planck density are firmly in the Term 3 regime. The spin-spin repulsion grows as ρ², reversing the collapse at the Planck threshold. The collapsed matter is gravitationally bound and cannot escape the event horizon — it re-collapses, bounces again, and repeats continuously.

The condensate field — Term 2 — is not confined to the black hole interior. Each bounce drives a condensate wave into the surrounding spacetime. The condensate propagation frequency is:

$$f_{\text{cond}} \sim \frac{\hbar c^4}{4 G^2 m_{\text{eff}} M^2}$$

This scales as M⁻²: larger black holes drive slower condensate waves. The quality factor Q ~ exp(m_eff c²/k_B T_Hawking) is effectively infinite for all astrophysical black holes. Black holes are the most perfect condensate resonators in the universe. The condensate hum does not decay on any astrophysical timescale.

Draft 2.0 left a question unanswered: where do these waves go? On an infinite flat manifold they would disperse. The universe is not an infinite flat manifold. It is an $S^3$. Section 2.11 answers the question.

## 2.10a Matter Accumulation Across Bounce Cycles

*[Revised in Draft 2.4 to reflect Appendix P v14. Draft 2.3 reported the chirality-inversion question as revised (following the PT-1 analysis programme and its IVN-I convention correction) but still open at the level of the underlying Branch 2 mechanism, whose supporting calculation had itself been superseded twice over between v13 and v13.1 (first by a clean-room re-derivation, then by that re-derivation's own supersession). Appendix P v14 — the single-pass canonical rewrite that closes that freeze — reports that three independent derivation routes now converge on the same torsion self-coupling coefficient. This section is rewritten below to match.]*

The cosmological bounce operates by the same Term 3 mechanism as the black hole bounce (Section 2.10). At the bounce, the spinor condensate carries chirality encoded in the axial current $A^\mu$, alongside the pseudoscalar bilinear $P$ and the scalar condensate $\eta$ itself.

Whether $A^\mu$ inverts sign across a bounce — successive cycles alternating between matter-dominated and antimatter-dominated — is **not** a default topological consequence of $S^3$ geometry. This conclusion has held, unchanged, since Draft 2.2 across every revision of the underlying calculation. Appendix P Section P.7.7 derives the cosmological evolution of $(\eta, A^0, P)$ from the cosmological Dirac equation and finds that the transformation of $A^\mu$ over one full cycle is the holonomy of a connection on the condensate axial-current bundle, with phase $\Phi_{\text{cycle}}$ set continuously by the action parameters $\{m, \lambda, \kappa\alpha\}$ and the cycle duration. A full sign inversion ($A^\mu \to -A^\mu$) requires $\Phi_{\text{cycle}}$ to land on an odd multiple of $\pi$ — a condition with no topological protection, confirmed non-generic across every version of the calculation, including the version now closed in Appendix P v14.

What is new in this revision is that the calculation itself is no longer provisional. Earlier versions of this section reported a coefficient that moved twice between drafts (first via the IVN-I convention correction, then via a subsequent clean-room finding that was itself superseded). Appendix P v14 establishes, via three independently-executed derivation routes reaching the same answer, that the scalar condensate $\eta$ is genuinely sourced in the torsion-active branch of the cosmology (Branch 2, $A^\mu \neq 0$) by the product $\kappa\alpha A^0 P$, at a specific, now-fixed coefficient. This is not a new physical claim relative to Draft 2.3 — the qualitative picture (chirality inversion non-generic; $\eta$ and the chirality sector coupled in Branch 2) is the same. What has changed is the epistemic status: from an open item pending independent verification (IVN-I-3 in Draft 2.3's language) to an established mechanism, with only its numerical magnitude — how large the correction is relative to the leading $a^{-3}$ dilution of $\eta$ — left open, pending the Bi-209 calibration.

**What this means for matter accumulation.** The physical mechanism proposed for within-cycle matter surplus — sympathetic nucleation, in which a nonzero $\langle A^0\rangle$ during the matter-creation epoch biases vacuum pair-creation toward same-chirality pairs — does **not** depend on whether $A^\mu$ inverts at every bounce. It depends only on $\langle A^0 \rangle \neq 0$ at the start of the current cycle's matter-creation epoch, whatever the sign or history of that value. The current matter dominance reflects the accumulated chirality state inherited from all previous cycles through the (now-established) holonomy, not a simple alternation. Within any matter-dominated cycle, sympathetic nucleation proceeds as before: vacuum pair-creation events can produce two matter particles of the same chirality rather than the standard matter-antimatter pair, and this within-cycle matter surplus remains the proposed explanation for why early-universe galaxies are more massive than ΛCDM predicts (full treatment in Appendix C).

**What changed and what didn't, across the full revision history.** The physical mechanism (sympathetic nucleation) and its connection to the JWST early-massive-galaxy anomaly (Section 1.4) are unchanged since Draft 2.0. What Draft 2.2 retracted was the earlier framing that cycle-to-cycle alternation was close to automatic. What Draft 2.3 added was the recognition that $\eta$ and the chirality sector are coupled in Branch 2, flagged at the time as requiring independent verification. What this draft adds is that the verification is complete: the coupling mechanism and its coefficient are established by three independent routes, closing the freeze that had been in place on this sector of Appendix P. Both the magnitude of the within-cycle surplus and the cycle-to-cycle chirality pattern remain parametric — not because the calculation is unsettled, but because they depend on the numerical value of $\alpha$ and $m$, which only the Bi-209 calibration can supply. See Appendix P Section P.7.7 for the full derivation and Section P.7.7.10 for the complete resolution record.

## 2.11 The Galactic Engine: Antipodal Coupling and Coherence-Forced Halos

*The physical picture developed here is stated first in plain language. The formal derivation requirements are CT-xix and CT-xx in Appendix P. Epistemic status: PREDICTION for the antipodal coupling mechanism and the rotation curve flattening correlation; CONJECTURE for the coherence-forced halo picture and the M-sigma consequence.*

**Black holes are not sinks.** Matter falling into a black hole carries w-spin — the rotational organizational state of whatever structure it had. As that matter compresses toward the Planck density, Term 3 grows as $\rho^2$ and eventually dominates. The spin-spin repulsion reverses the collapse. The matter bounces. It cannot escape — it re-collapses and bounces again continuously. Each bounce drives a coherent condensate wave into the surrounding spacetime through the Term 2 propagation mechanism.

This emission is not thermal. Hawking radiation carries no structural information about infallen matter. The condensate wave emission is different: it carries w-spin information about the rotational state of the infallen matter, encoded in the wave's phase and amplitude structure. The black hole is a processor. It takes in matter carrying rotational organizational information, processes it through the Planck density nonlinearity, and emits that information outward as coherent condensate waves. The rotational energy of infallen matter is not lost. It is converted and transmitted.

**Antipodal convergence on $S^3$.** On $S^3$, every geodesic departing from a point converges at the unique antipodal point — the point diametrically opposite on the manifold. A condensate wave emitted by a black hole therefore has a geometric destination. Rather than dispersing across an unbounded volume, the full wave amplitude arrives at a single point on the manifold. At the antipodal point, the nonlinear quartic coupling $\lambda$ in $S_{\text{geo}}$ converts the arriving wave energy into excitation of global $S^3$ modes — the lowest-frequency eigenstates of the condensate field that span the entire manifold.

This is the mechanism that couples local black hole emission to the global rotation rate $\omega(t)$. Every black hole, through its condensate hum, replenishes the global rotational pool through antipodal convergence. The bounce cosmology energy cycle — previously asserted but mechanistically unspecified — closes here. The universe's black hole population is not a passive recipient of the global rotation rate. It is an active contributor to its maintenance.

This also mechanistically connects four predictions that were previously derived from the same axioms but had no causal link to each other: the black hole bounce resonance (Section 2.10), the $S^3$ spatial topology (Section 2.9), the antipodal CMB correlation signature (Paper B Section 7.2), and the bounce cosmology energy cycle (Section 0.6). The antipodal CMB correlation is not merely a topological signature — it is the observational imprint of condensate waves arriving at antipodal convergence points and coupling into global modes.

**Coherence-forced halos.** Near the galactic centre, condensate waves from the central black hole complex — the SMBH and any surrounding intermediate-mass black holes — propagate outward through the strataract field. These waves maintain rotational coherence in whatever matter they pass through: a massive object emitting a coherent condensate hum at frequency $f_{\text{cond}} \sim M^{-2}$ keeps the matter in its neighbourhood in a state of higher w-spin alignment than thermal decoherence alone would produce. The region within which this coherence maintenance is effective — where the condensate wave amplitude exceeds the threshold needed to overcome local thermal decoherence — is the spatial extent of the anomalously high gravitational sourcing. It is what we observe as the dark matter halo.

The halo is not a population of particles. It is a region — the acoustic shadow of the galactic engine. Its size is not a free parameter fitted to each galaxy. It is set by the mass and emission power of the central black hole population, the thermal decoherence rate of the halo matter, and the propagation physics of the condensate field. These are in principle calculable from the framework parameters once CT-vii (condensate propagator) and CT-xx (thermodynamic consistency) are complete.

**The transition radius and rotation curve flattening.** Near the galactic centre, the condensate field is complex: multiple sources at different frequencies producing structured interference patterns with well-defined constructive and destructive nodes. As the waves propagate outward, the individual source contributions blur into a unified coherent hum — the superposition of all black hole emissions averaged over the phase relationships that develop with distance. The transition from structured near-field interference to unified propagating coherence occurs at a characteristic radius set by the condensate wavelengths $\lambda_{\text{cond}} = c / f_{\text{cond}} \sim M^2$. More massive central black holes emit at lower frequencies and longer wavelengths; the transition occurs at larger radii.

This transition radius is the rotation curve flattening radius — the radius at which the unified coherence hum becomes the dominant influence on halo matter's w-spin alignment, producing the approximately flat anomalous gravitational sourcing profile observed beyond the optical disc. The prediction: **rotation curve flattening radii should correlate with central black hole mass** in a specific functional form derivable from $f_{\text{cond}} \sim M^{-2}$. This is falsifiable against existing rotation curve data correlated with central black hole mass estimates. CT-vii is the prerequisite for the quantitative prediction.

**The M-sigma consequence.** The M-sigma relation — the empirically tight correlation between central black hole mass and galaxy velocity dispersion — has been known for decades but lacks a first-principles explanation. In the galactic engine picture it is a consequence of the coherence forcing scale. The SMBH sets the coherence forcing range for the entire galaxy through $f_{\text{cond}} \sim M^{-2}$: a more massive SMBH forces coherence to larger radii, maintaining a larger halo, producing higher anomalous orbital velocities throughout the galaxy, and therefore higher velocity dispersion. The M-sigma relation is the observational signature of this scaling. A quantitative derivation requires CT-xx (thermodynamic consistency of the coherence-forcing mechanism), which establishes the range at which a given SMBH can maintain halo coherence as a function of its mass and emission power.

**The contrast class tightened.** The existing contrast class (Section 1.5) predicts anomalous gravitational signatures in systems with high rotational coherence and their absence in systems with randomized orbital configurations. The galactic engine picture makes this more precise. The relevant variable is not only the stellar orbital coherence but the coherence of the local condensate wave field, which depends on the black hole population's organization. A galaxy with a dominant central SMBH has a coherent, organized condensate field that maintains halo coherence — the canonical mechanism. A galaxy with a disorganized, randomly distributed population of black holes produces incoherent condensate waves that average toward zero, and shows weak or absent anomalous signatures. The outliers — dwarf irregular galaxies that show anomalously strong gravitational signatures despite lacking a central SMBH — are predicted to have black hole populations with harmonic mass relationships that produce structured resonance rather than random cancellation. This is distinguishable from dark matter explanations: the SCH prediction correlates the anomaly with black hole mass distribution structure; dark matter correlates it with total mass.

**Falsification conditions for Section 2.11:**

(1) No statistically significant correlation between rotation curve flattening radius and central black hole mass, in a sample with reliable measurements of both, falsifies the coherence-forcing mechanism as the origin of halo extent.

(2) CT-xix returning zero mode coupling at the antipodal point — meaning condensate waves pass through without exciting global modes — severs the link between black hole emission and $\omega(t)$ maintenance, requiring an alternative bounce cosmology energy cycle mechanism.

(3) CT-xx returning a violation of total entropy non-decrease for typical galaxy configurations falsifies the thermodynamic consistency of the coherence-forcing mechanism.

(4) Anomalous outlier dwarf irregulars showing random black hole mass distributions indistinguishable from the non-anomalous population falsifies the harmonic resonance prediction.

Full formal treatment in *SCH_GalacticEngine_PhysicalPicture_v1* and Appendix P (CT-xix, CT-xx).

---

# 3. Methodological Grounding

## 3.1 What Cannot Be Used as Evidence

Residuals in baryonic scaling relations — particularly Mass-Metallicity residuals in fiber-fed surveys — are not valid evidence for or against the present framework. The mapping from latent galaxy state to observed residual is a composition of non-commuting operators: the aperture operator A(z) and the selection operator S. Because [A, S] ≠ 0, the derived residual is not a coordinate-invariant scalar. Spatially resolved IFU spectroscopy is the required instrument class.

## 3.2 The Thermal Control Requirement

The metallicity-lensing prediction is valid only within thermally controlled samples. Any comparison across thermally heterogeneous populations requires simultaneous measurement of both metallicity and suppression environment. The SLACS sample satisfies this constraint.

---

# 4. Primary Observational Tests

Tests 4.1 and 4.2 are co-primary. They probe the same core prediction through independent channels at different scales using different data, instruments, proxies, and lensing regimes.

## 4.1 λ_R vs. Weak Lensing — Galactic Scale (Co-Primary)

**Prediction:** At fixed stellar mass, redshift, and environment, galaxies with higher λ_R (more coherently rotating) produce stronger lensing signals. The relationship is monotonic across the full λ_R distribution and persists after baryon feedback controls.

**Data:** MaNGA survey (SDSS DR17, ~10,000 galaxies) for λ_R; Dark Energy Survey DR2 shear catalogue for weak lensing.

**Falsification condition:** No statistically significant monotonic λ_R-lensing dependence after controls in a sample of sufficient size falsifies the galactic-scale prediction.

## 4.2 Metallicity vs. Strong Lensing — Nuclear Scale (Co-Primary)

**Prediction:** At fixed total Einstein mass, within a thermally controlled sample, higher-metallicity lens galaxies produce systematically larger Einstein radii. GR predicts zero residual correlation at fixed mass.

$$\Delta\theta = \theta_{\text{GR}}\left(\frac{\eta_{\text{eff}}}{\eta_{\text{ref}}} - 1\right)$$

**Data:** SLACS sample (53 early-type lens galaxies).

**Falsification condition:** No statistically significant positive residual correlation between metallicity and Einstein radius at fixed mass falsifies the nuclear-scale prediction.

## 4.3 Large-Scale Alignment Test (Exploratory)

If the strataract field has a cosmological ground state with a preferred rotational axis, galactic spin handedness signals should show redshift-dependent evolution correlated with angular position relative to the CMB quadrupole axis. Testable via 21cm survey data.

---

# 5. Laboratory Calibration: The Bismuth-209 Experiment

## 5.1 Target Selection

Lead-208 (82 protons, 126 neutrons) is the heaviest known naturally occurring doubly magic nucleus — maximum spherical symmetry, η → 0. Bismuth-209 carries the magic neutron number 126 but one unpaired proton, holding the nucleus in geometric tension just outside the doubly magic ground state — near-maximum η(Z,N). Proton bombardment triggers transmutation to Lead-208. The transmutation event is the maximum contrast geometric reorganization available in stable matter: near-maximum w-spin coherence collapsing to near-zero w-spin coherence in a single nuclear transition.

## 5.2 Signal Magnitude

Bismuth-209 possesses the largest nuclear magnetic moment of any stable nucleus. Lead-208 has a nuclear magnetic moment of essentially zero. This transition represents one of the largest magnetic moment collapses available in stable nuclear physics — the experimental signature of the w-spin collapse described in Section 0.2.

## 5.3 Experimental Design

**Channel A — Near-field photon path deviation:** A collimated laser beam directed through the interaction region proximal to the target. Angular deviation monitored interferometrically with coincidence triggering on individual transmutation events. Standard Model prediction: zero deviation. Framework prediction: measurable angular deflection proportional to α.

**Channel B — Calorimetric anomaly:** High-precision calorimetric monitoring during bombardment. Standard Model prediction: temperature increase consistent with deposited beam energy. Framework prediction: anomalous calorimetric signal at the transition moment as w-spin energy releases.

**Channel C — Torsion sector timing signature:** The transmutation involves nuclear spin collapse from I = 9/2 (Bi-209) to I = 0 (Pb-208). The spin-9/2 initial state has A_μ ≠ 0; the spin-0 final state has A_μ = 0. Term 2 and Term 3 have different temporal profiles separable by high-resolution coincidence timing.

## 5.4 The Scaling Prediction

The Bi-209 experiment provides the calibration point — fixing α and m_eff — that converts all quantitative predictions from conditional statements to specific numbers. Until it is performed, all quantitative predictions are parametric.

---

# 6. Relationship to Existing Frameworks and Open Challenges

## 6.1 General Relativity

GR is recovered exactly in the zero-w-spin limit (Section 2.8). All confirmed GR predictions occur in this limit. The framework contains GR as an exact algebraic special case.

## 6.2 Modified Gravity Theories

MOND, TeVeS, and f(R) gravity modify the geometric side of the field equations. The present framework modifies the matter side. These produce different observational signatures.

## 6.3 Dark Matter

The framework proposes that signatures currently attributed to dark matter are the gravitational consequence of spatial gradients in geometric w-spin coupling efficiency. It does not assert that dark matter particles do not exist. Five observational predictions distinguish the framework from particle dark matter: (1) monotonic λ_R-lensing dependence at fixed stellar mass; (2) metallicity-lensing residual correlation at fixed mass; (3) Geometric Stripping with a spinor field diffusion timescale prediction; (4) morphology-dependent lensing excess at fixed stellar mass; (5) rotation curve flattening radius correlating with central black hole mass rather than total halo mass — a prediction of the coherence-forcing mechanism of Section 2.11 that particle dark matter has no mechanism to produce.

## 6.4 The Equivalence Principle

Eötvös experiments constrain composition-dependent accelerations to below 10⁻¹³ of g. The framework is not ruled out because η differential between laboratory test masses is small, both objects occupy the same local field, and nonlinear field saturation suppresses the coupling differential at terrestrial field densities. A formal quantitative demonstration remains an open requirement.

## 6.5 Formal Status: Closed Challenges

| **Challenge** | **Resolution** |
|---|---|
| Lagrangian architecture | CLOSED. S_geo is the Einstein-Cartan-Dirac action. Metric variation gives the field equation exactly. |
| Tensor emergence (Q_μν) | CLOSED. Theorem 1: unique rank-2 symmetric divergence-free spinor bilinear tensor at quadratic order. |
| η scalar nature | CLOSED. η = ψ̄ψ is a Lorentz scalar — the w-spin magnitude is observer-independent. |
| GR recovery | CLOSED. A_μ = 0 (zero net w-spin) makes torsion vanish algebraically, recovering exact GR. |
| Geometric Resonance | CLOSED. Follows from vacuum structure of SU(2) × SU(2) covering group. |
| Γ_decoh, Γ_recoh | CLOSED. Both derived from S_geo via Matsubara finite-temperature effective potential. |
| Chirality inversion mechanism and coefficient | CLOSED (Draft 2.4). Appendix P v14: three independent derivation routes converge on the torsion self-coupling coefficient. Numerical evaluation of the monodromy phase and matter surplus remains open, pending Bi-209. |

## 6.6 Remaining Calculational Programme

The following are calculational targets — well-defined computations within the closed theory:

- CT-i: Numerical evaluation of κ(T) at intermediate temperatures
- CT-ii: Quantitative Gordon decomposition corrections
- CT-iii: Lensing diffusion timescale measurement
- CT-iv: Uniqueness at higher order in ψ
- CT-v: Equivalence principle formal bound
- CT-vi: Quantitative evaluation of m_eff from action parameters
- CT-vii: Black hole condensate propagator — full perturbative mode analysis
- CT-viii: FLRW reduction and modified Friedmann equations — **closed**
- CT-ix: Derivation of R_universe from action parameters — **closed for Branch 1; Branch 2 mechanism established, magnitude pending Bi-209 (Appendix P v14)**
- CT-x: Bogoliubov analysis of sympathetic nucleation (PT-2). **Status note (Draft 2.4):** this calculation now proceeds from the fully-established $(\eta, A^0, P)$ system of Appendix P Section P.7.7.3 (v14), superseding every prior provisional system cited in Drafts 2.2 and 2.3. Its input $\langle A^0 \rangle$ is understood to be the accumulated holonomy value discussed in Section 2.10a, not a value fixed by an assumed per-cycle sign inversion.
- CT-xi: Perturbative vacuum stability and ghost analysis
- CT-xii: Hyperbolicity and causal propagation verification
- CT-xiii: Photon-condensate coupling cross section σ(ω) and CMB monopole derivation
- CT-xix: Antipodal condensate coupling and global mode contribution — formal derivation of the mechanism by which condensate waves on $S^3$ couple into global rotational modes at their antipodal convergence points, closing the bounce cosmology energy cycle. Prerequisites: CT-vii, CT-viii (closed).
- CT-xx: Thermodynamic consistency of the coherence-forcing mechanism — entropy accounting for the galactic engine, establishing that the SMBH pump pays the entropy cost of halo coherence maintenance; information-export consequence assessment (contingent). Prerequisites: CT-xix, Bi-209 calibration.

Full specifications for CT-xix and CT-xx in Appendix P, Section P.8. Full specification of the chirality-sector resolution — including the complete IVN-CT8-Dirac-1 series (convention audit, torsion coefficient derivation, the direct-bilinear route, and the twice-attempted 4D-first route) — in Appendix P v14, Section P.7.7.10.

## 6.6a Parameter Fixing Programme

- **α** (coupling constant): Fixed by the Bi-209 calibration experiment (Section 5).
- **m_eff** (spinor mass): Estimated from Pb-208 first excited state lifetime (~400 ps) as m_eff ~ 1.6 × 10⁻⁶ eV/c². Bi-209 provides independent determination.
- **λ** (quartic coupling): Constrained by requirement ρ_condensate ≥ 10⁻¹ g/cm³.
- **R_universe** (S³ topology scale): Constrained from CMB quadrupole suppression and angular diameter turnaround. Preliminary estimates: R_universe ~ 2-4 × R_Hubble.
- **c(t)** (speed of light): c(t) = ω(t) · R_cosmic(t). Not a constant — a live readout of the cosmic rotation rate. Fixed at any epoch by the rotation rate, which is set by the energy balance between free rotation and matter coherence.

## 6.7 CMB Constraint

Above the critical temperature T_c ~ m_eff/k_B, the spinor condensate melts (η → 0, C_μν → 0), and the framework reduces exactly to GR. At recombination temperatures the condensate is absent. The CMB acoustic peak structure is therefore unaffected. The quadrupole and octopole suppression reflects the topological mode cutoff of the S³ manifold (Section 2.9).

## 6.8 The Angular Diameter Distance Turnaround

On $S^3$ of radius $R_{\text{universe}}$, the angular diameter distance is:

$$d_A = R_{\text{universe}} \cdot \frac{\sin(d_{\text{proper}}/R_{\text{universe}})}{1+z}$$

This predicts a turnaround redshift z_turn beyond which objects appear larger with increasing distance — a one-parameter test with a sharp falsification condition. The test requires rest-frame optical size measurements across a broad redshift baseline. Current JWST morphologies at z > 8 are rest-frame UV only and are not reliable physical size indicators. The Roman Space Telescope wide-field clustering statistics provide the appropriate test at z ~ 2-8. HWO-era resolved imaging completes it at z > 8.

**Falsification condition:** Monotonically decreasing angular size at all observed redshifts with no improvement of the S³ fit over the flat-universe fit falsifies the S³ topology prediction.

## 6.9 Condensate Cosmology: Photon Redshift, the Olbers Mechanism, and CMB Origin

*Conjectures 6.9.1 and 6.9.2 carry CONJECTURE epistemic status. The two-tax redshift framework of Section 6.9.0 is DERIVED from the physical picture of Section 0. Proof target CT-xiii.*

### 6.9.0 The Two-Tax Redshift Framework

Photons traversing the cosmos pay two distinct energy taxes. Both are real. Both contribute to the observed redshift of distant sources. They are not competing explanations — they are additive mechanisms with different physical origins and, in principle, separable observational signatures.

**Tax 1 — Cosmological expansion.** The S³ manifold is expanding: $R_{\text{cosmic}}(t)$ grows over cosmic time. By Theorem 5, $c(t) = \omega(t) \cdot R_{\text{cosmic}}(t)$. As the S³ expands, $\omega(t)$ drops and $c(t)$ drops with it. A photon emitted when the surface velocity was higher arrives in an epoch where $c$ is lower. Photon energy is $E = h\nu$, and frequency is measured against the local $c$ at reception. The photon has not lost energy in any absolute sense — the ruler against which its energy is calibrated has changed. This is the standard cosmological redshift, now with an explicit physical mechanism: the S³ surface has slowed between emission and reception, and all energy measurements are made in units of the local surface velocity.

**Tax 2 — Strataract drag.** Photons carry minimum nonzero w-spin. They are not zero-w-spin objects — a zero-w-spin object would be completely decoupled from the condensate field and would not be deflected by massive bodies. Observation directly contradicts this: light bends around stars and galaxies. Gravitational lensing is the condensate acting on photons. The photon's w-spin is minimum but nonzero, producing a weak but real coupling to $C_{\mu\nu}$.

As a photon traverses the cosmos, it passes through the condensate field — through galaxy clusters, filaments, and the diffuse intergalactic condensate. Each traversal of a condensate concentration costs the photon a small amount of energy through this coupling. The energy transfer is governed by the photon-condensate cross section $\sigma(\omega)$ (CT-xiii). Over cosmological path lengths, the accumulated drag produces an additional redshift contribution proportional to the integrated condensate density along the line of sight:

$$z_{\text{drag}} \propto \int_0^{d_L} n_{\text{condensate}}(l)\,\sigma(\omega)\,dl$$

The total observed redshift is therefore:

$$z_{\text{obs}} = z_{\text{expansion}} + z_{\text{drag}}$$

These two taxes are not currently separable in standard cosmological measurements, which fit $z_{\text{obs}}$ to expansion models alone. The strataract drag contribution is absorbed into the inferred expansion history, slightly biasing measurements of $H_0$ and the dark energy equation of state. Separating them requires the line-of-sight signature described below.

**The separating signature.** Strataract drag correlates with large-scale structure along the line of sight. A photon passing through a cosmic void traverses lower condensate density than a photon passing through a filament at the same comoving distance. After correcting for expansion redshift, photons through voids should show slightly less total redshift than photons through filaments. This is a small effect — the condensate coupling for photons is weak — but it is in principle detectable with precision photometry across large samples at matched comoving distances. It would appear as a residual correlation between photon redshift and the integrated matter density along the line of sight, after expansion correction. This is a falsifiable prediction of the two-tax framework.

Note on gravitational lensing: the same minimum-nonzero w-spin coupling that produces strataract drag also produces gravitational lensing. Light bends around massive objects because the condensate concentration associated with those masses exerts a real force on the photon's minimum-w-spin state. The deflection angle is small — it requires the condensate concentration of a star or galaxy to produce a measurable effect — but it is nonzero and is observed. The Eddington deflection measurement of 1919, and all subsequent lensing observations, are direct evidence that photons are not zero-w-spin objects. They are minimum-w-spin objects, coupled to the condensate weakly but measurably.

### 6.9.1 Conjecture — Olbers Mechanism via Strataract Drag

*CONJECTURE — Proof target CT-xiii.*

The strataract drag of Section 6.9.0 provides a third mechanism contributing to the darkness of the night sky, supplementing the standard explanations of finite universe age and cosmological energy dilution. Light from sources at very large distances does not simply arrive redshifted and dimmed — it accumulates strataract drag over its entire path. Beyond a characteristic transition distance $d_{\text{flip}}$ (corresponding to redshift $z_{\text{flip}}$), the accumulated drag is sufficient to shift photon frequencies below the optical band entirely and to randomize their directional coherence. These photons arrive as real energy contributing to the diffuse background but carrying no recoverable source position or spectral identity.

The night sky is dark in the optical band partly because distant light has been taxed below visibility by strataract drag, not because the universe is finite or photons have been infinitely redshifted by expansion alone. This is a physically distinct mechanism with a distinct signature: it predicts that the transition to source-incoherent flux occurs at a specific $z_{\text{flip}}$ set by $\sigma(\omega)$ and the integrated condensate density, not by the expansion history alone.

### 6.9.2 Conjecture — CMB Monopole as Accumulated Strataract-Dragged Flux

*CONJECTURE — Proof target CT-xiii.*

The CMB monopole temperature receives a contribution from the accumulated flux of all photons from all sources beyond $z_{\text{flip}}$, progressively dragged by the strataract over cosmological path lengths until their directional and spectral coherence is fully randomized. A photon bath with no surviving phase or directional correlations is described by the maximum-entropy distribution — the Planck blackbody spectrum. The monopole temperature $T_{\text{CMB}} = 2.725$ K is set by the total energy density of this accumulated drag-randomized flux.

This conjecture does not address the CMB anisotropy structure. The acoustic peaks record baryon-photon plasma oscillations at recombination; those photons traveled from $z \approx 1100$ and carry genuine anisotropy information. The monopole conjecture concerns the isotropic background temperature only — the DC level on which the anisotropies sit — and proposes that this level is set in part by the accumulated strataract-dragged photon flux from all cosmic history.

**Falsification conditions:** (1) If CT-xiii derives $\sigma(\omega) = 0$ for all photon frequencies, both conjectures are falsified simultaneously — strataract drag does not exist for photons and the two-tax framework reduces to Tax 1 alone. This would also require an alternative explanation for gravitational lensing within the SCH framework. (2) If $\sigma(\omega) \neq 0$ but the resulting accumulated $T_{\text{CMB}}$ is inconsistent with 2.725 K, Conjecture 6.9.2 is falsified while 6.9.1 may still hold. (3) If precision photometry finds no residual correlation between source redshift and integrated line-of-sight matter density after expansion correction, the strataract drag contribution to redshift is constrained to be negligible, weakening both conjectures. (4) If $\sigma(\omega) \neq 0$ but gravitational lensing deflection angles are fully accounted for by the condensate coupling of massive matter alone with no photon coupling required, the minimum-nonzero-w-spin identification of the photon is falsified and both conjectures require revision.

---

# 7. Conclusion

We have proposed that the Einstein field equations are missing a source term representing the geometric organizational state of matter, and have derived that term from first principles — starting from the physical picture of matter as solitons with w-axis spin in an S³ cosmos.

Draft 2.0 established the correct logical order: the physical picture first, the mathematics as its encoding. The ground floor is three axioms — time is flat, space is flat, matter is a soliton with w-axis spin. From these three axioms, without additional postulates, the following fall out:

The origin of inertia. The origin of mass. The c asymptote as escape velocity from the S³ slice. Length contraction. Clock slowing. The matter-light phase distinction. Annihilation as w-spin cancellation. Spin quantization from S³ closure. The Pauli exclusion principle. The spin-statistics theorem. The discrete mass spectrum. The uncertainty principle as geometric cross-section. Electron orbital shapes. The double slit. Quantum entanglement without superluminal signaling. Variable c(t) as cosmic rotation readout. Matter stability as a function of cosmic epoch. Light predominance at epoch boundaries. The bounce as a matter-light-matter phase transition without singularity.

Draft 2.1 adds: Black holes as rotational processors rather than sinks. Antipodal convergence on $S^3$ as the coupling mechanism between local black hole emission and global $\omega(t)$. Coherence-forced halos as the physical origin of what appears as dark matter. The rotation curve flattening radius as a prediction correlated with central black hole mass. The M-sigma relation as a consequence of the coherence forcing scale.

Draft 2.3 revised Section 2.10a: the earlier claim that chirality inversion across the bounce is close to a default topological consequence was retracted, following the PT-1 analysis programme and its IVN-I convention correction. Chirality inversion per cycle was confirmed non-generic; the sympathetic nucleation mechanism for within-cycle matter surplus was noted as unaffected; a new coupling between the scalar condensate and the chirality sector in the torsion-active cosmological branch was identified as an open item pending independent verification.

**Draft 2.4 closes that item.** Appendix P v14 reports that three independent derivation routes — resolving a chain of internal errors across the intervening working papers, including one in the derivation used to reach this very draft — converge on the same torsion self-coupling coefficient. Chirality inversion per cycle remains confirmed non-generic, as it has been since Draft 2.2. The mechanism coupling $\eta$ to the chirality sector in Branch 2, open since Draft 2.3, is now established. What remains open — deliberately, and stated as such throughout this draft and in Appendix P — is purely numerical: the monodromy phase, the within-cycle matter surplus, and the size of the Branch 2 correction to the standard $a^{-3}$ dilution law all require the Bi-209 calibration before they become specific numbers rather than calculable forms.

The Einstein-Cartan-Dirac action is the mathematical encoding of this physical picture — not its source. GR is the exact zero-w-spin limit. The anomaly cluster is a set of predicted consequences, not motivating puzzles.

**The decisive next steps are:** (1) independent expert verification of the four theorems in Appendix P; (2) execution of the MaNGA-DES cross-match test (Test 4.1); (3) execution of the SLACS metallicity-lensing test (Test 4.2); (4) the Bismuth-209 laboratory calibration, now the single remaining gate on every numerical prediction in the chirality sector as well as the nuclear and galactic sectors; (5) the S³ standard ruler test; (6) derivation of the photon-condensate coupling cross section σ(ω) (CT-xiii); (7) derivation of the black hole condensate propagator (CT-vii), which is the prerequisite for both CT-xix (antipodal coupling) and the quantitative rotation curve flattening prediction; (8) empirical test of the rotation curve flattening radius versus central black hole mass correlation — awaiting direct dynamical BH mass measurements for a sufficient sample of late-type spirals (data gap confirmed by pipeline execution June 2026; expected from MBHBM* and WISDOM/ALMA programmes); (9) numerical evaluation of the now-established PT-1 monodromy calculation and the Branch 2 late-time correction, both fully well-posed and both awaiting only item (4).

---

# References

Boylan-Kolchin, M. (2023). Stress testing ΛCDM with high-redshift galaxy candidates. Nature Astronomy, 7, 731.

Hehl, F.W. et al. (1976). General relativity with spin and torsion. Reviews of Modern Physics, 48(3), 393.

Kibble, T.W.B. (1961). Lorentz invariance and the gravitational field. Journal of Mathematical Physics, 2(2), 212.

Labbe, I. et al. (2023). A population of red candidate massive galaxies ~600 Myr after the Big Bang. Nature, 616, 266.

NANOGrav Collaboration (2023). The NANOGrav 15-year data set: Evidence for a gravitational-wave background. Astrophysical Journal Letters, 951, L8.

Sciama, D.W. (1964). The physical structure of general relativity. Reviews of Modern Physics, 36(1), 463.

[Full reference list from Draft 1.5 retained in submission package]

---

*Appendices A, B, and C are unchanged from Draft 1.5 and are carried forward in the submission package. Appendix P is updated to v14.*

---

**End of Paper A — Draft 2.4**
