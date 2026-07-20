### The Documentation Principle

**Statement.** When auditing a theoretical derivation, distinguish:

1. the mathematical existence of a derivation,
2. the explicit documentation of that derivation in the corpus,
3. the uniqueness of that derivation.

Evidence for (2) is not evidence for (1), and failure to establish (2) is not evidence against (1).

### Rationale

A corpus document can assert a correct result while failing to document its derivation, and it can document a derivation that is not the only one possible. Auditing without this distinction collapses three separate questions ("is it true," "is it shown," "is it the only way") into one, producing overclaims in both directions: treating an undocumented assertion as false, or treating a documented derivation as definitive.

### Case History

Applied against Appendix P Theorem 6 and §P.11.2 (`Reconstruction_Master_Report_v1.md`, Parts II–III): both state effective-potential forms "from $S_{\rm geo}$" with no shown Hubbard–Stratonovich transform, fermion determinant, or regularization. The correct finding is **"no derivation is documented within the cited proof"** — not "the stated potential is wrong." The reconstruction independently constructed a documented A→B→C chain (Part IV) and found it does not reproduce either stated potential; this shows a *discrepancy between constructions*, not a refutation of the corpus's physical claim.

A second, self-referential instance: an early draft of this reconstruction asserted a Fierz-derived coefficient "cannot originate from Object B at all," a claim about non-existence based only on the absence of a single constructed derivation. Corrected to "does not arise within the explicit Object-B construction carried out in this reconstruction" — see `Scope-Principle.md` for the companion correction.

### Application Rule

Any statement of the form "X is not derived" appearing in project documents must specify *within which document or construction* X is not derived. A bare claim of non-derivation, without that qualifier, does not meet the Documentation Principle and should be flagged for revision on sight.

---
