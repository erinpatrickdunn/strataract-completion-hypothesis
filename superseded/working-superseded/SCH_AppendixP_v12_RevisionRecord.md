# Appendix P — v12 Revision Record
## Changes from v11 | June 2026

This document records all changes between Appendix P v11 and v12.
It is not a standalone version of Appendix P — it records the diffs
only. The full v12 is produced by applying these changes to v11.

All other content from v11 is carried forward unchanged.

---

## Revision Header (replaces v11 header block)

**Appendix P — v12 | June 2026**

Revised from v11: Gap 7 status revised following completion of the PT-1
analysis programme (PT-1 Problem Specification v1, PT-1 Proof Attempt v1,
IVN-16 Resolution v1, PT-1 Monodromy Calculation v1, PT-1 Topological
Phase Investigation v1). The claim that the standard spin representation
on $S^3$ predicts $A^\mu \to -A^\mu$ universally is not supported by
calculation. The correct result is that the chirality transformation per
cycle is the holonomy of a natural $\mathrm{U}(1)$ connection on the
condensate axial-current line bundle, with value $e^{i\alpha_+}$ where
$\alpha_+ = \int_{\text{cycle}}\Omega\,dt$ is a continuous, parameter-dependent
quantity. A systematic investigation of topological quantization mechanisms
finds no mechanism that forces $e^{i\alpha_+} = -1$ universally. Gap 7
status changed from PREDICTION to OPEN QUESTION — CLAIM REVISED.
Section P.7.7 updated accordingly. CT-ix closed (Section P.10, added).
All other content from v11 unchanged. Version bumped to v12.

---

## 1. Status Table: Gap 7 Entry (replaces line 37 of v11)

**Old entry:**

| Gap 7 — Chirality inversion across bounce and sympathetic nucleation | **PREDICTION (proof outstanding)** | Standard spin representation on S³ predicts A(mu) → −A(mu). PT-1 is the formal confirmatory proof target. CT-viii prerequisite. |

**New entry:**

| Gap 7 — Chirality inversion across bounce and sympathetic nucleation | **OPEN QUESTION — CLAIM REVISED** | The PT-1 analysis programme (v1, June 2026) established: (1) $A^0$ is continuous through the bounce with no local sign flip; (2) the normal-mode evolution defines a natural $\mathrm{U}(1)$ connection on the condensate axial-current line bundle $L_+$ over the cosmological cycle; (3) the chirality transformation per cycle is the holonomy $e^{i\alpha_+}$ where $\alpha_+ = \int_{\text{cycle}}\Omega\,dt \approx 2m T_{\text{eff}}$; (4) a systematic investigation of topological quantization mechanisms (spin structures, Aharonov-Bohm, Berry phase, global $S^3$ mode coupling) finds no mechanism that forces $e^{i\alpha_+} = -1$ universally; (5) the original argument from the spatial antipodal map on $S^3$ gives $\psi \to -\psi$ but $A^\mu \to +A^\mu$ for bilinears — the wrong sign. The holonomy is a continuous function of the action parameters, computable after the Bi-209 calibration. Sympathetic nucleation is not ruled out but the chirality inversion claim is not established. See PT-1 working documents (June 2026). |

---

## 2. Status Table: CT-ix Entry (new row, to be inserted after Gap 15)

**New entry:**

| Gap 16 — Cosmological dynamics: solution structure of the modified Friedmann system | **CLOSED** | CT-ix (June 2026): Branch 1 fully characterised — two-phase dynamics (stiff-condensate $a \propto t^{1/3}$, then dust-condensate); analytic solutions in each phase; explicit $a_{\text{max}} = \kappa m\eta_0/3$ and $R_{\text{universe}}$ as function of $m\eta_0$; CMB quadrupole constraint translates to $m\eta_0 \geq 9c^4/(8\pi G)$. Branch 2 asymptotes to Branch 1 at late times. Phase I stiff-condensate epoch predicts blue-tilted gravitational wave background ($n_T = -1$). Eight IVN items and five open questions identified; independent verification required before downstream use. See SCH_CT_ix_CosmologicalDynamics_v1.md. |

---

## 3. Closure Summary Table: Additional Rows (to be appended to P.6 table)

**New rows to append to the P.6 closure summary:**

| Cosmological dynamics: Branch 1 and Branch 2 solution structure | **CLOSED (IVN pending)** | CT-ix: two-phase Branch 1 dynamics, $R_{\text{universe}}$ derived, CMB constraint on $m\eta_0$, Branch 2 late-time attractor. Eight IVN items require independent verification. |

