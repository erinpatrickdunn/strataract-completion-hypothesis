### Category Discipline

**Statement.** Every equation appearing in a derivation is labeled as exactly one of:

- **Category 1 (Definition):** pure notation, no physical content, reversible with no loss of information.
- **Category 2 (Derived identity):** obtained from prior Category 1/2 statements by an explicit, checkable calculational step. No step may be skipped with "it follows that" or "one finds" without the intermediate line shown.
- **Category 3 (Hypothesis):** an explicitly flagged physical assumption not derived from the frozen action, stated as "We hypothesize that..." and never presented as a consequence of the action.

Any statement not clearly assignable to one of these three halts the derivation at that point, pending reclassification.

### Worked Examples

**C1 example:** $\eta\equiv\bar\psi\psi$. Pure notation.

**C2 example:** the Fierz sandwich formula's derivation from the swap operator $P=\frac1n\sum_A\Gamma_A\otimes\Gamma^A$, with the trace-orthonormality contraction shown explicitly rather than quoted (`Foundations Notebook 3`, A4a). Every intermediate line — the expansion coefficient, the trace evaluation, the final coefficient — appears in the derivation; none is asserted by pattern-matching to a remembered formula.

**C3 example, correctly flagged:** the original Target-0 Constitution's explicit statement that regularization requires "a Category-3 hypothesis not supplied by $S_{\rm geo}$ as frozen" (`Target-0 Reconstruction`, §5) — the derivation halted at exactly this point rather than silently picking a regulator.

**C3 example, incorrectly *un*flagged (found and corrected):** Appendix P §P.11.2's tree-level potential $V(\eta,P)=\frac{\mu^2}2(\eta^2+P^2)+\ldots$ is presented in the source document without a C3 flag, despite the $(\eta^2+P^2)$ completion and the additional quartic term both being unlabeled physical choices not derived from $S_{\rm geo}$ within the cited proof (see `Documentation-Principle.md` case history). This is the primary motivating example for why category tagging must be applied to *corpus* documents during audit, not only to newly generated derivations.

### Application Rule

Any newly written derivation in this project must carry category tags inline. Any corpus document under audit must have its key equations retroactively tagged during the audit process, with un-flagged C3-type content explicitly surfaced as a finding (see `Reconstruction_Master_Report_v1.md`, Part VI).

---
