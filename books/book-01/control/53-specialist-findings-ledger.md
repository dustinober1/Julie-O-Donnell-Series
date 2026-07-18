# Book 1 Specialist Findings Ledger

**Manuscript:** *Veridrift*  
**Canonical inventory:** `../ACCEPTED_MANUSCRIPT.yaml`  
**External-review state:** No named external specialist finding has yet been received.  
**Internal desk-review state:** Public-source review completed 2026-07-18; see `58-internet-research-desk-review.md`.

## External finding register

| ID | Area | Reviewer | Date | Chapter / passage | Severity | Finding | Smallest correction | Downstream ledgers / chapters | Editorial decision | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | Awaiting named external reviews |

## Public-source desk findings

These entries are internal editorial findings. They do not satisfy the named-reviewer gate.

| ID | Area | Source basis | Chapter / passage | Severity | Finding | Correction | Decision | Status |
|---|---|---|---|---|---|---|---|---|
| DR-01 | Military targeting / UAS / JAG | USAF AFDP 3-60; USAF MQ-9 fact sheet | Prologue, emergency strike-channel transmission | Material | “Transmitted the order” overstates Julie’s engagement authority while the later inquiry correctly calls it an abort recommendation. | Change to “transmitted the formal abort recommendation.” | ACCEPT-MODIFIED | Applied; automated verification pending |
| DR-02 | PKI / hardware token / digital forensics | NIST SP 800-63B; RFC 5280 | Chapter 2, APX-DIR-0019 mirror | Material | A non-exportable private-key act and fresh biometric activation cannot be established by replaying identity metadata; the existing line conflicts with Chapter 17’s counter evidence. | Replace biometric-token replay with identity/public-certificate mirroring and a server-side confirmation assertion; state that no live finger or physical private-key act was reproduced. | ACCEPT | Applied; automated verification pending |
| DR-03 | Federal investigation / custody / legal process | Fed. R. Crim. P. 5; D.C. Courts arrest/no-paper guidance; U.S. Courts pretrial guidance | Chapter 24, release authority | Material | A federal magistrate is assigned release authority over MPD custody after no federal detainer and no filed charge. | Use written MPD release authorization after federal/local prosecutorial consultation and counsel preservation undertakings. | ACCEPT-MODIFIED | Applied; automated verification pending |
| DR-04 | SIGINT / ELINT / source provenance | NIST provenance and research-data framework | Prologue; Chapters 1–2, 8, 10, 18 | Retain | The distinction among originals, transformations, labels, derived products, and proof limits is conceptually sound; classified implementation remains unverifiable publicly. | None. | RETAIN | Closed at desk-review ceiling |
| DR-05 | Secure facility / fire / suppression | OSHA egress and fixed-suppression guidance; NIST clean-agent research | Chapters 2–3, 5–9 | Retain with limitation | Hardwired fire egress and hazardous total flooding are plausible; disabled occupied-room abort must remain clearly malicious, not normal design. | None. | RETAIN | Closed at desk-review ceiling |
| DR-06 | Indian Army / artillery / South Asia | Government of India Ministry of Defence / PIB releases | Chapters 2, 4–5, 8, 18, 23 | Retain with limitation | Public sources support surveillance fusion, LC readiness, artillery capability, and escalation awareness, but not the fictional bilateral pilot or exact command chain. | None. | RETAIN | Closed at desk-review ceiling |
| DR-07 | Trauma medicine / injury continuity | CDC mild-TBI guidance; NCBI rib-fracture guidance | Chapters 6–17, 24 | Retain | Capability limits, oxygen concern, imaging, monitoring, and driving/lifting prohibitions are proportionate to the injuries shown. | None. | RETAIN | Closed at desk-review ceiling |

## Severity

- **Critical:** Central mechanism, law, safety, command, or causal sequence fails expert scrutiny. Publication stops.
- **Material:** Informed readers are likely to reject or strongly question the scene. Correction is expected.
- **Minor:** Terminology, title, sequence detail, or localized procedure can be repaired during copyedit.
- **Preference:** One of several defensible real-world implementations or a stylistic recommendation.
- **Retain:** Public authoritative sources support the mechanism at the level claimed, while exact implementation remains within the external-review gate.

## Editorial decisions

- **ACCEPT:** Apply the proposed smallest correction.
- **ACCEPT-MODIFIED:** Correct the field issue using a different story-preserving solution.
- **DEFER TO COPYEDIT:** Technically minor; no continuity risk.
- **RECONCILE:** Conflicts with another specialist or adjacent system and requires cross-domain review.
- **REJECT:** Unsupported, inaccurate, outside reviewer competence, or purely stylistic against the content lock.
- **REOPEN CONTENT LOCK:** Critical issue cannot be repaired without changing a locked story fact; requires explicit author decision.
- **RETAIN:** No correction supported at the current evidence ceiling.

## Required workflow for each accepted critical or material external finding

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

All external critical findings must be **CLOSED / VERIFIED**. All external material findings must be **CLOSED / VERIFIED** or carry an explicit author-approved acceptance rationale. Minor findings must be included in the copyedit style sheet or closed. Preference findings require no action unless voluntarily adopted.