| Chirality inversion: holonomy of condensate axial-current bundle | **OPEN QUESTION — CLAIM REVISED** | PT-1 programme: holonomy is $e^{i\alpha_+}$, not universally $-1$. No topological quantization mechanism identified. Computable after Bi-209 calibration. See PT-1 working documents. |

---

## 4. Section P.7.7 Replacement

The following replaces Section P.7.7 in its entirety.

---

### **P.7.7 Chirality Across the Bounce and Sympathetic Nucleation**

*[Revised in v12 following the PT-1 analysis programme, June 2026.
The PT-1 analysis comprises five working documents: Problem Specification v1,
Proof Attempt v1, IVN-16 Resolution v1, Monodromy Calculation v1, and
Topological Phase Investigation v1. The original P.7.7 (v5–v11) is
superseded by this section. The physical motivation for sympathetic
nucleation is preserved. The claimed mechanism for chirality inversion
is revised.]*

#### **P.7.7.1 The Question**

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

This question was the subject of PT-1. The result is stated in P.7.7.3
below.

#### **P.7.7.2 The Original Claim and Why It Fails**

Previous versions of this section (v5–v11) stated:

> *"In the standard spin representation, spinors on $S^3$ acquire a
> sign change under the antipodal map: $A^\mu \to -A^\mu$ (chirality
> inverts at each bounce). This is not one of two open possibilities —
> it is the default consequence of the standard spin representation
> on $S^3$."*

The PT-1 analysis shows this claim is incorrect in two respects.

**First**, the spatial antipodal map on $S^3$ sends $\psi \to -\psi$
(because $-\mathbf{1} \in \mathrm{SU}(2)$ acts as $-1$ on the spinor
representation). But $A^\mu = \bar{\psi}\gamma^\mu\gamma^5\psi$ is
bilinear in $\psi$: under $\psi \to -\psi$, both $\bar{\psi}$ and
$\psi$ change sign, giving $A^\mu \to (-1)^2 A^\mu = +A^\mu$.
The spatial antipodal map gives $A^\mu \to +A^\mu$, not $-A^\mu$.

**Second**, the bounce is not a spatial antipodal map. The bounce is
a continuous event in the temporal evolution — the turnaround of
$\dot{a}(t)$ — governed by the cosmological Dirac equation from CT-viii.
$A^0$ is continuous through the bounce (P.9.6.3) with no local sign flip.

Neither the spatial antipodal map nor the temporal bounce produces
$A^\mu \to -A^\mu$ as a local, automatic consequence of the dynamics.

#### **P.7.7.3 The PT-1 Result: The Holonomy of the Axial-Current Bundle**

The cosmological Dirac equation (P.9.5.3), applied to the bilinears
$(A^0, P)$ where $P = \bar{\psi}\gamma^5\psi$, produces (in the
corrected $(-,+,+,+)$ convention established by the IVN-16 Resolution):

$$\dot{A}^0 = i(2m + \lambda\eta)P - i\kappa\alpha J^0 A^0 \tag{E-A}$$

$$\dot{P} = i(2m + \lambda\eta)A^0 - i\kappa\alpha J^0 P \tag{E-P}$$

These decouple into normal modes $u = A^0 + P$ and $v = A^0 - P$:

$$\dot{u} = i\Omega_+(t)\,u, \qquad \dot{v} = -i\Omega_-(t)\,v$$

where $\Omega_\pm = \Omega \pm \Gamma$, $\Omega = 2m + \lambda\eta_0/a^3$,
$\Gamma = \kappa\alpha\mathcal{J}/a^3$.

The solution is:
$$u(t) = e^{i\int\Omega_+ dt}\,u(0), \qquad
v(t) = e^{-i\int\Omega_- dt}\,v(0)$$

This is the form of parallel transport — holonomy — in a $\mathrm{U}(1)$
connection on a complex line bundle. The connection is natural with
respect to the $\mathrm{SO}(3)$ isotropy of the cosmological background:
it is derived from the spin connection and condensate dynamics of
$S_{\text{geo}}$, not introduced by hand.

**The monodromy matrix** after one complete cosmological cycle is:

$$M = e^{i\alpha_-}\begin{pmatrix}
\cos\alpha_+ & i\sin\alpha_+ \\
i\sin\alpha_+ & \cos\alpha_+
\end{pmatrix}$$

where:

