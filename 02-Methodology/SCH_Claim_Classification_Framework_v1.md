# SCH_Claim_Status_Framework_v1

---

## Purpose

The existing SCH corpus (`04-Canonical-Theory`) labels claims with an ad hoc vocabulary — THEOREM, DERIVED, CLOSED, CONJECTURE, PREDICTION, EXPLORATORY, ESTABLISHED, DIM. ESTIMATE, and others, applied inconsistently across Papers A/B/C and Appendix P's many revisions. This framework replaces that ad hoc vocabulary with a controlled set of status labels, each with a precise meaning tied directly to the six principles in `02-Methodology/`, so that reclassifying a corpus claim is a mechanical act of checking evidence against a fixed definition rather than a fresh editorial judgment each time.

This framework does not itself reclassify anything. It defines the labels. Application to specific claims occurs in `Reconstruction_Master_Report_v1.md` Part VI and in future audit passes.

---

## The Status Vocabulary

### 1. `ESTABLISHED`

**Definition.** A Category-2 derivation exists, is fully documented (no skipped steps, per `Derivation-Requirements.md`), and has met the Reproducibility Standard (independently confirmed by a structurally distinct second method, per `Reproducibility-Standard.md`) — **or** is explicitly marked `ESTABLISHED (single derivation)` if it has not yet met the reproducibility bar.

**Required annotation.** Every `ESTABLISHED` claim must cite: (a) the construction it was derived within (Scope Principle), (b) its evidence-classification tier (`Evidence-Classification.md`).

**Example from this reconstruction:** the closed Fierz system (`Foundation-A-Closed-v1.1`) — `ESTABLISHED`, independently confirmed (double-derived and matrix-verified for every channel except the parity/chiral-rotation rows, which remain `ESTABLISHED (single derivation)`).

### 2. `ESTABLISHED — CONSTRUCTION-SCOPED`

**Definition.** A result is `ESTABLISHED` by the criteria above, but only within one specific, named construction, with no claim (and explicit disclaimer) that it generalizes. This label exists specifically to prevent the Scope Principle violation this project has twice committed and corrected.

**Required annotation.** Must state explicitly what would be required to lift the scope restriction (i.e., what a generalizing derivation would need to show).

**Example:** Reconstruction Finding 1 (Mean-Field Fierz Dependence, `Reconstruction_Master_Report_v1.md` IV.3) — established for the one-fermion-loop, PSC-reduced Target-0 object; explicitly not shown to hold for every mean-field realization or for the exact theory.

### 3. `CONDITIONAL — PROVENANCE UNDOCUMENTED`

**Definition.** A claim is stated in the corpus as if derived, but the corpus does not document the derivation chain from the frozen action to the stated result (Documentation Principle: failure of criterion (2), existence (1) neither confirmed nor denied). This is the label for claims found in Part II (Corpus Extraction) that could not be matched to a documented A→B→C chain in Part IV.

**Required annotation.** Must state precisely which step is undocumented (e.g., "no HS transform shown," "quartic term unaccounted for in constructed Object B") — not a bare "undocumented," per the Documentation Principle's application rule.

**Distinguishing from `ESTABLISHED — CONSTRUCTION-SCOPED`:** the latter has a complete, shown derivation restricted to a narrow scope; the former has *no* complete shown derivation at all, regardless of scope.

**Examples:** Appendix P Theorem 6 (missing the entire HS/determinant/regularization chain); §P.11.2's GMOR potential (missing derivation, plus a quartic term unaccounted for even in the reconstruction's own constructed Object B).

### 4. `CONDITIONAL — DOWNSTREAM DEPENDENCY`

**Definition.** A claim does not itself require reclassification under any other label, but depends on an input (a parameter, a background value) whose own provenance is `CONDITIONAL — PROVENANCE UNDOCUMENTED` or worse. The claim's *own* derivation structure is not in question; its status is entirely inherited.

**Required annotation.** Must name the upstream claim(s) it depends on.

