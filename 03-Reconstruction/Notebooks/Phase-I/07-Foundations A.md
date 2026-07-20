# Foundations A: Algebraic Structure of the SCH Fermion Sector
*Working document — closure status assessed against the A1–A5 exit criteria*

---

## A1. Conventions — closed, with one addition

**[C1]** Metric $(+,-,-,-)$; Clifford algebra $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$; Dirac representation as previously fixed; $\gamma^5=i\gamma^0\gamma^1\gamma^2\gamma^3$; Dirac adjoint $\bar\psi=\psi^\dagger\gamma^0$.

**[C1] — added here:** Levi-Civita convention $\varepsilon_{0123}=+1$, hence $\varepsilon^{0123}=\eta^{00}\eta^{11}\eta^{22}\eta^{33}\varepsilon_{0123}=(1)(-1)(-1)(-1)(+1)=-1$. This fixes the sign in any future dual-tensor definition ($\sigma^{\mu\nu}$ duals, $\tilde T^{\mu\nu}$) and was not previously stated. **A1 is now closed** — no further ambiguity identified.

## A2. Reality/Hermiticity/discrete symmetries

**[C2] — Hermiticity table**, carried forward as previously derived (explicit matrix computation, §3–5 of the prior document): $\eta,V^\mu,A^\mu,T^{\mu\nu}$ Hermitian/real; $P=\bar\psi\gamma^5\psi$ anti-Hermitian/imaginary; real field is $\tilde P \equiv iP$.

