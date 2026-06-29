# SCH — PT-1 Topological Phase Investigation
## Is the Monodromy Phase a Geometric Holonomy?

*Working Document — v1 | June 2026*

**Status:** OPEN INVESTIGATION — motivated by the monodromy calculation (v1)

**The question:** The normal-mode equations of the $(A^0, P)$ system are

$$\dot{u} = i\Omega_+(t)\,u, \qquad \dot{v} = i\Omega_-(t)\,v$$

with solutions $u(t) = e^{i\int\Omega_+ dt}\,u(0)$, which is the form
of holonomy in a $\mathrm{U}(1)$ bundle. The monodromy calculation showed
the accumulated phase $\alpha_+ \sim 10^{54}$ appears unconstrained.

**The precise question is:** Does the normal-mode evolution define a
*natural* connection on a principal bundle associated with the condensate
dynamics in SCH? If yes, the topology of that bundle may quantize the
holonomy and constrain $\alpha_+$. If no, $\alpha_+$ is purely dynamical
and the monodromy is generically irrational.

This is the question. Everything below is an attempt to answer it.

---

## Section 1 — The Geometric Setup

### 1.1 What Is Already Present in the Framework

The SCH action $S_{\text{geo}}$ is defined on a principal $\mathrm{Spin}(1,3)$
bundle $P_{\text{spin}}$ over spacetime $M = S^3 \times \mathbb{R}$. The
spinor field $\psi$ is a section of the associated spinor bundle
$\mathcal{S} = P_{\text{spin}} \times_{\rho} \mathbb{C}^4$ where $\rho$
is the Dirac representation.

The geometric data includes:
- A $\mathrm{Spin}(1,3)$ connection $\omega^{ab}_\mu$ (the spin connection)
- A tetrad $e^a_\mu$ encoding the $S^3$ geometry
- The spinor field $\psi$ as a section of $\mathcal{S}$

The cosmological reduction (CT-viii) projects all of this onto the
time axis: $\psi = \psi(t)$, with the spatial $S^3$ integrated out.
After reduction, the only surviving geometric structure is the temporal
evolution of $\psi(t)$.

### 1.2 The Reduced Bundle Structure

After the $S^3$ integration of P.9.4.1, the reduced system lives on
the temporal manifold $\mathbb{R}$ (or $S^1$ if the cycle is compact).
The relevant bundle is the restriction of $\mathcal{S}$ to the time axis:

$$\mathcal{S}\big|_{\mathbb{R}} = \mathbb{R} \times \mathbb{C}^4$$

This is trivial as a vector bundle over $\mathbb{R}$. A trivial bundle
has no nontrivial topology to quantize anything.

**However**, the condensate dynamics define a preferred decomposition
of $\mathbb{C}^4$ at each time: the four spinor components split into
the bilinear eigenspaces corresponding to the normal modes $(u, v)$.
This splitting is not the full $\mathbb{C}^4$ — it is a $\mathbb{C}^2$
subbundle spanned by the condensate degrees of freedom $(A^0, P)$.

The question reduces to: what is the geometric structure of this
$\mathbb{C}^2$ subbundle over the cosmological cycle?

---

## Section 2 — Identifying the Connection

### 2.1 The Normal-Mode Bundle

Define the normal-mode bundle as follows. At each time $t$, the
condensate bilinears $(A^0(t), P(t))$ span a two-dimensional real
subspace of the space of spinor bilinears. The normal modes
$u = A^0 + P$ and $v = A^0 - P$ define a basis for this subspace.

Under the cosmological evolution, this basis rotates. The evolution
equations are:

$$\dot{u} = i\Omega_+(t)\,u, \qquad \dot{v} = -i\Omega_-(t)\,v$$

where $\Omega_+ = \Omega - \Gamma$ and $\Omega_- = \Omega + \Gamma$
with $\Omega = 2m + \lambda\eta_0/a^3$ and $\Gamma = \kappa\alpha\mathcal{J}/a^3$.

Each of $u$ and $v$ evolves in its own complex line. The evolution
is multiplication by a $\mathrm{U}(1)$ phase. This is precisely the
definition of parallel transport in a $\mathrm{U}(1)$ connection on
a complex line bundle.

