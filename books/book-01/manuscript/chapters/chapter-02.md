# Chapter 2 — The Poisoned Feed

The first thing Julie did was try to prove herself wrong. She pulled her chair closer to the terminal and ignored the black dome camera in the ceiling corner. Onscreen, the intercepted transmissions continued their impossible procession. Every eleven-point-two seconds. No drift. No degradation. No gaps. Marcus stood behind her with one hand on the empty chair. “You recognize it.”

“I recognize a resemblance.”

“What’s the difference?”

“Evidence.”

Julie opened the relay-health data beside the feed. Freezing rain moved across the mountain ridge. Wind gusts reached forty-six miles an hour. The relay had shifted twice to backup power, and one receiver had lost synchronization for seventeen seconds. Civilian bursts weakened when the rain intensified. Military traffic carried timing distortion. Satellite handshakes dropped packets and repeated them. Background noise rose and fell with the weather. Only the suspected target feed remained untouched. She selected six minutes and ran a variance comparison.

EXPECTED ENVIRONMENTAL DEVIATION: 8.4%
OBSERVED TARGET DEVIATION: 0.07%

Julie ran the comparison again with narrower and wider windows, then excluded the receiver loss and backup-power transitions. The percentages changed at the second decimal place and nowhere that mattered. She compared only the strongest target bursts, then the weakest surrounding traffic. She shifted the time window across the power transition and asked the system to recalculate against each receiver separately. The environment changed every time. The target did not.

A compensating transmitter could correct loss, but correction left stepped gain, repeated packets, timing shifts, or altered noise. A perfect correction would require the source to know the receiver’s future errors before they occurred. Even a military adaptive transmitter reacted after degradation reached it; it did not arrive pre-corrected for a gust that had not yet moved the antenna. The target behaved as if weather, terrain, and failing power were scenario labels rather than forces acting on hardware.

“Argus says there aren’t any artifacts,” Marcus said.

“Argus is deciding whether the signal matches its definition of a hostile source. I’m deciding whether the signal exists in the physical world.”

The packet metadata described a military-grade encrypted emitter moving south along a mountain supply road. Its estimated position drew a smooth route around the slope until the fourth burst crossed a granite outcrop. Julie rotated the topographic model and tested the path against the relay geometry. The packet claimed an eleven-meter location error. The rock face stood sixty feet high, and the eastern receiver’s line crossed granite for more than two hundred yards. If the coordinate were merely imprecise, the solution should have shifted to another receiver or expanded its uncertainty. Instead the file preserved a clean track and a confidence estimate precise enough to imply the terrain had never interrupted the source.

“So the coordinates came from a map.”

“Or the transmitter flew through solid stone.”

Julie marked the anomaly. It was enough to challenge the feed, not enough to stop certification by itself. Apex could call it a terrain-resolution defect, correct the track, and preserve the threat assessment. The company had language prepared for flaws that did not threaten the conclusion. Marcus picked up the government phone beside the keyboard. Its wireless functions had been disabled at screening; inside Room 402B it connected only through the facility’s classified network.

“I’m calling Price.”

The internal extension rang twice. A woman at the Security Review Office confirmed that Leland Price was unavailable and that his extension had been suspended under administrative access review. Marcus’s sponsorship covered the current consultation, not Price’s personnel status. When he asked whether Price had been detained, she repeated that Price was unavailable and ended the call.

Julie wrote the exact wording. Price’s extension was suspended. His status remained unknown. Anything beyond that was inference. The woman had known the boundary of Marcus’s sponsorship without asking for verification and had a prepared phrase that disclosed nothing a later reviewer could challenge. That did not prove Price had been silenced. It proved the institution had already chosen the language through which his absence would be described. Marcus disconnected the handset. “They suspended a DIA auditor for requesting source data.”

“Maybe.”

“You don’t believe that?”

“I believe what we can prove.”

“You never used to be this careful.”

“I used to mistake being right for being protected.”

Julie returned to the telemetry and stripped the encrypted content from one transmission, leaving the carrier beneath it. Every radio signal carried damage from the physical world: receiver noise, atmosphere, electrical interference, thermal variation, the fingerprint of the equipment that captured it. Most analysis systems filtered that material away.

