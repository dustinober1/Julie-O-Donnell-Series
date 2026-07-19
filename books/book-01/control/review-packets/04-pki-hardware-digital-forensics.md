# External Review Packet — PKI / Hardware Token / Digital Forensics

**Tracking issue:** #73
**Status:** UNREVIEWED
**Accepted-manuscript baseline:** `main` commit `0a0ed1c5330cbe48a59499d7a4104aa02f6c059a`
**Manifest:** `books/book-01/ACCEPTED_MANUSCRIPT.yaml`, version 2
**Accepted structure:** Prologue + Chapters 1–24
**Accepted total:** 105,144 words
**Publication state:** NOT APPROVED FOR PUBLICATION

An AI review, public-source review, informal conversation, or unnamed opinion cannot close this external-review gate. The issue remains **UNREVIEWED** until a named qualified reviewer supplies a dated, qualification-backed deliverable tied to the baseline above.

## Minimum useful reviewer profile

Applied cryptographer, HSM or hardware-token engineer, PKI architect, secure-identity specialist, digital-forensics examiner, or practitioner experienced with non-exportable keys and signed audit records.

## Reviewer

- Name:
- Qualifications / relevant experience:
- Review date:
- Exact manuscript commit, manifest version, or generated compilation reviewed:

## Current identity and proof baseline

- `APX-DIR-0019` mirrors Elias's identity binding and public certificate.
- The server record asserts that biometric confirmation succeeded and preserves workstation, clock, credential-path, and identity metadata.
- No live finger is reproduced, the private key inside Elias's physical board is not invoked, and the original 02:14 event has no matching physical signing-counter event.
- Later gate and recovery events are distinct live-biometric and physical-private-key acts.
- `APX-DIR-0019` does not identify the original human operator.
- Vance's later authenticated release does not prove he performed the original deployment.

## Content lock

Preserve the distinction between Elias's physical board and the identity presented during the original deployment; preserve his later voluntary gate and recovery signatures; preserve `APX-DIR-0019` as an executive authority binding without an identified original human operator or personal keystrokes; preserve `SSO-NS-004`'s office registration without Sterling's physical possession or command.

## Required scenes

- Chapters 2 and 7–10.
- Chapters 17 and 20–22.
- Relevant WSS-4 and Hartwell passages in Chapters 11–14 and 19.

## Questions

1. Can a system mirror an employee identity binding and public certificate, and preserve a server-side assertion of biometric success, without reproducing a live finger or invoking the private key on the physical secure element?
2. Can a monotonic counter credibly exclude the board's physical participation in the original 02:14 event while preserving later uses?
3. Are the rotating code, live-finger/liveness check, private-key release, challenge-response, and local audit flow plausible?
4. Which claims should use `append-only`, `tamper-evident`, `hardware-sealed`, or another term instead of `immutable`?
5. Can a standalone reader expose public identity, certificate policy, and monotonic history without source writes or private-key invocation?
6. Is the reference-token test and blind replication defensible?
7. Can `APX-DIR-0019` operate as a hardware authority/service binding registered to Vance while the original human operation and personal keystrokes remain unproved?
8. Is the WSS-4 full-chain capture credible, including suite certificate, external signer, challenge, response, device time, event order, ciphertext, and controller seal?
9. Is a closed portable signer case responding in a challenge cradle credible?
10. Can legislative security preserve the same device under a no-use hold without opening it?
11. Can a continuity broker inherit Price's legitimate request identity/reference and add operational routing while the produced journal records no human caller?
12. What cryptographic or forensic wording currently implies a stronger guarantee than the mechanism can support?

Report both (a) errors or concerns and (b) credible material that should remain unchanged. Tie every finding to the exact chapter and passage and propose the smallest story-preserving correction.

## Findings

| Severity | Chapter / passage | Problem | Smallest story-preserving correction | Downstream impact |
|---|---|---|---|---|
|  |  |  |  |  |

## Credible elements to retain

- [To be completed by reviewer]

## Final disposition

- [ ] Approved
- [ ] Approved with corrections
- [ ] Not approved

Reviewer signature / confirmation:
