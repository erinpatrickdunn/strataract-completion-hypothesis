# Target 0 Reconstruction: 1PI Effective Potential Γ[η_cl]

Following the Constitution §§1–7 exactly. Every line below is tagged **[C1]**, **[C2]**, or **[C3]**. I use signature $(+,-,-,-)$, $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$, $\bar\psi=\psi^\dagger\gamma^0$ — this convention choice is itself a **[C1]** notational fix, not a physical input.

## 1. Setup

**[C1]** From §P.1.2, flat-space, $S_{\text{matter}}$ excluded:
$$S_{\text{geo}} = \int d^4x\left[\bar\psi(i\gamma^\mu\partial_\mu - m)\psi - \frac{\lambda}{4}(\bar\psi\psi)^2\right]$$
(the symmetrized kinetic term reduces to $\bar\psi i\gamma^\mu\partial_\mu\psi$ after an integration by parts discarding a boundary term — **[C2]**, standard, assumes fields vanish at infinity.)

**[C1]** Source-coupled generating functional (§5(a) of the Constitution):
$$Z[J] = \int\mathcal D\psi\,\mathcal D\bar\psi\;\exp\left\{i\int d^4x\left[\bar\psi(i\partial\!\!\!/-m)\psi - \frac{\lambda}{4}(\bar\psi\psi)^2 + J\,\bar\psi\psi\right]\right\}$$

## 2. Hubbard–Stratonovich linearization

**[C2]** Claim: for any real auxiliary field $\sigma(x)$,
$$\exp\left\{-i\int d^4x\,\frac{\lambda}{4}\eta^2\right\} = \mathcal N^{-1}\int\mathcal D\sigma\,\exp\left\{i\int d^4x\left[\frac{1}{\lambda}\sigma^2-\sigma\eta\right]\right\}$$
**Proof (Gaussian, exact — [C2]):** the $\sigma$-integral is Gaussian; its stationary point is $\delta/\delta\sigma\left[\frac{1}{\lambda}\sigma^2-\sigma\eta\right]=0 \Rightarrow \sigma=\lambda\eta/2$. Since the integrand is exactly quadratic in $\sigma$, completing the square shows the fluctuation piece is $\eta$-independent (absorbed into $\mathcal N$), and the exact on-shell value is
$$\frac{1}{\lambda}\left(\frac{\lambda\eta}{2}\right)^2-\frac{\lambda\eta}{2}\eta=\frac{\lambda\eta^2}{4}-\frac{\lambda\eta^2}{2}=-\frac{\lambda\eta^2}{4},$$
reproducing the quartic term exactly, with no approximation. $\blacksquare$

**[C2]** Substituting into $Z[J]$ and collecting the linear-in-$\eta$ terms ($-\sigma\eta+J\eta$):
$$Z[J] = \mathcal N^{-1}\int\mathcal D\sigma\;e^{i\int(1/\lambda)\sigma^2}\int\mathcal D\psi\,\mathcal D\bar\psi\;\exp\left\{i\int\bar\psi\big(i\partial\!\!\!/-\underbrace{[m+\sigma-J]}_{\equiv\,M(x)}\big)\psi\right\}$$

## 3. Integrating out the fermion

**[C2]** Grassmann Gaussian integral (standard):
$$\int\mathcal D\psi\,\mathcal D\bar\psi\;e^{i\int\bar\psi(i\partial\!\!\!/-M)\psi} = \operatorname{Det}[i\partial\!\!\!/-M] = \exp\big\{\operatorname{Tr}\ln[i\partial\!\!\!/-M]\big\}$$
so
$$Z[J] = \mathcal N^{-1}\int\mathcal D\sigma\;\exp\left\{i\int\frac{\sigma^2}{\lambda} + \operatorname{Tr}\ln\big[i\partial\!\!\!/-m-\sigma+J\big]\right\}$$

## 4. Restriction to the Target-0 ansatz