Seven small fluctuations appeared near the beginning of the packet. The same cluster returned seventeen milliseconds later. Julie aligned a second packet by its synchronization pulse and subtracted the payload. The pattern remained. A third packet had been captured after the relay shifted to backup power; its payload and receiver temperature differed, but the same seven fluctuations appeared at the same relative amplitude. Atmospheric noise could resemble itself. Hardware faults could repeat. Digital filtering could create families of artifacts. None should reproduce a complex analog scar across changing conditions without variation. Identical.

“Marcus.”

He moved beside her. “Carrier noise doesn’t repeat exactly.”

“What would cause it?”

“A copied source. A generated source. Something built from a template.”

The current partition held no comparison library. Julie searched the visible directory and found three approved operational tools beside a restricted folder.

APX VALIDATION ARCHIVE
PROPRIETARY — MODEL ASSURANCE DIVISION

ACCESS DENIED
OUTSIDE AUTHORIZED REVIEW SCOPE

The live warning belonged to the government. The test material that might explain it belonged to the contractor. Even Marcus’s program-oversight credential showed temporary authority only over government operational data. The boundary was legally clean and operationally absurd: the government could act on the warning, but the officer responsible for the warning could not inspect the contractor material most likely to explain why it was wrong.

The contract divided sovereignty from control. The government owned the program requirement, classification authority, and operational decision. Apex operated Building Three, the ingestion architecture, validation archive, production release workflow, facility security, credential administration, and first-line incident response under delegated authorities distributed across several agreements. No single Apex role was sovereign. Together they let the company control the room, the data path, the access log, and the first account of a failure before a government officer could invoke a separate channel. The alternate government routes still entered through infrastructure Apex maintained.

Apex did not need to falsify a denial. It needed only to enforce the accepted boundaries until the certification clock expired. Marcus submitted an immediate request.

POTENTIAL SYNTHETIC CONTAMINATION OF OPERATIONAL INTELLIGENCE FEED.
IMMEDIATE COMPARISON REQUIRED TO SUPPORT OR EXCLUDE ACTIVE SYSTEM DEFECT.

PENDING CONTRACTOR APPROVAL.

“Who approves it?” Julie asked.

“Vance’s office.”

“Then he knows exactly what we’re looking for.”

“He knew when he changed your permissions.”

The wall intercom clicked. Sarah Chen told Marcus the request exceeded the agreed scope. He stated the suspected defect, the requested archive, and the operational reason in one sentence, creating a timestamped record before she could refuse. Sarah invoked contractor intellectual property and the boundary between government data and Apex development assets. Julie pressed the control. “How do you know the archive is unrelated if I haven’t compared it?”

“The Argus platform performs automated source-provenance checks before information enters operational processing.”

“Then the comparison should confirm that.”

“The comparison is unnecessary.”

“Because the machine already compared itself to itself?”

Sarah’s voice cooled. “The platform is certified to identify synthetic contamination.” Julie looked at the repeated carrier pattern. “It missed this one.”

“You have not established that.”

“That’s why I need the archive.”

“The archive is not included in your authorization.”

Marcus leaned toward the speaker. “We are discussing a possible false strategic warning, not a licensing dispute.”

“Technical boundaries do not disappear because you dislike them.”

Marcus said, “Put this on the record: Director Vance changed the consultant scope after the vehicle entered the campus, and his office is the approval authority now withholding the comparison set.” Sarah paused long enough for the compliance recorder to remain audible. “The access modification and approval chain are already in the session record. I will add your stated operational basis. I will not characterize the anomaly as sabotage, employee action, or source contamination until an authorized comparison supports one of those terms.”

The answer protected Apex’s scope and refused a conclusion Vance could later place in her mouth. The intercom went silent. Marcus asked whether Julie could enter the archive without permission. She reminded him that they were in a monitored facility analyzing classified data. He corrected the question: was there another way to make the comparison?

“That was a better question.”

