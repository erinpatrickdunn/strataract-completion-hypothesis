# The Strataract Completion Hypothesis (SCH)

**A modified gravitational field equation in which the geometric organisational
state of matter — the coherence of w-axis spin in a four-dimensional soliton
picture — sources gravitational effects beyond mass-energy alone.**

This repository contains the working papers, formal derivations, and
calculational programme for SCH: a multi-scale theoretical framework spanning
particle physics, nuclear physics, galactic dynamics, and cosmology, together
with the falsification tests and empirical pipelines used to evaluate it
against existing data.

**This is a hypothesis under active development, not an established theory.**
Every claim in this repository carries an explicit epistemic status — theorem,
derived result, prediction, conjecture, or open question — and every major
prediction carries a stated falsification condition. The project is organised
specifically to make it easy to tell which parts of SCH are settled
mathematics, which are open calculational targets, and which have already
been tested against data.

---

## Start Here

If you read one thing, read **Paper A**. It states the physical picture in
plain language (Section 0, no equations) before giving the mathematical
encoding. Understanding Section 0 of Paper A is sufficient to understand what
SCH claims; the rest is precision.

| If you want to know... | Read... |
|---|---|
| What SCH claims, physically | `papers/Paper_A.md`, Section 0 |
| The full mathematical framework and falsifiable test program | `papers/Paper_A.md` |
| The formal proof that the framework is a closed variational theory | `papers/Appendix_P.md` |
| Empirical evidence, observational tests, and lab proposals | `papers/Paper_B.md` |
| The particle-physics extension (B-meson anomaly) | `papers/Paper_C.md` |
| What is currently being calculated, and what isn't settled yet | `papers/working/README.md` |
| What has been superseded and why | `papers/superseded/` |
| Plots, diagrams, animations | `media/` |

---

## Repository Structure

```
papers/
├── Paper_A.md              Physical framework, predictions, falsification tests
├── Paper_B.md               Empirical evidence, observational/lab proposals
├── Paper_C.md                Particle-scale extension (B-meson anomaly)
├── Appendix_P.md              Formal variational closure and proofs
│
├── working/                 Active calculational programme — NOT frozen
│   ├── README.md              Index: status, dependencies, outstanding work
│   └── ...                    Derivations, proof attempts, pipelines
│
└── superseded/               Retired drafts and superseded working documents
    └── ...                     Retained for the historical/derivation record

media/
└── ...                       Figures, diagrams, animations
```

### The Four Documents

**Paper A** — *Geometric State as a Gravitational Source Variable.* The
physical picture (matter as a 4D rotating soliton, mass as w-axis spin, the
universe as a closed $S^3$), the modified field equation, the anomaly cluster
this predicts (rotation curves, the Bullet Cluster, JWST early galaxies), and
the primary falsifiable test program. Contains a full epistemic status table
mapping every claim to AXIOM / DERIVED / THEOREM / PREDICTION / CONJECTURE.

**Appendix P** — *Proof of Closure.* The formal Einstein-Cartan-Dirac action,
the variational derivation of the field equation, and the theorems
establishing GR recovery, tensor uniqueness, and the FLRW cosmological
reduction. This is the document that makes SCH a closed variational theory
within its stated regime, rather than a collection of physically-motivated
postulates. Updated when a calculational target in `working/` closes and its
result is verified.

**Paper B** — *Empirical Evidence and Observational Tests.* What has actually
been computed against public data (the MaNGA rotational coherence signal),
cross-scale consistency checks (the Earth flyby anomaly), and a set of
proposed tests — JWST standard ruler, post-merger lensing timescales, the
Ampère force anomaly, NANOGrav, antipodal CMB correlation — each with an
explicit falsification condition and an honest statement of what data is
still needed.

**Paper C** — *Particle-Scale Extension.* A conditional extension of SCH into
the leptonic sector, proposing a mass-weighted condensate coupling as a
candidate mechanism for the B-meson angular anomaly. Explicitly conditional
on an unresolved calculational target (CT-xiv); includes a sharp,
parameter-free falsification target (the tau/muon anomaly ratio ≈ 16.8).

### `papers/working/`

This is where the framework is actually being built right now. It contains
open derivations, proof attempts (including ones that were wrong and were
superseded — those are kept, not deleted), numerical pipelines, and the
running list of calculational targets (CT-i through CT-xx and beyond) and
proof targets (PT-1 through PT-4).

**Start with `papers/working/README.md`.** It indexes every document by
status (OPEN / CLOSED / SUPERSEDED / BLOCKED), lists what each depends on and
unlocks, and gives a dependency graph for the active calculational chains.
This is the most up-to-date single source for "what is SCH's current state."

Documents in `working/` are not citable as settled results. They are
promoted — their results migrated into Appendix P or one of the papers, with
independent verification — once their open verification items (marked IVN
throughout) are cleared.

### `papers/superseded/`

Retired paper drafts and working documents that have been replaced. Nothing
is deleted from this project; when a draft or derivation is superseded, the
prior version moves here intact, with a note on what replaced it and why.
This preserves the derivation record — including dead ends — which matters
for a framework under active mathematical development.

### `media/`

Figures, diagrams, and animations supporting the papers.

---

## How to Engage With This Project

**If you want to check the math:** Appendix P and the documents in
`papers/working/` are written with explicit, numbered derivation steps and
IVN (independent-verification-needed) flags at every sign-convention-sensitive
step. Independent verification of these is the single highest-value
contribution at this stage — several results currently rest on internal
review only.

**If you want to check a prediction against data:** Every falsifiable claim
in Papers A, B, and C has a stated falsification condition. Paper B Section 2
and `papers/working/` contain a live empirical pipeline (the MaNGA rotational
coherence replication) with full data provenance and a documented data gap.

**If you want to know whether something is settled:** Check the epistemic
status table in Paper A first, then the closure summary table in Appendix P.
Anything not marked THEOREM or DERIVED should be treated as exactly what it
says: a prediction, a conjecture, or an open question.

**A standing methodological commitment of this project:** branches of the
mathematics are not pruned because they produce an inconvenient or
unexpected result. When a calculation has produced a result that
contradicts an earlier physically-motivated claim, the claim has been
revised and the discrepancy documented — see, for example, the chirality
inversion question in `papers/working/`, where a topological argument
originally presented as settled was found not to hold under direct
calculation, and the framework's documentation was corrected accordingly.

---

## Status at a Glance

- **Galactic-scale variational closure:** established (Appendix P, theorems closed).
- **FLRW cosmological reduction:** derived (Appendix P v11, CT-viii), pending
  full independent verification.
- **Cosmological dynamics (bounce, two-phase expansion):** derived
  (`papers/working/`, CT-ix), pending independent verification.
- **Chirality inversion across the cosmological bounce:** open question,
  revised from an earlier stronger claim — see `papers/working/README.md`.
- **Primary empirical test (MaNGA rotational coherence):** directional
  positive signal reported; quantitative confirmation pending two external
  datasets.
- **Laboratory calibration (Bismuth-209):** proposed, not yet performed.
  This experiment fixes the framework's only two free parameters and is the
  single highest-leverage open item across the entire programme.

---

*This README reflects the repository structure as of June 2026. For the most
current state of active calculations, see `papers/working/README.md`.*
