# SCH Project Wide Audit Protocol v1

---

## One placement correction before drafting

Per `01-Governance/SCH_Project_Governance_Charter_v3.md` §1 (Repository Authority Map): `02-Methodology` defines *how* claims are evaluated; `03-Reconstruction` *applies* that evaluation to recover the corpus's actual derivational content. A project-wide audit's **protocol** (this document) belongs in `02-Methodology` — it's a procedure definition. The audit's **findings** (the six-phase execution, the final status ledger) are an application of that procedure to the actual corpus, and per the authority map that's `03-Reconstruction`'s job, not Methodology's. So:

```
02-Methodology/SCH_Project_Wide_Audit_Protocol_v1.md    ← this document
03-Reconstruction/SCH_Project_Wide_Audit_Report_v1.md   ← the executed findings
```

This isn't pedantry — it's the Reconstruction Firewall operating exactly as designed: a protocol that defines evaluation criteria is methodology; a report that says "Theorem 4's transport claim does not survive audit" is a finding about the corpus, which is reconstruction's domain. Keeping them in separate directories preserves the same firewall that prevents reconstruction from silently becoming revision.

## A second correction: classification vocabulary

The six-phase proposal introduces a classification tier set (Derived / Conditional / Empirical / Speculative / Retired). This would be a second, competing claim-classification vocabulary alongside `SCH_Claim_Classification_Framework_v1.md`'s three-layer model (Claim Status / Scope / Evidence). Per the Documentation and Scope Principles, introducing a second vocabulary for the same purpose is exactly the kind of silent duplication this project's methodology exists to prevent. The audit will use the **existing** framework, not a new one. Mapping, once and for all:

| Proposed tier | Maps to (existing framework) |
|---|---|
| Derived | `Claim Status: ESTABLISHED` |
| Conditional | `Claim Status: CONDITIONAL — PROVENANCE UNDOCUMENTED` or `CONDITIONAL — DOWNSTREAM DEPENDENCY` (per which applies) |
| Empirical | Not a Claim Status — this is `Layer 3: Evidence`, specifically `Empirical: Independent replication` or `Empirical: Experimental confirmation`, layered on top of whatever Claim Status the underlying theoretical claim carries |
| Speculative | `Claim Status: OPEN` |
| Retired | `Claim Status: SUPERSEDED` |

This mapping is used throughout the protocol below instead of the proposed five-tier table.

---

## Purpose

Determine the current logical, mathematical, empirical, and governance status of every active claim in the corpus, without modifying canonical theory, by applying the existing Methodology framework project-wide rather than sector-by-sector as has been done to date (fermion sector only, via `Reconstruction_Master_Report_v1.md`).

## Governing constraints

This protocol operates entirely within the existing governance and methodology apparatus. It does not introduce new authority, new classification vocabulary, or new principles. Every phase below cites the existing document that governs it.

---

## Phase 1 — Repository Integrity Audit

**Question:** Is the project internally organized according to its own governance?

