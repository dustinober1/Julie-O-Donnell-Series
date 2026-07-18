#!/usr/bin/env python3
"""Add the final measured layer of consequence needed for Book 1 target length."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "books/book-01/manuscript/chapters"


def add_before(text: str, anchor: str, addition: str, marker: str) -> str:
    if marker in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"missing anchor: {marker}")
    return text.replace(anchor, addition + anchor, 1)


def add_after(text: str, anchor: str, addition: str, marker: str) -> str:
    if marker in text:
        return text
    if anchor not in text:
        raise RuntimeError(f"missing anchor: {marker}")
    return text.replace(anchor, anchor + addition, 1)


def revise_15(text: str) -> str:
    anchor = """The record no longer depended on Marcus remaining conscious.

At 08:03, the medical team moved him toward the ramp."""
    addition = """The record no longer depended on Marcus remaining conscious.

Brooks ordered the three detainees transported separately and the evidence vehicle routed by a fourth path. She gave the ambulance teams no case theory, only the restraint, medical, and security conditions each needed. Marcus was an injured detainee under oxygen, not the custodian once the receipts closed. Elias was a represented employee claiming voluntary participation, not a hostage because Apex had used the word. Julie was an injured former officer under arrest, not the technical authority for the evidence after MPD accepted it.

The distinctions changed how every later person would meet them. No paramedic would be asked to guard the case. No patrol officer would decide whether Elias was free by interpreting his fear. No hospital room would hold one subject beside the objects another agency wanted him to explain.

Park copied the destination hospitals onto a sealed transport sheet and withheld them from the open dispatch channel until the ambulances entered controlled routes. The measure did not hide the detainees from lawful custody. It kept the Apex pursuit network and public lookout from becoming a map to three medical rooms before MPD had secured them.

Ortiz signed the separation plan beneath Brooks. Two names now owned the choice.

At 08:03, the medical team moved Marcus toward the ramp."""
    return text.replace(anchor, addition, 1) if "Brooks ordered the three detainees transported separately" not in text else text


def revise_16(text: str) -> str:
    anchor = """Marcus had reached the trauma unit. His oxygen saturation had improved but remained low. Imaging of his ribs, chest, scalp, thigh, and head was pending. Elias was in guarded observation for the hip injury, dizziness, cold exposure, exhaustion, and the cut on the finger used for his live biometric acts.

Alvarez stated that no substantive interview would occur that day."""
    addition = """Marcus had reached the trauma unit. His oxygen saturation had improved but remained low. Imaging of his ribs, chest, scalp, thigh, and head was pending. Elias was in guarded observation for the hip injury, dizziness, cold exposure, exhaustion, and the cut on the finger used for his live biometric acts.

Two agencies had already sent interview requests to the hospitals. Army investigators wanted Marcus's account of credential loss and removal of classified material. An Apex security liaison wanted Elias to confirm that Julie had directed his emergency access. A federal coordination desk wanted Julie to identify the most urgent foreign target before the K-17 trail aged further.

The physicians rejected all three requests on medical grounds. Webb rejected them again on representation and scope. Alvarez entered the refusals into incident 187463 so the lost hours could not later be described as subjects declining cooperation after receiving the evidence.

Hackett objected most strongly to the K-17 delay. Julie could hear the problem in his voice. The field team might still be moving while lawyers protected rooms in Washington.

Alvarez asked whether he possessed a lawful military channel to warn India that a low-level field anomaly remained unresolved without exposing the seized material or attributing the operation.

He did.

“Use it,” she said. “Preserve the warning and let the local commander decide what it changes.”

The message that left contained no accusation against Tariq, Sterling, Vance, or Apex. It asked Northern Command to preserve K-17 local records, avoid destructive maintenance, and treat the relay state as unresolved pending independent field inspection.

The urgent action went forward without turning an injured detainee into its authority.

Alvarez stated that no substantive interview would occur that day."""
    return text.replace(anchor, addition, 1) if "Two agencies had already sent interview requests" not in text else text


def revise_17(text: str) -> str:
    anchor = """Grant compared the two method logs. Different operators had reached the same direct observation from the same object without using Apex software or Julie's instructions.

Only then did she allow the finding to seal."""
    addition = """Grant compared the two method logs. Different operators had reached the same direct observation from the same object without using Apex software or Julie's instructions.

