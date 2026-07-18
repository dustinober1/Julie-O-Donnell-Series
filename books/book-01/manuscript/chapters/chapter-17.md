# Chapter 17 — The First Examination

October 14
09:17 Eastern Daylight Time

Secure MPD Evidence Intake
Washington, D.C.

“The question is smaller than the accusation.”

Special Agent Leila Grant said it before anyone opened the chest.

Julie sat in the camera-covered observation alcove with her left wrist secured to the front rail and her right forearm inside a rigid hospital immobilizer. Overnight imaging had found no fracture requiring surgery and enough ligament and soft-tissue damage to make grip, rotation, and ordinary writing impossible. The physician had cleared her for a two-hour recorded proceeding, not for work.

The distinction was written on the medical authorization beside her.

NO KEYBOARD ACCESS.
NO EVIDENCE HANDLING.
NO POSITIONING OR LIFTING.
STOP ON INCREASED SWELLING, NUMBNESS, OR DIZZINESS.

Grant stood at the examination table wearing a plain dark suit beneath a disposable grounding coat. Her serialized kit remained closed in a hard case at her feet. She had arrived with a DCIS digital-evidence technician, but the technician’s role was limited to documenting Grant’s tool before and after use. The method and conclusion belonged to Grant.

Officer Ortiz held one key to the common chest. MPD property supervisor Hannah Park held the second. Their body cameras were backed by two fixed room cameras and a third lens aimed only at the wall clock and examination surface.

Miriam Alvarez appeared on the authenticated DCIS channel. Apex counsel occupied a separate window. General Hackett had observer status but no control over the room.

Elias and his attorney joined from a hospital consultation suite. His injured hip was supported by a wedge beneath the left leg. A fresh dressing covered the cut on his right index finger. Both hands remained visible above the blanket. He looked as if sleep had occurred near him rather than to him.

His attorney identified herself and the scope of his consent.

“Mr. Thorne consents to a non-destructive examination of the administrator-token board for hardware identity, public certificate state, monotonic signing history, and presence or absence of a physical signing event corresponding to the original 02:14 deployment. He does not consent to invocation of a private key, biometric challenge, modification, repair, firmware access, or examination beyond the stated hardware question.”

Grant asked Elias, “Is that your decision?”

“Yes.”

“Has anyone promised immunity, employment protection, restored access, or favorable treatment in exchange?”

“No.”

“Are you under medication that prevents you from understanding this proceeding?”

“No. Pain medication at six this morning. Nothing sedating since.”

His counsel confirmed the hospital record.

Grant read the authorities into the room.

MPD retained physical custody. DCIS controlled the examination method. Elias controlled consent to the board inspection. Apex had notice, access to the video feed, and the right to submit technical objections. It could not select the reader, touch the board, or direct Grant’s queries. No other package would open. No source data would enter the tool. No finding about motive, operator identity, conspiracy, or the legal status of Elias’s later emergency acts could be drawn from the hardware test.

Apex counsel objected before the chest moved.

“The board’s monotonic counters are meaningful only within the Apex certificate and mirror-service architecture. A local reader cannot exclude an authorized server-side signature, backup authority, or emergency identity service.”

Grant entered the objection verbatim.

“Today’s finding will not exclude every server-side mechanism. It will answer whether this physical secure element performed the original signing act attributed to it and whether its later emergency acts are distinguishable.”

“The absence of a local event could be consistent with authorized remote operation.”

“Then the later record must identify the remote operation. This board does not become evidence of it by silence.”

Julie watched Grant close the objection pane.

Six years earlier, the Army had treated the surviving server record as stronger than the local event Julie remembered because the local cache had disappeared. Grant had reversed the order. She would not make the physical object prove a remote theory it did not contain.

Ortiz and Park approached the common chest together. They read the outer seal, compared it to the prior night’s fixed-camera record, and unlocked the two-key system. The lid rose only far enough for all seven packages to remain visible.

Park named each package by role, not by theory. Case. Recovery cartridge. Paper log. Telematics module. Waterproof folder and itemization. Administrator board. Dual-partition field module.

She removed only the board package. Ortiz closed the chest, and both officers applied a temporary examination seal before the package crossed the yellow floor line.

