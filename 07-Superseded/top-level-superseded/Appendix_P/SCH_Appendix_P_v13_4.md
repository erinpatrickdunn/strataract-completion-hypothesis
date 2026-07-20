**Appendix P — v13.4 | June 2026**

Revised from v13.3: IVN-CT8-Dirac-1b-i investigated
(`SCH_IVN-CT8-Dirac-1b-i_InvestigationLog_v1.md`, June 2026). **Status
language corrected: 1b is NOT "nearly there."** The current state is
**internally inconsistent** — the derivation as it stands produces an
imaginary residual in $\dot P$ that cannot be correct, confirmed via
three independent computational checks (an independent Hermiticity
classification of the raw integral, a from-scratch direct computation of
$\dot P$ bypassing the general lemma entirely, and re-verification of the
antisymmetrization-linearity step). None of these checks located the
source of the inconsistency; they ruled out three candidate locations
with reasonable confidence. **IVN-CT8-Dirac-1b-i is promoted to the
current gating issue** for the entire chirality/Branch-2 sector — no
downstream item in this section should be treated as resting on solid
ground until it closes. A triangulation strategy is adopted for closing
it: derive the torsion-fermion coupling via three independent routes —
(1) **4D-first**: solve the Cartan equation algebraically in the full 4D
Einstein-Cartan-Dirac action, substitute to get the 4D quartic fermion
action, then reduce to FLRW; (2) **reduced-action**: perform the same
elimination/variation starting from the already-reduced FLRW action (the
route attempted in `SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md`); (3)
**direct-bilinear**: derive the torsion contribution to the Dirac equation
first, then contract directly into $\dot\eta,\dot J^0,\dot P,\dot A^0$
without passing through a reduced quartic action at all. If two of the
three agree and the third does not, the disagreement pinpoints where the
pathology lives — whether in the reduction-to-FLRW step, in the
auxiliary-field elimination itself, or in the antisymmetrization
prescription's extension to quartic terms (the leading hypothesis from
the investigation log). This triangulation has not yet been executed.
Version bumped to v13.4.

---

**Appendix P — v13.3 | June 2026**

Revised from v13.2: IVN-CT8-Dirac-1b (Section P.7.7.10) attempted and
found **PARTIAL**, not closed. A re-derivation from raw contorsion tensor
contraction (`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md`, June 2026)
confirms the axial coupling's operator structure ($\gamma^0\gamma^5$) and
magnitude directly from the Cartan equation, but finds that the coupling
is self-sourced (built from the same $\psi$ whose equation of motion is
being derived, not an external field), requiring an auxiliary-field
elimination treatment that produces a genuine quartic self-interaction
$\propto(A^0)^2$ — structurally consistent with the framework's existing
"Term 3 $\sim A_\mu A^\mu$" language. Varying that term correctly gives a
real contribution to $\dot\eta$ but an **inconsistent, unremoved imaginary
residual in $\dot P$**, which the document could not resolve. This opens
**IVN-CT8-Dirac-1b-i (CRITICAL)** and **reopens the question of whether
$\eta$ is protected in Branch 2** — Branch 1 remains unaffected since
$A^0=0$ there makes the entire question moot. The freeze established in
v13.1 remains in effect and is, if anything, reinforced by this finding.
1b-i should be pursued alongside 1c rather than after it. Version bumped
to v13.3.

---

**Appendix P — v13.2 | June 2026**