**Definition:** Let $L_+$ and $L_-$ be the complex line bundles over
the cosmological time interval $I = [0, T_{\text{cycle}}]$ whose
fibres at time $t$ are spanned by $u(t)$ and $v(t)$ respectively.
The cosmological Dirac equation defines a connection $\nabla$ on
$L_+ \oplus L_-$ by:

$$\nabla_t u = \dot{u} - i\Omega_+(t)\,u = 0$$
$$\nabla_t v = \dot{v} + i\Omega_-(t)\,v = 0$$

The parallel transport of $u$ from $t=0$ to $t=T$ is multiplication
by $e^{i\int_0^T \Omega_+(t)\,dt}$, and similarly for $v$.

**This is a connection.** The question is whether it is a *natural*
one — arising from the geometry of $S_{\text{geo}}$ rather than from
an arbitrary choice.

### 2.2 Naturality: Tracing the Connection to $S_{\text{geo}}$

The connection on $L_+ \oplus L_-$ is natural if it can be derived
from the original spin connection $\omega^{ab}_\mu$ on $P_{\text{spin}}$
by a canonical procedure (restriction, projection, reduction).

**The derivation chain:**

Step 1. The full spin connection $\omega^{ab}_\mu$ on $S^3 \times \mathbb{R}$
defines parallel transport of sections of $\mathcal{S}$.

Step 2. The cosmological reduction (CT-viii, P.9.4.1) computes the
spatial components $\omega^{ab}_i$ and integrates them over $S^3$,
leaving only the temporal component $\omega^{ab}_0$ (which is pure
gauge in the homogeneous case, set to zero by the cosmological gauge
choice in P.9.2).

Step 3. The mass and interaction terms in $S_{\text{geo}}$ (the $m$,
$\lambda$, and $\kappa\alpha$ terms) contribute to the equation of
motion for $\psi(t)$.

Step 4. The bilinear projection onto $(A^0, P)$ — a specific
two-dimensional subspace of the full spinor bilinear space — defines
the sub-bundle $L_+ \oplus L_-$.

The connection on $L_+ \oplus L_-$ is the pullback of the full
$\mathrm{Spin}(1,3)$ connection through this chain of reductions
and projections.

**Naturality criterion:** The connection is natural if the projection
in Step 4 commutes with the $\mathrm{Spin}(1,3)$ action. That is,
if the subspace spanned by $(A^0, P)$ is preserved by the
$\mathrm{Spin}(1,3)$ symmetry of the action.

**Check:** The bilinear $A^0 = \bar{\psi}\gamma^0\gamma^5\psi$ is
the temporal component of the axial current $A^\mu = \bar{\psi}\gamma^\mu\gamma^5\psi$.
Under a local Lorentz transformation $\Lambda \in \mathrm{Spin}(1,3)$:

$$A^\mu \to \Lambda^\mu{}_\nu A^\nu$$

The temporal component $A^0$ is not preserved by general Lorentz
transformations — boosts mix $A^0$ with spatial components $A^i$.

**However**, in the cosmological context, the spatial components
$A^i = 0$ by the isotropy of $S^3$ (P.9.3). The residual symmetry
that preserves $A^i = 0$ is the $\mathrm{SO}(3)$ spatial rotation
subgroup of $\mathrm{Spin}(1,3)$. Under $\mathrm{SO}(3)$, $A^0$
is a scalar and is preserved.

**The projection is natural with respect to $\mathrm{SO}(3)$**
(the isotropy group of the cosmological background), but not with
respect to the full $\mathrm{Spin}(1,3)$.

This is sufficient for the purposes of the cosmological problem:
the cosmological background breaks $\mathrm{Spin}(1,3)$ to $\mathrm{SO}(3)$,
and within this reduced symmetry, the connection on $L_+ \oplus L_-$
is natural.

### 2.3 The Curvature of the Connection

For a $\mathrm{U}(1)$ connection on a line bundle $L$ over a
one-dimensional base $I = [0, T]$, the curvature two-form vanishes
identically (there are no two-forms on a one-dimensional manifold).

A flat connection on a trivial bundle over an interval has no
topological content: the holonomy is $e^{i\int_I A}$ where $A$
is the connection one-form, and this can take any value in $\mathrm{U}(1)$.

