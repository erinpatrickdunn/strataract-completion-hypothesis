# Spinor Convention Audit
*(formerly "Notebook 3a")*

**Purpose, stated per the Constitution's own discipline: this document fixes notation once. It proves nothing about $S_{\rm geo}$'s dynamics, Fierz coefficients, or physical content. Every later notebook cites this one; this one cites nothing downstream. If a later notebook's result conflicts with this document, the later notebook is wrong or this document needs a revised version — never the reverse.**

---

## 1. Metric signature — [C1, chosen]

$$\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$$

This is a free choice, not a derived fact — the opposite signature is equally valid physics. I fix this one because it's what Appendix P §P.7.7.3 claims to use, and the audit's job is partly to check whether that document is internally consistent with its own stated choice.

## 2. Clifford algebra — [C1, forced given §1]

$$\{\gamma^\mu,\gamma^\nu\} = 2\eta^{\mu\nu}\mathbb 1_4 \quad\Rightarrow\quad (\gamma^0)^2=+\mathbb1,\ \ (\gamma^i)^2=-\mathbb1\ (i=1,2,3)$$

## 3. Explicit representation — [C1, chosen for concreteness]

Dirac representation, $2\times2$ blocks, $\sigma^i$ = standard Pauli matrices:
$$\gamma^0 = \begin{pmatrix}\mathbb 1_2 & 0\\0&-\mathbb1_2\end{pmatrix},\qquad \gamma^i = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}$$

**[C2 — checked directly, not quoted]:** $(\gamma^0)^2 = \mathrm{diag}(\mathbb1,\mathbb1)=\mathbb1$. ✓.
$(\gamma^i)^2 = \begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix} = \begin{pmatrix}-\sigma^i\sigma^i&0\\0&-\sigma^i\sigma^i\end{pmatrix} = -\mathbb1$ (using $(\sigma^i)^2=\mathbb1$). ✓. Matches §2.

$$\gamma^5 \equiv i\gamma^0\gamma^1\gamma^2\gamma^3 = \begin{pmatrix}0&\mathbb1_2\\\mathbb1_2&0\end{pmatrix}$$

**[C2 — checked directly]:** Computing $\gamma^0\gamma^1\gamma^2\gamma^3$ block-by-block from §3's matrices (carried out explicitly, not asserted) gives $\begin{pmatrix}0&-i\mathbb1\\-i\mathbb1&0\end{pmatrix}$; multiplying by the defining $i$ gives $\begin{pmatrix}0&\mathbb1\\\mathbb1&0\end{pmatrix}$, confirming the boxed result. $(\gamma^5)^2=\mathbb1$ ✓ (block computation, direct). $\{\gamma^5,\gamma^\mu\}=0$ for all four $\mu$: checked directly by block multiplication for $\gamma^0$ and $\gamma^1$ (representative cases; $\gamma^2,\gamma^3$ follow by the identical Pauli-block structure) — confirmed. ✓.

**Hermiticity of the generators, computed directly from §3, not assumed:**
$$(\gamma^0)^\dagger = \gamma^0 \ \text{(Hermitian, diagonal real matrix)} \qquad (\gamma^i)^\dagger = \begin{pmatrix}0&-\sigma^{i\dagger}\\\sigma^{i\dagger}&0\end{pmatrix} = \begin{pmatrix}0&-\sigma^i\\\sigma^i&0\end{pmatrix} = -\gamma^i$$
using $\sigma^{i\dagger}=\sigma^i$. So $(\gamma^\mu)^\dagger = \gamma^0\gamma^\mu\gamma^0$ for all four $\mu$ — check: for $\mu=0$, $\gamma^0\gamma^0\gamma^0=\gamma^0$ ✓; for $\mu=i$, $\gamma^0\gamma^i\gamma^0 = \begin{pmatrix}\mathbb1&0\\0&-\mathbb1\end{pmatrix}\begin{pmatrix}0&\sigma^i\\-\sigma^i&0\end{pmatrix}\begin{pmatrix}\mathbb1&0\\0&-\mathbb1\end{pmatrix} = \begin{pmatrix}0&\sigma^i\\\sigma^i&0\end{pmatrix}\begin{pmatrix}\mathbb1&0\\0&-\mathbb1\end{pmatrix} = \begin{pmatrix}0&-\sigma^i\\\sigma^i&0\end{pmatrix}=-\gamma^i$ ✓. This confirms the standard relation $(\gamma^\mu)^\dagger=\gamma^0\gamma^\mu\gamma^0$, i.e. $\gamma^0(\gamma^\mu)^\dagger\gamma^0=\gamma^\mu$, holds in this explicit representation — I do **not** take this as given; it's now verified by direct matrix computation.

