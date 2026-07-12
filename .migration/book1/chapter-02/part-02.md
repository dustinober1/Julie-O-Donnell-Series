eared.

ELIAS, DO NOT ALTER THE PRODUCTION REGISTRY.
COMPLIANCE IS REVIEWING THE CONFLICT.

He did not recognize the sender.

No name. No department.

41%.

His badge reader chirped behind him.

Elias turned.

The light beside the lab door had changed from green to amber.

He stood and crossed the room.

The door did not open.

His badge vibrated against the reader.

ACCESS TEMPORARILY SUSPENDED
REMAIN IN ASSIGNED WORK AREA

He backed away.

His phone rang on the desk.

Not his mobile. The internal line.

Elias let it ring.

56%.

Footsteps sounded in the corridor outside.

Measured. More than one person.

He returned to the workstation and opened a second window, trying to accelerate the transfer.

The system rejected the request.

63%.

The internal phone stopped ringing.

A moment later, his supervisor’s face appeared in a video-call window.

Martin Keller looked pale.

“Elias, what are you doing?”

Elias muted the microphone.

Keller’s eyes moved away from the camera as if someone stood beside him.

“Stop the transfer,” he said. “Compliance flagged a corrupted validation object. They’re isolating the lab.”

Elias unmuted the call.

“Payload Eighty-Eight is in production.”

Keller’s face went still.

That was answer enough.

“You knew,” Elias said.

“Listen to me. Do not touch anything else.”

“You knew.”

“The system is showing a false environment conflict. We need to let compliance resolve it.”

“They stripped the sandbox headers.”

“Elias—”

“They used my token.”

Keller glanced aside again.

“Step away from the workstation.”

“Who authorized APX-DIR-0019?”

Keller ended the call.

72%.

The footsteps stopped outside the lab.

A radio crackled beyond the door.

Elias pulled the drive slightly loose in the port. The transfer continued, but he would be able to remove it with one movement.

78%.

The door reader flashed red.

A heavy mechanical lock engaged inside the frame.

The system had sealed him in before whoever stood outside entered.

Elias looked at the empty badge casing clipped to his belt.

The plastic shell had a narrow gap behind the printed identity card. Enough space for the maintenance drive if he removed its outer cover.

He grabbed a screwdriver from the desk and pried at the drive’s casing.

82%.

A voice came through the door.

“Mr. Thorne, this is facility security. Step away from the workstation and place both hands where the camera can see them.”

Elias kept working.

The plastic cover snapped.

He removed the thin memory board inside.

86%.

“Mr. Thorne, acknowledge.”

Elias slid the memory board behind his identity card.

The badge bulged slightly.

He pressed the casing closed.

91%.

A buzzer sounded.

The magnetic lock released.

Elias grabbed the drive from the port.

The transfer window vanished.

He did not know whether the final files had written cleanly.

The door opened.

Two security officers entered.

Their sidearms remained holstered, but their hands were positioned close to them. A third person waited in the corridor wearing an Apex compliance badge.

“Hands away from the terminal,” the lead officer said.

Elias raised them.

His badge hung against his chest.

The thin circuit board inside it felt as visible as a flare.

The compliance officer looked at the screen, then at Elias.

“Director Vance would like to speak with you.”

Elias swallowed.

“Am I being detained?”

“You are being escorted to an administrative interview.”

“Can I call counsel?”

“You may discuss representation after the preliminary security assessment.”

“That isn’t an answer.”

The officer stepped closer.

“Come with us.”

Elias looked once at the production map.

The false signals continued moving toward the border.

No one shut them off.

Julie ran the index metadata through three additional comparisons.

The first linked Validation Package 88 to the same packet interval as the Pakistan relay feed.

The second showed that both used an identical model for compensating terrain interference.

The third required information she did not yet have.

She needed the carrier-noise profile stored inside the validation package itself.

The metadata was enough to establish similarity.

Not identity.

Not deliberate deployment.

Not yet.

Marcus paced behind her.

“Can we use the index record to suspend certification?”

“Apex will say Package Eighty-Eight was built from historical field data, which explains the similarities.”

“Was it?”

“I don’t know.”

“Then put that in the defect report.”

“And watch it disappear into the same system that suspended Price?”

“We need something on record.”

“We need something they can’t explain away.”

The access-request timer remained on the screen.

PENDING CONTRACTOR APPROVAL: 09:14

Nine minutes without an answer.

Julie opened the package’s version history.

The file contents were restricted, but each archived revision included a checksum—a long cryptographic fingerprint used to verify that a file had not changed.

Payload 88 had eight revisions.

Julie compared their checksum dates against the development index.

Revision Eight was the final archived package.

A ninth checksum appeared three weeks later.

No revision label.

No listed author.

No explanation.

“Someone modified it after archiving,” she said.

Marcus stopped pacing.

“What changed?”

