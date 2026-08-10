# SCH — The Ampère Anomaly as a Term-3 Falsification Branch
## CISP, the Cartan Substitution, and the Nonequilibrium-Mechanics Choke Point

*Working Document — v1 | August 2026*

**Status:** OPEN INVESTIGATION — audit pass complete; mechanical link unresolved by design, not by omission.

**Origin:** Paper B (Draft 2.0) §6.3 identifies the Term-3 (torsion) contribution to the Ampère force anomaly as a "secondary candidate," flagged as requiring "a quantitative estimate of spin polarization magnitude in specific conductor materials before it can be evaluated" — a requirement never previously met. This document is that evaluation, carried as far as it currently goes.

**What this document is not:** a numerical Term-3 prediction. No such prediction is made here, and Section 7 explains specifically why one would currently be manufactured rather than derived.

**Relationship to the existing corpus:** This document does not modify Paper B §6, Appendix P, or any closed theorem. It is a standalone audit of one previously unexamined sub-claim (§6.3's spin-polarization mechanism), producing a falsification-branch classification suitable for incorporation into Paper B's Section 6 and Appendix P's calculational-target table on future revision, at the discretion of whoever performs that integration pass.

---

## Executive Summary

Paper B §6.3 proposes that the Ampère force anomaly (Nasilowski 1964; Graneau 1982, 1983, 1987) might have a secondary Term-3 (torsion) contribution, sourced by current-induced spin polarization coupling through the Cartan equation. This was never quantified. This audit traces the mechanism from its kinematic requirement through to its first genuine theoretical obstruction, with five results:

1. **The mechanism's kinematic prerequisite — a current-*aligned* (axial) spin polarization — does not exist in ordinary conductors by symmetry**, but does exist, and is experimentally measured, in a specific class of chiral, spin-orbit-coupled crystals (Current-Induced Spin Polarization, CISP). This closes a geometric objection that was not previously identified in the corpus.
2. **The operator dictionary connecting SCH's relativistic axial bilinear to a laboratory spin observable has an exact, closed-form piece** — the spatial components — resolving what was expected to be an open normalization problem (cf. Paper A §2.3's flagged $\eta_{\max}$ gap, of which this is a structural relative).
3. **A real, published measurement anchors the numerical scale of $A^\mu_{\rm SCH}$** for the first time in any laboratory context in this corpus, replacing an earlier order-of-magnitude benchmark that is now known to have been wrong by roughly 42 orders of magnitude.
4. **The tightest existing laboratory bound on fermion-coupled torsion (Kostelecký, Russell & Tasson 2008) does not constrain $\alpha$** at the measured CISP amplitude — not narrowly, but by a margin of decades of orders of magnitude, closing this particular kill-test route without closing the theory.
5. **The remaining step — whether the SCH torsion-contact interaction produces a mechanical force in this driven, nonequilibrium state — is unresolved, and is shown to be unresolved for reasons that are not specific to SCH.** This is classified accordingly.

Section 8 gives the full choke-point classification and the reasoning for treating unresolved steps differently depending on whether the theory or the surrounding field is the bottleneck.

---

## 1. Starting Point: What Paper B §6.3 Actually Claims

Paper B §6.2–6.3 propose two independent SCH mechanisms for the Ampère anomaly:

- **Term 2** (primary): bulk electron velocity coherence in ballistic pre-thermal current flow sources $C_{\mu\nu}=\rho\eta u_\mu u_\nu$, producing longitudinal stress. This has a derived leading-order scaling law (Draft 2.0, audit item BB-1): $\Delta Q_{zz}^{(2)} = \tfrac23\rho\eta\bar v_d^2 \propto \eta J^2$.
- **Term 3** (secondary): current-induced spin polarization activates the axial current $A^\mu\neq0$, which sources torsion via the Cartan equation, producing a competing contribution. Paper B states plainly that this "requires a quantitative estimate of spin polarization magnitude in specific conductor materials before it can be evaluated" and supplies no such estimate.

This document supplies that estimate, or rather, traces exactly how far the chain

$$J \;\longrightarrow\; A^\mu \;\longrightarrow\; T_{\lambda\mu\nu} \;\longrightarrow\; H_{\rm SCH} \;\longrightarrow\; \Delta Q_{zz}^{(3)}$$

can currently be carried, and where it stops.

---

