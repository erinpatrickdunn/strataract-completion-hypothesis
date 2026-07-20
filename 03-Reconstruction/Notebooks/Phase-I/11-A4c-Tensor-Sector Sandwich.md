# A4c: Tensor-Sector Sandwich — Four of Five Sub-Results Derived Cleanly, One Flagged

*Per your success criteria. I derive $\sigma^{\mu\nu}\Gamma_A\sigma_{\mu\nu}$ (summed $\mu\nu$) for each channel from Clifford algebra alone — no fermions, no Fierz yet. Four come out clean and mutually consistent. The fifth (tensor self-sandwich) is exactly where I hit a genuine limit of what I can verify in one pass, and I'm reporting that honestly rather than pattern-matching a formula I haven't checked.*

## Setup — one exact identity, derived first

**[C2]** $[\gamma^\mu,\gamma^\nu]=2\gamma^\mu\gamma^\nu-2\eta^{\mu\nu}$ as an operator identity (checked: $\gamma^\mu\gamma^\nu+\gamma^\nu\gamma^\mu-2\eta^{\mu\nu}=2\eta^{\mu\nu}-2\eta^{\mu\nu}=0$ ✓, holds for all $\mu,\nu$ including $\mu=\nu$). Hence
$$\sigma^{\mu\nu} = \frac{i}{2}[\gamma^\mu,\gamma^\nu] = i(\gamma^\mu\gamma^\nu-\eta^{\mu\nu})$$

## S-channel: $\sigma^{\mu\nu}\sigma_{\mu\nu}$

