# Foundations Notebook 2: Fierz Structure of $S_{\rm geo}$

*Governed by the same category discipline as before. One imported fact is used as background (analogous to importing the Clifford algebra itself): the standard Fierz completeness identity for $4\times4$ Dirac matrices. Everything downstream of it is shown in full, not asserted.*

## 0. Response to the two specific cautions

You're right on both points, and both change how I present the rest of this notebook:

- The Gross–Neveu analogy is downgraded to exactly the hedged phrasing you proposed — shared discrete symmetry only, not dimension, renormalizability, or large-$N$ structure.
- "The theory lacks the $P^2$ channel" is exactly the claim that needed pressure-testing before being load-bearing. It turns out to be **false as stated**, for a precise and derivable reason — not because the claim was careless, but because Fierz statistics for a *single* field (no color, no flavor index to swap) does something specific and non-obvious. That's the result below.

## 1. The imported fact

**[C1 — imported, standard]** For $4\times4$ Dirac matrices, the sixteen-element basis $\Gamma^A \in \{\mathbb 1,\ \gamma^5,\ \gamma^\mu,\ \gamma^\mu\gamma^5,\ \sigma^{\mu\nu}\,(\mu<\nu)\}$ is trace-orthogonal, $\text{Tr}[\Gamma^A\Gamma_A]=4$ per element (no sum), and satisfies the completeness/Fierz identity (index form, $i,j,k,l$ = Dirac indices):
$$\delta_{ij}\delta_{kl} = \frac14\Big[\delta_{il}\delta_{kj} + (\gamma^5)_{il}(\gamma^5)_{kj} + (\gamma^\mu)_{il}(\gamma_\mu)_{kj} - (\gamma^\mu\gamma^5)_{il}(\gamma_\mu\gamma^5)_{kj} + \tfrac12(\sigma^{\mu\nu})_{il}(\sigma_{\mu\nu})_{kj}\Big]$$
This is textbook (Itzykson & Zuber; standard in the NJL-Fierz literature). I import it exactly as the reconstruction imports $\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}$ — as background linear algebra, not something to re-derive from scratch. The minus sign on the axial term is the one detail worth flagging explicitly, since it's easy to misremember and it matters below.

## 2. Applying it to a single field

**[C2]** Write $(\bar\psi\psi)(\bar\psi\psi) = \bar\psi_i\delta_{ij}\psi_j\,\bar\psi_k\delta_{kl}\psi_l$. Move $\psi_j$ past $\bar\psi_k$ (one Grassmann transposition — **[C2]**, sign $=-1$):
$$(\bar\psi\psi)^2 = -\bar\psi_i\bar\psi_k\,\delta_{ij}\delta_{kl}\,\psi_j\psi_l$$

**[C2]** Substitute the completeness identity for $\delta_{ij}\delta_{kl}$ (note: I need it in the form pairing $(i,l)$ and $(k,j)$, which is exactly the form quoted in §1 above — no relabeling needed):
$$(\bar\psi\psi)^2 = -\frac14\Big[(\bar\psi\psi)^2 + (\bar\psi\gamma^5\psi)^2 + (\bar\psi\gamma^\mu\psi)(\bar\psi\gamma_\mu\psi) - (\bar\psi\gamma^\mu\gamma^5\psi)(\bar\psi\gamma_\mu\gamma^5\psi) + \tfrac12(\bar\psi\sigma^{\mu\nu}\psi)(\bar\psi\sigma_{\mu\nu}\psi)\Big]$$

**[C1]** Abbreviate $\eta\equiv\bar\psi\psi$, $P\equiv\bar\psi\gamma^5\psi$, $V^2\equiv V^\mu V_\mu$, $A^2\equiv A^\mu A_\mu$, $T^2\equiv T^{\mu\nu}T_{\mu\nu}$.

**[C2]** Then:
$$\eta^2 = -\frac14\Big[\eta^2+P^2+V^2-A^2+\tfrac12T^2\Big]$$
$$\frac54\eta^2 = -\frac14P^2-\frac14V^2+\frac14A^2-\frac18T^2$$
$$\boxed{\eta^2 = -\frac15P^2-\frac15V^2+\frac15A^2-\frac1{10}T^2}$$

## 3. What this means — the sharp answer to Document 10's Q2

This is not "$P^2$ could optionally be added to complete the theory." It is an **exact algebraic identity**, true pointwise for any classical Grassmann-valued $\psi$ at a spacetime point, entirely independent of the equations of motion, entirely independent of $S_{\rm geo}$'s parameters. $(\bar\psi\psi)^2$, written out in the complete bilinear basis, simply *is* the right-hand side above — there is no sense in which the two sides are different operators that happen to agree; they are the same operator in two bases.

