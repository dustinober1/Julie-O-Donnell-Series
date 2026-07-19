# Book 1 Specialist Review Brief

**Manuscript:** *Veridrift*
**Accepted-manuscript baseline:** `main` commit `0a0ed1c5330cbe48a59499d7a4104aa02f6c059a`
**Manifest:** `books/book-01/ACCEPTED_MANUSCRIPT.yaml`, version 2
**Accepted structure:** Prologue + Chapters 1–24
**Accepted total:** 105,144 words
**Status of every specialist area below:** **UNREVIEWED**
**Tracking register:** `52-specialist-review-register.md`
**Dispatch-readiness record:** `60-external-review-dispatch-readiness.md`

This brief identifies the precise scenes, mechanisms, and questions that require qualified external review before copyediting and publication. It does not imply that any specialist has approved the manuscript. An AI review, public-source review, informal conversation, or unnamed opinion cannot close an external-review gate. A specialist area remains **UNREVIEWED** until a named qualified reviewer supplies a dated, qualification-backed deliverable tied to the accepted baseline above.

The manuscript is **not ready for publication**. Reviewers should identify both errors or concerns and credible material that should remain unchanged. Recommendations must use the smallest story-preserving correction and must not exceed the manuscript's proof ceilings.

## 1. SIGINT / ELINT / Sensor-Provenance Review — UNREVIEWED

**Minimum useful reviewer profile:** Current or former signals-intelligence, electronic-warfare, telemetry, sensor-fusion, collection, or source-provenance practitioner able to distinguish raw observations from transformations and derived assessments.

### Primary scenes

- Prologue: synthetic carrier noise inside a live encrypted signal; 11.2-second interval; environmental comparison; line-of-sight contradiction.
- Chapters 1–2: 0.07 percent target deviation, impossible path through granite, Validation Package 88, the post-archive derivative, and `SIGMA-NORMALIZE-4`.
- Chapter 8: provenance reconciliation, source-boundary selection, dependency tables, cached conclusions, Julie's overbroad boundary, and the supplemental K-17 review.
- Chapters 10 and 18: K-17 sensor events, local relay journal, field-route challenge, and failed source-record reconstruction.

### Questions

1. Does the distinction among raw packet content, carrier/background noise, environmental variation, reconstruction, normalization, and source provenance read credibly?
2. Could a validation package realistically preserve a copied carrier structure while a source-correction process flattens modeled timing and equipment irregularities?
3. Is the causal chain coherent: messy Revision Eight → post-archive derivative → irregularities classified as collection damage → common-reference reconstruction → unnaturally clean live feed?
4. Would the 11.2-second regularity, 0.07 percent environmental deviation, repeated seventeen-millisecond carrier structure, and impossible terrain path support Julie's level of suspicion without constituting proof by themselves?
5. Is it plausible that conflicting observations sharing the reconstructed carrier family could be diverted into a correction-dependent side table and thereby mask the K-17 movement?
6. Are the recovery-console proof limits credible? Can source labels be restored and downstream products suspended while primary raw observations remain preserved?
7. Does Julie's overbroad lineage boundary create a technically plausible forty-three-second delay without reversing the no-fire result?
8. What terminology should be corrected for real SIGINT/ELINT, telemetry, collection, sensor-fusion, or provenance practice?
9. Which elements are credible and should remain unchanged?

## 2. Military Targeting / UAS / JAG Review — UNREVIEWED

**Minimum useful reviewer profile:** Targeting officer, MQ-9 aircrew or operations specialist, operational-law attorney, military intelligence professional, or other practitioner with strike-chain and post-strike review experience.

### Current authority baseline

- Julie identifies the compromised intelligence and communicates a **formal abort recommendation**.
- Julie does not exercise weapons-release or engagement authority.
- Hargrove and the existing command structure retain responsibility for the targeting decision.
- The pilot receives the recommendation after weapon release because the gateway holds it for four seconds.
- The later inquiry asks whether Julie formally communicated the recommendation in time.

### Primary scenes

- Prologue: Reaper strike sequence, target validation, release criteria, emergency recommendation routing, four-second gateway delay, pilot call, and post-strike investigation.
- Chapters 1, 8, and 18: U.S. warning support to Indian Northern Command, Indian firing authority, counter-battery product, and Sharma's hold-fire decision.
- Chapters 23–24: public correction and Marcus's corrected testimony about the recommendation and timeline.

