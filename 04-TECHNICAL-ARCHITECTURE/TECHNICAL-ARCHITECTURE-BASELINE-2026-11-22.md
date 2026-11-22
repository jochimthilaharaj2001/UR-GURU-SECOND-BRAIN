# UR GURU — Technical Architecture Alignment (22 November 2026)

**Status: TEAM-SELECTED ENGINEERING DIRECTION / PROPOSED — NOT PRODUCTION-APPROVED.**
**Sources:** BRD v6.2.2 (controlled review candidate) and `UR_GURU_Complete_Technical_Architecture_v1.0.docx` (design candidate). This note reconciles the newer engineering choices with the older Second Brain; it does not approve OD-20 or rewrite BRD requirements.

## Current engineering direction
| Concern | Direction | Approval |
|---|---|---|
| Student/Teacher responsive web | Angular | Engineering selection; OD-20 pending |
| Separate Admin web | Angular, separate deployment | Engineering selection; OD-20 pending |
| Backend | C# ASP.NET Core modular monolith | Engineering selection; OD-20 pending |
| Database | MySQL 8.4 LTS Community Edition, InnoDB | User-selected; schema/provider compatibility tests and OD-20 pending |
| Data access | EF Core with MySQL-compatible provider | Validate EF Core/provider version compatibility before migrations |
| Hosting | Hetzner Cloud VPS, Ubuntu Linux | Recommended candidate; OD-16/20 pending |
| Reverse proxy / deployment | Nginx, Docker Compose | Engineering candidate |
| Live classes | LiveKit Cloud Build | Team selection; OD-06 contract/cost/security pending |
| Payments | PayHere Lite | Team selection; OD-05 settlement/refund/limit/fee review pending |
| Media storage | Cloudflare R2 | Recommended candidate; rights/access/CDN design pending |
| Email / push | Resend / Firebase Cloud Messaging | Recommended, not approved |
| Monitoring | Sentry / Uptime Kuma | Recommended, not approved |

## Logical deployment
Browsers -> HTTPS/Nginx -> two Angular web channels + ASP.NET Core modular monolith -> private MySQL. Backend integrates with LiveKit, PayHere, Cloudflare R2 and messaging adapters. Paid media uses backend authorization and short-lived links; approved free demos have separate preview access. MySQL must never be exposed publicly.

## Physical design safeguards
- One MySQL database is a startup proposal, **not** an approved ERD/DDL. Use InnoDB transactions, explicit unique/FK constraints, utf8mb4 and verified collation choices, consistent UTC handling, migrations and separate module ownership.
- Verify EF Core/MySQL provider compatibility, transaction semantics, locking for seat reservations, concurrency/idempotency and append-only financial ledger before migrations.
- Use persistent database volumes, off-VPS encrypted backups, restore drills, secret management, TLS, role + ownership checks and CI/CD environment gates.
- XACT immutable question/key snapshots, server timers/autosave, optional free demo and StudentSubject != Enrollment remain non-negotiable BRD rules.
- Proposed RPO <=60 minutes and RTO <=4 hours are candidate NFRs, not promises.

## Source conflict handling
Older SQL Server/PostgreSQL alternatives, SQL Server team assignments and infrastructure-neutral wording in this repository are **historical/provisional**, not current selected engineering direction. Existing diagrams and schema catalogs remain **logical candidates**, not validated MySQL physical schema. Do not silently mass-replace database syntax in DDL, CSV, DBML, API docs or images.

## Required follow-up approvals
OD-20 stack/ERD; OD-16 hosting, capacity and NFR; OD-05 payment; OD-06 live/media; OD-02 demo rights; OD-15 privacy; final API DTO contracts, migration tests, deployment readiness and UAT. No claim that 292 MVP APIs are implementation-ready until request/response DTO gaps are resolved.
