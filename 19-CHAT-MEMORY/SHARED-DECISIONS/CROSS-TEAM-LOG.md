# UR GURU — Cross-Team Decision Log

**Folder:** `19-CHAT-MEMORY/SHARED-DECISIONS/`  
**Purpose:** Record decisions made by one developer that impact other team members (API contracts, DB schemas, auth tokens, business rules).

---

## Decision Protocol
When any developer makes a decision affecting another module:
1. Add an entry to the table below.
2. Tag the affected developer IDs (`@DEV_2`, `@DEV_3`, etc.).
3. Wait for acknowledgment before finalizing dependent code.

---

## Cross-Team Log

| Date | Log ID | Author | Affected Devs | Decision / Change Summary | Status |
|---|---|---|---|---|---|
| 2026-11-17 | XDEC-001 | DEV_1 | All | Adopted BRD V6.1 as Level 1 Truth. Responsive Web only; A/L Grade 12/13 only. | `Adopted` |
| 2026-11-17 | XDEC-002 | DEV_4 | DEV_2, DEV_5 | 26-Entity ERD with 7 Critical Fixes finalized. QuestionVersion snapshotting enforced. | `Adopted` |
| 2026-11-17 | XDEC-003 | DEV_1 | DEV_2, DEV_3 | Safeguarding & Consent (`BR-21`) confirmed as Phase 1 Must. No personal phone exchange. | `Adopted` |
| 2026-11-17 | XDEC-004 | DEV_5 | DEV_2, DEV_3 | Exam Munnodi canonical translation model (`C-04`): zero silent fallback to other languages. | `Adopted` |
| 2026-11-24 | XDEC-005 | DEV_2 | DEV_3, DEV_5, DEV_6 | Finalized Identity & Profile APIs (MVP-01-010..013): GET /users/me, PATCH /students/me/profile, PATCH /teachers/me/profile, POST /teachers/me/identity-documents. | `Adopted` |

---

### [XDEC-005] Identity & Profiles API Contracts Finalized
- **Date:** 2026-11-24
- **Author:** DEV_2
- **Impacted Members:** @DEV_3, @DEV_5, @DEV_6
- **Context:** Completed all 13 Identity Module APIs in the backend with full integration test suites.
- **Decision:**
  - Strict form field whitelisting on PATCH /students/me/profile and PATCH /teachers/me/profile.
  - POST /teachers/me/identity-documents accepts multipart/form-data with `documentType` (NIC_Front, NIC_Back, Degree_Cert, NIC) and `file` (PDF/JPEG/PNG <= 5MB).
  - Storage keys are server-generated opaque keys; private storage is non-public outside wwwroot.
  - DisableAntiforgery is applied to the identity-documents endpoint with Bearer header authentication.
- **Action Required by Others:**
  - `@DEV_3` (Student Frontend) can integrate `/auth/*`, `GET /users/me`, and `PATCH /students/me/profile`.
  - `@DEV_5` (Teacher Frontend) can integrate `/auth/*`, `PATCH /teachers/me/profile`, and `POST /teachers/me/identity-documents`.
  - `@DEV_6` (Admin Frontend) can integrate `/admin/login` and prepare the verification queue shell.

---

## Log Entry Template
```markdown
### [XDEC-XXX] <Short Title>
- **Date:** YYYY-MM-DD
- **Author:** DEV_X
- **Impacted Members:** @DEV_X, @DEV_Y
- **Context:** <Why was this decision needed?>
- **Decision:** <What was agreed or changed?>
- **Action Required by Others:** <What do affected devs need to update?>
```

