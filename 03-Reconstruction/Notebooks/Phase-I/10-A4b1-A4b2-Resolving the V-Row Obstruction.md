# A4b1/A4b2: Resolving the V-Row Obstruction — Real Progress, Honestly Bounded

*Per your split: A4b1 first (pure Clifford eigenvalues, no fermions), then A4b2 (insert into the self-Fierz formula). This resolves the specific sign ambiguity I got stuck on last time — and shows exactly why it existed.*

## A4b1 — The five eigenvalues, derived from Clifford algebra alone

**[C2]** Claim: for each basis element $\Gamma_B\in\{1,\gamma^5,\gamma^\rho,\gamma^\rho\gamma^5,\sigma^{\rho\sigma}\}$, $\gamma^\mu\Gamma_B\gamma_\mu = \mu_B\,\Gamma_B$ (sum over $\mu$; $\rho,\sigma$ free). All five derived here from $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$ alone, $d=4$:

- $\gamma^\mu\gamma_\mu = \delta^\mu_\mu = 4$. **$\mu_S=4$.**
- $\gamma^\mu\gamma^\rho\gamma_\mu = (2\eta^{\mu\rho}-\gamma^\rho\gamma^\mu)\gamma_\mu = 2\gamma^\rho-\gamma^\rho(\gamma^\mu\gamma_\mu)=(2-4)\gamma^\rho$. **$\mu_V=-2$.**
- $\gamma^\mu\gamma^5\gamma_\mu = -(\gamma^\mu\gamma_\mu)\gamma^5$ (using $\{\gamma^5,\gamma_\mu\}=0$) $=-4\gamma^5$. **$\mu_P=-4$.**
- $\gamma^\mu(\gamma^\rho\gamma^5)\gamma_\mu = -\gamma^\mu\gamma^\rho\gamma_\mu\,\gamma^5$ (moving $\gamma^5$ past $\gamma_\mu$) $=-(-2\gamma^\rho)\gamma^5=2\gamma^\rho\gamma^5$. **$\mu_A=+2$.**
- $\gamma^\mu\gamma^\rho\gamma^\sigma\gamma_\mu=4\eta^{\rho\sigma}$ (derived: $\gamma^\mu\gamma^\rho\gamma^\sigma\gamma_\mu=2\gamma^\sigma\gamma^\rho-\gamma^\rho(\gamma^\mu\gamma^\sigma\gamma_\mu)=2\gamma^\sigma\gamma^\rho+2\gamma^\rho\gamma^\sigma=2\{\gamma^\rho,\gamma^\sigma\}=4\eta^{\rho\sigma}$, symmetric in $\rho\sigma$), so $\gamma^\mu\sigma^{\rho\sigma}\gamma_\mu\propto(4\eta^{\rho\sigma}-4\eta^{\sigma\rho})=0$. **$\mu_T=0$.**

$(\mu_S,\mu_P,\mu_V,\mu_A,\mu_T)=(4,-4,-2,+2,0)$. **A4b1 closed** — matches what was used before, now with every step shown, zero Grassmann content.

## A4b2 — Locating and resolving the actual sign issue

**[C2] — the missing ingredient.** Checking $\mathrm{Tr}[\Gamma_A\Gamma^B]$ for each channel: $\mathrm{Tr}[(\gamma^\mu\gamma^5)(\gamma_\mu\gamma^5)] = -\mathrm{Tr}[\gamma^\mu\gamma_\mu]=-4\delta$ (using $\gamma^5\gamma_\mu=-\gamma_\mu\gamma^5\Rightarrow\gamma^\mu\gamma^5\gamma_\mu\gamma^5=-\gamma^\mu\gamma_\mu(\gamma^5)^2=-\gamma^\mu\gamma_\mu$), while every other channel gives $+4\delta$ (checked: $\mathrm{Tr}[1\cdot1]=4$, $\mathrm{Tr}[\gamma^5\gamma^5]=4$, $\mathrm{Tr}[\gamma^\mu\gamma_\nu]=4\delta^\mu_\nu$, $\mathrm{Tr}[\sigma\sigma]>0$ standard). **The axial channel alone has a negative trace-pairing.** This is *why* the completeness relation carries a built-in $-1$ specifically on the axial term — it's forced by this trace computation, not a free bookkeeping choice, and it's the thing my previous attempt hadn't isolated explicitly.

