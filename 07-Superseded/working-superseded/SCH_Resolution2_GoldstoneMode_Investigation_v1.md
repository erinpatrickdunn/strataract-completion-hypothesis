# SCH — Resolution 2 Investigation: Is Diffusion Even the Right Picture?
## A Deeper Problem Found, and a Candidate Fix With a Real Cost

**Status:** OPEN. Supersedes nothing; extends
`SCH_DiffusionScale_Tension_v1.md`. June 2026.

**What this document does.** Resolution 2 of the diffusion-scale
tension asked whether $\tau_{\text{diff}} \sim R^2 m_{\text{eff}}/\hbar$
is simply the wrong functional form — a dimensional estimate valid only
near the source, with the true large-$R$ behavior being wave-like
rather than diffusive, and therefore not subject to Check 1–3's
distance limits at all. That question is answered below, but the
answer surfaces a sharper problem than the one it was meant to resolve:
under the most natural reading of "wave-like propagation" — a
standard massive relativistic dispersion relation — **every condensate
wave frequency already tabulated in Appendix P Section P.7.5.2 is far
below the threshold frequency required to propagate as a real wave at
all.** A candidate resolution exists, grounded in ordinary QFT
(explicit vs. spontaneous symmetry breaking), but it is not free: it
requires revising Theorem 4's diffusion language and dropping one of
Paper B Section 5's two proposed discriminating signatures.

---

## 1. Setting Up the Check

If the condensate wave is a genuine propagating excitation rather than
a diffusive spread, the natural candidate is a linearized fluctuation
$\delta\eta$ around the condensate equilibrium value, obeying (from
expanding $S_{\text{geo}}$'s effective potential to quadratic order
around $\eta_{\text{eq}}$, exactly as Theorem 0 Step 3 already sets up
the curvature $m_{\text{eff}}^2 = m^2 - \lambda\eta_{\text{eq}}^2/2$) a
Klein-Gordon equation:

$$\left(\partial_t^2 - c^2\nabla^2 + \left(\frac{m_{\text{eff}}c^2}{\hbar}\right)^2\right)\delta\eta = 0$$

with dispersion relation $\omega^2 = c^2k^2 + (m_{\text{eff}}c^2/\hbar)^2$.
A mode of frequency $\omega$ propagates as a real traveling wave only if
$\omega \geq m_{\text{eff}}c^2/\hbar$ (the Compton/threshold frequency).
Below that, $k$ is imaginary and the disturbance is evanescent — it
decays exponentially over a Compton wavelength $\hbar/(m_{\text{eff}}c)$,
not a wave at all.

## 2. The Check

$$\omega_C = \frac{m_{\text{eff}}c^2}{\hbar}, \qquad f_C = \frac{\omega_C}{2\pi}$$

With $m_{\text{eff}} \sim 1.6\times10^{-6}$ eV/$c^2$:

$$f_C \approx 3.87\times10^{8}\text{ Hz} \approx 387\text{ MHz}$$

$$\lambda_C = \frac{\hbar}{m_{\text{eff}}c} \approx 12.3\text{ cm}$$

Against Appendix P Section P.7.5.2's own table:

| Source | $f_{\text{cond}}$ | Orders of magnitude below $f_C$ |
|---|---|---|
| 3 $M_\odot$ (stellar) | 0.5 Hz | 8.9 |
| 30 $M_\odot$ (stellar) | $5\times10^{-3}$ Hz | 10.9 |
| $10^4\,M_\odot$ (intermediate) | $5\times10^{-9}$ Hz | 16.9 |
| Sgr A* ($4\times10^6\,M_\odot$) | $10^{-13}$ Hz | 21.6 |
| M87* ($6.5\times10^9\,M_\odot$) | $4\times10^{-20}$ Hz | 28.0 |

Every entry is sub-threshold, and the gap grows systematically with
mass — because $f_{\text{cond}} \sim M^{-2}$ falls while $f_C$ is fixed
by $m_{\text{eff}}$ alone. **Under the standard massive dispersion
relation, none of these are propagating waves. All of them would be
evanescent within about 12 centimeters of the source.**

This is not the diffusion-scale problem restated. It's underneath it.
Even granting a genuinely wave-like (non-diffusive) picture, the
specific frequencies already tabulated throughout the framework — used
for the NANOGrav interpretation (Paper B 7.1), the antipodal
convergence mechanism (Paper A 2.11), and the rotation-curve-flattening
wavelength $\lambda_{\text{cond}} = c/f_{\text{cond}}$ (Paper A 2.11,
Paper B 7.4) — cannot propagate at all under the simplest reading of
"massive relativistic field," at the currently-adopted $m_{\text{eff}}$.

