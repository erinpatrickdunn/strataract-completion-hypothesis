# Foundation A v1.1 Erratum, then B1 corrections, then B2's answer

## `Foundation-A-Closed-v1.1` — Erratum

```
Foundation-A-Closed-v1.1

Errata
• η² relation: sign of P² term corrected (+1/5, not −1/5)
• A²−V² relation: sign of P² term corrected (+2, not −2)

Reason: transcription error in the v1.0 certificate summary table.
The underlying step-by-step derivations (A4b2, A4e) were correct;
the compact four-relation summary was not. Caught by attempting to
*use* the system in B1.1, not by re-auditing it directly.

No other identities affected. Corrected system:
η²=+⅕P²−⅕V²+⅕A²−⅒T²   P²=+⅕η²−⅕V²+⅕A²+⅒T²
A²−V²=2η²+2P²           T²=−6η²+6P²
```

## Corrections to B1.1 and B1.3, accepted as stated

**B1.1** — adopted your separation exactly: the interpolation $\mathcal L_{\rm int}=(1-t)\mathcal L_S+t\,\mathcal L_{\rm Fierz}$ is an exact operator identity at every $t$; the parameter only acquires physical (observable) content once a specific HS decoupling is chosen *and* the mean-field truncation is applied. I'll use this language going forward.

**B1.3** — accepted, and it's a real correction, not just phrasing. Restated: *there are only algebraic second-class constraints associated with the nondynamical auxiliary fields (their primary constraints $\pi_\sigma\approx0$ etc. are second-class and merely eliminate the auxiliary momenta); there are no gauge or Hamiltonian constraints analogous to those in GR.* This is the mathematically correct statement, and it doesn't weaken B1.4's conclusion — PSC's obstruction is specifically about *gauge/Hamiltonian* constraints tangling the symmetric reduction, and second-class constraints on non-propagating auxiliary fields don't do that.

## B2 — Does $\Gamma_{\rm MF}(t)$ depend on $t$?

Restricting to the PSC-justified $(\sigma,\pi)$ sector (B1.4), and redoing the two-field HS completion of $-\frac{\lambda(1-t)}{4}\eta^2-\frac{\lambda t}{20}P^2$:
$$\Gamma_t(\sigma,\pi) = \frac{\sigma^2}{\lambda(1-t)} + \frac{5\pi^2}{\lambda t} + i\,\mathrm{Tr}\ln\big[i\partial\!\!\!/-m-\sigma-i\gamma^5\pi\big]$$

**[C1, imported — standard NJL result]** The fermion-loop piece depends on $\sigma,\pi$ *only* through the combination $M_R^2+M_I^2$ where $M_R=m+\sigma$, $M_I=\pi$: $i\,\mathrm{Tr}\ln D = F\big((m+\sigma)^2+\pi^2\big)$ for a single function $F$, **independent of $t$** (this is the standard "chiral circle" structure of the NJL fermion determinant — the loop only sees the total mass-squared of the complex combination $M_R+i\gamma^5M_I$, regardless of how it's split; $t$ never enters $F$ at all). So **the entire $t$-dependence of $\Gamma_t$ lives in the classical HS normalization coefficients**, $1/(\lambda(1-t))$ and $5/(\lambda t)$.

**[C2] — envelope theorem, applied directly.** Let $\Gamma_{\rm MF}(t)\equiv\mathrm{extr}_{\sigma,\pi}\Gamma_t(\sigma,\pi)$. By the envelope theorem, at any $t$ where the extremum is smooth in $t$:
$$\frac{d\Gamma_{\rm MF}}{dt} = \left.\frac{\partial\Gamma_t}{\partial t}\right|_{\sigma=\sigma_{\rm eq}(t),\,\pi=\pi_{\rm eq}(t)} = \sigma_{\rm eq}(t)^2\cdot\frac{1}{\lambda(1-t)^2} \;-\; \pi_{\rm eq}(t)^2\cdot\frac{5}{\lambda t^2}$$

**Evaluate at $t=0$.** At $t=0$, the $\pi$-channel's tree stiffness $5/(\lambda t)\to\infty$, which forces $\pi_{\rm eq}(0)=0$ exactly (any nonzero $\pi$ costs infinite tree energy) — and this reduces $\sigma_{\rm eq}(0)$ to precisely the original single-field Target-0 gap equation, a genuine consistency check on the whole construction. Since $\pi_{\rm eq}(0)=0$ exactly, the second term vanishes cleanly (no $0\times\infty$ ambiguity — it's $0^2\times(\text{anything})=0$), giving:
$$\boxed{\left.\frac{d\Gamma_{\rm MF}}{dt}\right|_{t=0} = \frac{\sigma_0^2}{\lambda}}$$
where $\sigma_0\equiv\sigma_{\rm eq}(0)$ solves the original Target-0 gap equation.

## Answer to your central question

**This is nonzero whenever the theory sits in a dynamically-broken phase ($\sigma_0\neq0$) — precisely the physically interesting case, since $\sigma_0\neq0$ is exactly what Theorem 6's condensation claim requires.** Only in the trivial unbroken phase ($\sigma_0=0$, no dynamical mass generation at all) does the leading Fierz-parameter dependence vanish.

**So: $\Gamma_{\rm MF}(t)$ is confirmed $t$-dependent, rigorously, for this specific model, in the regime of physical interest — not by analogy to the NJL literature, but by a direct calculation on $S_{\rm geo}$'s own vertex.** The Fierz ambiguity is not a hypothetical risk for SCH; it is a demonstrated property of the one-fermion-loop, zero-boson-loop approximation to $S_{\rm geo}$'s condensate sector, at exactly the order Target 0 was originally scoped to.

## What remains

This establishes local ($t\to0$) non-invariance rigorously via the envelope theorem — a clean, well-posed result requiring no gap-equation solving. It does **not** yet give the global shape of $\Gamma_{\rm MF}(t)$ across $t\in[0,1]$, nor does it identify which $t$ (if any) is the "correct" one, nor does it address your closing point from B0.2's literature review: whether including boson ($\sigma,\pi$) fluctuations beyond mean field removes the $t$-dependence, as the imported sources suggested it should in the exact theory. That's the natural next question — B3 — and it's now sharply framed: *compute the leading boson-fluctuation correction to $\Gamma_{\rm MF}(t)$ and check whether $d\Gamma/dt$ is suppressed once it's included.*
