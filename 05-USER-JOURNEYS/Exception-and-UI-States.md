# Journey Exceptions, UX States and Recovery Checklist

> **Document status:** Documentation draft based on UR GURU BRD v6.2.2 (19 November 2026); stakeholder sign-off pending.  
> **Controlled source:** [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](../02-BRD-AND-REQUIREMENTS/UR_GURU_Full_Corrected_BRD_v6.2.2.pdf).  
> **Important:** Proposed UI labels and screen splits are *design suggestions*, not verified screen inventory or approved routes. Backend/API/database details require their own approved contracts.

The exception names below are drawn from **BRD §12 pp. 8–9**. UI state names and suggested recovery messaging are **derived UX design considerations**, not approved screenshots, routes or final copy. Avoid guaranteeing unapproved retries, deadlines or refunds.

| Journey | Exception / source | Proposed user-visible handling | Key invariants |
|---|---|---|---|
| SJ-01 | Invalid code; duplicate/suspended user; invalid subject | Explain validation/pending access; safe retry or support | No account enumeration; StudentSubject ≠ Enrollment |
| SJ-02 | Teacher needs info; rejected; expired evidence | Show review status, requested action and limited access | No publishing without approval |
| SJ-03 | No match/inactive teacher/class withdrawn | No results + filters; do not expose inactive class | Only eligible approved listings |
| SJ-04 | No demo/failed/withdrawn preview | Hide or unavailable/retry; **keep Enroll visible** | No preview gating or trial booking |
| SJ-05 | Full seats; failed payment; duplicate/delayed callback | Clear pending/failed/reconciliation state | No duplicate paid entitlement or oversell |
| SJ-06 | Provider outage; late join; reschedule | Live unavailable/changed session status | Access only within authorized join policy |
| SJ-07 | Resource revoked/scan failed/expired access | Access denied or resource unavailable | No private media URL bypass |
| SJ-08 | Refund denied/partial/provider failure/dispute | Show status and approved next steps | Append-only financial corrections |
| SJ-09 | Medium unavailable; answer locked; save interrupt | Exact unavailable language; save retry notice | No silent translation fallback |
| SJ-10 | Too few questions; expiry; repeat submit | Request valid selection; deadline/complete state | No invented questions or duplicate results |
| SJ-11 | Unauthorized/expired/too many attempts | Assignment unavailable/closed | Scope to recipient only |
| SJ-12 | Withdrawn/invalid question; regrade | Prevent invalid publication; review version history | Do not rewrite scored history |
| SJ-13 | Processing/rejected/rights complaint | Show review status; hide playback | Written explanation fallback |
| SJ-14 | Unauthorized admin; escalation/rollback | Access denied, audit incident, safe correction | Least privilege, audit every change |
| SJ-15 | Emergency/confidential report | Protected escalation and acknowledgment | No sensitive evidence in generic alerts |
| SJ-16 | Missing/revoked/unreachable guardian | Conditional access restriction and support | No default guardian dashboard |

## Required standard UI states per journey

- [ ] **Loading:** clear progress without exposing private data.
- [ ] **Empty:** no records available; explain the safe next action.
- [ ] **Validation error:** field or configuration restriction; no fabricated eligibility.
- [ ] **Forbidden:** backend denies role/object access; no data leak.
- [ ] **Unavailable/external provider:** transparent temporary failure and safe recovery route.
- [ ] **Submitted/confirmed:** state is shown only after trustworthy server confirmation.
- [ ] **Retry/idempotency:** safe action replay; do not duplicate payment, exam submission or assignment.
- [ ] **Time window:** exam, assignment and live join windows based on backend policy.
- [ ] **Localization/accessibility:** Tamil, Sinhala, English (only approved content), keyboard/focus and scientific notation.
- [ ] **Support:** accessible path for unresolved identity, payment, rights or safety issues.

## No invented policy defaults

Do **not** pick trial times, exam grace period, negative mark rate, refund SLA, teacher percentage, account retention duration, or provider retry count unless backed by approved source. Existing technical targets in §11 are **candidate** only.