She turned the board toward the overhead camera before resealing it and asked Elias whether he wanted to see the physical object one last time through the video feed. His counsel could have answered for him. Elias leaned closer instead.

The scrape on the corner remained. The copper contacts remained. Nothing about the board looked capable of carrying the weight Apex had placed on its absence from one event and presence at another.

“That is mine,” he said.

Grant asked what he meant.

“The hardware. The author certificate. The later choices. Not the deployment.”

She entered no new conclusion. The statement belonged to Elias's represented attachment, not her examination.

Julie watched Grant give him the object back in language before MPD returned it in custody. The board would remain evidence, but the separation between identity and action no longer belonged only to the people who had used it against him.

Only then did Grant allow the finding to seal."""
    return text.replace(anchor, addition, 1) if "She turned the board toward the overhead camera" not in text else text


def revise_18(text: str) -> str:
    anchor = """The original cartridge, derivative, and patrol package closed separately. Pal’s medical removal remained attached to the patrol record so no later summary could turn his interrupted words into a complete account.

At 19:29, Qureshi transmitted the acknowledgment."""
    addition = """The original cartridge, derivative, and patrol package closed separately. Pal’s medical removal remained attached to the patrol record so no later summary could turn his interrupted words into a complete account.

Restoring K-17 required a fourth record. Sethi prepared a clean replacement cartridge and verified it against the relay specification without connecting it to the operational network. The original would never return to the cassette. If the inner boundary was cleared, the relay would restart on new incident media while the old journal remained sealed under the event it recorded.

Northern Command approved a two-team inspection for first light: explosive-ordnance personnel would clear the inner seam, and relay engineers would enter only after the physical space was safe. The patrol that had recovered the cartridge would not be sent back merely because it already knew the route. Fatigue and injury were conditions, not qualifications.

Sharma signed the restoration plan beside the preservation order. One document kept the old state intact. The other allowed the mountain to continue functioning without asking the evidence to become equipment again.

At 19:29, Qureshi transmitted the acknowledgment."""
    return text.replace(anchor, addition, 1) if "Restoring K-17 required a fourth record" not in text else text


def revise_19(text: str) -> str:
    anchor = """The result did not identify Sterling.

It converted the signer from a certificate into a moving physical object that an institution now had to find."""
    addition = """The result did not identify Sterling.

Collins asked Grant whether Hartwell should suspend every Sterling-office credential until the device was found. The broader action would be easy to explain and difficult to undo. It would also convert one challenged serial into a presumption against people and credentials that had never entered the event.

Grant limited the hold to SSO-NS-004, the support path that carried it, and the specific challenge interval. Other office credentials remained active unless their own records triggered a separate review. Hartwell added a live alert so the serial could not pass another perimeter challenge while the locator request was pending.

The restriction followed the object instead of turning the whole office into a suspect.

It converted the signer from a certificate into a moving physical object that an institution now had to find."""
    return text.replace(anchor, addition, 1) if "Collins asked Grant whether Hartwell should suspend every Sterling-office credential" not in text else text


def revise_20(text: str) -> str:
    anchor = """The physical signer was no longer the most urgent object.

The name that had put it into circulation was."""
    addition = """The physical signer was no longer the most urgent object.

Vega issued two additional preservation notices before ending the intake. The office secure-communications ledger had to retain the complete assignment history for SSO-NS-004, including superseded drafts and rejected assignments. The LSS support system had to preserve every challenge, case movement, credential class, and no-use event without exposing unrelated office traffic.

Office counsel objected that rejected drafts could contain deliberative material beyond the authorized inquiry.

“Preservation is not production,” Vega said. “The privilege question can survive only if the record does.”

The second notice went to the staff responsible for portable signer inventory. No device could be substituted into the SSO-NS-004 asset record, and no replacement could inherit its serial or assignment history. The office could receive another device for lawful work under a new identity after an independent security review. It could not make the challenged signer disappear by calling its replacement continuity.

The name that had put it into circulation was."""
    return text.replace(anchor, addition, 1) if "Vega issued two additional preservation notices" not in text else text


def revise_21(text: str) -> str:
    anchor = """The borrowed name was resolved.

The person who borrowed it was not."""
    addition = """The borrowed name was resolved.

DIA counsel asked Price whether he wanted to remain on paid administrative leave or request immediate separation from the agency. The choice had no bearing on the federal finding and every bearing on whether he would return to a building whose systems had turned his caution into authority.