### Questions

1. Is Julie's intelligence role, access, and ability to communicate a formal abort recommendation plausible for her rank without giving her weapons authority?
2. Would a time-sensitive recommendation realistically route through an authenticated software gateway, and could a four-second authentication delay be decisive after release criteria were reached?
3. Are the pilot terminology, weapons-release call, command relationships, and final weapons authority accurate for the platform and operation depicted?
4. Could Hargrove physically or procedurally delay the recommendation while the existing command structure remains responsible for the strike?
5. Does the investigation's focus on when Julie's objection became a formal recommendation reflect plausible military/JAG review practice?
6. Is the classified bilateral pilot framed credibly: the United States supplies machine-readable warning and counter-battery support while Indian commanders retain firing authority?
7. Are Sharma's orders—mechanical readiness, ammunition movement, staged firing data, hold-fire authority, and safe-state confirmation—credible?
8. What changes would preserve the four-second emotional structure while improving targeting-chain realism?
9. Which elements are credible and should remain unchanged?

## 3. Classified-Facility Security / Fire Protection / Clean-Agent Review — UNREVIEWED

**Minimum useful reviewer profile:** Fire-protection engineer, clean-agent suppression designer, classified-facility security professional, code-enforcement specialist, or practitioner responsible for protected industrial life-safety systems.

### Primary scenes

- Chapters 2–3: contractor-controlled secure review room, access-profile modification, facility-security authority, administrative hold, ventilation interruption, fire-alarm evacuation, and escape through the garage.
- Chapters 5–9: lower-tier quarantine, shutters, cooling galleries, production enclave, emergency administrator access, clean-agent suppression, occupied-room override, hardwired life-safety relay, and service-egress escape.

### Questions

1. Is Apex's mixture of delegated facility security, proprietary-system control, government program access, and first-line incident response plausible under defense contracting arrangements?
2. Are the distinctions among corporate authority, government classification authority, program authority, and lawful custody clear enough?
3. Would a secure facility plausibly permit the access-profile changes, room isolation, elevator/stair controls, and sector quarantine shown?
4. Are the fire-alarm and county-response consequences credible after Julie pulls a manual station during a ventilation/life-safety fault?
5. Could an inert-gas or clean-agent suppression system reduce oxygen as described, and would an occupied-room interlock, malicious executive override, pre-discharge sequence, abort control, and external physical reset operate this way?
6. Is the two-zone verified-fire strategy plausible, including a power-distribution heat condition, smoke/particulate sampling, hardwired egress relay, security-lock subordination, and continued agent discharge after gate opening?
7. Would the production gate, pressure equalization, optical threshold, hinge arcs, emergency cycle control, and local override sequence behave credibly?
8. Which details present safety or liability problems that a knowledgeable reader would immediately reject?
9. Which elements are credible and should remain unchanged?

## 4. PKI / Hardware Token / Digital Forensics Review — UNREVIEWED

**Minimum useful reviewer profile:** Applied cryptographer, HSM or hardware-token engineer, PKI architect, secure-identity specialist, digital-forensics examiner, or practitioner experienced with non-exportable keys and signed audit records.

### Current identity and proof baseline

- `APX-DIR-0019` mirrors Elias's identity binding and public certificate.
- The server record asserts that biometric confirmation succeeded and preserves workstation, clock, credential-path, and identity metadata.
- No live finger is reproduced, the private key inside Elias's physical board is not invoked, and the original 02:14 event has no matching physical signing-counter event.
- Later gate and recovery events are distinct live-biometric and physical-private-key acts.
- `APX-DIR-0019` does not identify the original human operator.
- Vance's later authenticated release does not prove he performed the original deployment.

### Primary scenes

- Chapters 2, 7–10, and 17: identity/public-certificate mirror, workstation path, `APX-DIR-0019`, secure-element board, local biometric release, immutable or tamper-evident gate record, evidence case, recovery cartridge, monotonic counters, and certificate chain.
- Chapters 20–22: blind replication, portable signer custody, challenge-response events, continuity broker, identity-construction family, and Vance's later live-authenticated release.
- Relevant WSS-4 and Hartwell passages in Chapters 11–14 and 19.