**This confirms: over the interval $I$, topology does not constrain
the holonomy.** The phase $\alpha_+$ is not quantized by the topology
of $I$.

---

## Section 3 — The Loop: Where Topology Could Enter

### 3.1 Compactifying the Time Direction

Topology becomes relevant when the base is a compact manifold with
nontrivial fundamental group or higher homotopy groups.

The cosmological cycle is naturally a loop: the universe evolves from
one bounce through maximum expansion back to another bounce, and the
physical situation at the second bounce is (by the bounce regularity
established in CT-viii) metrically identical to the first. This
compactifies the time direction to a circle $S^1$:

$$S^1_{\text{cycle}} = [0, T_{\text{cycle}}]\,/\,\sim$$

where the identification $0 \sim T_{\text{cycle}}$ is valid if
(and only if) the boundary conditions on $\psi$ are compatible
with the identification.

The fundamental group $\pi_1(S^1) = \mathbb{Z}$. A $\mathrm{U}(1)$
bundle over $S^1$ is classified by its winding number $n \in \mathbb{Z}$.
The holonomy of the canonical connection on the degree-$n$ bundle
is $e^{2\pi i n}$ — but this equals $1$ for all $n$, so the holonomy
of the *canonical* $\mathrm{U}(1)$ bundle is always trivial.

The connection one-form on the degree-$n$ bundle is $A = n\,d\theta$
where $\theta \in [0, 2\pi]$ parametrises $S^1$, and the holonomy
is $e^{i\oint A} = e^{2\pi i n} = 1$.

For a *general* connection with one-form $A = f(\theta)d\theta$,
the holonomy is $e^{i\int_0^{2\pi}f(\theta)d\theta}$, which can be
any element of $\mathrm{U}(1)$. Topology constrains the bundle
(the winding number $n$) but not the connection (the function $f$).

**Conclusion for $\alpha_+$:** Even after compactification to $S^1$,
the holonomy $e^{i\alpha_+}$ is unconstrained by the topology of the
$\mathrm{U}(1)$ bundle over $S^1$. It can be any element of
$\mathrm{U}(1)$.

### 3.2 The Boundary Condition Constraint

The compactification $0 \sim T_{\text{cycle}}$ is only valid if the
boundary conditions on $\psi$ are consistent. This is sub-question (a)
from the PT-1 problem specification: which spin structure on the
temporal $S^1$ is physical?

The two spin structures on $S^1$ correspond to:
- **Periodic:** $\psi(T_{\text{cycle}}) = +\psi(0)$ (trivial spin structure)
- **Antiperiodic:** $\psi(T_{\text{cycle}}) = -\psi(0)$ (non-trivial spin structure)

If the antiperiodic spin structure is chosen, then the temporal
circle is actually a *spin circle* $S^1_{\text{spin}}$ with the
non-trivial spin structure. The relevant bundle is not a $\mathrm{U}(1)$
bundle but a $\mathrm{Spin}(1)$ bundle, and the correct holonomy
condition is:

$$\text{Holonomy} = -1 \in \mathrm{Spin}(1) \cong \mathbb{Z}/2$$

This would force $e^{i\alpha_+} = -1$, i.e., $\alpha_+ = (2n+1)\pi$.

**This is exactly the quantization condition for chirality inversion.**

The question has now been precisely localised: **does SCH select the
antiperiodic spin structure on the temporal $S^1$?**

---

## Section 4 — The Spin Structure Question

### 4.1 Spin Structures on $S^3 \times S^1$

The full cosmological spacetime (after compactification) is
$S^3 \times S^1$. The spin structures on a product manifold are
products of spin structures on the factors.

$S^3$ has a unique spin structure (since $\pi_1(S^3) = 0$, there
is only one spin structure up to isomorphism — or equivalently,
$H^1(S^3; \mathbb{Z}/2) = 0$).

$S^1$ has exactly two spin structures, classified by
$H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$: periodic and antiperiodic.

Therefore $S^3 \times S^1$ has exactly **two** spin structures,
differing only in the spin structure on the $S^1$ factor:

$$\mathcal{S}_{++}: \text{ periodic on } S^1 \text{ (trivial)}$$
$$\mathcal{S}_{+-}: \text{ antiperiodic on } S^1 \text{ (non-trivial)}$$