## 2. The Kinematic Obstruction, and Why It Is Not Fatal

### 2.1 The naive picture fails by symmetry

The most natural candidate source for current-induced spin polarization is the Pauli/Zeeman response to a conductor's own self-field, $B(r)=\mu_0 I r/2\pi a^2$ inside a wire of radius $a$. This mechanism requires no spin-orbit coupling and needs no exotic material. It also fails to produce what Term 3 requires: the induced polarization tracks the local field direction, which is **azimuthal** ($\hat\phi$, circling the wire axis) by construction. At every point in the cross-section the induced moment points transverse to the current, not along it. There is no macroscopic axial ($\hat z$) polarization to feed into $A^z$ from this channel, regardless of material or current density.

Ordinary current-induced spin-orbit effects (the interfacial Edelstein effect, the spin Hall effect) do not rescue this: both produce polarization **transverse** to the current, not parallel to it, in generic conductors.

### 2.2 The symmetry condition for axial polarization

By Neumann's principle, a linear response connecting a polar vector (current $J$) to an axial vector (spin polarization $S$) in the *same* direction requires a **pseudoscalar** coupling coefficient — a quantity that changes sign under a mirror reflection. This is symmetry-forbidden in any material with a mirror plane or inversion center. It is allowed, and only allowed, in materials belonging to one of the eleven **Sohncke (enantiomorphic) point groups** — crystals with a genuine structural handedness and no improper symmetry operations at all.

### 2.3 The real mechanism: Current-Induced Spin Polarization (CISP)

This is not hypothetical. It is measured, and it has a name in the condensed-matter literature: **Current-Induced Spin Polarization**, also called the bulk (collinear) magnetoelectric or collinear Rashba-Edelstein effect, requiring the joint condition of spin-orbit coupling **and** crystallographic chirality.

**The canonical material is elemental trigonal tellurium** (space groups $P3_121$/$P3_221$, chiral, non-centrosymmetric, non-magnetic). Furukawa et al. (2017) observed the effect directly via $^{125}$Te-NMR: a pulsed current along the crystal's $c$-axis (the chiral screw axis) produces a magnetization parallel to the current, detected as a current-polarity-dependent NMR line shift. The effect reverses sign under crystal-handedness reversal — the direct experimental signature of a pseudoscalar coupling. CrNb$_3$S$_6$ and several chiral disilicide crystals show related effects, so this is a small family of materials, not a single curiosity.

**Practical consequence, stated as a falsifiable side-prediction:** ordinary metals (Cu, W — the materials actually used by Nasilowski and Graneau) are centrosymmetric/achiral. CISP is symmetry-forbidden in them, exactly. **Term 3's polarization mechanism should be identically zero, to leading order, in every historical Ampère-anomaly dataset.** If an anomalous mechanical signal is ever found to correlate with material chirality in future replications, that is evidence for this specific mechanism; if found in ordinary achiral wire, it is not Term 3.

**Status: CLOSED, conditionally.** The kinematic prerequisite $A_\parallel\neq0$ is physically achievable. This does not yet establish that CISP's measured observable is SCH's specific $A^\mu$ (Section 4), nor that the mechanism produces a mechanical force (Section 7).

---

## 3. The Cartan Substitution

Torsion in the SCH action is non-propagating — algebraically fixed by the local axial current via

$$T_{\lambda\mu\nu} = \frac{\kappa\alpha}{2}\,\varepsilon_{\lambda\mu\nu\rho}A^\rho, \qquad A^\rho \equiv \bar\psi\gamma^\rho\gamma^5\psi$$

(Appendix P, §P.1.3). Because torsion is auxiliary, the correct procedure is not to treat its stress-energy as an independent force, but to solve its equation of motion and substitute back into the matter action. Doing so converts the contorsion term in the Dirac covariant derivative into a genuine **four-fermion contact interaction**,

$$H_{\rm SCH} \;\sim\; g_{\rm SCH}\int d^3r\; A_\mu(r)\,A^\mu(r)$$

