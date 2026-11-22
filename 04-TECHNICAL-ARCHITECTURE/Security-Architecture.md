# Security & Privacy Architecture

**Status:** PROPOSED security controls; legal/identity/session approvals **PENDING OD-15/19/20**.  
**Source:** BRD v6.2.2 §§4, 6–11, AC-01–04, AC-05/06, AC-11–15, AC-16–33.

## 1. Trust boundaries

```text
Untrusted browser -> TLS/API perimeter -> authenticated user/session
   -> role + ownership/membership policy -> module application command
   -> module-owned persistence / restricted external adapter

Untrusted provider callback -> signature verification + replay prevention
   -> verified provider state -> idempotent module state transition
```

The Admin Web is a **separate entry point** but not an exception to authorization. Never trust role claims, hidden menu items, URLs or client-side XACT scoring.

## 2. Authentication and session lifecycle

- Required account states: `Pending Verification`, `Active`, `Locked`, `Suspended`, `Closed` (BRD §6.1).
- Login/logout/recovery session invalidation and account existence non-disclosure (AC-02); rate-limit login/OTP recovery by policy, without making up threshold numbers.
- Privileged staff should have MFA; precise session/token/cookie architecture is **PENDING OD-20/security sign-off**.
- Secure cookie + CSRF protection, secure headers and session rotation are engineering candidates. Avoid storing bearer tokens in long-lived browser local storage by default.
- Every high-risk state change requires actor, timestamp, reason and protected audit reference.

## 3. Authorization matrix (minimum invariants)

| Actor | Allowed example | Forbidden example |
|---|---|---|
| Student | Own `StudentSubject`, own authorized classes/XACT attempts | Other student's result, unrelated class resources, finance data |
| Approved teacher | Own approved classes, assigned recipients, submit own demos/papers | Self-approve DemoVideo, alter bank source key, view unrelated learners |
| Academic reviewer | Assigned translations, keys and XACT explanation review | Skip source rights/approval audit |
| Admin/Operations | Authorized review and moderation | Blanket access without audit; bypass policy owner |
| Finance reviewer | Authorized refunds/payout review and reconciliation | Silent ledger edits or unrelated identity access |
| Guardian contact | Limited legally permitted consent/communications | General guardian dashboard or all learner history |
| Anonymous/public viewer | Approved published free class preview **if public access policy allows** | Raw media source, moderation notes, watch-history or paid assets |

Combine **RBAC + object-level membership/ownership** checks inside server/application layer; authorization is **deny by default**.

## 4. Content + demo media

- Demo: teacher owns linked ClassOffering; independent reviewer approval before publication; public preview cannot expose private raw files or paid content.
- Demo is always **free** when approved/public; playback must not create booking/payment/entitlement or require completion for enrollment (AC-07/31/33).
- Uploads: validate media file type and size, scan as appropriate, processing/transcoding state, rights and content review. Keep immutable audit history.
- Class resources and XACT video: private object storage, short-lived signed delivery, server-side entitlement checks. Store access audit according to retention policy.
- Teacher video licence/compensation and question reproduction rights **not approved**; rights evidence before publishing.

## 5. Payment and exam integrity

- Do not trust payment browser callback. Authenticate server-to-server notifications, validate gateway reference/amount/status and enforce replay/idempotency controls.
- Append-only ledger plus compensating entries for refunds/chargebacks; no mutable manual balance adjustment.
- XACT server stores immutable question/translation/key/snapshot; no ability to choose marks on client; idempotent save/submit and server enforced deadline.
- Question and language rights must be active; every medium-specific translation/key separately reviewed; no silent medium fallback.
- Teacher result access limited to authorized recipients/class scope.

## 6. Sensitive personal data & minors

- Collect only minimum needed data; do not require NIC from every minor by default. NIC-format pass **does not equal government identity verification** (AC-03).
- Consent events must capture purpose, policy version, evidence and revocation. Whether/when guardian consent applies is **PENDING OD-15/19**.
- Encryption at rest/in transit, data access logging, secrets management, secure backup and restricted operational access are design requirements.
- Retention, deletion/anonymization, data processors, cross-border transfer and Sri Lankan PDPA matters require legal review. Never invent days/months for deletion.
- Avoid raw student personal info in request logs and notification bodies.

## 7. Threat → control mapping

| Threat | Control and validation test |
|---|---|
| User accesses another student's exam result via ID | Object-ownership policy + 403/not found as approved; negative integration test |
| Teacher approves own demo | Separate reviewer privilege + review audit + negative test |
| Replayed payment webhook grants duplicate access | Signature/replay window + idempotency key + exactly one entitlement test |
| Direct resource URL bypasses class entitlement | Short-lived link issued only after backend authorization + revoked-user test |
| Approved translation replaced silently | Versioned record and no fallback; medium mismatch test |
| Malicious upload or illegal content | Scan, moderation and rights controls; reject/unpublish test |
| Privileged account stolen | MFA, least privilege, audit alerts and session revocation |
| Sensitive info leaked via logs | Structured scrub/redaction and sample log review |

## 8. Secure implementation checklist

- [ ] Authentication/session and MFA mechanism approved.
- [ ] Role + ownership policy tests exist for every endpoint.
- [ ] Provider credentials/secrets not in code, README or client build.
- [ ] CORS/CSRF, rate limits and safe headers configured per deployment.
- [ ] File upload safety, signed URL expiry, rights and reviewer independence tested.
- [ ] Payment callback signature/idempotency and ledger corrections tested.
- [ ] XACT tamper/deadline/duplicate/regrade scenarios tested.
- [ ] Guardian/NIC/retention and privacy decisions logged before launch.

**Related:** [`Integrations-Design.md`](./Integrations-Design.md), [`Reliability-Observability-and-Testing.md`](./Reliability-Observability-and-Testing.md), BRD OD-07/09/15/19/20.
