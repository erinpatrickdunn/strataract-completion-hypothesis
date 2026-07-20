### The Reproducibility Standard

**Statement.** A load-bearing result — one that other conclusions in the project depend on — requires a second, genuinely independent derivation route before it may be certified at the "independently confirmed" evidence level (see `Evidence-Classification.md`). "Independent" means no shared derivational ancestry: not a re-statement of the same algebraic manipulation, but a structurally different method (e.g., explicit low-level matrix computation versus abstract algebraic peeling).

### Rationale

Two derivations that share a common intermediate step are not independent confirmations of each other — they are one derivation checked twice. If the shared step is wrong, both "independent" derivations will agree and be wrong together. Genuine independence requires a method with no common point of failure.

### Case History

The clearest demonstration in this project: the S-row and P-row of the Fierz system were each derived by two distinct methods and found to agree (`Foundations Notebook A4b2`) — a genuine reproducibility win. By contrast, the V-row and A-row initially shared a single derivational pipeline (one Clifford sandwich calculation inserted into one general self-Fierz identity), and their mutual agreement was correctly flagged as *not* constituting independent confirmation — "siblings, not cousins," in the language used at the time. When the tensor row ($\lambda_T$) was later derived by explicit matrix computation with genuinely no shared ancestry to the Clifford-peeling method, it exposed a real sign error in the peeling derivation, resolving a standing factor-of-3 contradiction in the involution check. This is the single clearest case in the entire reconstruction of the Reproducibility Standard doing its job: an error that survived one derivation and its naive "check" was caught only by a structurally unrelated second method.

### Application Rule

Before any result is entered into a project status table as "independently confirmed," the second derivation route must be checked against this standard: does it share a critical intermediate step with the first? If yes, the result remains at "single derivation" confidence regardless of how many times it has been recomputed by the same method.

---