“The index doesn’t say.”

“Can you retrieve the ninth version?”

“Not without access.”

Marcus moved to the terminal and opened the sponsorship-control screen.

“I can escalate.”

“To whom?”

“DIA duty counsel.”

“Through Apex’s network.”

“It’s still a government channel.”

“Inside an Apex building, on an Apex terminal, connected through an Apex-managed gateway.”

“You have a better option?”

Julie looked at the government evidence drive sealed inside the aluminum case Marcus had placed beneath the table.

It was approved for classified incident capture. It could store the index, the relay data, and any logs Julie could reach.

Under her original access profile, the drive would have been permitted.

Vance had disabled exports after she arrived.

“Maybe.”

She opened the system diagnostics.

The supervised sandbox consisted of two layers. The visible environment held the files Apex had approved for review. Beneath it, a temporary processing partition performed calculations before returning results to the visible screen.

Query monitoring tracked activity in both layers.

But the evidence drive had been connected to the terminal before Julie entered the room, when Marcus’s full-review authorization was still active. The system had recognized it, assigned it a device path, and then hidden the path when Vance revoked export privileges.

Hidden was not the same as disconnected.

Julie opened a command prompt inside the processing partition.

Marcus watched her.

“What are you doing?”

“Creating a comparison cache.”

“Is that permitted?”

“No one has told me it isn’t.”

“That is not the same as yes.”

“Now you’re learning.”

She created a temporary diagnostic file and directed it toward the hidden evidence-drive path.

The command returned:

WRITE ACCESS AVAILABLE
SESSION AUTHORIZATION: REED-OVERSIGHT-117

Vance had changed the visible permissions.

He had not fully revoked the device handshake established under Marcus’s earlier authority.

Julie felt the first small opening in the walls around them.

“We can preserve what we have.”

Marcus pulled the aluminum case onto the table and opened it.

Inside, the evidence drive sat in a foam cradle, already connected to the terminal through a shielded cable.

“How much?”

“The relay feed, Package Eighty-Eight’s index history, the unexplained ninth checksum, and the access logs.”

“That proves manipulation?”

“It proves enough to demand a real investigation.”

“And the connection to six years ago?”

Julie did not answer immediately.

She returned to the carrier-noise sequence and searched the operational system for the name of the normalization routine that had processed it.

The routine appeared in a software dependency record.

SIGMA-NORMALIZE-4

The name meant nothing to Marcus.

Julie remembered it.

Six years earlier, during the investigation into the Anwar strike, one of the surviving routing reports had referenced an earlier version:

SIGMA-NORMALIZE-2.

The routine was designed to smooth degraded signals before Argus evaluated them. In principle, it prevented weather noise from lowering confidence in a legitimate intercept.

In practice, it could make artificial data appear to have survived environmental interference.

Julie’s hand stopped above the keyboard.

“Julie?”

She opened the dependency record.

SIGMA-NORMALIZE-4
DEVELOPER: APEX DEFENSE SYSTEMS
FUNCTION: ENVIRONMENTAL SIGNAL RECONSTRUCTION
CHANGE HISTORY: RESTRICTED

Marcus read the name.

“What is it?”

“The original Pakistan feed passed through an earlier version of this routine.”

“You’re sure?”

“I read the routing report.”

“Could be standard software.”

“It could.”

“But you don’t think so.”

Julie looked at the smooth line marching across the relay-health graph.

Six years ago, the carrier noise had been generated in a training archive and wrapped inside a live signal.

Now another training package had appeared inside another Pakistan feed, processed by a newer version of the same normalization system.

Coincidence remained possible.

The word felt increasingly dishonest.

“This wasn’t the first time,” she said.

Marcus lowered himself into the chair beside her.

The admission seemed to take weight from his body rather than add it.

“The Anwar strike.”

“We never proved how the test data entered the feed.”

“You think it came through Apex.”

“I think someone used the same method.”

Marcus looked toward the camera.

“If they did this six years ago—”

“We do not know who did it.”

“Argus was an Apex prototype.”

“Used by the Army.”

“Under Hargrove.”

“And reviewed by people like you.”

He accepted that.

Julie began the export.

The progress window appeared inside the hidden processing layer.

EVIDENCE CAPTURE
4%

Marcus reconnected his secure phone to the government network.

“I’m sending the defect notice now.”

“Wait until the files are on the drive.”

“If they shut us down, there needs to be a record somewhere else.”

He began composing the report.

Julie watched the transfer.

11%.

She selected the relay feed and Package 88 metadata.

A warning appeared in the corner of the screen.

PROCESSING LOAD EXCEEDS SANDBOX PARAMETERS

She dismissed it.

18%.

Marcus entered the key conclusion:

POTENTIAL SYNTHETIC TELEMETRY CONTAMINATION OF ACTIVE ALLIED THREAT ASSESSMENT. IMMEDIATE CERTIFICATION HOLD RECOMMENDED.