Nothing else entered the scene.

Grant photographed the board package beneath the overhead camera. The intake seal matched. She opened the outer enclosure and lifted the antistatic sleeve by its edges.

“Mr. Thorne, identify what you can identify without assuming internal state.”

“The administrator-token board I carried out of Building Three. Secure-element serial EAT-0881147. Scrape at the upper-left corner from the cooling gallery. Contact marks from the enclave gate and recovery console. One edge of the badge housing was no longer flush before police received it.”

“Does that identification establish the contents are unchanged?”

“No.”

“Does possession establish you used it at 02:14?”

“No.”

Grant removed the board. The corner scrape, copper-contact wear, and housing pressure mark matched Park’s intake images. Grant did not call them unique. She called them consistent.

The standalone reader had been purchased and held by DCIS before the incident. Its source-side interface exposed only the secure element’s public hardware identity and immutable event counters. The network port had been physically removed. A write-test block occupied the service slot. The technician photographed the empty external ports and demonstrated the known reference token before the evidence board approached the reader.

The reference token carried four signed events. The reader returned four in order and reported zero source writes. Grant restarted the device and repeated the test.

Same result.

Only then did she seat Elias’s board.

The first screen showed the secure-element serial and author certificate associated with VAL-088. Grant compared the displayed serial to the etched hardware and package record.

Match.

She asked for the monotonic signing state surrounding 02:14 on October 13.

No event appeared.

She widened the range by twelve hours in each direction.

Still none.

Grant asked the reader for the board’s lifetime counter, manufacturing initialization, last verified maintenance event, and every increment between them. The total was continuous. No rollover, reset, skipped number, or counter-repair event appeared. The deployment interval sat between two ordinary development signatures without room for the missing act.

Apex counsel argued that the secure element could have entered an emergency shadow mode not exposed to an untrusted reader. Grant requested the public certificate policy stored on the board. The policy listed every event class capable of using the private key. Emergency administrator access remained counter-bound. Backup signing remained counter-bound. Recovery signing remained counter-bound. No uncounted shadow mode appeared.

“That policy could be incomplete,” counsel said.

“It could,” Grant replied. “Produce the signed manufacturer extension or Apex modification that adds the claimed mode. Until then, the physical object exposes one continuous counter.”

Julie watched Grant refuse the temptation to call the missing event impossible. She made Apex carry the mechanism it proposed instead of using confidence in the board as a substitute.

Apex counsel said, “That does not exclude a mirrored-signature service presenting the board certificate without advancing the local counter.”

Grant looked at the screen. “Correct. It excludes physical signing by this board in the displayed range.”

The counsel tried again. “You cannot say the deployment signature was false.”

“I have not.”

Grant moved to the emergency period.

The counter advanced when Elias authenticated the quarantine gate. That event included the local challenge, emergency administrator role, live-finger release, and hardware time state. It advanced again at the provenance reconciliation, carrying the new rule adjustment, restored label confirmation, and sealed recovery reference.

Grant did not stop at one view. She queried by counter order, by time range, and by event class. Then she shut down the reader, had the technician confirm its state, restarted it, and ran the same queries again.

The sequence did not change.

Original deployment event absent.

Later emergency gate event present.

Later recovery event present.

The board treated the acts as different because they were different physical uses.

Grant turned to Elias’s screen.

“Can this secure element produce a signature without advancing its monotonic counter?”

“Not while remaining valid. The counter increments inside the element before the private-key operation completes.”

“Can the private key be copied?”

“Not through any supported process. Extracting it would destroy or invalidate the secure element.”

“Can the board’s identity be presented through another service?”

“Yes. A system can replay the public certificate, mirror the workstation, or assert an identity binding. That can make a server record look like the employee and token acted together.”

“Does this board identify who performed such a replay?”

“No.”

“Does it establish APX-DIR-0019 performed one?”

“Not by itself.”

“Does it establish the original deployment was unauthorized?”

“No. It establishes that the physical act attributed to this board did not occur on this board.”

Grant looked toward Alvarez’s window. “Proposed direct finding.”

She read it slowly enough for every source to object.