Revised from v13.1: IVN-CT8-Dirac-1a (Section P.7.7.10) is CLOSED. A formal
convention audit (`SCH_IVN-CT8-Dirac-1a_ConventionAudit_v1.md`, June 2026),
performed as a self-contained linear-algebra question before any further
dynamics, found that the only alternative Hermitian intertwiner capable of
making the scalar and vector-current bilinears simultaneously real without
the clean-room package's compensating factor is $A=r\,\gamma^0\gamma^5$
(unique up to real scaling) — and that this alternative works only by
exchanging physical roles (its "scalar" is the old pseudoscalar $P$; its
"current" is the old axial charge $A^0$, which cannot serve as a
probability density since it lacks a fixed sign relative to $\vert\psi\vert^2$).
The bare-$\gamma^0$ adjoint used throughout the clean-room package is
therefore forced by the ordinary physical requirement on $J^0$, not an
arbitrary convention choice. This validates the clean-room package's
central protection theorem for $\eta$ and unblocks IVN-CT8-Dirac-1b and
1c to proceed in parallel; 1d is downgraded to a notational
reconciliation. **The freeze on the Dirac/bilinear sector established in
v13.1 remains in effect** — 1a's closure increases confidence but does not
itself license migrating results into P.9.4.2, P.9.5.3, P.7.7.3,
P.7.7.3a, or CT-ix Section P.10.5; that single-pass canonical rewrite
still waits on 1b and 1c. Version bumped to v13.2.

---

**Appendix P — v13.1 | June 2026**

Revised from v13: This is a **freeze-and-annotate patch, not a canonical
rewrite.** A clean-room re-derivation of the cosmological Dirac equation and
its bilinear sector (`SCH_CleanRoom_Rederivation_v1.md`, June 2026) found
that IVN-I's Branch 2 correction (v13, Section P.7.7.3/P.7.7.3a) does not
survive re-derivation under a fully audited signature/reality convention —
the clean-room package finds $\dot\eta=-3H\eta$ exactly in both branches
(no $\kappa\alpha A^0P$ sourcing), traces the discrepancy to an unaudited
assumption about which fermion bilinears are real in this framework's
Clifford algebra, and additionally finds P.9.4.2 double-counts a term and
P.9.5.3 has the wrong sign on its Hubble-friction coefficient. Per an
explicit decision **not** to migrate this result into Appendix P
piecemeal, v13.1 does the following and no more: (1) marks IVN-I's monodromy
document `SCH_IVNI_MonodromyCorrection_v1.md` as **SUPERSEDED PENDING
CLEAN-ROOM CANONICALIZATION** rather than operative; (2) opens a single
consolidated upstream item, **IVN-CT8-Dirac-1** (new Section P.7.7.10,
below), absorbing what were separately tracked as the P.9.4.2 recheck, the
P.9.5.3 replacement, the P.7.7.3/P.7.7.3a replacement, and the CT-ix Branch
2 replacement; (3) updates the STATUS SUMMARY table (Gap 7, Gap 16) to
point to the freeze rather than to IVN-I's specific (now-superseded)
findings. **The body text of Sections P.7.7.3, P.7.7.3a, and P.10 (via the
companion CT-ix document) is deliberately left unrewritten** — those
sections are frozen in their v13 state, annotated as historical, pending
the canonical rewrite that will happen in one pass once IVN-CT8-Dirac-1
closes. Do not treat v13's P.7.7.3/P.7.7.3a content, or the CT-ix Branch 2
sections, as current physics as of this patch. Version bumped to v13.1.