Both are geometrically valid spin structures. The choice between
them is a physical input to the theory, not determined by the
local geometry.

### 4.2 Can SCH Select the Spin Structure?

The action $S_{\text{geo}}$ is defined on the spinor bundle
$\mathcal{S}$. For a given spin structure, the action, path integral,
and partition function are all well-defined. Different spin structures
give different partition functions.

In quantum field theory at finite temperature, the choice of spin
structure on the temporal $S^1$ determines whether fermions obey
periodic ($\mathcal{S}_{++}$) or antiperiodic ($\mathcal{S}_{+-}$)
boundary conditions. Antiperiodic boundary conditions for fermions
in the thermal direction is the *standard* choice — it is required
for the correct thermal partition function (Matsubara formalism,
referenced in Appendix P Theorem 3). The antiperiodic boundary
condition for fermions on the thermal $S^1$ is not a choice — it
is imposed by the spin-statistics theorem.

**This is the key observation:**

> The spin-statistics theorem requires fermions to have antiperiodic
> boundary conditions on any compact temporal direction. In the
> cosmological context, the temporal $S^1$ of the cosmological cycle
> plays the role of the thermal circle. The spin-statistics theorem
> therefore selects $\mathcal{S}_{+-}$ — the antiperiodic spin
> structure on the temporal $S^1$ — as the physical spin structure.

If this selection is correct, the boundary condition on $\psi$ is:

$$\psi(T_{\text{cycle}}) = -\psi(0) \tag{BC-anti}$$

### 4.3 Translating the Boundary Condition to the Phase

The boundary condition (BC-anti) constrains the solution $\psi(t)$
of the cosmological Dirac equation. In the normal-mode decomposition,
$u = A^0 + P$ and $v = A^0 - P$ are bilinears — they are quadratic
in $\psi$, not linear.

Under $\psi \to -\psi$: $u \to (-1)^2 u = +u$ and $v \to +v$.

So the antiperiodic boundary condition on $\psi$ gives **periodic**
boundary conditions on the bilinears $u$ and $v$:

$$u(T_{\text{cycle}}) = +u(0), \qquad v(T_{\text{cycle}}) = +v(0)
\tag{BC-bilinear}$$

The monodromy of $u$ is $e^{i\Phi_-} = +1$, requiring $\Phi_- = 2k\pi$.
The monodromy of $v$ is $e^{-i\Phi_+} = +1$, requiring $\Phi_+ = 2l\pi$.

**This gives $A^0 \to +A^0$ and $P \to +P$ per cycle — not chirality inversion.**

The antiperiodic spin structure on the temporal $S^1$, applied to
the bilinears, produces periodicity of the bilinears, not inversion.

### 4.4 The Resolution: The Boundary Condition Must Act on $\psi$, Not on Bilinears

The PT-1 claim $A^\mu \to -A^\mu$ cannot follow from the boundary
condition on $\psi$ alone, because $A^\mu$ is bilinear in $\psi$ and
the sign of $\psi$ cancels in bilinears.

For $A^0 \to -A^0$ to be enforced by a boundary condition, one would
need a boundary condition that is *linear* in $A^0$, not derivable
from a boundary condition on $\psi$.

This is possible only if there is an independent dynamical field — a
field that transforms as $A^\mu$ under Lorentz symmetry and has its
own boundary condition. In SCH, $A^\mu = \bar{\psi}\gamma^\mu\gamma^5\psi$
is a composite operator, not an independent field. It does not have
independent boundary conditions.

**Conclusion from Section 4:** The spin-statistics argument selects
the antiperiodic spin structure on the temporal $S^1$, but this forces
the bilinears to be *periodic*, giving $A^0 \to +A^0$ per cycle, not
$A^0 \to -A^0$.

---

## Section 5 — A Different Topological Mechanism

### 5.1 The Aharonov-Bohm Possibility

There is one remaining mechanism that could quantize the holonomy
non-trivially: an Aharonov-Bohm type effect, where the connection
has a non-trivial holonomy around a loop even though the curvature
vanishes everywhere on the loop.

This requires the loop (the cosmological cycle) to be non-contractible
in the *total space* of the bundle, even if it is contractible in
the base manifold.

