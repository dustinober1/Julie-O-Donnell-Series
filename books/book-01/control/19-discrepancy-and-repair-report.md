# 19. DISCREPANCY AND REPAIR REPORT

## Accepted repair summary

The Chapter 5-to-6 continuity repair was accepted and integrated on 2026-07-12.

- Integration commit: `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`
- Chapter 5 title: **The Second Clock**
- Chapter 6 change: none
- Deadline architecture: 16:30 source certification; 05:00 executable support commit
- Immediate handoff: lower-tier incident-transfer corridor → hydraulic shutter L3-7
- Permanent history: `../repairs/chapter-05-to-06-continuity-repair/`

The original discrepancy descriptions below are retained as historical records. Resolved items are explicitly labeled.

## Discrepancy 1 — Chapter 5-to-Chapter 6 immediate continuity — RESOLVED

**Resolution:** Chapter 5 now ends at shutter L3-7 in the exact physical state required by Chapter 6. The obsolete circular-vault branch was removed from the controlling manuscript. Integrated in `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`.

### Conflict

Chapter 5 ends at approximately 16:14 EDT with the trio trapped between an elevator and a circular production-vault door. Elias triggers a director-certificate compromise review and the circular door begins turning.

Chapter 6 opens at 04:52 EDT with Julie driving Elias beneath an already descending hydraulic shutter, Marcus behind them, and a 05:00 release deadline.

### Manuscript evidence

Both sequences are in the accepted manuscript.

### Older source

The Chapter 6 production instruction required the 04:52 shutter scene to continue directly from Chapter 5, but the actual Chapter 5 ending was not revised to create that handoff.

### Recommended controlling version

For Act III planning, use the Chapter 6–12 branch because:

- It is internally coherent.
- It controls all accepted Act II injuries and evidence.
- The requested endpoint is 07:18.
- Hartwell deadlines depend on it.

The author must revise the accepted Chapter 5 ending and likely earlier present-day clock structure to create a valid handoff.

### Manuscript revision needed

Yes.

### Severity

**Critical.**

---

## Discrepancy 2 — Global present-day deadline and India clock — RESOLVED

**Resolution:** 16:30 EDT / 02:00 IST is allied source certification; 05:00 EDT / 14:30 IST is the dependent executable support commit and firing-decision point. Integrated in `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`.

### Conflict

Chapters 1–5 establish:

- Final certification at 16:30 EDT / 02:00 IST.
- Recommended Indian action window 02:10–05:00 IST.

Chapters 6–8 establish:

- Final external commit at 05:00 EDT / 14:30 IST.
- Counter-battery mission reaches its firing point at 14:30 IST.

These cannot describe one uninterrupted operation without a missing major delay and revised orders.

### Recommended controlling version

Chapter 6–12 timing should provisionally govern future chapters. A deliberate revision pass must decide whether to retime Chapters 1–5 or rebuild the transition as a later phase.

### Manuscript revision needed

Yes; not a one-line correction.

### Severity

**Critical.**

---

## Discrepancy 3 — Chapter 5 and Chapter 7 share the title “The Human Key” — RESOLVED

**Resolution:** Chapter 5 is **The Second Clock**; Chapter 7 uniquely retains **The Human Key**. Integrated in `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`.

### Conflict

Two accepted numbered chapters have the same title.

### Recommended controlling version

Retitle one after the timeline repair. Chapter 7 is more directly centered on Elias becoming the literal authenticated human key, so it has the stronger claim to the title.

### Manuscript revision needed

Yes, but not before Chapter 13 drafting.

### Severity

**Moderate.**

---

## Discrepancy 4 — Elias’s clothing during escape

### Conflict

Chapter 9 contains references to Elias’s or the group’s coveralls, while Chapters 5, 10, 11, and 12 establish Elias in a wrinkled office shirt, later covered only by an oversized Potomac rain shell. At Fenwick he leaves the shell in Mercer’s hand and is explicitly back in torn office clothes.