## 3. A Candidate Resolution: The Condensate Wave Is Not the Amplitude Mode

Theorem 6 already states that the matter phase spontaneously breaks a
$U(1)$ symmetry, $\psi \to e^{i\theta}\psi$. If that were the whole
story, Goldstone's theorem would guarantee an exactly massless
propagating mode — no threshold frequency, ballistic propagation at
exactly $c$, and both this problem and the diffusion-scale problem
would dissolve at once. It is not quite the whole story, and the
qualification matters.

**Checking which symmetry is actually relevant.** $\eta = \bar\psi\psi$
is invariant under the vector phase rotation $\psi\to e^{i\theta}\psi$
($\bar\psi\to\bar\psi e^{-i\theta}$, so $\bar\psi\psi$ is unchanged) —
that symmetry is not the one $\eta\neq0$ breaks. The symmetry $\eta\neq0$
*does* break is the chiral rotation $\psi\to e^{i\alpha\gamma^5}\psi$,
under which $(\eta, P)$ rotate into each other as a two-component
object: $\eta\to\eta\cos2\alpha - P\sin2\alpha$. This is exactly the
structure of chiral symmetry breaking by a scalar condensate in the NJL
model — the same mechanism that gives the pion its role as the
(pseudo-)Goldstone boson of QCD's chiral condensate $\langle\bar\psi\psi\rangle\neq0$.

**Why it's a *pseudo*-Goldstone mode, not an exact one.** The mass term
$-m\bar\psi\psi$ in $S_{\text{geo}}$ is not invariant under this chiral
rotation either — it explicitly breaks the same symmetry the
condensate spontaneously breaks, exactly as the quark mass explicitly
breaks QCD's chiral symmetry. Goldstone's theorem does not apply
cleanly to an explicitly-broken symmetry. What results instead is a
pseudo-Goldstone boson — a mode that would be exactly massless if $m=0$,
and acquires a mass suppressed relative to the condensate scale by the
size of the explicit breaking, in exact analogy to the
Gell-Mann–Oakes–Renner relation that gives the pion its small (but
nonzero) mass from the small (but nonzero) quark mass, rather than the
zero mass a purely spontaneous breaking would give.

**What this means concretely.** If this is the right picture, the
object that actually propagates as the "condensate wave" throughout the
framework is not a fluctuation of $\eta$ itself (mass $m_{\text{eff}}$,
the object relevant to Bi-209 and the $T_c$ calculation) but a
fluctuation of $P$ — a pseudo-Goldstone mode with its own mass,
call it $m_\pi^{\text{SCH}}$, set by a GMOR-type relation involving $m$
and $\lambda$, not simply equal to $m_{\text{eff}}$. If
$m_\pi^{\text{SCH}} \ll m_{\text{eff}}$ — plausible by analogy with the
real pion, which is roughly five times lighter than the constituent
quark mass scale that sets the QCD condensate, and could in principle
be suppressed by a much larger factor here depending on how small the
explicit breaking (the ratio of $m$ to the condensate scale) actually
is — then the Compton threshold computed in Section 2 above is the
wrong number entirely, and the real threshold could be low enough for
every frequency in the P.7.5.2 table to propagate as a genuine wave.

**This is not yet demonstrated.** It's a candidate mechanism, grounded
in standard QFT rather than invented for this problem, but it requires
an actual calculation — the SCH analogue of the GMOR relation — before
anyone can say whether $m_\pi^{\text{SCH}}$ is actually small enough.
That calculation is not done here.

## 4. What This Would Fix, If It Holds

If $m_\pi^{\text{SCH}}$ turns out sufficiently below the frequencies in
the P.7.5.2 table:

- **The evanescence problem in Section 2 above is resolved** — these
  become genuine propagating modes, not evanescent artifacts of using
  the wrong mass in the dispersion relation.
- **The diffusion-scale tension in
  `SCH_DiffusionScale_Tension_v1.md` is resolved as well, and by the
  same mechanism.** A propagating mode with a small mass moves
  ballistically at close to $c$; the travel time to any astrophysical
  distance is simply $R/c$ (or slightly more, for a nearly-massless but
  not-quite-massless mode), never the $R^2m/\hbar$ diffusive scaling
  that produced Neptune-orbit-scale distances over the age of the
  universe. A 1 Mpc separation, which took $8\times10^{29}$ years under
  the diffusive formula, takes about 3.26 million years at light speed
  — utterly unremarkable on cosmological timescales.
