# Book 1 Specialist Findings Ledger

**Manuscript:** *Veridrift*  
**Canonical inventory:** `../ACCEPTED_MANUSCRIPT.yaml`  
**Current state:** No external specialist finding has yet been received.

## Finding register

| ID | Area | Reviewer | Date | Chapter / passage | Severity | Finding | Smallest correction | Downstream ledgers / chapters | Editorial decision | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | Awaiting reviews |

## Severity

- **Critical:** Central mechanism, law, safety, command, or causal sequence fails expert scrutiny. Publication stops.
- **Material:** Informed readers are likely to reject or strongly question the scene. Correction is expected.
- **Minor:** Terminology, title, sequence detail, or localized procedure can be repaired during copyedit.
- **Preference:** One of several defensible real-world implementations or a stylistic recommendation.

## Editorial decisions

- **ACCEPT:** Apply the proposed smallest correction.
- **ACCEPT-MODIFIED:** Correct the field issue using a different story-preserving solution.
- **DEFER TO COPYEDIT:** Technically minor; no continuity risk.
- **RECONCILE:** Conflicts with another specialist or adjacent system and requires cross-domain review.
- **REJECT:** Unsupported, inaccurate, outside reviewer competence, or purely stylistic against the content lock.
- **REOPEN CONTENT LOCK:** Critical issue cannot be repaired without changing a locked story fact; requires explicit author decision.

## Required workflow for each accepted critical or material finding

1. Enter the external finding verbatim or as a faithful bounded summary.
2. Record reviewer qualifications and the manuscript commit reviewed.
3. Identify every affected chapter and continuity ledger.
4. Draft the smallest correction.
5. Verify the correction against adjacent specialist areas.
6. Apply prose and control-file changes on a review branch.
7. Regenerate accepted word counts and hashes.
8. Run automated validators.
9. Complete manual continuity review.
10. Request reviewer confirmation when the correction changes the reviewed mechanism materially.

## Prohibited handling

- Do not mark an issue reviewed from an informal conversation without a dated deliverable.
- Do not convert web research or AI analysis into an external approval.
- Do not let a terminology correction silently alter plot, character knowledge, evidence scope, or institutional authority.
- Do not combine separate findings into a cleaner narrative that exceeds any source.
- Do not delete an adverse fact merely because the source-origin accusation is corrected.

## Publication gate

All critical findings must be **CLOSED / VERIFIED**. All material findings must be **CLOSED / VERIFIED** or carry an explicit author-approved acceptance rationale. Minor findings must be included in the copyedit style sheet or closed. Preference findings require no action unless voluntarily adopted.
