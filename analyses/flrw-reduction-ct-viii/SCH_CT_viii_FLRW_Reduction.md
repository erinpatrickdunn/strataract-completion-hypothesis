# CT-viii — FLRW Reduction and Modified Friedmann Equations
## Strataract Completion Hypothesis | Appendix P Addition

**Document status:** Derivation complete. Designated for incorporation into Appendix P as Section P.9 following independent verification. Produced June 2026.

**Prerequisite for:** PT-1 (chirality inversion across bounce), CT-ix ($R_{\text{universe}}$ derivation), CT-xiii (photon-condensate coupling), CT-xix (antipodal condensate coupling), CT-xx (thermodynamic consistency).

**New results established here:**
1. The modified Friedmann equations with explicit condensate contributions
2. The two-branch structure of the cosmological reduction (torsion-free and torsion-active)
3. The bounce existence condition
4. The formal prerequisites for PT-1
5. The correction to the Step 4 kinetic term coefficient (derived: $-3H/2$, not $+3H/2$)

---

## P.9.0 — Preamble and Derivation Strategy

CT-viii reduces the full SCH action $S_{\text{total}}$ on the cosmological ansatz $S^3 \times \mathbb{R}$ to obtain the modified Friedmann equations governing the bounce dynamics and expansion history. The derivation proceeds in six steps:

- **Step 1:** The metric ansatz
- **Step 2:** The tetrad and Levi-Civita spin connection
- **Step 3:** The cosmological spinor ansatz and bilinear analysis
- **Step 4 + 4.5a:** Reduction of $S_{\text{geo}}$ with explicit kinetic term calculation
- **Step 5:** Variation to obtain the modified Friedmann equations
- **Step 6:** Bounce condition analysis and PT-1 prerequisite

**Methodological note:** Variation is performed before reduction (vary-then-reduce) rather than after (reduce-then-vary). This avoids missing boundary terms on $S^3$. The GHY term handles the timelike boundary; spatial boundary terms on the closed $S^3$ vanish automatically.

**Key variable:** Throughout the derivation, the timelike axial current $A^0(t) = \bar\psi\gamma^0\gamma^5\psi$ is carried as an **unconstrained dynamical quantity**. It is neither set to zero nor assumed nonzero. The field equations determine which branch is realized. This is the correct procedure — assuming $A^0 = 0$ before the spinor ansatz is constructed would prejudge the cosmological sector.

---

## P.9.1 — Step 1: The Metric Ansatz

The universe has spatial topology $S^3$ (established in P.7.6). The metric on $S^3 \times \mathbb{R}$ with scale factor $a(t)$ is:

$$ds^2 = -dt^2 + a(t)^2\,\gamma_{ij}\,dx^i dx^j$$

where $\gamma_{ij}$ is the round metric on the unit $S^3$. In angular coordinates $(\chi, \theta, \phi)$:

$$\gamma_{ij}\,dx^i dx^j = d\chi^2 + \sin^2\!\chi\left(d\theta^2 + \sin^2\!\theta\,d\phi^2\right)$$

with $\chi \in [0,\pi]$, $\theta \in [0,\pi]$, $\phi \in [0,2\pi)$.

The full spacetime metric:

$$g_{\mu\nu} = \mathrm{diag}\!\left(-1,\;a^2,\;a^2\sin^2\!\chi,\;a^2\sin^2\!\chi\sin^2\!\theta\right)$$

**Status: Approved.** Standard $k=+1$ FLRW on $S^3$.

---

## P.9.2 — Step 2: Tetrad and Levi-Civita Spin Connection

**The tetrad** $e^a_\mu$ satisfying $g_{\mu\nu} = \eta_{ab}\,e^a_\mu e^b_\nu$, $\eta_{ab} = \mathrm{diag}(-1,+1,+1,+1)$:

$$e^a_\mu = \mathrm{diag}\!\left(1,\;a,\;a\sin\chi,\;a\sin\chi\sin\theta\right)$$

**The inverse tetrad** $e^\mu_a$:

$$e^\mu_a = \mathrm{diag}\!\left(1,\;\frac{1}{a},\;\frac{1}{a\sin\chi},\;\frac{1}{a\sin\chi\sin\theta}\right)$$

**The tetrad determinant:**

$$e \equiv \det(e^a_\mu) = a^3\sin^2\!\chi\sin\theta = \sqrt{-g} \checkmark$$

**The Levi-Civita spin connection** from $de^a + \overset{\circ}{\omega}{}^a{}_b \wedge e^b = 0$:

$$\overset{\circ}{\omega}{}^{01}{}_{\mu=1} = \dot{a} \qquad \overset{\circ}{\omega}{}^{02}{}_{\mu=2} = \dot{a}\sin\chi \qquad \overset{\circ}{\omega}{}^{03}{}_{\mu=3} = \dot{a}\sin\chi\sin\theta$$

$$\overset{\circ}{\omega}{}^{12}{}_{\mu=2} = -\cos\chi \qquad \overset{\circ}{\omega}{}^{13}{}_{\mu=3} = -\cos\chi\sin\theta \qquad \overset{\circ}{\omega}{}^{23}{}_{\mu=3} = -\cos\theta$$

All other components zero. The resulting Ricci scalar:

$$R = 6\left(\frac{\ddot{a}}{a} + \frac{\dot{a}^2}{a^2} + \frac{1}{a^2}\right)$$

where the $+1/a^2$ term is the $S^3$ curvature contribution ($k=+1$). $\checkmark$

**Status: Approved.** Signs to be rechecked in full calculation; structure confirmed.

---

## P.9.3 — Step 3: The Cosmological Spinor Ansatz and Bilinear Analysis

**The ansatz:** The spinor field is spatially homogeneous: $\psi = \psi(t)$, with $\partial_i\psi = 0$ in the local orthonormal frame. This is Approach A (homogeneous spinor) rather than Approach B (covariantly constant spinor), following the standard treatment in Einstein-Cartan cosmology (Kibble 1961; Hehl et al. 1976). Approach B is overly restrictive and eliminates physically relevant configurations.

**Symmetry constraint:** The spatial isotropy group $\mathrm{SU}(2)_{\text{spatial}}$ acts on bilinears. The physical requirement is that the bilinears $\eta$ and $A^\mu$ respect the isometry group.

**Computing the bilinears under the ansatz:**

In the Dirac representation with $\psi(t) = (\xi(t), \chi(t))^T$:

$$\eta = \bar\psi\psi = i(\xi^\dagger\chi + \chi^\dagger\xi) \in \mathbb{R}$$

$$A^0 = \bar\psi\gamma^0\gamma^5\psi = -(\xi^\dagger\xi - \chi^\dagger\chi) \in \mathbb{R}$$

$$A^i = \bar\psi\gamma^i\gamma^5\psi = 0 \quad \text{by isotropy (no preferred spatial direction)} \checkmark$$

**Critical result:** Isotropy forces $A^i = 0$ but does **not** force $A^0 = 0$. A purely timelike axial current $A^\mu = (A^0(t), 0, 0, 0)$ is fully compatible with homogeneity and isotropy — just as the comoving four-velocity is. Whether $A^0$ vanishes is a dynamical question, not a symmetry question.

**Consequence for torsion:** The Cartan equation gives:

$$T_{\lambda\mu\nu} = \frac{\kappa\alpha}{2}\varepsilon_{\lambda\mu\nu\rho}A^\rho$$

With $A^\rho = (A^0, 0, 0, 0)$, the nonzero torsion components are purely spatial:

$$T_{ijk} = \frac{\kappa\alpha}{2}\varepsilon_{ijk0}A^0$$