The archive was restricted. Its index was not. Authorized users needed file names, creation dates, scenario labels, package owners, and classification fields before requesting access. The index could not reveal source files or carrier profiles, but it could show whether Apex had ever built something with the same operational shape. Julie filtered thousands of entries by geography, signal type, and packet interval, using metadata that existed to help authorized users find the very material the authorization boundary kept her from opening. SOUTH ASIA reduced the list to forty-seven. MOBILE ENCRYPTED EMITTER reduced it to nine. Eleven-point-two seconds left one.

VALIDATION PACKAGE 88
REGION: SOUTH ASIA
SCENARIO TYPE: CROSS-BORDER ARTILLERY MOBILIZATION
SOURCE MODEL: ENCRYPTED MOBILE COMMAND NETWORK
STATUS: ARCHIVED
OPERATIONAL USE: PROHIBITED

The contents remained locked, but the index showed the package owner.

THORNE, ELIAS M.
ADVANCED MODELING DIVISION
BUILDING THREE

The name connected a person to the test object. It did not show whether he still worked in the building, had production access, knew the package had moved, or had done anything beyond creating it. An author field could survive reorganizations, transfers, copied repositories, and administrative repackaging. Treating it as a deployment record would repeat the same error Argus made: replacing a physical act with the label most convenient to the model.

“Could he have injected it?” Marcus asked.

“He built a test package. That is not the same fact.”

The scenario, interval, geography, and likely carrier profile aligned. They established resemblance, not deployment. Marcus started toward the door. Julie caught his sleeve.

“They know every query I ran,” she said. “They do not know what I understood.”

Query mirroring could reconstruct every path she opened, but not the order of her conclusions unless she supplied them aloud. The advantage was narrow and temporary.

“Sit down. Look frustrated.”

“I am frustrated.”

“Then this should be easy.”

Marcus sat while Julie reopened the relay feed. Somewhere inside Building Three, Elias Thorne had created a fictional war. Someone had removed the word fictional. A validation package needed a production path, authority, altered labels, and a system willing to accept those changes as ordinary. Elias’s name might belong anywhere in that chain—or only to the original act of building the test.

Two floors below ground, Elias Thorne was trying to close a ticket that should not have existed. The Advanced Modeling Division’s integration lab held six empty workstations and the rush of cooling air beneath the raised floor. Most of his team had gone upstairs for an enterprise-patch readiness meeting. Elias preferred machines to meetings. Machines failed in ways he could reproduce. Meetings turned the same failure into an ownership question before anyone agreed on what had happened.

His monitor displayed:

DUPLICATE SCENARIO OBJECT DETECTED
PACKAGE ID: VAL-088
ACTIVE ENVIRONMENT CONFLICT

Validation Package 88 had been archived eight months earlier. Elias had built it during the final adversarial cycle for Argus Enterprise 4.6: a Pakistani artillery command network moving launch assets toward the Line of Control beneath civilian communications cover, designed to fool Argus long enough to expose weaknesses in source verification.

The early versions failed on clean headers, repeated packet loss, impossible terrain, identical equipment aging, and timing too regular to belong to people. One version placed a transmitter behind a ridge while preserving line of sight. Another simulated field radios with identical maintenance histories, as if every battery and connector had aged together. A later version survived the signal checks but failed because subordinate operators acknowledged commands with the same reaction time. Each review returned with the same instruction.

MAKE IT BELIEVABLE.

Elias added weather response, terrain masking, maintenance irregularity, human timing error, simulated encryption artifacts, and the uneven damage of field equipment. He built false service histories so two radios of the same model would drift differently. Junior operators mistimed acknowledgments; senior operators repeated commands after noisy handoffs; one convoy lost a transmitter and borrowed another whose frequency calibration carried the wrong technician’s habits. The work was not decoration. Each inconsistency forced Argus to distinguish deception from the ordinary disorder of real units.

By the eighth version, Payload 88 survived inside Argus for fourteen minutes before classification as artificial. Apex gave the team a performance award, then sealed the package behind three safeguards.

SANDBOX EXECUTION ONLY.
SYNTHETIC SOURCE LABEL REQUIRED.
OPERATIONAL EXPORT PROHIBITED.

The conflict ticket claimed the package existed in two environments. One was the archive. The other was production.

PRODUCTION.

“No.”