This is the standard Einstein-Cartan-Sciama-Kibble (ECSK) mechanism (Hehl, von der Heyde, Kerlick & Nester, *Rev. Mod. Phys.* 48, 393 (1976) — already in this corpus's reference list), not a novel feature of SCH. The vanilla ECSK coefficient for a single Dirac field is $3/16$; **the SCH-normalized value of $g_{\rm SCH}$ has not been separately re-derived here** and should not be assumed equal to $3/16$ without doing so.

$H_{\rm SCH}$, as derived, is a **pure electron-electron contact interaction** — built entirely from the electron field, with no explicit dependence on ionic/lattice coordinates $R_i$. This fact is structurally important for Section 7.

**Status: structurally closed, coefficient pending.**

---

## 4. The Operator Dictionary (AA-4)

### 4.1 An exact identity for the spatial components

In the standard Dirac representation, $\gamma^5=\begin{pmatrix}0&I\\I&0\end{pmatrix}$, $\gamma^i=\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$. Direct computation gives

$$\gamma^i\gamma^5 = \begin{pmatrix}\sigma^i & 0\\0&\sigma^i\end{pmatrix} \quad\Longrightarrow\quad \bar\psi\gamma^i\gamma^5\psi = \psi^\dagger\Sigma^i\psi$$

where $\Sigma^i={\rm diag}(\sigma^i,\sigma^i)$ is the standard 4-component Dirac spin operator. **This is an exact operator identity, not a nonrelativistic approximation** — it holds regardless of the state $\psi$ is in. The temporal component, $\bar\psi\gamma^0\gamma^5\psi=\psi^\dagger\gamma^5\psi$, mixes upper and lower spinor components and is therefore suppressed for any state dominated by the large (upper) component — consistent with, though logically independent of, CT-viii's cosmological finding that only $A^0$ survives in the opposite (homogeneous background) regime.

Conduction electrons in Te are nonrelativistic to high precision ($v/c\sim10^{-2}$ or smaller), so lower-component admixture is suppressed by $(v/c)^2\lesssim10^{-4}$. Consequently:

$$A^z_{\rm SCH} \;\approx\; \langle\psi^\dagger\Sigma^z\psi\rangle \quad\text{(exact operator; no free normalization constant for the spatial components)}$$

**This resolves the normalization concern raised by analogy with Paper A §2.3's unfixed $\eta_{\max}$.** That gap is real for $\eta=\bar\psi\psi$ generally, but does not propagate to the spatial axial current in the nonrelativistic regime.

**Status: substantially resolved for the spatial components.** The many-body extension — how a single-particle operator identity extends to an ensemble expectation value in a driven, disordered many-body Fermi liquid, and the precise spin/orbital decomposition of the measured signal (§5) — remains a refinable rather than closed item.

---

## 5. Experimental Anchoring

### 5.1 Source data (both independently verified by direct retrieval)

**Furukawa, Shimokawa, Kobayashi & Itou, *Nat. Commun.* 8, 954 (2017).** $^{125}$Te-NMR measurement of the current-induced shift of line H, right-handed $P3_121$ tellurium single crystal, $T=100$ K. Proportionality coefficient: $8.4(\pm0.4)\times10^{-4}\ {\rm mT\,A^{-1}cm^2}$, measured up to a maximum applied current density of $82\ {\rm A\,cm^{-2}}$. Carrier (hole) density for this sample: $5\times10^{15}\ {\rm cm^{-3}}$ (Hall measurement). *(Confirmed directly from the primary source; both the coefficient and the current density match exactly.)*

**Barts, Tenzin & Sławińska, *Nat. Commun.* 16, 4056 (2025).** Exact Boltzmann-transport (relaxon) calculation, reproducing the 2017 NMR result: at $j_z=82\ {\rm A\,cm^{-2}}$,

$$M_z = 1.3\times10^{-8}\,\mu_B \text{ per Te atom}$$

with a reported charge-to-spin conversion efficiency of 50% (defined as $(N_\uparrow-N_\downarrow)/(N_\uparrow+N_\downarrow)$ for the driven population imbalance $\delta f_k$, not as "50% of all carriers polarized" — this distinction matters for §5.3 below). The transport mechanism is explicitly semiclassical Boltzmann, relaxation-balanced ("relaxon" collective modes with finite lifetime) — a genuinely driven, dissipative steady state, not an adiabatic/equilibrium one. *(Confirmed directly; this framing is load-bearing for Section 7.)*

**Important stated caveat, from the source itself:** $M_z$ "already incorporates the $g$-factors (2 for spin, 1 for orbital)," and with those included, spin and orbital contributions are reported as "nearly equal throughout the considered chemical potential range." The paper also states the theory–experiment agreement, while good, has "an important open question" remaining, with wavepacket self-rotation and itinerant-orbital corrections explicitly identified as not yet included.

### 5.2 A citation that did **not** check out and was excluded

A separate claimed source — "Einstein–Cartan fermion condensates trapped in double walls induce axial torsion coupling bounds," *Eur. Phys. J. C* (2026) — could not be located under direct, specific search despite the same search successfully surfacing multiple genuinely real, closely related 2024–2025 papers on adjacent topics. It is not used anywhere in this document and should not enter the corpus. **This is logged explicitly as a discipline note**, not merely a correction: an earlier audit pass also invoked an unfounded order-of-magnitude benchmark before this one; both are recorded here so the pattern of catching them is visible, not just their outcomes.

### 5.3 Extraction of $A^z_{\rm SCH}$

Te's hexagonal unit cell ($a=4.52$ Å, $c=5.81$ Å, 3 atoms/cell) gives an atomic number density

$$n_{\rm Te} = \frac{3}{(\sqrt3/2)\,a^2 c} \approx 2.9\times10^{22}\ {\rm cm^{-3}}$$

Converting the per-atom moment to a magnetization density:

$$M_z^{\rm total} = (1.3\times10^{-8}\,\mu_B)\times n_{\rm Te} \approx 3.8\times10^{14}\ \mu_B\,{\rm cm^{-3}}$$

Taking the spin share as half the total (§5.1's stated near-equality with orbital), and dividing out $g_s=2$:

$$\langle S_z\rangle_{\rm density} \approx \frac{M_z^{\rm total}/2}{g_s\,\mu_B} \approx 1\times10^{14}\ {\rm cm^{-3}}$$

Using the exact identity $A^z=\psi^\dagger\Sigma^z\psi = 2\langle S_z\rangle$ (Section 4):

$$\boxed{A^z_{\rm SCH} \approx 1.9\times10^{14}\ {\rm cm^{-3}} \approx 1.5\times10^{-27}\ {\rm GeV^3}}$$

**This supersedes an earlier reconnaissance-stage benchmark** that used a crude $n\varepsilon$ estimate with bulk metallic carrier density ($n\sim10^{22}\ {\rm cm^{-3}}$ at near-full polarization) as a stand-in for the true CISP source term. The properly extracted value is smaller by approximately **42 orders of magnitude**. That earlier number should not be treated as having ever been a serious estimate of $A^z_{\rm SCH}$; it is retained in working notes only as a record of the correction, not as a benchmark to build on.

**Status: experimentally anchored**, not fully closed — refinable in the spin/orbital split and the single-particle-to-ensemble mapping, per §4's status note.

---

## 6. The Torsion-Bound Kill Test

### 6.1 Matching to the Kostelecký–Russell–Tasson (2008) bound

Kostelecký, Russell & Tasson, *Phys. Rev. Lett.* 100, 111102 (2008) (verified directly: real, and its headline numbers check out exactly) constrain 19 of 24 independent torsion components using Lorentz-violation/fermion-coupling precision tests, decomposing torsion as

$$T_{\alpha\mu\nu} = \tfrac13(g_{\alpha\mu}T_\nu-g_{\alpha\nu}T_\mu) - \epsilon_{\mu\nu\alpha\beta}A^\beta_{\rm KRT} + M_{\alpha\mu\nu}$$

SCH's Cartan equation produces torsion of **purely** this axial ($A_{\rm KRT}$) type — no trace piece, no mixed piece — placing it entirely in KRT's most tightly bounded sector. Matching coefficients (relabeling SCH's $\alpha\to\Lambda$ to avoid index collision, and verified by explicit index permutation — a cyclic three-index relabeling is even, no sign flip):

$$A^\beta_{\rm KRT} = -\frac{\kappa\Lambda}{2}\,A^\beta_{\rm SCH}$$

KRT further state that "the special case of minimal coupling is recovered for $\xi_4^{(4)}=3/4$, with other couplings zero" — and SCH's covariant derivative, $D_\mu\psi=\partial_\mu\psi+\tfrac14\omega_\mu^{ab}\gamma_{ab}\psi$ with $\omega=\mathring\omega+K$, is exactly this minimal-coupling case (torsion enters only through the standard spin connection). Their reported bound, already reduced to this case, gives (tightest direction) $|A_{\rm KRT}|\lesssim2\times10^{-31}$ GeV.

### 6.2 The bound on $\alpha$

$$\kappa = 8\pi G/c^4 = 8\pi/M_{\rm Pl}^2 \approx 1.7\times10^{-37}\ {\rm GeV^{-2}}$$

$$\alpha\,|A^z_{\rm SCH}| \;\lesssim\; \frac{2\times(2\times10^{-31}\ {\rm GeV})}{1.7\times10^{-37}\ {\rm GeV^{-2}}} \approx 2\times10^{6}\ {\rm GeV^3}$$

Using the experimentally anchored value from §5.3:

$$\boxed{\alpha \;\lesssim\; \frac{2\times10^{6}\ {\rm GeV^3}}{1.5\times10^{-27}\ {\rm GeV^3}} \approx 1\times10^{33}}$$

**Result: no constraint of any practical value.** Replacing the earlier crude benchmark with the real, measured CISP amplitude *loosens* the bound by roughly eight further orders of magnitude, because the real axial-current source available in any terrestrial chiral conductor is dramatically smaller than bulk-density intuition suggests. Combined with $\kappa$'s intrinsic gravitational suppression, this particular kill-test route is exhausted: **the best existing laboratory torsion bound cannot distinguish SCH's allowed $\alpha$ range from an unconstrained one, at any current density achievable with known CISP materials.**

**Status: route closed (negative).** This is a genuine result, not an inconclusive one — it rules out this specific falsification path without ruling out the theory.

---

## 7. The Mechanical-Force Problem (Open, and Why)

### 7.1 Why $H_{\rm SCH}$ is not amenable to the obvious force formula

$H_{\rm SCH}$ (Section 3) is a pure electron-electron contact interaction with **no explicit dependence on ionic coordinates**. This rules out the naive Todorov/Dundas current-induced-force formalism (Todorov 2010; Dundas, McEniry & Todorov, *Nat. Nanotechnol.* 2009) as the direct tool: that formalism computes $F_i=-\langle\partial H/\partial R_i\rangle$, which is identically zero for a Hamiltonian with no $R_i$-dependence at this order. $H_{\rm SCH}$ instead structurally resembles an exchange-correlation-type term — depending on lattice geometry only *implicitly*, through the electronic state — which is the regime the equilibrium quantum-mechanical **stress theorem** (Nielsen & Martin, *Phys. Rev. B* 32, 3780 (1985)) is built for.

### 7.2 Why the equilibrium tool doesn't transfer either

The equilibrium stress theorem gets to differentiate only the explicit strain-dependence of the energy and ignore the wavefunction's own response, *because* the ground state sits at a variational extremum. CISP's steady state — confirmed directly from the source (§5.1) to be a Boltzmann relaxation-time construction, a driven population imbalance sustained against continuous scattering, not an adiabatic minimum — has no such extremal principle protecting it. The response of the driven density matrix to strain is not guaranteed to be negligible, and there is no general reason to expect it is.

### 7.3 The naive nonequilibrium formula is explicitly flagged as unjustified

Checking the specialist nonequilibrium-thermodynamics literature directly: work on the variational grand-potential formulation of driven tunneling transport distinguishes a rigorously conservative **thermodynamic force**, derived from a properly constructed variational steady-state ensemble $\hat\rho_{LS}$ via its own generalized Hellmann-Feynman theorem, from the naive **electrostatic force** $F_i=-\langle\partial H/\partial R_i\rangle_{\rm NEQ}$ — and states explicitly that "there is no rigorous argument for the general use of electrostatic forces... in infinite, open nonequilibrium tunneling systems," only in linear response. The Ampère anomaly's own motivating physics (Paper B §6.4, the pre-thermal ballistic window) is specifically about being driven far from that regime.

The rigorous alternative ($\hat\rho_{LS}$) requires establishing that CISP's actual Boltzmann-relaxation steady state falls into the class of states for which the generalized theorem is proven. **This mapping has not been established, either way.**

### 7.4 Explicit non-claim

No mechanical force sign, magnitude, or scaling is asserted in this document. An earlier reconnaissance-stage estimate of the mechanical effect, built on the now-superseded bulk-density benchmark (§5.3), is not reproduced here with a corrected number: doing so before resolving §7.1–7.3 would attach a numerically precise-looking figure to an unresolved physical object, which is the specific error this audit was structured to avoid.

**Status: OPEN — load-bearing gap.**

---

## 8. Choke-Point Classification

The audit chain has four links. They do not carry equal evidentiary weight, and conflating them would be a methodological error — treating a field-wide open problem as if it were a defect specific to SCH.

| Link | Current status | What a failure there would mean |
|---|---|---|
| **CISP $\to A^\mu$** | Experimentally anchored; many-body mapping still being refined | **SCH-specific failure** if the measured CISP observable cannot be consistently mapped to the axial bilinear |
| **Cartan $\to H_{\rm SCH}$** | Structurally supported; coefficient ($g_{\rm SCH}$) pending | **SCH-specific failure** if the explicit ECSK-type substitution contradicts the claimed interaction form |
| **$H_{\rm SCH} \to$ mechanical force** | Open | **Not presently diagnostic of SCH** — inherits an unresolved problem in nonequilibrium statistical mechanics that would exist for ordinary current-induced forces regardless of SCH |
| **Mechanical force $\to$ Ampère anomaly** | Not yet calculable | Future empirical discriminator, once the preceding link is resolved |

This classification is provisional at the third link specifically: if a rigorous nonequilibrium force/stress theorem is established (by this project or by the host field) and is shown to apply to CISP's specific driven state, a null or wrong-sign result **becomes SCH-specific at that point** and this table must be revised accordingly. The "not presently diagnostic" classification is not a permanent exemption.

---

## 9. Falsification Conditions

**FC-T3-1 — Chirality dependence.** *[Testable now, in principle, against future replication of Nasilowski/Graneau-type experiments.]* If an anomalous longitudinal mechanical signal, of the kind reported by Nasilowski or Graneau, is observed in ordinary achiral conductors (Cu, Al, W) at a magnitude inconsistent with Term 2 alone, and is *not* found to correlate with crystallographic chirality when the same protocol is applied to a chiral/achiral material pair at matched current density, this is evidence against the Term-3/CISP mechanism specifically (though not against Term 2 or SCH generally).

**FC-T3-2 — Torsion-bound revision.** If a future laboratory torsion-Lorentz-violation bound improves on KRT (2008) by more than approximately eight orders of magnitude in the relevant sector *and* a materials system with substantially larger measured CISP amplitude than Te is identified, §6's conclusion should be re-evaluated — the current margin is large but not fundamentally unbridgeable by advances on both fronts simultaneously.

**FC-T3-3 — Mechanical force resolution.** Once a rigorous, verified nonequilibrium force formalism applicable to CISP's driven steady state exists: if it returns zero, the wrong sign, or a force with the wrong spatial symmetry (transverse rather than longitudinal) for the SCH-derived $H_{\rm SCH}$, **Term 3 is dead** without requiring the Bi-209 calibration. If it returns a longitudinal force of the correct sign, the branch proceeds to magnitude estimation using the anchored $A^z_{\rm SCH}$ of §5.3 and the (still-pending) $g_{\rm SCH}$ coefficient of §3.

---

## 10. Summary Table

| Item | Status | Basis |
|---|---|---|
| Kinematic obstruction (axial polarization exists) | **CLOSED, conditionally** | CISP in chiral, SOC-coupled (Sohncke-group) conductors; Te directly measured |
| Operator dictionary, spatial components | **Substantially resolved** | Exact Dirac identity $\bar\psi\gamma^i\gamma^5\psi=\psi^\dagger\Sigma^i\psi$; no free normalization constant |
| Cartan substitution to contact interaction | **Structurally closed; coefficient pending** | Standard ECSK mechanism; SCH-normalized $g_{\rm SCH}$ not yet separately derived |
| Numerical anchoring of $A^z_{\rm SCH}$ | **Experimentally anchored** | Furukawa et al. 2017 + Barts et al. 2025, verified directly; supersedes a benchmark later found to be off by ~42 orders of magnitude |
| Torsion-bound constraint on $\alpha$ | **Route closed (negative)** | KRT (2008), verified directly; $\alpha\lesssim10^{33}$ — no practical constraint |
| $H_{\rm SCH}\to$ mechanical force | **OPEN — load-bearing** | No applicable rigorous force formalism identified; classified as inherited, not SCH-specific |

**Net methodological result of this pass:** two SCH-internal choke points (operator dictionary, Cartan substitution) have been exposed to genuine falsification and have, so far, survived; one falsification route (laboratory torsion bounds) has been tested and closed without killing the theory; one link (mechanical force) has been correctly identified as an inherited open problem in nonequilibrium statistical mechanics rather than misclassified as a defect of SCH specifically. This is a materially stronger outcome than "Term 3 remains inconclusive," and was reached without the Bi-209 calibration.

---

## References

Barts, E., Tenzin, K. & Sławińska, J. Efficient spin accumulation carried by slow relaxons in chiral tellurium. *Nat. Commun.* **16**, 4056 (2025).

Dundas, D., McEniry, E. J. & Todorov, T. N. Current-driven atomic waterwheels. *Nat. Nanotechnol.* **4**, 99–102 (2009).

Furukawa, T., Shimokawa, Y., Kobayashi, K. & Itou, T. Observation of current-induced bulk magnetization in elemental tellurium. *Nat. Commun.* **8**, 954 (2017).

Furukawa, T., Watanabe, Y., Ogasawara, N., Kobayashi, K. & Itou, T. Current-induced magnetization caused by crystal chirality in nonmagnetic elemental tellurium. *Phys. Rev. Res.* **3**, 023111 (2021).

Hehl, F. W., von der Heyde, P., Kerlick, G. D. & Nester, J. M. General relativity with spin and torsion: Foundations and prospects. *Rev. Mod. Phys.* **48**, 393 (1976).

Kostelecký, V. A., Russell, N. & Tasson, J. D. Constraints on torsion from bounds on Lorentz violation. *Phys. Rev. Lett.* **100**, 111102 (2008).

Nielsen, H. B. & Martin, R. M. Quantum-mechanical theory of stress and force. *Phys. Rev. B* **32**, 3780 (1985).

Todorov, T. N. Time-dependent scattering approach to current-induced forces. *J. Phys.: Condens. Matter* (2010) [and associated current-induced-force / electronic-friction formalism].

*[Nonequilibrium thermodynamics of driven tunneling transport — variational grand potential and the electrostatic-vs-thermodynamic force distinction; source verified during this audit, full citation to be confirmed before this document is integrated into the canonical corpus.]*

Nasilowski, J. Undulatory corrugation of a thin copper wire exploded in air. In *Exploding Wires*, Vol. 3 (Plenum Press, 1964).

Graneau, P. Ampere-Neumann electrodynamics of metallic conductors. *Eur. J. Phys.* **3**, 235 (1982); First indication of Ampere tension in solid electric conductors. *Phys. Lett. A* **97**, 253 (1983); *Fortschritte der Physik* **35**, 787 (1987).

---

## Appendix: Corrections Made During This Audit

Recorded per this corpus's standing documentation convention (cf. Paper B, Paper C revision histories) — corrections are logged, not silently absorbed.

1. An initial reconnaissance-stage benchmark for $A^z_{\rm SCH}$, using bulk metallic carrier density at near-full polarization, was superseded by the experimentally anchored value of §5.3 — smaller by approximately 42 orders of magnitude. The original benchmark should not be cited as a prior estimate of this quantity.
2. A claimed EPJC 2026 source ("Einstein–Cartan fermion condensates trapped in double walls...") could not be verified under direct, specific search and is excluded from this document and from the corpus (§5.2).
3. An initial attempt to apply the electromagnetic constant-current co-energy sign rule ($F=+\partial U/\partial\ell$) to the SCH contact interaction was withdrawn after establishing that CISP's steady state is a driven, dissipative, relaxation-balanced construction rather than a reactive/adiabatic one, to which that rule does not obviously apply (§7.2).
4. An initial application of the Todorov/Dundas current-induced-force formalism was reconsidered after noting that $H_{\rm SCH}$ has no explicit ionic-coordinate dependence, making that formalism structurally inapplicable at leading order (§7.1).

---

*Working document | August 2026*
*Produced by: Variable Systems*
*Verification status: Primary sources (Furukawa 2017, Barts et al. 2025, Kostelecký-Russell-Tasson 2008) independently retrieved and confirmed. Secondary formalism claims (Todorov/Dundas, Nielsen-Martin, the variational nonequilibrium grand-potential source) drawn from search-verified but not independently re-derived literature. Not for citation without author approval.*
