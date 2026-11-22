# Guardian Consent Touchpoint — Not a Guardian Dashboard

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

**Source:** BRD §§4, 6.1, 10, SJ-16 and OD-15/19. **Release:** R0–R1 safety/consent foundation. The **full guardian portal is future / uncommitted (BR-16)**.

## SJ-16 — Conditional permission and consent

1. During a protected student operation, backend determines whether an **approved** legal/product policy requires guardian consent or other identity assurance.
2. If required, collect only approved minimum guardian contact/relationship information and send a controlled authorization request through approved communication.
3. Verify the eligible guardian using an approved method (not merely a valid NIC format).
4. Record specific purpose, applicable policy version, timestamp, consent/revocation status and protected evidence.
5. On success, allow the authorized next step; on refusal/no response/revocation, apply approved restrictions and provide secure support escalation.

## Non-negotiable boundaries

- Do not mandate NIC collection for every minor without OD-19 decision.
- No implied parent login/dashboard or unrestricted view of student activity.
- Guardian contact is for approved consent/communication only.
- Revoked or failed consent must lead to a clearly handled state according to policy.
- Minimize data and protect evidence; restrict access and retention under OD-15.

## Source exceptions

No consent, revoked consent, unreachable guardian (SJ-16); failed required verification/identity assistance (BRD §6.1); safeguarding complaint escalation (SJ-15).

## Candidate UI concepts — approval required

Conditional consent-needed notice; guardian contact request; verification pending; approved/declined/revoked state; support contact. These are not evidence that a guardian portal is required.

## Required acceptance evidence

AC-04: purpose- and version-specific protected consent evidence. AC-03: NIC-format validation alone is not government verification. Also verify access restriction and safe notification handling under policy.

## Pending decisions

OD-15 minor thresholds/guardian/PDPA/retention; OD-19 NIC necessity and verification alternatives; OD-20 schema approval. Until resolution, document decision gates without inventing age thresholds, retention periods or consent channels.