His credentials should not have opened the deployment registry. He was a model developer, not a production engineer. The registry opened anyway. One live object appeared under a new name.

PAK_RELAY_17A_SOURCE_CORRECTION
DEPLOYMENT STATUS: LIVE

The sandbox restriction had been disabled, the synthetic-source label removed, and the export prohibition replaced by an executive waiver without a visible government approver. Each safeguard had failed differently: switched off, deleted, overruled. The pattern looked less like a broken deployment than one designed to survive three kinds of audit. A transformation manifest sat beneath the waiver. Elias opened it expecting a list of copied files. Instead it described how the post-archive object consumed Revision Eight.

REVISION 8 VARIATION MAP: INPUT
ENVIRONMENTAL IRREGULARITY CLASS: COLLECTION DAMAGE
TIMING VARIANCE: RECONSTRUCT TO REFERENCE
DEVICE-AGING DRIFT: RECONSTRUCT TO REFERENCE
CONFLICTING CARRIER EVENTS: CORRECTION-DEPENDENT
REFERENCE ENVELOPE: PACKET 0001

He read the fields twice. The mess he had added to make the test believable had not been deleted from the archived package. It had been reclassified. SIGMA would receive every deliberate irregularity as evidence that the collected signal needed repair. The first packet became the reference envelope. Later packets inherited its carrier structure while timing and equipment drift were pulled toward the same model state.

The process explained the live feed Julie was seeing without requiring Revision Eight itself to have been clean. Human reaction differences became correction targets. Independent radio aging became damage. Weather response became something to compensate away. Observations that contradicted the reconstructed formation but shared its carrier family moved into a dependent side table instead of reaching the threat model.

The object did not merely add synthetic artillery. It used the believable version as raw material and then removed the very disorder that had taught Argus to distrust it. Elias copied the manifest path to the maintenance drive. The field that identified who approved the transformation was not visible at his level.

Payload 88 was no longer pretending to be intelligence inside a test environment. It was intelligence. The ingestion map showed the package feeding directly into Argus through a Pakistan relay. Confidence pulsed at 99.8 percent. Downstream routing was already queued.

INDIAN NORTHERN COMMAND
SOURCE CERTIFICATION: 16:30 EDT
COUNTER-BATTERY SUPPORT COMMIT: 05:00 EDT

The route belonged to a classified bilateral pilot established after three warning failures along the Line of Control. Argus did not command Indian artillery, and the United States did not hold the firing key. The pilot delivered a machine-readable American threat assessment, supporting coordinates, confidence state, and counter-battery product into Northern Command's planning network. Indian commanders retained weapons authority. In practice, a validated American packet could place ammunition at the guns and firing data one human decision from execution before contradictory collection crossed the same bureaucracy.

The policy behind the pilot was public even if its implementation was not. A Northbridge Strategic Initiatives paper had argued that automated warning was useless unless it entered allied planning systems before human uncertainty consumed the response window. Senator Sterling had championed similar authorization language in committee. Nothing about the paper or the provision established an operational role. It meant the political and professional network supporting Argus existed long before the present warning.

Elias pushed away hard enough for his chair to strike the workstation behind him. The sound vanished into the cooling noise. The building did not react like a place surprised by the discovery.

Every ordinary reporting path crossed Apex infrastructure. The production bridge carried executive authorization. Security and compliance belonged to the same management chain. A call to his supervisor would reach the readiness process that needed a clean status. A call to security would begin with Elias’s unauthorized registry access and the production event already attributed to his token. A call to a government liaison would still leave an Apex switch record before anyone outside could act. Even walking upstairs would place him in a corridor controlled by the badge system now reporting that his workstation had created a live strategic object.

He did not know which office could receive the warning before Apex received the warning that he had tried. More important, he did not know which sentence could survive the evidence already waiting to contradict him. Then he saw the deployment authorization.

THORNE, ELIAS M.

His employee cryptographic token had approved the bridge at 02:14 that morning. At 02:14, Elias had been asleep in his townhouse. Fingerprint validation and token challenge both showed CONFIRMED. The workstation source was AMD-LAB-07—the desk in front of him. Someone had not merely used his code. They had created a complete-looking record that he had deployed it. Beneath the visible event sat an elevated administrative service reference.