$$\alpha_+ = \int_{\text{cycle}}\Omega\,dt
= \int_{\text{cycle}}\left(2m + \frac{\lambda\eta_0}{a^3}\right)dt
\quad \text{(oscillation phase)}$$

$$\alpha_- = -\int_{\text{cycle}}\Gamma\,dt
= -\int_{\text{cycle}}\frac{\kappa\alpha\mathcal{J}}{a^3}\,dt
\quad \text{(damping phase)}$$

*(Both integrals are regulated by the condensate melting at $T = T_c$,
providing a physical cutoff at $a = a_c$ near the bounce. IVN items
from the monodromy calculation require independent verification.)*

**$M = -\mathbf{1}$ (chirality inversion) if and only if** $\alpha_+
= (2n-1)\pi$ (odd multiple of $\pi$) and $\alpha_- = 2k\pi$ for
integers $n, k$, or $\alpha_+ = 2n\pi$ and $\alpha_- = (2k+1)\pi$.
These are quantization conditions on the action parameters, not
automatic consequences of the dynamics.

#### **P.7.7.4 Is the Phase Topologically Quantized?**

A systematic investigation (PT-1 Topological Phase Investigation v1,
June 2026) checked all candidate mechanisms for topological quantization
of $\alpha_+$:

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
degeneracy point $\mathcal{J} = 0$ is not enclosed for the physical
case $\mathcal{J} \neq 0$.
Result: zero for Branch 1; zero for Branch 2 with $\mathcal{J} \neq 0$.

**Global $S^3$ mode coupling:** The spatial modes of $\psi$ on $S^3$
decouple from the zero mode at quadratic order (shown by the $S^3$
integration in P.9.4.1). Nonlinear corrections from the quartic
term are suppressed in the mean-field approximation.
Result: no quantization from global $S^3$ modes at this order.

**Conclusion:** No topological mechanism quantizes $\alpha_+$.
The holonomy $e^{i\alpha_+}$ is a continuous, parameter-dependent
element of $\mathrm{U}(1)$.

#### **P.7.7.5 The Physical Situation**

With the preliminary estimate $m \sim m_{\text{eff}} \sim 10^{-6}$ eV
and $T_{\text{eff}} \sim t_{\text{max}} \sim (\pi/2)R_{\text{universe}}
\sim 10^{60}$ eV$^{-1}$:

$$\alpha_+ \approx 2m \cdot T_{\text{eff}} \sim 2 \times 10^{-6}
\times \frac{\pi}{2} \times 10^{60} \sim 10^{54}$$

The phase is astronomically large. The value of $\alpha_+ \mod \pi$
— which determines whether $M = -\mathbf{1}$ — is exquisitely sensitive
to the precise values of $m$ and $R_{\text{universe}}$. It cannot be
determined without the Bi-209 calibration.

**However**, the sensitivity cuts both ways. The matter-creation epoch
(the $T < T_c$ window following the bounce during which sympathetic
nucleation operates) has a duration $\delta t_c \sim H_c^{-1}$ where
$H_c$ is the Hubble rate at $T = T_c$. During this epoch, $A^0$
rotates by an angle $\delta\alpha \sim 2m \cdot \delta t_c$.

If $\delta\alpha \ll \pi$ — i.e., if the matter-creation epoch is
short compared to one half-rotation period $\pi/(2m)$ — then $A^0$
has an approximately definite sign during nucleation regardless of
whether $M = -\mathbf{1}$ over the full cycle. The chirality of each
cycle's matter content is set by the sign of $A^0$ at the start of
the matter-creation epoch, which is determined by the accumulated
phase from all previous cycles.

Whether $\delta\alpha \ll \pi$ is a quantitative question requiring:

(1) $m$ from the Bi-209 calibration
(2) $H_c$ from the condensate melting temperature $T_c \sim m_{\text{eff}}/k_B$
    and the standard thermal history

This calculation is identified as a sub-target of CT-ix (OQ-CT-ix-5)
and should be performed once the Bi-209 calibration is available.

#### **P.7.7.6 The Sympathetic Nucleation Mechanism: Preserved**

The physical mechanism for within-cycle matter surplus is unchanged:

Standard vacuum pair creation (Event Type 1): particle + antiparticle,
opposite chirality, net baryon number 0.

In the presence of a condensate with $\langle A^0\rangle \neq 0$
(Event Type 2): two particles, same chirality, net baryon number $+2$.

