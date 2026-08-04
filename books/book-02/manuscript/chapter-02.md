<!--
Migration provenance
Drive title: chapter-02
Drive file ID: 1UTI-4gTG7mqJ7F-sqOZqDpchhWQuQADm_cqWCLalmvY
Drive parent: 02_BOOK 2/01_Manuscript
Drive modified: 2026-07-26T01:56:27.187Z
Imported: 2026-08-04
Import method: Google Drive MCP read_file_content text representation
Authority: DRAFT COMPLETE — PENDING FORMAL ACCEPTANCE. Not yet Book 2 canon.
Normalization: line endings, Google-export escape sequences, and paragraph spacing only; no prose was altered
-->

# Chapter 2 — The Missing Architect

At three o’clock, the scientist’s daughter placed her phone face down on the conference table and kept two fingers resting across the case.

The gesture settled the first question before anyone asked it.

The room belonged to family counsel, not the commission. Frosted glass shut out the corridor. A carafe of water, four untouched glasses, and a yellow legal pad had been arranged with the careful neutrality of a place where every sentence might later acquire an exhibit number. Deepa Dhaliwal sat at the daughter’s left. The scientist’s former spouse occupied the chair nearest the door. Julie took the opposite side of the table, leaving the empty seat beside her for counsel.

Her right wrist was still locked in the brace. She set her notebook square to her left hand and slid the pen out with her thumb rather than reaching across the table.

Counsel started the recorder only after the daughter nodded.

“This is a voluntary interview,” Dhaliwal said. “You can decline any question. You can end the interview at any time. Nothing on your phone will be viewed, copied, searched, or retained today unless you give specific consent through counsel.”

“And nobody is taking it,” the daughter said.

“Nobody is taking it,” Dhaliwal confirmed.

The daughter looked at Julie. “You’re the American analyst.”

“I’m attending under Superintendent Dhaliwal’s authority. I don’t have search, seizure, or compulsory interview powers here.”

“That wasn’t my question.”

“No,” Julie said. “It was the part of the answer that matters before you decide whether to talk to me.”

Counsel’s expression changed by a fraction. Approval, or at least the suspension of an objection.

The daughter’s fingers remained on the phone. “The commission shut my mother out, and now people from the same country want to search the things she left with me.”

“I’m not asking to search them.”

“Not yet.”

Julie wrote SOURCE CONTROLS ACCESS at the top of the page. Beneath it, she added: behavior, last contact, ordinary preparations. She turned the notebook so the words could be read across the table.

“These are the areas I’m asking about. What she did before she left. What contact you had. What she normally did when she expected to be unavailable. You can stop me if a question moves outside them.”

“And the work records?”

“Only what you choose to describe today. The underlying material stays where its lawful custodian put it.”

The former spouse leaned forward. “You keep saying lawful. Does that mean you think what she copied was unlawful?”

“It means I don’t know the authority under which each copy was made. I won’t turn that uncertainty into an accusation.”

The daughter glanced toward counsel, then back to Julie. “She copied records after they took her out of the room. She said the people writing the correction had never seen the original failure.”

“What kind of records?”

“No.” The daughter’s answer was immediate. “That is exactly how this starts. A category becomes a folder, then everything. The same goes for a saved map.”

Julie drew a line through the question. “Then we stay with conduct.”

For twenty minutes, every answer came with conditions. The scientist had missed calls before, but rarely without sending a time window. She had worked through meals, slept in secure offices, and once gone forty-eight hours without contacting anyone during a platform incident. She had also arranged someone to feed the cat on that occasion and had told her daughter not to expect a response. This time, the cat had been left with extra food, no message had been sent to the former spouse, and a scheduled medical appointment had passed without cancellation.

None of it proved compulsion. Taken together, it narrowed the shape of an ordinary departure.

At 15:34, Julie asked, “When did you first believe this was different?”

The daughter’s hand tightened over the phone.

“The last call,” she said. “She made it sound normal.”

“What made you think it wasn’t?”

The daughter looked at counsel before answering. “Because my mother never had to work that hard to sound ordinary.”

* * *

At 15:12, the scientist opened a dependency register she had helped design and found three fields missing from the version on the screen.

The omissions were deliberate.

The terminal sat on a metal desk bolted to the floor. Two monitors showed legitimate platform documentation: service boundaries, build histories, interface specifications, and a partial record of fallback dependencies. The files were real enough to be dangerous. They had been selected by someone who understood that fabricated material would slow her down and genuine material would make refusal harder to defend.

A guard stood inside the door. Another person, dressed in a dark shirt without insignia, watched from behind the scientist’s right shoulder.

“The continuity review ended,” she said.

The person behind her did not answer.

“You told me this was to preserve operation during an authorized transfer. That explanation no longer fits what you’re asking me to produce.”

A printed task sheet lay beside the keyboard. It requested a portable dependency model: the minimum services, trust relationships, update channels, and recovery assumptions needed to reproduce the platform’s behavior outside its current environment.

The word portable had been underlined.

“We need the model,” the person said.

“For what target environment?”

“You have the materials.”

“That isn’t an environment.”

“Build from the stated assumptions.”