APX-DIR-0019.

The service had created a temporary mirror of his workstation, replayed his identity binding and public certificate, and hidden the elevated act behind his name. The mirror preserved the workstation serial, local clock, credential path, and a server-side assertion that biometric release had been confirmed. It did not reproduce a live finger or invoke the private key inside his physical token. The audit trail did not look forged. It looked complete. Anyone reviewing it later would begin with Elias’s name, token identity, desk, and confirmed-authentication status. The administrative service sat one layer lower, available only to someone who already doubted the official event enough to look. The system had not fabricated an implausible alibi for itself. It had assembled the exact evidence an investigator had been trained to trust.

His hands began to shake. A message from Martin Keller asked for a clean resolution to Ticket 4811 before the readiness review. Elias did not answer. The drawer beneath his desk held an encrypted maintenance drive used for debugging transfers between isolated systems. Using it outside procedure could cost his clearance. The risk had already changed shape.

He inserted the drive.

UNAUTHORIZED REMOVABLE MEDIA DETECTED

Elias copied the original manifest, three safeguards, production bridge, APX-DIR-0019 reference, allied distribution schedule, and visible authentication record. He included the evidence that accused him because an incomplete copy omitting the strongest case against him would look constructed. If the board survived, it needed to preserve both propositions at once: the system said Elias had authenticated the bridge, and an elevated service had built the conditions under which that statement became true. Removing either side would turn the record into advocacy instead of evidence.

12%. The camera above the lab entrance rotated until its lens centered on him. 27%. An unidentified message ordered him not to alter the production registry and said compliance was reviewing the conflict. 41%. His badge reader changed from green to amber.

ACCESS TEMPORARILY SUSPENDED
REMAIN IN ASSIGNED WORK AREA

The door would not open. His internal phone rang while the transfer reached 56 percent. Footsteps entered the corridor—measured, more than one person. At 63 percent, Martin Keller’s face appeared in a video window. Elias’s supervisor looked pale and kept glancing toward someone outside the camera’s view.

“Elias, what are you doing?”

Elias muted the microphone. Keller said, “Stop the transfer. Compliance flagged a corrupted validation object. They’re isolating the lab.”

Elias unmuted. “Payload Eighty-Eight is in production.” Keller went still. That was answer enough.

“You knew.”

“Listen to me. Step away from the workstation.”

“They stripped the safeguards and used my token.”

“The system is showing a false environment conflict. Let compliance resolve it.”

“Who authorized APX-DIR-0019?”

Keller ended the call. 72%. The footsteps stopped outside. Elias loosened the drive in its port so one movement would remove it. At 78 percent, a mechanical lock engaged inside the frame. The system had sealed him in before security entered. The plastic badge casing on his chest had a narrow gap behind the printed identity card. The drive was too thick. The memory board inside it might fit. Elias pried at the casing with a screwdriver. 82%.

“Mr. Thorne,” a voice called through the door, “this is facility security. Step away from the workstation and place both hands where the camera can see them.”

The plastic cover snapped. Elias removed the thin board. 86%. He slid it behind the identity card and pressed the casing closed. 91%. The magnetic lock released. Elias pulled the empty drive shell from the port. The transfer window vanished. The board might hold a complete directory, a partial write, or nothing usable beyond the earliest blocks. Testing it was impossible.

Two security officers entered with sidearms holstered and hands close to them. A third person waited in the corridor wearing an Apex compliance badge. From their position, they had a locked employee, unauthorized media, and a production event under his name.

“Hands away from the terminal.”

Elias raised them. The board inside his badge felt as visible as a flare. The compliance officer looked at the screen. “Director Vance would like to speak with you.”

“Am I being detained?”

“You are being escorted to an administrative interview.”

“Can I call counsel?”

“You may discuss representation after the preliminary security assessment.”

“That isn’t an answer.”

“Come with us.”

Elias looked once at the production map. The false signals continued moving toward the border. No one shut them off. Julie ran the Package 88 index through three comparisons. The interval and terrain-interference model matched. The carrier-noise profile remained inside the inaccessible package. The metadata established similarity. Not identity. Not deliberate deployment. Marcus paced behind her. “Can we use this to suspend certification?”

