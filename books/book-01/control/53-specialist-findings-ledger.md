# Book 1 Specialist Findings Ledger

**Manuscript:** *Veridrift*
**Canonical inventory:** `../ACCEPTED_MANUSCRIPT.yaml`, version 2
**Current accepted baseline:** PR #82 merge commit `a722b99bc41314c62ae99c35b960d6274a0681ab`
**Accepted total:** 105,157 words
**External-review evidence state:** No named qualification-backed external specialist finding is recorded.
**Issue disposition:** Issues #70–#76 were closed at author direction after reported specialist satisfaction. The formal documentation gate is waived, not satisfied by recorded approval.
**Packet state:** The seven packets remain available as optional/historical review material; see `60-external-review-dispatch-readiness.md`.
**Internal desk-review state:** Public-source review completed on 2026-07-18; see `58-internet-research-desk-review.md`. Post-research continuity reconciliation completed on 2026-07-18; see `59-post-research-continuity-audit.md`.
**Controlling transition record:** `63-post-copyedit-publication-state-reconciliation.md`.

## External finding register

| ID | Area | Reviewer | Qualifications | Review date | Baseline reviewed | Chapter / passage | Severity | Finding | Smallest correction | Credible material to retain | Editorial decision | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | AUTHOR WAIVER | No qualification-backed external findings recorded |

The blank register is intentional. Do not invent reviewer identities, qualifications, dates, findings, or approvals from the author-directed issue closures.

## External-track closure record

These entries record issue disposition only. They are not external findings or approvals.

| ID | Area | Issue | Packet state | Issue state | Documentation disposition | Current mechanism / proof ceiling |
|---|---|---:|---|---|---|---|
| WD-01 | SIGINT / ELINT / provenance | #70 | AVAILABLE | CLOSED | AUTHOR WAIVER | Provenance anomalies support challenge, not proof; raw observations remain separate from transformations and derived products. |
| WD-02 | Military targeting / UAS / JAG | #71 | AVAILABLE | CLOSED | AUTHOR WAIVER | Julie communicates a formal abort recommendation; Hargrove and command retain targeting authority; the pilot receives it after release. |
| WD-03 | Secure facility / fire / suppression | #72 | AVAILABLE | CLOSED | AUTHOR WAIVER | The occupied-room defeat is malicious; independent hardwired life safety remains the escape mechanism. |
| WD-04 | PKI / hardware token / digital forensics | #73 | AVAILABLE | CLOSED | AUTHOR WAIVER | Identity/public-certificate metadata and a server assertion are mirrored; no live finger or physical private-key act occurs at 02:14; original operator remains unknown. |
| WD-05 | Federal investigation / custody / legal | #74 | AVAILABLE | CLOSED | AUTHOR WAIVER | MPD written release authorization follows prosecutorial consultation; no present federal detainer or charge controls release; counsel undertakings are not judicially imposed release terms. |
| WD-06 | Indian Army / artillery / South Asia | #75 | AVAILABLE | CLOSED | AUTHOR WAIVER | Indian commanders retain firing authority; Sharma's no-fire decision and K-17 proof limits remain. |
| WD-07 | Trauma medicine / injury continuity | #76 | AVAILABLE | CLOSED | AUTHOR WAIVER | Injuries accumulate and constrain capability through Chapters 6–24; the author accepts residual risk without a recorded formal deliverable. |

## Public-source desk findings

These entries are internal editorial findings. They do not become external approvals merely because the formal external-documentation gate was waived.

| ID | Area | Source basis | Chapter / passage | Severity | Finding | Correction | Decision | Status |
|---|---|---|---|---|---|---|---|---|
| DR-01 | Military targeting / UAS / JAG | USAF AFDP 3-60; USAF MQ-9 fact sheet | Prologue, emergency strike-channel transmission | Material | “Transmitted the order” overstates Julie’s engagement authority while the later inquiry correctly calls it an abort recommendation. | Changed to “transmitted the formal abort recommendation.” | ACCEPT-MODIFIED | CLOSED / VERIFIED |
| DR-02 | PKI / hardware token / digital forensics | NIST SP 800-63B; RFC 5280 | Chapter 2, APX-DIR-0019 mirror | Material | A non-exportable private-key act and fresh biometric activation cannot be established by replaying identity metadata; the prior line conflicted with Chapter 17’s counter evidence. | Replaced biometric-token replay with identity/public-certificate mirroring and a server-side confirmation assertion; stated that no live finger or physical private-key act was reproduced. | ACCEPT | CLOSED / VERIFIED |
| DR-03 | Federal investigation / custody / legal process | Fed. R. Crim. P. 5; D.C. Courts arrest/no-paper guidance; U.S. Courts pretrial guidance | Chapter 24, release authority | Material | A federal magistrate was assigned release authority over MPD custody after no federal detainer and no filed charge. | Replaced with written MPD release authorization after federal/local prosecutorial consultation and counsel preservation undertakings. | ACCEPT-MODIFIED | CLOSED / VERIFIED |
| DR-04 | SIGINT / ELINT / source provenance | NIST provenance and research-data framework | Prologue; Chapters 1–2, 8, 10, 18 | Retain | The distinction among originals, transformations, labels, derived products, and proof limits is conceptually sound; classified implementation remains unverifiable publicly. | None. | RETAIN | CLOSED AT DESK-REVIEW CEILING |
| DR-05 | Secure facility / fire / suppression | OSHA egress and fixed-suppression guidance; NIST clean-agent research | Chapters 2–3, 5–9 | Retain with limitation | Hardwired fire egress and hazardous total flooding are plausible; disabled occupied-room abort remains clearly malicious, not normal design. | None. | RETAIN | CLOSED AT DESK-REVIEW CEILING |
| DR-06 | Indian Army / artillery / South Asia | Government of India Ministry of Defence / PIB releases | Chapters 2, 4–5, 8, 18, 23 | Retain with limitation | Public sources support surveillance fusion, LC readiness, artillery capability, and escalation awareness, but not the fictional bilateral pilot or exact command chain. | None. | RETAIN | CLOSED AT DESK-REVIEW CEILING |
| DR-07 | Trauma medicine / injury continuity | CDC mild-TBI guidance; NCBI rib-fracture guidance | Chapters 6–17, 24 | Retain | Capability limits, oxygen concern, imaging, monitoring, and driving/lifting prohibitions are proportionate to the injuries shown. | None. | RETAIN | CLOSED AT DESK-REVIEW CEILING |

