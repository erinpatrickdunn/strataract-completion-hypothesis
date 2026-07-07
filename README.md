# The Strataract Completion Hypothesis (SCH)

SCH is a speculative, closed-variational-theory framework proposing that
gravity has a second source beyond mass-energy: the *geometric
organizational state* of matter. Concretely, it models every particle
as a topological soliton with spin on a fourth spatial axis ("w-axis"),
identifies rest mass with the magnitude of that w-axis spin, models the
universe as a closed three-sphere ($S^3$) rotating on that axis, and
derives gravity as gradients in a rotational pressure field (the
"strataract") rather than curved spacetime. The mathematics is an
Einstein-Cartan-Dirac action with a quartic spinor self-coupling; the
physics is a set of falsifiable, scale-spanning predictions — galactic
rotation curves, a nuclear calibration experiment, a B-meson decay
signature, and cosmological structure — derived from three stated
axioms rather than fit to any one of them individually.

**This is a hypothesis under active development, not an established
theory.** Every claim in this repository carries an explicit epistemic
status (AXIOM, DERIVED, THEOREM, PREDICTION, CONJECTURE, or
EXPLORATORY), and falsification conditions are stated wherever a claim
is testable. Nothing here should be read as settled physics. Where a
claim depends on an unmeasured parameter — most centrally, the coupling
constant fixed by a proposed Bismuth-209 laboratory experiment — that
dependency is stated explicitly rather than left implicit.

---

## Current Status

*(This section is the one meant to change most often. It summarizes;
it does not replace [`governance/`](./governance/), which is the actual
source of truth for what's established, what's pending, and why.)*

As of **Appendix P v14** and **Governance Charter v2** (June 2026):

- The core physical picture, the field equation, the $S^3$ topology
  derivation, and the galactic-scale empirical programme are on
  settled footing.
- The cosmological chirality/torsion sector — previously an open,
  repeatedly-revised question — is now closed at the level of
  mechanism: three independently-derived calculations agree on the
  torsion self-coupling coefficient. What remains open there is purely
  numerical, gated on the Bi-209 calibration below.
- The single largest open dependency across the entire framework is
  the **Bismuth-209 calibration experiment** (proposed, not yet run),
  which fixes the coupling constant $\alpha$ and the condensate mass
  $m_{\text{eff}}$. Most quantitative predictions in this repository
  are parametric until that experiment is performed.
- Two narrowly-scoped items are open and explicitly flagged rather than
  silently assumed either way — see `governance/` for what they are.

For the full picture — what's Canonical, what's still being verified,
and what's been retired and why — start at
[`governance/SCH_Project_Governance_Charter_v2.md`](./governance/README.md).

---

## Where to Find What

This repository is organized by **epistemic status**, not by topic.
The question "is this settled?" determines which folder a document
lives in; the question "what is it about?" is answered inside the
document itself.

| Folder | What it holds | Go here if you want... |
|---|---|---|
| [`canonical/`](./canonical/) | The current, citable statement of the framework: the three core papers, the formal appendix, and their direct supporting derivations. | ...the theory as it currently stands, full stop. |
| [`governance/`](./governance/) | The project's own rules for how results get promoted, demoted, or retired, and the current classification of everything in the project. | ...to know *why* something is where it is, or what it would take to change that. |
| [`track-b/`](./track-b/) | Active and recently-closed verification work on specific open questions — the derivations themselves, not just their conclusions. | ...to see the actual math behind a recent resolution, including the wrong turns. |
| [`superseded/`](./superseded/) | Every retired draft, working paper, and abandoned derivation, kept in full rather than deleted. | ...history: what used to be claimed, and what replaced it. |
| [`support/`](./support/) | Data, analysis code, and non-claim material backing the empirical sections of the papers. | ...to rerun or audit an actual computed result. |

**The four documents to start with, in order, are in `canonical/`:**
Paper A (the framework and its field equation), Paper B (the empirical
and observational programme), Paper C (the particle-scale extension),
and Appendix P (the full formal derivation). Each carries its own
version history at the top explaining what changed and why.

## A Note on How This Repository Is Maintained

This project has a specific, recurring failure mode it is organized to
prevent: a result looking settled enough to migrate into the canonical
record before it has actually been independently checked. The
governance charter formalizes the rule for that (stated in full in
`governance/`): nothing is promoted to `canonical/` without a second,
genuinely independent derivation route reaching the same answer, and
the audit trail — including derivations that turned out to be wrong —
is preserved in `track-b/` and `superseded/` rather than cleaned away.
If something in `canonical/` looks recently changed, the reason is
almost always documented in that document's own revision history first,
and in `governance/` second.