**[C2] — parity, derived here, not before.** Under $\psi(x)\to\psi_P(x')=\gamma^0\psi(x)$, $x'=(t,-\mathbf x)$: using $\bar\psi_P(x')=\bar\psi(x)\gamma^0$ (from $\psi^\dagger=\bar\psi\gamma^0$),
$$\eta_P(x')=\bar\psi\gamma^0\gamma^0\psi=\eta(x)\quad\text{(scalar, even)}$$
$$\tilde P_P(x') = i\bar\psi\gamma^0\gamma^5\gamma^0\psi = i\bar\psi(-\gamma^5)\psi=-\tilde P(x)\quad\text{(pseudoscalar, odd — confirms the name)}$$
$$V^0_P=V^0,\ \ V^i_P=-V^i \qquad A^0_P=-A^0,\ \ A^i_P=A^i$$
all obtained by the same $\gamma^0\Gamma\gamma^0$ conjugation, computed explicitly rather than assumed.

**This is a genuine, useful result, not just bookkeeping:** it retroactively *justifies* Theorem 2's assumption "parity symmetry enforces $P=0$" — since $\tilde P$ is now shown to be parity-odd, a parity-symmetric vacuum forces $\langle\tilde P\rangle=0$ by the ordinary odd-function argument. That claim in Appendix P was previously asserted; it is now derived.

**Not done — genuine gap in A2:** charge conjugation and time reversal for all five bilinear classes. These require fixing a $C$-matrix ($C\gamma^{\mu T}C^{-1}=-\gamma^\mu$ or equivalent) and an antiunitary $T$ operation, neither of which has been touched. **A2 is not closed.** This matters concretely: Theorem 6's Landau-theory argument invokes only parity (now justified), but any future claim about $CP$ or $T$ properties of the condensate (e.g. in the chirality-inversion sector, §P.7.7) is currently unaudited.

## A3. Chiral transformation — full block structure, derived

**[C2]** Under $\psi\to e^{i\alpha\gamma^5}\psi$, direct computation (using $\{\gamma^5,\gamma^\mu\}=0$, $[\gamma^5,\sigma^{\mu\nu}]=0$, both established in A2's algebra) gives $\bar\psi\to\bar\psi e^{i\alpha\gamma^5}$, and:

$$\eta' = \cos2\alpha\,\eta+\sin2\alpha\,\tilde P,\qquad \tilde P' = -\sin2\alpha\,\eta+\cos2\alpha\,\tilde P$$

**[C2] — verified as a genuine $SO(2)$ representation:** the matrix $R(2\alpha)=\begin{pmatrix}c&s\\-s&c\end{pmatrix}$ satisfies $RR^T=\mathbb1$, $\det R=1$, and $\eta'^2+\tilde P'^2=\eta^2+\tilde P^2$ (checked by direct substitution) — confirming $\eta^2+\tilde P^2$, **not** $\eta^2+P^2$, is the chirally invariant combination. This is a precision correction to every earlier notebook's loose use of "$P$" in the invariance statement.

**[C2]** $V^\mu$ invariant ($\gamma^\mu$ anticommutes with $\gamma^5$ once on each side, cancelling); $A^\mu$ invariant (same mechanism, one extra cancellation from $\gamma^\mu\gamma^5$'s own anticommutation with $\gamma^5$) — both shown by explicit conjugation, not quoted from memory. This matches the standard chiral-multiplet pattern (vector and axial currents inert under $U(1)_A$; scalar/pseudoscalar rotate).

**[C2, partial]** $T^{\mu\nu}\to\cos2\alpha\,T^{\mu\nu}+i\sin2\alpha\,(\bar\psi\gamma^5\sigma^{\mu\nu}\psi)$ — the tensor mixes into a dual pseudotensor by the identical mechanism as $\eta\leftrightarrow\tilde P$. **Not verified:** whether $\gamma^5\sigma^{\mu\nu}$'s bilinear needs its own $i$-compensation to be real (plausible by analogy with $P\to\tilde P$, but not checked). Flagged as open.

**A3 verdict:** closed for $(\eta,\tilde P)$ and $(V^\mu,A^\mu)$; open for the tensor sector.

## A4. Fierz matrix — attempted, and a genuine inconsistency was found

**[C1, imported — this is the one master identity, per the Constitution's allowance]** the general Fierz sandwich formula, for any two matrices $\Gamma^{(1)},\Gamma^{(2)}$ in the trace-orthonormal basis $\{\Gamma^A\}$ (Tr$[\Gamma^A\Gamma_B]=4\delta^A_B$):
$$\Gamma^{(1)}_{ij}\Gamma^{(2)}_{kl} = \frac14\sum_A\big(\Gamma^{(1)}\Gamma^A\Gamma^{(2)}\big)_{il}(\Gamma_A)_{kj}$$
**[C2] — checked, not just imported:** setting $\Gamma^{(1)}=\Gamma^{(2)}=\mathbb1$ reproduces exactly the completeness relation used in the S-row derivation. This is a real consistency check on the imported formula, not a bare assertion.

**S-row, redone in real fields [C2]:**
$$\eta^2 = \frac15\tilde P^2-\frac15V^2+\frac15A^2-\frac1{10}T^2$$

**P-row, derived here for the first time [C2].** Applying the sandwich formula with $\Gamma^{(1)}=\Gamma^{(2)}=\gamma^5$: since $\gamma^5$ anticommutes with $\gamma^\mu,\gamma^\mu\gamma^5$ (sign flip on conjugation) but commutes with $\mathbb1,\gamma^5,\sigma^{\mu\nu}$ (no flip):
$$(\gamma^5)_{ij}(\gamma^5)_{kl}=\frac14\big[\mathbb1_{il}\mathbb1_{kj}+(\gamma^5)_{il}(\gamma^5)_{kj}-(\gamma^\mu)_{il}(\gamma_\mu)_{kj}+(\gamma^\mu\gamma^5)_{il}(\gamma_\mu\gamma^5)_{kj}+\tfrac12(\sigma^{\mu\nu})_{il}(\sigma_{\mu\nu})_{kj}\big]$$
Grassmann reassembly (verified by explicit transposition count: the four-fermion reordering is an even permutation, no extra sign — checked, not assumed) gives $P^2=-\frac15\eta^2+\frac15V^2-\frac15A^2-\frac1{10}T^2$, hence in real fields ($P=-i\tilde P$, $P^2=-\tilde P^2$):
$$\tilde P^2 = \frac15\eta^2-\frac15V^2+\frac15A^2+\frac1{10}T^2$$

**The involution check — performed, and it fails.** Substituting the $\tilde P^2$ identity back into the $\eta^2$ identity (apply Fierz twice; should return the original $\eta^2$ with coefficient $1$):
$$\eta^2 = \frac15\Big[\frac15\eta^2-\frac15V^2+\frac15A^2+\frac1{10}T^2\Big]-\frac15V^2+\frac15A^2-\frac1{10}T^2$$
The $\eta^2$ coefficient on the right comes out to $\boxed{1/25}$, not $1$.

**This is a genuine, located failure, not a rounding issue.** Per the exit criteria's own instructions, I am reporting it rather than adjusting a sign to make it come out right. Three candidate sources, none yet isolated:
1. An error in my application of the general sandwich formula's normalization (the $\frac14$ prefactor, or a missing overall sign convention for repeated/self-Fierzing of identical operators — self-Fierz of $\Gamma^{(1)}=\Gamma^{(2)}$ may carry a subtlety the general two-different-matrices formula doesn't warn about).
2. An error already present in Notebook 2's original S-row (imported without re-derivation from the master sandwich formula until just now).
3. An error in the Grassmann-reordering sign-counting, despite the explicit transposition count above.

**A4 verdict: not closed, and the specific failure point is now isolated** — narrower than before ("some coefficient might be off") to "the $\eta$–$\tilde P$ 2×2 sub-block, closed under repeated Fierzing, fails involution by a factor of 25," which is a concrete, debuggable target rather than a vague concern.

## A5. Canonical identities appendix

**Not started**, correctly — it is a compilation task and everything in A4 is still provisional.

---

## Overall verdict

**Foundation A is not closed.** A1 is closed. A2 is closed for parity, open for C/T. A3 is closed for the $(\eta,\tilde P)$ and $(V,A)$ sectors, open for the tensor sector. A4 — the centerpiece — is not closed, and the involution check you specified as the acceptance test caught a real, specific, quantified inconsistency (factor of 25) rather than confirming the matrix.

**Recommended next unit of work:** before touching V/A/T rows or the tensor chiral block, resolve the involution failure in the 2×2 $(\eta,\tilde P)$ sub-block. This is now the smallest possible reproduction of the problem — two rows, one check, one numerical discrepancy — and is exactly the kind of isolated, falsifiable target the whole reconstruction has been converging toward. I have not attempted to fix it in this document, since guessing at a correction without finding the actual error would reintroduce the same discipline failure this whole process has been designed to catch.
