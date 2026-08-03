SCH Project Governance Charter v2
Track A / Track B Bifurcation, Status Tiers, and the Four-Question Rule
Status: GOVERNANCE — adopted June 2026; revised June 2026 (v2) to close
Deliverables B1 and B2 and correct an error in v1's own retrospective.

**Revision note (v2).** Section 2's Deliverable B1 and B2 are closed
below. This did not happen cleanly. The result v1 recorded as "leading
candidate" — the doubled coefficient $-3\kappa\alpha$, attributed to a
4D-first derivation reportedly disagreeing with the reduced-action route
by a factor of 2 — traced, on inspection, to a document that did not
exist. When that derivation was actually carried out, it did not
reproduce the doubling. It found the doubling itself was the error: the
first 4D-first attempt had selected the wrong contorsion component (one
sourced by the spatial axial current, which vanishes identically on the
homogeneous background) and found a real combinatorial identity attached
to a term that contributes nothing physically. A corrected second pass,
using the contorsion component actually sourced by $A^0$, reproduced the
original reduced-action/direct-bilinear coefficient exactly:
$-\tfrac{3\kappa\alpha}{2}$. Three independent routes now agree. This is
recorded in full below, including the correction of v1's own text,
because the entire point of this charter is that the audit trail is the
deliverable, not just the endpoint.

Why this exists (unchanged from v1). The chirality/torsion cosmology
sector has been rewritten repeatedly, each rewrite triggered by a result
that looked settled enough to migrate into Appendix P, CT-ix, and Paper A
simultaneously, and then wasn't. Appendix P has been functioning as a
research notebook, a canonical reference, and a live paper changelog at
the same time. That is the structural cause of the repeated churn, not
any single derivation error. This charter fixes the structure, not just
the current derivation. **v2 adds a second lesson to that diagnosis:**
even a properly-scoped Track B verification effort, run under this
charter's own rules, produced one more spurious result before producing
the confirmed one — because the missing-document gap flagged at the time
was real, and the derivation that filled it was wrong on its first pass.
The rules did not prevent that error. What they did was force it to be
written down, checked against an independent route, and caught before it
reached Appendix P's mainline text. That is the standard this charter
holds itself to, not a guarantee that first attempts are error-free.

1. Track A — Canonical Core
Rule: nothing enters Track A unless it has passed the verification bar
the project is willing to defend in a paper, unqualified.

Track A currently contains:

The geometric/topological framework not implicated by the Dirac/torsion
audit: the $S^3$ topology derivation (P.7.6), the physical picture of
Paper A Section 0, spin quantization from $S^3$ closure, the
matter-light phase transition (Theorem 6), the $c$-as-tangential-velocity
derivation (Theorem 5), GR recovery (Section 2.8), the galactic-scale
variational closure (Theorem 1, established since v8).

Theorem 0, with the notational clarification that
$\eta\equiv-i\bar\psi\psi$ makes explicit what the bare formula left
implicit (IVN-CT8-Dirac-1a settled this is a labeling clarification, not
a substantive reopening).

CT-viii's FLRW reduction (Appendix P Section P.9) for Branch 1 only
($A^0=0$): the modified Friedmann equations, the bounce existence
condition, the two-phase Branch 1 dynamics, $R_{\text{universe}}$ as a
function of $m\eta_0$, the CMB quadrupole constraint. None of this
involves the axial current and none of it has been touched by any
version of the torsion audit.

**New in v2 — the chirality/Branch 2 sector, promoted from Track B:**
the torsion self-coupling coefficient $-\tfrac{3\kappa\alpha}{2}$ in
$\dot\eta$; the full confirmed $(\eta, A^0, P)$ bilinear system
(Appendix P v14, Section P.7.7.3); the conclusion that chirality
inversion per cycle is confirmed non-generic; the qualitative
Branch 2 late-time-approaches-Branch-1 statement, now expressed as a
calculable oscillatory correction rather than an unknown-sized one. This
promotion is made on the strength of the B1/B2 closure documented in
Section 2 below — three independently-executed derivation routes
converging on the same result, the first time this sector has cleared
that bar. **Explicitly not promoted:** the numerical value of the
monodromy phase, the within-cycle matter surplus, and the fractional
size of the Branch 2 correction — all of these remain gated on the
Bi-209 calibration and are not claimed as Canonical numbers, only as
Canonical forms.

Paper B's entire empirical programme (MaNGA replication, Earth flyby
consistency check, JWST standard ruler test, post-merger lensing test,
Ampère force proposal, NANOGrav/antipodal-CMB exploratory sections,
rotation curve flattening test) — none of it depends on the chirality
sector's internal dynamics.

Paper C's entire particle-scale programme — it depends only on the
scalar $\eta$ coupling to fermion mass, not on the axial current
$A^\mu$ or any Branch 2 dynamics.

The Replication Study working paper — no dependency of any kind.

The statement that IVN-I's original Branch 2 equations are superseded,
and the statement that the clean-room package's "no sourcing" claim is
also superseded — both are Track A facts regardless of which corrected
system eventually won, and both are now further confirmed: the clean-room
package's central claim did not survive precisely because sourcing is
real, at the coefficient established in Section 2 below.

