# Frontend Technical Architecture — Responsive Web

**Status:** PROPOSED / framework selection **PENDING OD-20**. 
**BRD source:** v6.2.2 pp. 1–4, 5–9, acceptance AC-01–33.

## 1. Application boundaries

| Web entry point | Users | Responsibility | Design boundary |
|---|---|---|---|
| **Student/Teacher Responsive Web** | Students and verified/pending teachers | Registration, catalogue, discovery, optional demo, enrollment, classes, XACT practice, teacher papers | Role-guarded routes; public browsing must not grant protected access |
| **Separate Admin Web Portal** | Approved admin, academic reviewer, finance reviewer, operations/safeguarding | Teacher verification, demo/XACT content approval, finance oversight, audit and support | Distinct host/deployment or routing isolation candidate; server policies are authoritative |

**Current scope is web only:** no native Flutter/mobile app, Play Store billing or full guardian dashboard. Framework (Angular, React, etc.) is **not** determined by BRD v6.2.2. Do not infer framework from old prototypes.

## 2. Proposed client composition

```text
Web App
├── app-shell                 route table, session boundary, navigation
├── platform                  authenticated HTTP client, retry rules, locale, feature guards
├── shared-ui                 design tokens, accessible controls, error/empty/loading states
├── features/
│   ├── account-and-academics
│   ├── teacher-discovery
│   ├── optional-demo-preview
│   ├── classes-and-enrollment
│   ├── learning-resources
│   ├── xact-practice
│   └── teacher-paper-builder
└── tests                     unit, component, browser/E2E

Admin Web
├── app-shell
├── security-and-auth
├── teacher-verification
├── demo-moderation
├── xact-content-and-review
├── finance-and-reconciliation
└── audit-and-support
```

Route names are illustrative; authoritative screen IDs/routes belong in `06-UI-UX-DESIGN` and API contracts in `08-API-DOCUMENTATION`.

## 3. State and API handling

- **Server is the source of truth:** payment success, entitlements, XACT score, answer deadline, role/object permission and content approval.
- Client caches data for presentation only; invalidate on confirmed transitions, not on optimistic gateway redirects.
- Standard view states: loading, empty, error, offline/retry, permission denied, success, processing/pending approval.
- Use typed API client from approved OpenAPI when available; versioning and auth errors are standardized.
- Distinguish persistent form draft vs authoritative `StudentSubject` selection and `Enrollment`.
- Do not store secrets, private media URLs or payment sensitive data in frontend logs; short-lived access URLs may expire.

## 4. Product-critical screen behavior

### Student enrollment + optional free preview

- Teacher/class page shows approved, published demo when present; if absent/unavailable show teacher/class data and direct batch/checkout action.
- **No playback gate**; user can immediately skip preview and continue.
- Demo video is not `TrialBooking`, no free seat hold/attendance/payment is created.
- Payment pending/failed/success UI reflects **server-confirmed** status; no claim of access on client redirect alone.

### Grade 12/13 subject selection

- Bio/Maths launch choices only; validate subject combinations with server and show invalid reason.
- Selecting subject shows selected subjects **not paid enrollments**; no class access implied.

### XACT

- Only approved medium translations; show explicit “not available in this medium” rather than silently switching Tamil/Sinhala/English.
- Present exam timer using server deadline; display timer is **non-authoritative**.
- Show autosave status, retry/error state and attempt submitted/expired states; score returned by backend.
- Scientific symbols, equations, long options, text scaling and keyboard controls must be testable on low-bandwidth/mobile browser matrix.

### Admin

- Teacher cannot self-approve demo/question content; admin/reviewer UI checks permission but backend independently enforces it.
- Finance cases require scoped roles; moderation audit and content version links visible only to authorized roles.

## 5. Localization & accessibility

- Tamil, Sinhala and English UI/content **only where approved**; locale must not change answer keys/option identity.
- Use semantic HTML, keyboard focus, accessible validation errors and diagram alt-text/structured alternatives where possible.
- Decide browser support/target WCAG version under NFR release gate; include low-end devices and Sri Lankan network testing.

## 6. Security + resilience

- Prefer a backend-mediated secure-session model (e.g., HttpOnly Secure SameSite cookie + CSRF mitigation) **as a design candidate**; exact token/session strategy requires Security Lead approval.
- Handle 401 re-authentication and 403 no-access differently; never expose object IDs to circumvent backend checks.
- Require revalidation on protected joins/material downloads, and never infer access solely from a hidden button or disabled menu.
- Network reconnect attempts must not auto-submit a mock if server deadline/attempt state no longer permits it.

## 7. Exit criteria

Document approved framework, route/screen inventory, design system, browser support matrix, accessibility standard, secure session strategy, contract generation workflow, analytics consent and test evidence before declaring frontend design accepted.

**Links:** [`Security-Architecture.md`](./Security-Architecture.md), [`../05-USER-JOURNEYS/`](../05-USER-JOURNEYS/), [`../06-UI-UX-DESIGN/`](../06-UI-UX-DESIGN/), [`../08-API-DOCUMENTATION/`](../08-API-DOCUMENTATION/).