---

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
| Gap 7 — Chirality inversion across bounce and sympathetic nucleation | **FROZEN — INTERNALLY INCONSISTENT AS DERIVED, PENDING IVN-CT8-Dirac-1b-i** | The v13 entry (IVN-I's convention-corrected monodromy calculation) is superseded pending clean-room canonicalization. The clean-room package's own claim ($\dot\eta=-3H\eta$ exactly, no sourcing) is itself **not confirmed** — IVN-CT8-Dirac-1b's re-derivation of the torsion coupling from raw contraction produces a term whose bilinear consequences are demonstrably inconsistent (an unremoved imaginary residual in $\dot P$, confirmed via three independent checks). This is not "pending further verification of a plausible result" — the current derivation, as it stands, is not internally consistent, and no claim about whether $\eta$ is sourced in Branch 2 should be treated as reliable until IVN-CT8-Dirac-1b-i closes. The qualitative PT-1 conclusion (chirality inversion per cycle non-generic) is not directly contradicted by any of this and may survive, but rests on machinery that is currently unverified. See Section P.7.7.10 for the consolidated open item and its triangulation strategy, and `SCH_IVNI_MonodromyCorrection_v1.md` for its own supersession notice. |
| Gap 8 — Photon-condensate coupling and CMB monopole | **OPEN TARGET** | CT-xiii identified. Prerequisites: CT-vii + CT-viii. |
| Gap 9 — Physical primitive: ψ as derived object, not ansatz | **ESTABLISHED** | P.0b: ψ is the unique minimal 4D rotational encoder; S_geo follows as consequence. Theorem 0. [New in v8] |
| Gap 10 — W-spin as mass: η as physical rotational departure | **ESTABLISHED** | Theorem 0: η = ψ̄ψ is the w-spin magnitude of the 4D knot; bridges physical picture and formalism. [New in v8] |
| Gap 11 — c as tangential S³ velocity: speed of light derived | **ESTABLISHED** | Theorem 5: c(t) = ω(t) · R_cosmic(t). Photon as minimum-w-spin surface wave. Constancy of c derived from S³ geometry. Lensing confirms photon w-spin is nonzero. [New in v8] |
| Gap 12 — Matter-light phase transition: topological distinctness | **ESTABLISHED** | Theorem 6: η = 0 and η ≠ 0 are distinct phases separated by a topological boundary, not points on a speed continuum. [New in v8] |
| Gap 15 — FLRW reduction of $S_{\text{geo}}$: modified Friedmann equations and bounce condition | **CLOSED** | CT-viii: modified Friedmann equations derived, two-branch cosmology established, bounce existence condition proven, GR recovery confirmed, kinetic coefficient $-3/2$ derived explicitly. Section P.9. [New in v10] |
| Gap 13 — Antipodal condensate coupling: mechanism linking local BH emission to global $S^3$ modes | **OPEN TARGET** | CT-xix identified. Prerequisites: CT-vii + CT-viii. CT-viii now closed. Physical motivation in *SCH_GalacticEngine_PhysicalPicture_v1* Section 2. [New in v9] |
| Gap 14 — Thermodynamic consistency of coherence-forcing: entropy accounting for galactic engine | **OPEN TARGET** | CT-xx identified. Prerequisites: CT-xix + Bi-209 calibration. Physical motivation in *SCH_GalacticEngine_PhysicalPicture_v1* Section 7. [New in v9] |
| Gap 16 — Cosmological dynamics: solution structure of the modified Friedmann system | **CLOSED for Branch 1; Branch 2 FROZEN — current derivation internally inconsistent, pending IVN-CT8-Dirac-1b-i** | CT-ix (June 2026): Branch 1 fully characterised — two-phase dynamics (stiff-condensate $a \propto t^{1/3}$, then dust-condensate); analytic solutions in each phase; explicit $a_{\text{max}} = \kappa m\eta_0/3$ and $R_{\text{universe}}$ as function of $m\eta_0$; CMB quadrupole constraint translates to $m\eta_0 \geq 9c^4/(8\pi G)$. **Confirmed unaffected by the freeze; Branch 1 involves no axial current and none of this section's difficulties apply to it.** Branch 2's late-time-attractor claim is frozen — not "pending confirmation of a working result" but pending resolution of a demonstrated internal inconsistency in the current derivation of the torsion coupling itself (IVN-CT8-Dirac-1b-i, CRITICAL, gating). Whether $\eta$ decouples from the chirality sector in Branch 2, as the clean-room package claimed, is an open question, not a likely-correct-but-unverified one. See Section P.7.7.10. See SCH_CT_ix_CosmologicalDynamics_v2.1.md. |

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
**Status as of v13.1: this paragraph describes what v13 claimed, not
what is currently believed — see the next paragraph.**

**Clean-room re-derivation (freeze trigger, v13.1):** A subsequent
clean-room re-derivation of the cosmological Dirac equation, performed
in a single audited $(-,+,+,+)$ convention with an explicit
bilinear-reality check done *before* any dynamics were derived, found
that IVN-I's own Branch 2 correction above does not survive
re-derivation. The corrected result is $\dot\eta=-3H\eta$ exactly, in
both branches, with no $\kappa\alpha A^0P$ source term — protected by
a structural argument ($X=\gamma^0\times\text{Hermitian}$ automatically
preserves $\bar\psi\psi$) rather than approximately true. Two further
upstream defects were located in the process: Section P.9.4.2
double-counts a term from the P.9.4.1 kinetic reduction, and Section
P.9.5.3's cosmological Dirac equation has the wrong sign on its
Hubble-friction coefficient. **Per an explicit decision not to migrate
this piecemeal, the chirality/Branch-2 sector of this appendix (Gap 7,
Gap 16, Sections P.7.7.3/P.7.7.3a, and the CT-ix Branch 2 sections) is
now FROZEN pending independent verification of the clean-room package
and a single-pass canonical rewrite.** See Section P.7.7.10
(IVN-CT8-Dirac-1) below and `SCH_CleanRoom_Rederivation_v1.md`.

**Status update, v13.2–v13.3:** IVN-CT8-Dirac-1a closed in favor of the
clean-room package's convention (the bare-$\gamma^0$ adjoint is forced,
not arbitrary — see P.7.7.10). This validated the *convention* underlying
the protection argument. However, IVN-CT8-Dirac-1b — re-deriving the
torsion coupling itself from raw contraction rather than importing it —
found that the coupling is self-sourced and, once treated correctly via
auxiliary-field elimination, produces an internally inconsistent result
under the current derivation, opening IVN-CT8-Dirac-1b-i (CRITICAL). **The
clean-room package's headline claim — $\dot\eta=-3H\eta$ exactly in
Branch 2, no sourcing — should therefore itself be read as reopened, not
confirmed**, pending 1b-i. What 1a settled is narrower than it may have
appeared: it settled that *if* the Dirac equation takes the protected
form, no alternative convention rescues a sourcing term; it did not
settle that the Dirac equation *does* take that form once the coupling's
self-sourced nature is fully accounted for. See
`SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md`.

