# A4d: Tensor Normalization Audit — The Obvious Fix Doesn't Work

*Per your three questions. I traced the normalization convention all the way through, expecting to find the 1/2-vs-double-counting mismatch you flagged as the prime suspect. I did not find it there. The discrepancy survives, now isolated to a narrower and more specific location than before.*

## Q1: Orthonormal tensor basis

**[C2]** $\Gamma_A^{\text{tensor}} = \sigma^{\mu\nu}$, $\mu<\nu$ — six independent generators. Standard bilinear notation $T^{\mu\nu}T_{\mu\nu}$ sums over **all** sixteen ordered $(\mu,\nu)$ pairs (the usual tensor-contraction convention), which counts each of the six independent generators **twice** (since $\sigma^{\nu\mu}=-\sigma^{\mu\nu}$ and $\sigma^{\nu\mu}\sigma_{\nu\mu}=\sigma^{\mu\nu}\sigma_{\mu\nu}$, verified directly below).

## Q2: $\mathrm{Tr}(\sigma^{\mu\nu}\sigma^{\rho\sigma})$, derived explicitly (not previously done)

**[C2]** Using $[\gamma^\mu,\gamma^\nu]=2(\gamma^\mu\gamma^\nu-\eta^{\mu\nu})$ and the standard four-gamma trace $\mathrm{Tr}(\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=4(\eta^{\mu\nu}\eta^{\rho\sigma}-\eta^{\mu\rho}\eta^{\nu\sigma}+\eta^{\mu\sigma}\eta^{\nu\rho})$, direct expansion gives:
$$\mathrm{Tr}(\sigma^{\mu\nu}\sigma^{\rho\sigma}) = 4\big(\eta^{\mu\rho}\eta^{\nu\sigma}-\eta^{\mu\sigma}\eta^{\nu\rho}\big)$$
**Direct spot-check against explicit matrices** (Dirac representation, $\sigma^{01}=i\gamma^0\gamma^1$): $(\sigma^{01})^2 = -\gamma^0\gamma^1\gamma^0\gamma^1 = \gamma^0\gamma^0\gamma^1\gamma^1=(1)(-1)=-1$, so $\mathrm{Tr}(\sigma^{01}\sigma^{01})=-4$. Formula: $4(\eta^{00}\eta^{11}-\eta^{01}\eta^{10})=4((1)(-1)-0)=-4$. **Match.** ✓

Summing all 16 ordered pairs: $\mathrm{Tr}(\sigma^{\mu\nu}\sigma_{\mu\nu})=4(\eta^\mu_\mu\eta^\nu_\nu-\eta^\mu_\nu\eta^\nu_\mu)=4(16-4)=48$. Each of the six independent generators contributes equally (checked at both $(0,1)$ and $(1,2)$: both give $\mathrm{Tr}(\sigma^{\mu\nu}\sigma_{\mu\nu})=+4$ individually, matching $6\times 4\times 2=48$ with the factor-of-2 double-count from summing both orderings). **So each independent tensor generator is normalized to trace $4$ — identical to every other channel's per-generator normalization.** This directly answers your suspicion: **the basic completeness-relation normalization is not the problem.** The "$1/2$" in the standard relation is exactly and only the compensation for summing over all 16 ordered pairs instead of the 6 independent ones — nothing more exotic.

## Q3: Re-deriving the $1/2$, and applying it consistently to the T-row

**[C2]** I re-derived, rather than assumed, that $\sum_{\mu<\nu}(\cdots) = \frac12\sum_{\text{all }\mu\nu}(\cdots)$ for any tensor-symmetric combination — this follows immediately from the doubling just verified in Q2, and is exactly the origin of the completeness relation's $\frac12$.

**Applying this with full explicit bookkeeping to the T-row (the actual check you asked for):** Setting $\Gamma^{(1)}=\sigma^{\rho\sigma}$, $\Gamma^{(2)}=\sigma_{\rho\sigma}$ (summed over **all** $\rho,\sigma$, matching the standard $T^2=T^{\rho\sigma}T_{\rho\sigma}$ definition exactly), the self-Fierz formula gives, for the tensor channel's self-contribution:
$$T^2 \ni -\frac14\cdot\frac12\Big[\sum_{\rho\sigma}\sigma^{\rho\sigma}\sigma^{\mu\nu}\sigma_{\rho\sigma}\Big]\otimes\sigma_{\mu\nu}$$
where the bracketed quantity, summed over **all** $\rho,\sigma$ (not just $\rho<\sigma$) is exactly $\lambda_T$ as I computed it in A4c ($\lambda_T=4$). **This confirms the $\tfrac12\lambda_T$ combination — i.e. $-\tfrac14\cdot\tfrac12\cdot4=-\tfrac12$ — was already applied correctly and consistently in A4c; there was no missing or doubled $\tfrac12$.** I re-derived this independently here and it reproduces exactly $T^2=-2\eta^2+2\tilde P^2$, the same result as before.

**So the "obvious suspect" is ruled out, cleanly.** The normalization bookkeeping between the completeness relation's tensor slot and the full-index-sum convention for $T^2$ is self-consistent; re-deriving it from scratch here reproduces the identical coefficient. The factor-of-3 disagreement against the S/P-row-derived $T^2=-6\eta^2+6\tilde P^2$ is **not** explained by tensor multiplicity bookkeeping.

## Where this leaves things

I have ruled out the leading hypothesis, not confirmed it. The discrepancy is now narrowed to exactly two remaining candidates, both more specific than "the tensor normalization":

1. **An error in $\lambda_T=4$ itself** (the A4c Clifford computation) — I did not get a second independent derivation of this number, exactly the gap flagged last time, and it remains the least-verified single number in the whole chain.
2. **An error in $\lambda_S=\lambda_P=12$**, which feed the S-row/P-row side of the comparison and which I have *not* independently cross-checked the way $\lambda_V,\lambda_A$ were cross-checked against each other — they came from one Clifford expansion each, sharing the same intermediate ($\sum\gamma^\mu\gamma^\nu\gamma_\mu\gamma_\nu=-8$) that also feeds directly into $\lambda_T$'s derivation. **If that shared intermediate is wrong, it would propagate into $\lambda_S,\lambda_P,$ and $\lambda_T$ simultaneously** — which is exactly the kind of single-point-of-failure your A4.5 criterion exists to catch, and which I have not yet isolated.

I'm not going to guess which. The next honest move is a second, independent derivation of $\sum_{\mu\nu}\gamma^\mu\gamma^\nu\gamma_\mu\gamma_\nu=-8$ itself — by direct explicit-matrix computation rather than algebraic peeling — since that single intermediate result is now the common ancestor of every number in the current contradiction.
