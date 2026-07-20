# Corpus-Wide Audit: Does Theorem 6 / §P.11 / Paper C Inherit the Fierz Ambiguity?

*Adopting your final wording tweak first, then proceeding with the audit as prioritized.*

## Wording adopted

> **Representation-independence has been shown to fail for at least one legitimate mean-field realization of the exact interaction.**

This is `Foundation-B-Result-B2-v1.2`'s central claim, replacing the v1.1 language. It's the correct framing: I exhibited a positive construction demonstrating non-invariance, not merely a failure to prove invariance.

---

## Audit method

For each downstream document, I check: (a) does it perform a mean-field/HS-type extremization of $S_{\rm geo}$'s quartic term, (b) does it specify or implicitly fix a decoupling channel, (c) is there any independent argument in that document that would restore invariance regardless of channel choice.

### Theorem 6 (Appendix P, matter-light phase transition)

**[C1, quoting the source directly]** Theorem 6's derivation states the effective potential as $V_{\rm eff}(\eta) = \frac{m^2}{2}\eta-\frac\lambda4\eta^2+\text{higher order}$, and explicitly calls this "the effective potential for the condensate order parameter $\eta$ in the mean-field approximation." **No HS field is introduced, no fermion determinant is computed, and no regularization is specified anywhere in Theorem 6's proof.** The quartic coefficient is simply carried over from the classical action with a sign flip and no derivation of where the flip comes from — this is a bare assertion, not a calculation.

**Consequence:** Theorem 6 does not merely inherit B2's ambiguity — **it never actually performed the mean-field calculation that would exhibit it.** It asserted a *specific form* of the potential (bare $-\lambda\eta^2/4$, no loop contribution, no $t$-dependence visible at all because no bosonization was carried out) without deriving that form from $S_{\rm geo}$. This is a **different and more basic problem than the one B2 diagnosed**: B2 shows that *if* you do the calculation carefully, the answer depends on an unstated choice; Theorem 6 shows a case where the calculation wasn't done at all, and a plausible-looking classical-level potential was substituted for it. Recall also §P.11.2's own honest admission (quoted in Foundations Notebook 2/3 material) that the "$(\eta^2+P^2)$" quartic form used there was a **silent Fierz-completion**, not derived from $S_{\rm geo}$ as frozen — this is now visible as the *same* underlying issue from a different angle: Theorem 6 and §P.11.2 both quietly picked *a* representation of the quartic term (implicitly $t=0$-like for Theorem 6's bare form; implicitly the symmetric $\eta^2+P^2$ completion for §P.11.2) without ever showing the choice doesn't matter.

**Verdict: Theorem 6 is conditionally affected, and worse than conditionally — it never demonstrated the calculation whose channel-dependence B2 has now shown is generically real.**

### §P.11 (GMOR relation, Theorem 4a/4b)

**[C1, quoting]** §P.11.2 explicitly writes: "$V(\eta,P)=\frac{\mu^2}2(\eta^2+P^2)+\frac\lambda4(\eta^2+P^2)^2-m\eta$" and derives $m_P^2=m/\eta_{\rm eq}$ (the GMOR relation) from extremizing *this* potential.

**This is exactly a $t\ne0$-type choice** — specifically, it's the fully symmetric completion (equal weight on $\eta^2$ and $P^2$), which is **not** even a point on my $t$-interpolation family as constructed (my family interpolates between $\eta^2$ alone and the *Fierz-forced* combination at fixed ratios $-1/5,-1/5,+1/5,-1/10$ for $P^2,V^2,A^2,T^2$; §P.11.2's potential instead imposes an *equal* $\eta^2,P^2$ coefficient by fiat, which is neither the bare action nor the Fierz-derived combination — it's a third, independently chosen representation, chosen specifically because it's the one that produces the desired NJL-style chiral-symmetry-breaking phenomenology). **This is worse than inheriting B2's ambiguity — it's a specific, unlabeled instance of exactly the free choice B2's counterexample shows has physical consequences**, and moreover it isn't even drawn from the two natural anchors (raw action, or Fierz-forced form) that this reconstruction has been tracking — it's a third point introduced with no stated justification for why *that* combination and not another.

**Verdict: §P.11.2's GMOR relation directly and demonstrably depends on an unstated channel choice, confirmed as a specific case of the general problem B2 identifies — and identified here as an even less well-motivated choice than the ones this reconstruction has been comparing.**

### Paper C (leptonic mass shift, §2.1)

**[C1, quoting]** Paper C's derivation of $\delta m_\ell=\alpha\eta m_\ell$ takes $\eta=\langle\bar\psi\psi\rangle$ as a **given background value**, sourced from "the mean-field condensate limit" without re-deriving $\eta_{\rm eq}$ itself — it takes whatever value Theorem 6/§P.11 supply as an external input, via the parameter $m_{\rm eff}$, and builds the leptonic coupling on top of that.

**Verdict: Paper C does not introduce a *new* instance of the ambiguity — it inherits it entirely secondhand, through its dependence on $\eta_{\rm eq}$ and $m_{\rm eff}$, both of which trace back to Theorem 6/§P.11.2's unaudited choices.** Nothing in Paper C's own derivation (§2.1's dimensional argument, the mass-proportionality structure) requires re-examination independently; it's a pass-through dependency, not an independent point of failure.

## Summary table

| Document | Performs the mean-field calculation? | Channel choice stated? | Independently affected? |
|---|---|---|---|
| Theorem 6 | **No** — asserts form, doesn't derive it | No | **Yes — more basic gap than B2's issue** |
| §P.11.2 (GMOR) | Yes, extremizes a stated $V(\eta,P)$ | No — unmotivated symmetric completion, not even matching Foundation A's Fierz-forced ratios | **Yes — direct instance of B2's issue** |
| Paper C §2.1 | No — takes $\eta_{\rm eq}$ as external input | N/A | Secondhand only, via $\eta_{\rm eq}, m_{\rm eff}$ |

## Conclusion of the audit

The ambiguity **does propagate into the parts of SCH that matter most**, and does so more severely than B2's abstract counterexample alone suggested: Theorem 6 never performed the calculation, and §P.11.2 performed it using a third, unmotivated representation that is neither the raw action nor the Fierz-forced combination this reconstruction has been tracking. Per your closing framing: **a bosonic-fluctuation program (B3) is not yet the right next move, because it would be refining an approximation order on top of a mean-field calculation whose baseline (which channel, which representation) has never been fixed or justified anywhere in the corpus.** The higher-priority gap is establishing — or explicitly flagging as unresolved — *why* any particular representation should be preferred, before asking whether boson loops restore invariance among representations that haven't themselves been chosen for a stated reason.

**Recommendation:** the next notebook should be a **Foundation C scoping document** that states this finding plainly as Foundation C's opening problem, rather than a B3 extension of Foundation B. Foundation C was always going to ask "does a Mexican-hat/GMOR structure emerge from $S_{\rm geo}$" — this audit shows the answer is now sharper: **not without first specifying which of (at least) three inequivalent representations of the quartic term is being extremized, a choice none of Theorem 6, §P.11, or the original Target 0 ever made explicitly.**