Probability ratio: $P(\text{Type 2})/P(\text{Type 1}) \sim
|\langle A^0\rangle|^2/m_{\text{eff}}^2$.

In the language of Theorem 6: the matter-creation epoch begins at the
first-order phase transition $\eta: 0 \to \eta_{\text{eq}}$ following
the bounce. The chirality bias $\langle A^0\rangle \neq 0$ of the
reconstituted condensate drives Type 2 nucleation. The sign of
$\langle A^0\rangle$ at this epoch determines whether the current
cycle is matter-dominated or antimatter-dominated.

**What is preserved:** The sympathetic nucleation mechanism itself.
The existence of a chirality bias. The Sakharov condition realisations
(P.7.7.8 below).

**What is revised:** The claim that this bias necessarily inverts
sign at each bounce. It may invert, may not invert, or may follow
a complex multi-cycle pattern. The specific value of $\langle A^0\rangle$
at the start of the current cycle's matter-creation epoch is determined
by the accumulated holonomy phase from all previous cycles — a quantity
that is computable but not universally fixed by topology.

#### **P.7.7.7 Relationship to the JWST Anomaly**

The JWST early massive galaxy anomaly (anomalously massive, compact
galaxies at $z \sim 10$–16) was interpreted in earlier versions as
evidence for within-cycle matter surplus from sympathetic nucleation.

This interpretation is preserved in the following sense: if the
current cycle has $\langle A^0\rangle \neq 0$ at the matter-creation
epoch (which is required for any matter to exist at all), then
sympathetic nucleation is active and the within-cycle matter surplus
is nonzero. The JWST anomaly is consistent with this.

What is no longer claimed: that the matter surplus is a universal
consequence of the bounce rather than a consequence of the specific
value of $\langle A^0\rangle$ in the current cycle. The magnitude of
the surplus — and therefore the degree of early galaxy enhancement —
depends on $|\langle A^0\rangle|/m_{\text{eff}}$ at the matter-creation
epoch. This is computable after the Bi-209 calibration provides $m$
and $m_{\text{eff}}$.

#### **P.7.7.8 Relationship to the Sakharov Conditions**

Unchanged from v11. The condensate structure provides geometric
realisations of all three Sakharov conditions:

(1) **Baryon number violation:** Event Type 2 nucleation produces net
    baryon number $+2$ per event.

(2) **CP violation:** $\langle A^0\rangle \neq 0$ is a nonzero axial
    current, breaking $C$ and $CP$ symmetry in the condensate background.

(3) **Departure from thermal equilibrium:** The bounce drives the
    condensate through the $\eta = 0$ phase boundary (Theorem 6) —
    a first-order phase transition, not a thermal equilibrium process.

These are structural correspondences. Quantitative demonstration
requires PT-2 (Bogoliubov analysis) and the Bi-209 calibration.
PT-4 (formal derivation of Sakharov conditions from $S_{\text{geo}}$)
is an identified proof target.

#### **P.7.7.9 Revised Proof Target Structure**

**PT-1** [REVISED — now a quantitative calculation, not a confirmatory
proof]:

Compute the monodromy phase $\alpha_+^{\text{reg}}$ and $\alpha_-^{\text{reg}}$
numerically for the physical action parameters fixed by the Bi-209
calibration. Determine the value of $M_{\text{reg}}$ and whether the
matter-creation epoch duration $\delta t_c$ satisfies $\delta\alpha
\ll \pi$. Report $\langle A^0\rangle$ at the start of the current
cycle's matter-creation epoch.

*Prerequisite:* Bi-209 calibration (fixing $m$, $\alpha$, $m_{\text{eff}}$).
*Expected result:* A specific numerical value for the holonomy phase
and a quantitative prediction for the within-cycle matter surplus.
*Nature of result:* Numerical, not topological.

**PT-2** [Unchanged]: Bogoliubov analysis of pair creation in chiral
condensate background. Full computation of $P(\text{Type 2})/P(\text{Type 1})$
as a function of $\{\alpha, \lambda, m, \langle A^0\rangle\}$.
*Prerequisite:* PT-1 (revised) for the value of $\langle A^0\rangle$.

**PT-3** [Status changed — now primary, not contingent]:

Self-consistent evolution equation for $\langle A^0\rangle$ across
$N$ bounce cycles, using the monodromy matrix $M_{\text{reg}}$
established by PT-1. Determine whether the long-run sequence of
$\langle A^0\rangle$ values is periodic, quasi-periodic, or ergodic.