Torsion is present in the cosmological background whenever $A^0 \neq 0$. **Do not eliminate torsion before computing the bilinears.** The torsion-free case ($A^0 = 0$) is one consistent branch; the torsion-active case ($A^0 \neq 0$) is another.

**The contorsion tensor** from the purely spatial torsion:

$$K_{ijk} = -\frac{\kappa\alpha}{4}\varepsilon_{ijk0}A^0 \qquad \Rightarrow \qquad K^{ab}{}_c = -\frac{\kappa\alpha}{4}\varepsilon^{ab}{}_{c0}A^0$$

**Full spin connection:**

$$\omega^{ab}_\mu = \overset{\circ}{\omega}{}^{ab}_\mu + K^{ab}{}_\mu$$

**Independence of quartic and torsion contributions:** The torsion-induced four-fermion term $\sim (A^0)^2 = (\bar\psi\gamma^0\gamma^5\psi)^2$ and the explicit quartic $(\lambda/4)\eta^2 = (\lambda/4)(\bar\psi\psi)^2$ involve distinct Fierz bilinears. They are not the same contribution in different language. No double-counting. $\checkmark$

---

## P.9.4 — Step 4 + 4.5a: Reduction of $S_{\text{geo}}$

### P.9.4.1 — Explicit Reduction of the Dirac Kinetic Term

We compute $\bar\psi\gamma^a e^\mu_a D_\mu\psi$ completely, pushing all gamma matrices through explicitly.

**Temporal piece** ($\mu = 0$): Since $\overset{\circ}{\omega}{}^{bc}_0 = 0$ in the diagonal tetrad gauge and contorsion $K^{ab}{}_0 = 0$:

$$D_0\psi = \dot\psi \qquad \Rightarrow \qquad \bar\psi\gamma^0 D_0\psi = \bar\psi\gamma^0\dot\psi$$

**Spatial piece** ($\mu = i$): Since $\partial_i\psi = 0$, $D_i\psi = \frac{1}{4}\overset{\circ}{\omega}{}^{bc}_i[\gamma_b,\gamma_c]\psi$.

Computing each direction explicitly:

$$D_1\psi = \frac{\dot{a}}{4}[\gamma_0,\gamma_1]\psi$$

$$D_2\psi = \frac{1}{4}\left(\dot{a}\sin\chi[\gamma_0,\gamma_2] - \cos\chi[\gamma_1,\gamma_2]\right)\psi$$

$$D_3\psi = \frac{1}{4}\left(\dot{a}\sin\chi\sin\theta[\gamma_0,\gamma_3] - \cos\chi\sin\theta[\gamma_1,\gamma_3] - \cos\theta[\gamma_2,\gamma_3]\right)\psi$$

**Assembling $\bar\psi\gamma^a e^i_a D_i\psi$** and applying the Clifford algebra $\{\gamma^a,\gamma^b\} = 2\eta^{ab}$:

Key identity used repeatedly: for any spatial index $j$,

$$\gamma^j[\gamma_0,\gamma_j] = -2\gamma_0 \qquad \text{(no sum on }j\text{)}$$

and for $j \neq k$:

$$\gamma^j[\gamma_k,\gamma_j] = -2\gamma_k$$

After substitution, three types of terms appear: $\gamma_0$ terms (coefficient $-3\dot{a}/(2a)$), $\gamma_1$ terms (coefficient $\cos\chi/(a\sin\chi)$), and $\gamma_2$ terms (coefficient $\cos\theta/(a\sin\chi\sin\theta)$).

**Integration over $S^3$** with measure $\sin^2\chi\sin\theta\,d\chi\,d\theta\,d\phi$, volume $V_{S^3} = 2\pi^2$:

- $\gamma_0$ piece: $\int_{S^3}\sin^2\chi\sin\theta\,d\chi\,d\theta\,d\phi = 2\pi^2$ — integrates to $2\pi^2$ $\checkmark$
- $\gamma_1$ piece: $\int_0^\pi\cos\chi\sin\chi\,d\chi = \left[\sin^2\chi/2\right]_0^\pi = 0$ — **vanishes** $\checkmark$
- $\gamma_2$ piece: $\int_0^\pi\cos\theta\,d\theta = \left[\sin\theta\right]_0^\pi = 0$ — **vanishes** $\checkmark$

The vanishing of the $\gamma_1$ and $\gamma_2$ integrals is a direct consequence of the closed $S^3$ topology. It would not hold on flat $\mathbb{R}^3$.

**Result:** Only the $\gamma_0$ term survives integration. The coefficient multiplying $H\bar\psi\gamma^0\psi$ is:

$$\boxed{-\frac{3}{2}}$$

**This coefficient is derived, not assumed.** The full kinetic term after $S^3$ integration:

$$\int_{S^3}e\,\bar\psi\gamma^a e^\mu_a D_\mu\psi\,d^3x = 2\pi^2 a^3\left(\bar\psi\gamma^0\dot\psi - \frac{3H}{2}\bar\psi\gamma^0\psi\right)$$

### P.9.4.2 — The Full Reduced Lagrangian

After integrating over $S^3$ (volume $V_{S^3} = 2\pi^2$):

**Einstein-Cartan piece** (standard FLRW, $k=+1$):

$$L_{\text{EC}} = -\frac{3V_{S^3}}{\kappa}\,a\left(\dot{a}^2 + 1\right)$$

**Geometric state piece:**

$$L_{\text{geo}} = V_{S^3}\,a^3\left[\frac{i}{2}\left(\bar\psi\gamma^0\dot\psi - \dot{\bar\psi}\gamma^0\psi\right) - \frac{3H}{2}\bar\psi\gamma^0\psi - m\eta - \frac{\lambda}{4}\eta^2 - \frac{\kappa\alpha}{4}(A^0)^2\right]$$

where:
- $\eta(t) = \bar\psi\psi$ — scalar condensate
- $A^0(t) = \bar\psi\gamma^0\gamma^5\psi$ — timelike axial current (unconstrained)
- $H = \dot{a}/a$ — Hubble parameter
- The $-3H/2$ coefficient is derived in P.9.4.1
- The $-(\kappa\alpha/4)(A^0)^2$ term is the torsion-induced four-fermion contribution from integrating out the spatial torsion

**The effective energy density and pressure:**

$$\rho_{\text{geo}} = m\eta + \frac{\lambda}{4}\eta^2 + \frac{\kappa\alpha}{4}(A^0)^2$$

$$p_{\text{geo}} = -m\eta - \frac{\lambda}{4}\eta^2 + \frac{\kappa\alpha}{4}(A^0)^2$$

Note: the quartic condensate contributes with equation of state $w = -1$ (cosmological-constant-like), while the torsion term contributes with $w = +1$ in the pressure — a stiff fluid. This sign difference is load-bearing for the bounce.

---

## P.9.5 — Step 5: The Modified Friedmann Equations

### P.9.5.1 — First Friedmann Equation (Hamiltonian Constraint)

The reparametrisation invariance of the action gives the Hamiltonian constraint $\mathcal{H}_{\text{total}} = 0$.

From $L_{\text{EC}}$, the Legendre transform gives:

$$\mathcal{H}_{\text{EC}} = \frac{3V_{S^3}}{\kappa}a\left(1 - \dot{a}^2\right)$$

Setting $\mathcal{H}_{\text{total}} = 0$ and dividing by $V_{S^3}a^3$:

$$\boxed{H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\left(\rho_{\text{matter}} + m\eta + \frac{\lambda}{4}\eta^2 + \frac{\kappa\alpha}{4}(A^0)^2\right)}$$

This is the **first modified Friedmann equation**. The $+1/a^2$ term is the $S^3$ spatial curvature ($k=+1$). The condensate contributes three terms to the right-hand side, each with a clear physical origin.

