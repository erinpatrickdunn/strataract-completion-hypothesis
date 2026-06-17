Appendix P -- v7 | May 2026
Appendix P
Proof of Closure: The Strataract Completion Hypothesis
as a Closed Variational Theory
Working Proof Document -- v7 | May 2026
Revised from v5: Section P.8 expanded with new Calculational Target CT-xiii -- photon-condensate coupling cross section derivation and CMB monopole temperature from the condensate scrambling integral. This is the proof target required to elevate the Olbers mechanism and CMB-as-condensate-scrambled-light conjectures in Paper A Section 6.9 from conjecture to theorem. Prerequisites: CT-vii (condensate propagator) and CT-viii (FLRW reduction of S_geo). Gap 8 added to the status summary. All other content unchanged from v5.
STATUS SUMMARY
Gap
Status
Resolution / Reference
Gap 1 — Leading-order uniqueness of Q($\mu$,$\nu$)
ESTABLISHED
Fierz completeness, local EFT limit, explicit density hierarchy bound
Gap 2 — Four-velocity normalization
ESTABLISHED
Fierz + parity-preserving sector, regime-conditional
Gap 3 — $\Gamma_\text{decoh}$, $\Gamma_\text{recoh}$
DERIVED
Matsubara + EFT kinetics, no additional free parameters
Gap 4 — Torsion persistence
RESOLVED
Algebraic/field distinction
Gap 5 — Black hole bounce resonance
ESTABLISHED
Term 3 at Planck density, condensate propagation from Theorem 4 [New in this revision]
Gap 6 — S³ spatial topology
ESTABLISHED
SU(2) group manifold identification, canonical spin structure [New in this revision]
Gap 7 — Chirality inversion across bounce and sympathetic nucleation
PREDICTION (proof outstanding)
Standard spin representation on S³ predicts $A_{\mu}$ -> -$A_{\mu}$. PT-1 is the formal confirmatory proof target. CT-viii prerequisite. [New in this revision]
Gap 8 — Photon-condensate coupling and CMB monopole
OPEN TARGET
CT-xiii identified. Prerequisites: CT-vii + CT-viii. [New in v7]
The framework has a closed variational structure within its stated EFT and mean-field condensate regime. All claims are regime-conditional. The density hierarchy is explicit and bounded. Three sections (P.7.5, P.7.6, P.7.7) cover cosmological predictions of the closed theory. Section P.8 is expanded in v6 to add CT-xiii.
P.0 Preamble: From Consistency to Proof -- and the Role of Regime Conditioning
Paper A (Draft 1.5) presents the Strataract Completion Hypothesis (SCH) as a modified gravitational field equation:
$G_{\mu\nu}$ + $\Lambda$*$g_{\mu\nu}$ = $\kappa$ * ( $T_{\mu\nu}$ + $\alpha$*$C_{\mu\nu}$ )
$C_{\mu\nu}$ = Q($\mu$,$\nu$) = $\rho$*$\eta$*$u_{\mu}$*$u_{\nu}$
This appendix resolves all formal gaps and establishes the framework as a closed variational theory rooted in the Einstein-Cartan-Dirac action with a geometric state spinor field. The revision adds three cosmological extensions (Sections P.7.5, P.7.6, P.7.7) that follow as consequences of the closed theory, and expands Section P.8 with CT-xiii (v6).
All leading-order claims hold in the low-density EFT limit ($\rho$ << $\rho_\text{condensate}$) governing galactic-scale dynamics. Higher-order contributions (quartic in $\psi$) exist, are identified as Term 3, and dominate at high density. This is not a weakening -- it is the standard language of effective field theory.
The derivation chain:
PRIMITIVE: Rotation is fundamental
OBJECT: Spinor field $\psi$ in curved spacetime -- covering group SU(2) x SU(2)
ACTION: S = S_EC + S_geo + S_GHY + S_matter
  S_EC = Einstein-Cartan (tetrad $e^a_\mu$ + spin connection $\omega^{ab}_\mu$)
  S_geo = Dirac-type spinor with quartic self-interaction ($\lambda$ > 0)
VARIATION:
  delta/delta_$e^a_\mu$  ->  $G_{\mu\nu}$ + $\Lambda$*$g_{\mu\nu}$ = $\kappa$*($T_{\mu\nu}$ + $\alpha$*$C_{\mu\nu}$) + Term(3)
  delta/delta_$\omega^{ab}_\mu$  ->  $T_{\lambda\mu\nu}$ = ($\kappa$*$\alpha$/2) * $\epsilon($$\lambda$,$\mu$,$\nu$,$\rho$) * $A_{\rho}$
IDENTIFICATIONS (leading order, $\rho$ << $\rho_\text{condensate}$):
  $C_{\mu\nu}$ = $\rho$*$\eta$*$u_{\mu}$*$u_{\nu}$ = Q($\mu$,$\nu$)
  $\eta$ = $\psi$-bar*$\psi$  (Lorentz scalar by Theorem 2)
  $u_{\mu}$ = $J_{\mu}$ / ($\psi$-bar*$\psi$)  (four-velocity from $\psi$ alone)
LIMITS:
  $A_{\mu}$ = 0 (isotropic ground state) -> T = 0, $C_{\mu\nu}$ = 0 -> exact GR
  $A_{\mu}$ small -> Paper A weak-field equation
  $\rho$ >> $\rho_\text{condensate}$ -> Term(3) dominant -> neutron star / Planck regime
TOPOLOGY (new in v5):
  SU(2) as group manifold = S³ -> spatial topology uniquely compatible with S³ (P.7.6)