He pressed SEND.

The phone displayed:

TRANSMITTING THROUGH SECURE GATEWAY

A gray wheel began to turn.

Julie looked at it.

For an instant, the room disappeared.

She saw a plywood table beneath her hands. A white point separating from a drone. Two children crossing a courtyard.

Four seconds.

The wheel continued turning.

Marcus noticed her staring.

“What?”

“Nothing.”

The message status changed.

TRANSMISSION DELAYED
SPONSOR AUTHORITY UNDER REVIEW

Marcus stood.

“What the hell?”

Julie looked at her export.

29%.

The intercom clicked.

Sarah spoke.

“Colonel Reed, suspend all activity and step away from the terminal.”

Marcus pressed the control.

“On whose authority?”

“Director Vance has placed the consultation on administrative hold.”

“For what reason?”

“Your review has entered proprietary development environments outside the authorized scope.”

“We accessed index metadata using government oversight credentials.”

“You initiated an unauthorized export.”

“The device was approved before your office altered the access profile.”

“That approval has been rescinded.”

Julie continued typing.

Sarah’s voice sharpened.

“Ms. O’Donnell, remove your hands from the keyboard.”

Julie muted the intercom.

38%.

Marcus stared at her.

“How long?”

“Depends how quickly they find the hidden session.”

The terminal flashed.

SPONSOR AUTHORITY MODIFIED

Marcus’s name changed from blue to amber.

REED, MARCUS L.
STATUS: TEMPORARILY SUSPENDED
REVIEW PENDING

The evidence transfer continued under the original session token.

46%.

“They suspended me,” Marcus said.

“That means Price wasn’t an exception.”

The steel door gave a soft mechanical click.

Marcus crossed the room and pulled the handle.

It did not move.

“They locked it.”

Julie kept working.

55%.

The visible file directory began disappearing.

First the validation index.

Then the relay-health logs.

Then the software-dependency record.

“They’re wiping the partition,” she said.

“Can you stop them?”

“No.”

“Can you copy faster?”

“I can copy carelessly.”

“Do it.”

Julie abandoned the full relay file and selected only the critical packet range, checksums, authorization history, and software references.

The estimated transfer size fell.

The progress jumped to sixty-eight percent.

A new process appeared in the system monitor.

REMOTE SANITIZATION ACTIVE

The files were not simply vanishing from view.

The temporary review environment was being destroyed.

Julie opened parallel copy threads.

The terminal slowed.

73%.

The camera above them rotated.

Its lens adjusted until it pointed directly at the evidence-drive case.

“They know where it’s going,” Marcus said.

“I assumed they would.”

“Then why are they waiting?”

“They aren’t.”

Footsteps sounded beyond the door.

More than one person.

Marcus moved away from the terminal and positioned himself beside the steel frame.

“You expecting to fight facility security?”

“I’m expecting them to open the door.”

“And then?”

“I’m working on that.”

Julie looked at the transfer.

79%.

The intercom came alive without warning.

“Colonel Reed,” Sarah said, “security personnel are outside the room. When the door opens, you will keep your hands visible and comply with their instructions.”

Marcus did not answer.

“Ms. O’Donnell, the data on that device is classified and proprietary. Removing it constitutes an unauthorized disclosure.”

Julie pressed the intercom button.

“Then open the door and explain why a prohibited test package is inside a live intelligence feed.”

A pause.

“You are not qualified to make that determination.”

“Open the archive and prove me wrong.”

“The consultation is over.”

“No,” Julie said. “The supervision is over. The consultation just became useful.”

The overhead fluorescent lights went out.

The room fell into darkness.

A second later, the terminal switched to internal backup power, bathing Julie and Marcus in pale blue light.

The transfer remained active.

82%.

Marcus looked toward the ventilation grille.

The low hiss of conditioned air had stopped.

“They killed the room systems.”

“They isolated the sector.”

A heavy deadbolt drove into the steel door with a hard mechanical crack.

Julie’s pulse accelerated.

Not because they were locked in.

Because she had heard that sound before—not in a building, but inside a decision. The instant an institution stopped asking questions and began protecting its answer.

The transfer slowed.

83%.

Beyond the door, someone tested the handle.

A muffled voice ordered the security team into position.

Marcus turned toward Julie.

“How long?”

She watched the progress bar move one fraction at a time.

“Longer than they’re going to give us.”

The terminal flickered.

REMOTE SANITIZATION: 91%

The transfer advanced.

84%.

Something struck the far side of the door.

Once.

Then again.

Julie wrapped one hand around the evidence drive’s cable.

If she pulled it too early, they would lose the final write sequence and possibly corrupt everything.

If she waited, Apex would open the room and take it.

The transfer reached eighty-five percent.

The deadbolt began to retract.