“The stated assumptions omit identity controls, hardware roots, and jurisdictional access. Any output would be misleading.”

“Then mark the gaps.”

The instruction was almost reasonable. That made it worse.

She looked again at the source register. The absent fields normally tied each dependency to an authority boundary, an accountable owner, and a failure consequence. Without them, a reader could mistake technical reachability for permission and recoverability for control.

She moved her hands away from the keyboard. “Who will validate the model?”

“You will.”

“I can validate internal consistency. I can’t validate a deployment I’m not allowed to see.”

The guard shifted weight. The movement brought a soft scrape of rubber against concrete. No threat was spoken. None was required.

The scientist pulled the keyboard closer.

She could refuse and learn nothing. She could cooperate without limits and give them a transfer map dressed as engineering documentation. The remaining choice was narrower: produce only what the verified records supported, preserve every uncertainty, and make later alteration difficult to hide.

She opened a clean model.

The first line identified the source-document versions. The second established a dependency identifier that could not be reused across domains. She added a field for provenance status, another for validation authority, and a third for assumptions that had not been tested. Where the supplied records skipped an owner, she entered OWNER NOT ESTABLISHED rather than infer one. Where an interface required a credential, she described the class of credential but excluded values, issuance paths, and live endpoints.

The person behind her said, “You’re adding fields.”

“They are required to make the output accurate.”

“They weren’t requested.”

“Then you requested an artifact that could not be validated.”

Silence held for several seconds.

“Continue.”

She did. Every completed row carried a source version, a confidence boundary, and a checksum derived from the materials they had provided. The checksums were ordinary engineering hygiene. So were the explicit unknowns. Neither would prevent misuse, but together they would leave seams if someone stripped away the limits and presented the result as complete.

At 15:31, a new document appeared in the shared workspace. MIGRATION ASSUMPTIONS.

She did not open it.

“What system receives this model?” she asked.

“No questions about the receiving environment.”

“Then I cannot certify portability.”

“You are not being asked to certify it.”

The distinction told her more than an answer would have. They did not need her judgment attached to the model. They needed the structure of her knowledge separated from the institution that had governed it.

She resumed typing, slower now.

The person behind her stepped closer. “How long?”

“For a bounded dependency model, several hours. For the thing described on that sheet, longer.”

“What is the difference?”

“A bounded model tells you what the records establish. Your sheet asks what could be made to work.”

“And?”

“That requires choices about risk, authority, and acceptable failure. Those choices are not in the documents.”

“They are not your concern.”

“They become my concern when you ask me to encode them as technical necessity.”

The guard moved again. This time a hand touched the back of her chair, steadying it or claiming it.

The scientist kept her eyes on the screen. She created a new section titled UNRESOLVED DECISIONS and entered the first item: Receiving authority not identified. The second: External access conditions not established. The third: Failure ownership not assigned.

The person behind her read each line as it appeared.

“Remove that section.”

“Then the model will state conclusions the source material does not support.”

“Remove it.”

She selected the section. Her finger rested above the key.

A refusal might preserve the page and end her ability to mark the work. Compliance might preserve her access long enough to leave other boundaries. She deleted the heading, then inserted the same limits into the affected dependency rows, where they looked like technical qualifications rather than a challenge.

The person behind her missed none of it but allowed the entries to remain.

At 15:47, the guard directed her away from the desk. The model stayed open on the monitor, incomplete and traceable to the exact records they had chosen.

She had given them less than they wanted and more than she could take back.

* * *

At 15:35, Julie drew four columns across a fresh page.

VOLUNTARY TRAVEL. PROTECTED LEAVE. FAMILY WITHDRAWAL. EMERGENCY WORK.

The daughter watched her write. “You’re trying to prove she left.”

“I’m testing the ordinary explanations first.”

“Why?”

“Because if one of them accounts for the evidence, we need to know before anyone builds a more serious claim on top of the gap.”

The former spouse exhaled through the nose. “She could disappear when she wanted to.”

“Disappear from work, or from you?”

“Both. Usually not at the same time.”

Julie asked for examples, then separated each answer by source. The former spouse described conferences extended without warning, a hotel change made after a security concern, and one week spent alone after a public dispute with the commission. The daughter described a different pattern: her mother might conceal where she was working, but she always left a practical boundary. Feed the cat. Cancel dinner. Do not call before Thursday. Use the landline if the building loses power.

The family conflict complicated the picture. Three days before the transfer claim, mother and daughter had argued about the copied records. The daughter had called them insurance. The scientist had called them context. Neither had agreed on whether keeping them protected the work or put the family at risk.

“Did she say she planned to release anything?” Julie asked.

“No.”

“Did she identify anyone she intended to meet?”

“No.”

“Did she say she was leaving Canada?”

“No.”

Each answer narrowed the family’s knowledge, not the world.

Dhaliwal passed Julie a single-page liaison return. Two authorized repositories had been checked again under the same bounded window. No acceptance record had been found. The result did not expand the search and did not convert absence into universal non-receipt.

Julie initialed the time she received the page and left it with Dhaliwal.

