# `01-Governance`

This folder contains the project's rules for how the repository operates: who has authority to change what, what process a result must pass before it enters the canonical record, and how the project's own governance documents are themselves revised and corrected.

**This folder does not contain scientific claim classifications.** If you're looking for the current status of a specific theorem, coefficient, or derivation, see `02-Methodology/SCH_Claim_Classification_Framework_v1.md` for the classification system and `03-Reconstruction/` or `04-Canonical-Theory/` for its application to specific claims. This separation is itself a governance rule (see below) — this README will not drift back into tracking theory content, and if you find it doing so, that's a sign something has been misfiled.

## Why This Exists

Read `SCH_Project_Governance_Charter_v3.md` for the current rules. The charter exists because this project has a documented history of results migrating into the canonical record before they were independently confirmed — and, separately, of governance documents themselves accumulating theory-specific content until they could no longer function as governance. The charter is the structural fix for both problems.

## What Changed in v3

Earlier versions of this charter (see `07-Superseded/SCH_Project_Governance_Charter_v2.md`) combined governance with a live snapshot of the theory: which sectors were "Track A" versus "Track B," a specific coefficient's confirmed value, a dependency map for one part of the corpus. That content required the charter to be rewritten every time the physics moved — which meant it was functioning as a reconstruction report wearing governance's name, not as governance.

v3 removes all theory-specific content. What remains is purely structural:

- **The Repository Authority Map** — what each of the seven top-level directories is responsible for, and the rule that no directory does another's job.
- **The Reconstruction Firewall** — reconstruction may find gaps in the theory's documented derivations; it may not fix them. Fixes belong in `05-Alternatives/` until independently reviewed.
- **The Immutability Principle** — canonical documents are historical records. Corrections happen through versioned replacement, not in-place editing; superseded versions are preserved in full.
- **The Four-Question Rule** — what must be answered in writing, before an edit is made, before any result enters `04-Canonical-Theory/`.
- **The Audit Trail Principle** — the record of what was tried and what failed is part of the deliverable, not discarded once a clean answer is reached.
- **Self-correction rules for the charter itself**, and a rule for when the charter needs a new version at all (structural changes only — never a theory update).

## On Reading the Charter's Own History

The charter has, at least once, been wrong about its own status — v1 listed a derivation as confirming a result before that derivation had actually been written down, and v2 corrected this in the open rather than quietly. v3 preserves this precedent explicitly (§6, Self-Correction of Governance) as the standing example of the principle, stripped of the specific coefficient it originally concerned, because the lesson is about governance discipline, not about that sector of the theory.

This is deliberate: the charter is not exempt from its own rules. If you're checking whether a claim in this repository is truly settled, the place to look is no longer this folder — it's `02-Methodology`'s classification framework applied via `03-Reconstruction`'s audits. What this folder guarantees is that *when* a claim is checked, the Four-Question Rule was actually followed, and that the record of how it was checked hasn't been quietly overwritten.

## Version History

Older versions of the charter move to `07-Superseded/` when a new version replaces them, retained in full, not edited in place, with the revision note in the new version explaining exactly what changed and why. `SCH_Project_Governance_Charter_v2.md` is filed there now, as the governance record of the project's Track A/Track B period.
