# SCH Working Directory — Index

*Maintained index of all documents in /papers/working/. Updated whenever a
document is added, closed, or superseded. This file is the entry point for
navigating the calculational programme — start here before searching the
directory.*

**Last updated:** June 2026 (following PT-1 analysis programme and Appendix P v12 revision)

---

## How to Read This Index

Each entry lists: filename, status, what it depends on (prerequisites), what
depends on it (unlocks), and a one-line summary. Status values:

- **OPEN** — active working document, not yet incorporated into the canonical papers
- **CLOSED** — results verified and migrated into Appendix P or a Paper; document retained as derivation record
- **SUPERSEDED** — replaced by a later working document; retained for history
- **BLOCKED** — cannot proceed until a prerequisite closes

Canonical papers (`/papers/Paper_A.md`, `Paper_B.md`, `Paper_C.md`, `Appendix_P.md`)
are never listed here — only documents in `/papers/working/` are indexed.

---

## Current Documents

### 1. `SCH_Replication_Study_WorkingPaper_v1.md`

**Status:** OPEN — awaiting external data

**Prerequisites:** None (independent empirical pipeline)

**Unlocks:** Quantitative confirmation/falsification of Paper B Section 2
(beta_z / lambda_R rotational coherence staircase)

**Summary:** Independent replication pipeline for the MaNGA rotational
coherence signal. Mid-mass tertile shows monotonic staircase (Spearman
ρ = 0.145, p = 3.6×10⁻⁷, N = 1,214). Blocked on MaNGA DAP velocity dispersion
maps (noise too high in current release) and DES Y6 Metadetection shape
catalogue (public release pending). Will be superseded by full analysis upon
data availability.

**Cited by:** Paper B Section 2 (as the empirical anchor, pending upgrade to RAR residual)

---

### 2. `SCH_CT_ix_CosmologicalDynamics_v1.md`

**Status:** OPEN — 8 IVN items outstanding

**Prerequisites:** CT-viii (CLOSED, Appendix P v11 Section P.9)

**Unlocks:** PT-1 (provides Branch 1/Branch 2 dynamical structure and the
parametric solution used in the monodromy calculation); CT-xix (provides
Phase I/Phase III boundary structure); $R_{\text{universe}}$ constraint
(Appendix P v12 Gap 16, CLOSED pending IVN); angular diameter turnaround
prediction (Paper A Section 6.8, Paper B Section 4)

**Summary:** Solves the modified Friedmann system from CT-viii. Branch 1
(torsion-free) gives two-phase dynamics: Phase I stiff-condensate
($a \propto t^{1/3}$, predicts blue-tilted GW background $n_T = -1$) and
Phase III dust-condensate (standard closed-universe parametric solution).
Derives $R_{\text{universe}} = \kappa m \eta_0 R_{\text{unit}}/3$ and the CMB
quadrupole constraint $m\eta_0 \geq 9c^4/(8\pi G)$. Branch 2 (torsion-active)
shown to asymptote to Branch 1 at late times. Five open questions identified,
most significantly OQ-CT-ix-5 (duration of matter-creation epoch relative to
$\pi/(2m)$), which directly feeds the revised PT-1 calculation.

**Highest-priority IVN items:** IVN-2 ($\eta$ dilution law derivation),
IVN-5 (full term-by-term confirmation of E1)

**Migrated to:** Appendix P v12, Gap 16 / Section P.10 (status summary only;
full derivation remains here)

**Cited by:** Appendix P v12 (Gap 16, P.10); PT-1 documents (below)

---

### 3. `SCH_PT1_ProblemSpecification_v1.md`

**Status:** CLOSED — specification complete, superseded in role by the
proof attempt and monodromy calculation, retained as the reference framing document

**Prerequisites:** CT-viii (P.9.6.4 prerequisites); Appendix P P.7.7 (original claim)

**Unlocks:** PT-1 Proof Attempt (this document defines what a valid proof must contain)

**Summary:** Decomposes the PT-1 claim ($A^\mu \to -A^\mu$ across the bounce)
into three sub-questions: spinor bundle holonomy, CPT transformation, and the
relationship between the spatial antipodal map and temporal reversal. Shows
the spatial antipodal map alone gives $A^\mu \to +A^\mu$ (wrong sign for
bilinears) — this is the key early result that redirected the entire programme.
Establishes the transformation table (Section 6) used throughout subsequent
documents. Recommends the ODE integration strategy that the Proof Attempt follows.