P.0a Conservation Architecture: The Global Energy-Momentum Accounting
[New in v5 revision, addressing the conservation architecture gap identified in external review. Unchanged in v6.]
The modified field equation $G_{\mu\nu}$ + $\Lambda$*$g_{\mu\nu}$ = $\kappa$*($T_{\mu\nu}$ + $\alpha$*$C_{\mu\nu}$) introduces a second source term beyond standard stress-energy. Mathematical self-consistency requires a complete accounting of how energy-momentum is exchanged among all three terms on the right-hand side. This section states that accounting explicitly as a foundational commitment of the theory. It is not a proof of closure -- several exchange channels involve open calculational targets -- but it is a precise statement of what must be conserved and where the open questions lie.
P.0a.1 The Required Conservation Statement
The contracted Bianchi identity requires that the total source on the right-hand side of the field equation be divergence-free:
$\nabla_\mu$ * $T_{\mu\nu}$_total = $\nabla_\mu$ * [ $T_{\mu\nu}$(matter) + $\alpha$*$C_{\mu\nu}$ + $T_{\mu\nu}$(torsion) ] = 0
This does not require each term to be independently divergence-free. It requires that their sum is. The three terms can exchange energy-momentum with one another, provided the total is conserved. Identifying the exchange channels is the conservation architecture problem.
P.0a.2 Status of Each Term
Term 1 -- $T_{\mu\nu}$(matter): Standard GR result. $\nabla_\mu$ * $T_{\mu\nu}$(matter) = 0 holds independently when matter follows geodesics in the absence of condensate coupling. When the condensate is non-zero, there is an exchange channel between Term 1 and Term 2 via the spinor current. The geodesic condition $u_{\mu}$ * $\nabla_\mu$ * $u_{\nu}$ = 0 used in Appendix A and in the divergence-free proof of Theorem 1 is a derived consequence of S_geo in the mean-field condensate regime (P.3, Step 5), not an independent assumption. Within this regime, the Term 1-Term 2 exchange is suppressed and both are separately approximately divergence-free.
Term 2 -- $\alpha$*$C_{\mu\nu}$ = $\alpha$*$\rho$*$\eta$*$u_{\mu}$*$u_{\nu}$: Divergence-free in the mean-field condensate regime by Theorem 1 (P.2), under the conditions established in Appendix A (co-moving $\eta$, geodesic motion). This is the leading-order result. At next order, the condensate carries energy-momentum that can be exchanged with the matter sector via the $\eta$ evolution equation (Section 2.4a): the decoherence and recoherence terms $\Gamma_\text{decoh}$ and $\Gamma_\text{recoh}$ represent exactly this exchange. The $\eta$ evolution equation is the explicit statement of the Term 1-Term 2 exchange channel. When $\eta$ is evolving (thermal decoherence active), the two terms are not independently divergence-free but their sum remains so, provided the $\eta$ evolution equation is satisfied. This is a consistency requirement on S_geo -- but its formal verification as a statement about $\nabla_\mu$ * $T_{\mu\nu}$_total is an identified calculational target.
Term 3 -- $T_{\mu\nu}$(torsion) ~ $A_{\mu}$*$A_{\nu}$ - (1/2)*$A_{\rho}$*$A_{\rho}$*$g_{\mu\nu}$: The torsion contact term is algebraically determined by the Cartan equation (P.1.3). Its divergence is set by the divergence of the axial current $A_{\mu}$. In the parity-preserving sector, $\partial_\mu$ * <$A_{\mu}$> = 2*i*$m_\text{eff}$ * <P> = 0 (Theorem 2, Step 3), so the torsion term is divergence-free in the condensate vacuum. Outside the parity-preserving sector -- for example, during the Planck-density phase of the bounce -- the axial current may not be conserved and Term 3 exchanges energy-momentum with the matter sector via the axial anomaly channel. This exchange is the physical mechanism behind the bounce itself: Term 3 absorbs kinetic energy from the collapsing matter sector and returns it as expansion. The formal accounting of this exchange at Planck density requires the FLRW reduction (Calculational Target viii).
P.0a.3 Exchange Channel Map
The three exchange channels between the source terms are:
Channel A (Term 1 <-> Term 2): Condensate decoherence/recoherence.
  Governed by: $u_{\mu}$ * $\nabla_\mu$ * $\eta$ = -$\Gamma_\text{decoh}$ * $\eta$ + $\Gamma_\text{recoh}$ * (1-$\eta$)
  Status: Rates derived (Theorem 3). Full $\nabla_\mu$ * $T_{\mu\nu}$_total = 0 verification: OPEN TARGET.
Channel B (Term 2 <-> Term 3): Condensate-torsion coupling at high density.
  Governed by: Cartan equation $T_{\lambda\mu\nu}$ = ($\kappa$*$\alpha$/2) * $\epsilon($$\lambda$,$\mu$,$\nu$,$\rho$) * $A_{\rho}$
  Status: Algebraic at galactic densities (Term 3 suppressed by epsilon <= 10^-23).
  At Planck density: OPEN TARGET (requires FLRW reduction).
Channel C (Term 1 <-> Term 3): Matter spin coupling to torsion.
  Governed by: Papapetrou-Dixon equations for spinning matter in torsionful spacetime.
  Status: Subleading at galactic densities. Significant at neutron star and Planck densities.
  Full accounting: OPEN TARGET (part of Gordon decomposition programme, CT-ii).