Track A does NOT currently contain: the numerical value of $\alpha$,
$m$, or any quantity requiring the Bi-209 calibration; the two
clean-room-flagged subsidiary claims about Appendix P Sections P.9.4.2
and P.9.5.3, neither of which has been independently re-derived by any
document in this project (see Appendix P v14, Section P.9.7 — this is a
newly and narrowly scoped open item, distinct from and not resolved by
the B1/B2 closure below).

2. Track B — Chirality/Torsion Verification Branch
Track B's job was three specific deliverables, each with a defined
completion criterion. **All three are now closed.**

Deliverable B1 — Canonical Branch 2 System — **CLOSED.**

One signed-off system of equations for $(\eta,J^0,P,A^0)$:

$$\dot\eta = -3H\eta - \frac{3\kappa\alpha}{2}A^0P$$
$$\dot J^0 = -3HJ^0$$
$$\dot P = -3HP - \left(2m+\left(\lambda-\frac{3\kappa\alpha}{2}\right)\eta\right)A^0$$
$$\dot A^0 = -3HA^0 + (2m+\lambda\eta)P$$

Convention: fixed, $(-,+,+,+)$/bare-$\gamma^0$ adjoint
(IVN-CT8-Dirac-1a). Torsion-elimination route: fixed, auxiliary-field
elimination, substitute-then-vary, reconfirmed by the 4D-first route's
Lorentz-covariance argument. Coefficient normalization: **fixed**, at
$-\tfrac{3\kappa\alpha}{2}$ — this is the correction relative to v1,
which listed the coefficient as still moving between
$\kappa\alpha \to -\tfrac{3\kappa\alpha}{2}\to-3\kappa\alpha$ and named
the last of these as leading. The apparent third value was itself an
error, not a further refinement; the correct history is
$\kappa\alpha \to -\tfrac{3\kappa\alpha}{2}$, confirmed, full stop.
Derivation tree: documented in full in Appendix P v14, Section P.7.7.10.

Deliverable B2 — Proof of Route-Consistency — **CLOSED.**

Reduced-first and 4D-first now agree, at $-\tfrac{3\kappa\alpha}{2}$.
Getting here required catching two separate errors, not one: the
original reduced-action route's imaginary residual (traced to a
gamma-algebra slip applying an abstract lemma to the $\Gamma=\gamma^5$
bilinear, fixed by the direct-bilinear route), and a first 4D-first
attempt's apparent factor-of-2 discrepancy (traced to contracting the
wrong contorsion component — one sourced by the spatial axial current,
which vanishes on the background, rather than the one sourced by $A^0$,
which does not). The antisymmetric contorsion summation ambiguity that
v1 flagged as still needing an explicit, unambiguous convention
statement is resolved by the same finding: the correct object to
contract is the fully-spatial component $K_{ijk}$, sourced by $A^0$,
with all index pairs summed unrestricted (standard Einstein
convention); the vanishing electric-type component $K_0^{\ ij}$ should
not be used as the basis for this calculation regardless of how its
own internal combinatorics are handled. This is now stated explicitly,
closing the ambiguity B2 was opened to fix.

Deliverable B3 — Dependency Map — **updated, not fully closed.**

Document / Section | Depends on | Current exposure (v2)
--- | --- | ---
Paper A §2.10a (chirality narrative) | Existence + qualitative non-generic-inversion conclusion, now also the confirmed coefficient | **Resolved.** Paper A Draft 2.4 rewrites this section in full against the closed B1/B2 result.
Paper A epistemic table, chirality row | Same as above | **Resolved** in Draft 2.4.
Paper A §6.6, CT-x note | Full coupled system | **Resolved** in Draft 2.4 — references the confirmed system and Appendix P v14 directly.
Appendix P §P.7.7.3 / P.7.7.3a | Full coupled system | **Resolved.** Rewritten in full in Appendix P v14; no longer frozen.
CT-ix §P.10 (Branch 2) | Full coupled system | **Resolved.** Rewritten in full in Appendix P v14; no longer frozen.
Appendix P Gap 7 / Gap 16 status rows | Full coupled system, by design | **Resolved** — both moved to ESTABLISHED/CLOSED in v14, with numerical-magnitude caveats stated explicitly rather than left implicit.
Paper B | None (own results); version-pointer housekeeping only | **Pending as of this charter revision** — addressed in the same session, see Paper B Draft 1.8.
Paper C | None (uses $\eta$ scalar only) | Canonical, unaffected, no action.
CT-ix Branch 1 (Sections P.10.1–P.10.4 in earlier numbering) | None ($A^0=0$) | Canonical, unaffected, no action.
Replication Study | None | Canonical, unaffected, no action.

Status: this table reflects the closure of B1/B2. The one remaining
open row (Paper B) is a housekeeping dependency, not a physics
dependency — consistent with the pattern already established when
Paper B moved from Draft 1.6 to 1.7 for the same kind of reason.