For the $\mathrm{U}(1)$ bundle $L_+$ over $S^1_{\text{cycle}}$,
the total space is $L_+ = S^1 \times \mathbb{C}$ (trivial bundle)
or a non-trivial $\mathrm{U}(1)$ bundle over $S^1$. The non-trivial
bundles over $S^1$ are classified by $\pi_1(\mathrm{U}(1)) = \mathbb{Z}$
— the winding number.

A degree-$n$ $\mathrm{U}(1)$ bundle over $S^1$ admits connections
with holonomy $e^{2\pi i n/N}$ for various $N$, but as noted in
Section 3.1, the holonomy is determined by the connection one-form,
not the bundle degree alone.

The Aharonov-Bohm mechanism requires a *source* of curvature in the
interior of the loop — a magnetic flux enclosed by the loop. In the
condensate bundle, the curvature of the connection on $L_+$ over
the cosmological time interval is zero (no two-forms on a 1D base).
There is no enclosed flux.

**The Aharonov-Bohm mechanism does not apply.**

### 5.2 The Berry Phase Possibility

Berry phases arise when parameters of a Hamiltonian are varied
adiabatically around a closed loop in parameter space. The accumulated
phase is the holonomy of the Berry connection on the parameter-space
bundle.

The Berry connection is geometric (natural) if the parameter space
has a natural metric and the eigenstates vary smoothly. The Berry
phase is quantized if the parameter-space loop encloses a source of
curvature (a degeneracy point, a monopole in parameter space).

In the condensate system, the "Hamiltonian" governing $(u, v)$
evolution has the eigenvalues $i\Omega_\pm(t)$. The parameters
are $\{\Omega_+(t), \Omega_-(t)\}$, which are functions of $a(t)$.
The cosmological evolution traces a path in the $(\Omega_+, \Omega_-)$
plane.

The path starts at the bounce ($a \to a_{\text{b}}$, $\Omega_\pm \to \infty$),
reaches maximum expansion ($a = a_{\text{max}}$, $\Omega_\pm \to 2m \pm \kappa\alpha\mathcal{J}/a_{\text{max}}^3$),
and returns to the bounce. This path is contractible in the
$(\Omega_+, \Omega_-)$ plane (it is a loop that retraces itself,
since the expansion and contraction phases are symmetric in Branch 1).

A contractible loop in parameter space encloses no flux and gives
zero Berry phase.

**The Berry phase mechanism does not produce non-trivial quantization
for a symmetric cosmological cycle.**

However, if the cycle is asymmetric — if $\Omega_+(t)$ on the
expanding phase differs from $\Omega_+(t)$ on the contracting phase —
the parameter-space loop is not contractible and could enclose flux.
In Branch 2 (torsion-active), the $A^0$ oscillations produce
asymmetry between the expanding and contracting phases, and the
parameter-space loop may be non-contractible. This deserves
investigation but is beyond the current scope.

---

## Section 6 — The Most Promising Remaining Mechanism

### 6.1 Global Condensate Modes on $S^3$

The spatial $S^3$ has a quantised mode spectrum for the condensate
field, with the lowest modes at wavelength $\sim 2\pi R_{\text{universe}}$
(Appendix P, P.7.6.3). These global modes are excited by the
cosmological dynamics.

The cosmological Dirac equation (D) governs $\psi(t)$ in the
homogeneous sector — the zero spatial momentum mode. But the full
spinor field on $S^3 \times \mathbb{R}$ has an infinite tower of
spatial modes:

$$\psi(\mathbf{x}, t) = \sum_n \psi_n(t)\,Y_n(\mathbf{x})$$

where $Y_n$ are spinor harmonics on $S^3$.

The homogeneous reduction uses only the $n=0$ mode ($Y_0 = $ const).
But the global $S^3$ modes couple to the zero mode through the
curvature of $S^3$ — specifically through the Ricci scalar term in
the spin connection.

If this coupling between the zero mode and the global $S^3$ modes
is non-trivial, the effective connection on $L_+$ (derived from the
zero mode) acquires corrections from the global mode structure. These
corrections are topological in origin — they reflect the quantised
spectrum of $S^3$ — and could force $\alpha_+$ to take values in a
discrete set.

**This is the most promising remaining mechanism**, because:

(a) It is internal to SCH — the $S^3$ topology is already a derived
    result of the framework (P.7.6).

(b) It connects the temporal evolution (the monodromy) to the spatial
    topology (the $S^3$ mode spectrum), which is physically natural
    for a closed universe.

(c) It has not yet been computed in the SCH framework.

### 6.2 The Coupling Term

The coupling between the zero mode $\psi_0(t)$ and the $n$-th spatial
mode $\psi_n(t)$ through the $S^3$ curvature enters through the
spatial part of the covariant derivative $D_i\psi$. In P.9.4.1, the
spatial covariant derivatives were integrated over $S^3$ and found to
produce the $-3/2$ kinetic coefficient for the zero mode. The
cross-terms between different modes vanish by orthogonality of the
$S^3$ harmonics.

This means the zero mode $\psi_0(t)$ and the spatial modes $\psi_n(t)$
decouple at the level of the quadratic action. There is no coupling
from the $S^3$ curvature at this order.

**At quadratic order, the global $S^3$ modes do not correct the
connection on $L_+$.** Corrections would arise from the quartic
self-interaction $(\lambda/4)(\bar{\psi}\psi)^2$ — the Term 3
condensate interaction — which couples different spatial modes
non-linearly. At the level of the mean-field approximation used
throughout the framework, these cross-mode couplings are suppressed.

### 6.3 Summary of the Topological Investigation

| Mechanism | Status | Result |
|-----------|--------|--------|
| $\mathrm{U}(1)$ bundle topology over $I = [0,T]$ | Checked | No constraint: bundle over interval is trivial |
| Compactification to $S^1$, winding number | Checked | Constrains bundle degree, not connection holonomy |
| Spin structure on temporal $S^1$ | Checked | Antiperiodic BC on $\psi$ gives periodic BC on bilinears: $A^0 \to +A^0$ |
| Aharonov-Bohm effect | Checked | No enclosed flux on a 1D base |
| Berry phase from parameter-space loop | Checked | Zero for symmetric cycle; possibly nonzero in Branch 2 |
| Global $S^3$ mode coupling | Checked | Decouples at quadratic order; suppressed in mean-field |

---

## Section 7 — The Geometric Meaning of the Connection

Despite the negative results above on quantization, the identification
of the normal-mode evolution as a $\mathrm{U}(1)$ connection is
geometrically meaningful. It clarifies what the monodromy phase *is*:

**$\alpha_+$ is the holonomy of the condensate axial-current connection
over the cosmological cycle.**

This connection is natural with respect to the $\mathrm{SO}(3)$ isotropy
of the cosmological background (Section 2.2). It is derived from the
spin connection and the condensate dynamics — it is not an arbitrary
rewriting.

The holonomy is a physical observable: it determines the phase
relationship between the condensate's chiral state before and after
one cosmological cycle. It is an intrinsic property of the SCH
cosmological solution.

The fact that it is not topologically quantized (at the level of
analysis completed here) does not make it unphysical. It means the
holonomy is a continuous function of the action parameters, taking
values in $\mathrm{U}(1)$. Its value for the physical parameters of
our universe is determined by $m$, $\alpha$, $\eta_0$, $\mathcal{J}$,
and $a_c$ — all of which are in principle measurable.

**The reformulation that is correct and publishable:**

> *The cosmological Dirac equation in SCH defines a natural $\mathrm{U}(1)$
> connection on the condensate axial-current line bundle $L_+$ over the
> cosmological cycle. The holonomy of this connection, $e^{i\alpha_+}$,
> determines the chirality transformation of the condensate across one
> bounce cycle. The holonomy is not topologically quantized but is a
> well-defined function of the SCH action parameters, computable after
> the Bi-209 calibration.*

---

## Section 8 — One Remaining Thread: The Berry Phase in Branch 2

The Berry phase analysis in Section 5.2 found zero Berry phase for
the symmetric Branch 1 cycle. Branch 2 (torsion-active) is asymmetric:
the $A^0$ oscillations in Branch 2 (CT-ix, Section P.10.5) produce
different values of $\Omega_\pm$ on the expanding vs. contracting phases.