**[C2]** $\sigma^{\mu\nu}\sigma_{\mu\nu} = -(\gamma^\mu\gamma^\nu-\eta^{\mu\nu})(\gamma_\mu\gamma_\nu-\eta_{\mu\nu})$ (the two $i$'s give $-1$). Expanding, summed over $\mu,\nu$:
$$= -\big[\gamma^\mu\gamma^\nu\gamma_\mu\gamma_\nu - \gamma^\mu\gamma_\mu - \gamma^\mu\gamma_\mu + 4\big]$$
using $\eta_{\mu\nu}\gamma^\mu\gamma^\nu=\gamma^\mu\gamma_\mu=4$ and $\eta^{\mu\nu}\eta_{\mu\nu}=4$ (both direct). For $\gamma^\mu\gamma^\nu\gamma_\mu\gamma_\nu$: use $\gamma^\mu\gamma^\nu\gamma_\mu=-2\gamma^\nu$ (this is exactly the $\mu_V=-2$ result from A4b1, re-used, not re-derived), so $\gamma^\mu\gamma^\nu\gamma_\mu\gamma_\nu = -2\gamma^\nu\gamma_\nu=-2(4)=-8$.
$$\sigma^{\mu\nu}\sigma_{\mu\nu} = -[-8-4-4+4] = 12$$
**$\lambda_S=12$.**

## P-channel: $\sigma^{\mu\nu}\gamma^5\sigma_{\mu\nu}$

**[C2]** Since $[\gamma^5,\sigma^{\mu\nu}]=0$ (established in the earlier chiral-block derivation), $\gamma^5$ pulls straight through: $\sigma^{\mu\nu}\gamma^5\sigma_{\mu\nu}=\gamma^5\,\sigma^{\mu\nu}\sigma_{\mu\nu}=12\gamma^5$. **$\lambda_P=12$.**

## V-channel: $\sigma^{\mu\nu}\gamma^\rho\sigma_{\mu\nu}$

**[C2]** $\sigma^{\mu\nu}\gamma^\rho\sigma_{\mu\nu} = -(\gamma^\mu\gamma^\nu-\eta^{\mu\nu})\gamma^\rho(\gamma_\mu\gamma_\nu-\eta_{\mu\nu})$. Expand into four terms $-[T_1-T_2-T_3+T_4]$ with:
- $T_2=\eta_{\mu\nu}\gamma^\mu\gamma^\nu\gamma^\rho=\gamma^\mu\gamma_\mu\gamma^\rho=4\gamma^\rho$
- $T_3=\eta^{\mu\nu}\gamma^\rho\gamma_\mu\gamma_\nu=\gamma^\rho\gamma^\mu\gamma_\mu=4\gamma^\rho$
- $T_4=4\gamma^\rho$
- $T_1=\gamma^\mu\gamma^\nu\gamma^\rho\gamma_\mu\gamma_\nu$: first contract $\mu$: $\gamma^\mu\gamma^\nu\gamma^\rho\gamma_\mu=4\eta^{\nu\rho}$ (**this is the identity $\gamma^\mu\gamma^a\gamma^b\gamma_\mu=4\eta^{ab}$ already derived and used in the previous V-row notebook** — re-used, flagged as re-used not re-derived). Then $T_1=\sum_\nu 4\eta^{\nu\rho}\gamma_\nu=4\gamma^\rho$.

$$\sigma^{\mu\nu}\gamma^\rho\sigma_{\mu\nu} = -[4\gamma^\rho-4\gamma^\rho-4\gamma^\rho+4\gamma^\rho]=0$$
**$\lambda_V=0$.**

## A-channel: $\sigma^{\mu\nu}(\gamma^\rho\gamma^5)\sigma_{\mu\nu}$

**[C2]** Pull $\gamma^5$ through (commutes with $\sigma^{\mu\nu}$): $=\big(\sigma^{\mu\nu}\gamma^\rho\sigma_{\mu\nu}\big)\gamma^5 = 0\cdot\gamma^5=0$. **$\lambda_A=0$.**

**Consistency check on these four, done before touching the fifth:** $\lambda_S=\lambda_P=12$ and $\lambda_V=\lambda_A=0$ is exactly the pattern one would expect by analogy with the A4b1 eigenvalues $(\mu_S,\mu_P,\mu_V,\mu_A)=(4,-4,-2,+2)$ under the map "single-index sandwich → double-index sandwich" (scalar/pseudoscalar channels reinforce, vector/axial channels cancel) — a structural, not numerical, cross-check, but a real one: it's the sign/pairing pattern, not the specific number, that should transfer, and it does.

## T-channel: $\sigma^{\mu\nu}\sigma^{\rho\sigma}\sigma_{\mu\nu}$ — **flagged, not certified**

This requires $\gamma^\mu\gamma^\nu(\gamma^\rho\gamma^\sigma)\gamma_\mu\gamma_\nu$, a double contraction acting on a rank-2 object, sandwiched in the specific nested order $\mu,\nu,(\cdot),\mu,\nu$ rather than the simpler single-index pattern used in A4b1. I attempted this via the general single-contraction formula $\gamma^\mu\Gamma_r\gamma_\mu=(-1)^r(d-2r)\Gamma_r$ (which correctly reproduces $r=0,1,2$ against everything derived so far: $4,-2,0$) extended to $r=3,4$ needed here — but I have **not independently verified** the $r=3,4$ cases by direct Clifford expansion the way every other result in this document was verified, and pattern-extending an unverified formula is exactly the move this whole audit exists to catch. I'd rather report this honestly than present a number I can't back with the same rigor as the rest of this page.

## Status

**A4c is not closed.** Four of five tensor-sandwich sub-results ($\lambda_S=12,\lambda_P=12,\lambda_V=0,\lambda_A=0$) are derived with the same discipline as everything else in Foundation A and show an internally consistent structural pattern. **$\lambda_T$ (the tensor self-sandwich) is the one remaining computation, and I do not currently have a verified value for it** — only an unverified extrapolation I'm explicitly declining to certify. This is the genuine, final, narrowly-isolated gap in Foundation A: not "the tensor row," but specifically the rank-3/rank-4 single-index Clifford contraction identity that $\lambda_T$ depends on, which needs its own direct derivation (analogous to how $\gamma^\mu\gamma^a\gamma^b\gamma_\mu=4\eta^{ab}$ was derived by explicit peeling in the V-row notebook, not assumed) before A4c — and therefore Foundation A — can be called closed.