*Prerequisite:* PT-1 (revised).
*Note:* PT-3 was previously contingent on an "unexpected" PT-1 result.
The PT-1 analysis has produced exactly this situation: the holonomy is
not $-\mathbf{1}$ universally, and the multi-cycle evolution of
$\langle A^0\rangle$ requires PT-3 for its description.

**PT-4** [Unchanged]: Formal derivation of Sakharov conditions from
$S_{\text{geo}}$.

---

## 5. Section P.10: CT-ix Summary Entry (new section, to be appended after P.9)

The following section header and summary are added as P.10. The full
CT-ix derivation is in the companion document
SCH_CT_ix_CosmologicalDynamics_v1.md (June 2026).

---

### **P.10 CT-ix: Cosmological Dynamics from the Modified Friedmann System**

*[New in v12. Full derivation in SCH_CT_ix_CosmologicalDynamics_v1.md.
Verification status: internally derived; eight IVN items require
independent verification before downstream use.]*

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

**Branch 2 (torsion-active, $A^0 \neq 0$):**

The $(A^0, P)$ bilinears satisfy coupled oscillator equations with
time-varying frequency $\Omega_{\text{mix}} = 2m + \lambda\eta_0/a^3$.
At late times, $(A^0)^2$ decays as $a^{-3}$ and Branch 2 asymptotes
to Branch 1. The bounce condition is satisfied generically.

**Open questions generated by CT-ix:**

OQ-CT-ix-1: Explicit $c(t)$ derivation from the Phase III solution.
OQ-CT-ix-2: Overlap between Phase I power suppression and CMB quadrupole.
OQ-CT-ix-3: $\eta$ evolution correction at finite $A^0$ in Branch 2.
OQ-CT-ix-4: Transition scale $a_*$ vs. observed matter-radiation equality.
OQ-CT-ix-5: Duration of matter-creation epoch relative to rotation period $\pi/(2m)$ — the key input for the revised PT-1 calculation.

**IVN items:** Eight independent-verification items are identified in
the CT-ix document. IVN-2 ($\eta$ dilution derivation) and IVN-5 
(confirmation of E1 by explicit calculation) are highest priority.
Results should not be used downstream until these are verified.

---

## 6. Final Status Paragraph (replaces the closing paragraph of the v11 STATUS SUMMARY)

**Old closing paragraph:**

> The framework has a closed variational structure within its stated
> EFT and mean-field condensate regime. All claims are regime-conditional.
> The density hierarchy is explicit and bounded. Sections P.7.5, P.7.6,
> and P.7.7 cover cosmological predictions of the closed theory. Section
> P.0b and Theorems 0, 5, and 6 are new in v8. CT-xix and CT-xx are
> new open targets in v9; they are extensions into territory opened by
> the galactic engine physical picture and do not affect the existing
> variational closure.

**New closing paragraph:**

The framework has a closed variational structure within its stated
EFT and mean-field condensate regime. All claims are regime-conditional.
The density hierarchy is explicit and bounded.

Two developments in v12 change the epistemic landscape of the
cosmological sector:

**CT-ix (closed):** The cosmological dynamics are now derived from the
modified Friedmann equations of CT-viii. The Phase I and Phase III
solution structures are established, $R_{\text{universe}}$ is derived
as a function of the action parameters, and the CMB quadrupole
suppression constraint is expressed as a bound on $m\eta_0$. Eight
IVN items require independent verification.

**PT-1 (revised):** The chirality inversion claim is not established
as a universal consequence of the dynamics. The correct formulation
is that the chirality transformation per cycle is the holonomy of a
natural $\mathrm{U}(1)$ connection on the condensate axial-current
line bundle, with value $e^{i\alpha_+}$ determined by the action
parameters. No topological mechanism quantizes this phase. The
chirality of the current cycle and the magnitude of the within-cycle
matter surplus are computable after the Bi-209 calibration. PT-3,
previously contingent, is now a primary proof target alongside PT-2.

The galactic-scale variational closure established in v8 and the
FLRW reduction of v10–v11 are unaffected by these revisions. The
revisions are confined to the cosmological chirality sector and do
not alter any galactic-scale prediction or formal proof.

---

*Appendix P v12 Revision Record — June 2026*
*Not for citation without author approval.*
*This document records changes only. The full v12 is v11 with these
changes applied. Independent verification of all IVN items from
CT-viii (P.9) and CT-ix (P.10) is required before downstream calculations
treat those results as established.*
