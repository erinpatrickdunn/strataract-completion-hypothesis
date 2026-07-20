# SCH Project Governance Charter v1
## Track A / Track B Bifurcation, Status Tiers, and the Four-Question Rule

**Status:** GOVERNANCE — adopted June 2026, effective immediately.

**Why this exists.** The chirality/torsion cosmology sector has been
rewritten four times in succession (v12 PT-1 → IVN-I correction →
clean-room package → IVN-CT8-Dirac-1 series), each rewrite triggered by
a result that looked settled enough to migrate into Appendix P, CT-ix,
and Paper A simultaneously, and then wasn't. Appendix P has been
functioning as a research notebook, a canonical reference, and a live
paper changelog at the same time. That is the structural cause of the
repeated churn, not any single derivation error. This charter fixes the
structure, not just the current derivation.

---

## 1. Track A — Canonical Core

**Rule:** nothing enters Track A unless it has passed the verification
bar the project is willing to defend in a paper, unqualified.

**Track A currently contains:**

- The geometric/topological framework not implicated by the Dirac/torsion
  audit: the $S^3$ topology derivation (P.7.6), the physical picture of
  Paper A Section 0, spin quantization from $S^3$ closure, the
  matter-light phase transition (Theorem 6), the $c$-as-tangential-velocity
  derivation (Theorem 5), GR recovery (Section 2.8), the galactic-scale
  variational closure (Theorem 1, established since v8).
- Theorem 0, **with the notational clarification that $\eta\equiv-i\bar\psi\psi$
  makes explicit what the bare formula left implicit** (IVN-CT8-Dirac-1a
  settled this is a labeling clarification, not a substantive reopening).
- CT-viii's FLRW reduction (Appendix P Section P.9) **for Branch 1 only**
  ($A^0=0$): the modified Friedmann equations, the bounce existence
  condition, the two-phase Branch 1 dynamics, $R_{\text{universe}}$ as a
  function of $m\eta_0$, the CMB quadrupole constraint. None of this
  involves the axial current and none of it has been touched by any
  version of the torsion audit.
- Paper B's entire empirical programme (MaNGA replication, Earth flyby
  consistency check, JWST standard ruler test, post-merger lensing test,
  Ampère force proposal, NANOGrav/antipodal-CMB exploratory sections,
  rotation curve flattening test) — none of it depends on the chirality
  sector's internal dynamics.
- Paper C's entire particle-scale programme — it depends only on the
  scalar $\eta$ coupling to fermion mass, not on the axial current $A^\mu$
  or any Branch 2 dynamics. Already established as independent in the
  Paper C polish pass; reaffirmed here as a standing classification, not
  re-derived each time the chirality sector changes.
- The Replication Study working paper — no dependency of any kind.
- **The statement that IVN-I's original Branch 2 equations are
  superseded.** This is itself a Track A fact: it does not depend on
  which corrected system eventually wins, only on the (already
  established) fact that IVN-I's derivation mixed conventions.

**Track A does NOT currently contain:** any specific claim about whether
$\eta$ is sourced in Branch 2, by what mechanism, or with what
coefficient. That entire question — and everything built on a specific
answer to it — lives in Track B until B1–B3 below close.

---

## 2. Track B — Chirality/Torsion Verification Branch

**Track B's job is narrow, not exploratory.** It is not "understand
Branch 2." It is three specific deliverables, each with a defined
completion criterion.

### Deliverable B1 — Canonical Branch 2 System

One signed-off system of equations for $(\eta, J^0, P, A^0)$, with:
convention fixed ($(-,+,+,+)$, bare-$\gamma^0$ adjoint, per
IVN-CT8-Dirac-1a — this part is CLOSED and should not be reopened absent
new evidence); torsion-elimination route fixed (auxiliary-field
elimination, substitute-then-vary — reconfirmed independently by the
4D-first route's Lorentz-covariance argument, though the exact
coefficient is still moving); coefficient normalization fixed (**not yet
— currently at its third value in three attempts:
$\kappa\alpha\to-\tfrac{3\kappa\alpha}2\to-3\kappa\alpha$**); and one
documented derivation tree from action → Dirac equation → bilinear
system, in a single document, not scattered across four.

**Status: OPEN.** Current best candidate (provisional, not yet B1-complete):

$$\dot\eta=-3H\eta-3\kappa\alpha A^0P,\qquad \dot J^0=-3HJ^0$$
$$\dot P=-3HP-\Big(2m+(\lambda-3\kappa\alpha)\eta\Big)A^0,\qquad \dot A^0=-3HA^0+(2m+\lambda\eta)P$$

### Deliverable B2 — Proof of Route-Consistency

Show that: reduced-first and 4D-first agree (**currently: they do NOT** —
the reduced-route Part A computation is off by a factor of 2 from the
4D-first computation, traced to an unsummed antisymmetric index pair in
$K_i^{jk}\gamma_j\gamma_k$; the 4D-first route is judged correct, but the
reduced-route document itself has not been corrected in place); the
antisymmetric contorsion summation is handled unambiguously (**this is
precisely what B2 must fix** — the ambiguity that caused the factor-of-2
error must be closed with an explicit summation-convention statement, not
just a one-off correction); the coefficient is confirmed or rejected with
a pinpointed reason (**currently: confirmed doubled, reason pinpointed** —
but only after two rounds of disagreement, which is exactly why B2 exists
as a standing deliverable rather than a one-time check).

**Status: PARTIALLY CLOSED.** The route-consistency check succeeded at
catching a real error. It has not yet been re-run a third time to confirm
no further such error remains. Recommend one confirming pass before B1 is
declared complete, per the project's own four-question rule below.

### Deliverable B3 — Dependency Map

