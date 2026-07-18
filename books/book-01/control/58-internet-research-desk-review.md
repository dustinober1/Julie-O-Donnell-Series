# Book 1 Internet-Research Desk Review

**Manuscript:** *Veridrift*  
**Branch:** `agent/book1-internet-research-review`  
**Review date:** 2026-07-18  
**Method:** Public-source desk research using official government standards, doctrine, court guidance, and medical guidance.  
**Status ceiling:** **INTERNAL DESK REVIEW — NOT EXTERNAL SPECIALIST APPROVAL**

This review identifies corrections that can be supported from public authoritative sources. It cannot validate classified architectures, unit-specific procedures, unpublished rules of engagement, or the exact practices of the fictional institutions. Issues #70–#76 remain open until named qualified reviewers deliver dated findings.

## Editorial rules used

1. Preserve plot, chronology, POV order, evidence outcomes, character decisions, suspense, and the final line.
2. Correct only a contradiction or overstatement supported by an authoritative public source.
3. Preserve fictional system names and mechanisms where public sources establish plausibility but not exact implementation.
4. Do not convert public-source plausibility into proof that a classified or fictional procedure exists.
5. Record uncertainty rather than inventing specificity.

## Finding summary

| ID | Area | Severity | Decision | Affected prose |
|---|---|---|---|---|
| DR-01 | Military targeting / UAS / JAG | Material | ACCEPT-MODIFIED | Prologue |
| DR-02 | PKI / hardware token / digital forensics | Material | ACCEPT | Chapter 2 |
| DR-03 | Federal investigation / custody / legal process | Material | ACCEPT-MODIFIED | Chapter 24 |
| DR-04 | SIGINT / ELINT / provenance | Retain | NO PROSE CHANGE | Prologue; Chapters 1–2, 8, 10, 18 |
| DR-05 | Secure facility / fire / suppression | Retain with limitation | NO PROSE CHANGE | Chapters 2–3, 5–9 |
| DR-06 | Indian Army / artillery / South Asia | Retain with limitation | NO PROSE CHANGE | Chapters 2, 4–5, 8, 18, 23 |
| DR-07 | Trauma medicine / injury continuity | Retain | NO PROSE CHANGE | Chapters 6–17, 24 |

---

## DR-01 — Military targeting / UAS / JAG

### Public-source basis

- U.S. Air Force Doctrine Publication 3-60, *Targeting*, 1 May 2026: https://www.doctrine.af.mil/Portals/61/documents/AFDP_3-60/3-60-AFDP-TARGETING.pdf
- U.S. Air Force Doctrine publication page: https://www.doctrine.af.mil/Doctrine-Publications/AFDP-3-60-Targeting/
- U.S. Air Force MQ-9 Reaper fact sheet: https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104470/mq-9-reaper/

### Source principles

AFDP 3-60 separates intelligence, targeting, operations, and command functions. During execution, the Air Operations Center’s Combat Operations Division supervises the air tasking order; targeteers monitor execution and recommend changes; the senior intelligence duty officer supplies analysis. The doctrine separately notes that a platform may complete all kill-chain steps only when it carries both the relevant capabilities and target-engagement authority. Legal and rules-of-engagement review remain integrated throughout targeting.

### Finding

The prologue already treats Julie’s act as an “abort recommendation” during the later investigation, but the live scene says she “transmitted the order.” That phrase gives an intelligence officer personal engagement authority the surrounding scene does not establish. Hargrove holds the push-to-talk authority, command has approved the package, and the aircraft is waiting on release criteria.

### Correction

Change only:

> transmitted the order

To:

> transmitted the formal abort recommendation

The radio call, four-second gateway delay, release timestamp, pilot call, Hargrove pressure, and investigation remain unchanged. The revision clarifies authority without reducing Julie’s urgency or moral responsibility.

### Residual external-review questions

- Whether “Overwatch,” “Rifle,” and the exact pilot/controller call sequence fit the fictional operation.
- Whether a software authentication gateway would sit in this emergency route.
- Whether Hargrove’s position would permit the delay shown.
- Whether the four timestamps and post-strike inquiry language match a specific service/JAG practice.

**External issue remains open:** #71.

---

## DR-02 — PKI / hardware token / digital forensics

### Public-source basis

- NIST SP 800-63B-4, *Digital Identity Guidelines: Authentication and Authenticator Management*: https://pages.nist.gov/800-63-4/sp800-63b.html
- NIST SP 800-63B authenticator requirements: https://pages.nist.gov/800-63-4/sp800-63b/authenticators/
- NIST SP 800-63B replay-resistance discussion: https://pages.nist.gov/800-63-3/sp800-63b.html
- RFC 5280, *Internet X.509 Public Key Infrastructure Certificate and CRL Profile*: https://www.rfc-editor.org/rfc/rfc5280

### Source principles

A hardware cryptographic authenticator can keep a private key non-exportable and require a local activation factor for each private-key operation. Challenge/nonce protocols are designed to resist recorded-message replay. A certificate binds identity information to a public key; possession or presentation of certificate data does not prove that the associated physical private key signed a particular event. A verifier or compromised service can preserve or fabricate identity metadata and status assertions without reproducing the physical biometric act.

