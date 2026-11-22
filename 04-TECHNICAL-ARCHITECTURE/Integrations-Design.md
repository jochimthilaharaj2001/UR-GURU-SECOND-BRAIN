# External Integrations — Ports, Adapters and Failure Contracts

**Status:** PROPOSED; final providers/terms **PENDING OD-02/05/06/07/15/20**.  
**Source:** BRD v6.2.2 §§6–10, AC-07–15, AC-26, AC-29.

## 1. Provider-agnostic architecture

Each external provider is behind an **interface/port** owned by the relevant module. HTTP endpoints never call provider SDKs and then directly grant entitlements without verification.

| Integration | Module owner | Proposed port / key methods (illustrative) | Pending approval |
|---|---|---|---|
| Payment gateway | Commerce | `BeginPayment`, `VerifyCallback`, `QueryPaymentStatus`, `RequestRefund` | OD-03/04/05; supported settlement/refund/reconciliation |
| Live classroom | Classes | `CreateSession`, `IssueAuthorizedJoinCredential`, `GetSessionStatus` | OD-06; provider, recording and pricing |
| Object storage/CDN | Demo/Resources/XACT | `PutPrivateObject`, `GetSignedReadUrl`, `PublishApprovedPreview` | OD-02/06/07; media rights, delivery mode |
| Media processing | Demo / XACT Explanations | `ProcessMedia`, `ReadProcessingStatus`, `GenerateRenditions` | OD-06; costs, latency, moderation |
| Email/SMS | Operations | `SendNotification`, `CheckDelivery` | channel/vendor/consent limits |
| Government identity check (conditional) | Identity | **No integration until policy and legality approved** | OD-19, OD-15 |

Names are **interface examples**, not contracted C# signatures.

## 2. Payment callback flow

```text
Student checkout -> Commerce creates order + attempt + gateway request
   -> user completes provider checkout (may return via browser)
Provider callback/status query -> authenticity + correlation + amount/currency validation
   -> idempotent payment event state transition + ledger/outbox
   -> approved enrollment/entitlement after VERIFIED success
   -> notification delivery
```

- Browser redirect, `?success=true`, client clock and unchecked callback body cannot grant paid access.
- Must handle duplicate/delayed/out-of-order callbacks, gateway outage, user abandoned payment, partial refunds, chargebacks and payout reversal.
- Refund/cancellation policies are **not** provided by a technical adapter; they come from **OD-04**.
- Exact temporary seat-reservation timeout and refund sequence need business approval. Do not invent timings.
- Verify gateway signature/credentials/merchant reference using approved provider manual, and store minimal allowed payment metadata.

## 3. Live class provider

- Authorized join only after server verifies session window, role, class enrollment and active entitlement.
- Short-lived provider-specific credential/room mapping; never expose moderator token to students.
- Session unavailable, teacher disconnected, canceled or rescheduled generates a server-controlled state and approved notification flow.
- Live class recording requires a separate consent/policy decision; it is not implied by selecting a provider.
- Reconcile provider usage/minutes and session logs with Finance once approved.

## 4. Class DemoVideo and XACT explanation video: separate products

| Aspect | `DemoVideo` (`BR-04`) | XACT `ExplanationVideo` (`BR-20`) |
|---|---|---|
| Purpose | **Optional free** class preview before buying | Review of a specific approved question/translation |
| Parent | `ClassOffering` | XACT question/translation version |
| Public? | Approved public preview per OD-02 access policy | Entitlement/reveal policy; typically protected |
| Approval | Independent rights/content reviewer | Academic/content reviewer + rights/compensation controls |
| Checkout rule | Can skip; demo never gates checkout | Never used as a fake class preview |
| Failure fallback | Keep class/checkout accessible | Written explanation when eligible |

A trial booking is **not** a demo video: do not migrate `TrialBooking` rows mechanically into `DemoVideo`.

## 5. File upload and media pipeline (candidate)

1. Obtain restricted upload authorization and media metadata record.
2. Upload to private quarantine area; validate type/size and scan media.
3. Transcode/optimize when applicable; preserve original rights evidence.
4. Independent moderation: `Uploaded → Processing → SubmittedForReview → Approved / Rejected / ChangesRequested`; publish only when approved and active.
5. Deliver through constrained public-preview path (demo) or short-lived private signed link (paid/XACT).
6. Handle process failure/withdrawal; revoke future delivery; record audit and notify owner.

Exact media processing states, provider API details and file thresholds require technical and content-policy approval.

## 6. Notifications and outbox

- Business transaction commits a durable notification/outbox record; independent worker attempts delivery.
- Distinguish email/SMS/in-app recipients; privacy rules restrict personal details in outbound messages.
- Retry transient errors with approved bounded backoff and dead-letter review; do not promise exactly-once external delivery.
- Use deduplication and delivery IDs (including event payload schema version), and monitor queue/outbox age.

## 7. Failure contract template

For each approved provider, capture:

`Provider | Endpoint/SDK version | Auth method | Secret owner | Retryable statuses | Idempotency key | Timeout | PII restrictions | Webhook signature procedure | Reconciliation | Mock test sandbox | Fallback | Ops escalation | Contract ID`.

**Related:** [`Security-Architecture.md`](./Security-Architecture.md), [`Infrastructure-Design.md`](./Infrastructure-Design.md), [`Module-Contracts.md`](./Module-Contracts.md).