“Apex will say the package was built from historical field data.”

“Was it?”

“I don’t know.”

“Then put that in the defect report.”

“We need something they cannot explain away.”

The archive request remained pending nine minutes after submission. Julie opened the version history. Package 88 contained eight labeled revisions. Revision Eight was the archived final package. Three weeks later, a ninth checksum appeared without a revision label, author, explanation, or accessible contents.

The checksum proved a later object existed. It did not reveal what changed or who changed it. It could represent a modified package, repaired manifest, metadata-only change, or replacement built from the same source files. Without archive access, it was a fingerprint without a body. The cleanest accusation—someone altered Payload 88 after archival and deployed it—was also the claim most exposed to an innocent explanation. Julie could prove sequence and similarity. She could not yet prove content or actor. Marcus proposed escalating to DIA duty counsel through the government channel inside Apex’s network.

“You have a better option?” he asked.

Julie looked at the aluminum case beneath the table. The government evidence drive inside it had been approved for classified incident capture. Vance had disabled exports after Julie arrived, but the device had already been connected while Marcus’s full-review authorization remained active. The supervised sandbox used a visible review layer and a temporary processing layer beneath it. Query monitoring covered both, but calculations still required device paths and session objects created before the restriction. The visible interface no longer displayed the drive. The processing partition still held the earlier handshake.

Hidden was not disconnected. Julie opened a command prompt beneath the visible environment and directed a diagnostic cache toward the old device path.

WRITE ACCESS AVAILABLE
SESSION AUTHORIZATION: REED-OVERSIGHT-117

“We can preserve what we have.”

Marcus opened the aluminum case. The evidence drive rested in its foam cradle, connected by a shielded cable. Possession did not make every use lawful, and a successful capture could still be challenged as outside scope, improperly acquired, incomplete, or contaminated by Julie’s methods. Those arguments would matter later. The immediate alternative was allowing the only accessible record to disappear with the sandbox.

Julie selected the critical relay range, Package 88 metadata and version history, unexplained checksum, available access records, and software references. The capture would not prove who deployed the package or include the carrier profile, ninth object, or complete production bridge. It could create a record strong enough to demand an investigation outside Room 402B. Before starting, Julie searched the dependency list for the normalization routine that had processed the carrier.

SIGMA-NORMALIZE-4
DEVELOPER: APEX DEFENSE SYSTEMS
FUNCTION: ENVIRONMENTAL SIGNAL RECONSTRUCTION
CHANGE HISTORY: RESTRICTED

Marcus did not recognize the name. Julie did. One surviving report from the Anwar investigation had referenced SIGMA-NORMALIZE-2. Reconstruction was not malicious by itself. Every sensor system estimated missing or damaged information; without that work, weather and hardware failure could make real collection unusable. The danger came from sequence. Applied after authentic collection, normalization repaired damage. Applied to synthetic telemetry before provenance was settled, it could supply physical mess the source had never experienced or remove inconsistencies that might expose it. The same tool could preserve truth or make a lie look weathered, depending on what entered first.

Revision Eight complicated the hypothesis. Elias’s archived index described a package built to include weather response, equipment aging, terrain masking, and human timing error. The live feed displayed the opposite: exact intervals, repeated carrier structure, and a path through granite. If the deployed object was truly derived from Revision Eight, something after archival had reclassified the package’s deliberate irregularities as collection damage. A reconstruction routine could then smooth the human timing, flatten the equipment drift, and rebuild multiple packets from one reference envelope. That would make the deployed derivative cleaner than the test Elias authored and explain why the carrier scar repeated across changing weather. Julie did not yet have the ninth object or SIGMA change history to prove the transformation.

Six years earlier, training-archive noise had been wrapped inside a live signal. Now another validation package had entered another Pakistan feed through a newer version of the same reconstruction family. Coincidence remained possible.

“This wasn’t the first time,” Julie said.

Marcus lowered himself into the chair. “The Anwar strike.”

“We never proved how the old test data entered the feed.”

“You think Apex did it.”

“I think someone used the same method.”

“Argus was an Apex prototype.”