Price did not answer that day. He requested the decision in writing, the criteria for restored access, and confirmation that refusing to resign would not be described as failure to cooperate. Shah added that no employment action could rely on the later continuity request as Price's authenticated act after the DCIS finding.

The administrative attorney agreed to preserve the request and respond through counsel. No one promised Price his clearance, job, or reputation back.

For the first time since security removed him from his desk, he had a decision that did not need to be made before a record disappeared.

The person who borrowed his name was not resolved."""
    return text.replace(anchor, addition, 1) if "DIA counsel asked Price whether he wanted to remain" not in text else text


def revise_22(text: str) -> str:
    anchor = """For the first time, the government could say exactly which lie Arthur Vance had personally made operational.

It still could not say who had written the first one."""
    addition = """For the first time, the government could say exactly which lie Arthur Vance had personally made operational.

Alvarez asked whether the release finding justified immediate criminal arrest. The duty prosecutor refused to convert a strong operational record into a charging decision without reviewing classification, authority, intent, and the evidence connecting the release to a federal offense. Vance remained represented, restricted from operational systems, and subject to preservation and travel conditions negotiated through counsel.

Hackett called the delay institutional cowardice.

Grant called it a different question.

Julie understood both reactions. Vance's live hand was finally visible. The temptation to make visibility equal every legal element was the same temptation the manuscript's institutions had repeatedly used against her and Elias.

The release record would support the next process. It would not replace it.

It still could not say who had written the first lie."""
    return text.replace(anchor, addition, 1) if "Alvarez asked whether the release finding justified immediate criminal arrest" not in text else text


def revise_23(text: str) -> str:
    anchor = """The correction protected cause without erasing cost.

Grant closed the news monitor but left the three receipts visible."""
    addition = """The correction protected cause without erasing cost.

Webb received twelve requests for Julie before the public receipts finished propagating. News organizations wanted interviews. Two senators wanted private briefings. A defense contractor offered independent-consultant protection. An inspector general requested voluntary cooperation. A former colleague sent only the words I believed you.

Webb declined every request except the lawful preservation and custody notices already in place. She did not ask Julie which opportunities mattered. Julie remained detained, injured, and represented. Public interest did not create informed consent or erase the prohibition on investigating her own case.

The refusal disappointed people who believed vindication should immediately become testimony, service, or access. It also prevented the first hours of the corrected record from becoming a market in which every institution tried to acquire Julie's authority before she had any reason to trust its mandate.

Grant closed the news monitor but left the three receipts visible."""
    return text.replace(anchor, addition, 1) if "Webb received twelve requests for Julie" not in text else text


def revise_24(text: str) -> str:
    anchor = """The neighbor packed the ground again. This time Julie did not reach for the bar or test whether her injured hand might take some of the load.

She had spent six years believing responsibility meant carrying the full weight until no one else could distort the result."""
    addition = """The neighbor packed the ground again. This time Julie did not reach for the bar or test whether her injured hand might take some of the load.

“Lawyer said you aren't supposed to be working,” he said.

“I am holding a level.”

“That sounds like lawyer language.”

Julie looked at the post, then at the tamping bar in his hands. “It probably is.”

He did not ask what had happened in Washington. He had seen enough television to know every public answer was changing. Instead he told her the mare had found a weak lower rail near the creek and that the feed delivery would arrive Monday unless Julie wanted him to postpone it.

Ordinary work assembled itself into a list with no strategic release clock. Julie could ask for help, accept delay, or leave a rail imperfect overnight without anyone firing because of it.

She had spent six years believing responsibility meant carrying the full weight until no one else could distort the result."""
    return text.replace(anchor, addition, 1) if "Lawyer said you aren't supposed to be working" not in text else text


def main() -> None:
    revisions = {
        "chapter-15.md": revise_15,
        "chapter-16.md": revise_16,
        "chapter-17.md": revise_17,
        "chapter-18.md": revise_18,
        "chapter-19.md": revise_19,
        "chapter-20.md": revise_20,
        "chapter-21.md": revise_21,
        "chapter-22.md": revise_22,
        "chapter-23.md": revise_23,
        "chapter-24.md": revise_24,
    }
    for name, revise in revisions.items():
        path = CHAPTER_DIR / name
        original = path.read_text(encoding="utf-8")
        updated = revise(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
