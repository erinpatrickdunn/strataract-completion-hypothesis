# Foundations Notebook 1: Classification of the Microscopic Theory

*Companion to the Target-0 Reconstruction. Governed by the same category discipline as the Constitution (§6): every claim below is tagged **[C1]** (definition), **[C2]** (derived, checkable), or **[C3]** (hypothesis). This notebook classifies $S_{\rm geo}$; it does not modify it, complete Target 0, or touch Theorem 6's status. Per your instructions, I am stopping at classification and flagging one structural finding it exposes — not proceeding to a gap equation.*

---

## Q1 — Is $S_{\rm geo}$ the NJL model?

**[C1]** The original Nambu–Jona-Lasinio interaction (1961) is the *chirally symmetric* quartic:
$$\mathcal L_{\rm NJL} = \bar\psi i\partial\!\!\!/\psi + G\big[(\bar\psi\psi)^2 + (\bar\psi i\gamma^5\psi)^2\big]$$
i.e. $G(\eta^2+P^2)$ in the notation of the Constitution.

**[C1]** $S_{\rm geo}$'s quartic term, as frozen, is
$$-\frac{\lambda}{4}(\bar\psi\psi)^2 = -\frac{\lambda}{4}\eta^2$$
— **the $P^2$ partner is absent.**

**[C2] — this absence is not cosmetic.** Under the continuous chiral rotation $\psi\to e^{i\alpha\gamma^5}\psi$ (using $\bar\psi\to\bar\psi e^{i\alpha\gamma^5}$, since $\gamma^5$ anticommutes with $\gamma^0$):
$$\bar\psi\psi \;\to\; \bar\psi e^{2i\alpha\gamma^5}\psi = \cos(2\alpha)\,\eta - \sin(2\alpha)\,P$$
(this reproduces exactly the transformation quoted in Appendix P §P.11.1). Squaring:
$$\eta^2 \to \cos^2(2\alpha)\,\eta^2 - 2\sin(2\alpha)\cos(2\alpha)\,\eta P + \sin^2(2\alpha)\,P^2 \neq \eta^2 \quad (\alpha \neq 0,\tfrac{\pi}{2},\dots)$$
Only the *combination* $\eta^2+P^2$ is invariant under this rotation ($\eta^2+P^2 \to \eta^2+P^2$, by the same substitution — a one-line check). $\eta^2$ alone is not.

**Finding 1 (Category 2, not a hypothesis):** *$S_{\rm geo}$'s quartic term explicitly breaks continuous chiral symmetry all by itself — independent of, and in addition to, the explicit breaking already provided by the mass term $-m\eta$.* This is a stronger and qualitatively different statement than "the mass term tilts an otherwise chirally-symmetric potential," which is what Appendix P §P.11.2 assumes when it writes the tree potential as
$$V(\eta,P) = \frac{\mu^2}{2}(\eta^2+P^2) + \frac{\lambda}{4}(\eta^2+P^2)^2 - m\eta.$$
**That potential is not the potential implied by $S_{\rm geo}$ as frozen.** It silently upgrades $\eta^2 \to (\eta^2+P^2)$ in the quartic term — a Fierz-completion choice, not a consequence of the stated action. This is exactly the kind of unlabeled step the Constitution exists to catch.

**So: is $S_{\rm geo}$ "basically NJL"?** Partially, and the precise statement matters:
- It has NJL's *scalar channel* (same operator, same four-fermion contact structure, same non-renormalizability class).
- It lacks NJL's *pseudoscalar channel*, and therefore lacks NJL's continuous $U(1)_A$ symmetry and its associated Goldstone phenomenology.
- The correct classification is: **a chirally-non-invariant, scalar-channel truncation of the NJL interaction** — not the NJL model itself, and not automatically inheriting NJL's chiral-dynamics literature without modification.

## Q2 — Attractive or repulsive channel?

**[C1]** Convention check: with $\lambda>0$ (as Theorem 6 states is required for condensation), the interaction $-\frac{\lambda}{4}\eta^2$ has the same sign convention as $+G\eta^2$ with $G>0$ in the standard NJL Lagrangian above (both are "$+$coupling$\times\eta^2$" once the overall sign convention for $\mathcal L$ vs. the Euclidean action is matched — this is a genuine [C2] check, not assumed, and it comes out consistent).

**[C2]** In the scalar-channel-only NJL literature, $G>0$ (in this convention) is indeed the *attractive* channel required for a nontrivial gap equation solution — this is standard and holds regardless of whether the $P^2$ partner is present, since the partner term doesn't change the sign structure of the $\eta$-channel Fierz decomposition. So: **yes, the sign matches the attractive channel**, consistent with dynamical-mass-generation-type behavior being possible in principle. This does *not* yet establish that condensation *occurs* — that's a magnitude question (coupling vs. cutoff), addressed in Q4 below.

## Q3 — Which regularizations preserve which symmetries?

**[C2] — this is now a differently-shaped question than it would be for real NJL**, because there is less symmetry here to preserve. For real NJL (with the $P^2$ partner), the standard menu is:

| Scheme | Lorentz invariant? | Chiral invariant? | Notes |
|---|---|---|---|
| 3-momentum cutoff $\Lambda_3$ | No | Yes | Most common in NJL phenomenology (Klevansky, *Rev. Mod. Phys.* **64**, 649 (1992); Vogl & Weise, *Prog. Part. Nucl. Phys.* **27**, 195 (1991)); breaks boost invariance explicitly |
| Proper-time regularization | Approximately | Yes | Preferred when chiral Ward identities must hold exactly |
| Pauli–Villars | Yes (with care) | Partially | Awkward for four-fermion (non-gauge) interactions; less commonly used here |
| Dimensional regularization | Yes | Yes | Cleanest for symmetry bookkeeping; still requires a renormalization scale $\mu$ chosen by hand |

**[C2] — but for $S_{\rm geo}$ specifically:** since chiral symmetry is already explicitly broken by the action itself (Finding 1), the traditional reason to prefer a chiral-symmetry-preserving regulator (proper-time, dim reg) over a cutoff — namely, protecting Ward identities relating the $\eta$ and $P$ sectors — **does not apply here**, because there is no such Ward identity to protect. This removes one of the usual arguments for scheme choice and leaves the regulator choice for $S_{\rm geo}$'s scalar-only theory genuinely more open than it would be for standard NJL — which sharpens, rather than answers, your Stage 2 question ("what physical principle fixes the cutoff, if any?").

## Q4 — What does the literature already establish for this exact interaction class?

**[C2]** For the full NJL model, the one-loop (large-$N_c$, leading order) gap equation, critical coupling $G_c\Lambda^2 \sim \pi^2$ (scheme-dependent $O(1)$ coefficient), and the existence of a first-order-in-coupling transition between $M=0$ and $M\neq0$ solutions are textbook results (Nambu & Jona-Lasinio 1961; Klevansky 1992 review, full derivation with multiple regulators compared side by side). This machinery is directly importable for the *magnitude/divergence-structure* question your reconstruction halted on (Target 0, §5) — it answers exactly "does a nontrivial $\eta_{\rm eq}$ exist for given $\{m,\lambda,\Lambda\}$" once a regulator is chosen.

**[C2] — but it does not directly answer the Goldstone/GMOR question**, because that part of the NJL literature (pion as pseudo-Goldstone boson, GMOR relation $m_\pi^2 f_\pi^2 \propto m_q\langle\bar qq\rangle$) is a direct consequence of the $P^2$ channel's presence — the very piece Finding 1 shows is absent from $S_{\rm geo}$. **This means §P.11.2's derivation of the "SCH GMOR relation" for a $\delta P$ mode cannot be imported from the NJL literature as-is**: in the NJL literature, the pion mass formula follows from an *exact* Ward identity tied to the spontaneously-broken continuous chiral symmetry; here, there is no such symmetry to spontaneously break, so whatever mass the $P$-fluctuation has must come from an ordinary (non-Goldstone-protected) loop calculation, not a symmetry argument. Whether $m_P$ ends up small is now an open dynamical question rather than a protected one.

## Central finding, stated once, plainly

$S_{\rm geo}$ is a scalar-channel four-fermion contact interaction, correctly classified as **an irrelevant (dimension-6) operator** requiring a regulator/cutoff to define — as your reconstruction already found — but *additionally*, it possesses **no continuous symmetry protecting a light pseudoscalar mode**, because the interaction is not Fierz-complete: it contains $\eta^2$ but not $P^2$. The only symmetry the quartic term possesses beyond the trivial vector $U(1)$ (which any bilinear preserves) is a **discrete** $\mathbb Z_2$: $\eta \to -\eta$ under $\psi\to\gamma^5\psi$ — this *is* a genuine [C2]-derivable symmetry of the quartic term, explicitly broken by $m$, structurally analogous to the Gross–Neveu model's discrete chiral symmetry rather than NJL's continuous one (though Gross–Neveu is 2D and renormalizable, so even that analogy is partial). This single discrete symmetry is the honest surviving core of Theorem 6's "$\eta \to -\eta$ asymmetric potential" remark — but it does not support the continuous-rotation, Mexican-hat, GMOR-relation apparatus built on top of it in §P.11.

## What this means for your staged plan (not executed here)

- **Stage 2** (deriving the cutoff) is now a sharper question than before: since there's no chiral Ward identity to preserve, the usual NJL argument for scheme choice doesn't transfer, and the cutoff really might be a free EFT parameter unless gravity/torsion supplies one independently — worth investigating on its own terms, not folded into Target 0.
- **Stage 3** (reconstructing Theorem 6) should now ask a narrower question than "does a Mexican hat emerge" — it should ask whether the discrete $\mathbb Z_2$ alone, run through the one-loop machinery of Target 0, reproduces *anything* resembling Theorem 6's continuous-potential picture, or whether Theorem 6's continuous form requires quietly restoring the $P^2$ term (i.e., silently changing $S_{\rm geo}$) — which would itself be a reportable finding under §7(c).
- **Stage 4** is unaffected by this notebook and remains untouched.

I have not derived a gap equation, chosen a regulator, or revised $S_{\rm geo}$. This notebook only answers what class of theory is on the table.