3. The Three-Tier Status System
Unchanged in structure from v1. Tier 1 (Canonical), Tier 2
(Provisional), Tier 3 (Superseded), with the same entry bars and the
same rule that Provisional results may be built upon internally but
must not be silently propagated as settled.

Current classification (v2, superseding v1's table in full)

Result | Tier | Note
--- | --- | ---
IVN-I's original Branch 2 $(A^0,P)$ system | Superseded | By the clean-room package, itself since superseded.
Clean-room package's "no sourcing" claim | Superseded | By the direct-bilinear route's finding of real sourcing.
Direct-bilinear resolution, coefficient $-\tfrac{3\kappa\alpha}{2}$ | **Canonical** | Confirmed by an independent 4D-first route (see below); promoted from Provisional as of this charter revision.
First 4D-first attempt, coefficient $-3\kappa\alpha$ (doubled) | **Superseded** | Traced to selecting the wrong contorsion component (electric-type, vanishing on the background) rather than an arithmetic error in an otherwise-valid combinatorial identity. The identity itself was correct; its application was not.
Confirmed 4D-first pass, coefficient $-\tfrac{3\kappa\alpha}{2}$ | **Canonical** | Agrees with the direct-bilinear result exactly. This is the result that actually closes B1/B2.
Non-chirality SCH framework (Track A contents, Section 1) | Canonical | Subject to any locally known issues already flagged in prior polish passes; not reopened by this charter.
Paper A's references to the chirality sector | **Corrected** | Draft 2.4 updates §2.10a, the epistemic table row, and the §6.6 CT-x note against the now-Canonical result. No longer flagged as stale.
Appendix P P.9.4.2 (claimed double-count) | **Unverified, open** | Never independently re-derived by any document in this project. Not part of the B1/B2 closure. See Appendix P v14 Section P.9.7.
Appendix P P.9.5.3 (claimed sign error) | **Unverified, open** | Same status as above. Flagged explicitly rather than silently accepted or silently fixed.

4. The Hard Rule
Unchanged from v1, reproduced here in full because it is the operative
constraint and should not be a pointer:

Before any future result is allowed to modify a paper or a canonical
appendix section, it must answer all four of the following, in writing,
before the edit is made — not after:

1. What exact equation set is being claimed? Not "the Branch 2
correction" — the literal equations, written out.
2. What derivation route produced it? Reduced-first, 4D-first,
component-spinor, or other — named specifically.
3. What independent route has reproduced it? If none, it is Provisional
by definition and does not clear the bar for Tier 1 regardless of how
confident the derivation feels.
4. What downstream sections become wrong if this changes? Answered by
consulting (and updating) the B3 dependency map before, not after,
propagating the change.

**Corrected retrospective (v2).** v1 claimed that the doubled
coefficient was "the first result in this entire episode that actually
satisfies question 3 as stated (two genuinely independent routes, in
disagreement, resolved with a pinpointed cause)," and that only one
further confirming pass (B2) remained before promotion. **This claim
was itself wrong**, for a reason worth stating plainly: the "genuinely
independent route" it pointed to did not exist as a written document at
the time v1 was adopted. The charter described a result that had been
reasoned about but not yet actually derived. When the derivation was
finally carried out, in the same session that produced this revision,
it did not confirm the doubling — it found the doubling was itself the
product of an error, and the actually-independent, actually-confirmed
result is $-\tfrac{3\kappa\alpha}{2}$, not $-3\kappa\alpha$.

This is not a failure of the Hard Rule. It is exactly what the rule is
for, working one level up: question 3 does not just ask "has a second
route been run" — it requires that the second route's *output* be
checked, not assumed, before a result is treated as reproduced. v1
listed a document as existing and agreeing before that document had
been written. That is precisely the "migrated before independent
confirmation" failure mode the rule exists to catch, and this time it
caught itself, one edit late rather than after reaching Appendix P's
mainline text. The lesson carried forward is not "add a fifth
deliverable" — it is: a charter should not describe the result of a
derivation in the past tense until the derivation has actually been
performed and its written output inspected, even when the eventual
outcome seems overdetermined by the surrounding argument.

5. Standing Declaration
**The freeze on the chirality/torsion cosmology sector is lifted.**
Three independently-executed derivation routes converge on
$-\tfrac{3\kappa\alpha}{2}$ in $\dot\eta$, Appendix P v14 performs the
single-pass canonical rewrite of the previously frozen sections in full,
and Paper A Draft 2.4 updates its dependent sections against that
result. This sector moves from Track B to Track A, per Section 1 above,
with the explicit and repeated caveat — stated in Appendix P v14, in
Paper A Draft 2.4, and here — that the coefficient's *numerical*
evaluation, and everything downstream of it (the monodromy phase, the
matter surplus, the size of the Branch 2 correction to standard
dilution), remains gated on the Bi-209 calibration and is not being
claimed as settled.

Two items remain explicitly open and are not resolved by this charter
revision: the clean-room package's claims about Appendix P P.9.4.2 and
P.9.5.3, and Paper B's version-pointer housekeeping. Neither is treated
as closed by omission. Both are named here so that, consistent with the
whole point of this document, nothing about this project's status is
inferred rather than stated.
