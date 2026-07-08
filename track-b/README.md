# `track-b/` — Active Verification Branch

This folder holds work-in-progress on specific, narrowly-scoped open
questions in the framework — not general research, and not a place for
new physics ideas. Per the governance charter, a Track B item exists
because exactly one thing is unresolved (a coefficient, a sign, a
convention), it has a stated completion criterion, and it will move
either into `canonical/` (if resolved and independently confirmed) or
`superseded/` (if a derivation route turns out to be wrong) — never
staying here indefinitely as a third, permanent state.

## Why This Folder Exists at All

Read the derivations here, not just their conclusions, if you want to
actually check the project's work rather than take its word for it.
The governing rule (full text in `governance/`) is that nothing is
promoted to `canonical/` on the strength of one derivation alone — a
second, genuinely independent route has to reach the same answer before
a result counts as settled. That means the interesting content in this
folder is often the *disagreement* between two documents, not either
one in isolation.

## `resolved/`

Contains the complete derivation chain for the one Track B item this
project has fully closed: the torsion self-coupling coefficient in the
cosmological Branch 2 chirality sector. Read in this order to follow
the actual history, including the wrong turns:

1. `SCH_IVN-CT8-Dirac-1a_ConventionAudit_v1.md` — fixes the sign/metric
   convention used by everything downstream.
2. `SCH_IVN-CT8-Dirac-1b_TorsionCoefficient_v1.md` — the first
   (reduced-action) attempt. Correct in its overall structure; contains
   an error in one specific term that this document itself does not
   catch.
3. `SCH_IVN-CT8-Dirac-1b-i_InvestigationLog_v1.md` — the search for that
   error.
4. `SCH_IVN-CT8-Dirac-1b-i_Resolution_v1.md` — finds it, via an
   independent direct-component method. Establishes the coefficient
   $-\tfrac{3\kappa\alpha}{2}$, but explicitly recommends one further,
   genuinely independent check before treating it as settled.
5. `SCH_IVN-CT8-Dirac-1_ConfirmingPass_v1.md` — that check, run via a
   third, structurally different method (working from the full 4D
   action rather than the pre-reduced one). Confirms the same
   coefficient, and along the way documents that a *first* attempt at
   this same confirming pass was itself wrong (filed in
   `superseded/working-superseded/SCH_IVN-CT8-Dirac-1_4DFirst_v1.md`)
   — caught precisely because the rule requires an independent route,
   not just a second attempt by the same reasoning.

The result of this chain — three independent derivations converging on
one coefficient — is what's stated as established in
`canonical/SCH_Appendix_P_v14.md`, Section P.7.7.10, which also
summarizes this history in prose. This folder is the primary-source
version of that summary.

## What's Currently Open

Nothing, as of the current state of this repository. The last Track B
item closed with the derivation chain above. Two items remain
explicitly flagged as unresolved in `governance/` — a claimed
double-count and a claimed sign error in an unrelated part of the
formal derivation — but neither has an active investigation underway
yet, so neither has a folder here. When one starts, it will get one,
following the same pattern as `resolved/` above.
