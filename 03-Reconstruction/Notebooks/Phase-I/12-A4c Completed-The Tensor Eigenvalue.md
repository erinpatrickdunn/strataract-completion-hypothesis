# A4c Completed: The Tensor Eigenvalue, Full Matrix, and the Involution Check

*I did not take the Schur's-lemma shortcut as literally "pick one basis vector and read off a known coefficient" — instead I used the equivalent but fully explicit route: treat $\sigma^{\rho\sigma}=i(\gamma^\rho\gamma^\sigma-\eta^{\rho\sigma})$ as before and expand the triple product directly, term by term, exactly as every other channel in this document was done. This keeps the derivation in the same style as A4b1/A4b2 rather than importing a representation-theory shortcut I haven't independently earned within this notebook.*

## Deriving $\lambda_T$

**[C2]** Write $X=\gamma^\mu\gamma^\nu-\eta^{\mu\nu}$, $Y=\gamma^\rho\gamma^\sigma-\eta^{\rho\sigma}$ (fixed $\rho\ne\sigma$), $Z=\gamma_\mu\gamma_\nu-\eta_{\mu\nu}$, so $\sigma^{\mu\nu}\sigma^{\rho\sigma}\sigma_{\mu\nu}=-i\sum_{\mu\nu}XYZ$ ($i^3=-i$). Expanding and collecting the four cross-terms with $\eta_{\mu\nu}\gamma^\mu\gamma^\nu=\eta^{\mu\nu}\gamma_\mu\gamma_\nu=4$, $\eta^{\mu\nu}\eta_{\mu\nu}=4$ (all direct):
$$\sum_{\mu\nu}XYZ = \sum_{\mu\nu}\gamma^\mu\gamma^\nu Y\gamma_\mu\gamma_\nu - 4Y$$

**Inner contraction, using A4b1's $\mu_T=0$ result:** $\gamma^\nu(\gamma^\rho\gamma^\sigma)\gamma_\nu = \gamma^\nu(-i\sigma^{\rho\sigma}+\eta^{\rho\sigma})\gamma_\nu = -i(0)+4\eta^{\rho\sigma}=4\eta^{\rho\sigma}$ — a pure number for fixed $\rho\sigma$. Then the outer contraction: $\sum_\mu\gamma^\mu(4\eta^{\rho\sigma})\gamma_\mu = 4\eta^{\rho\sigma}\cdot4=16\eta^{\rho\sigma}$.

Combined with the already-derived $\sum_{\mu\nu}\gamma^\mu\gamma^\nu\gamma_\mu\gamma_\nu=-8$ (S-channel intermediate, reused):
$$\sum_{\mu\nu}\gamma^\mu\gamma^\nu Y\gamma_\mu\gamma_\nu = 16\eta^{\rho\sigma} - \eta^{\rho\sigma}(-8) = 24\eta^{\rho\sigma}$$
$$\sum XYZ = 24\eta^{\rho\sigma}-4(\gamma^\rho\gamma^\sigma-\eta^{\rho\sigma}) = 28\eta^{\rho\sigma}-4\gamma^\rho\gamma^\sigma$$

Converting back via $\gamma^\rho\gamma^\sigma=-i\sigma^{\rho\sigma}+\eta^{\rho\sigma}$: $\sum XYZ = 24\eta^{\rho\sigma}+4i\sigma^{\rho\sigma}$, so
$$\sigma^{\mu\nu}\sigma^{\rho\sigma}\sigma_{\mu\nu} = -i(24\eta^{\rho\sigma}+4i\sigma^{\rho\sigma}) = 4\sigma^{\rho\sigma} - 24i\eta^{\rho\sigma}$$
**For the physical (antisymmetric, $\rho\ne\sigma$) case, $\eta^{\rho\sigma}=0$ identically, so the second term vanishes and:**
$$\boxed{\lambda_T = 4}$$

**Consistency note:** I attempted a second route (the Schur's-lemma shortcut you suggested — direct evaluation on $\sigma^{01}$ using the explicit Dirac matrices from the Spinor Convention Audit) as a cross-check but ran out of room to carry it through the full six-bivector sum in this pass; I'm reporting $\lambda_T=4$ from the single completed derivation above, **not yet double-derived**, and flagging that as the honest status rather than claiming A4.5-level confirmation for this one number.

## Assembling and checking $F^2=\mathbb 1$

Using $(\lambda_S,\lambda_P,\lambda_V,\lambda_A,\lambda_T)=(12,12,0,0,4)$ in the self-Fierz formula for $\Gamma^{(1)}=\Gamma^{(2)}=\sigma^{\rho\sigma}$ (with the same built-in axial-slot minus sign, and the tensor channel's own $\tfrac12$ multiplicity factor from the original completeness relation, carried through unchanged from Notebook 2):
$$T^2 = -\frac14\Big[12\eta^2+12P^2+0-0+\frac12(4)T^2\Big] = -3\eta^2-3P^2-\frac12T^2$$
$$\Rightarrow\ \frac32T^2=-3\eta^2-3P^2 \ \Rightarrow\ T^2=-2\eta^2-2P^2=-2\eta^2+2\tilde P^2$$

**Compare against the previously-derived S+P relation:** $T^2=-6\eta^2+6\tilde P^2$. **These disagree** ($-2,+2$ vs. $-6,+6$) — by exactly a factor of 3, not a factor matching the earlier resolved $1/25$ artifact.

## Honest final status

I do not certify $F^2=\mathbb1$. The T-row, derived independently here, contradicts the S/P-row prediction for $T^2$ by a clean factor of 3 — clean enough to suggest a specific, findable bookkeeping error (most likely in how the tensor channel's multiplicity/normalization factor, mentioned in your review as "six generators, not five equal blocks," enters the self-Fierz formula's $\Gamma^{(1)}\Gamma_A\Gamma^{(2)}$ step versus how it entered the plain completeness relation) — but I have not located it, and I am not going to force-fit the coefficient to make the two sides match.

**A4c is not closed.** What is now established: $\lambda_T=4$ from one clean derivation (not yet cross-verified), and a *specific, quantified* inconsistency between the T-row and the S/P-rows — the same species of problem as the earlier $1/25$ episode, but this time I can't yet attribute it to an obvious truncation error, since this check used the actual T-row equation, not a frozen sub-block. The multiplicity-factor concern you raised in your last review (tensor channel = 6 components, not a simple 5th slot) is my leading suspect and the next thing to check before anything else in Foundation A.
