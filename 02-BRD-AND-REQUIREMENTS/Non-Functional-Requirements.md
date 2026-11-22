# Non-Functional Requirements — BRD v6.2.2

> **UR GURU Second Brain — Development reference**  
> Source: [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](./UR_GURU_Full_Corrected_BRD_v6.2.2.pdf), consolidated corrected edition, 19 November 2026.  
> **Document status:** DRAFT EXTRACTION from BRD v6.2.2; source itself is a **review candidate pending stakeholder sign-off**.  
> **Use:** Requirements analysis / development planning; not independent approval or an executed test record.

## Status and scope

The values below come from **BRD v6.2.2 §11, p. 8**. The BRD calls them **candidate engineering benchmarks, NOT approved SLAs**. They require agreed test environments, a Sri Lankan device/network matrix, realistic class/payment/XACT concurrency, and sign-off (OD-16, OD-20).

| Domain | Source-based requirement / candidate benchmark | Proposed verification evidence (not yet performed) | Responsible party from BRD |
|---|---|---|---|
| Security | TLS, server-side object/role access, privileged MFA, encrypted secrets, webhook signature and replay controls | Threat model; role/object authorization tests; secret and webhook replay tests | Security owner |
| Performance | **Candidate** P95 authenticated read API **under 1.0 s**; autosave acknowledgement **under 1.5 s** at defined load | Load test with approved dataset/device/network, P95 report and autosave measurements | Engineering / QA |
| Scoring integrity | Same immutable question/key snapshot must always give identical score; repeated submit creates one final result | Snapshot and retry/idempotency integration tests | Academic / QA |
| Availability | **Candidate** 99.5% monthly platform uptime excluding approved maintenance; provider SLA separate | Monitoring definition and availability calculations | Sponsor / Operations |
| Recovery | **Candidate** DB **RPO ≤ 60 min**, **RTO ≤ 4 h**, validated by restore drills | Backup/restore log, drill report, observed recovery time | Operations |
| Capacity | Forecast live joins, payments and exams independently; stress-test at **2×** agreed forecast | Capacity model and stress test evidence | Engineering / Finance |
| Mobile/browser compatibility | Responsive browser support with low-bandwidth fallback for PDFs, live video and free demos; no native app commitment | Agreed browser/device/network coverage matrix | Product / QA |
| Localization | Approved Tamil, Sinhala, English content; readable equations/diagrams/units and long MCQ options | Language/content and accessibility test evidence | Academic / UX |
| Accessibility | Keyboard navigation, labels, focus, contrast and scaling; agreed WCAG target is **not yet specified** | Accessibility audit against signed target | UX / QA |
| Reliability | Transactional paid-seat reservation; payment/exam idempotency; durable outbox/retries; demo playback failure must not block enrollment | Concurrency tests, callback replay tests, provider outage tests | Engineering / QA |
| Observability | Alert on failed joins, payment mismatch, outbox backlog, answer-save errors, demo/explanation-video failures and safety escalations | Dashboards, alert test cases, incident playbooks | Operations |

## NFR constraints elsewhere in the BRD

- **Privacy and consent:** Minimum personal data; minors' consent; purpose-specific versioned evidence; retention and legally reviewed transfers (pp. 4–5, 7–8).
- **Media security:** Private class resources and XACT videos use entitled, short-lived access; approved public demos use separately controlled free-preview delivery (pp. 5–8).
- **Content integrity:** Per-language review and canonical question/version snapshots; no silent fallback between languages (pp. 3, 6–7).
- **Audit:** Role/object ownership checks, teacher verification, approvals, refunds, regrades, safety cases and ledger corrections are auditable (pp. 4–8).

## Before production approval

- [ ] Approve NFR numeric targets, SLAs and test environment/device matrix.
- [ ] Name security and operational owners.
- [ ] Confirm approved capacity estimates, data retention periods and incident response SLAs.
- [ ] Test backup/restore and failure modes for live class, payment, autosave and demo delivery.
- [ ] Link validated evidence to test register; **no tests are claimed to have been executed by this document**.

See BRD §11 (p. 8), `OD-15`, `OD-16` and `OD-20`.