### Finding

Chapter 2 says APX-DIR-0019 “replayed his biometric token” and preserved an “expected biometric response.” Chapter 17 later and more carefully establishes that the physical board’s counter did not advance at 02:14, while later live-finger/private-key acts did advance it. The Chapter 2 wording therefore overstates what the administrative service reproduced and conflicts with the book’s strongest forensic finding.

### Correction

Replace the overstatement with a mirrored identity binding, public-certificate presentation, and server-side assertion that biometric release had been confirmed. Add an explicit proof limit: the mirror did not reproduce a live finger or invoke the private key inside the physical token.

This preserves the false attribution, complete-looking audit trail, APX-DIR-0019 layer, Elias’s fear, and Chapter 17’s counter evidence.

### Residual external-review questions

- Whether a monotonic counter would expose the exact history described.
- Whether the standalone reader and blind replication method are vendor-neutral and non-destructive.
- Whether the audit fields and certificate terminology should be refined for a specific secure-element architecture.

**External issue remains open:** #73.

---

## DR-03 — Federal investigation / evidence custody / legal process

### Public-source basis

- Federal Rule of Criminal Procedure 5, initial appearance without unnecessary delay: https://www.law.cornell.edu/rules/frcrmp/rule_5
- District of Columbia Courts, arrests and “Arrest Only / No Paper” outcomes: https://www.dccourts.gov/superior-court/superior-court-divisions/criminal-division/arrests
- District of Columbia Courts, first appearance: https://www.dccourts.gov/index.php/node/205
- District of Columbia Courts, arraignment and presentment: https://www.dccourts.gov/superior-court/superior-court-divisions/criminal-division/arraignment
- U.S. Courts, pretrial release and detention: https://www.uscourts.gov/about-federal-courts/probation-and-pretrial-services/pretrial-release-and-detention-federal-judiciary
- Department of Justice examples describing DCIS as the criminal investigative arm protecting DoD procurement and programs: https://www.justice.gov/opa/pr/executive-pleads-guilty-multi-million-dollar-bid-rigging-conspiracy

### Source principles

A federal arrest normally requires a prompt federal initial appearance. D.C. arrests ordinarily proceed to D.C. Superior Court arraignment/presentment, while a prosecutor may decline to proceed, creating an “Arrest Only” or “No Paper” outcome. Federal pretrial conditions are imposed in a federal criminal case; a federal magistrate does not ordinarily serve as the release authority for an MPD-only custody event when no federal detainer or charge exists. DCIS involvement in suspected defense-contract fraud and misuse of DoD systems is credible at a high level.

### Finding

Chapter 24 has a federal magistrate enter an order directing MPD to remove a local restraint immediately after the United States Attorney declines a federal detainer and while no charge has been filed. The authority is allocated to the wrong judicial chain. The desired story function is valid: independent release authority, unresolved charging exposure, medical transport, and enforceable evidence boundaries.

### Correction

Reframe the event as:

- written MPD release authorization following a recorded multi-party custody conference;
- no present federal detainer;
- a D.C. prosecutor declining to paper a local charge that day;
- voluntary written preservation undertakings made through counsel;
- release for counsel-arranged medical transport, subject to any later lawful arrest, warrant, summons, or detainer.

This preserves unresolved charging, the separation between public correction and personal liability, the seven-package no-contact boundary, the medical sequence, and the authority-centered theme.

### Residual external-review questions

- Whether the preceding multi-day custody interval is justified by the story’s medical and calendar facts.
- Which specific prosecutor, court, or written form would control the release.
- Whether DCIS would be lead, co-lead, or a receiving agency in the exact classified-program configuration.
- Whether the fictional legislative-security hold needs a more explicit statutory or chamber-rule basis.

**External issue remains open:** #74.

---

## DR-04 — SIGINT / ELINT / source provenance

### Public-source basis

- NIST provenance glossary: https://csrc.nist.gov/glossary/term/provenance
- NIST Research Data Framework, provenance and chain-of-custody concepts: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/1500-18/NIST.SP.1500-18r2.html

### Assessment

The manuscript consistently distinguishes original observations, metadata, transformations, source labels, derived products, cached conclusions, and proof limits. NIST defines provenance as the documented chronology of origin, processing, ownership, location, and alteration; the book’s recovery and custody logic follows that conceptual structure.

The eleven-point-two-second interval, environmental deviation, impossible granite path, reconstructed carrier family, correction-dependent side table, and source-reconciliation machinery are fictional technical details. Public sources can support the logic of traceability and transformation but cannot validate the exact SIGINT/ELINT implementation.

### Decision

Retain the prose. It presents anomalies as grounds for challenge, not proof; preserves primary observations; and separates correction of source status from deletion of raw data.

**External issue remains open:** #70.

---

## DR-05 — Secure facility / fire / suppression

### Public-source basis

