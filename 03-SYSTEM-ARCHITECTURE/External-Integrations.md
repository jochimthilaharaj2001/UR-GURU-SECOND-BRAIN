# External Integrations — Conceptual Contracts

**Document:** SYS-EXT-01 | **Status:** DRAFT; exact providers and integration DTOs are **not selected** | **Source:** BRD v6.2.2 §§ 2, 6–11, 14

The BRD specifies **behavioral safeguards**, not signed vendor choices. All provider names, credentials, prices, callback field names and network endpoints are **PENDING APPROVAL** and must not be invented.

| External dependency | Logical purpose | Required controls and failure handling | Decision |
|---|---|---|---|
| Payment gateway / settlement partner | Class checkout, payment attempts, refunds, reconciliations, possibly future XACT paid access | HTTPS; authenticated/revalidated callbacks; idempotency; unique references; append-only correcting ledger; never trust browser redirect; reconcile delayed/duplicate/failed callbacks | OD-05, OD-03/04; BRD p. 6 |
| Live classroom provider | Create/authorize teacher session join for enrolled students | Backend-issued short-lived join credentials; check membership and valid window; handle outages/reschedules/attendance audit; recording policy needs approval | OD-06; pp. 5–6 |
| Private media/object storage and delivery | Class resources, protected XACT explanation media, raw demo uploads | Private source keys; upload validation/scanning; review before publish; signed/short-lived protected delivery; separate **public demo-preview** policy | OD-02/06; pp. 5–7 |
| Media processing/CDN/video playback | Transcode/demo preview/VOD explanation delivery | Processing/review states; reject unprocessed or withdrawn content; fallback if video fails; never block class checkout because demo unavailable | OD-02/06; pp. 5, 7–8 |
| Email/SMS/push or equivalent messaging | Verification, class enrollment/join changes, refunds and assignment alerts | Minimal personal data; retryable delivery; idempotent notifications; track delivery failures | Vendor not chosen; BR-13, pp. 7–8 |
| NIC/identity verification partner (conditional) | Identity assurance if necessary and legally approved | Format validation is **not** identity verification; protect minors; approved purpose, exemptions, retention and audit | OD-19; pp. 4–5, 11 |
| AI/speech-to-text (later, conditional) | Lecture transcription, teacher-reviewed notes, study help | Explicit class-recording permission, human review, approved privacy, budgets; **not** dependency of initial R0/R1/XACT scoring | BR-08/09/10, pp. 3–4 |

## Integration contract checklist (complete only after provider choice)

For each provider, obtain and version: owner, approved contract, data residency/processor terms, domain/endpoint allow-list, authentication/signatures, retries/backoff, idempotency key semantics, timeouts, secret rotation, observability, sandbox, webhook testing, refund/reversal semantics, failover, cost/rate limits and incident contacts.

## Payment callback boundary (mandatory)

1. Browser starts authorized checkout for an order; sends user to provider/hosted flow.
2. Browser return **does not** grant access.
3. Server verifies gateway notification/result authenticity and current provider state; processes event idempotently.
4. Ledger, entitlement and enrollment decisions reflect verified transactions and capacity/commission policy.
5. If event is delayed/duplicate, retrieve status safely without duplicate entitlement or double charge posting.
6. For refund, append linked correcting ledger entries and apply only authorized entitlement changes; preserve audit trail.

Exact state machine and seat reservation order must be specified in the finance/technical design before coding (OD-04/05/20).

## Free preview vs paid/XACT media boundaries

- **Free DemoVideo** is linked to ClassOffering, reviewer-approved, publicly previewable **without prior payment/enrollment**. Viewer account/analytics policy remains pending. No charge, attendance or booking events (pp. 5, 12).
- **Paid class resources** require an authorized enrolled student and short-lived asset links (p. 6).
- **XACT explanation video** requires approved question/translation and teacher-created content review; access follows review/entitlement policy (p. 7).

## Outage examples

| Scenario | Safe fallback |
|---|---|
| Payment provider not responding | Pending/failed status; do not grant paid entitlement until verified |
| Duplicated webhook | Idempotent no-op for previously processed event, preserve audit |
| Live provider outage | Display unavailable; log/report and use approved reschedule policy |
| Demo file absent/fails | Allow skipping; paid batch selection and checkout remain available |
| XACT video unavailable | Keep authorized written explanation fallback |
| Notification gateway outage | Queue/retry, avoid unsafe duplicate business action |
| Identity verification undecided | Leave pending/alternative route; no invented NIC-based certification |

**Open decisions:** See BRD v6.2.2 pp. 10–11 (OD-02 through OD-06, OD-15/19/20).