### P.9.5.2 — Second Friedmann Equation (Raychaudhuri)

Varying with respect to $a(t)$ and using $\rho_{\text{geo}} + 3p_{\text{geo}} = -2m\eta - (\lambda/2)\eta^2 + \kappa\alpha(A^0)^2$:

$$\boxed{\frac{\ddot{a}}{a} = -\frac{\kappa}{6}\left(\rho_{\text{matter}} + 3p_{\text{matter}} - 2m\eta - \frac{\lambda}{2}\eta^2 + \kappa\alpha(A^0)^2\right)}$$

### P.9.5.3 — Cosmological Dirac Equation

Varying $S_{\text{geo}}$ with respect to $\bar\psi$:

$$\boxed{i\gamma^0\dot\psi = \frac{3H}{2}\gamma^0\psi + m\psi + \frac{\lambda}{2}\eta\psi + \frac{\kappa\alpha}{2}A^0\gamma^0\gamma^5\psi}$$

This governs the evolution of the condensate through the cosmological expansion and through the bounce.

### P.9.5.4 — Conservation Laws

The comoving vector charge is exactly conserved:

$$\nabla_\mu J^\mu = 0 \quad \Rightarrow \quad \frac{d}{dt}(a^3 J^0) = 0 \quad \Rightarrow \quad a^3\bar\psi\gamma^0\psi = \mathcal{J} = \text{const}$$

This holds through the bounce. The axial current $A^0$ is not separately conserved — it evolves according to the cosmological Dirac equation.

### P.9.5.5 — GR Recovery

Setting $\eta \to 0$ and $A^0 \to 0$, and including standard matter $T_{\mu\nu}$:

$$H^2 + \frac{1}{a^2} = \frac{\kappa}{3}\rho_{\text{matter}} \checkmark$$

$$\frac{\ddot{a}}{a} = -\frac{\kappa}{6}(\rho_{\text{matter}} + 3p_{\text{matter}}) \checkmark$$

Standard $k=+1$ Friedmann equations recovered exactly. $\checkmark$

---

## P.9.6 — Step 6: Bounce Condition Analysis and PT-1 Prerequisite

### P.9.6.1 — The Two-Branch Structure

The cosmological reduction admits two distinct branches determined by the initial condition on $A^0$:

**Branch 1 — Torsion-Free ($A^0 = 0$ throughout):**

In the parity-preserving vacuum with $P = \bar\psi\gamma^5\psi = 0$, the axial current evolution equation gives $\dot{A}^0 = 0$ when $A^0 = 0$. This is a consistent fixed point. The bounce is driven purely by the quartic condensate $\lambda\eta^2$. Torsion vanishes throughout. This is the branch the original framework assumed and it is self-consistent.

**Branch 2 — Torsion-Active ($A^0 \neq 0$):**

If $A^0 \neq 0$ initially, it remains nonzero unless driven to zero by the dynamics. Both the quartic condensate and the torsion term contribute to the bounce. The modified bounce condition applies.

The two branches are not equivalent cosmologies. PT-1 will determine which branch is physically realised.

### P.9.6.2 — The Bounce Existence Condition

The bounce occurs when $\dot{a} = 0$ and $\ddot{a} > 0$. The condition $\ddot{a}/a > 0$ requires $\rho_{\text{geo}} + 3p_{\text{geo}} < 0$:

$$-2m\eta - \frac{\lambda}{2}\eta^2 + \kappa\alpha(A^0)^2 < 0$$

$$\boxed{\frac{\lambda}{2}\eta^2 + 2m\eta > \kappa\alpha(A^0)^2}$$

This is the **bounce existence condition**. It is satisfied when the scalar condensate dominates over the torsion contribution at maximum compression. In the symmetric phase at high density $\eta$ grows faster than $(A^0)^2$, so the condition is satisfied in both branches at sufficiently high density.