**Status update, v13.4 — corrected framing.** A dedicated investigation
of IVN-CT8-Dirac-1b-i
(`SCH_IVN-CT8-Dirac-1b-i_InvestigationLog_v1.md`) ruled out three
candidate error locations (the raw-integral reality classification,
lemma-misapplication in the bilinear contraction, and dropped
cross-terms between the Levi-Civita and contorsion pieces) via
independent re-derivation, but **did not find the source of the
inconsistency**. To be unambiguous about what this means: **the
statement is not that 1b is a promising result awaiting final
confirmation. The statement is that the current derivation of the
torsion coupling, as it stands, is demonstrably self-inconsistent** — it
produces a real equation for $\dot\eta$ and a non-real (hence
impossible) equation for $\dot P$ from the same term via the same
method, checked three independent ways. No claim about whether $\eta$ is
sourced in Branch 2 can be made until this is fixed, in either
direction. **IVN-CT8-Dirac-1b-i is promoted to the current gating issue
for the entire chirality/Branch-2 sector.**

**Triangulation strategy adopted for closing 1b-i.** Rather than
continuing to re-derive along the single route already tried three
times, the coupling should be independently derived via three distinct
paths: **(1) 4D-first** — solve the Cartan equation algebraically in the
full 4D Einstein-Cartan-Dirac action, substitute to obtain the 4D
quartic fermion action, then reduce to the FLRW background; **(2)
reduced-action** — perform the same elimination/variation starting from
the already-reduced FLRW action (the route attempted so far); **(3)
direct-bilinear** — derive the torsion contribution to the Dirac
equation first, then contract directly into
$\dot\eta,\dot J^0,\dot P,\dot A^0$ without passing through a reduced
quartic action at all. If two of the three routes agree and the third
does not, the disagreement identifies where the pathology lives —
whether in the FLRW reduction step, in the auxiliary-field elimination
itself, or in the antisymmetrization prescription's extension to
quartic terms (the leading, unconfirmed hypothesis from the
investigation log). **This triangulation has not yet been executed.**

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

