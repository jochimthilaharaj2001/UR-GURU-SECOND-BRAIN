# Admin, Academic, Finance & Operations Journeys — UR GURU

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

## Role boundaries

BRD §4 p. 4 distinguishes **Admin/Operations**, **Academic Reviewer**, **Finance Reviewer**, and protected safeguarding responsibilities. These are not interchangeable superuser permissions. No hidden button equals authorization: backend checks role **and** object ownership/membership; privileged accounts should use MFA.

## SJ-14 — Moderation and operational decisions (R0–R2)

**Source:** BRD §§4, 6.2, 6.3, 8.1, 8.4, 9 and §12. **BR-14/24; candidate AC-05/25/27/31.**

1. Receive a scoped task: teacher verification; demo/video review; catalogue/question translation approval; rights or safety concern; support exception.
2. Check authorized reviewer scope, supporting evidence and rights/consent status.
3. Record decision with actor, timestamp, reason and version.
4. Update permitted publication/access status and trigger retriable notification.
5. Preserve auditable outcome and allow authorized investigation/rollback procedure.

**Exceptions:** Unauthorized operator, approval conflict, pending content rights, failed media process, escalation breach, invalid rollback; reject without leaking private content.

## Teacher verification moderation (R1)

Approve/reject/request details/suspend only according to OD-01 policy. Unapproved teachers must not publish public classes or appear in discovery. Prior paid-student continuity action remains a separate policy decision.

## Demo moderation (R1)

An independent authorized reviewer checks video, rights, medium, safeguarding and processing. Publish only **Approved + Published + Active** demos; immediately disallow withdrawn, rights-invalid, rejected or still-processing videos. Teacher cannot approve own demo. Public playback may not expose moderation notes or storage keys. Detailed public-view analytics/consent under OD-02/15.

## Finance review / refund authorization — SJ-08

Finance reviewer reviews original order/line items, gateway status, policy and dispute holds; approves/rejects refund according to OD-04; payment processor state and append-only correction ledger must reconcile; prevent duplicate refund/reversal and unaudited manual ledger edits. Payment provider capability OD-05 is pending. See [Payment-and-Refund-Journey.md](Payment-and-Refund-Journey.md).

## Academic content review / XACT

Academic reviewer independently approves applicable source rights, translated options, answer key version, written and video explanations before question is eligible for XACT. Question correction/withdrawal is versioned and historical attempts preserved; any regrade follows OD-09 policy.

## SJ-15 — Help/safeguarding escalation

Report → secure triage → restricted access where necessary and authorized → assigned safeguarding owner → controlled outcome and private audit. Do not expose confidential evidence in generic notifications. Emergency escalation policy OD-15 remains pending.

## Proposed admin screen families — NOT approved IDs

Review queues; teacher verification case; demo review case; subject/question moderation; finance/refund case; notification and audit status; safeguarding report/case; incident exception dashboard. Actual screen inventory must be validated in Section 06.

## Admin UAT evidence

At minimum verify role separation, audit trail, moderation state, content visibility, protected evidence, payment callback idempotency, refund reconciliation, notification retries and least-privilege access.