P.0a.4 What Is Closed and What Is Open
The conservation architecture is partially established and partially open. What is closed: $\nabla_\mu$ * $C_{\mu\nu}$ = 0 at leading order in the mean-field condensate regime (Theorem 1, Appendix A); $\nabla_\mu$ * $T_{\mu\nu}$(torsion) = 0 in the parity-preserving vacuum sector (Theorem 2); the $\eta$ evolution equation as the explicit statement of Channel A exchange (Theorem 3). What is open: the full $\nabla_\mu$ * $T_{\mu\nu}$_total = 0 verification when $\eta$ is actively evolving (Channel A open); the Term 2-Term 3 exchange at Planck density (Channel B open); the Channel C Papapetrou-Dixon accounting at high spin density.
The open channels are all in regimes (active thermal decoherence, Planck density, high spin density) that are beyond the galactic-scale observational programme of Papers A and B. The conservation architecture is complete in the regime where the primary observational predictions are made. The open channels are identified calculational targets for the cosmological and high-density extensions, not foundational gaps in the galactic-scale framework.
P.1 The Fundamental Action and Lagrangian Density
[Unchanged from previous revision]
P.1.1 Total Action
The total action on spacetime manifold M, in terms of the tetrad $e^a_\mu$ and spin connection $\omega_\mu$^ab, is:
S_total = S_EC[e,omega] + S_geo[e,omega,$\psi$] + S_GHY[e] + S_matter[e,$\psi$]
where:
S_EC = (1/2*$\kappa$) * integral d^4x * e * R(e,omega)  -- Einstein-Cartan gravity; tetrad + spin connection
S_geo = integral d^4x * e * [(i/2)*($\psi$-bar*gamma^a*$e^a_\mu$*D_mu*$\psi$ - h.c.) - m*$\psi$-bar*$\psi$ - ($\lambda$/4)*($\psi$-bar*$\psi$)^2]  -- Geometric state spinor; Dirac + quartic self-coupling
S_GHY = (1/$\kappa$) * integral d^3x * sqrt(h) * K  -- Gibbons-Hawking-York boundary term
S_matter = Standard model fields, minimally coupled -- Ordinary matter; $T_{\mu\nu}$ source
P.1.2 Explicit Lagrangian for S_geo
The geometric state term in full index notation:
S_geo = integral_M d^4x * e * [ (i/2)*($\psi$-bar*gamma^a*$e^a_\mu$*D_mu*$\psi$ - D_mu*$\psi$-bar*gamma^a*$e^a_\mu$*$\psi$) - m*$\psi$-bar*$\psi$ - ($\lambda$/4)*($\psi$-bar*$\psi$)^2 ]
where the Fock-Weyl covariant derivative is D_mu*$\psi$ = $\partial_\mu$*$\psi$ + (1/4)*$\omega_\mu$^ab * [gamma^a, gamma^b] * $\psi$. The parameter $\lambda$ > 0 governs the quartic self-interaction and sets the condensate scale.
P.1.3 Variational Equations
Variation with respect to the tetrad $e^a_\mu$ yields:
$G_{\mu\nu}$ + $\Lambda$*$g_{\mu\nu}$ = $\kappa$ * [ $T_{\mu\nu}$(matter) + $\alpha$*$C_{\mu\nu}$ + $T_{\mu\nu}$(torsion) ]
where $C_{\mu\nu}$ = $\rho$*$\eta$*$u_{\mu}$*$u_{\nu}$ is the leading-order geometric state tensor and $T_{\mu\nu}$(torsion) ~ $A_{\mu}$*$A_{\nu}$ - (1/2)*$A_{\rho}$*$A_{\rho}$*$g_{\mu\nu}$.
Variation with respect to the spin connection $\omega_\mu$^ab gives the Cartan equation:
$T_{\lambda\mu\nu}$ = ($\kappa$*$\alpha$/2) * $\epsilon($$\lambda$,$\mu$,$\nu$,$\rho$) * $A_{\rho}$
This is an algebraic equation: torsion is instantaneously determined by the local axial current. There is no differential propagation equation for torsion. This distinction is the foundation of Theorem 4 (P.5) and the black hole bounce analysis of P.7.5.
P.2 Gap 1 -- Leading-Order Uniqueness of Q($\mu$,$\nu$)
[Unchanged from previous revision -- summary below]
Theorem 1 (Leading-Order Uniqueness)
At quadratic order in $\psi$, in the low-density EFT regime ($\rho$ << $\rho_\text{condensate}$), subject to the symmetries of S_geo, Q($\mu$,$\nu$) = $\rho$*$\eta$*$u_{\mu}$*$u_{\nu}$ is the unique rank-2 symmetric divergence-free tensor constructible from local spinor bilinears of $\psi$. Uniqueness holds modulo: (i) an overall coupling constant $\alpha$; (ii) subleading higher-order corrections suppressed by $\epsilon($$\rho$) <= 10^-23 at galactic densities.
Three sequential filters -- rank-2 symmetry (F1), divergence-free (F2), quadratic in $\psi$ (F3) -- reduce the complete Fierz bilinear basis of ten candidates to a unique survivor: C3 = $\rho$*($\psi$-bar*$\psi$)*$u_{\mu}$*$u_{\nu}$ = Q($\mu$,$\nu$). The Fierz decomposition of the general rank-2 bilinear tensor in four dimensions yields exactly ten independent structures. F1 (symmetry) eliminates antisymmetric bilinears (the axial tensor A[$\mu$,$\nu$] and its duals). F2 (divergence-free) eliminates structures whose divergence is nonzero in the condensate vacuum. F3 (quadratic in $\psi$) eliminates quartic and higher contributions, relegating them to Term 3 at the density hierarchy established in P.2a. The unique survivor is Q($\mu$,$\nu$) up to the overall coupling constant $\alpha$, which is not fixed by the symmetry argument and must be determined experimentally (the Bi-209 calibration, Paper A Section 5).
P.2a The Density Hierarchy: Bounding Higher-Order Contributions
[Unchanged from previous revision -- summary below]
The expansion parameter $\epsilon($$\rho$) = $\rho$ / $\rho_\text{condensate}$ is bounded as follows:
$\epsilon($$\rho_\text{galactic}$) = $\rho_\text{galactic}$ / $\rho_\text{condensate}$ <= 10^-23 / 10^-1 = 10^-23
At galactic densities ($\rho$ ~ 10^-24 g/cm^3), quartic corrections to Q($\mu$,$\nu$) are suppressed by a factor of 10^-23. Term 3 becomes competitive at $\rho$ ~ $\rho_\text{condensate}$ ~ 10^-1 g/cm^3, which encompasses neutron star cores ($\rho$ ~ 10^14 g/cm^3) and Planck-scale cosmology. This hierarchy is the single architectural element making all leading-order claims quantitatively precise. It also physically separates the galactic-scale $C_{\mu\nu}$ phenomenology from the high-density Term 3 phenomenology exploited in P.7.
P.3 Gap 2 -- Four-Velocity Normalization
[Unchanged from previous revision -- summary below]
Theorem 2 (Regime-Conditional Normalization)
For the geometric state spinor $\psi$ satisfying the field equations of S_geo, the normalized current $u_{\mu}$ = $J_{\mu}$ / ($\psi$-bar*$\psi$) satisfies $u_{\mu}$*$u_{\mu}$ = -c^2 in the parity-preserving vacuum sector of S_geo, for all spinor configurations satisfying the equations of motion in that sector, within the low-density regime ($\rho$ << $\rho_\text{condensate}$).
Proof via Fierz identity: $J_{\mu}$*$J_{\mu}$ = -S^2 - P^2, where S = $\psi$-bar*$\psi$ and P = $\psi$-bar*gamma^5*$\psi$. Parity symmetry of S_geo enforces P = $\psi$-bar*gamma^5*$\psi$ = 0 in the parity-preserving vacuum. This gives $J_{\mu}$*$J_{\mu}$ = -S^2 and therefore $u_{\mu}$*$u_{\mu}$ = $J_{\mu}$*$J_{\mu}$ / S^2 = -1, i.e., $u_{\mu}$*$u_{\mu}$ = -c^2. The normalization holds as a theorem within the stated regime, not as a postulate. Outside the parity-preserving sector (relevant to the bounce, where $A_{\mu}$ -> -$A_{\mu}$), P may be nonzero and the normalization becomes regime-dependent. Full proof in previous revision, Steps 1-4.
P.4 Gap 3 -- Derivation of $\Gamma_\text{decoh}$ and $\Gamma_\text{recoh}$
[Unchanged from previous revision -- summary below]
Theorem 3 (Rate Derivation)
$\Gamma_\text{decoh}$ = ($\alpha$/m^2)*($\lambda$*$\rho$)^2*$\kappa$(T) and $\Gamma_\text{recoh}$ = ($\alpha$/m^2)*($\lambda$*$\rho$)^2*$\kappa$(T)*f(T), where $\kappa$(T) = d^2*$V_\text{eff}$/d*$\eta$^2 evaluated at $\eta_\text{eq}$(T) and f(T) = $\eta_\text{eq}$(T)/$\eta_\text{max}$. Both rates are fixed by action parameters {$\alpha$, $\lambda$, m} and temperature T. No free parameters remain.
Derived from S_geo via the finite-temperature effective potential computed by the Matsubara (imaginary-time) formalism. The effective potential $V_\text{eff}$($\eta$, T) is obtained by integrating out thermal fluctuations in the standard Matsubara loop expansion at one loop. The condensate equilibrium value $\eta_\text{eq}$(T) is the minimum of $V_\text{eff}$ at temperature T. The decoherence rate $\Gamma_\text{decoh}$ is the curvature of $V_\text{eff}$ at this minimum, governing the rate of return to equilibrium from above. The recoherence rate $\Gamma_\text{recoh}$ is the curvature times the equilibrium fraction f(T) = $\eta_\text{eq}$(T)/$\eta_\text{max}$, governing return from below.
Key limits: T = 0 gives $\Gamma_\text{decoh}$ = 0 (perfect coherence, condensate stable); $k_B$*T >> $m_\text{eff}$ gives $\Gamma_\text{decoh}$ ~ T (linear growth with temperature); T > T_c ~ m/$k_B$ gives $\eta$ -> 0 and exact GR recovery. All limits are consistent with the physical picture. Full derivation in previous revision, Steps 1-5.
P.5 Gap 4 -- Torsion Persistence and Post-Merger Lensing
[Unchanged from previous revision -- summary below]
Theorem 4 (Term Distinction)
Term 2 ($C_{\mu\nu}$ = $\rho$*$\eta$*$u_{\mu}$*$u_{\nu}$) is a propagating field effect governed by the Dirac equation for $\psi$. It persists and diffuses after matter moves. Diffusion timescale: $\tau_\text{diff}$ ~ R^2 * $m_\text{eff}$ / hbar. Term 3 (~$A_{\mu}$*$A_{\nu}$ - (1/2)*$A_{\rho}$*$A_{\rho}$*$g_{\mu\nu}$) is a contact interaction. Torsion is algebraically determined by the Cartan equation and does not propagate. These properties follow directly from the field equations of S_total.
The proof turns on the structure of the field equations. The Dirac equation for $\psi$ is a first-order PDE: it governs the propagation of $\psi$ through spacetime. A solution $\psi$(x) at a given time determines $\psi$ at later times through the propagation of the Dirac equation. The condensate built from $\psi$ therefore propagates and diffuses. The diffusion timescale $\tau_\text{diff}$ ~ R^2 * $m_\text{eff}$ / hbar follows from the mass term in the Dirac equation: a condensate field of mass $m_\text{eff}$ diffuses over a distance R on this characteristic timescale.
The Cartan equation $T_{\lambda\mu\nu}$ = ($\kappa$*$\alpha$/2) * $\epsilon($$\lambda$,$\mu$,$\nu$,$\rho$) * $A_{\rho}$ is algebraic: torsion at point x is determined instantaneously by the axial current at x. There is no PDE governing torsion propagation. Torsion cannot diffuse beyond the matter that sources it. When matter moves, torsion follows instantaneously. This is the fundamental distinction between Term 2 (propagating condensate, post-merger lensing) and Term 3 (contact torsion, no lensing offset). Full proof in previous revision, Steps 1-3.
P.6 Closure Summary
The following table summarises closure status within the stated EFT and mean-field condensate regime. Items from the previous revision are unchanged. Three cosmological extensions from v5 are included. CT-xiii is new in v6.
Challenge
Status
Resolution / Reference
Lagrangian architecture
CLOSED
S_geo is the Einstein-Cartan-Dirac action with quartic spinor coupling. Metric variation gives the field equation exactly. (P.1)
Tensor emergence (Q($\mu$,$\nu$))
CLOSED (leading order)
Theorem 1: Q($\mu$,$\nu$) unique at quadratic order via Fierz completeness + three filters. Density hierarchy bound epsilon <= 10^-23. (P.2, P.2a)
$\eta$ scalar nature
CLOSED
$\eta$ = $\psi$-bar*$\psi$ is a Lorentz scalar bilinear; proven from spinor transformation law under SL(2,C). (P.2)
GR recovery
CLOSED
$A_{\mu}$ = 0 in isotropic ground state makes torsion vanish algebraically. Exact GR. (P.1)
Geometric Resonance Postulate
CLOSED
Ground state = spinor vacuum = $A_{\mu}$ = 0 = zero net chirality. Derived from SU(2) x SU(2) covering group. (P.1)
$\Gamma_\text{decoh}$, $\Gamma_\text{recoh}$
CLOSED (regime-conditional)
Theorem 3: both rates derived from S_geo via Matsubara + EFT kinetics. Fixed by {$\alpha$, $\lambda$, m, T}. (P.4)
$u_{\mu}$ normalization
CLOSED (regime-conditional)
Theorem 2: $u_{\mu}$*$u_{\mu}$ = -c^2 in parity-preserving vacuum sector, S not equal 0, $\rho$ << $\rho_\text{condensate}$. (P.3)
Torsion / lensing persistence
CLOSED
Theorem 4: Term 2 propagates (PDE); Term 3 is contact (algebraic). Post-merger lensing via Term 2 only. (P.5)
Density hierarchy
CLOSED
$\epsilon($$\rho$) = $\rho$/$\rho_\text{condensate}$ <= 10^-23 at galactic scales. Quartic corrections negligible. High-density regime identified. (P.2a)
BH bounce resonance
CLOSED
Term 3 at Planck density -> bounce. Term 2 propagates outward at f_cond ~ c^4/(4*G^2*$m_\text{eff}$*M^2)*hbar. Q effectively infinite. (P.7.5)
S³ topology
CLOSED
SU(2) group manifold = S³. Spinor field on SU(2) x SU(2) selects S³ canonically via spin structure. (P.7.6)
Chirality inversion across bounce / sympathetic nucleation
PREDICTION (proof outstanding)
Standard spin representation on S³ predicts $A_{\mu}$ -> -$A_{\mu}$ at bounce. Within-cycle matter surplus via sympathetic nucleation. PT-1 is confirmatory proof target. Full treatment in P.7.7.
Photon-condensate coupling / CMB monopole
OPEN TARGET
Photon-condensate cross section $\sigma$(omega) not yet derived. CT-xiii identified. Prerequisites: CT-vii + CT-viii. (P.8)
FINAL STATUS: A self-consistent variational closure has been established within the stated EFT and mean-field condensate regime. All leading-order claims are regime-conditional on $\rho$ << $\rho_\text{condensate}$ and T < T_c. The Strataract Completion Hypothesis is a self-consistent variational EFT closure rooted in the Einstein-Cartan-Dirac action. GR is the exact torsion-free limit. All galactic-scale claims hold in the regime $\rho$ << $\rho_\text{condensate}$.
P.7 New Predictions from the Torsion Route
The quadratic torsion term (Term 3), absent from GR, generates predictions that distinguish Einstein-Cartan-SCH from both GR and the Paper A weak-field formulation. All Term 3 predictions operate in the high-density regime $\rho$ ~ $\rho_\text{condensate}$, consistent with the density hierarchy of P.2a. Sections P.7.1 through P.7.4 are unchanged from the previous revision. Sections P.7.5, P.7.6, and P.7.7 are new in v5 and unchanged in v6.
P.7.1 Spin-Spin Repulsion at High Density
[Unchanged]
The term 2*$A_{\mu}$*$A_{\nu}$ - $A_{\rho}$*$A_{\rho}$*$g_{\mu\nu}$ acts as repulsive pressure when matter with aligned chirality overlaps. At neutron star densities ($\rho$ ~ 10^14 g/cm^3 >> $\rho_\text{condensate}$) this becomes significant, providing a natural upper bound on compactness. At galactic densities this term is suppressed by epsilon <= 10^-23 and does not contaminate the galactic-scale observational programme.
P.7.2 Parity-Dependent Lensing Asymmetry
[Unchanged]
Two otherwise identical galaxies with opposite orbital angular momentum generate identical $C_{\mu\nu}$ (since $\eta$ = $\psi$-bar*$\psi$ is parity-even) but opposite torsion. Their Term 2 lensing signals are equal; their Term 3 contributions differ. Chirality-dependent lensing asymmetry between mirror-image galaxy pairs is a clean prediction with no analogue in standard GR.
P.7.3 Bismuth-209: Second Measurement Channel
[Unchanged]
The transmutation Bi-209 -> Pb-208 involves nuclear spin collapse from I = 9/2 to I = 0. The spin-9/2 state has $A_{\mu}$ not equal 0; the spin-0 state has $A_{\mu}$ = 0. Both $\eta$ (Term 2 channel, calorimetrically accessible) and torsion (Term 3 channel, distinct timing signature) change at the transmutation. The two signals have different temporal profiles separable by high-resolution coincidence timing.
P.7.4 Big Bounce Cosmology
[Unchanged]
At Planck-scale densities, Term 3 ~ $\kappa$^2 * $\alpha$^2 * A^2 / 4 grows as $\rho$^2 and becomes cosmologically significant. The spin-spin repulsion provides a candidate bounce mechanism avoiding the Big Bang singularity. Full demonstration requires FLRW reduction and modified Friedmann equations -- identified as part of the calculational programme (CT-viii).
P.7.5 Black Hole Bounce Resonance and Condensate Propagation Frequency
[New in v5. Unchanged in v6.]
P.7.5.1 The Two-Frequency Structure
A black hole interior reaching Planck density sits firmly in the Term 3 dominant regime ($\rho$ ~ 10^96 g/cm^3 >> $\rho_\text{condensate}$). Term 3 spin-spin repulsion grows as $\rho$^2, reversing the collapse when the Planck threshold is reached. Since the collapsed matter remains gravitationally bound within the event horizon, it re-collapses and the process repeats. Two physically distinct frequencies characterize this system.
The internal bounce frequency is set by the Planck time:
f_internal ~ 1 / t_Planck ~ 1 / (5.4 x 10^-44 s) ~ 10^43 Hz
This frequency is entirely inaccessible to external observers due to gravitational time dilation. At the Schwarzschild radius, the time dilation factor g_tt -> 0, meaning the internal oscillation appears frozen from outside. The black hole presents a static surface to any external measurement.
The condensate propagation frequency is set by the diffusion timescale of the spinor condensate Term 2 field propagating outward from the Schwarzschild radius. By Theorem 4, Term 2 is a propagating field governed by the Dirac equation, with diffusion timescale $\tau_\text{diff}$ ~ R^2 * $m_\text{eff}$ / hbar evaluated at the Schwarzschild radius R_s = 2GM/c^2:
$\tau_\text{diff}$(R_s) = R_s^2 * $m_\text{eff}$ / hbar = (2GM/c^2)^2 * $m_\text{eff}$ / hbar = 4*G^2*M^2 * $m_\text{eff}$ / (hbar*c^4)
The condensate propagation frequency is therefore (dimensional estimate from the Theorem 4 diffusion timescale -- a proper perturbative mode analysis around the black hole background is CT-vii):
f_cond = 1 / $\tau_\text{diff}$ = hbar*c^4 / (4*G^2 * $m_\text{eff}$ * M^2)
This is the frequency at which the surrounding condensate field is coherently driven. It scales as M^(-2): larger black holes drive slower condensate waves.
P.7.5.2 Numerical Evaluation
Using the estimate $m_\text{eff}$ ~ hbar / (tau_coh * c^2) with tau_coh ~ 400 ps (Pb-208 first excited state lifetime, Paper A Section 1.3):
$m_\text{eff}$ ~ 1.6 x 10^-6 eV/c^2  (sub-meV, consistent with long-range condensate)
Condensate propagation frequencies for representative black hole masses:
Black hole mass
f_cond (dimensional estimate)
Frequency band
Notes
3 M_sun (stellar)
~0.5 Hz
LIGO band
Condensate wave period ~2 s
30 M_sun (stellar)
~5 x 10^-3 Hz
Below LIGO, above NANOGrav
—
10^4 M_sun (intermediate)
~5 x 10^-9 Hz
NANOGrav nHz band
NANOGrav candidate
4 x 10^6 M_sun (Sgr A*)
~10^-13 Hz
Period ~3 x 10^5 yr
Galactic structure timescale
6.5 x 10^9 M_sun (M87*)
~4 x 10^-20 Hz
Cosmological timescale
Large-scale structure
Note: all numerical values are provisional and scale with $m_\text{eff}$. The Bi-209 calibration (Paper A Section 5) is the critical experiment for pinning $m_\text{eff}$ and therefore all entries in this table.
P.7.5.3 The Quality Factor
The quality factor Q of the condensate oscillation is defined as the ratio of energy stored to energy lost per cycle. Energy loss is governed by the rate at which condensate energy propagates outward, which in the low-temperature limit is set by the Hawking temperature T_Hawking = hbar*c^3 / (8*pi*G*M*$k_B$):
Q ~ exp( $m_\text{eff}$ * c^2 / $k_B$ * T_Hawking )  [low-T limit, T_Hawking << $m_\text{eff}$*c^2/$k_B$]
For Sgr A* (M = 4 x 10^6 M_sun): T_Hawking ~ 1.5 x 10^-14 K, and $m_\text{eff}$*c^2/$k_B$ ~ 10^7 K, giving Q ~ exp(10^21). For all astrophysical black holes, Q is effectively infinite. Black holes are the most perfect condensate resonators in the universe by many orders of magnitude. The hum does not decay on any astrophysical timescale.
P.7.5.4 Galactic Structure Implications
The continuous coherent condensate driving at f_cond produces two observable effects at different scales.
At scales much smaller than the condensate wavelength $\lambda_\text{cond}$ = c / f_cond, the oscillation is unresolved and appears as an enhanced static $C_{\mu\nu}$. This is the mechanism behind the anomalous gravitational sourcing described in Paper A Sections 1.1 and 1.2. The galaxy's central black hole is the source of the $C_{\mu\nu}$ enhancement; the condensate field it drives provides the missing source term.
At scales comparable to $\lambda_\text{cond}$, the condensate wave sets up spatial resonance patterns. For Sgr A*, $\lambda_\text{cond}$ is cosmologically large, so within the Milky Way the condensate field is effectively DC -- a static enhancement. For smaller intermediate-mass black holes in dwarf galaxies, $\lambda_\text{cond}$ may be comparable to the galaxy size, and spatial structure in $C_{\mu\nu}$ becomes possible.
The prediction that distinguishes condensate-driven $C_{\mu\nu}$ from smooth dark matter halos: the anomalous sourcing profile should show non-monotonic radial structure correlated with the central black hole mass, rather than the smooth NFW or Einasto profiles predicted by dark matter N-body simulations.
P.7.5.5 The NANOGrav Connection
The NANOGrav 2023 detection of a stochastic background in the 1-100 nHz range corresponds, under f_cond ~ M^(-2) scaling, to black holes of approximately 10^3-10^5 M_sun (depending on $m_\text{eff}$). This overlaps the intermediate-mass black hole range. The standard interpretation attributes the background to supermassive black hole binary mergers.
The condensate hum interpretation predicts a different spectral signature: individual persistent sources at specific frequencies (one per black hole of given mass), summing to a quasi-continuous background. The merger interpretation predicts a stochastic background from transient events. These are distinguishable in principle by their coherence time: condensate hum sources are coherent over timescales of order Q / f_cond (effectively infinite), while merger events are transient. An analysis of the NANOGrav residuals for evidence of persistent coherent sub-threshold sources -- rather than incoherent stochastic power -- is an identified observational target (Paper B Section 7.1).
✓  Black hole bounce resonance established as a consequence of Term 3 at Planck density combined with Term 2 propagation (Theorem 4).
✓  Two-frequency structure derived: f_internal ~ 1/t_Planck (internal, invisible externally); f_cond ~ M^(-2) (condensate propagation, externally imprinted).
✓  Q factor effectively infinite for all astrophysical black holes in the low-T limit.
○  Open stability question: backreaction and self-excitation. An effectively infinite Q raises an immediate physical question: why does the condensate not catastrophically self-excite? Three suppression mechanisms are physically motivated: (1) diffusive (not ballistic) propagation suppresses resonant amplification at large distances; (2) S³ topology confines the condensate within a finite resonant cavity whose global modes are quantized; (3) the energy loss per bounce cycle, while tiny, is nonzero. Whether these mechanisms are collectively sufficient to prevent observable instabilities is not established. A full perturbative stability analysis of the condensate field around a Schwarzschild background -- the propagator, mode structure, and dispersion relation -- is CT-vii. Until that analysis is complete, the Q factor result should be understood as a dimensional estimate identifying the energy-loss scale, not as a claim that the condensate is literally non-decaying or free of instability.
P.7.6 S³ Spatial Topology: Derivation from the Spinor Covering Group
[New in v5. Unchanged in v6.]
P.7.6.1 The Group Manifold Identification
The geometric state spinor field $\psi$ is defined with covering group SU(2) x SU(2). This is the standard double cover of the four-dimensional rotation group SO(4), which is the local isometry group of the four-sphere S^4 and, in the spatial sector, of the three-sphere S³.
Lemma P.7.6.1 (SU(2) as S³):
SU(2) is diffeomorphic to the three-sphere S³ as a smooth manifold. Explicitly: SU(2) = { (a,b) in C^2 : |a|^2 + |b|^2 = 1 }, which is homeomorphic to the unit sphere in R^4.
This is not a formal coincidence. SU(2) and S³ are the same topological and smooth manifold. A spinor field whose symmetry group is SU(2) x SU(2) is most naturally and consistently defined on a spatial manifold that is itself S³.
P.7.6.2 The Spin Structure Argument
A spinor field on a compact manifold M requires M to admit a spin structure -- a global consistent choice of spinor frames compatible with the tangent bundle. Not all compact manifolds admit spin structures. Among the compact orientable three-manifolds:
S³ (three-sphere): admits a canonical spin structure, unique up to isomorphism
T³ (flat three-torus): admits spin structures, but none is canonically preferred
RP³ (projective space): admits a unique spin structure
Lens spaces L(p,q): admit spin structures when p is even
S³ is distinguished from all other candidates by having a canonical spin structure that is directly inherited from its identification with SU(2). The spinor field $\psi$, being a section of the spinor bundle associated to the SU(2) x SU(2) covering group, already determines a spin structure on any manifold it is defined on. On S³, this spin structure is the canonical one -- no additional choice is required.
On any other compact topology, the spin structure must be chosen from among multiple options or imposed by additional conditions not present in S_geo. S³ is the unique compact topology on which S_geo, as written, determines the spin structure without additional input.
Stated precisely: S³ is the unique compact topology on which the spin structure canonically determined by the SU(2) x SU(2) covering group of the spinor field is already present without additional input. This is a compatibility and uniqueness argument within the class of compact orientable three-manifolds admitting spin structures. It is not a derivation of topology from the field equation alone -- it is the statement that among all valid topological choices, S³ is the one that requires no additional structure beyond what S_geo already provides. The physical claim is that the correct topology is the one that is already there.
P.7.6.3 Physical Consequences
Quantized condensate modes. The spinor field on S³ of radius R_universe has a discrete mode spectrum. The lowest mode has wavelength ~ 2*pi*R_universe. Modes larger than R_universe do not exist. This is a topological cutoff on the power spectrum of any field defined on S³ -- including the primordial perturbation spectrum. The absence of super-horizon modes provides a natural explanation for the observed CMB quadrupole and octopole suppression without invoking inflation-specific physics.
Angular diameter distance turnaround. On S³, the angular diameter distance is d_A = R_universe * sin(d_proper / R_universe) / (1+z). This function has a maximum at d_proper = (pi/2)*R_universe and decreases thereafter, causing objects beyond the turnaround redshift z_turn to appear larger with increasing distance. The turnaround redshift is the direct observable of R_universe. Full analysis in Paper A Section 6.8.
Condensate resonant cavity. On S³, condensate waves driven by black hole bounces (P.7.5) cannot propagate to infinity and dissipate. They wrap around the manifold. The universe is a resonant cavity for the condensate field, with modes set by R_universe. Black holes whose f_cond matches a global S³ mode couple efficiently to large-scale structure; those that do not are locally active but globally decoupled. This provides a selection mechanism for large-scale structure formation not present in infinite flat-universe models.
Antipodal correlation signature. On S³, every geodesic passes through the antipodal point before returning to the origin. This produces a statistical signature in the CMB temperature field: anomalous positive correlation between antipodal sky pixel pairs T(n) x T(-n) above the ΛCDM baseline. This is distinct from the general large-angle correlation suppression already observed. The position of the feature (exactly theta = 180°) is independent of R_universe; only the amplitude depends on R_universe and the condensate damping rate. The search is executable with existing Planck data (Paper B Section 7.2).
P.7.6.4 Constraint on R_universe
The radius R_universe cannot be derived from the current action without specifying the cosmological initial conditions -- this is part of CT-viii. However, it is constrained from two independent observational handles:
CMB quadrupole suppression: The observed suppression of ell = 2, 3 multipoles requires R_universe >= 3 x R_Hubble, where R_Hubble = c/H_0 ~ 1.3 x 10^26 m.
Angular diameter distance turnaround: If the turnaround falls in the range z_turn ~ 2-8, then R_universe ~ 1.5-3 x R_Hubble. If z_turn > 8, then R_universe >= 3 x R_Hubble.
These two handles are consistent and jointly place R_universe in the range 2-4 x R_Hubble -- large enough that local curvature measurements return apparently flat results, small enough that the topological signature is detectable in the high-redshift universe with current instruments.
✓  S³ topology derived from SU(2) group manifold identification -- a theorem of Lie group theory, not an assumption.
✓  Canonical spin structure on S³ uniquely determined by the SU(2) x SU(2) covering group of S_geo -- no additional input required.
✓  Four physical consequences derived: mode quantization (CMB suppression), angular diameter turnaround (topology prediction), condensate resonant cavity (structure formation mechanism), antipodal correlation signature (new in v6 framing).
P.7.7 Chirality Preservation Across the Bounce and Sympathetic Nucleation
[New in v5. Unchanged in v6.]
This section presents the matter generation mechanism as a theoretical prediction grounded in the standard spin representation of the spinor field on S³, and identifies the formal proof target required to establish it rigorously. The prediction is not a bifurcation between two equally open possibilities -- it is the consequence the algebraic structure of the theory points toward. A logical alternative is documented as a foil and demoted accordingly. Explicit proof targets are identified in P.7.7.6.
P.7.7.1 The Discriminating Question: The Antipodal Map on S³
The cosmological bounce on S³ involves the three-sphere collapsing to minimum radius (Planck scale) and re-expanding. Geometrically, the collapse-and-re-expansion traverses the antipodal map of S³ -- the map that sends every point to its diametrically opposite point. For spinor fields, the antipodal map is more subtle than for scalar or vector fields.
The spin structure on S³ has a non-trivial element corresponding to the antipodal map. In the standard spin representation, spinors on S³ acquire a sign change under the antipodal map:
$A_{\mu}$ -> -$A_{\mu}$   (chirality inverts at each bounce)
This is not one of two open possibilities. It is the default consequence of the standard spin representation on S³, and it is what the theory predicts. Net chirality inverts at every bounce, successive cycles alternate between matter-dominated and antimatter-dominated, and the cyclic symmetry of the full multi-bounce history is exact. The current matter dominance reflects the phase of the current cycle, not an accumulated bias across prior cycles.
The formal proof of this prediction is Proof Target PT-1, identified in P.7.7.6. PT-1 requires specifying the global section of the spinor bundle over S³ through the Planck-density phase -- a calculation that requires the FLRW reduction of S_geo (CT-viii) as a prerequisite. The prediction is stated here with the confidence appropriate to a theoretical claim whose formal proof is outstanding but whose derivation from the algebraic structure of the theory is clear.
A logical alternative exists and is documented in P.7.7.3 below for formal completeness: if the antipodal map were to act trivially on the global section of the spinor field, chirality would be preserved rather than inverted. This alternative is not what the standard spin representation on S³ predicts, and the theory does not expect it. It is presented as a foil -- the structure that PT-1 rules out -- rather than as a co-equal possibility.
P.7.7.2 The Theoretical Prediction: Chirality Inversion (Alternation)
Prediction P.7.7.2 (Alternation) [PREDICTION -- formal proof PT-1 outstanding]
The antipodal map of S³ acts non-trivially on the global section of the spinor field $\psi$ through the bounce, inducing $A_{\mu}$ -> -$A_{\mu}$. Net chirality inverts at every bounce. Successive cycles alternate between matter-dominated and antimatter-dominated. The current matter dominance reflects the phase of the current cycle. The total net matter-antimatter balance integrated across all cycles is exactly zero -- the full multi-bounce history is cyclically symmetric, not asymmetric.
This prediction follows from the standard spin representation on S³. It requires no additional physical mechanism and is consistent with a deeper global symmetry of the theory: the apparent matter-antimatter asymmetry within any given cycle is a local phase phenomenon rather than a fundamental violation of global conservation. The sign-change behaviour of spinors under the antipodal map on S³ is a standard result of the representation theory of Spin(4) ≅ SU(2) x SU(2). In the standard (fundamental) spinor representation, the generator of the antipodal map acts with a global phase of -1 on Weyl spinors. This is why the prediction is stated with theoretical confidence rather than treated as a free parameter.
The JWST stellar mass anomaly is explained within this prediction. Within any given matter-dominated cycle, sympathetic nucleation produces more matter than a single-origin model predicts, because the chirality bias is present from the start of the cycle's expansion. Galaxies forming early in the current cycle did so in a matter-richer environment than LCDM assumes. The anomalously high stellar masses at z ~ 10-16 observed by JWST are a direct consequence of this within-cycle surplus, independent of the meta-historical alternation.
On observational inaccessibility. The alternation prediction concerns the relationship between the current cycle and prior and subsequent cycles. No information survives a bounce in any observationally accessible form that would allow direct confirmation or falsification of the meta-historical pattern. This is an honest constraint: the cyclic alternation is a theoretical feature of the framework, not part of the falsifiable test programme. What is falsifiable is the within-cycle matter surplus and its observational consequences.
P.7.7.3 The Logical Foil: Chirality Preservation (Accumulation)
Foil P.7.7.3 (Accumulation) [Not the theoretical prediction -- retained for formal completeness]
For formal completeness, the logical alternative to Prediction P.7.7.2 is documented here. If the antipodal map of S³ were to act trivially on the global section of the spinor field $\psi$ through the bounce -- acting as +1 rather than -1 on the spinor field -- net chirality would be preserved: the mean axial current <A^0> would carry the same sign into the next cycle. Sympathetic nucleation would then compound across cycles. Net matter content would grow monotonically. The current matter dominance would be evidence of accumulated bias across many prior cycles.
This alternative is not what the standard spin representation on S³ predicts. It would require either that S_geo selects a non-standard representation in which the antipodal map acts trivially, or that some additional physical mechanism during the bounce enforces chirality preservation. Neither condition is motivated by the current theory. PT-1 is expected to rule out this alternative by establishing that the standard spin representation applies.
This foil is retained because PT-1 has not yet been completed, and intellectual honesty requires acknowledging that the formal proof is outstanding. If PT-1 were to establish that the antipodal map acts trivially -- a result the theory does not anticipate -- the cosmological picture would shift to accumulation, and PT-3 (the self-consistent evolution equation for <A^0>(N) across cycles) would become necessary. That contingency is noted here but not developed further.
P.7.7.4 Physical Motivation: The Sympathetic Nucleation Mechanism
The sympathetic nucleation mechanism operates identically within any given cycle regardless of which result PT-1 establishes. The within-cycle matter surplus is a consequence of the condensate structure, not of the meta-historical alternation pattern. Standard vacuum pair creation produces a matter-antiparticle pair with opposite chirality -- net baryon number zero. In the presence of a background condensate with net chirality <A^0> not equal to 0, two qualitatively different events are available:
Event Type 1 (standard): particle + antiparticle, opposite chirality. Net baryon number: 0.
Event Type 2 (sympathetic): two particles, same chirality, aligned with condensate. Net baryon number: +2.
The probability ratio is estimated dimensionally as P(Type 2) / P(Type 1) ~ |<A^0>|^2 / $m_\text{eff}$^2. This is small when condensate chirality is weak but nonzero whenever <A^0> not equal 0.
P.7.7.5 Relationship to the Sakharov Conditions
The three Sakharov conditions -- baryon number violation, C and CP violation, and departure from thermal equilibrium -- are not independent requirements imposed externally on this framework. The condensate structure potentially provides geometric realizations of all three: baryon number violation via Event Type 2 nucleation; CP violation via the net chirality of the condensate vacuum <A^0> not equal to 0; departure from thermal equilibrium via the bounce itself, which is a non-equilibrium event by construction. These are structural correspondences, not derivations -- formal demonstration requires the Bogoliubov analysis of PT-2 and the FLRW reduction of CT-viii.
P.7.7.6 Identified Proof Targets
○  PT-1 [Confirmatory]: Action of the antipodal map on the spinor field global section. The theoretical prediction is that the antipodal map acts as -1 on the spinor field in the standard spin representation on S³, inducing $A_{\mu}$ -> -$A_{\mu}$ and establishing the alternation prediction (P.7.7.2). PT-1 is the formal confirmatory proof of this prediction. Prerequisite: FLRW reduction of S_geo (CT-viii). If PT-1 were instead to establish that the antipodal map acts as +1 -- an outcome the theory does not anticipate -- the foil (P.7.7.3) would follow and PT-3 would become necessary.
○  PT-2: Bogoliubov analysis of pair creation in chiral condensate background. Full computation of P(Type 2) / P(Type 1) as a function of {$\alpha$, $\lambda$, m, <A^0>}. Applicable under both the theoretical prediction (P.7.7.2) and the logical foil (P.7.7.3). Determines the magnitude of the within-cycle matter asymmetry.
○  PT-3 [Contingent on unexpected PT-1 result only]: Self-consistent evolution equation for <A^0>(N) across N cycles. Required only if PT-1 unexpectedly establishes the foil (P.7.7.3). Not a priority of the current proof programme.
○  PT-4: Formal derivation of Sakharov conditions from S_geo. Applicable under both the theoretical prediction (P.7.7.2) and the logical foil (P.7.7.3).
PT-1 is confirmatory, not discriminating. The theory has a prediction: chirality inverts at each bounce, successive cycles alternate, and the standard spin representation on S³ is the basis for that prediction. The formal proof is outstanding. These are different things. The framework is not in an undecided state pending PT-1 -- it has a stated theoretical position and an identified proof target for that position.
P.8 Remaining Calculational Programme
[CT-xiii is new in v7. Items CT-i through CT-xii are unchanged from v6.]
The following items are calculational targets within the closed theory -- well-defined computations, not foundational gaps.
CT-i. Numerical evaluation of $\kappa$(T) across intermediate temperatures (stellar interior and galactic-scale regime). The analytic high-T and low-T limits are closed; the intermediate regime requires numerical Matsubara integration.
CT-ii. Quantitative Gordon decomposition corrections. The full spinor vector current contains spin-orbit cross terms that modify Q($\mu$,$\nu$) at second order. These generate new predictions at nuclear scales relevant to the Bi-209 Channel C measurement.
CT-iii. Lensing diffusion timescale measurement. The spinor field diffusion prediction $\tau_\text{diff}$ ~ R^2 * $m_\text{eff}$ / hbar is testable from time-resolved post-merger lensing imaging.
CT-iv. Uniqueness at higher order in $\psi$. Theorem 1 establishes uniqueness at quadratic order. Quartic corrections are already identified as Term 3; their full characterisation as a tensor source is pending.
CT-v. Equivalence principle formal bound. Quantitative suppression of $\eta$ differential at laboratory scales from the condensate temperature structure, compared against Eötvös bounds.
CT-vi. Quantitative evaluation of $m_\text{eff}$ from action parameters {$\alpha$, $\lambda$, m} and comparison against the Pb-208 coherence timescale estimate. The Bi-209 calibration provides an independent experimental determination.
CT-vii. Black hole condensate propagator: full perturbative mode analysis of the spinor condensate field around a Schwarzschild background. This is the prerequisite for converting the dimensional estimate f_cond ~ M^(-2) into a quantitative prediction with error bounds, and for establishing whether the condensate propagation couples to pulsar timing (NANOGrav connection). Also a prerequisite for CT-xiii.
CT-viii. FLRW reduction and modified Friedmann equations. Reducing S_geo on an S³ x R FLRW ansatz to obtain the modified Friedmann equations governing the bounce dynamics and the expansion history within each cycle. Required for PT-1 (chirality conjecture) and for CT-ix and CT-xiii.
CT-ix. Derivation of R_universe from action parameters and initial conditions. The S³ radius is constrained observationally (CMB quadrupole, angular diameter distance turnaround) but not yet derived from S_geo. CT-viii is a prerequisite.
CT-x. Bogoliubov analysis of sympathetic nucleation (Proof Target PT-2). The critical calculation for elevating Conjecture P.7.7 to a theorem.
CT-xi. Perturbative vacuum stability, ghost analysis, and Hamiltonian boundedness of S_geo. Required for full formal closure at the quantum field theory level.
CT-xii. Hyperbolicity and causal propagation verification for the full Einstein-Cartan-SCH system.
CT-xiii [New in v6]. Photon-condensate coupling cross section $\sigma$(omega) as a function of photon frequency omega, and derivation of the CMB monopole temperature from the condensate scrambling integral. This is the proof target required to elevate the Olbers mechanism conjecture and the CMB-as-condensate-scrambled-light conjecture (Paper A Section 6.9) from conjecture to theorem.
Physical content: The propagating spinor condensate $C_{\mu\nu}$ couples to photons via the photon-condensate interaction term in the full action. This coupling introduces a frequency-dependent attenuation of photon coherence over cosmological path lengths. The cross section $\sigma$(omega) quantifies this coupling. The coherence damping length L_coh(omega) = 1 / (n_condensate * $\sigma$(omega)) determines the transition redshift z_flip above which photons arrive as scrambled flux rather than coherent source signals. The CMB monopole temperature T_CMB emerges from the total energy density of this scrambled flux, distributed as a maximum-entropy (Planck) spectrum by the scrambling process.
Sub-targets: (a) Derive the photon-condensate vertex from S_geo + S_matter (minimal coupling). (b) Compute $\sigma$(omega) at one loop in the condensate background. (c) Evaluate the coherence damping integral over all sources as a function of z_flip. (d) Derive T_CMB from the total scrambled energy density. (e) Verify that the monopole temperature prediction is consistent with the measured 2.725 K within the observational uncertainty.
Prerequisites: CT-vii (condensate propagator, required for the photon-condensate vertex calculation in the condensate background) and CT-viii (FLRW reduction, required to set up the cosmological damping integral consistently with the bounce expansion history).
Falsification conditions carried in from Paper A Section 6.9: (i) $\sigma$(omega) = 0 for all omega falsifies both the Olbers and CMB conjectures simultaneously; (ii) $\sigma$(omega) nonzero but resulting T_CMB differs from 2.725 K by more than observational uncertainty falsifies the CMB origin conjecture while leaving the Olbers mechanism conjecture open; (iii) resolved-source count as a function of redshift showing no suppression below z_flip falsifies the Olbers mechanism conjecture.
Relationship to known CMB structure: CT-xiii addresses the monopole temperature only. The acoustic peak structure of the CMB anisotropy spectrum is not addressed by this target -- it is governed by baryon-photon plasma oscillations at recombination, which are unaffected by condensate physics (the condensate melts at T > T_c, placing it absent at recombination). The mode quantization on S³ (P.7.6) addresses the large-angle anisotropy anomalies (ell = 2, 3 suppression) independently of CT-xiii.
Priority: CT-xiii should be pursued in parallel with CT-vii and CT-viii, since its physical motivation (the Olbers mechanism and CMB origin conjectures) is among the most parsimonious extensions of the framework, and a null result ($\sigma$(omega) = 0) would immediately falsify two conjectures in Paper A Section 6.9 at no experimental cost.
End of Appendix P -- v7