At 15:58, counsel permitted a review of the daughter’s handwritten list of missed obligations. Julie did not touch the original. Counsel held it flat while she read: medical appointment, veterinary refill, a scheduled call with a retired colleague, building access renewal, automatic grocery delivery. Three items had independent timestamps. Two rested only on family memory.

“May we request certified confirmation for the timed items?” Julie asked.

“Through me,” counsel said.

“Through you.”

The daughter folded her arms. “She could have left all of that behind on purpose.”

“Yes.”

“You say that like it doesn’t matter.”

“It matters because it stays possible.”

The answer landed badly. Julie let the silence stand instead of softening it into something false.

The former spouse broke it. “She took work when she wanted distance. She took a toothbrush when she expected a night away. She took the blue charger because the others overheated.”

“Was the charger gone?” Julie asked.

“No. It was beside the bed.”

The daughter stared at the table.

Julie wrote: ordinary preparation item reportedly left; source—former spouse; confirmation pending. The fact added weight. It did not choose a cause.

At 16:17, Dhaliwal asked counsel whether the family would authorize a premises inventory limited to ordinary travel indicators. Counsel declined pending written scope. The refusal was recorded without argument.

Julie returned to the last contact. “You said the final call sounded normal because she was trying to make it sound normal. What did she discuss?”

The daughter’s fingers moved once across the phone case. “Nothing that helps you.”

“What made the effort visible?”

“She used my full name.”

The former spouse looked up.

Julie asked, “Was that unusual?”

“When she was angry, yes. When she was frightened, she shortened everything. Names. Sentences. Plans.” The daughter swallowed. “She was careful on the call. Too careful.”

“Did she ask you to do anything?”

“I’m not discussing the message.”

“Was it a live call or a recording?”

Counsel raised a hand. “That moves toward content.”

Julie stopped. “Understood.”

The daughter looked from counsel to Dhaliwal. “There is a voicemail. It came after the call.”

No one reached for the phone.

Julie asked only, “Is it still on the device?”

“Yes.”

“Has anyone else accessed it?”

“My lawyer listened with me. Nobody copied it.”

Counsel confirmed the statement.

Dhaliwal closed the liaison return. “That changes the preservation question.”

“It doesn’t change who owns the phone,” the daughter said.

“No,” Julie said. “It changes what we need to protect without taking it from you.”

* * *

At 16:35, Julie placed one sheet of paper in the center of the table.

She had written the proposed acquisition limits by hand because opening a government laptop would have changed the temperature in the room. Her wrist ached from holding the pen, so she rested the brace against the table edge while Dhaliwal read the terms aloud.

The device would remain with the daughter. Any acquisition would occur at a neutral Canadian facility the next morning. Consent would be item-specific and revocable until each selected copy was complete. The authorized scope would cover the disclosed voicemail, any consent-selected map artifact directly associated with the relevant period, and the minimum authentication metadata required to establish source, sequence, and integrity. No unrelated messages, photographs, applications, location history, or account content could be searched.

A Canadian examiner would perform the work. The source would remain visible to the daughter or counsel. Each copied item would be hashed at acquisition. Identical manifests would go to the source holder and the investigative team. The American side could receive only the authorized derivative, through the Canadian channel, with the restriction recorded.

Counsel tapped the phrase directly associated. “Who decides that?”

“The source identifies the item,” Julie said. “The examiner confirms the technical relationship. If there is disagreement, acquisition stops.”

“And deleted material?”

“Outside scope.”

“Cloud backups?”

“Outside scope unless separately offered and separately authorized.”

The daughter studied the page. “What if the voicemail makes her look guilty?”

“It may support more than one interpretation.”

“That isn’t an answer.”

“It’s the only honest one. A copy can establish what was said, when the system records it, and whether the file remained unchanged after receipt. It cannot decide why she said it, whether she spoke freely, or what happened afterward.”

“And the maps?”

“The same limit. A saved place can show interest or preparation. It does not prove travel, destination, or custody.”

The daughter’s jaw tightened. “The commission already treated her preservation choices like misconduct.”

Julie glanced at Dhaliwal before continuing. “Then the scope needs to protect the distinction between preserving a record and proving an act. Your conditions become part of the acquisition record. So do ours.”

“Your people still get a copy.”

“Only if Canada lawfully provides the bounded derivative. I don’t take the phone. I don’t direct the examiner. I don’t widen the search.”

Dhaliwal added, “And any later request comes back through my office and counsel. It does not attach itself to tomorrow’s consent.”

The former spouse read the page twice. “Can she stop after the voicemail?”

“Yes,” counsel said. “If that is how the authorization is written.”

The daughter turned the phone over. Its dark screen reflected the ceiling lights, four pale rectangles without depth.

For the first time, she moved her hand away from it.

“I’ll bring it,” she said. “The voicemail first. Then I decide about anything else.”

Counsel marked two changes, and Dhaliwal initialed them. The proposed session was set for 09:00 the following morning, subject to the daughter’s signed authorization at the facility.

At 17:10, the recorder was stopped.

The daughter slipped the phone into her bag and closed the zipper before she stood. “It stays with me tonight.”

“Yes,” Julie said.

The phone left the room in its owner’s custody. What followed would begin with permission, not possession.