“Physical token EAT-0881147 contains no signing event corresponding to the original 02:14 deployment attribution. It contains distinct later signatures for the emergency gate and provenance reconciliation, each with live biometric release and local hardware state. The earlier identity may have been mirrored, replayed, or constructed through another mechanism. This examination does not identify that mechanism or operator.”

Hackett leaned toward his camera. “That clears Thorne of deployment.”

Alvarez answered before Julie could.

“It excludes the physical mechanism the original record asserted. It does not identify every other possible authority path, and it does not decide his later conduct.”

Grant added, “The later acts remain physically authenticated.”

Elias’s attorney looked toward him. “Do you want to attach a statement?”

Elias stared at the board on Grant’s table.

“My father learned from the news that I was called a hostage, then a possible saboteur. I was supposed to be at his retirement dinner last night.” His voice tightened, but he kept going. “That does not change the record. I opened the gate. I authenticated the recovery. I restored the labels, removed the recorder, entered Northbridge, and held the module after the abort. Those acts are mine. The original deployment is not.”

Grant asked whether he wanted the family reference included.

“No. Put only the acts in the formal attachment.”

The personal cost remained spoken and did not become proof.

Grant entered the represented voluntary statement separately from the hardware finding.

Julie watched Elias sign left-handed on his hospital screen. His name appeared below acts that could still prosecute him. He had refused the version of innocence that required the record to forget what he had chosen.

Grant removed power from the reader. The technician confirmed zero source writes and the same tool state shown before the examination. Grant photographed the board again, returned it to its antistatic sleeve, and closed the MPD package under a replacement seal. The former seal entered a labeled evidence pocket.

Ortiz and Park reopened the common chest under dual control, restored the package to its marked position, and closed the lid.

Seven packages remained seven.

No technical subset had left the room.

Apex counsel requested that the finding await a complete architecture explanation.

“You may submit one,” Alvarez said. “It will accompany the result as an objection and supporting theory. It will not delay the direct hardware observation.”

The examination record sealed at 10:06.

BOARD EAT-0881147
ORIGINAL DEPLOYMENT PHYSICAL SIGNATURE: NOT PRESENT
LATER EMERGENCY SIGNATURES: PRESENT / DISTINCT / LIVE RELEASE RECORDED
REPLAY OR MIRROR MECHANISM: NOT IDENTIFIED

The result created the next question without answering it.

If the physical board had not signed, what had assembled the complete-looking deployment identity?

Grant requested three independent source records: the government program registry state surrounding 02:14, the source-native Apex identity-mapping journal, and Elias’s workstation access history. Each would remain with its own custodian and state its clock basis and withheld fields.

Hackett asked, “Why all three?”

“Because a constructed identity should create disagreement between the physical token, the government registry, and the contractor’s identity layer. If all three agree, this examination is incomplete. If one differs, we learn where the account was assembled.”

Julie felt a brief, unreasonable relief.

Grant had not inherited Julie’s method. She had arrived at her own.

A second channel opened from DIA. Leland Price was alive, represented, and on restricted administrative leave. His classified access remained suspended. DIA had preserved his authentic raw-source request, the transient display record, and the chronology ending his authority. No general interview or production would occur until counsel and the review office agreed on scope.

Julie asked, “Was he detained on October twelfth?”

The DIA representative answered carefully. “He was not in criminal custody. He was removed from classified access, directed to remain available, and restricted from the workplace during an administrative inquiry.”

The distinction corrected Marcus’s assumption that Price had disappeared into detention. It did not make the suspension or timing harmless.

Julie looked toward Grant. “Sarah’s preservation notice supports—”

“Sarah’s notice supports what she directly received, issued, and preserved,” Grant said. “It does not tell us what she knew before those moments.”

Julie stopped.

She had revised her judgment of Sarah once and had already begun turning the correction into a broader conclusion. Grant kept her from replacing one simplification with another.

At 10:14, Ortiz read the common chest state.

Seven packages. All current seals green. Board replacement seal documented. No later movement or connection.

The words no longer needed to be repeated every few minutes. The fixed cameras and custody system would carry them until something changed.

Grant’s first finding left the room under her signature, Alvarez’s authority, MPD’s custody reference, Elias’s represented statement, and Apex’s objection.

It did not clear the case.

It made the original accusation physically harder to sustain.