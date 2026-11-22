# Administration, Notifications and Operational Audit Rules

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Scope
Admin, finance and academic reviewers have **separated privileged capabilities**. Events must be auditable and replay-safe, and support/safeguarding workflows must protect confidential evidence.

## Main rules
| Rule ID | Requirement (review baseline) | BRD source | Related UAT | Approval gate |
|---|---|---|---|---|
| UG-RULE-075 | Notification events must be independently trackable, retryable and avoid unnecessary personal details in email/SMS. | BRD §9 p.7 | AC-29 | Review baseline |
| UG-RULE-076 | Outbox delivery and provider retries must recover from worker interruption without duplicate harmful effects. | BRD §9 p.7, §13 p.10 | AC-29 | Review baseline |
| UG-RULE-077 | Teacher verification, payment/refund, demo publication, question corrections and consent decisions need actor/time/status audit. | BRD §5–10 pp.4–8 | AC-10, AC-25, AC-31 | Review baseline |
| UG-RULE-078 | Finance reviewers approve authorized refunds/payouts; no unaudited manual ledger edits. | BRD §4 p.4, §7 p.6 | AC-14, AC-15 | Review baseline |
| UG-RULE-079 | Support and safeguarding escalations require a controlled owner, restricted evidence and protected case history. | BRD §9 p.7, §12 p.9 | AC-27 | Review baseline |
| UG-RULE-080 | Proposed numerical performance/availability/RPO/RTO benchmarks are candidates, not production SLAs. | BRD §11 p.8 | AC-30 | Pending policy OD-16 |
| UG-RULE-081 | Operational monitoring covers live failures, payment mismatches, outbox backlog, exam autosave failures, videos and safety escalations. | BRD §11 p.8 | AC-30 | Review baseline |

## Operational acceptance
- Notifications survive worker crash and retry safely (BRD AC-29).
- All privileged decisions include actor, timestamp, reason where appropriate.
- Incident, backup, concurrency and monitoring verification must be demonstrated before production (AC-30).

## Non-functional approval
BRD §11 p.8 SLO metrics are *candidate benchmarks*, not contracted or approved SLAs. **OD-16** covers production targets.
