# Reliability, Observability & Test Architecture

**Status:** PROPOSED implementation patterns; **BRD §11 metrics are candidate targets, not signed SLA**.  
**Source:** BRD v6.2.2 §§8–13, AC-01–33, OD-16/18/20.

## 1. Reliability invariants

- **Class payment:** payment success only after verified server gateway state; idempotent callbacks; capacity race safe; ledger corrections preserve audit.
- **Free demo:** missing, rejected, withdrawn, or failed preview must **not** interrupt class purchase.
- **XACT:** server owns deadlines and scores; autosave retry safely retains acknowledged answers; duplicate submit yields one final result.
- **Content approvals:** no unapproved question, translation, key, demo or explanation video can be published/selected.
- **Notifications:** transactional outbox + idempotent consumers; transient retries, bounded failures and alerting.
- **Live sessions:** provider outage/teacher disconnect produces traceable attendance/access/support state; do not invent grace period without approved rules.

## 2. Outbox / inbox delivery pattern (candidate)

1. A module updates its domain state and inserts an outbox message in the **same DB transaction** when supported.
2. Worker reads eligible outbox rows, calls provider or internal handler with dedupe key, records delivery state.
3. On retry, consumer uses message ID/idempotency key to avoid duplicate effects.
4. Failed messages after bounded retries enter a visible operator review state; protect personal data in stored payload.
5. For payment: verify callback authenticity before generating trusted domain event; external provider may deliver multiple times.

Not a claim of exactly-once delivery across external services.

## 3. Minimum structured telemetry

| Signal | Example event/metric (no PII) | Why |
|---|---|---|
| Identity | failed sign-in/OTP rate, session expiry, privileged changes | Account abuse |
| Demo | media upload/processing/rights/review failures, public play failure | Preview moderation; never block enrollment |
| Classes | seat contention, session token issuance denied, join failure | Availability and safeguarding |
| Finance | callback verification failure, pending payment age, ledger mismatch, refund exceptions | Access + money integrity |
| XACT | question-pool shortage, autosave lag, duplicate submit, scoring invariant breach | Exam fairness |
| Notifications | outbox backlog age, retries and delivery errors | Reliable communication |
| Security | object-access denials, suspicious media access, safety-case overdue | Privacy / safeguarding |

Correlate by request ID, event ID and opaque entity IDs. Avoid logging raw NIC, tokens, payment credentials, test answers or minors' private details.

## 4. Proposed test pyramid and boundary checks

| Test layer | Examples | Evidence |
|---|---|---|
| Unit/domain | Subject eligibility; demo lifecycle; ledger posting rules; XACT scoring | Automated results |
| Integration/DB | Duplicate selection constraint; batch capacity race; payment idempotence; attempt snapshot persistence | Tests against approved DB engine |
| Contract/API | Auth errors, DTOs, provider callbacks/sandbox, version compatibility | OpenAPI/provider contract tests |
| Architecture | Forbidden module-to-module infrastructure dependencies | Automated architecture guard |
| E2E/browser | Demo watch-or-skip → checkout; enrollment → live join; student XACT submit; Admin review | Automated browser + manual UAT |
| Security/abuse | IDOR, role escalation, forged callbacks, media URL bypass, consent revocation | Security test report |
| Load/recovery | API p95, autosave latency, concurrency, restart/recovery, backup restore | Performance/DR evidence |

## 5. UAT critical scenarios from BRD

- `AC-01` and `AC-32`: valid Bio/Maths `StudentSubject`; reject duplicates and invalid combinations; no paid enrollment.
- `AC-07`, `AC-31`, `AC-33`: approved optional free preview watch/skip; no booking/payment/entitlement call or mandatory watch completion.
- `AC-08`, `AC-12`–`AC-15`: seat concurrency, forged/duplicate gateway callbacks, refunds and payout consistency.
- `AC-16`–`AC-22`, `AC-25`: rights/medium/snapshot, autosave, deadline, duplicate submit, historical accuracy.
- `AC-23`–`AC-24`: teacher paper version reuse; recipient-scoped attempts and results.
- `AC-26`–`AC-30`: videos/rights, safeguarding, localization, outbox recovery and restore.

Test IDs belong to latest **v6.2.2**, not old V6.1 acceptance mappings; update [`../12-TESTING/`](../12-TESTING/) accordingly.

## 6. Candidate NFR targets (unapproved)

| Measurement | BRD proposal | Required validation |
|---|---|---|
| Authenticated read API | p95 < 1.0 s | Define endpoint set, user load, environment, networks |
| Autosave ack | < 1.5 s | Define persistence/ack semantics and retry conditions |
| Platform uptime | 99.5% monthly excluding approved maintenance | Agree calendar, provider dependencies and exclusions |
| DB recovery | RPO ≤ 60 min, RTO ≤ 4 h | Backup restore tests and recovery budget |
| Capacity | Stress test 2× forecast | Agree traffic model: live, payments, XACT separately |

All above remain targets under evaluation until **OD-16** approval. Do not advertise as guaranteed.

## 7. Definition of Done candidate

`Requirement + business-rule reference → approved UI states → authorized API contract → approved DB migration → unit/integration/E2E/security tests → telemetry/audit → fallback/support → documentation updates → reviewer sign-off`.

Do not mark a feature “passed” without test evidence and traceability; vendor demos alone are not sufficient.

**Related:** [`Infrastructure-Design.md`](./Infrastructure-Design.md), [`Security-Architecture.md`](./Security-Architecture.md), [`../12-TESTING/`](../12-TESTING/).