For every downstream document, state what it depends on: only the
existence of torsion coupling; the sign of sourcing; the exact
coefficient; the full coupled system; or none of the above.

| Document / Section | Depends on | Current exposure |
|---|---|---|
| Paper A §2.10a (chirality narrative) | Existence + qualitative non-generic-inversion conclusion only | Low — the qualitative point is not coefficient-sensitive, but the section cites IVN-I and P.7.7 machinery by name, which has since moved twice more. **Stale pending update, not to be silently trusted as current.** |
| Paper A epistemic table, chirality row | Same as above | Same — stale pending update. |
| Paper A §6.6, CT-x note | Full coupled system (references "the corrected $(A^0,P)$ system") | **High** — this note explicitly names a system that no longer matches the current provisional candidate. Needs revision once B1 closes, not before. |
| Appendix P §P.7.7.3 / P.7.7.3a | Full coupled system | Frozen (Provisional tier); do not cite. |
| CT-ix §P.10.5 (Branch 2) | Full coupled system | Frozen (Provisional tier); do not cite. |
| Appendix P Gap 7 / Gap 16 status rows | Full coupled system, by design (they exist to report this status) | Correctly track Track B status; update as B1/B2 progress, no other action needed. |
| Paper B | None | Canonical, unaffected, no action. |
| Paper C | None (uses $\eta$ scalar only) | Canonical, unaffected, no action. |
| CT-ix Branch 1 (Sections P.10.1–P.10.4, P.10.7–P.10.8) | None ($A^0=0$) | Canonical, unaffected, no action. |
| Replication Study | None | Canonical, unaffected, no action. |

**Status: this table is the initial pass, current as of this document.**
It should be re-checked, not assumed static, each time B1's candidate
system changes.

---

## 3. The Three-Tier Status System

Every result in the project now carries exactly one of three tags.

**Tier 1 — Canonical.** Safe to cite in Paper A / Paper B / Paper C /
CT-ix / Appendix P mainline text as settled theory. Entry bar: passed
route-consistency checks where applicable, or structurally independent
of anything still moving (per the dependency map above).

**Tier 2 — Provisional.** Current best result, quarantined in a
verification section or standalone note (Track B territory). May be
discussed and built upon internally, but must not be silently propagated
into mainline theory narrative as if settled. Every Provisional result
must state what would promote it to Canonical (typically: a specific
B1/B2-style check).

**Tier 3 — Superseded.** Retained for history and audit trail only. Not
citable as current theory under any circumstance. Superseded documents
keep their content unedited (per the freeze-and-annotate discipline
already established) with a supersession notice naming the replacement.

### Current classification

| Result | Tier | Note |
|---|---|---|
| IVN-I's original Branch 2 $(A^0,P)$ system | **Superseded** | By the clean-room package, itself since superseded. |
| Clean-room package's "no sourcing" claim | **Superseded** | By 1b-i's resolution. |
| 1b-i's original resolution ($-\tfrac{3\kappa\alpha}2$ coefficient) | **Superseded** | By the 4D-first route's factor-of-2 correction. |
| Doubled-coefficient system ($-3\kappa\alpha$) | **Provisional — leading candidate** | Pending B1 sign-off and one further confirming route-consistency pass (B2). |
| Non-chirality SCH framework (Track A contents, Section 1) | **Canonical** | Subject to any locally known issues already flagged in prior polish passes; not reopened by this charter. |
| Paper A's current references to IVN-I as live status | **Stale, flagged** | Not silently trusted. Not yet corrected — correction is deferred until B1 closes, per the "don't migrate piecemeal" discipline this project already committed to. Listed here specifically so it is not forgotten by omission. |

---

## 4. The Hard Rule

**Before any future result is allowed to modify a paper or a canonical
appendix section, it must answer all four of the following, in writing,
before the edit is made — not after:**

1. **What exact equation set is being claimed?** Not "the Branch 2
   correction" — the literal equations, written out.
2. **What derivation route produced it?** Reduced-first, 4D-first,
   component-spinor, or other — named specifically.
3. **What independent route has reproduced it?** If none, it is
   Provisional by definition and does not clear the bar for Tier 1
   regardless of how confident the derivation feels.
4. **What downstream sections become wrong if this changes?** Answered
   by consulting (and updating) the B3 dependency map before, not after,
   propagating the change.

This rule is retroactive in spirit: reviewing the chirality/torsion
episode against it, every one of the four rewrites so far would have
been caught at question 3 alone — none of IVN-I, the clean-room package,
or 1b-i's original resolution had independent-route confirmation at the
time each was migrated into Appendix P's mainline narrative. The doubled
coefficient found by the 4D-first pass is the *first* result in this
entire episode that actually satisfies question 3 as stated (two
genuinely independent routes, in disagreement, resolved with a pinpointed
cause) — which is exactly why it is only Provisional, not yet Canonical:
satisfying question 3 once is what makes a result eligible for
Tier 1 consideration, not automatically promoted to it. B2's remaining
confirming pass is what would complete that promotion.

---

## 5. Standing Declaration

**Effective immediately: the chirality/torsion cosmology sector is a
verification branch (Track B), not part of SCH's canonical cosmological
narrative, until a single Branch 2 system survives route-consistency
checks (B1 signed off, B2 closed).** Appendix P's Gap 7 and Gap 16 freeze
notices, and CT-ix's Section P.10.5 freeze, remain in effect under this
declaration — this charter does not change their operative status, it
formalizes why they exist and what would lift them.

This is not punitive. It is the specific structural change that would
have prevented needing a fifth rewrite.

---

*SCH Project Governance Charter — v1 | June 2026*
*Adopted by project decision. Applies to all subsequent SCH work.*
