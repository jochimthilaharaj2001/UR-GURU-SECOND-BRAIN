# Authentication and Authorization Flow

**Document:** SYS-AUTH-01 | **Status:** DRAFT, workflow requirements from BRD v6.2.2 | **No auth vendor/session specification has been formally approved** (OD-15, OD-19, OD-20).

## 1. Separation of roles, identity and ownership

- **Student** — own academic profile/subject selection, paid enrollments, live access, personal XACT attempts/results only.
- **Teacher** — own authorized class offerings, classes, demos/materials; assigned learners and permitted assessment recipients only.
- **Academic reviewer** — assigned question translation/answer key/explanation review; cannot bypass rights approvals.
- **Admin / operations** — scoped teacher/catalogue/demo/safety moderation; privileged edits audited.
- **Finance reviewer** — authorized reconciliation, refund/payout review; ledger modifications auditable.
- **Guardian contact** — legally applicable consent/communications only; **no full guardian dashboard** in current scope.

The BRD distinguishes **role** and **object membership/ownership**; just hiding a button in UI is not authorization (pp. 3–4).

## 2. Authentication lifecycle (BR-01, 21, 22)

`Start → register/login → verify required contact/identity/consent → create/validate server-side session → role + object policy on each protected request → permitted response`.

- Account statuses: **Pending Verification, Active, Locked, Suspended, Closed** (p. 5).
- Recovery, logout, reset must invalidate appropriate sessions (p. 5).
- Unknown-account behavior/recovery must avoid leaking whether a user exists (AC-02, p. 9).
- **NIC is not mandatory by default for every minor.** NIC format validation alone does not authenticate government identity. Necessity/provider/exemptions/retention pending legal/product approval (OD-19; pp. 4–5).
- Guardian consent, *if required*, is purpose-specific, revocable, policy-versioned and access-protected (OD-15; p. 5).
- MFA for privileged users is a proposed security control; enrollment/integration details pending implementation decisions (p. 4, p. 8).

## 3. Server-side authorization per request

For a protected action, evaluate in order:

1. Is caller authenticated with valid active account/session (where required)?
2. Is caller's **role** permitted for this function?
3. Is caller the **owner/authorized member/assigned reviewer/recipient** of this specific object?
4. Is current object state permissible (approved/published/active/paid/within join or exam window)?
5. Are privacy/consent and content rights restrictions met?
6. Log sensitive/privileged changes and return minimum authorized data.

**Never** authorize based on client-submitted role, teacher ID, exam score, callback redirect or guessed storage key.

## 4. Context-specific examples

| Action | Required authorization / policy |
|---|---|
| Student select A/L subject | Student owns profile; Grade 12/13 + stream/subject/year valid; **no enrollment or entitlement granted** (pp. 3, 5; AC-32) |
| Watch free published demo | Approved active class-linked demo; free independent of payment. Account/viewer policy **pending OD-02**; do not force prior booking or checkout (p. 5; AC-07/31/33) |
| Teacher upload demo | Verified approved teacher owns eligible ClassOffering; separate reviewer moderates (p. 5) |
| Student join live class | Valid authorized enrollment/entitlement, session window and short-lived provider credential (pp. 5–6; AC-09) |
| Student download private material | Class membership/entitlement; short-lived signed URL; not accessible by guessed URL (p. 6; AC-11) |
| Student start XACT mock | Eligible approved question/medium/version; current exam rules and attempt status (pp. 6–7) |
| Teacher issue XACT paper | Approved teacher + authorized subject + selected recipients; teacher sees only related results (p. 7; AC-23) |
| Academic reviewer publish question/video | Assigned reviewer, valid rights/versions and complete review evidence; submitter cannot self-approve demo (pp. 4–7) |
| Admin/finance action | Least privilege, documented review/policy authority, audit entries (p. 4) |

## 5. Error and exception behavior

- Authentication failure: deny action with safe error; no account enumeration; log appropriately.
- Unauthorized object access: do not expose other students' profile, attempts, rosters, private videos or payment details.
- Suspended teacher: block new publication; current paid student continuity must follow approved policy (p. 5).
- Revoked consent: record change, stop disallowed processing and follow approved retention/legal policy (p. 5).
- Expired exam/assignment: enforce server deadline; preserve existing submitted attempts (pp. 6–7).
- Demo unavailable: do **not** block enrollment (BR-04, p. 5).

## 6. Open technical policy decisions

- Login/session mechanism, MFA implementation, token TTL/rotation, authentication provider: **OD-20**.
- Public demo viewer login requirement/analytics/consent: **OD-02, OD-15**.
- NIC check necessity and official verification route: **OD-19**.
- Child/minor consent and retention/deletion: **OD-15**.
- Full permission matrix and API-specific policies: validate after API/ERD sign-off; do not invent endpoints here.

**Acceptance references:** AC-01–06, AC-07/09/11/12, AC-16/17, AC-21/23, AC-27/31–33 (BRD pp. 9–10).