### Recommended controlling version

Endpoint clothing controls: Elias wears torn office clothes with no rain shell.

### Manuscript revision needed

A narrow wording correction in Chapter 9 may be appropriate.

### Severity

**Minor.**

---

## Discrepancy 5 — Older repository source hierarchy places prose below planning

### Conflict

The repository continuity file states that `PROJECT_STATE.yaml`, bibles, and outlines outrank draft prose. The user’s current authority hierarchy and accepted production practice place accepted manuscript prose first.

### Older source

The repository file explicitly ranks draft prose last.

### Recommended controlling version

Accepted manuscript first, as used by this pack.

### Manuscript revision needed

No. Repository controls should be archived or updated.

### Severity

**No repair needed** in manuscript; **Major documentation repair** externally.

---

## Discrepancy 6 — Superseded 50-chapter outline and cast

### Conflict

Repository materials describe a pre-draft 50-chapter book involving Mara Keene, Evan Rusk, Reed Calder, Dr. Selene Cho, RoboWarning, and a real convoy attack. The accepted manuscript instead establishes Marcus Reed, Elias Thorne, Sarah Chen, Senator Sterling, Major Tariq, Payload 88, and the false artillery warning.

The repository drift audit itself reports that the project was pre-draft and scaffold-based at that point.

### Recommended controlling version

Accepted manuscript.

### Manuscript revision needed

No.

### Severity

**No repair needed.** Older plan cleanly superseded.

---

## Discrepancy 7 — Older ARGUS/RoboWarning naming

### Conflict

Older repository bibles identify “RoboWarning” as the present-day module. The accepted manuscript never uses that term.

### Recommended controlling version

Use Argus, Argus Enterprise, and ARGUS-ENT-4.6 as established in accepted prose. Keep RoboWarning out unless deliberately reintroduced.

### Manuscript revision needed

No.

### Severity

**Minor documentation issue.**

---

## Discrepancy 8 — Older Act II review overstates the WSS-4 proof

### Conflict

The older Act II review says the transmission confirms:

- Tariq’s team has crossed the first line.
- K-17 is the physical target.
- A second manipulation will cover the assault.
- Sterling expects to exploit the incident.
- Apex will receive expanded authority.

The accepted WSS-4 scene proves only:

- Security Line One passed.
- Relay access not confirmed.
- Phase B on hold.
- Tariq field authority accepted.
- Sterling-office signer authenticated.
- Hartwell and second-window fields exist.
- Message blocks remain encrypted.

### Recommended controlling version

Accepted Chapter 12’s narrower proof.

### Manuscript revision needed

No. Update or archive the older review.

### Severity

**Major documentation conflict.**

---

## Discrepancy 9 — Older review states Sterling carries the signer

### Conflict

The review says Sterling carries the hardware certificate. Accepted Chapter 12 explicitly maintains that an aide, counsel, intermediary, or other authorized person could possess it.

### Recommended controlling version

Physical custodian unknown.

### Manuscript revision needed

No.

### Severity

**Major documentation conflict.**

---

## Discrepancy 10 — Older review requires stealing or cloning the signer certificate

### Conflict

The review defines the Northbridge objective as stealing or cloning the certificate. Accepted Chapters 11–12 instead capture the full live chain and hardware signature while leaving the physical signer outside their possession.

### Recommended controlling version

Accepted module-capture mechanics. Hartwell concerns physical verification, not retroactive need to clone the certificate.

### Manuscript revision needed

No.

### Severity

**No repair needed.** Superseded plan.

---

## Discrepancy 11 — Older review gives Marcus the interior Northbridge role

### Conflict

The older review divides the infiltration among all three. Accepted Chapter 11 deliberately leaves Marcus with PCF-27 and the primary evidence because of his injuries.

### Recommended controlling version

Accepted Chapters 11–12.

### Manuscript revision needed

No.

### Severity

**No repair needed.**

---

## Discrepancy 12 — Older review treats the K-17 team’s old position as current

