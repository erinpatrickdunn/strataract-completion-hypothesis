# `Foundation-B-Result-B2-v1.0`

## The Fierz Ambiguity of the Mean-Field Condensate in $S_{\rm geo}$

**Status: Established result. Halted at a legitimate Category-3 boundary per Constitution §7(b)–(c).**

---

### 1. The corrected algebraic substrate (Foundation A v1.1)

$$\eta^2=\tfrac15P^2-\tfrac15V^2+\tfrac15A^2-\tfrac1{10}T^2 \qquad P^2=\tfrac15\eta^2-\tfrac15V^2+\tfrac15A^2+\tfrac1{10}T^2$$
$$A^2-V^2=2\eta^2+2P^2 \qquad\qquad T^2=-6\eta^2+6P^2$$
Mutually self-consistent under independent substitution ($F^2=\mathbb1$). Error history: v1.0's certificate summary contained a transcription sign error, caught only by using the system to build $\Gamma[\sigma,\pi]$, not by re-auditing the certificate directly — the derivation chain itself was never wrong.

### 2. Exact bosonization — unambiguous

For any $t\in[0,1)$, the operator identity
$$-\frac\lambda4\eta^2 = -\frac{\lambda(1-t)}4\eta^2-\frac{\lambda t}{20}P^2+\frac{\lambda t}{20}(V^2-A^2)+\frac{\lambda t}{40}T^2$$
holds exactly (Fierz identity, not approximation). A single-field HS transform of the *exact* path integral suffices at $t=0$; the parameter $t$ only acquires observable content once a specific decoupling **and** a mean-field truncation are both applied.

### 3. Symmetric reduction — exact within flat-space Target 0

$\Gamma[\sigma,\pi,V^{\rm aux},A^{\rm aux},T^{\rm aux}]$ is exactly $SO(3)$-invariant (trace-under-similarity argument). Auxiliary fields carry only algebraic second-class constraints (no kinetic terms $\Rightarrow$ no gauge/Hamiltonian constraint structure). Target 0's explicit flat-background restriction removes gravity, and with it the Hawking-type obstruction to Palais' PSC. **Restricting to $V^{\rm aux}=A^{\rm aux}=T^{\rm aux}=0$ before extremizing is exact, not a truncation** — but this conclusion is scope-limited to flat-space Target 0 and does not transfer automatically to §P.9's constrained cosmological system.

### 4. Fermion determinant — derived from $S_{\rm geo}$'s own operator

With $D=i\partial\!\!\!/-(m+\sigma)-i\gamma^5\pi$ and $\bar M=(m+\sigma)-i\gamma^5\pi$: $p\!\!\!/\bar M=Mp\!\!\!/$ exactly (using $\gamma^5p\!\!\!/=-p\!\!\!/\gamma^5$), giving $(p\!\!\!/-M)(p\!\!\!/+\bar M)=p^2-(m+\sigma)^2-\pi^2$. Independently confirmed by explicit rest-frame block-matrix determinant. **$\mathrm{Tr}\ln D = F\big((m+\sigma)^2+\pi^2\big)$, established directly**, not imported from the NJL literature by analogy.

### 5. The central theorem

$$\Gamma_t(\sigma,\pi) = \frac{\sigma^2}{\lambda(1-t)}+\frac{5\pi^2}{\lambda t}+F\big((m+\sigma)^2+\pi^2\big)$$
is exactly even in $\pi$ at every $t$ $\Rightarrow$ $\pi=0$ is an exact stationary point at every $t$, and the exact minimum for $t$ below a threshold $t_*$ set by $F'$ at the background value. Hence $\pi_{\rm eq}(t)=0$ exactly (not asymptotically) near $t=0$, closing the envelope-theorem evaluation with no asymptotic gap:
$$\boxed{\left.\frac{d\Gamma_{\rm MF}}{dt}\right|_{t=0} = \frac{\sigma_0^2}{\lambda}}$$

### 6. Statement of the result

> Within the mean-field approximation used by Target 0, the condensate sector of $S_{\rm geo}$ exhibits a genuine Fierz ambiguity: the stationary effective potential depends on the auxiliary-field decoupling channel whenever the scalar condensate is nonzero. This does not falsify condensation; it falsifies the claim that Target 0 had already derived condensation from the underlying theory in a representation-independent way.

### 7. Halt point (Category 3, per Constitution §7(b))

Removing this dependence requires including boson ($\sigma,\pi$) fluctuation loops — a genuinely different approximation order than Target 0's stated scope (one-fermion-loop, zero-boson-loop, §4 of the original Constitution). This is not a continuation of B2; it is a new target requiring its own scoping document if pursued.

---

## Interpretive note, flagged now rather than left implicit

This result has a direct bearing on the rest of the SCH corpus that I want to state plainly rather than let sit unstated: **Theorem 6's Mexican-hat potential, §P.11's GMOR relation, and every downstream quantity built on "$\eta_{\rm eq}\ne0$" (the Bi-209 calibration's target parameter $m_{\rm eff}$, the bounce mechanism's condensate density, Paper C's entire leptonic-mass-shift program) are all built on a mean-field potential of exactly the kind just shown to be Fierz-ambiguous.** None of those documents specify which $t$ (equivalently, which HS channel) their stated potential corresponds to — the choice was made implicitly by writing $-\frac\lambda4\eta^2$ and HS-transforming it as if that were the only option, which B0–B2 has now shown it is not, at the level of approximation those documents actually use. This doesn't mean $\eta_{\rm eq}\ne0$ is wrong — it means the specific value, and possibly the qualitative existence, of $\eta_{\rm eq}$ as computed anywhere in the current corpus has an unstated, unquantified dependence on a choice that was never made explicit. That's a finding for whoever picks up Foundation C or revisits Papers A–C, not something to resolve here.

**`Foundation-B-Result-B2-v1.0` is frozen.** Awaiting direction on whether to open B3 (boson-fluctuation corrections) or pivot to documenting this interpretive consequence for the wider corpus first.