**Cited by:** All subsequent PT-1 documents; Appendix P v12 P.7.7.2

---

### 4. `SCH_PT1_ProofAttempt_v1.md`

**Status:** SUPERSEDED — superseded by `SCH_IVN16_Resolution_v1.md`, which
corrects a signature-convention error discovered in this document's
component-route derivation. Retained as the derivation record showing the
discovery process.

**Prerequisites:** PT-1 Problem Specification v1; CT-viii P.9.5.3 (Dirac equation)

**Unlocks:** Identification of IVN-16 (the signature-convention conflict
between the bilinear route and component route)

**Summary:** First attempt to integrate the cosmological Dirac equation
through the bounce. Derives the bilinear evolution equations for $\eta$, $J^0$,
$P$, $A^0$ via two independent routes (abstract bilinear algebra and explicit
2-component spinor algebra). The two routes disagree (IVN-16) — this
disagreement, not a finished proof, is the document's main product. Confirms
$A^0$ is continuous through the bounce with no local sign flip regardless of
which route is correct. 18 IVN items catalogued.

**Cited by:** IVN-16 Resolution v1 (as the source of the discrepancy)

---

### 5. `SCH_IVN16_Resolution_v1.md`

**Status:** CLOSED — root cause identified and corrected equations derived

**Prerequisites:** PT-1 Proof Attempt v1 (source of the discrepancy)

**Unlocks:** PT-1 Monodromy Calculation v1 (provides the correct $(A^0, P)$
system to integrate)

**Summary:** Traces the discrepancy between the two PT-1 Proof Attempt
derivations to a mixed signature convention: the bilinear route used
$(\gamma^0)^2 = -\mathbf{1}$ (correct for $(-,+,+,+)$) while the component
route implicitly used $(\gamma^0)^2 = +\mathbf{1}$ (the $(+,-,-,-)$
convention). Re-derives the $\dot{A}^0$ equation with the consistent
$(-,+,+,+)$ convention throughout, producing (E-A-correct):
$\dot{A}^0 = 2imP + i\lambda\eta P - i\kappa\alpha A^0 J^0$, with no Hubble
friction term. Flags that the Appendix P v11 P.9.3 bilinear expressions
(written in terms of 2-component $\xi, \chi$) do not reproduce standard
Dirac-representation matrices and require independent re-derivation
(IVN-D, IVN-E — still open).

**Open items carried forward:** IVN-D and IVN-E (re-derivation of the P.9.3
bilinear expressions) are not yet resolved and should be prioritised — they
affect the bilinear definitions used throughout CT-viii, CT-ix, and all PT-1 documents.

**Cited by:** PT-1 Monodromy Calculation v1; Appendix P v12 P.7.7.3

---

### 6. `SCH_PT1_MonodromyCalculation_v1.md`

**Status:** OPEN — analytic structure established; numerical evaluation
blocked on Bi-209 calibration

**Prerequisites:** IVN-16 Resolution v1 (corrected equations); CT-ix
(parametric solution for $a(t)$)

**Unlocks:** PT-1 Topological Phase Investigation v1; the revised PT-1 proof
target (Appendix P v12 P.7.7.9)

**BLOCKED on:** Bi-209 calibration (Paper A Section 5) for numerical values
of $m$, $\alpha$; OQ-CT-ix-5 for matter-creation epoch duration

**Summary:** Decouples the $(A^0, P)$ system into normal modes
$u = A^0+P$, $v = A^0-P$, each evolving as a pure $\mathrm{U}(1)$ phase.
Derives the monodromy matrix over one cosmological cycle in closed form
(equation M-final) and the exact condition for $M = -\mathbf{1}$ (chirality
inversion): $\alpha_+ = (2n-1)\pi$ for integer $n$, where $\alpha_+ =
\int_{\text{cycle}}(2m + \lambda\eta_0/a^3)\,dt$. Estimates $\alpha_+ \sim
10^{54}$ for plausible parameters — astronomically large and not naturally
quantized. Identifies the divergence near the bounce and its physical
regularisation via condensate melting at $T_c$. Concludes $M = -\mathbf{1}$
is not generic; the result is parameter-dependent and requires Bi-209.