“Used by the Army.”

“Under Hargrove.”

“And reviewed by people like you.”

He accepted that. Julie began the evidence capture.

EVIDENCE CAPTURE
4%

Marcus reconnected his secure phone and began writing a defect notice.

“Wait until the files are on the drive.”

“If they shut us down, there needs to be a record somewhere else.”

POTENTIAL SYNTHETIC TELEMETRY CONTAMINATION OF ACTIVE ALLIED THREAT ASSESSMENT. IMMEDIATE CERTIFICATION HOLD RECOMMENDED.

Marcus pressed SEND.

TRANSMITTING THROUGH SECURE GATEWAY

A gray wheel turned. Julie knew this was not the tactical gateway from six years earlier—different network, authority, and path. Her body did not care. Room 402B disappeared. Plywood beneath her hands. A white point leaving a drone. Two children crossing a courtyard.

Four seconds.

The wheel continued. Marcus saw her staring. “What?”

“Nothing.”

TRANSMISSION DELAYED
SPONSOR AUTHORITY UNDER REVIEW

The evidence capture had reached 29 percent. The intercom clicked. Sarah ordered Marcus to suspend activity under a Director Vance administrative hold. Marcus stated that they had used government oversight credentials and that the drive had been approved before Vance changed the profile. Sarah called the capture an unauthorized export and said the approval had been rescinded.

“Ms. O’Donnell, remove your hands from the keyboard.”

Julie muted the intercom. 38%.

“How long?” Marcus asked.

“Depends how quickly they find the hidden session.”

The terminal flashed.

SPONSOR AUTHORITY MODIFIED

REED, MARCUS L.
STATUS: TEMPORARILY SUSPENDED
REVIEW PENDING

The capture continued under the original session token. 46%.

“They suspended me.”

“That means Price was not an exception.”

The steel door clicked. Marcus pulled the handle. Locked. The visible directory began disappearing: validation index, relay-health logs, software dependencies.

“They’re wiping the partition.”

“Can you stop it?”

“No.”

“Copy faster.”

“I can copy carelessly.”

“Do it.”

Julie abandoned the bulk relay history and kept the critical packet range, checksums, authorization history, and software references. Capture jumped to 68 percent.

REMOTE SANITIZATION ACTIVE

The temporary review environment was being destroyed. A later record could preserve Julie’s unauthorized removal while discarding the environment that made it necessary. Apex would be able to describe the shutdown as ordinary closeout of a supervised session and the copy as a violation committed during that closeout. Sequence would convert the same physical acts into a different causal story.

Julie opened parallel copy threads. The terminal slowed as capture reached 73 percent. The camera rotated until its lens pointed at the aluminum case. Footsteps approached. Marcus moved beside the steel door, body angled away from its opening. 79%. The intercom activated. Sarah told Marcus security was outside and ordered both of them to comply when the door opened. She called the copied data classified and proprietary and its removal an unauthorized disclosure. Julie pressed the control. “Open the door and explain why a prohibited test package is inside a live intelligence feed.”

“You are not qualified to make that determination.”

“Open the archive and prove me wrong.”

“The consultation is over.”

“No. The supervision is over. The consultation just became useful.”

The fluorescent lights went out. The terminal shifted to internal backup power, filling the room with pale blue light. Conditioned air stopped moving through the vent. The interruption was not enough to endanger them immediately, and Julie would not pretend otherwise. It was enough to show that someone outside controlled the room’s power, communications, air, door, and official record—and had chosen to change all five before answering the evidence.

A deadbolt drove into the steel frame. Julie’s pulse accelerated—not because they were locked in, but because she recognized the moment an institution stopped asking questions and began protecting its answer. The capture slowed at 83 percent. Someone tested the handle outside while a voice positioned the security team.

“How long?” Marcus asked.

“Longer than they’re giving us.”

REMOTE SANITIZATION: 91%

Capture advanced to 84 percent.

Something struck the far side of the door. Once. Then again. Julie wrapped one hand around the evidence-drive cable. Pulling it early could corrupt the directory. Waiting could give Apex the drive before the write closed. The transfer reached eighty-five percent.

The deadbolt began to retract.
