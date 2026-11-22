# Module Interactions and Responsibilities

**Document:** SYS-MOD-01 | **Status:** DRAFT — proposed logical boundaries, NOT fixed microservice boundaries | **Source:** BRD v6.2.2 §§ 2–10, Appendix A (p. 11)

> **Proposed implementation style:** ASP.NET Core **Modular Monolith**, with these logical modules running in-process inside one backend deployable. This is an engineering proposal awaiting **OD-20 approval**; the BRD does **not** mandate microservices, an internal message broker, physical tables or API URL paths. Each module should expose explicit interfaces and own its data access; do not reach into another module's persistence directly. See [`Modular-Monolith-Architecture.md`](./Modular-Monolith-Architecture.md).

| Logical module | Responsibility | Collaborates with | Primary refs |
|---|---|---|---|
| Identity & authorization | Accounts, sessions, scoped role/ownership checks, recovery | Academic catalogue, teacher, commerce, XACT, admin | BR-01, 21, 22; pp. 4–5 |
| Academic catalogue | A/L Bio/Maths streams, subjects, medium, syllabus-year/topics, subject eligibility and `StudentSubject` | Identity, discovery, XACT | BR-01, 23; p. 3 |
| Teacher verification & discovery | Evidence lifecycle, authorized public profiles/filtering | Identity, class offerings, moderation | BR-02, 03; pp. 4–5 |
| Demo video management | Free optional prerecorded class previews, upload, processing, review, published view; **never** a paid enrollment gate | Teacher, class offering, media, content moderation | BR-04; p. 5 |
| Class & batch scheduling | ClassOffering, ClassBatch, schedules, capacity, cancellation/rescheduling | Teacher, enrollment, attendance, commerce | BR-05; pp. 5–6 |
| Enrollment & entitlements | Reserve/enroll authorized student, prevent duplicate seats, enforce paid/class access | Academic catalogue, commerce, live, resources | BR-05/06; pp. 5–6 |
| Live sessions & attendance | Timed authorized provider join, attendance and correction audits | Enrollment, provider adapter, notifications | BR-05; p. 6 |
| Learning resources | Protected class-linked files, scanning, revisions, signed asset links | Enrollment, media store, audit | BR-07; p. 6 |
| Orders, payment & refunds | Checkout, attempts, verified callbacks, partial/full refund reconciliation | Enrollment, entitlements, finance ledger, provider | BR-06; p. 6 |
| Finance ledger, earnings & payouts | Append-only accounting entries, approved commission, holds/disputes, payout oversight | Orders, payments, reviewers | BR-06; p. 6 |
| XACT question/content governance | Rights, canonical concept, approved translation/version/answer key, media moderation | Catalogue, academic reviewers, XACT engine | BR-18/20/23; pp. 6–7 |
| XACT exam engine | Eligible question pool, immutable question/key snapshots, attempt timer/autosave/submit, server scoring | Question bank, identity, results/analytics | BR-11/18; pp. 6–7 |
| XACT teacher papers & assignments | Paper version/draft, allowed recipient selection, per-user attempts and reports | Teacher auth, question bank, exam engine | BR-19; p. 7 |
| Notifications & outbox | Trigger/rate/queue/retry authorized events; avoid sensitive message payloads | All operational modules, external messaging | BR-13; pp. 7–8 |
| Admin, safety & audit | Approvals/reviews, report handling, privilege events, compliance evidence | All modules | BR-14/21/24; pp. 4, 7–9 |

## Authorized interaction patterns

### A. Student chooses a subject

`Identity/StudentProfile → Catalogue eligibility validation → StudentSubject record`.

**Must not** call Enrollment, Payment, Entitlement or seat reservation merely because a subject is selected (pp. 3, 5; AC-32).

### B. Teacher creates and publishes a free preview

`Teacher verified → ClassOffering exists → upload media to private store → media processing → separate reviewer approves → public-preview delivery`. 

**Must not** create TrialBooking, live trial session, booked seat, purchase or mandatory demo watching (pp. 5, 8, 12; AC-07, AC-31, AC-33).

### C. Student purchases a batch

`Class/batch eligibility → order/payment attempt → verified gateway result → idempotent settlement → appropriate enrollment/entitlement/ledger → notification → live-join authorization`.

Use transactional invariants for seats and paid entitlements; exact order/reservation design, timeouts and gateway choice are not settled (pp. 5–6; OD-04/05/20).

### D. Student takes XACT mock

`Authenticated student → permitted subject/medium → approved bank → immutable exam snapshot → autosave/submit → authoritative server scoring → scoped result + approved explanations`.

Question key correction is versioned and audited. No AI-based answer scoring replaces approved answer keys (pp. 6–7; AC-16–26).

### E. Teacher issues XACT paper

`Verified teacher → authorized subject → approved question filter → versioned draft → publish → assignment recipients → individual attempts → scoped review` (p. 7; AC-23/24).

## Cross-cutting controls

- **Access**: role **and** object ownership/membership on backend; teacher sees no unrelated students.
- **Reliability**: idempotent payment callbacks and exam submits; notifications/outbox retryable; preserve financial and exam histories.
- **Privacy**: minors' data, sensitive cases and private teacher/student records separated from public demo content.
- **Content**: source reproduction rights and per-medium reviews before XACT publication; demo moderation independent of XACT explanation videos.
- **Logging**: decisions and state transitions auditable; avoid sensitive credentials/data in logs.

## Implementation questions to resolve first

1. Final frontend/backend/database, deployment topology and physical DB schema (**OD-20**).
2. Exact gateway/provider events/webhooks, capacity reservation window and refund policies (**OD-03–06**).
3. Media/transcode/CDN platform and public preview authorization/analytics consent (**OD-02/06**).
4. Child/guardian, identity check, MFA, retention and policy versions (**OD-15/19**).
5. XACT rules and source/content legal approvals (**OD-07–11**).
6. Foundation/Marketplace/XACT rollout sequence (**OD-18**).
