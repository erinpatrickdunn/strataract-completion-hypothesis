### Derivation Requirements

**Statement.** A Category-2 (Derived) step is only valid if every intermediate line is shown. Phrases that substitute for an intermediate line — "it follows that," "one finds," "by standard manipulation," "clearly" — do not satisfy this requirement and mark the step as incomplete until the intermediate algebra is supplied.

### Rationale

Reconstructing SCH's fermion sector repeatedly found that corpus claims failed not at the level of wrong conclusions but at the level of *skipped steps that turned out to conceal an unstated choice*. A skipped step is not neutral — it is exactly where a Category-3 assumption can enter without being flagged as one.

### Case History

The original attempt to derive the fermion determinant reduction via the standard NJL companion-operator trick $(i\partial\!\!\!/-M)(i\partial\!\!\!/+M)$ failed silently when tried in full: the cross term $[M,\gamma^\mu]\partial_\mu$ does not vanish because $M$ contains $\gamma^5$, which anticommutes rather than commutes with $\gamma^\mu$. This was only caught because the full multiplication was carried out explicitly rather than asserted by analogy to the standard chiral-rotation argument (`Foundation-B-Result-B2`, point 3). The corrected route ($\bar M=(m+\sigma)-i\gamma^5\pi$, with $p\!\!\!/\bar M=Mp\!\!\!/$ shown by direct computation) is the version retained in `Reconstruction_Master_Report_v1.md`, Part IV.2.

A second case: the tensor-sector Fierz eigenvalue $\lambda_T$ was initially derived via Clifford-algebra peeling and asserted with an unverified extrapolation from lower-rank contractions; flagged explicitly as uncertified rather than presented as complete (`Foundations Notebook A4c`). The subsequent explicit-matrix derivation (`A4e`) found the peeling argument had the wrong sign — caught only because the earlier notebook had refused to skip the verification step and paper over the gap.

### Application Rule

Any derivation submitted to this project that contains an unjustified transitional phrase must be returned for completion before its result can be entered into a status table as "established."

---