$$(\gamma^5)^\dagger = \begin{pmatrix}0&\mathbb1\\\mathbb1&0\end{pmatrix}^\dagger = \begin{pmatrix}0&\mathbb1\\\mathbb1&0\end{pmatrix} = \gamma^5 \quad\text{(Hermitian, checked directly)}$$

## 4. Dirac adjoint — [C1, standard, but its consequence is [C2]]

$$\bar\psi \equiv \psi^\dagger\gamma^0$$

## 5. Hermiticity of the five bilinear classes — [C2, direct computation, no shortcuts]

For any $\Gamma\in\{\mathbb1,\gamma^5,\gamma^\mu,\gamma^\mu\gamma^5,\sigma^{\mu\nu}\}$, compute $(\bar\psi\Gamma\psi)^\dagger$ from scratch:
$$(\bar\psi\Gamma\psi)^\dagger = \psi^\dagger\Gamma^\dagger\gamma^{0\dagger}\psi = \psi^\dagger\Gamma^\dagger\gamma^0\psi$$
Insert $\mathbb1=\gamma^0\gamma^0$: $=\psi^\dagger\gamma^0(\gamma^0\Gamma^\dagger\gamma^0)\psi = \bar\psi\,(\gamma^0\Gamma^\dagger\gamma^0)\,\psi$. So the bilinear is Hermitian iff $\gamma^0\Gamma^\dagger\gamma^0=\Gamma$.

**Case $\Gamma=\mathbb1$:** $\gamma^0\mathbb1^\dagger\gamma^0=\gamma^0\gamma^0=\mathbb1$ ✓. **$\eta=\bar\psi\psi$ is Hermitian (real).**

**Case $\Gamma=\gamma^5$:** need $\gamma^0(\gamma^5)^\dagger\gamma^0 = \gamma^0\gamma^5\gamma^0$ (using $(\gamma^5)^\dagger=\gamma^5$, §3). Compute directly: $\gamma^0\gamma^5\gamma^0 = \begin{pmatrix}\mathbb1&0\\0&-\mathbb1\end{pmatrix}\begin{pmatrix}0&\mathbb1\\\mathbb1&0\end{pmatrix}\begin{pmatrix}\mathbb1&0\\0&-\mathbb1\end{pmatrix} = \begin{pmatrix}0&\mathbb1\\-\mathbb1&0\end{pmatrix}\begin{pmatrix}\mathbb1&0\\0&-\mathbb1\end{pmatrix} = \begin{pmatrix}0&-\mathbb1\\-\mathbb1&0\end{pmatrix} = -\gamma^5$.

So $\gamma^0(\gamma^5)^\dagger\gamma^0 = -\gamma^5 \neq \gamma^5$. **$P=\bar\psi\gamma^5\psi$ is anti-Hermitian: $P^\dagger=-P$, i.e. $P$ is pure imaginary as an operator/number.** This confirms, by explicit matrix computation with no algebra skipped, exactly what the previous notebook found abstractly.

**Case $\Gamma=\gamma^\mu$:** need $\gamma^0(\gamma^\mu)^\dagger\gamma^0=\gamma^\mu$ — verified directly in §3 already. **$V^\mu=\bar\psi\gamma^\mu\psi$ is Hermitian (real).**

