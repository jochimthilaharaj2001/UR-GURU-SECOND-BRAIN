# Architecture Decision Candidate — 22 Nov 2026

**Not an approved ADR.** Proposed architecture: Angular responsive Student/Teacher + separate Admin, ASP.NET Core modular monolith, MySQL 8.4 LTS, Hetzner VPS/Ubuntu/Docker/Nginx. LiveKit Build and PayHere Lite are team choices subject to contract/operational gates. Cloudflare R2, Resend, FCM and monitoring are candidates.

**Reasoning:** lower startup operational complexity and cost; modular boundaries preserve clarity. **Risks:** single VPS failure, MySQL-specific EF Core compatibility, minors/privacy, financial correctness, LiveKit limits and PayHere Lite settlement/volume limits. **Pending:** named sponsor/engineering approvals, OD-05/06/16/20, ERD/DTO sign-off, performance, backups and UAT evidence.