### Questions

1. Is the distinction credible between mirroring identity/public-certificate metadata and physically invoking a private key inside the secure element?
2. Can a monotonic hardware-signing counter plausibly exclude the board's physical participation in the original 02:14 event while preserving later emergency signatures?
3. Are the live-finger release, liveness check, local challenge, rotating code, private-key operation, and local audit described accurately enough?
4. Would a standalone read-only reader expose the public certificate, asserted identity metadata, and counter history without invoking a private key or changing source state?
5. Is the blind replication method defensible, including reference-token testing, continuous lifetime counter, no write path, and vendor objection?
6. Could `APX-DIR-0019` function as an executive hardware authority/service binding while leaving the original human operator and personal keystrokes unproved?
7. Is the WSS/Hartwell portable signer chain credible: office-registered serial, local challenge cradle, hardware response, device time, closed case, and separate legislative custody?
8. Does the continuity-broker mechanism plausibly inherit Price's legitimate request identity/reference and construct an operational route without preserving a human caller in the produced journal?
9. Which cryptographic or forensic terms should be replaced to avoid implying impossible guarantees?
10. Which elements are credible and should remain unchanged?

## 5. Federal Investigation / Evidence Custody / Legal Process Review — UNREVIEWED

**Minimum useful reviewer profile:** Federal criminal practitioner, D.C. prosecutor or defense attorney, federal agent, evidence-custody specialist, former MPD/federal liaison, or attorney experienced with classified-program investigations.

### Current custody and release baseline

- MPD initially controls physical custody.
- DCIS accepts bounded federal investigative responsibility without automatically taking the evidence chest or every source original.
- No federal charge has been filed at the time of Julie's release, no present federal detainer is sought, and the D.C. prosecutor declines to paper a local charge that day.
- Julie is released through written MPD authorization accepted by the watch commander.
- Counsel arranges medical transport and records availability and evidence-preservation undertakings; those undertakings are counsel agreements rather than judicially imposed release terms.
- Later arrest, warrant, summons, detainer, or charging remains possible.
- Classified access is not restored, and evidence contact remains prohibited without new written authority.

### Primary scenes

- Chapters 15–17: MPD apprehension, seven-package separation, scene authority, medical removal, unnamed federal demand, overnight hold, DCIS receiving authority, represented consent, and first examination.
- Chapters 19–23: federal incident receipt, foreign bounded acknowledgment, Hartwell production, legislative-security no-use hold, Price comparison, Apex source production, public correction, and unresolved charging.
- Chapter 24: federal and D.C. prosecutorial consultation, absence of a present federal detainer, D.C. no-paper decision, written MPD release authorization, counsel-arranged medical transport, preservation undertakings, and unresolved later process.

### Questions

1. Is MPD's initial custody of classified physical evidence plausible pending a named federal receiver and classification plan?
2. Are the seven packages appropriately separated, with the aluminum case, recovery cartridge, paper log, telematics module, waterproof folder/itemization, administrator board, and dual-partition module remaining distinct?
3. Would DCIS have plausible jurisdiction and bounded lead/receiving responsibility for the defense-contract and classified-program aspects while MPD retains physical custody?
4. Are the overnight delay, representation requirements, medical limits, written examination authority, and independent tool selection realistic?
5. Is the multi-day timeline plausible for obtaining DIA, Apex, Hartwell, LSS, Northbridge, Indian military, program-office, prosecutorial, preservation, and production actions?
6. Could Legislative Secure Services maintain a no-use hold and resist executive seizure of a Senate-office device in the way shown?
7. Are privilege, classification, source-custody, and cross-reference limits credible when three institutions issue separate public corrections?
8. Would law-enforcement bulletins be amended rather than overwritten, and could the original private-security alert remain preserved beside later corrections?
9. Is Chapter 24's release sequence plausible: written MPD authorization, watch-commander acceptance, no present federal detainer, a D.C. prosecutor declining to paper a charge that day, counsel-arranged transport, and voluntary preservation/availability undertakings?
10. Are the continuing possibilities of later arrest, warrant, summons, detainer, or charging stated accurately without implying a current judicial release proceeding?
11. Which agency names, titles, receipts, consent forms, warrants, subpoenas, or procedural steps require correction?
12. Which elements are credible and should remain unchanged?

