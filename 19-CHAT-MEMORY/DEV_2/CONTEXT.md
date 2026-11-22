# DEV_2: Backend Specialist (C# ASP.NET Core) — Context & Starter

**Developer ID:** `DEV_2`  
**Role:** Backend Developer (ASP.NET Core Web API)  
**Primary Focus:** Clean Architecture solution setup, REST API endpoints, business logic validation, JWT authentication, RBAC, payment gateway webhooks, and third-party integrations.

---

## 1. My Core Responsibilities
- **Solution Architecture:** Implement ASP.NET Core 8.0 Clean Architecture (`Domain`, `Application`, `Infrastructure`, `WebApi`).
- **Authentication & RBAC:** Student, Teacher, Admin roles (`BR-01`, `BR-02`, `BR-14`, `BR-21`). No client-side bypass.
- **Tuition Marketplace Engine:** Teacher class creation, schedule generation, booking transactions, seat capacity guards (`BR-03`, `BR-05`).
- **Payment & Ledgers:** Idempotent gateway webhooks, separate tuition GMV ledger from digital product ledger, payout calculations (`BR-06`, `C-06`, `16-FINANCE`).
- **API Matrix Compliance:** Implement endpoints listed in [UR_GURU_API_List_V6_0.xlsx](../../08-API-DOCUMENTATION/UR_GURU_API_List_V6_0.xlsx) (161 active endpoints).

---

## 2. Key References I Must Read
1. [`08-API-DOCUMENTATION/UR_GURU_API_List_V6_0.xlsx`](../../08-API-DOCUMENTATION/UR_GURU_API_List_V6_0.xlsx)
2. [`09-BUSINESS-RULES/UR_GURU_Business_Rules_V2_0.docx`](../../09-BUSINESS-RULES/UR_GURU_Business_Rules_V2_0.docx) (BR-001 to BR-077)
3. [`07-DATABASE-DESIGN/README.md`](../../07-DATABASE-DESIGN/README.md) (26 entities)
4. [`16-FINANCE/FINANCIAL_ARCHITECTURE_AND_LEDGER.md`](../../16-FINANCE/FINANCIAL_ARCHITECTURE_AND_LEDGER.md)
5. [`02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md`](../../02-BRD-AND-REQUIREMENTS/UR_GURU_BRD_V6_1_CORRECTED_BASELINE.md)

---

## 3. AI Starter Prompt (Copy-paste this when starting a new session)
```markdown
I am DEV_2 (Backend Developer) working on the UR GURU C# ASP.NET Core 8.0 Web API.
Workspace: D:\Unicom\UR_GURU_finalProject
Please read my context file:
UR-GURU-SECOND-BRAIN\19-CHAT-MEMORY\DEV_2\CONTEXT.md
And our database design:
UR-GURU-SECOND-BRAIN\07-DATABASE-DESIGN\README.md

Today I am implementing [NAME OF API / FEATURE / SERVICE].
Make sure all code follows Clean Architecture, strongly-typed DTOs, FluentValidation rules matching BR-001..077, and strict server-side state enforcement.
```

---

## 4. My Daily Work Log
Record daily activities in `WORK-LOG-YYYY-MM-DD.md`.
Log any API contract changes or new DTOs in `../SHARED-DECISIONS/CROSS-TEAM-LOG.md` so DEV_3 (Frontend) is updated.
