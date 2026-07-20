# SCH Project Governance Charter v3

---

**Status:** GOVERNANCE — adopted [date]. Supersedes `SCH_Project_Governance_Charter_v2.md`, which is retired to `07-Superseded/` in full, unedited, as the historical governance record of the project's Track A/Track B period.

**Note on this revision.** v2 was the constitution of a specific moment: the Track A/Track B bifurcation created to manage one recurring failure mode (results migrating into Appendix P before independent confirmation). That problem was real, and v2's mechanisms for handling it — the Four-Question Rule, the audit-trail philosophy, the willingness to correct governance's own errors — worked and are preserved below. But v2 also embedded a snapshot of the theory's content directly into the governance document. That content is now the responsibility of `02-Methodology` and `03-Reconstruction`, and a governance charter that must be rewritten every time a coefficient is confirmed is not functioning as governance. v3 removes all theory-specific content from this document. Nothing about the underlying physics is retracted by this move — see `07-Superseded/SCH_Project_Governance_Charter_v2.md` for the full historical record, and `03-Reconstruction/` for current derivational status.

---

## 1. Repository Authority Map

```
01-Governance/           Defines how the project operates: authority, process, revision rules.
02-Methodology/          Defines how scientific claims are evaluated and classified.
03-Reconstruction/       Applies the Methodology to recover the documented derivational
                          content of the canonical theory, without modifying that theory.
04-Canonical-Theory/     Contains the current accepted canonical corpus.
05-Alternatives/         Contains new constructions that intentionally depart from or
                          extend the canonical theory.
06-Support/              Software, datasets, and auxiliary materials.
07-Superseded/           Preserves historical provenance — retired documents, in full,
                          unedited.
```

*(Directory renamed `04-Theory/` → `04-Canonical-Theory/` to match the terminology used throughout this charter and `02-Methodology`. Update all cross-references accordingly.)*

**Governance does not define scientific status.** Claim classification (ESTABLISHED, CONDITIONAL, OPEN, etc.) is the exclusive domain of `02-Methodology/SCH_Claim_Classification_Framework_v1.md` and its companion documents. This charter will not contain, reference by value, or attempt to summarize any specific claim's current classification.

**Governance does not track theory content.** This charter will not list which theorems are canonical, which sections are frozen, or what a coefficient's value is. That is `03-Reconstruction`'s and `04-Canonical-Theory`'s job. A governance document that requires revision every time Appendix P is edited has failed at being governance.

## 2. The Reconstruction Firewall

**Definition.** Reconstruction is a governed activity whose purpose is to recover the derivational content of the canonical theory without modifying that theory. Reconstruction may identify undocumented assumptions, incomplete derivations, or scope limitations, but shall not introduce replacement physics into the canonical corpus. Proposed replacements belong in `05-Alternatives/` until independently reviewed and adopted.

This firewall is a defining structural characteristic of the project, established through direct experience during the fermion-sector reconstruction: every finding in `03-Reconstruction` — a Fierz-dependence result, a provenance gap in Theorem 6, an unresolved UV halt point — is a statement about what the frozen action does or does not establish, never a proposed correction to the action itself. Without this firewall, reconstruction inevitably drifts into unconsciously "repairing" the theory it is meant only to audit — rationalizing an unlabeled assumption as "obviously what was intended" rather than reporting it as a gap. Work that proposes a correction is, by definition, no longer reconstruction and must be relocated to `05-Alternatives/`.

## 3. The Immutability Principle

**Canonical documents are historical records, not living notebooks.**

Once adopted into `04-Canonical-Theory/`, a document is corrected only through explicit versioned revision. Reconstruction does not edit canonical history in place, and superseded documents are preserved intact in `07-Superseded/`. Every change to canonical theory therefore has a traceable provenance.

This is a record-keeping decision, not a scientific one — it belongs in governance rather than methodology because it governs *how the institution handles its own documents*, independent of what those documents claim. It is the reason the repository retains multiple historical versions of Appendix P rather than overwriting them, and it is the same discipline already applied to this charter itself: v2 is not deleted or edited into v3, it is retired, in full, to `07-Superseded/`.

## 4. The Four-Question Rule

Before any result is allowed to modify a document in `04-Canonical-Theory/`, it must answer all four of the following, in writing, before the edit is made — not after:

1. **What exact equation set (or claim) is being asserted?** Not a description — the literal statement, written out.
2. **What derivation route produced it?** Named specifically, per the construction-scoping discipline of `02-Methodology/Scope-Principle.md`.
3. **What independent route has reproduced it?** If none, the result does not clear the bar for `ESTABLISHED` status regardless of how confident the derivation feels — per `02-Methodology/Reproducibility-Standard.md`. Critically: the independent route's *output* must actually exist and be inspected, not merely be planned or assumed to agree. A charter or report may not describe the result of a derivation in the past tense until that derivation has actually been performed and its written output checked, even when the outcome seems overdetermined by the surrounding argument.
4. **What downstream documents become affected if this changes?** Answered by consulting the relevant dependency map before, not after, propagating the change.

This rule is procedural, not scientific. It does not tell anyone what the answer is. It tells the project what must exist before an answer is allowed into the canonical corpus.

## 5. The Audit Trail Principle

**The audit trail is the deliverable, not just the endpoint.**

A result is not simply "true" or "false" as far as this project's records are concerned — it has a history: what was tried, what failed, what was corrected, and why. That history is retained deliberately (see `07-Superseded/` and `03-Reconstruction/Notebooks/`), not discarded once a clean final answer is reached, because the failed attempts and corrections are themselves part of what makes the final answer trustworthy. This principle governs *why* the Immutability Principle's preserved records exist and are worth consulting, not merely that they are kept.

## 6. Self-Correction of Governance

This charter is not exempt from its own standards. Governance documents, like scientific claims, can be wrong, and finding that out is not a failure of the project — it is the project working as intended.

**Historical precedent (preserved from v2, in full, as the standing example rather than theory-specific content):** v2 itself contained an error in its own retrospective section, where it described an independent confirming derivation as already having occurred and agreed with a prior result, when in fact the document in question had not yet been written at the time that claim was made. When the derivation was actually carried out, it did not confirm the earlier result — it found the earlier result was itself the product of an error. v2 corrected this in its own text rather than quietly revising the claim, explicitly naming the mistake, why it occurred, and what it demonstrated about the Four-Question Rule (specifically: that Question 3 requires inspecting a second route's actual output, not merely confirming that a second route is planned or "should" agree).

This precedent is retained here, independent of the specific coefficient or sector it concerned, because it establishes the operating norm: **when governance itself is found to have overreached, the record says so, plainly, in the same place the original claim was made** — following exactly the same discipline `02-Methodology/Documentation-Principle.md` requires of scientific claims.

## 7. Revision Rule for This Charter

A new version of this charter is warranted when:
- The repository authority map changes (a directory's responsibility is redefined, added, or removed).
- A structural governance mechanism (the Four-Question Rule, the Reconstruction Firewall, the Immutability Principle, or an equivalent) is found to be insufficient and requires amendment.
- A governance-level error (per §6) is discovered and must be corrected in the charter's own text.

A new version is **not** warranted for: changes to specific theory content, changes to claim classifications, opening or closing a specific reconstruction track, or any event whose correct home is `02-Methodology`, `03-Reconstruction`, or `04-Canonical-Theory`. If a proposed charter revision turns out to be theory-specific content, it belongs in one of those directories instead, not here.

---

*Retired predecessor: `07-Superseded/SCH_Project_Governance_Charter_v2.md`, preserved in full as the governance record of the Track A/Track B period (adopted June 2026, revised June 2026).*