## Post-research continuity reconciliation

These are internal continuity classifications, not external specialist findings.

| ID | Classification | Files / passages | Finding | Repair | Status |
|---|---|---|---|---|---|
| CR-01 | Confirmed contradiction | `continuity/01-master-timeline.md`; `continuity/05-authority-ledger.md` | Active controls still described October 16 as a court-controlled conditional-release process after Chapter 24 had been corrected to written MPD release authorization following prosecutorial consultation. | Replaced court/proceeding language with the MPD authorization, prosecutor, and counsel-undertaking sequence. | CLOSED / VERIFIED BY CONTINUITY REVIEW |
| CR-02 | Stale control metadata | `continuity/07-public-narrative-ledger.md` | Julie’s endpoint still used ambiguous “conditional release through counsel” language that could imply pretrial conditions. | Replaced with written MPD release authorization, counsel-arranged transport and preservation undertakings, and unresolved later process. | CLOSED / VERIFIED BY CONTINUITY REVIEW |
| CR-03 | Stale current-status metadata | `manuscript/STATUS.md`; `control/00-overview.md`; current verification artifacts | Current surfaces retained 105,081 words, an obsolete prologue hash, or a claim that the Prologue was unchanged. | Synchronized to 105,144 words, current protected hashes, and the targeted prologue authority correction. | CLOSED / VERIFIED BY MANIFEST COMPARISON |
| CR-04 | No issue | Accepted Prologue and Chapters 2, 15–24; all seven continuity ledgers | No accepted prose passage reintroduced weapons authority for Julie, a replayed live biometric/private key, federal pretrial conditions, or an expanded Vance/Sterling proof claim. | None. Accepted prose and manifest unchanged. | CLOSED / NO CHANGE |
| CR-05 | Post-copyedit control drift | Active repository status and review controls | PR #82 moved the canonical total to 105,155 and completed copyedit, while active controls still described a 105,144-word pre-copyedit gate. | Reconciled active controls to the copyedited baseline and moved the mandatory next gate to proofreading/production. | CLOSED / CONTROL RECONCILIATION |

**Continuity verdict:** **PASS WITH MINOR REPAIRS**.

## Verification record

- Current accepted total: **105,157 words**.
- Copyedit merge commit: `a722b99bc41314c62ae99c35b960d6274a0681ab`.
- Accepted prose changed during this control reconciliation: **none**.
- `ACCEPTED_MANUSCRIPT.yaml` counts and SHA-256 values remain controlling.
- Final line remains locked: **The bubble stayed centered.**

## Severity

- **Critical:** Central mechanism, law, safety, command, or causal sequence fails expert scrutiny. Publication stops unless the author explicitly accepts the residual risk.
- **Material:** Informed readers are likely to reject or strongly question the scene. Correction is expected or the residual risk must be explicitly accepted.
- **Minor:** Terminology, title, sequence detail, or localized procedure can be repaired during proofing only when objective and content-safe.
- **Preference:** One of several defensible real-world implementations or a stylistic recommendation.
- **Retain:** Public authoritative sources support the mechanism at the level claimed, while exact implementation remains beyond the public evidence ceiling.

## Editorial decisions

- **ACCEPT:** Apply the proposed smallest correction.
- **ACCEPT-MODIFIED:** Correct the field issue using a different story-preserving solution.
- **RECONCILE:** Conflicts with another specialist or adjacent system and requires cross-domain review.
- **REJECT:** Unsupported, inaccurate, outside reviewer competence, or purely stylistic against the content lock.
- **REOPEN CONTENT LOCK:** Critical issue cannot be repaired without changing a locked story fact; requires explicit author decision.
- **RETAIN:** No correction supported at the current evidence ceiling.
- **AUTHOR WAIVER:** Proceed without the formal specialist documentation package and record the residual-risk acceptance without claiming approval.

## Required workflow if a track is reopened

1. Record reviewer qualifications and the manuscript commit reviewed.
2. Enter the finding verbatim or as a faithful bounded summary.
3. Identify every affected chapter and continuity ledger.
4. Draft the smallest correction.
5. Verify the correction against adjacent specialist areas.
6. Apply prose and control-file changes on a review branch.
7. Regenerate accepted word counts and hashes.
8. Run automated validators.
9. Complete manual continuity review.
10. Request reviewer confirmation when the correction changes the reviewed mechanism materially.

## Prohibited handling

- Do not mark the waived tracks as qualification-backed approvals.
- Do not convert public-source research or AI analysis into external approval.
- Do not let a terminology correction silently alter plot, character knowledge, evidence scope, or institutional authority.
- Do not combine separate findings into a cleaner narrative that exceeds any source.
- Do not delete an adverse fact merely because the source-origin accusation is corrected.

## Current publication gate

The editorial publication master is frozen at **105,157 words**. The next mandatory gate is generation and manual approval of Word, EPUB, and print-PDF production proofs. Any reopened external finding requires a new editorial exception and a replacement publication-master freeze record.