**Cited by:** PT-1 Topological Phase Investigation v1; Appendix P v12 P.7.7.3, P.7.7.9

---

### 7. `SCH_PT1_TopologicalPhase_v1.md`

**Status:** CLOSED — systematic investigation complete; definite negative result

**Prerequisites:** PT-1 Monodromy Calculation v1 (the holonomy structure to be tested)

**Unlocks:** Final resolution of Gap 7 epistemic status (Appendix P v12);
clears the question of whether topology rescues the original PT-1 claim

**Summary:** Identifies the normal-mode evolution $u(t) = e^{i\int\Omega_+ dt}u(0)$
as a genuine holonomy and asks whether it is topologically quantized.
Systematically checks five candidate mechanisms: (1) $\mathrm{U}(1)$ bundle
topology over an interval — no constraint; (2) compactification to $S^1$ and
winding number — constrains bundle degree, not holonomy value; (3) spin
structure on the temporal $S^1$ — selects antiperiodic BC on $\psi$ via
spin-statistics, but this gives *periodic* BC on bilinears ($A^0 \to +A^0$,
wrong sign); (4) Aharonov-Bohm effect — inapplicable, no enclosed flux on a
1D base; (5) Berry phase — zero for the symmetric Branch 1 cycle and for
Branch 2 with $\mathcal{J} \neq 0$. Conclusion: the holonomy is geometrically
natural (derived from the spin connection, not ad hoc) but **not**
topologically quantized by any mechanism identified. The phase is a
continuous function of the action parameters, computable after Bi-209.

**Cited by:** Appendix P v12 P.7.7.4 (full mechanism-by-mechanism summary
incorporated directly into the canonical document)

---

### 8. `SCH_AppendixP_v12_RevisionRecord.md`

**Status:** CLOSED — applied to canonical Appendix P

**Prerequisites:** All PT-1 documents (2–7 above); CT-ix

**Unlocks:** N/A (this document is itself the migration record)

**Summary:** Records the full diff between Appendix P v11 and v12: Gap 7
status revision (PREDICTION → OPEN QUESTION — CLAIM REVISED), new Gap 16 for
CT-ix, full replacement of Section P.7.7, and new Section P.10 (CT-ix
summary). This is the document that performed the Layer 2 (Appendix P)
migration from the Layer 3 (working) results in documents 2–7. Once applied,
the changes live in `/papers/Appendix_P.md` v12; this record stays here as
the audit trail.

**Cited by:** None (terminal document in this chain)

---

### 9. `SCH_IVNDE_BilinearResolution_v1.md`

**Status:** CLOSED — canonical bilinear definitions established; downstream consistency audit initiated

**Prerequisites:** SCH_IVN16_Resolution_v1.md (identification of IVN-D/E); CT-viii Appendix P P.9.3 (original bilinear definitions)

**Unlocks:** IVN-F, IVN-G, IVN-H, IVN-I consistency audits; Appendix P v13 spinor-sector revision; re-verification of CT-viii, CT-ix, and all PT-1 documents using the corrected bilinear definitions

**Summary:** Performs a clean-room re-derivation of the scalar, pseudoscalar, vector, and axial-vector bilinears directly from the Clifford algebra and the adopted gamma-matrix convention, resolving the outstanding IVN-D and IVN-E discrepancies identified in the IVN-16 Resolution. Demonstrates that the previous Appendix P P.9.3 expressions were inconsistent with the stated Dirac representation and replaces them with canonical expressions derived independently from first principles. Propagates the corrected bilinear identities through the spinor sector, identifying which subsequent derivations remain unchanged and which require re-verification. Establishes that the principal consequence is not an immediate physical revision but a formal consistency audit of the condensate sector, with IVN-F through IVN-I opened to determine whether the corrected reality structure represents a convention change or a genuine physical reformulation.

**Open items carried forward:** IVN-F (Dirac equation consistency), IVN-G (Lagrangian reality conditions), IVN-H (physical interpretation of the condensate variables), and IVN-I (global propagation audit through CT-viii, CT-ix, PT-1, and Appendix P). The canonical bilinear definitions are considered resolved; remaining work concerns their consequences.