## 6. Indian Army / Artillery / South Asia Security Review — UNREVIEWED

**Minimum useful reviewer profile:** Current or former Indian Army officer, artillery practitioner, South Asia defense analyst, Line-of-Control security specialist, or practitioner familiar with Indian field command and escalation practice.

### Primary scenes

- Chapters 2, 4–5, 8, 18, and 23: Forward Post Arjun, Northern Command, brigade pressure, artillery readiness, Point Kestrel patrol, K-17 inspection, local custodian, no-fire decision, and public operational statement.

### Questions

1. Are the ranks, forms of address, roles, and command relationships plausible, including Major Ananya Sharma, Lieutenant Qureshi, Captain Rao, Naib Subedar Sethi, and Lance Naik Pal?
2. Is the relationship among forward post, batteries, brigade, Northern Command, fire-direction personnel, and local relay custody credible?
3. Are ammunition movement, mechanical readiness, radar use, staged fire-control data, loaded-tube safety, and counter-battery abort procedures accurate?
4. Would Sharma plausibly retain or exercise the local authority to hold fire after receiving a validated allied product and a written higher-command order?
5. Are the mountain movement, icing, observation, Point Kestrel approach, patrol hard-stop, Line-of-Control risk, and casualty response credible?
6. Could K-17's exterior isolation cartridge and local maintenance confirmation be handled by the identified personnel and under the depicted field conditions?
7. Does the U.S.–India warning integration create geopolitical or sovereignty implications that require additional setup or different wording?
8. Are Pakistan-facing terminology, escalation assumptions, and field behavior balanced and plausible rather than simplified for the plot?
9. Which elements are credible and should remain unchanged?

## 7. Trauma Medicine / Injury Continuity Review — UNREVIEWED

**Minimum useful reviewer profile:** Emergency physician, trauma surgeon, paramedic, sports-medicine physician, or clinician experienced with concussion, rib/chest injury, wrist/thumb injury, and hip injury.

### Primary scenes

- Chapters 6–15: Julie's wrist injury; Marcus's rib, scalp, thigh, boot, breathing, balance, and concussion symptoms; Elias's hip injury, dizziness, cold exposure, and injured biometric finger.
- Chapters 15–17 and 24: paramedic assessment, oxygen saturation, hospital transport, imaging, restraint accommodations, representation limits, and discharge restrictions.

### Questions

1. Can Julie plausibly drive, handle the case, brace doors, and continue through Hartwell with the described wrist and ligament injury?
2. Can Marcus plausibly fight, walk, drive briefly with his left foot, maintain custody, and remain oriented with the described rib injury, scalp wound, low oxygen saturation, thigh trauma, and concussion symptoms?
3. Can Elias plausibly walk, use stairs, manipulate the module, and authenticate with the described hip injury, dizziness, cold exposure, and cut finger?
4. Are the field assessments and first-aid choices credible, including pupil checks, no rib binding, wound cleaning, makeshift wrist support, cold packs, and movement limits?
5. Are the paramedic, hospital, restraint, oxygen, imaging, observation, and discharge decisions plausible?
6. Which actions require reduced duration, assistance, changed injury severity, or different medical description?
7. Provide a chapter-by-chapter capability ceiling for Julie, Marcus, and Elias.
8. Which elements are credible and should remain unchanged?

## Review Deliverable Required

For each specialist area, provide:

- reviewer name, relevant qualifications, and review date;
- exact manuscript baseline reviewed: `main` commit `0a0ed1c5330cbe48a59499d7a4104aa02f6c059a`, manifest version 2, or a compilation generated from that manifest;
- factual or procedural errors ranked as **critical**, **material**, **minor**, or **preference**;
- exact chapter and passage affected;
- the smallest correction that preserves plot, timing, character decisions, and suspense;
- any term that should be replaced with authentic professional language;
- any scene that remains implausible even after terminology changes;
- confirmation of what is credible and should not be overcorrected;
- final disposition of **approved**, **approved with corrections**, or **not approved**.

No specialist correction should be incorporated without a subsequent continuity review across the accepted manuscript and control files. No area may be marked reviewed without a named, dated, qualification-backed deliverable. No reviewer disposition by itself marks the book ready for publication.
