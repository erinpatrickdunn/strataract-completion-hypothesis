**Appendix P — v13 | June 2026**

Revised from v12: Section P.7.7.3 (the PT-1 monodromy calculation) is
redone from scratch following discovery that v12's derivation mixed
metric-signature conventions. IVN-I ("PT-1 Monodromy in the
$(+,-,-,-)$ Convention", June 2026) reworks the calculation
consistently in $(+,-,-,-)$ and finds: (1) the bilinear evolution
equations are real, with no spurious $i$ factors, once the convention
is fixed throughout; (2) the qualitative PT-1 conclusion of v12 is
**unchanged** — chirality inversion per cycle is not a generic
consequence of the dynamics, and $M = -\mathbf{1}$ requires a
non-topologically-protected fine-tuning of the action parameters;
(3) a **new physical effect** not visible in the v12 (mixed-convention)
calculation: in Branch 2 ($A^0 \neq 0$), the scalar condensate $\eta$
is sourced by the product $\kappa\alpha A^0 P$ and does **not** dilute
purely as $a^{-3}$, contrary to what P.10 (CT-ix) assumed for its
Branch 2 late-time-attractor claim. This is flagged as requiring
revision. Section P.7.7.3 is rewritten below; a new Section P.7.7.3a
documents the Branch 2 sourcing effect; Section P.7.7.9 (proof target
structure) is updated; the STATUS SUMMARY table Gap 7 entry and the
CT-ix closure entry (Section P.10) are both updated with the new
status and an explicit caveat. Seven new IVN items (IVN-I-1 through
IVN-I-7) are opened; IVN-I-3 (verifying the $\eta$-sourcing term) is
CRITICAL and gates any downstream use of the Branch 2 dynamics. All
other content is carried forward unchanged from v12. Version bumped
to v13.

---

**STATUS SUMMARY**

| **Gap** | **Status** | **Resolution / Reference** |
| --- | --- | --- |
| Gap 1 — Leading-order uniqueness of $Q_{\mu\nu}$ | **ESTABLISHED** | Fierz completeness, local EFT limit, explicit density hierarchy bound |
| Gap 2 — Four-velocity normalization | **ESTABLISHED** | Fierz + parity-preserving sector, regime-conditional |
| Gap 3 — Gamma_decoh, Gamma_recoh | **DERIVED** | Matsubara + EFT kinetics, no additional free parameters |
| Gap 4 — Torsion persistence | **RESOLVED** | Algebraic/field distinction |
| Gap 5 — Black hole bounce resonance | **ESTABLISHED** | Term 3 at Planck density, condensate propagation from Theorem 4 |
| Gap 6 — S³ spatial topology | **ESTABLISHED** | SU(2) group manifold identification, canonical spin structure |
| Gap 7 — Chirality inversion across bounce and sympathetic nucleation | **OPEN QUESTION — CONVENTION-CORRECTED, CONCLUSION UNCHANGED** | The PT-1 analysis programme (v1, June 2026) established the holonomy picture in a mixed-convention calculation. IVN-I (June 2026) redid the calculation consistently in $(+,-,-,-)$ and found: the bilinear ODE system is real (no spurious $i$ factors); the qualitative conclusion of v12 — that chirality inversion per cycle is not generic and requires a non-topologically-protected fine-tuning $\Phi_{\text{cycle}} = (2n-1)\pi$ — is **confirmed**, not overturned. However, the corrected monodromy matrix (M-correct) has a different structure than v12's (M), since $\Omega_1 \neq \Omega_2$ in the corrected system. A **new physical effect** was found in the correction: in Branch 2, $\eta$ is sourced by $\kappa\alpha A^0 P$ and does not dilute as pure $a^{-3}$. This affects the CT-ix Branch 2 late-time-attractor claim (Section P.10) — see caveat there. IVN-I-3 (verifying the $\eta$-sourcing term) is CRITICAL and outstanding. See P.7.7.3, P.7.7.3a, and IVN-I working documents (June 2026). |
| Gap 8 — Photon-condensate coupling and CMB monopole | **OPEN TARGET** | CT-xiii identified. Prerequisites: CT-vii + CT-viii. |
| Gap 9 — Physical primitive: ψ as derived object, not ansatz | **ESTABLISHED** | P.0b: ψ is the unique minimal 4D rotational encoder; S_geo follows as consequence. Theorem 0. [New in v8] |
| Gap 10 — W-spin as mass: η as physical rotational departure | **ESTABLISHED** | Theorem 0: η = ψ̄ψ is the w-spin magnitude of the 4D knot; bridges physical picture and formalism. [New in v8] |
| Gap 11 — c as tangential S³ velocity: speed of light derived | **ESTABLISHED** | Theorem 5: c(t) = ω(t) · R_cosmic(t). Photon as minimum-w-spin surface wave. Constancy of c derived from S³ geometry. Lensing confirms photon w-spin is nonzero. [New in v8] |
| Gap 12 — Matter-light phase transition: topological distinctness | **ESTABLISHED** | Theorem 6: η = 0 and η ≠ 0 are distinct phases separated by a topological boundary, not points on a speed continuum. [New in v8] |
| Gap 15 — FLRW reduction of $S_{\text{geo}}$: modified Friedmann equations and bounce condition | **CLOSED** | CT-viii: modified Friedmann equations derived, two-branch cosmology established, bounce existence condition proven, GR recovery confirmed, kinetic coefficient $-3/2$ derived explicitly. Section P.9. [New in v10] |
| Gap 13 — Antipodal condensate coupling: mechanism linking local BH emission to global $S^3$ modes | **OPEN TARGET** | CT-xix identified. Prerequisites: CT-vii + CT-viii. CT-viii now closed. Physical motivation in *SCH_GalacticEngine_PhysicalPicture_v1* Section 2. [New in v9] |
| Gap 14 — Thermodynamic consistency of coherence-forcing: entropy accounting for galactic engine | **OPEN TARGET** | CT-xx identified. Prerequisites: CT-xix + Bi-209 calibration. Physical motivation in *SCH_GalacticEngine_PhysicalPicture_v1* Section 7. [New in v9] |
| Gap 16 — Cosmological dynamics: solution structure of the modified Friedmann system | **CLOSED (Branch 2 detail under revision)** | CT-ix (June 2026): Branch 1 fully characterised — two-phase dynamics (stiff-condensate $a \propto t^{1/3}$, then dust-condensate); analytic solutions in each phase; explicit $a_{\text{max}} = \kappa m\eta_0/3$ and $R_{\text{universe}}$ as function of $m\eta_0$; CMB quadrupole constraint translates to $m\eta_0 \geq 9c^4/(8\pi G)$. **Branch 2's claimed asymptote to Branch 1 at late times assumed $\eta \propto a^{-3}$ in Branch 2, which IVN-I (v13) shows is incomplete — see caveat in Section P.10.** Eight IVN items and five open questions identified in the original CT-ix document; independent verification required before downstream use. See SCH_CT_ix_CosmologicalDynamics_v1.md and IVN-I working documents. |

The framework has a closed variational structure within its stated
EFT and mean-field condensate regime. All claims are regime-conditional.
The density hierarchy is explicit and bounded.

Three developments change the epistemic landscape of the
cosmological sector across v12 and v13:

**CT-ix (closed, v12):** The cosmological dynamics are now derived from the
modified Friedmann equations of CT-viii. The Phase I and Phase III
solution structures are established, $R_{\text{universe}}$ is derived
as a function of the action parameters, and the CMB quadrupole
suppression constraint is expressed as a bound on $m\eta_0$. Eight
IVN items require independent verification.

**PT-1 (revised, v12):** The chirality inversion claim is not established
as a universal consequence of the dynamics. The correct formulation
is that the chirality transformation per cycle is the holonomy of a
natural $\mathrm{U}(1)$ connection on the condensate axial-current
line bundle, with value $e^{i\alpha_+}$ determined by the action
parameters. No topological mechanism quantizes this phase.

**IVN-I (convention correction, v13):** The v12 monodromy calculation
mixed metric-signature conventions. Redone consistently in
$(+,-,-,-)$, the bilinear system is real rather than complex, and the
monodromy matrix has a different structure ($\Omega_1 \neq \Omega_2$,
no simple $\cos/i\sin$ form). The qualitative PT-1 conclusion is
unaffected: chirality inversion is still non-generic. But the
correction surfaces a previously invisible effect — a Branch 2
source term for $\eta$ — that requires revising the CT-ix Branch 2
discussion. This revision is confined to the monodromy/chirality
sector and the Branch 2 late-time behaviour; it does not alter Branch
1, the FLRW reduction of CT-viii, or any galactic-scale prediction.

The galactic-scale variational closure established in v8 and the
FLRW reduction of v10–v11 are unaffected by these revisions.

---

# **P.0 Preamble: From Consistency to Proof — and the Role of Regime Conditioning**

*[Unchanged from v7]*

Paper A (Draft 1.5) presents the Strataract Completion Hypothesis (SCH) as a modified gravitational field equation:

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

**TOPOLOGY** (new in v5): $\mathrm{SU}(2)$ as group manifold $= S^3$ $\Rightarrow$ spatial topology uniquely compatible with $S^3$ (P.7.6)

**GROUND FLOOR** (new in v8): $\psi$ derived as minimal rotational encoder in 4D; $\eta$ identified as w-spin magnitude; $c$ derived as tangential S³ velocity; photon identified as minimum-w-spin surface wave (lensing confirms $\eta_{\text{photon}} > 0$); matter-light distinction derived as phase transition (P.0b, Theorems 0, 5, 6)

*[Sections P.0a, P.0b, Theorem 0, Theorem 5, Theorem 6, P.1 through P.6, P.7.1 through P.7.6 are unchanged from v12 and are not reproduced in full here — see SCH_Appendix_P_v12.md for the complete text. Only P.7.7 (chirality) and P.10 (CT-ix, Branch 2 caveat) are revised below. All cross-references to those unchanged sections remain valid.]*

---

### **P.7.7 Chirality Across the Bounce and Sympathetic Nucleation**

*[Revised in v13 following IVN-I. The v12 text — itself a revision of
the original v5–v11 P.7.7 following the PT-1 analysis programme — is
superseded in Section P.7.7.3 below. The physical motivation for
sympathetic nucleation is preserved throughout. The v12 conclusion
("chirality inversion is not generic") is confirmed by the corrected
calculation, but the calculation supporting it is replaced, and a
new physical effect is surfaced.]*

#### **P.7.7.1 The Question**

*[Unchanged from v12.]*

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

#### **P.7.7.2 The Original Claim and Why It Fails**

*[Unchanged from v12.]*

Previous versions of this section (v5–v11) stated that spinors on $S^3$
acquire a sign change under the antipodal map, $A^\mu \to -A^\mu$, as
"the default consequence of the standard spin representation on $S^3$."
This is incorrect for two reasons. First, the spatial antipodal map
sends $\psi \to -\psi$, but $A^\mu$ is bilinear, so
$A^\mu \to (-1)^2 A^\mu = +A^\mu$ — the spatial antipodal map gives the
wrong sign. Second, the bounce is not a spatial antipodal map; it is a
continuous temporal event governed by the cosmological Dirac equation
(CT-viii), and $A^0$ is continuous through it with no local sign flip.

#### **P.7.7.3 The Corrected Monodromy Calculation (IVN-I, $(+,-,-,-)$ Convention)**

*[Rewritten in v13. This section replaces the v12 derivation, which
mixed the $(-,+,+,+)$ convention of the cosmological Dirac equation
(P.9.5.3) with $(+,-,-,-)$ bilinear definitions, producing spurious
$i$ factors and an artificially simple monodromy matrix. IVN-I
("PT-1 Monodromy in the $(+,-,-,-)$ Convention", June 2026) redoes the
calculation with a single convention held fixed throughout:
$\eta_{ab} = \mathrm{diag}(+1,-1,-1,-1)$; $(\gamma^0_D)^2 = +\mathbf{1}$;
$\eta = \bar\psi\psi = \xi^\dagger\xi - \chi^\dagger\chi$;
$A^0 = \bar\psi\gamma^0_D\gamma^5_D\psi = \xi^\dagger\chi + \chi^\dagger\xi$;
$P = \bar\psi\gamma^5_D\psi = -i(\xi^\dagger\chi - \chi^\dagger\xi)$;
$J^0 = \xi^\dagger\xi + \chi^\dagger\chi$. Full step-by-step component
derivation is in the IVN-I working document; the results are stated
here with the key intermediate equations.*

**The component equations.** Rewriting the cosmological Dirac equation
(P.9.5.3) in $(+,-,-,-)$ and projecting onto the upper/lower Dirac
components $(\xi,\chi)$:

$$\dot{\xi} = -i\frac{3H}{2}\xi - im\xi - i\frac{\lambda}{2}\eta\xi
- i\frac{\kappa\alpha}{2}A^0\chi$$

$$\dot{\chi} = -i\frac{3H}{2}\chi + im\chi + i\frac{\lambda}{2}\eta\chi
- i\frac{\kappa\alpha}{2}A^0\xi$$

The sign flip on the mass term between the $\xi$ and $\chi$ equations
(a consequence of $\gamma^0_D$ acting as $+1$ on the upper component and
$-1$ on the lower) is the feature that, once propagated consistently
into the bilinear equations, removes the spurious $i$ factors present
in v12's system.

**The corrected bilinear evolution equations.** Carrying the component
equations through to the bilinears $\eta$, $A^0$, $P$, $J^0$ (full
term-by-term cancellation shown in IVN-I Part 2) gives:

$$\dot{\eta} + 3H\eta = \kappa\alpha A^0 P \tag{E1-new}$$

$$\dot{A}^0 = -(2m + \lambda\eta)\,P \tag{E-A-new}$$

$$\dot{P} = \left(2m + (\lambda - \kappa\alpha)\eta\right) A^0 \tag{E-P-new}$$

$$\dot{J}^0 + 3H J^0 = 0 \quad \text{(tentative — see IVN-I-4, IVN-I-5)} \tag{E-J-new}$$

All four equations are **real**, with no factors of $i$ — a structural
improvement over the v12 system, which carried spurious $i$ factors as
an artifact of the convention mismatch. Two features are new relative
to v12:

(i) **In Branch 1** ($A^0 = 0$), (E1-new) reduces to $\dot\eta + 3H\eta = 0$,
recovering the familiar dilution law $\eta \propto a^{-3}$ exactly as
before. Branch 1 is unaffected by this revision.

(ii) **In Branch 2** ($A^0 \neq 0$), (E1-new) has a nonzero source term
$\kappa\alpha A^0 P$. This is new physics not visible in v12's
(mixed-convention) calculation, where $\eta$ appeared to dilute
independently of the chirality sector in both branches. See P.7.7.3a
below.

**The corrected $(A^0, P)$ system.** Equations (E-A-new) and (E-P-new)
form a real, coupled linear system:

$$\dot{A}^0 = -\Omega_1 P, \qquad \dot{P} = \Omega_2 A^0$$

where $\Omega_1 \equiv 2m + \lambda\eta$ and
$\Omega_2 \equiv 2m + (\lambda-\kappa\alpha)\eta$. This differs
structurally from v12's system, which had $\Omega_1 = \Omega_2 = \Omega$
and complex coefficients with an explicit Hubble-friction term $\Gamma$.
Neither the friction term nor the $\Omega_1 = \Omega_2$ degeneracy
survives the corrected calculation: the corrected system has **no**
Hubble friction in the $(A^0,P)$ sector, and $\Omega_1 \neq \Omega_2$
whenever $\kappa\alpha \neq 0$.

For $\Omega_1\Omega_2 > 0$ (the generic case when $\lambda > \kappa\alpha$,
i.e. weak torsion coupling relative to the quartic self-coupling), the
system is oscillatory with adiabatic phase

$$\Phi_{\text{cycle}} = \int_{\text{cycle}} \sqrt{\Omega_1(t)\,\Omega_2(t)}\;dt$$

replacing v12's $\alpha_+ = \int_{\text{cycle}} \Omega\,dt$. The
corrected monodromy matrix, in the adiabatic approximation, is

$$M_{\text{correct}} = \begin{pmatrix}
\cos\Phi_{\text{cycle}} & -\sqrt{\Omega_1/\Omega_2}\,\sin\Phi_{\text{cycle}} \\
\sqrt{\Omega_2/\Omega_1}\,\sin\Phi_{\text{cycle}} & \cos\Phi_{\text{cycle}}
\end{pmatrix}$$

which is **not** the simple $e^{i\alpha_-}\begin{pmatrix}\cos&i\sin\\i\sin&\cos\end{pmatrix}$
form reported in v12 — that form was an artifact of the
$\Omega_1 = \Omega_2$ degeneracy and the spurious complex structure.
$M_{\text{correct}} = -\mathbf{1}$ still requires
$\Phi_{\text{cycle}} = (2n-1)\pi$ (odd multiple of $\pi$), the same
qualitative condition as v12, now derived from a corrected and
structurally different underlying system.

**The phase estimate.** In Phase III (near $\eta \approx 0$, late-time,
large $a$), $\sqrt{\Omega_1\Omega_2} \to 2m$ and

$$\Phi_{\text{cycle}} \approx 2m\,T_{\text{cycle}} \sim 10^{54}$$

— the same order-of-magnitude estimate reported in v12, using the
preliminary $m \sim m_{\text{eff}} \sim 10^{-6}$ eV and
$T_{\text{cycle}} \sim 10^{60}\,\text{eV}^{-1}$. In Phase I (near the
bounce, $\eta \gg 2m/\lambda$), the correction introduces a finite
$\kappa\alpha$-dependent shift to this estimate:

$$\delta\Phi = -\frac{\kappa\alpha}{2}\int_{\text{cycle}}\eta\,dt$$

which reduces $\Phi_{\text{cycle}}$ relative to the naive
$2m\,T_{\text{cycle}}$ estimate by a finite, calculable amount once
$\alpha$ is fixed by the Bi-209 calibration. This shift does not, in
general, move $\Phi_{\text{cycle}}$ onto the nearest odd multiple of
$\pi$ — landing on $(2n-1)\pi$ remains a set of measure zero in the
space of possible action-parameter values, with no topological
mechanism (spin structure, Aharonov-Bohm, Berry phase, or global
$S^3$ mode coupling — see P.7.7.4, unchanged from v12) forcing it.

**Conclusion of P.7.7.3 (v13):** The v12 conclusion is confirmed under
a corrected, convention-consistent derivation: chirality inversion per
cycle ($M = -\mathbf{1}$) is not a generic consequence of the dynamics.
It requires the action parameters to satisfy a non-topologically-protected
quantization condition. The corrected calculation additionally
identifies a Branch 2 coupling between $\eta$ and the chirality sector
absent from all prior versions of this section — see P.7.7.3a.

#### **P.7.7.3a New Result: Branch 2 $\eta$-Sourcing by the Chiral Sector**

*[New in v13.]*

Equation (E1-new), $\dot\eta + 3H\eta = \kappa\alpha A^0 P$, means that
in Branch 2 the scalar condensate is not simply diluting under
expansion — it is dynamically driven by the product of the axial
current and the pseudoscalar bilinear. Since $A^0$ and $P$ oscillate
(Section P.7.7.3, adiabatic solution) at frequency
$\sim\sqrt{\Omega_1\Omega_2} \approx 2m$, their product oscillates at
roughly double this frequency, and in general
$\langle A^0 P\rangle_{\text{osc}} \neq 0$ once the phase relationship
between the two oscillators is accounted for (generic $90°$ phase
offset for a coupled linear oscillator pair does not guarantee the
time-averaged product vanishes when $\Omega_1 \neq \Omega_2$).

**Physical interpretation.** $A^0$ is the chiral charge density; $P$
is the parity-odd pseudoscalar amplitude. Their product is
parity-even and couples to $\eta$ through the torsion coupling
$\kappa\alpha$. In Branch 2, the condensate is not in the
parity-preserving vacuum; the coexistence of nonzero $A^0$ and $P$ is
itself a parity-broken state, and the torsion coupling allows energy
to flow between the scalar condensate and the parity-odd sector. This
was invisible in the v12 calculation because the (incorrect) mixed
convention gave $\Omega_1 = \Omega_2$ and a decoupled $\eta$ equation.

**Consequence for CT-ix.** The CT-ix document (Section P.10) derives
Branch 2 behaviour assuming $(A^0)^2$ decays as $a^{-3}$ and Branch 2
asymptotes to Branch 1 at late times. That derivation implicitly
assumed $\eta$ dilutes independently of the chirality sector in
Branch 2, which (E1-new) shows is not exact. See the caveat in
Section P.10 below. This does not necessarily overturn the
late-time-attractor conclusion — the correction may be a small
perturbation on top of the dominant $a^{-3}$ dilution — but it has
not been shown to be small, and must be checked (IVN-I-3, CRITICAL)
before the Branch 2 asymptote claim is used downstream.

#### **P.7.7.4 Is the Phase Topologically Quantized?**

*[Unchanged from v12. The systematic investigation of candidate
quantization mechanisms — spin structure on the temporal $S^1$,
Aharonov-Bohm, Berry phase, global $S^3$ mode coupling — found no
mechanism that quantizes the phase. That investigation examined the
structural question of whether *any* phase of this general type can
be topologically pinned; it is independent of the specific value or
functional form of the phase, and its conclusions carry over unchanged
to the corrected phase $\Phi_{\text{cycle}}$ of P.7.7.3. No topological
mechanism quantizes $\Phi_{\text{cycle}}$, exactly as none quantized
v12's $\alpha_+$.]*

#### **P.7.7.5 The Physical Situation**

*[Unchanged from v12 in substance; $\alpha_+$ should be read as
$\Phi_{\text{cycle}}$ throughout.]* With the preliminary estimate
$m \sim m_{\text{eff}} \sim 10^{-6}$ eV and
$T_{\text{eff}} \sim t_{\text{max}} \sim (\pi/2)R_{\text{universe}}
\sim 10^{60}$ eV$^{-1}$:

$$\Phi_{\text{cycle}} \approx 2m \cdot T_{\text{eff}} \sim 10^{54}$$

The phase is astronomically large and exquisitely sensitive to $m$ and
$R_{\text{universe}}$; it cannot be determined without the Bi-209
calibration. As in v12, the matter-creation epoch duration relative to
the rotation period $\pi/(2m)$ (OQ-CT-ix-5) determines whether $A^0$
has an approximately definite sign during nucleation regardless of the
full-cycle monodromy — this sub-calculation is unaffected in structure
by the IVN-I correction, though it should now be redone using
$\Phi_{\text{cycle}}$ and the corrected $(A^0,P)$ system rather than
v12's system.

#### **P.7.7.6 The Sympathetic Nucleation Mechanism: Preserved**

*[Unchanged from v12.]* The physical mechanism for within-cycle matter
surplus is unaffected by the convention correction: standard vacuum
pair creation gives net baryon number 0; in the presence of a
condensate with $\langle A^0\rangle \neq 0$, two same-chirality
particles are produced with net baryon number $+2$, at probability
ratio $\sim |\langle A^0\rangle|^2/m_{\text{eff}}^2$. What is preserved
is the mechanism and the existence of a chirality bias; what is
revised (as in v12, now on firmer convention-consistent footing) is
that this bias does not necessarily invert sign at each bounce, and
its value is set by the accumulated (corrected) holonomy from all
previous cycles.

#### **P.7.7.7 Relationship to the JWST Anomaly**

*[Unchanged from v12.]* The interpretive link to the JWST early
massive galaxy anomaly is unaffected: sympathetic nucleation being
active (nonzero $\langle A^0\rangle$ at the matter-creation epoch) is
required for any matter to exist at all, and the magnitude of the
within-cycle surplus depends on $|\langle A^0\rangle|/m_{\text{eff}}$,
computable after Bi-209 calibration.

#### **P.7.7.8 Relationship to the Sakharov Conditions**

*[Unchanged from v12.]* The condensate structure continues to provide
structural correspondences to all three Sakharov conditions
(baryon number violation via Type 2 nucleation; CP violation via
$\langle A^0 \rangle \neq 0$; departure from equilibrium via the
first-order bounce transition of Theorem 6). Quantitative
demonstration still requires PT-2 and the Bi-209 calibration.

#### **P.7.7.9 Revised Proof Target Structure**

*[Updated in v13.]*

**PT-1** [Status: numerical calculation, convention now fixed]:

Compute the corrected monodromy phase $\Phi_{\text{cycle}}$ and
matrix $M_{\text{correct}}$ numerically for the physical action
parameters fixed by the Bi-209 calibration, using the
$(+,-,-,-)$-consistent system of P.7.7.3. Determine whether the
matter-creation epoch duration $\delta t_c$ satisfies $\delta\Phi \ll
\pi$ (P.7.7.5). Report $\langle A^0\rangle$ at the start of the
current cycle's matter-creation epoch. **Additionally required in
v13:** confirm the Branch 2 $\eta$-sourcing correction (IVN-I-3) is
either negligible or must be folded into the phase integral
self-consistently, since $\eta(t)$ no longer decouples from
$(A^0, P)$ exactly in Branch 2.

*Prerequisite:* Bi-209 calibration; IVN-I-1 through IVN-I-7
(convention/derivation verification, see below).
*Expected result:* A specific numerical value for the holonomy phase
and a quantitative prediction for the within-cycle matter surplus.
*Nature of result:* Numerical, not topological.

**PT-2, PT-3, PT-4** [Unchanged from v12 in content; PT-3's
prerequisite is now the corrected P.7.7.3 monodromy matrix rather
than v12's.]

**New verification items opened by IVN-I:**

| IVN item | Content | Priority |
|---|---|---|
| IVN-I-1 | Verify the Dirac-conjugate equation (D'') in $(+,-,-,-)$ | HIGH |
| IVN-I-2 | Verify the component equations for $\dot\xi$, $\dot\chi$ | HIGH |
| IVN-I-3 | Verify $\dot\eta + 3H\eta = \kappa\alpha A^0 P$ term by term | **CRITICAL** |
| IVN-I-4 | Check the $A^0$ contribution to $\dot J^0$ | HIGH |
| IVN-I-5 | Resolve an apparent imaginary term surfacing in the $\dot J^0$ derivation (a real bilinear cannot have an imaginary source; this signals an unresolved algebra error requiring recheck, not a physical result) | HIGH |
| IVN-I-6 | Verify the eigenvectors of the $(A^0,P)$ system matrix | MEDIUM |
| IVN-I-7 | Derive $M_{\text{correct}}$ rigorously from the mode solutions (the adiabatic form given in P.7.7.3 is not yet independently re-derived end-to-end) | HIGH |

None of PT-1 through PT-4's conclusions should be treated as
independently confirmed until IVN-I-3 and IVN-I-5 in particular are
resolved. IVN-I-3 gates the Branch 2 CT-ix revision (P.10); IVN-I-5
gates confidence in the full bilinear algebra generally, since an
unresolved imaginary term in a real-valued equation indicates the
derivation is not yet fully trusted even where the headline results
(E-A-new, E-P-new) look structurally clean.

---

# **P.8 Remaining Calculational Programme**

*[Unchanged from v12 — CT-i through CT-xx as previously specified.
See SCH_Appendix_P_v12.md for full text. CT-x (Bogoliubov analysis of
sympathetic nucleation) should be understood as now depending on the
v13-corrected P.7.7.3/P.7.7.3a results rather than v12's.]*

---

# **P.9 CT-viii: FLRW Reduction and Modified Friedmann Equations**

*[Unchanged from v12/v11. See SCH_Appendix_P_v12.md for full text.
Not affected by the IVN-I correction — P.9 establishes the
cosmological Dirac equation and the two-branch structure that P.7.7.3
and P.10 build on; the correction is confined to how the bilinears
derived from that equation are evolved in a self-consistent metric
convention, not to the FLRW reduction itself.]*

---

## P.10 CT-ix: Cosmological Dynamics from the Modified Friedmann System

*[Carried from v12, with a new caveat added in v13 — see boxed note
below. Full derivation in SCH_CT_ix_CosmologicalDynamics_v1.md.
Verification status: internally derived; eight IVN items require
independent verification before downstream use; a ninth consideration
(the IVN-I Branch 2 caveat) is now added.]*

CT-ix delivers the solution structure of the modified Friedmann system
established by CT-viii. Principal results:

**Branch 1 (torsion-free, $A^0 = 0$):**

The condensate scalar satisfies $\dot{\eta} + 3H\eta = 0$, giving
$\eta(t) = \eta_0/a(t)^3$. Substituting into the modified Friedmann
equation:

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\left(\frac{m\eta_0}{a^3}
+ \frac{\lambda\eta_0^2}{4a^6}\right)$$

Two phases:

*Phase I (stiff-condensate, $a \ll a_*$):*
$a(t) \propto |t - t_{\text{b}}|^{1/3}$. Stiff-fluid equation of state.
Predicted gravitational wave spectral tilt: $n_T = -1$ (blue-tilted,
distinct from inflationary models).

*Phase III (dust-condensate, $a \gg a_*$):*
Standard closed-universe parametric solution. Maximum expansion radius:
$a_{\text{max}} = \kappa m\eta_0/3$, giving:

$$R_{\text{universe}} = \frac{\kappa m\eta_0}{3}\,R_{\text{unit}}$$

CMB quadrupole suppression constraint ($R_{\text{universe}} \geq
3R_{\text{Hubble}}$) translates to:

$$m\eta_0 \geq \frac{9c^4}{8\pi G}$$

Branch 1 is unaffected by the IVN-I correction: (E1-new) reduces
exactly to $\dot\eta + 3H\eta = 0$ when $A^0 = 0$, matching what CT-ix
already assumed. All Branch 1 results above stand without
qualification.

**Branch 2 (torsion-active, $A^0 \neq 0$):**

> **⚠️ CAVEAT ADDED IN v13.** The paragraph below was written under
> the (v12, mixed-convention) assumption that $\eta$ dilutes
> independently as $a^{-3}$ in Branch 2, exactly as in Branch 1. IVN-I
> shows this is not exact: the corrected bilinear system has
> $\dot\eta + 3H\eta = \kappa\alpha A^0 P \neq 0$ in Branch 2
> (Section P.7.7.3a). The $(A^0)^2$-decays-as-$a^{-3}$ and
> asymptotes-to-Branch-1 conclusions below should therefore be treated
> as **provisional** pending IVN-I-3 (CRITICAL, outstanding). If the
> $\kappa\alpha A^0 P$ source term turns out to be non-negligible over
> the timescale on which Branch 2 is dynamically relevant, the
> late-time attractor behaviour, the effective $\eta(t)$ profile, and
> potentially $R_{\text{universe}}$ in Branch 2 initial conditions
> would all need to be recomputed self-consistently as a coupled
> $(\eta, A^0, P)$ system rather than treating $\eta$'s decay as given
> and $(A^0, P)$ as evolving on top of it. This is now the
> highest-priority open item for the cosmological sector.

The $(A^0, P)$ bilinears satisfy coupled oscillator equations with
time-varying frequency $\Omega_{\text{mix}} = 2m + \lambda\eta_0/a^3$.
At late times, $(A^0)^2$ decays as $a^{-3}$ and Branch 2 asymptotes
to Branch 1. The bounce condition is satisfied generically.

*[End of carried-forward v12 text; see caveat above. The
$\Omega_{\text{mix}}$ notation above should be read as superseded by
the P.7.7.3 pair $(\Omega_1, \Omega_2)$ — CT-ix used a single
$\Omega$ for both bilinears, which is the same simplification IVN-I
found to be inexact once $\kappa\alpha \neq 0$.]*

**Open questions generated by CT-ix:**

OQ-CT-ix-1: Explicit $c(t)$ derivation from the Phase III solution.
OQ-CT-ix-2: Overlap between Phase I power suppression and CMB quadrupole.
OQ-CT-ix-3: $\eta$ evolution correction at finite $A^0$ in Branch 2.
**(v13 note: this open question is exactly what IVN-I Section
P.7.7.3a now surfaces explicitly. OQ-CT-ix-3 and IVN-I-3 should be
treated as the same outstanding calculation and resolved together.)**
OQ-CT-ix-4: Transition scale $a_*$ vs. observed matter-radiation equality.
OQ-CT-ix-5: Duration of matter-creation epoch relative to rotation
period $\pi/(2m)$ — the key input for the revised PT-1 calculation,
now to be computed using the corrected $\Phi_{\text{cycle}}$ and
$(\Omega_1,\Omega_2)$ system of P.7.7.3.

**IVN items:** Eight independent-verification items are identified in
the CT-ix document, plus the seven new IVN-I items listed in P.7.7.9
above (IVN-I-3 is the most urgent, since it directly determines
whether the Branch 2 caveat above is a large or negligible effect).
IVN-2 ($\eta$ dilution derivation) and IVN-5 (confirmation of E1 by
explicit calculation) are highest priority among the original eight;
**IVN-2 in particular should be revisited in light of IVN-I-3**, since
both concern the same equation (the $\eta$ dilution law) under the
same branch. Results should not be used downstream until these are
verified.

---
**End of Appendix P — v13**

*June 2026 | Not for citation without author approval*

*Summary of v13 changes: (1) Section P.7.7.3 rewritten — the PT-1
monodromy calculation is redone consistently in the $(+,-,-,-)$
convention (IVN-I), yielding a real bilinear ODE system in place of
v12's spurious-$i$ system. (2) The qualitative PT-1 conclusion is
confirmed unchanged: chirality inversion is not generic. (3) New
Section P.7.7.3a documents a previously invisible Branch 2 effect —
$\eta$ is sourced by $\kappa\alpha A^0 P$ and does not dilute purely
as $a^{-3}$ in Branch 2. (4) Section P.10 (CT-ix) Branch 2 discussion
is flagged with an explicit caveat; the late-time attractor claim is
now provisional pending IVN-I-3 (CRITICAL). (5) Seven new IVN-I
verification items opened; OQ-CT-ix-3 and IVN-I-3 identified as the
same outstanding calculation. (6) STATUS SUMMARY table updated for
Gap 7 and Gap 16. No other section is altered; Branch 1, the FLRW
reduction (P.9/CT-viii), and all galactic-scale results are
unaffected.*