**Cited by:** Appendix P v13 (planned P.9.3 revision); CT-viii re-verification; CT-ix re-verification; all future spinor-sector derivations.

---

## Dependency Graph

```
CT-viii (Appendix P v11, CLOSED)
    │
    ├──> CT-ix [OPEN, 8 IVN] ──────────────────────┐
    │                                                │
    └──> PT-1 Problem Specification [CLOSED] ──┐    │
                                                 │    │
              PT-1 Proof Attempt [SUPERSEDED] ──┤    │
                       │                        │    │
                       ▼                        │    │
         IVN-16 Resolution [CLOSED] ────────────┤    │
                       │                        │    │
                       ▼                        ▼    ▼
         PT-1 Monodromy Calculation [OPEN, blocked on Bi-209 + OQ-CT-ix-5]
                       │
                       ▼
         PT-1 Topological Phase Investigation [CLOSED]
                       │
                       ▼
         Appendix P v12 Revision Record [CLOSED, applied]
                       │
                       ▼
              /papers/Appendix_P.md (v12, canonical)
```

---

## Outstanding Work Tracked From This Directory

**Highest priority (blocks the most downstream work):**

1. **IVN-D, IVN-E** (flagged in IVN-16 Resolution) — re-derive the P.9.3
   bilinear expressions with a verified, consistent gamma-matrix convention.
   This affects every document in this directory that uses $\eta$, $A^0$, $P$,
   or $J^0$. Should be done before further PT-1 numerical work, and before
   CT-ix's IVN-2/IVN-5 are considered closed.

2. **CT-ix IVN-2, IVN-5** — the $\eta$ dilution law. Load-bearing for the
   entire Branch 1/Branch 2 structure.

3. **Bi-209 calibration** (Paper A Section 5, not a working document — the
   physical experiment) — unblocks the PT-1 Monodromy numerical evaluation
   directly.

**Second priority:**

4. **OQ-CT-ix-5** — matter-creation epoch duration vs. $\pi/(2m)$. Needed
   to determine whether the revised PT-1 picture still supports a
   well-defined chirality at nucleation even without universal $M = -\mathbf{1}$.

5. **PT-3** (now primary per Appendix P v12 P.7.7.9) — multi-cycle evolution
   of $\langle A^0 \rangle$ using the monodromy matrix. No working document
   yet exists for this; it should be opened once PT-1's numerical evaluation
   is available.

**Not yet started, anticipated:**

- CT-vii (black hole condensate propagator) — prerequisite for CT-xiii and
  CT-xix; no working document yet.
- CT-xiii (photon-condensate coupling) — blocked on CT-vii.
- CT-xix (antipodal condensate coupling) — blocked on CT-vii; partially
  informed by CT-ix's Phase I/III structure.
- CT-xx (thermodynamic consistency of coherence-forcing) — blocked on CT-xix.
- PT-2 (Bogoliubov analysis) — blocked on PT-1 numerical result.
- CT-xiv through CT-xviii (Paper C particle-scale targets) — independent of
  the cosmological chain above; no working documents yet exist for these.

---

## Filing Convention for New Documents

Use the pattern `SCH_{topic}_{type}_v{N}.md`:

- **topic**: the CT/PT/Gap identifier or subject (e.g. `CT_ix`, `PT1`, `IVN16`)
- **type**: the document's role — `ProblemSpecification`, `ProofAttempt`,
  `Resolution`, `MonodromyCalculation`, `CosmologicalDynamics`,
  `RevisionRecord`, `WorkingPaper` (for empirical pipelines)
- **v{N}**: explicit version number, incremented on revision, never overwritten

When a document closes and its results migrate to a canonical paper, add a
one-line header to the top of the working document: *"SUPERSEDED/CLOSED.
Results incorporated into [Paper/Appendix] vN, Section X. Retained as
derivation record."* Update this index entry's status accordingly. Never
delete a working document once it has been cited.

Update this index in the same commit/session that adds, closes, or supersedes
any document in this directory.

---

*Working Directory Index — v1 | June 2026*
