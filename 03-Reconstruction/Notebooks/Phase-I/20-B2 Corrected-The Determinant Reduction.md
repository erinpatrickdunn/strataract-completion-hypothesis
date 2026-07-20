# B2 Corrected: The Determinant Reduction and the $t\to0^+$ Limit, Both Derived Properly

## Point 3 — the determinant reduction, derived rather than imported

**Trying your suggested route first, and reporting that it doesn't work as stated.** Multiplying $D=i\partial\!\!\!/-M$ by $D'=i\partial\!\!\!/+M$ (same $M$), the cross terms are $i(M\gamma^\mu-\gamma^\mu M)\partial_\mu$, which do **not** vanish: $M=(m+\sigma)+i\gamma^5\pi$ contains $\gamma^5$, and $\{\gamma^\mu,\gamma^5\}=0$ gives $[\gamma^5,\gamma^\mu]=2\gamma^5\gamma^\mu\ne0$. So $[M,\gamma^\mu]=2i\pi\gamma^5\gamma^\mu\ne0$ in general — **the naive companion operator you proposed doesn't cancel the cross-term.** Flagging this rather than silently fixing it, since it's exactly the kind of "the standard trick doesn't transfer automatically" issue this whole reconstruction exists to catch.

**The working route.** Define $\bar M \equiv (m+\sigma)-i\gamma^5\pi$ (flip the sign of the $\pi$ term only, not of $M$ itself). In momentum space, using $\gamma^5\gamma^\mu=-\gamma^\mu\gamma^5$ directly: $p\!\!\!/\bar M = (m+\sigma)p\!\!\!/-i\pi\,p\!\!\!/\gamma^5$ and $Mp\!\!\!/=(m+\sigma)p\!\!\!/+i\pi\gamma^5p\!\!\!/=(m+\sigma)p\!\!\!/-i\pi p\!\!\!/\gamma^5$ (using $\gamma^5p\!\!\!/=-p\!\!\!/\gamma^5$) — **these are equal: $p\!\!\!/\bar M = Mp\!\!\!/$.** So:
$$(p\!\!\!/-M)(p\!\!\!/+\bar M) = p^2 + p\!\!\!/\bar M - Mp\!\!\!/ - M\bar M = p^2 - M\bar M$$
and $M\bar M = (m+\sigma)^2 - (i\gamma^5\pi)^2 = (m+\sigma)^2+\pi^2$ (using $(\gamma^5)^2=1$, $(m+\sigma)$ a number commuting freely). So $(p\!\!\!/-M)(p\!\!\!/+\bar M) = [p^2-(m+\sigma)^2-\pi^2]\cdot\mathbb 1$ — clean, exact.

**Independent cross-check, done directly in explicit matrices (rest frame $p=(E,0,0,0)$, per the Spinor Convention Audit's $\gamma^0=\mathrm{diag}(I,-I)$, $\gamma^5=\begin{pmatrix}0&I\\I&0\end{pmatrix}$):**
$$D = \begin{pmatrix}(E-(m+\sigma))I & -i\pi I\\ -i\pi I & -(E+(m+\sigma))I\end{pmatrix}$$
Block determinant of commuting-block form: $\det D = \big[(E-(m+\sigma))(-(E+(m+\sigma))) - (-i\pi)^2\big]^2 = \big[(m+\sigma)^2-E^2+\pi^2\big]^2 = \big[E^2-(m+\sigma)^2-\pi^2\big]^2$.

**Both routes agree, independently.** With $p^2=E^2$ at rest frame: $\det D = [p^2-(m+\sigma)^2-\pi^2]^2$, confirming $\mathrm{Tr}\ln D = F\big((m+\sigma)^2+\pi^2\big)$ exactly, from $S_{\rm geo}$'s own operator, not imported.

## Points 4/5 — the $t\to0^+$ limit, done properly

**[C2] — the structural fact that resolves the gap directly.** Since $\mathrm{Tr}\ln D$ depends on $\pi$ only through $\pi^2$ (just established), and the tree term $5\pi^2/(\lambda t)$ is likewise even in $\pi$, **$\Gamma_t(\sigma,\pi)$ is exactly invariant under $\pi\to-\pi$, at every $t$** — not an approximation, an exact symmetry of the truncated potential (this is precisely Foundation A's discrete $\mathbb Z_2$ on the $P$-channel, showing up concretely here). Consequently $\partial\Gamma_t/\partial\pi = \pi\big[10/(\lambda t) + 2F'(M^2)\big]$ (chain rule; note this is **linear in $\pi$ times a bracket**, not stiffness-plus-independent-forcing as your heuristic assumed) — **$\pi=0$ is an exact stationary point at every $t$, not merely a limiting statement.** This was the actual gap in my original argument: I asserted $\pi_{\rm eq}(0)=0$ correctly but for the wrong reason (divergent stiffness), when the real reason is this exact symmetry, valid at all $t$.

**Is $\pi=0$ the minimum, not just a critical point?** The second derivative at $\pi=0$ is $10/(\lambda t)+2F'((m+\sigma)^2)$. As $t\to0^+$, the first term diverges to $+\infty$ while $F'((m+\sigma)^2)$ is evaluated at the fixed, finite background value $(m+\sigma_0)^2$ — so **for $t$ below some threshold $t_*$, the divergent positive stiffness term dominates regardless of $F'$'s value, guaranteeing $\pi=0$ is the genuine local minimum**, not merely a symmetric critical point that could be a saddle. This closes exactly the gap you identified: $\pi_{\rm eq}(t)=0$ **exactly**, for all $t<t_*$, hence $\pi_{\rm eq}(t)^2/t^2=0$ **exactly** (not merely in a limit) throughout that range — which certainly covers the $t\to0^+$ neighborhood the envelope-theorem evaluation needs.

$$\boxed{\left.\frac{d\Gamma_{\rm MF}}{dt}\right|_{t=0} = \frac{\sigma_0^2}{\lambda}}$$

**now established rigorously**, with both prior gaps (the unverified determinant reduction, and the unjustified $t\to0^+$ asymptotics) closed by direct computation rather than import or hand-wave.

## One residual item, flagged rather than chased further

The bracket $10/(\lambda t)+2F'(M^2)=0$ *could* have a solution at larger $t$ (once the diverging stiffness no longer dominates), corresponding to a genuine pseudoscalar-condensed ($\pi_{\rm eq}\ne0$) branch competing with the scalar one. Whether that branch exists, and whether it's lower-energy, depends on $F'$ at large argument — which is exactly the UV-divergent, regulator-dependent quantity flagged at Target 0's original halt point. **The two open obstructions in this reconstruction (the regulator choice, and the Fierz-parameter dependence) are not independent** — resolving one may bear on the other, since the shape of $F$ far from the origin governs both the UV divergence structure and whether a competing pseudoscalar vacuum exists. Not pursuing this further now; flagging it as the natural link between B2/B3 and the original Target-0 regulator halt for whenever that's picked back up.

**Status: B2's central claim is now fully established, both previously-flagged gaps closed by direct derivation.** $\Gamma_{\rm MF}(t)$ has confirmed nonzero slope at $t=0$ whenever $\sigma_0\ne0$ — the Fierz/mean-field ambiguity is real for $S_{\rm geo}$'s condensate sector, rigorously, at exactly the approximation order Target 0 was scoped to.