**Checks, each tied to an existing governance rule:**
- Every document declares a Claim Status per `SCH_Claim_Classification_Framework_v1.md` — or is flagged as not yet classified. (Note: most of `04-Canonical-Theory` currently uses legacy labels, not this framework — see the Mapping table already provided there; Phase 1 checks *that a mapping has been attempted*, not that every document has been reclassified, which is Phase 2's job.)
- Superseded documents are actually retired to `07-Superseded/` and untouched thereafter (Immutability Principle, Governance Charter v3 §3).
- `03-Reconstruction` documents contain no claim that modifies canonical theory in place — only findings about it (Reconstruction Firewall, §2).
- `05-Alternatives` documents are not cited as if canonical anywhere in `04-Canonical-Theory`.
- Every claim addressed by any reconstruction report cites the construction it was derived within (Scope Principle) and the derivation route (Four-Question Rule, Question 1–2).

**Output:** A governance compliance report — pass/fail per check, with specific document citations for any failure. This is a structural check, not a scientific one; it does not evaluate whether any claim is true.

---

## Phase 2 — Claim Inventory Audit

**Method:** Every atomic claim (per the Atomic Claim Principle, `SCH_Claim_Classification_Framework_v1.md`) in `04-Canonical-Theory` is assigned Claim Status, Scope, and Evidence, using the existing three-layer model — not a new tier system. Compound claims (a theorem bundling a definition, a derivation, and a numerical estimate) are decomposed first, per the worked example already on file for Theorem 0.

**Explicit purpose, stated to prevent a known failure mode:** this phase exists specifically to catch the pattern already observed once — a mechanism being treated as established because it appears, cited approvingly, across multiple documents, without any single document actually carrying its derivation. Citation count is never evidence; only a traced derivation chain is (Documentation Principle).

**Output:** A claim inventory — one row per atomic claim, its Status/Scope/Evidence, and the specific document/section it was extracted from.

---

## Phase 3 — Reconstruction Consistency Audit

**Question:** What claims survive when all derivational dependencies are traced — not "which formulation is correct."

**Scope:** This phase generalizes the method already executed for the fermion sector (`Reconstruction_Master_Report_v1.md`, Parts II–V) to the rest of the corpus, in particular the sectors flagged as inconsistent: §P.7 statements, §P.9 constraints, §P.11's potential, and Theorem 6's coefficients — checking whether these descend from a single, traced $V(\eta,P)$ or from independently-asserted forms, exactly as the fermion-sector reconstruction already found for Theorem 6 vs. §P.11.2.

**Method:** Apply the Comparability Protocol before any cross-sector comparison: state what each sector's stated potential computes, what's built in as definition vs. approximation, and whether they share a licensed domain of comparison before treating any disagreement as a contradiction.

**Output:** Per dependency chain — preserved derivations (Claim Status `ESTABLISHED`, full chain shown), missing derivations (`CONDITIONAL — PROVENANCE UNDOCUMENTED`), genuine contradictions between two independently-derived (not merely independently-asserted) results, and unresolved choices (multiple valid representations, none singled out by the action — as already found for the $\eta^2$/$P^2$ completion question).

---

## Phase 4 — Physical Mechanism Audit

**Question:** For each major physical mechanism claimed in the corpus, is the mathematical chain from action to mechanism complete, per the same A→B→C standard used in the fermion-sector reconstruction (`Reconstruction_Master_Report_v1.md` Part IV)?

**Named sectors requiring this check** (from corpus extraction, not exhaustive — Phase 4 execution will identify others):

- **Condensate carrier/transport sector** (Appendix P Theorem 4, superseded by Theorem 4a/4b, §P.11): is the $\delta\eta$/$\delta P$ carrier derivation complete? Does the retracted diffusion formula's replacement (the damped relativistic wave equation) itself meet the Documentation Principle, or does it inherit the same gap pattern found in Theorem 6/§P.11.2? **Predicted likely outcome, stated as a hypothesis for the audit to check, not asserted here:** the transport *mechanism*'s existence may be `ESTABLISHED` while its specific *magnitude* (frequency table, propagation timescale) may need reclassification to `SUPERSEDED` or `OPEN`, consistent with Appendix P v16's own retraction notice at §P.7.5.2, which already does this self-correction — the audit's job here is largely to confirm the corpus's own retraction is complete and consistent, not to independently discover it.

- **Gravity coupling sector — Picture 1 vs. Picture 2 (Appendix P §P.12.1):** the corpus itself already flags this fork explicitly ("Two distinct uses of η exist... and must not be conflated"). This is not a new finding to make; it is a documented ambiguity to formally classify. Phase 4's job is to determine, for every downstream claim depending on $\eta$, which picture it actually uses, and flag any claim that switches pictures mid-derivation without saying so — a specific instance of the Scope Principle's "scope is never enlarged by omission" rule.

**Output:** Per mechanism — a completed A→B→C-style chain where one exists, or a specific halt point (Derivation Outcome: Complete/Halted/Abandoned) where it doesn't, per `Category-Discipline.md`'s Derivation Outcome taxonomy.

---

## Phase 5 — Empirical Program Audit

**Question:** Is the mapping from SCH variables to each empirical program's observables mathematically defined — not whether the empirical program supports SCH.

**Explicit non-goal, stated per the Documentation Principle's discipline:** this phase does not evaluate statistical significance, does not judge whether a correlation is "real," and does not rule on any pending experiment's outcome. It checks only whether the theoretical mapping used to interpret that data is itself derived or asserted.

**Buckets, using existing Evidence-Classification categories (not new tiers):**
- **Completed/analyzed** (`Evidence: Empirical — Independent replication` candidates): MaNGA rotational coherence staircase, JAM/NFW pipeline — check whether the SCH-side variable ($\lambda_R$, $\beta_z$, the RAR residual mapping) is itself derived from $C_{\mu\nu}=\rho\eta u_\mu u_\nu$ with a traced chain, or asserted as a proxy.
- **Pending** (`Claim Status: OPEN`, with a stated resolving observation): DES Y6 weak lensing, Bi-209 calibration.
- **Exploratory** (`Claim Status: OPEN`, Scope: prerequisite chain incomplete): DESI growth-of-structure — cross-check against Appendix P §P.12's own closure finding (screening length $\lambda_{\rm coh}\approx0.1$m, condensate sector screened out of survey-relevant scales) before treating this as open; §P.12 may have already closed it, in which case Phase 5's job is to confirm that closure is itself sound, not to re-open a settled question by default.

**Output:** Per empirical program — whether the SCH-to-observable mapping is `ESTABLISHED` (derived) or `CONDITIONAL`/`OPEN` (asserted proxy, unfixed parameter, or unresolved picture-1/picture-2 ambiguity per Phase 4).

---

## Phase 6 — Final Status Ledger

**Format**, using the existing three-layer model rather than the proposed ad hoc five-column table:

| Claim | Location | Claim Status | Scope | Evidence |
|---|---|---|---|---|
| *(one row per atomic claim from Phase 2, updated by Phases 3–5 findings)* | | | | |

This ledger is the single consolidated output of the full audit, filed as `03-Reconstruction/SCH_Project_Wide_Audit_Report_v1.md` per the placement correction above — it is the *application* of this protocol to the corpus, not part of the protocol itself.

---

## Expected character of the result

Per the Documentation Principle: a finding of "provenance undocumented" for a given sector is not a finding that the sector is wrong, and this protocol's execution should not be read or written as a validation/invalidation exercise. The realistic and intended output is a corpus mapped into `ESTABLISHED`, `CONDITIONAL` (two subtypes), `SUPERSEDED`, and `OPEN` claims with their dependencies traced — not a verdict on SCH as a whole.

## Governing citations

This protocol is executed under: `Documentation-Principle.md`, `Scope-Principle.md`, `Comparability-Protocol.md`, `Category-Discipline.md`, `Evidence-Classification.md`, `Derivation-Requirements.md`, `Reproducibility-Standard.md`, `SCH_Claim_Classification_Framework_v1.md` (all `02-Methodology`), and the Four-Question Rule, Reconstruction Firewall, and Immutability Principle (`01-Governance/SCH_Project_Governance_Charter_v3.md`). No new principle is introduced by this protocol; it is a procedural sequencing of existing ones, applied at project scope rather than single-sector scope.

---

Ready to begin Phase 1 (Repository Integrity Audit) whenever you'd like — it's the cheapest phase and establishes whether the rest of the audit can proceed on a sound structural footing, consistent with how the fermion-sector work always checked its foundation before building on it.