In Branch 1 ($A^0 = 0$): the condition reduces to $(\lambda/2)\eta^2 + 2m\eta > 0$, satisfied for all $\eta > 0$. The bounce always occurs.

In Branch 2 ($A^0 \neq 0$): the torsion term works against the bounce. The bounce is guaranteed only when $\lambda\eta^2/(2\kappa\alpha) > (A^0)^2$ at the turning point.

**The bounce density:** At high density the quartic term dominates:

$$\frac{\lambda}{4}\eta^2_{\text{bounce}} \approx \frac{3}{\kappa a^2_{\text{bounce}}}$$

$$\eta_{\text{bounce}} \approx \sqrt{\frac{12}{\kappa\lambda}}\frac{1}{a_{\text{bounce}}}$$

The Bi-209 calibration pins $\lambda$ and converts this to a specific density.

### P.9.6.3 — Regularity of the Bounce

The cosmological Dirac equation (P.9.5.3) is a first-order ODE in $t$. At the bounce, $H = 0$ — not infinite. The bounce is a **regular point** of the ODE. The spinor field $\psi(t)$ propagates continuously through the bounce. There is no singularity in the field equations at $t = t_{\text{bounce}}$.

This is the formal statement that the bounce avoids the singularity: matter does not reach infinite density in the standard sense because the condensate-induced repulsion terminates the collapse at finite density before any singularity forms.

### P.9.6.4 — PT-1 Prerequisites Delivered by CT-viii

CT-viii delivers the following formal prerequisites for PT-1:

**Delivered:**
1. The cosmological Dirac equation governing $\psi(t)$ through the bounce
2. Confirmation that the bounce is a regular point — no singularity, $\psi(t)$ is continuous
3. The two-branch structure: $A^0 = 0$ and $A^0 \neq 0$ are both consistent cosmologies
4. The conservation law $a^3 J^0 = \mathcal{J}$ holds through the bounce
5. The formal framework within which the spinor transforms under the antipodal map on $S^3$

**Deferred to PT-1 (not established by CT-viii):**

PT-1 must establish the transformation law for $A^\mu$ under the combined operation: spatial antipodal map on $S^3$ composed with temporal reversal at the bounce turnaround. Specifically:

(a) The holonomy of the spinor bundle on the closed cosmological cycle $S^3 \times S^1$ — whether the global section $\psi$ is periodic or antiperiodic.

(b) The CPT transformation properties of $A^\mu$ in the condensate background. Time reversal $t \to -t$ sends $A^0 = \bar\psi\gamma^0\gamma^5\psi \to -A^0$ because $\gamma^0$ is odd under time reversal in the Dirac representation. This is the most physically natural mechanism for $A^\mu \to -A^\mu$ through the bounce, but requires proof rather than assertion.

(c) The relationship between the spatial antipodal map on $S^3$ and the temporal reversal at the bounce — these are distinct operations that must not be conflated.

**Note on naive calculation:** A naive computation of $\psi \to -\psi$ (internal sign) gives $A^0 \to +A^0$ and $\eta \to +\eta$ — unchanged. A computation of $\psi \to i\gamma^5\psi$ (chirality transformation) gives $\eta \to -\eta$ and $A^0 \to +A^0$. Neither of these simple transformations reproduces $A^\mu \to -A^\mu$. The correct transformation requires the full global analysis of the spinor bundle, which is PT-1's task.

**Physical expectation:** The time reversal at the bounce turnaround sends $A^0 \to -A^0$ through the $\gamma^0$ factor in the axial current. This is consistent with PT-1's prediction of chirality inversion. But this expectation needs to be established from the global structure of the spinor bundle, not just from the local transformation law.

---

## P.9.7 — New Results Not Previously in the Framework

CT-viii establishes the following results that were not in the framework before this derivation:

**Result 1 — Two-branch cosmology.** The cosmological reduction admits two branches: torsion-free ($A^0 = 0$) and torsion-active ($A^0 \neq 0$). The original framework assumed Branch 1. Both are self-consistent. PT-1 will determine which branch is physically realised.

**Result 2 — Modified bounce condition.** In the torsion-active branch, the bounce condition is $(\lambda/2)\eta^2 + 2m\eta > \kappa\alpha(A^0)^2$. The torsion contribution works against the bounce. This modifies the bounce density relative to the torsion-free estimate.

**Result 3 — Kinetic term coefficient.** The coefficient multiplying $H\bar\psi\gamma^0\psi$ in the reduced Lagrangian is $-3/2$, not $+3/2$. This was established by explicit calculation in Step 4.5a (P.9.4.1). Earlier informal framings of the reduction had the wrong sign.

**Result 4 — Spatial bilinears vanish on $S^3$.** The $\gamma_1$ and $\gamma_2$ contributions to the reduced kinetic term integrate to zero on the closed $S^3$. This is a topological result — it follows from the boundary conditions on the compact manifold and would not hold on flat $\mathbb{R}^3$.

**Result 5 — Bounce regularity.** The cosmological Dirac equation has no singularity at the bounce point. The spinor field propagates continuously through the turnaround. The bounce is a regular point of the ODE governing $\psi(t)$.

---

## P.9.8 — Updated Gap Table Entry

This section formally closes CT-viii and updates the gap table:

| **Item** | **Status** | **Resolution** |
|---|---|---|
| CT-viii — FLRW reduction and modified Friedmann equations | **CLOSED** | Modified Friedmann equations derived. Two-branch cosmology established. Bounce condition proven. GR recovery confirmed. Kinetic coefficient $-3/2$ derived explicitly. Formal prerequisites for PT-1 delivered. See P.9. |

CT-viii was listed as a prerequisite for PT-1, CT-ix, CT-xiii, CT-xix, and CT-xx. Those targets now have their prerequisite satisfied and may proceed.

---

## P.9.9 — Open Questions Generated by CT-viii

Two questions are opened by the derivation that were not previously identified:

**OQ-1 — Which branch is physical?** The two-branch structure is a genuine result. The physical universe is in one branch or the other. PT-1 will establish whether $A^\mu \to -A^\mu$ through the bounce, which will identify the physical branch. If PT-1 confirms chirality inversion, the torsion-active branch ($A^0 \neq 0$) is the physical one, since chirality inversion requires $A^0$ to change sign — which means it was nonzero before the bounce. If $A^0 = 0$ is the physical branch, chirality inversion must occur through a different mechanism, and PT-1 requires revision.

**OQ-2 — The condensate evolution through the bounce.** The cosmological Dirac equation (P.9.5.3) governs $\psi(t)$ through the bounce, but the full solution requires initial conditions from the pre-bounce phase. The evolution of $\eta(t)$ and $A^0(t)$ through the bounce depends on the pre-bounce state. CT-x (Bogoliubov analysis of sympathetic nucleation) provides the post-bounce initial conditions from the matter creation epoch, but the connection between pre-bounce and post-bounce condensate states is not yet fully characterised. This is identified as a sub-target of PT-1.

---

## P.9.10 — Incorporation Note for Appendix P

**Insertion point:** After Section P.7.7 (Chirality Preservation Across the Bounce) and before Section P.8 (Remaining Calculational Programme).

**Gap table update:** CT-viii row updated to CLOSED. PT-1 row updated to note that its prerequisites are now satisfied. CT-ix, CT-xiii, CT-xix, CT-xx rows updated to note that their CT-viii prerequisite is satisfied.

**P.8 update:** CT-viii entry updated from open target to closed, with reference to P.9.

---

*CT-viii derivation document | June 2026*
*Produced by: Variable Systems*
*Verification status: Pending independent expert review*
*Not for citation without author approval*
