# Infrastructure & Deployment Design — Logical Proposal

**Status:** PROPOSED; cloud, vendor, service tier, locations, capacity and SLAs **PENDING OD-16/20**.  
**Baseline:** BRD v6.2.2 §§2, 10–11, 14.

## 1. Logical deployment

```text
[Browser: Student/Teacher]   [Browser: Admin]
            \                    /
                 HTTPS + DNS
                      |
                Edge / WAF  (proposed)
                      |
       [ASP.NET Core modular-monolith API]
                      |
        +-------------+------------+
        |                          |
  Relational DB                Private Object Storage
  (engine TBD)                 + approved CDN / public demo delivery
        |                          |
     Outbox/Jobs ------------------+
        |
   External adapters: payment, live room, video, messaging
```

**One backend deployable** may run multiple replicas. Optional outbox/media worker may run in-process or separately as the **same system**, with explicit version/transaction discipline; it is not automatically a new business microservice.

## 2. Minimum environment plan

| Environment | Intended use | Access and data |
|---|---|---|
| Developer local | Build + module/unit/integration tests | Synthetic/test accounts and mock provider responses |
| CI / ephemeral | Automated test/build/contract validation | No real payment/production credentials |
| Staging / UAT | Stakeholder tests, sandbox payment/video, restore rehearsal | Sanitized or synthetic data and role-separated test accounts |
| Production | Approved live service | Segregated secrets, backups, monitoring, release permissions |

Exact domain names, regions, account structure, database choice and infrastructure provider are **TBD**.

## 3. Deployment pipeline candidate

`Commit/PR → lint & compile → unit/architecture tests → dependency/security scans → integration/contract tests → immutable build artifact → staging deploy → migrations/backup gate → smoke/UAT → manual production approval → health/rollback verification`.

- Database migrations are reviewed artifacts; never auto-apply irreversible changes before backups and compatibility checks.
- Production deployment is not triggered by Codex documentation edit or AI-generated code without human approval.
- Keep environment variables and secrets in approved secret manager. Disallow secret files in Git.
- Configure rollback for binary changes, and forward/restore plan for DB changes. No assumed database downgrade.

## 4. Candidate availability & capacity targets **not approved**

BRD §11 proposes (not commits): p95 authenticated reads **under 1.0 s**, autosave acknowledgement **under 1.5 s** (under defined load); monthly platform availability **99.5%** excluding approved maintenance; RPO **≤60 min**, RTO **≤4 h** for database. Stress test at **2× expected** concurrent load.

Do **not** present these numbers as a contractual SLA. Sponsor, QA, Operations and engineering must approve workloads, measurement window and budget first.

## 5. Backups and recovery

- Database PITR/snapshot feasibility and schedule depend on selected database/provider.
- Separate encrypted backups for DB and versioned object storage/media; retention/deletion schedule requires privacy/legal review.
- Test restore into isolated staging regularly; verify ledger integrity, question snapshots and rights/consent evidence after restore.
- Document provider outage runbooks: payment pending/reconciliation, live room unavailable, media processing failures, notification backlog, XACT autosave degradation.
- Exercise incident communication and safeguarding escalation; audit access to incident evidence.

## 6. Network and secrets controls

- TLS everywhere; restrict database network access to the API/authorized job runners.
- Private source media and reviewer uploads should not be publicly enumerable; public demo media must be explicitly approved and distributed via controlled preview path.
- Segregate production/admin duties, enforce strong credentials/MFA, use short-lived tokens and rotate secrets.
- Logs and tracing must exclude raw payment data and minors' identity or exam answers unless strictly necessary and legally reviewed.

## 7. Monitoring and alerts

Minimum signals: API error rate/latency, auth failures, seat capacity conflicts, payment callback rejection/lag, ledger reconciliation mismatch, entitlement issuance, live join failure, media processing/review backlog, XACT autosave/submit failures and deadline exceptions, notification retries, consent/safety escalation. Page on failures with approved thresholds, not invented in document.

## 8. Release-readiness gate

- [ ] OD-16/20 approved hosting, DB choice, region, capacity, measurable SLO targets.
- [ ] OD-02/05/06/07 and legal rights/vendor contracts approved as required.
- [ ] Tested pipelines, rollback/restore rehearsal and security configuration.
- [ ] Access isolation and consent/retention policy signed.
- [ ] Critical UAT AC-01–33 evidenced; approved R1/R2 release sequence (OD-18).

**Related:** [`Technology-Stack.md`](./Technology-Stack.md), [`Reliability-Observability-and-Testing.md`](./Reliability-Observability-and-Testing.md), [`../14-DEPLOYMENT/`](../14-DEPLOYMENT/).