- OSHA interpretation on access-controlled egress doors: https://www.osha.gov/laws-regs/standardinterpretations/2003-11-21
- OSHA fixed-extinguishing-system guidance: https://www.osha.gov/etools/evacuation-plans-procedures/emergency-standards/fixed-extinguishing
- OSHA definition of oxygen-deficient atmosphere and inerting: https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.146
- NIST, *Clean Agent Suppression of Energized Electrical Equipment Fires*: https://www.nist.gov/publications/clean-agent-suppression-energized-electrical-equipment-fires-0

### Assessment

The hardwired life-safety path that subordinates access-control locks during verified fire is credible in principle. OSHA guidance recognizes fire-alarm/detection release, loss-of-power release, and direct manual egress release independent of access-control electronics. Total-flooding gaseous systems can create oxygen-deficient or otherwise hazardous atmospheres and require evacuation safeguards.

The occupied-room override and disabled manual abort must be understood as malicious defeat of safety controls, not normal compliant operation. The manuscript already frames them that way: the physical safety path survives while the incident controller has been manipulated.

### Decision

Retain the prose. No public source justifies rewriting the exact fictional enclave, gate, detector zoning, or suppression controller. The external reviewer should focus on discharge concentration, pre-discharge timing, abort/reset design, pressure equalization, and the plausibility of the two-zone fire method.

**External issue remains open:** #72.

---

## DR-06 — Indian Army / artillery / South Asia security

### Public-source basis

- Government of India, Ministry of Defence, Line of Control surveillance and monitoring measures: https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1703760&lang=2&reg=48
- Government of India, Indian Army operational preparedness along the Line of Control: https://www.pib.gov.in/PressReleaseIframePage.aspx?PRID=2088180&lang=2&reg=48
- Government of India, SANJAY battlefield-surveillance system integrating ground and aerial sensor inputs: https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=2095712&lang=2&reg=48
- Government of India statement on artillery and civilian-harm restraint along the Line of Control: https://www.pib.gov.in/Pressreleaseshare.aspx?PRID=1567641&lang=2&reg=48

### Assessment

Official Indian sources support a high-level picture of persistent Line of Control surveillance, human and technical sensor integration, operational preparedness, artillery capability, and attention to escalation and civilian harm. They also support automated fusion of ground and aerial sensor inputs into a common surveillance picture.

The fictional bilateral warning pilot is not publicly verifiable. The manuscript responsibly retains Indian weapons authority and gives Sharma an independent no-fire decision based on absent local confirmation and terrain uncertainty.

### Decision

Retain the prose. Do not infer from public modernization statements that the exact U.S.–India machine-readable feed, rank relationships, battery procedures, or K-17 custody arrangement exist.

**External issue remains open:** #75.

---

## DR-07 — Trauma medicine / injury continuity

### Public-source basis

- CDC, recovery after mild traumatic brain injury/concussion: https://www.cdc.gov/traumatic-brain-injury/response/index.html
- CDC, return to daily activities and caution with driving: https://www.cdc.gov/heads-up/hcp/clinical-guidance/index.html
- CDC, workplace limits after TBI: https://www.cdc.gov/traumatic-brain-injury/data-research/facts-stats/tbi-in-the-workplace.html
- NCBI Bookshelf, rib-fracture evaluation and management: https://www.ncbi.nlm.nih.gov/books/NBK541020/

### Assessment

The manuscript consistently limits Julie’s grip, rotation, lifting, writing, and driving; limits Marcus through rib pain, low oxygen saturation, head injury, thigh injury, and concussion observation; and limits Elias through hip pain, dizziness, cold exposure, exhaustion, and a hand wound. CDC guidance supports symptom-guided return to activity and particular caution with driving, attention, reaction time, heights, strenuous work, and machinery. Rib-fracture guidance supports imaging when broader trauma is suspected, pain control, respiratory monitoring, and conservative treatment for uncomplicated injuries.

Chapter 24’s physician prohibition on Julie driving, lifting, ordinary right-handed writing, grip, and rotation is especially credible. Marcus’s oxygen and imaging sequence is proportionate to the symptoms shown.

### Decision

Retain the prose. A trauma specialist should still verify exact oxygen values, transport priority, restraint choices, imaging sequence, and three-day capability progression.

**External issue remains open:** #76.

---

## Desk-review disposition

### Corrections authorized now

1. Prologue: clarify that Julie sends a formal abort recommendation rather than personally exercising engagement authority.
2. Chapter 2: distinguish mirrored identity/public-certificate metadata from live biometric and physical private-key use.
3. Chapter 24: place release authority in the local custody/prosecutorial chain and make preservation limits counsel undertakings rather than unsupported federal pretrial conditions.

### Material retained unchanged

- Eleven-point-two-second interval.
- Environmental-deviation finding.
- Impossible path through granite.
- Payload 88 → post-archive derivative → SIGMA-NORMALIZE-4 causal chain.
- Hardwired verified-fire egress path.
- Indian weapons authority and Sharma’s no-fire decision.
- Seven-package evidence separation.
- DCIS’s bounded defense-contract/program inquiry.
- Injury and treatment continuity.
- Vance, Sterling, and original-constructor proof ceilings.
- Final line: **The bubble stayed centered.**

### Gate status

This desk review reduces known public-source errors but does not close issues #70–#76. Publication remains blocked pending named, qualified external dispositions and final copyedit/production proof.