**Consequence for $S_{\rm geo}$:** the quartic term $-\frac{\lambda}{4}\eta^2$, substituted via this identity, is *identically equal* to
$$-\frac{\lambda}{4}\eta^2 = \frac{\lambda}{20}P^2 + \frac{\lambda}{20}V^2 - \frac{\lambda}{20}A^2 + \frac{\lambda}{40}T^2$$
**This is not a modification of $S_{\rm geo}$. It is the same term, rewritten.** The pseudoscalar self-interaction is not absent from the microscopic action — it is already present, at a coefficient of $+\lambda/20$, forced by Grassmann statistics rather than chosen.

**So does this restore chiral symmetry after all?** No — and this is the precise correction to Notebook 1's Finding 1 that your caution demanded. Chiral invariance of the quartic sector requires the *symmetric* combination $\eta^2+P^2$ to appear with a **common** coefficient (that combination, and only that combination, is invariant under $\psi\to e^{i\alpha\gamma^5}\psi$ — this was already checked directly in Notebook 1). Here, after using the identity, the coefficient multiplying $\eta^2$ is $-\lambda/4$ while the coefficient multiplying $P^2$ (forced, via the same identity, to appear at all) is $+\lambda/20$ — a fixed ratio of $-5:1$, not $1:1$. There is no value of $\lambda$ that makes these equal without also changing the $V^2,A^2,T^2$ coefficients, which are equally fixed by the same identity.

**Revised Finding 1 (replaces the Notebook 1 version):** *The quartic term in $S_{\rm geo}$ does contain a pseudoscalar self-interaction — not by omission-then-optional-completion, but as an algebraic identity of the single term already written. What it lacks is the specific relative coefficient ($1:1$ between $\eta^2$ and $P^2$, with $V^2=A^2=0$) required for chiral invariance. Reaching that symmetric point is not "restoring hidden content" — the content is already there in full — it requires a genuinely independent second coupling constant, decoupled from $\lambda$, that is not present in $S_{\rm geo}$ as frozen.* This is the sharper, Fierz-informed version of the claim your document asked me to strengthen, and it is a stronger conclusion than Notebook 1's, not a weaker one: **it is now demonstrated, not merely observed by inspection, that no relabeling or Fierz rearrangement of the single written term can produce a chirally invariant quartic sector.** Adding one would be a genuine, load-bearing modification of $S_{\rm geo}$, exactly as Notebook 1 concluded — but now for a reason that survives the Fierz-completeness objection you correctly raised, rather than being vulnerable to it.

## 4. What I have not verified — explicit residual

- **Only the S-row of the full $5\times5$ Fierz matrix is derived above**, fully and reproducibly. I attempted a cross-check via the analogous P-row identity ($\gamma^5\otimes\gamma^5\to\ldots$) from memory and it did **not** resolve cleanly against §2's result on substitution — which means either my recollection of the companion P-row identity is wrong, or there's an error I haven't isolated. I am flagging this rather than presenting it, per the Constitution's own rule: an unverified step doesn't get to be Category 2 just because it would be convenient.
- **This is a classical/pointwise Grassmann identity**, valid inside the path integral's classical action. Whether it survives intact at the *quantum* (normal-ordered, coincident-point) level — i.e., whether $\langle(\bar\psi\psi)^2\rangle$ and the right-hand side combination require independent renormalization once loop corrections are included — is a distinct question, not addressed here, and directly adjacent to the UV-divergence halt point already flagged in Target 0 §5.
- I have not touched $S^\text{V-row}$, $A$-row, or $T$-row identities, nor verified the involution property ($C^2=\mathbb 1$) that a correct Fierz matrix must satisfy. Any future notebook that needs those should re-derive them by the same completeness-relation method used in §2, not by importing the S-row result and assuming symmetry of the matrix.

## 5. Where this leaves the staged plan

Your Stage 2 (deriving the regulator) is unaffected by this finding — the UV-divergence structure of Target 0 doesn't change because the quartic term's *basis representation* changed; it's the same operator. Your Stage 3 (reconstructing Theorem 6) is the one materially sharpened: the question is no longer "does a Mexican-hat emerge from an incomplete operator basis" but the narrower and now well-posed "does the *forced* combination $-\frac{1}{5}P^2-\frac15V^2+\frac15A^2-\frac1{10}T^2$ (in place of a bare $\eta^2$) change the one-loop effective potential computed in Target 0 at all" — since Target 0 as executed treated $\eta^2$ as if it were a self-contained scalar-only interaction, when it also implicitly carries $V^2$ and $A^2$ pieces that couple to the fermion loop differently (vector/axial-vector channels renormalize differently than scalar/pseudoscalar channels in the standard NJL literature). That is a concrete, checkable amendment to Target 0 itself, and is probably the correct next notebook before Stage 3 rather than after it.