*[Historical note, v13.1: IVN-I-3 as stated above ("confirm the*
*Branch 2 η-sourcing correction") is itself superseded — see P.7.7.10*
*immediately below. It is retained here rather than deleted because it*
*is the item whose pursuit surfaced the deeper problem.]*

---

### **P.7.7.10 — Freeze Notice and IVN-CT8-Dirac-1**

*[New in v13.1.]*

**Freeze notice.** Sections P.7.7.3 and P.7.7.3a above, and the CT-ix
Branch 2 sections referenced from them (companion document
`SCH_CT_ix_CosmologicalDynamics_v2.md`, Section P.10.5), are **frozen as
of v13.1**. Their content is retained unrewritten for the historical
record and is not deleted, but neither should be cited as the current
state of the theory. The trigger is `SCH_CleanRoom_Rederivation_v1.md`
(June 2026), which re-derived the cosmological Dirac equation and its
bilinear consequences from a single audited $(-,+,+,+)$ convention
(explicit reality check performed on every bilinear before any dynamics
were written down) and found:

(i) $\dot\eta=-3H\eta$ exactly, in both branches, with no
$\kappa\alpha A^0P$ (or any other) source term — contradicting P.7.7.3a's
(E1-new). The protection is structural: any Dirac equation of the form
$\dot\psi=-\tfrac{3H}2\psi+\gamma^0W\psi$ with $W$ Hermitian (guaranteed
by any real action of the type used throughout this appendix)
automatically satisfies $\gamma^0X+X^\dagger\gamma^0=0$ for the scalar
channel, protecting $\bar\psi\psi$ exactly.

(ii) The $(A^0,P)$ oscillator itself differs in structure from both
v12's and IVN-I's corrected systems (different sign on $\dot A^0$
relative to $P$, an additional $\kappa\alpha A^0J^0$ term in $\dot P$
not present in either prior system, and retained Hubble friction that
IVN-I's correction had removed).

(iii) Two further upstream defects, both in Appendix P Section P.9:
P.9.4.2 double-counts a term already accounted for inside the
Hermitian-symmetrized kinetic construction of P.9.4.1, and P.9.5.3's
stated cosmological Dirac equation has the wrong sign on its
Hubble-friction coefficient (solving it as stated gives $\psi$ growing
with $a$, not diluting).

**Why a freeze rather than an incremental patch.** The clean-room
finding is a structural theorem, not a corrected numerical coefficient.
It either holds under independent check or it doesn't; there is no
"apply half of it" middle ground the way there might be for, e.g., a
mis-normalized coupling constant. Migrating it into this appendix
piecemeal — patching P.9.5.3 alone, or P.7.7.3 alone — risks leaving
the appendix in a state that is internally inconsistent in a new way
while the independent check is still pending. Sections P.7.7.3,
P.7.7.3a, P.9.4.2, P.9.5.3, and CT-ix Section P.10.5 will be rewritten
in a single pass once IVN-CT8-Dirac-1 (below) closes.

**IVN-CT8-Dirac-1** — consolidated upstream item, replacing the
now-superseded IVN-I-3 as the operative open question:

> *Re-derive the reduced cosmological Dirac equation and all four
> bilinear evolution equations ($\eta$, $J^0$, $P$, $A^0$) from the
> corrected real Lorentzian action, under a single fixed and explicitly
> audited convention charter, and confirm whether the clean-room
> system (`SCH_CleanRoom_Rederivation_v1.md`) is exact.*

This item absorbs, and replaces as separately-tracked items: the
P.9.4.2 double-count recheck, the P.9.5.3 replacement, the
P.7.7.3/P.7.7.3a replacement, and the CT-ix Branch 2 replacement. It is
sub-itemized as follows, mapped to the clean-room package's own
Verification Status section (CR-1 through CR-5):

| Item | Content | Maps to | Priority | Status |
|---|---|---|---|---|
| **IVN-CT8-Dirac-1a** | Confirm the Hermiticity assignment ($\gamma^{0\dagger}=-\gamma^0$ in $(-,+,+,+)$) is forced, not one of several valid choices — i.e., rule out an alternative representation in which $\bar\psi\psi$ *and* $J^\mu$ are simultaneously real without the compensating-$i$ construction the clean-room package used. This is the load-bearing item: if such a representation exists, the protection argument for $\eta$ must be rechecked under it. | CR-1 | **CRITICAL** | **CLOSED** — see `SCH_IVN-CT8-Dirac-1a_ConventionAudit_v1.md`. Solved exactly: the only alternative Hermitian intertwiner making $\Gamma=\mathbb1$ and $\Gamma=\gamma^\mu$ simultaneously real is $A=r\,\gamma^0\gamma^5$ (unique up to real scaling), and it works only by relabeling — its "scalar" is the old pseudoscalar $P$, and its "current" is the old axial charge $A^0$, which fails to track $\vert\psi\vert^2$ with a fixed sign and so cannot serve as $J^0$. The bare-$\gamma^0$ adjoint is therefore forced, and $\eta$'s protection theorem is validated, not merely assumed. |
| **IVN-CT8-Dirac-1b** | Independently re-derive the contorsion-sourced axial coupling coefficient ($\tfrac{\kappa\alpha}2A^0\gamma^0\gamma^5$) from the raw $K^{ab}_c$ contraction, matching the P.9.4.1-style spatial integration on $S^3$ but with the full $\omega=\overset\circ\omega+K$ connection. The clean-room package imported this coefficient's magnitude from the Cartan-equation normalization and verified only its reality, not its precise value/operator structure from first principles. | CR-3 | HIGH | **INTERNALLY INCONSISTENT AS DERIVED** — see `SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md`. The raw operator structure ($\gamma^0\gamma^5$) and magnitude are confirmed by direct index contraction — that part stands. But treating the self-sourced coupling via auxiliary-field elimination and varying the resulting quartic term produces a real $\dot\eta$ contribution alongside a **non-real, hence impossible, result for $\dot P$** from the identical method. This is not a promising-but-unconfirmed result; it is a demonstrated inconsistency. Superseded by IVN-CT8-Dirac-1b-i, now the gating item. |
| **IVN-CT8-Dirac-1b-i** | Identify and fix the source of the inconsistency in the self-sourced torsion coupling's derivation, such that all four bilinear equations ($\dot\eta,\dot J^0,\dot P,\dot A^0$) come out simultaneously real. See `SCH_IVN-CT8-Dirac-1b-i_InvestigationLog_v1.md`: three candidate error locations checked and ruled out (raw-integral reality classification; lemma-application in the bilinear contraction; cross-terms between Levi-Civita and contorsion pieces), **resolution not found**. Leading unconfirmed hypothesis: the antisymmetrization prescription $\tfrac i2(X-X^\dagger)$, established for terms linear in $\psi$, may not extend without modification to the quartic term produced by auxiliary-field elimination. **Recommended path: triangulate via three independent derivation routes — (1) 4D-first (solve Cartan in the full 4D action, substitute, then reduce to FLRW), (2) reduced-action (the route tried so far, starting from the already-reduced FLRW action), (3) direct-bilinear (derive the torsion contribution to the Dirac equation first, then contract directly into the four bilinear equations without a reduced quartic action at all). If two agree and one doesn't, the disagreement locates the pathology.** This triangulation has not yet been executed. Until this closes, whether $\eta$ is protected in Branch 2 is an **open question, not a likely-correct-but-unverified claim** — Branch 1 ($A^0=0$) is unaffected. | — (new) | **CRITICAL — CURRENT GATING ISSUE** | **OPEN.** |
| **IVN-CT8-Dirac-1c** | Independently re-verify the $J^0$, $P$, $A^0$ bilinear contractions in the clean-room package (Section 3 of that document). The $\eta$ contraction is simple enough to carry lower risk; these three involve more gamma-algebra and are comparatively under-checked. | CR-4 | HIGH | **UNBLOCKED** — may proceed, in parallel with 1b. |
| **IVN-CT8-Dirac-1d** | Reconcile the corrected $\eta\equiv-i\bar\psi\psi$ definition with Theorem 0's original, unqualified statement $\eta=\bar\psi\psi$. Confirm this is a labeling clarification (Theorem 0's physical content — w-spin magnitude, mass as departure-from-isotropy energy — is unaffected) rather than a substantive change requiring Theorem 0 itself to be reopened. **Scope note:** Theorem 0 is *not* frozen by this notice; only the literal bilinear formula requires the explicit sign/factor made visible. | CR-5 | MEDIUM | **UNBLOCKED, DOWNGRADED TO NOTATIONAL** — 1a's closure confirms Theorem 0's content is unaffected; this is now bookkeeping, not open physics. |

**Sequencing.** ~~IVN-CT8-Dirac-1a gates everything else~~ **1a is now
CLOSED** (see table and `SCH_IVN-CT8-Dirac-1a_ConventionAudit_v1.md`):
the alternative Hermiticity assignment that would have required rebuilding
the clean-room package's central argument does not exist in viable form.
**1b's derivation, as it stands, is internally inconsistent, not merely
partial** (see `SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md`): the raw
operator structure is confirmed, but the self-sourced coupling's
consequences fail a basic consistency check (real $\dot\eta$, non-real
$\dot P$, from the same method). A dedicated investigation
(`SCH_IVN-CT8-Dirac-1b-i_InvestigationLog_v1.md`) ruled out three
candidate causes without finding the actual one. **IVN-CT8-Dirac-1b-i is
the sole current gating issue for this entire section — updated order:
1a (closed) → 1b-i (gating; triangulate via the three routes specified in
the table above) → 1c.** 1c should wait on 1b-i's resolution rather than
run in parallel, since 1c re-verifies bilinear contractions that are
themselves in question until 1b-i identifies where the derivation goes
wrong. Only after 1b-i closes and 1c independently verifies the corrected
system should the canonical rewrite of P.9.4.2, P.9.5.3, P.7.7.3,
P.7.7.3a, and CT-ix Section P.10.5 be performed, in one pass. The freeze
established in this section remains in effect for the Dirac/bilinear
sector until that rewrite — **this is not a precaution against an
unconfirmed result; it is a direct consequence of the current derivation
being demonstrably inconsistent.** The question of whether $\eta$ is
protected in Branch 2 is open, not pending confirmation of a likely
answer. 1a's
closure
increases confidence in the clean-room package but does not itself lift
the freeze on P.7.7.3/P.7.7.3a/P.10.5, since 1b and 1c remain open.

**Status of `SCH_IVNI_MonodromyCorrection_v1.md`.** That working
document is marked **SUPERSEDED PENDING CLEAN-ROOM CANONICALIZATION** —
not simply superseded — in its own header. It is retained as the record
of the intermediate correction attempt that first exposed the
metric-convention inconsistency in the original v12 PT-1 calculation,
and its own internal inconsistencies are in turn what prompted the
clean-room package. Its qualitative conclusion (chirality inversion is
non-generic) is not contradicted by the clean-room finding and may
survive canonicalization; its specific bilinear system should not be
cited as current pending IVN-CT8-Dirac-1.

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
>
> **⚠️ UPDATE, v13.1 — SUPERSEDED PENDING CLEAN-ROOM CANONICALIZATION.**
> The IVN-I finding referenced in the box above ($\kappa\alpha A^0P$
> sourcing $\eta$) is itself now frozen and does not survive the
> clean-room re-derivation of the cosmological Dirac equation
> (`SCH_CleanRoom_Rederivation_v1.md`). That package finds
> $\dot\eta=-3H\eta$ exactly in both branches — if it holds under
> independent check (IVN-CT8-Dirac-1, Appendix P Section P.7.7.10),
> Branch 2 is *simpler* than this box assumed: $\eta$ decouples from
> the chirality sector entirely, and the "highest-priority open item"
> becomes rebuilding the $(A^0,P)$ oscillator alone, not a coupled
> three-variable system. Do not treat this box's IVN-I-3 framing, or
> the "provisional" conclusions below, as reflecting the current best
> understanding — both are themselves superseded pending
> IVN-CT8-Dirac-1. The original v13 caveat text is left otherwise
> unedited below, per the freeze policy of not migrating results
> piecemeal.

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
**End of Appendix P — v13.4**

*June 2026 | Not for citation without author approval*

*Summary of v13.4 changes: IVN-CT8-Dirac-1b-i investigated
(`SCH_IVN-CT8-Dirac-1b-i_InvestigationLog_v1.md`). Three candidate error
locations ruled out; the source of the inconsistency was not found.
**Status language corrected throughout this appendix: 1b is not a
promising, nearly-confirmed result — it is a demonstrated internal
inconsistency** (real $\dot\eta$, non-real $\dot P$, from the identical
derivation method). IVN-CT8-Dirac-1b-i is promoted to the sole current
gating issue for the chirality/Branch-2 sector; 1c is deferred to run
after it, not alongside it. A triangulation strategy (4D-first,
reduced-action, direct-bilinear routes) is specified for closing 1b-i but
has not been executed. The freeze is unchanged in scope but is now framed
correctly: it reflects a known inconsistency, not caution around an
unconfirmed-but-plausible result. Branch 1 remains fully unaffected.*

*June 2026 | Not for citation without author approval*

*Summary of v13.3 changes: IVN-CT8-Dirac-1b attempted, found PARTIAL.
Operator structure and magnitude of the torsion coupling confirmed by
direct contraction; but the self-sourced (auxiliary-field) treatment
required for a coupling built from the field's own current produces an
internally inconsistent (partially imaginary) result. Opens
IVN-CT8-Dirac-1b-i (CRITICAL). Whether $\eta$ is protected in Branch 2 is
now reopened, not confirmed. Freeze reinforced, not lifted. Branch 1
unaffected.*

*June 2026 | Not for citation without author approval*

*Summary of v13.2 changes: IVN-CT8-Dirac-1a CLOSED (Section P.7.7.10
table and sequencing updated) following the formal convention audit in
`SCH_IVN-CT8-Dirac-1a_ConventionAudit_v1.md`. The bare-$\gamma^0$ adjoint
is confirmed forced, not an arbitrary choice, validating the clean-room
package's $\eta$ protection theorem. 1b and 1c unblocked to proceed in
parallel; 1d downgraded to notational. The Dirac/bilinear-sector freeze
established in v13.1 remains in effect pending 1b/1c.*

*Summary of v13.1 changes (freeze-and-annotate patch, not a canonical
rewrite): (1) `SCH_IVNI_MonodromyCorrection_v1.md` marked SUPERSEDED
PENDING CLEAN-ROOM CANONICALIZATION in its own header. (2) New Section
P.7.7.10 opens IVN-CT8-Dirac-1 (sub-items 1a–1d) as the consolidated
upstream item, replacing IVN-I-3 and absorbing the P.9.4.2 recheck, the
P.9.5.3 replacement, the P.7.7.3/P.7.7.3a replacement, and the CT-ix
Branch 2 replacement. (3) STATUS SUMMARY table Gap 7 and Gap 16 entries
updated to point to the freeze. (4) The P.10 Branch-2 caveat box (v13)
receives a v13.1 update-box on top of it, without editing the original
text. (5) Sections P.7.7.3, P.7.7.3a are explicitly left unrewritten —
frozen, historical, not current. Branch 1, the FLRW reduction (P.9/CT-viii
proper), and all galactic-scale results remain unaffected and are not
part of the freeze. Theorem 0 is not frozen; only its literal bilinear
formula is flagged (IVN-CT8-Dirac-1d) as needing an explicit sign
clarification.*