In Branch 2, the parameter-space loop traced by $(\Omega_+, \Omega_-)$
during the cosmological cycle is not a retraced path — it is a genuine
loop in the $(\Omega_+, \Omega_-)$ plane. If this loop encloses a
degeneracy point (where $\Omega_+ = \Omega_-$, i.e., $\Gamma = 0$,
i.e., $\mathcal{J} = 0$), the Berry phase is non-zero.

The condition $\Gamma = 0$ corresponds to $\mathcal{J} = 0$ — zero
conserved vector current. This is a degenerate case (no condensate
particles). For $\mathcal{J} \neq 0$ (the physical case), the
degeneracy point is not enclosed by the loop unless the loop
specifically circles $\mathcal{J} = 0$, which would require
$\mathcal{J}$ to change sign during the cycle — forbidden by the
conservation law $a^3 J^0 = \mathcal{J} = \text{const}$.

**The Berry phase in Branch 2 is also zero for $\mathcal{J} \neq 0$.**

---

## Section 9 — Conclusion

**The phase $\alpha_+$ is a holonomy, but not a topologically
quantized one.**

The normal-mode evolution defines a genuine, natural $\mathrm{U}(1)$
connection on the condensate axial-current bundle. This is a correct
and meaningful geometric statement. However, all mechanisms that could
force the holonomy to take discrete values have been checked and found
either inapplicable or producing the wrong result:

- The spin structure on the temporal $S^1$ forces bilinear periodicity,
  giving $A^0 \to +A^0$, not $-A^0$.
- No Aharonov-Bohm flux is enclosed.
- The Berry phase vanishes for the physical symmetric cycle.
- The global $S^3$ modes decouple at the order of approximation used.

The holonomy $e^{i\alpha_+}$ is a continuous, parameter-dependent
element of $\mathrm{U}(1)$. Its value for the physical universe
is determined by the action parameters and is computable after the
Bi-209 calibration.

**This is a definite negative result.** It is also a clean result.
The monodromy is not constrained to $-\mathbf{1}$ by topology.
Whether the SCH framework predicts chirality inversion per cycle
is a quantitative question about the action parameters, not a
topological consequence of the framework's structure.

**The open question that remains genuinely open:** Whether the
action parameters of SCH, once fixed by the Bi-209 calibration,
happen to give $e^{i\alpha_+} = -1$. This is a numerical question.
It has a definite answer. It is not answerable without the calibration.

---

## Appendix: The Correct Statement for Appendix P

The gap table entry for Gap 7 / PT-1 should read:

> **Gap 7 — Chirality inversion across bounce / sympathetic nucleation:
> OPEN QUESTION — CLAIM REVISED.**
>
> The cosmological Dirac equation defines a natural $\mathrm{U}(1)$
> connection on the condensate axial-current line bundle $L_+$ over the
> cosmological cycle. The chirality transformation $A^0 \to -A^0$
> (equivalently, holonomy $= -1$) holds if and only if the accumulated
> phase $\alpha_+ = \int_{\text{cycle}}\Omega\,dt = (2n+1)\pi$ for
> some integer $n$.
>
> A systematic investigation of topological quantization mechanisms
> (spin structures, Aharonov-Bohm effects, Berry phases, global $S^3$
> mode coupling) finds no mechanism that forces this condition to hold
> universally. The holonomy is a continuous function of the SCH action
> parameters $\{m, \lambda, \alpha, \kappa, \eta_0, \mathcal{J}, a_c\}$.
>
> The original claim that the standard spin representation on $S^3$
> predicts $A^\mu \to -A^\mu$ is not supported: the spatial antipodal
> map gives $\psi \to -\psi$ but bilinears satisfy $A^\mu \to +A^\mu$.
> The temporal reversal argument gives $A^0 \to -A^0$ for linear
> fields but not for composite bilinears without additional structure.
>
> **Status: Computable after Bi-209 calibration. Not a universal
> topological consequence of SCH. Sympathetic nucleation mechanism
> is not established but is not ruled out.**

---

*SCH PT-1 Topological Phase Investigation — v1 | June 2026*
*Not for citation without author approval.*
*Main result: The monodromy phase is a genuine geometric holonomy
but is not topologically quantized by any mechanism identified
in the current framework. The chirality transformation per cycle
is a parameter-dependent continuous quantity.*