**Example:** Paper C §2.1's leptonic mass shift $\delta m_\ell=\alpha\eta m_\ell$ — the mass-proportionality derivation is sound on its own terms, but $\eta_{\rm eq}$ is taken as external input from Theorem 6/§P.11.2, both `CONDITIONAL — PROVENANCE UNDOCUMENTED`.

### 5. `SUPERSEDED`

**Definition.** A claim was once presented as established or conditional, and a later document or reconstruction step has replaced it with a corrected version. The original is retained in the record (per `Documentation-Principle.md`'s provenance-preservation practice) but is not to be cited as current.

**Required annotation.** Must cite the superseding document/version and, where relevant, the reason (erratum, corrected derivation, resolved ambiguity).

**Example:** `Foundation-A-Closed-v1.0`'s certificate table (superseded by `v1.1` following the sign-transcription erratum); the original Fierz S-row derivation before its involution-check correction.

### 6. `OPEN`

**Definition.** A well-posed question has been identified and precisely stated, but no derivation — successful or unsuccessful — has been attempted or completed within this project's scope.

**Required annotation.** Must state what a resolving derivation would need to show, and (if applicable) which Phase-II track it belongs to.

**Examples:** whether the exact (untruncated) theory is Fierz-invariant; whether an alternative A→B→C construction (CJT/2PI, large-$N$) reproduces Appendix P's stated potentials; whether the PSC argument transfers to §P.9's constrained cosmological system.

### 7. `HALTED — CATEGORY 3 REQUIRED`

**Definition.** A derivation was carried as far as Category-1/2 steps permit and reached a specific, identified point where it cannot proceed without an explicit, unjustified physical assumption (a Category-3 hypothesis). This is distinct from `OPEN`: a halted derivation has a *located* obstruction with a documented chain leading up to it; an open question may not yet have any attempted derivation at all.

**Required annotation.** Must state the exact point of the halt and what kind of Category-3 input would resolve it (e.g., "a regularization scheme and UV scale, neither supplied by $S_{\rm geo}$").

**Example:** Target 0's UV-divergence halt (`Reconstruction_Master_Report_v1.md` IV.4) — the derivation reaches a fully specified but UV-divergent $F\big((m+\sigma)^2+\pi^2\big)$ and cannot produce a finite $\Gamma_{\rm MF}$ without a regulator choice external to the frozen action.

---

## Mapping from the Legacy Corpus Vocabulary

For reference during the audit pass, approximate correspondence between existing Appendix P / Paper A–C labels and this framework (to be confirmed claim-by-claim, not applied automatically):

| Legacy label | Typical correct mapping | Caveat |
|---|---|---|
| THEOREM / CLOSED (with full proof shown) | `ESTABLISHED` | Verify Reproducibility Standard was actually met, not just claimed |
| THEOREM / CLOSED (potential/GMOR-type, no shown HS/determinant chain) | `CONDITIONAL — PROVENANCE UNDOCUMENTED` | This is the primary reclassification target identified in Part VI |
| DERIVED (dimensional estimate only) | `HALTED — CATEGORY 3 REQUIRED` or `OPEN`, depending on whether a specific obstruction was located | Check whether "derived" meant Category-2 or just dimensional analysis |
| PREDICTION / CONJECTURE | `OPEN` | Usually already appropriately hedged in the corpus; confirm no stronger claim is smuggled in nearby text |
| EXPLORATORY | `OPEN`, typically with additional prerequisite chains noted | Often already correctly labeled |
| Superseded working papers (e.g. earlier PT-1 monodromy versions) | `SUPERSEDED` | Corpus is generally good about this one already (IVN-I, v13→v14 notes) |

**Explicit non-goal:** this mapping table is a starting heuristic for the audit pass, not a substitute for it. Each legacy-labeled claim must still be checked individually against the seven definitions above before being relabeled — per the Documentation Principle, a plausible-looking mapping is not itself evidence of correct classification.

---

## Application Rule

Every claim addressed in any future audit of `04-Canonical-Theory` must receive exactly one of the seven labels above, with its required annotation. A claim that does not cleanly fit one label (e.g., partially documented, partially independent) should be split into sub-claims until each piece fits — mirroring the Category-Discipline rule that an unclassifiable statement halts progress until reclassified, not smoothed over.

---