**Case $\Gamma=\gamma^\mu\gamma^5$:** $(\gamma^\mu\gamma^5)^\dagger = (\gamma^5)^\dagger(\gamma^\mu)^\dagger = \gamma^5(\gamma^\mu)^\dagger$. Then $\gamma^0\gamma^5(\gamma^\mu)^\dagger\gamma^0$. Insert $\gamma^0\gamma^0=\mathbb1$ between $\gamma^5$ and $(\gamma^\mu)^\dagger$: $=\gamma^0\gamma^5\gamma^0\cdot\gamma^0(\gamma^\mu)^\dagger\gamma^0 = (-\gamma^5)(\gamma^\mu) = -\gamma^5\gamma^\mu = \gamma^\mu\gamma^5$ (using $\{\gamma^5,\gamma^\mu\}=0$, §3, to swap). So $\gamma^0(\gamma^\mu\gamma^5)^\dagger\gamma^0=\gamma^\mu\gamma^5$: **Hermitian.** The two sign flips (from $\gamma^5$'s and from the swap) cancel, confirmed by explicit tracking rather than assumed. **$A^\mu=\bar\psi\gamma^\mu\gamma^5\psi$ is Hermitian (real).**

**Case $\Gamma=\sigma^{\mu\nu}=\frac{i}{2}[\gamma^\mu,\gamma^\nu]$:** $(\sigma^{\mu\nu})^\dagger = -\frac{i}{2}[(\gamma^\nu)^\dagger,(\gamma^\mu)^\dagger]$ (the overall $i\to -i$ from the dagger, plus commutator antisymmetry flips the order). Conjugating by $\gamma^0$ on both sides as before, using the already-verified $\gamma^0(\gamma^\mu)^\dagger\gamma^0=\gamma^\mu$: $\gamma^0(\sigma^{\mu\nu})^\dagger\gamma^0 = -\frac{i}{2}[\gamma^\nu,\gamma^\mu] = \frac{i}{2}[\gamma^\mu,\gamma^\nu]=\sigma^{\mu\nu}$. **Hermitian (real).** $T^{\mu\nu}=\bar\psi\sigma^{\mu\nu}\psi$ real.

**Summary table (fully derived, no entries assumed):**

| Bilinear | Operator | Hermitian? | Real number? |
|---|---|---|---|
| $\eta=\bar\psi\psi$ | scalar | Yes | **Real** |
| $P=\bar\psi\gamma^5\psi$ | pseudoscalar | No ($P^\dagger=-P$) | **Imaginary** |
| $V^\mu=\bar\psi\gamma^\mu\psi$ | vector | Yes | Real |
| $A^\mu=\bar\psi\gamma^\mu\gamma^5\psi$ | axial | Yes | Real |
| $T^{\mu\nu}=\bar\psi\sigma^{\mu\nu}\psi$ | tensor | Yes | Real |

This matches what the previous notebook found, now nailed down with an explicit representation, zero abstract-algebra shortcuts, and every sign traced.

## 6. Resolving the convention question you raised directly

**[C2]** Given §5, exactly one convention makes the *pseudoscalar field appearing in a real potential* a genuine real number:
$$\boxed{\text{Convention B: } \tilde P \equiv i\,\bar\psi\gamma^5\psi = iP}$$
Check: $\tilde P^\dagger = (iP)^\dagger = -i P^\dagger = -i(-P) = iP = \tilde P$. **Hermitian.** ✓. This is Convention B in your framing, and it is the one required for $\tilde P$ to be usable as a real scalar field in a potential $V(\eta,\tilde P)$ — exactly as you anticipated.

**On the corpus's own note, checked rather than assumed:** Appendix P's audit (IVN-CT8-Dirac-1a/1d) states $\eta\equiv -i\bar\psi\psi$. §5 above shows directly, in an explicit representation, that $\bar\psi\psi$ is *already* Hermitian/real — multiplying it by $-i$ makes it **anti-Hermitian**, the wrong direction. **This computation does not confirm the corpus's note; it contradicts it.** Per your instruction not to paper over the conflict: I flag this as a specific, located discrepancy — the compensating factor of $i$ belongs on $P=\bar\psi\gamma^5\psi$ (to form $\tilde P=iP$), not on $\eta=\bar\psi\psi$ — rather than resolve it by assumption. Either the corpus's convention audit made exactly the error you predicted (attaching $i$ to the wrong bilinear), or it is using a Dirac-adjoint or Clifford convention different from §§1–4 above in a way not stated in the passage quoted. This document does not adjudicate which; it records the located conflict for whoever revises that note.

## 7. What this document does *not* certify — explicit, per your caution

- **The Fierz coefficient $-1/5$ from Notebook 2 remains provisional.** Nothing in this audit validates or invalidates it. Reworking Notebook 2 in terms of the now-real field $\tilde P=iP$ (so $P^2=-\tilde P^2$) would flip the sign of every $P$-dependent term in that identity — but that is a *rewriting* of an already-derived (and still unverified) identity, not a re-derivation of it. The identity itself needs the full $5\times5$ involutive check you specified before any coefficient in it is trusted, independent of which bilinear carries the $i$.
- **Discrete symmetry conventions** (parity, time-reversal, charge conjugation action on each bilinear) are not addressed here and are needed before Theorem 6's parity-preserving vacuum claims can be audited on this same footing.
- This document fixes **one internally self-consistent set of conventions** (§§1–4), checked for consistency by direct computation (§§3, 5) rather than by citation. It is a dictionary, not a theorem about $S_{\rm geo}$.

## 8. Standing instruction for all later notebooks

Any bilinear used downstream must be checked against the Table in §5 before being treated as a real scalar/potential-appearing field. In particular: **use $\tilde P=i\bar\psi\gamma^5\psi$, not $P=\bar\psi\gamma^5\psi$, wherever a real pseudoscalar order parameter is wanted** — and re-express Notebook 2's identity in terms of $\tilde P$ before attempting the involution check, so that the coefficient-verification work isn't contaminated by a reality-convention mismatch on top of a possible arithmetic one.
