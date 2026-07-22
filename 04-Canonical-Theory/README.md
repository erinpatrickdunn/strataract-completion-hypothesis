# `04-Canonical-Theory` 

## The Current Statement of the Framework

Everything in this folder is **Tier 1** per the project's governance
charter: it has cleared the bar the project is willing to defend
unqualified, in the sense defined in `governance/`. Nothing here is
final in the sense of unrevisable — physics documents in particular are
expected to gain new drafts over time — but everything here is the
*current* statement, not a provisional or historical one.

## The Core Papers

| Document | What it is |
|---|---|
| `Paper_A_Draft_2_5.md` | The framework itself: the physical picture, the modified field equation, its derivation, and the primary falsifiable predictions. Start here. |
| `Paper_B_Draft_1_9.md` | The empirical and observational programme: computed results from public data, consistency checks, and proposed tests with stated falsification conditions. |
| `Paper_C_Draft_1_4.md` | An extension to the particle scale: a conditional, parameter-free prediction for a B-meson decay anomaly, contingent on a single calculational target. |
| `SCH_Appendix_P_v17.md` | The full formal derivation: the action, the variational closure, every theorem, and the complete resolution record for the cosmological chirality sector. |

Each of these carries its own revision history at the top of the
document — what changed from the previous draft, and why. That history
is the fastest way to find out what's recent.

## Supporting Derivations (Companion Documents Pending Canonical Review as of Jul-22-2026)

| Document | What it is |
|---|---|
| `SCH_CT-viii_FLRW_Reduction_v1.md` | The full FLRW reduction of the action on $S^3 \times \mathbb{R}$ — the derivation behind Appendix P Section P.9. |
| `SCH_CT-viii_Independent_Replication_Report_v1.md` | Independent verification of the above. |
| `SCH_GalacticEngine_PhysicalPicture_v1.md` | The physical-picture document motivating the galactic engine mechanism (Paper A Section 2.11) and its two open calculational targets. |
| `SCH_PT1_TopologicalPhase_v1.md` | The investigation ruling out topological quantization mechanisms for the cosmological chirality holonomy phase (Appendix P Section P.7.7.4). Its conclusion is cited directly and is unaffected by the coefficient resolution in Appendix P v14. |

## What Gets a Document Moved Out of Here

A document leaves `canonical/` for `superseded/` the moment a newer
draft supersedes it — not before, and not gradually. There is
deliberately no intermediate state where two versions of the same
document are both "kind of current." Check the revision-history note
at the top of any document here for exactly what it supersedes; the
superseded version is filed under the matching paper's subfolder in
`superseded/top-level-superseded/`.

Nothing in this folder depends on unresolved work currently in
`track-b/` for its *qualitative* claims. Where a document here states a
result whose *numerical* value is still pending (overwhelmingly: the
Bi-209 calibration), that dependency is stated explicitly in the
document itself.