**[C1]** Per §4/§5, restrict to $\sigma(x)=\bar\sigma$, $J(x)=J$ constant (homogeneous, static, $T=0$). Then $M(x)=M\equiv m+\bar\sigma-J$ is constant, and the trace-log is diagonal in momentum space:
$$\operatorname{Tr}\ln[i\partial\!\!\!/-M] = \Omega\int\frac{d^4p}{(2\pi)^4}\,\operatorname{tr}\ln[p\!\!\!/-M]$$
where $\Omega$ is the (infinite) spacetime volume.

**[C2]** Determinant identity: $\det(p\!\!\!/-M) = (p^2-M^2)^2$ for the $4\times4$ Dirac operator. *Derivation:* $(p\!\!\!/-M)(p\!\!\!/+M)=(p^2-M^2)\mathbb 1_4 \Rightarrow \det(p\!\!\!/-M)\det(p\!\!\!/+M)=(p^2-M^2)^4$; and $\gamma^5(p\!\!\!/-M)\gamma^5=-p\!\!\!/-M$ combined with a parity relation shows $\det(p\!\!\!/-M)=\det(p\!\!\!/+M)$, giving $\det(p\!\!\!/-M)^2=(p^2-M^2)^4$, hence $\det(p\!\!\!/-M)=\pm(p^2-M^2)^2$; the sign is fixed to $+$ by matching the free ($M=0$) massless limit. So $\operatorname{tr}\ln[p\!\!\!/-M] = 2\ln(p^2-M^2+i\epsilon)$.

**[C2]** So, per unit 4-volume, defining $-\Gamma(\bar\sigma,J)/\Omega$ as the exponent's coefficient (standard effective-action normalization):
$$\Gamma(\bar\sigma,J)/\Omega = -\frac{\bar\sigma^2}{\lambda} - i\int\frac{d^4p}{(2\pi)^4}\,2\ln(p^2-M^2+i\epsilon)$$

**[C2]** Wick rotation $p^0\to ip_E^4$, $d^4p\to i\,d^4p_E$, $p^2\to -p_E^2$ (standard) converts the Minkowski phase-integral into a real Euclidean integral, giving the potential energy density
$$V_{\text{1-loop}}(M) = -2\int\frac{d^4p_E}{(2\pi)^4}\,\ln(p_E^2+M^2)$$
so that the full potential, as a function of $M=m+\bar\sigma-J$, at fixed $J$, is
$$V(\bar\sigma) = \frac{\bar\sigma^2}{\lambda} + V_{\text{1-loop}}(m+\bar\sigma-J)$$

## 5. Where this must stop

**[C2] — power counting.** $\int d^4p_E\,\ln(p_E^2+M^2) \sim \int p_E^3\,dp_E\,\ln(p_E^2+M^2)$ diverges as $\Lambda^4$ (field-independent), $\Lambda^2 M^2$ (quadratic), and $M^4\ln\Lambda$ (logarithmic) for a UV cutoff $\Lambda\to\infty$. The integral is **not finite** as written.

**[C2] — dimensional analysis, forced not assumed.** $[\psi]=3/2$ in natural units $\Rightarrow[\bar\psi\psi]=3\Rightarrow[(\bar\psi\psi)^2]=6$. A Lagrangian density has $[\mathcal L]=4$, so $[\lambda]=4-6=-2$: $\lambda$ carries an inverse-mass-squared dimension. This means the quartic vertex in $S_{\text{geo}}$ is, in the ordinary Wilsonian sense, a **non-renormalizable operator** — $S_{\text{geo}}$ as frozen in §1 of the Constitution is only meaningful as an effective theory with an implicit UV cutoff scale, and that scale is *not* one of the two parameters $\{m,\lambda\}$ the action supplies. $\lambda$ alone fixes a mass scale $\Lambda_\lambda\sim\lambda^{-1/2}$ only up to an $O(1)$ factor that is a **choice**, not a derivation.

**This is the halt point required by §7(b).** To obtain a specific $\Gamma[\eta_{\text{cl}}]$ — a specific numerical/functional stationary-point equation for $\eta_{\text{eq}}$ — the calculation requires one of the following, and none is derivable from $S_{\text{geo}}$ as stated:

- **[C3-required]** A regularization scheme (hard 3-momentum cutoff, Pauli–Villars, dimensional regularization + $\overline{\text{MS}}$, proper-time cutoff, …). These schemes give *different finite answers* for the coefficient of the $M^4\ln M^2$ term and for whether an $M^2\Lambda^2$ term is present at all (dim reg removes power divergences by construction; a hard cutoff keeps them).
- **[C3-required]** A value (or a defining relation) for the UV scale $\Lambda$, since $\lambda$ alone under-determines it up to the $O(1)$ ambiguity above.
- **[C3-required]** A renormalization condition fixing the finite part left over after subtraction (e.g., matching $V''(\eta_{\text{eq}})$ to a physical mass at some scale $\mu$).

None of these is a Category-1 definition or a Category-2 derived step; each is a physical choice external to $S_{\text{geo}}$. Per §7(b), the reconstruction halts **here**, precisely at Step 5, and this is reported as the location of the missing bridge rather than papered over with an unlabeled regularization choice.

## 6. What is established up to the halt (Category 2 only)

$$\boxed{\;V(\eta_{\text{eq}}) = \frac{\lambda}{4}\eta_{\text{eq}}^2 \;-\; 2\!\!\underbrace{\int\frac{d^4p_E}{(2\pi)^4}\ln\!\big(p_E^2+(m+\tfrac{\lambda}{2}\eta_{\text{eq}})^2\big)}_{\text{UV-divergent; scheme required}}\;}$$
using the on-shell relation $\bar\sigma_{\text{eq}}=\lambda\eta_{\text{eq}}/2$ from Step 2 (at $J=0$) and $M=m+\bar\sigma_{\text{eq}}$. This much is a fully Category-1/2 consequence of $S_{\text{geo}}$: the *classical* ($\lambda\eta^2/4$, sign **positive**, note) plus a well-defined but divergent one-loop fermion contribution as a specific functional of $M(\eta_{\text{eq}})$.

## 7. Data, not target (§7(c))

Two disagreements with prior Appendix P material surface here and are reported as data:

1. The classical piece obtained here is $+\frac{\lambda}{4}\eta_{\text{eq}}^2$ (positive), matching **§P.9.4.2's** $\rho_{\text{geo}}\ni+\frac{\lambda}{4}\eta^2$ — but *not* matching **Theorem 0/Theorem 6's** narrative of a negative quartic term "competing with" and overcoming the mass term to drive spontaneous condensation. As derived directly from the frozen action, the sign of the $(\bar\psi\psi)^2$ term does not by itself produce a Mexican-hat instability at tree level in $\eta$; Theorem 6's $V_{\text{eff}}=\frac{\mu^2}{2}\eta^2+\frac{\lambda}{4}\eta^4$ (quartic in $\eta$, not quadratic) is a *different functional form* from what this reconstruction obtains from $S_{\text{geo}}$ at tree level ($\lambda\eta^2/4$, quadratic in $\eta$) — the two cannot be directly compared without first resolving the divergence in §5, since it is the loop term, not the tree term, that could in principle generate quartic-in-$\eta$ structure.
2. Whether condensation ($\eta_{\text{eq}}\neq0$) occurs at all is not decidable at this stage: it depends on the sign and magnitude of the regularized $M^2$-divergent piece relative to $+\lambda\eta_{\text{eq}}^2/4$, which is exactly the quantity left undetermined by the halt in §5.

## 8. Formal classification

**Outcome: §7(b) — derivation obstructed.** Reconstruction of Target 0 is complete through Step 4 (a valid, fully Category-1/2 chain from $S_{\text{geo}}$ to a specific-but-divergent expression for $V(\eta_{\text{eq}})$). It cannot proceed to a stationary-point equation $\eta_{\text{eq}}=\eta_{\text{eq}}(m,\lambda)$ without a regularization/renormalization choice that is a Category-3 hypothesis not supplied by $S_{\text{geo}}$ as frozen.

If you want, the natural next move is to make that Category-3 choice *explicitly* (e.g. state "we hypothesize a hard 3-momentum cutoff at $\Lambda\equiv c/\sqrt\lambda$" as a labeled Category-3 assumption) and continue — but that is a decision for you to make, not one this reconstruction is entitled to make silently.