- **The antipodal convergence mechanism (Paper A 2.11, CT-xix)** was
  already implicitly assuming light-speed-scale wave propagation across
  $S^3$; this resolution makes that assumption consistent with the rest
  of the framework rather than an unexamined exception.

## 5. What This Costs, If It Holds

**Theorem 4's characterization of Term 2 as "diffusing" is wrong and
needs replacing.** The propagating condensate is not spreading via a
random-walk-like process with diffusion constant $\sim\hbar/m_{\text{eff}}$;
it is a (pseudo-Goldstone) wave propagating close to $c$. The formula
$\tau_{\text{diff}}\sim R^2m_{\text{eff}}/\hbar$ should not appear in a
future revision of Theorem 4 at all — it should be replaced with
$\tau \sim R/v_g$, where $v_g$ depends on $m_\pi^{\text{SCH}}$, not
$m_{\text{eff}}$.

**Paper B Section 5.2's Signature (ii) — "mass-dependence of diffusion
rate: heavier condensate diffuses more slowly" — does not survive.** A
pseudo-Goldstone mode propagating near $c$ has a propagation speed set
by its own (small, possibly universal) mass, not by $m_{\text{eff}}$,
and the whole premise of a slowly-spreading, measurably-still-catching-up
condensate profile is replaced by something that arrives at
essentially light-crossing speed. Section 5's test would need to be
substantially reconceived — plausibly as a null test (does the lensing
signal track the *current* position of stellar matter with negligible
lag, rather than a broadening-over-time signature) rather than a
timescale measurement. Signatures (i) and (iii) of Section 5.2 may
survive in modified form; Signature (ii) specifically does not.

**$m_{\text{eff}}$ and $m_\pi^{\text{SCH}}$ are now two different
parameters, not one.** Every place the framework currently treats a
single $m_{\text{eff}}$ as governing both the condensate's thermal
properties (Bi-209, $T_c$) and its propagation (black hole frequencies,
diffusion, lensing) needs to distinguish which of the two masses is
actually relevant. This is a nontrivial bookkeeping change across
Appendix P, Paper A, and Paper B, not a one-line fix.

## 6. What This Does Not Resolve

The actual value of $m_\pi^{\text{SCH}}$ is unknown. Nothing here shows
it is small enough — only that the mechanism exists to make it small,
by analogy with a real, established piece of physics (the pion). This
is exactly the kind of gap Paper C flagged honestly for its $T_c$
problem rather than assuming away, and the same standard applies here.

## 7. New Calculational Target Proposed

**CT-vii should be understood to include**, as a prerequisite
sub-calculation before its existing scope (the black hole condensate
propagator) can be trusted: derive the GMOR-type relation for this
action, expressing $m_\pi^{\text{SCH}}$ in terms of $\{m, \lambda,
\eta_{\text{eq}}\}$, and evaluate whether it is small enough relative
to the Compton frequency computed in Section 2 to permit the
propagating modes already claimed throughout Paper A and Paper B. Until
this is done, every claim in the framework that depends on
condensate-wave propagation over galactic-to-cosmological distances —
the black hole frequency table, the NANOGrav interpretation, the
antipodal convergence mechanism, and the rotation-curve-flattening
wavelength — rests on an unverified assumption about which mass
actually governs propagation.

## 8. Relationship to Resolution 1

Resolution 1 (density-dependent $m_{\text{eff}}$, CT-xviii sub-target
a) was not separately pursued here and remains a live fallback if the
GMOR-type calculation above returns a pseudo-Goldstone mass that is
*not* sufficiently suppressed. The two resolutions are not mutually
exclusive — a density-dependent condensate scale and a separately-light
propagating pseudo-Goldstone mode could both be true simultaneously —
but Resolution 2 is the more structurally motivated of the two, since
it follows from symmetry-breaking structure the framework already
claims (Theorem 6) rather than requiring a new, unmotivated
density-dependence to be fitted after the fact.

---

*SCH Resolution 2 Investigation — v1 | June 2026*
*Open item. Identifies a sharper problem than the one it set out to
resolve (sub-Compton-frequency evanescence, affecting the black hole
condensate table, NANOGrav interpretation, antipodal convergence
mechanism, and rotation-curve-flattening wavelength), and a candidate
fix (pseudo-Goldstone propagation via the already-claimed chiral
symmetry breaking of Theorem 6) that would resolve both this and the
diffusion-scale tension simultaneously — at the cost of revising
Theorem 4's diffusion language and dropping Paper B Section 5.2's
mass-dependence signature. The actual pseudo-Goldstone mass is not
calculated here and is the required next step.*
