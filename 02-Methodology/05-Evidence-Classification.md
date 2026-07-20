### Evidence Classification

**Statement.** A derived result carries one of the following confidence levels, and the level must be stated alongside the result:

| Level | Meaning |
|---|---|
| **Single derivation** | Derived once, by one method, no cross-check attempted. |
| **Double-derived** | Derived independently by two distinct methods (e.g., algebraic conjugation and explicit matrix computation), both reaching the same result. |
| **Matrix/numerically confirmed** | Cross-checked against an explicit, low-level computation with no shared derivational ancestry with the original method. |
| **Documented vs. existent** | A distinct axis, orthogonal to the above: whether a result is *shown* in a given document, independent of whether it is *true*. |

### Rationale

Not all results in this project were established to the same standard, and presenting them uniformly as "established" would misrepresent that. The evidence-classification table format (used throughout `Reconstruction_Master_Report_v1.md`, Part V) exists so that a reader six months later can ask "established relative to what confidence level" and get an answer directly from the document, rather than needing to re-derive the provenance.

### Case History

`Foundation-A-Closed-v1.0`'s certificate distinguished exactly this way: parity and the chiral rotation were marked **"Closed (single derivation)"** while the Fierz S/P/V/A/T rows were marked **"Independent confirmation"** (double-derived and matrix-confirmed) — following the discovery, during actual use of the system in Foundation B, of a transcription sign error in the *single-derivation-confidence* summary table, which had never been cross-checked at the level the higher-confidence rows had been. This is the direct empirical justification for maintaining the classification: the error occurred precisely in a lower-confidence-tier result, and was caught only when a downstream notebook attempted to build on it (`Foundation-A-Closed-v1.1` erratum).

### Application Rule

Every results table in the project (per `Evidence-Classification.md`, mirroring `Reconstruction_Master_Report_v1.md` Part V's three-column format: Result / Reconstruction Status / Dependency) must indicate, at minimum, whether a result is single-derived or independently confirmed, so that future work knows where the residual risk of an unfound error is concentrated.

---