### Conflict

The review says less than an hour remains before Tariq reaches K-17. Accepted Chapter 10 explicitly states the last sensor position is old, and Chapter 12 states access remains unconfirmed.

### Recommended controlling version

Current position unknown; access not confirmed at 07:08.

### Manuscript revision needed

No.

### Severity

**Major documentation conflict.**

---

## Discrepancy 13 — Vance identifier terminology

### Conflict

Some older material uses `APX-DIR-0019-VANCE`, implying a direct personalized signer. Accepted prose uses APX-DIR-0019 and later resolves the registered custodian through the full certificate chain.

### Recommended controlling version

Use APX-DIR-0019. State Vance’s registered authority separately.

### Manuscript revision needed

No, unless the obsolete term appears in manuscript outside the accepted DOCX.

### Severity

**Minor.**

---

## Discrepancy 14 — Older note claims core damage

### Conflict

Some planning language implies the production core was damaged. Accepted manuscript shows a limited overload test, small smoke source, suppression discharge, and fire egress, but no confirmed core destruction.

### Recommended controlling version

Core condition after escape unknown; no catastrophic damage established.

### Manuscript revision needed

No.

### Severity

**Moderate documentation issue.**

---

## Discrepancy 15 — Fleet-transponder mechanics

### Conflict

Older plans proposed cloned, swapped, or contaminated transponders. Accepted manuscript has Elias physically disconnect the existing PCF-27 fleet module and preserve it as evidence.

### Recommended controlling version

Disconnected original module; no clone or swap.

### Manuscript revision needed

No.

### Severity

**No repair needed.**

---

## Discrepancy 16 — Status notes incorrectly reported no unresolved timeline conflict — RESOLVED

**Resolution:** The controlling manuscript, status files, timeline, and control pack now record one integrated chronology. Integrated in `f6d49cbeae2b2f23daac55dc0bacfeb040428f5f`.

### Conflict

A production note treated the older 16:30 schedule as superseded but the accepted manuscript still contains it in Chapters 1–5. A Google Doc status file also recognized that the versions could not coexist without a larger revision.

### Recommended controlling version

This pack’s critical-discrepancy treatment.

### Manuscript revision needed

Yes, as described in Discrepancies 1–2.

### Severity

**Major documentation issue supporting a Critical manuscript repair.**

---

## Discrepancy 17 — Hargrove’s planned Act III witness role

### Conflict

Older repository canon files treat Hargrove’s Act III return as structurally locked. The accepted manuscript and current Act II endpoint do not yet establish it, and no approved full Act III outline was found.

### Recommended controlling version

Hargrove is a possible planned witness, not confirmed future canon.

### Manuscript revision needed

No.

### Severity

**Moderate planning issue.**

---

## Discrepancy 18 — Chapter 13 elapsed time and west-exit continuity — RESOLVED

**Resolution:** The Chapter 13 acceptance pass corrected the visual obstruction from nineteen to twenty-one seconds without changing the 07:33:08 or 07:33:29 timestamps. It also replaced the later “operational custody” description with a bounded state in which police movement exposes the west lane but does not physically control it; PCF-27 can still clear the garage and turn west.

### Conflict

The draft’s exact timestamps established a twenty-one-second obstruction, but the narrative described nineteen seconds. Separately, the 07:42:30 hard-abort test passed because one evidence-preserving exfiltration route remained, while later prose described that route as effectively controlled.

### Manuscript repair

Two sentence-level revisions only. Chapter 13 remained 6,175 words before and after. No accepted Chapter 1–12 prose changed.

### Continuity result

- The 07:42:30 decision remains valid.
- Observation remains continuous or defensibly recoverable.
- Primary evidence and exfiltration remain with Marcus.
- Police remain competent and lawful; no magical gap or chase is created.
- The physical custodian of `SSO-NS-004` remains unresolved.

### Severity

**Moderate draft continuity defect, resolved before promotion.**

---