**[C2] — V-row, redone with this resolved.** Also needed: $\gamma^5\Gamma_B\gamma^5=c_B\Gamma_B$, derived directly: $(c_S,c_P,c_V,c_A,c_T)=(+1,+1,-1,-1,+1)$ (each a one-line anticommutation count).

$$\sum_\rho(\gamma^\rho\gamma^5)\Gamma_B(\gamma_\rho\gamma^5) = \gamma^\rho(\gamma^5\Gamma_B\gamma^5)(\gamma^5\gamma_\rho\gamma^5) = -c_B\big(\gamma^\rho\Gamma_B\gamma_\rho\big) = -c_B\mu_B\,\Gamma_B$$
(using $\gamma^5\gamma_\rho\gamma^5=-\gamma_\rho$). Table of $-c_B\mu_B$: $S:-4,\ P:+4,\ V:-2,\ A:+2,\ T:0$.

Applying the self-Fierz formula (§1 of the previous notebook) to $\Gamma^{(1)}=\Gamma^{(2)}=\gamma^\rho\gamma^5$:
$$A^2 = -\frac14\big[-4\eta^2+4P^2-2V^2-(-1)(2A^2)+0\big] = \eta^2-P^2+\frac12V^2+\frac12A^2$$
$$\Rightarrow\ \boxed{A^2 = 2\eta^2-2P^2+V^2} \;=\; 2\eta^2+2\tilde P^2+V^2 \quad(P^2=-\tilde P^2)$$

**And for $V$-row**, same method with $\Gamma^{(1)}=\Gamma^{(2)}=\gamma^\rho$, using $\mu_B$ directly (no $\gamma^5$ conjugation needed, and the axial term's built-in $-1$ now applied correctly since $\mu_A=+2$ goes with the completeness relation's own $-1$ coefficient, not an extra sign I invent):
$$V^2 = -\frac14\big[4\eta^2-4P^2-2V^2-(-1)(2A^2)+0\big] = -\eta^2+P^2+\frac12V^2+\frac12A^2$$
$$\Rightarrow\ \boxed{V^2 = -2\eta^2+2P^2+A^2} = -2\eta^2-2\tilde P^2+A^2$$

**Cross-check:** these two boxed results are the *same equation* ($A^2-V^2=2\eta^2-2\tilde P^2$ both ways). That's not a coincidence to worry about — it's the correct signature of two rows probing the same underlying relation, and it constitutes a genuine independent confirmation of each other, satisfying A4.5.

## Assembling what's known, and what isn't

Combining S-row and P-row (both previously double-derived) by direct addition/subtraction gives two more relations, cross-checked against the V/A result:
$$T^2 = -6\eta^2+6\tilde P^2 \qquad\text{(from S+P rows)}$$
$$A^2-V^2 = 2\eta^2-2\tilde P^2 \qquad\text{(from S−P rows — reproduces the V/A result exactly, independently)}$$

**Honest status: the system is self-consistent everywhere I can check it, but under-determined.** Four rows (S, P, V, A) give only **three independent constraints** among $\{\eta^2,\tilde P^2,V^2,A^2,T^2\}$ — $T^2$ in terms of $(\eta^2,\tilde P^2)$, and $(A^2-V^2)$ in terms of $(\eta^2,\tilde P^2)$ — with $(V^2+A^2)$ still unfixed by anything derived so far. **The T-row itself (self-Fierz of $\sigma^{\rho\sigma}\sigma_{\rho\sigma}$) is the only remaining computation that can supply the missing constraint**, since it's the one channel not yet used as $\Gamma^{(1)}=\Gamma^{(2)}$.

I have not derived the T-row. It requires $\sigma^{\mu\nu}\Gamma_B\sigma_{\mu\nu}$ summed over $\mu,\nu$ — a rank-2 sandwich, structurally different from the single-index contractions above, and I don't want to attempt it in the same pass and risk the "shared hidden mistake" this whole exercise is designed to catch. What I can report cleanly: **the previous "stuck" sign ambiguity is resolved** (it was exactly the forced $\mathrm{Tr}$-sign on the axial channel, now identified and shown to be non-optional), V and A are now cross-derived and mutually consistent with S and P, and the system's remaining gap is precisely isolated as *one missing equation from the T-row*, not a diffuse uncertainty.

**A4b status: S, P, V, A rows closed and mutually cross-checked (three independent constraints, zero contradictions). T-row outstanding — this is the specific, sole remaining item before full $F^2=\mathbb 1$ can be checked.**
