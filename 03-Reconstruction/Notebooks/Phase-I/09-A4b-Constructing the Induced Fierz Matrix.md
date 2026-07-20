# A4b: Constructing the Induced Fierz Matrix — Progress Report, Not Closure

*Per your sharpened definition of A4b. I attempted the full $S,\tilde P,V,A,T\to(S,\tilde P,V,A,T)$ matrix. I got two rows solid, confirmed by independent methods, and hit a genuine bookkeeping obstruction in the remaining three that I am reporting precisely rather than smoothing over.*

## 1. The general self-Fierz formula, derived (not imported this time)

**[C2]** Starting from $(\bar\psi\Gamma^{(1)}\psi)(\bar\psi\Gamma^{(2)}\psi)$, one Grassmann transposition ($\psi_j\bar\psi_k\to-\bar\psi_k\psi_j$) gives $-\bar\psi_i\Gamma^{(1)}_{ij}\bar\psi_k\Gamma^{(2)}_{kl}\psi_j\psi_l$. Substituting the general two-matrix completeness identity (derived from A4a's swap-operator result, applied with $\Gamma^{(1)},\Gamma^{(2)}$ inserted rather than $\mathbb1,\mathbb1$) and reordering $\psi_j\psi_l\to\psi_l\psi_j$ paired correctly with two further transpositions (net sign $+1$, tracked explicitly rather than assumed) gives:
$$\boxed{(\bar\psi\Gamma^{(1)}\psi)(\bar\psi\Gamma^{(2)}\psi) = -\frac14\sum_A(\bar\psi\,\Gamma^{(1)}\Gamma_A\Gamma^{(2)}\,\psi)(\bar\psi\Gamma^A\psi)}$$
**Consistency check on this formula itself:** setting $\Gamma^{(1)}=\Gamma^{(2)}=\mathbb1$ reproduces exactly Notebook 2's original S-row computation. ✓.

## 2. S-row — reconfirmed

$\Gamma_B=\mathbb1$: $\Gamma_B\Gamma_A\Gamma_B=\Gamma_A$ trivially, giving directly
$$\eta^2 = -\frac14\Big[\eta^2+P^2+V^2-A^2+\tfrac12T^2\Big] \;\Rightarrow\; \eta^2 = -\frac15P^2-\frac15V^2+\frac15A^2-\frac1{10}T^2$$
Unchanged from before — **[C2], confirmed by exact match to the earlier independent derivation.**

## 3. P-row — derived twice, matches both times

**Method 1 (direct conjugation, done in the previous notebook):** using $\gamma^5\Gamma_A\gamma^5 = c_A\Gamma_A$ with $(c_S,c_P,c_V,c_A,c_T)=(+1,+1,-1,-1,+1)$ — each verified individually by explicit anticommutation counting, not asserted.

**Method 2 (the general formula of §1, applied fresh with $\Gamma^{(1)}=\Gamma^{(2)}=\gamma^5$):** substituting $\gamma^5\cdot1\cdot\gamma^5=1$, $\gamma^5\gamma^5\gamma^5=\gamma^5$, $\gamma^5\gamma^\mu\gamma^5=-\gamma^\mu$, $\gamma^5(\gamma^\mu\gamma^5)\gamma^5=+\gamma^\mu\gamma^5$ (sign flips tracked: two anticommutations through $\gamma^5\gamma^\mu=-\gamma^\mu\gamma^5$ applied twice, canceling — shown explicitly), $\gamma^5\sigma^{\mu\nu}\gamma^5=\sigma^{\mu\nu}$:
$$P^2 = -\frac14\Big[\eta^2+P^2-V^2+A^2+\tfrac12T^2\Big] \;\Rightarrow\; P^2=-\frac15\eta^2+\frac15V^2-\frac15A^2-\frac1{10}T^2$$

**Both methods agree exactly.** Converting to the real field ($P^2=-\tilde P^2$):
$$\boxed{\tilde P^2 = \frac15\eta^2-\frac15V^2+\frac15A^2+\frac1{10}T^2}$$
**This is now genuinely double-derived** — the A4.5 criterion you added is satisfied for this row specifically.

## 4. The 2×2 sub-block, checked *honestly* this time — and here is what it actually shows

Rather than the earlier (invalid) truncated check that froze $V,A,T$ and got $1/25$, I substitute the *actual* $\tilde P^2$ identity into the *actual* $\eta^2$ identity, treating $V^2,A^2,T^2$ as unknowns rather than assuming they vanish or are separately fixed points:

$$\eta^2 = -\frac15\Big[\frac15\eta^2-\frac15V^2+\frac15A^2+\frac1{10}T^2\Big] -\frac15V^2+\frac15A^2-\frac1{10}T^2$$
$$\eta^2-\frac1{25}\eta^2 = \Big(-\frac1{25}-\frac15\Big)V^2+\Big(\frac1{25}+\frac15\Big)A^2+\Big(\frac1{50}-\frac1{10}\Big)T^2$$
$$\frac{24}{25}\eta^2 = -\frac{6}{25}V^2+\frac6{25}A^2-\frac2{25}T^2$$

**This is the precise, correctly-obstructed statement — not "$1/25$", but a genuine linear relation between $\eta^2$ and $V^2,A^2,T^2$** that must itself be consistent with whatever the $V$-row, $A$-row, and $T$-row identities say when re-substituted. It is neither confirmed nor refuted by the S-row/P-row alone: **it is exactly the equation the V/A/T rows are needed to check**, which is precisely your point. I was wrong earlier to call the old $1/25$ result "an involution failure" — it wasn't testing involution at all; it was an artifact of setting $V^2=A^2=T^2=0$ by omission. The corrected version above is not a failure, it's an *open equation waiting on the other three rows*.

## 5. Where I got stuck on the V-row — reported precisely, not glossed over

Attempting $\Gamma_B=\gamma^\nu$ (summed), I need $\sum_\nu\gamma^\nu\Gamma_A\gamma_\nu$ for each channel. Using standard 4D gamma contraction identities (re-derived, not quoted, from $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$):
$$\sum_\nu\gamma^\nu\gamma_\nu=4,\quad \sum_\nu\gamma^\nu\gamma^5\gamma_\nu=-4\gamma^5,\quad \sum_\nu\gamma^\nu\gamma^\rho\gamma_\nu=-2\gamma^\rho,\quad \sum_\nu\gamma^\nu\sigma^{\rho\sigma}\gamma_\nu=0$$
all four confirmed by direct computation. The obstruction is the fifth: $\sum_\nu\gamma^\nu(\gamma^\rho\gamma^5)\gamma_\nu$. I derived $+2\gamma^\rho\gamma^5$ by one ordering of anticommutations, but when I fed this back through the general formula of §1 — which has an explicit **built-in relative minus sign on the axial slot** (visible in the original completeness relation's "$-(\gamma^\mu\gamma^5)_{il}(\gamma_\mu\gamma^5)_{kj}$" term) — I could not re-derive a self-consistent sign for the resulting $A^2$ coefficient in $V^2$ without the answer depending on *which of two legitimate-looking bookkeeping conventions* I used for where that built-in minus sign gets applied when $\Gamma^{(1)},\Gamma^{(2)}$ are no longer both $\mathbb 1$. This is exactly the kind of "shared hidden mistake" risk your A4.5 criterion was designed to catch, and I do not currently have a second independent method (analogous to the direct-conjugation cross-check that saved the P-row) for the $V$-row, because $\gamma^\nu\Gamma_A\gamma_\nu$ summed over $\nu$ is a genuinely different operation from simple conjugation by an involution like $\gamma^5$ — there's no single fixed matrix $M$ with $M\Gamma_AM^{-1}$ giving this; it's a trace-like contraction, so the "check by an independent route" I used for P doesn't transfer mechanically.

## 6. Status, plainly

- S-row, P-row: **Category 2, double-derived, closed.**
- The $\eta^2$-vs-$\tilde P^2$ cross-substitution: **correctly computed, not a contradiction — an open linear equation, correctly stated, pending the V/A/T rows.**
- V-row: **stuck at a specific, located sign-bookkeeping ambiguity** in the axial-channel contraction, not yet resolved, not papered over.
- A-row, T-row: **not attempted**, since they depend on getting the V-row's bookkeeping convention right first (same axial-slot sign issue will recur).

I have not completed A4b. I've isolated exactly one new place where the derivation needs a second, genuinely independent method before I'd trust it — the $\gamma^\nu(\cdot)\gamma_\nu$ contraction's interaction with the completeness formula's built-in axial minus sign — and I'd rather hand that back than guess at a sign to make three more rows come out looking clean.
