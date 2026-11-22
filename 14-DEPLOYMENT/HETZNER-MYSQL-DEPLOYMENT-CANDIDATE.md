# Hetzner + MySQL Deployment Candidate

**Status:** Planning only. No credentials, provisioning, vendor quote, or production sign-off supplied. Reference: BRD v6.2.2 and Section 04 full technical architecture.

## Proposed topology
- HTTPS entrypoint: Nginx, DNS and TLS for Student/Teacher web, separate Admin web, and API.
- Application: Angular static assets, ASP.NET Core API container, optional background worker.
- Data: MySQL 8.4 LTS with persistent volume on private network; never publish port 3306.
- Integrations: LiveKit Cloud, PayHere Lite, Cloudflare R2; provider secrets kept outside Git.

## Release gates
1. Confirm Hetzner region, instance, IPv4, backups, bandwidth, tax and capacity estimate; no guaranteed user count without load test.
2. Configure least-privilege SSH keys, OS updates, firewall, TLS, secrets and admin MFA.
3. Validate MySQL provider, utf8mb4 collation, transaction isolation, unique constraints and migrations in staging.
4. Establish off-server encrypted point-in-time/backups as required, retention, restore drills and RPO/RTO evidence.
5. Configure CI build/test/scan -> staging deploy -> UAT -> approval -> production deploy and rollback.
6. Verify PayHere callbacks/idempotency, LiveKit join authorization, media access, XACT autosave/deadlines, safeguarding audit and incident alerts.

**Do not copy sample secrets, open MySQL publicly, or assume a one-VPS deployment is highly available.**
