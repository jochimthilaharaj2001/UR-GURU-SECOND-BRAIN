# Deployment readiness — pending verification

This is a checklist, not a claim that deployment is ready.

- [ ] Confirm target environments, infrastructure owner and secrets storage.
- [ ] Confirm ASP.NET Core/Angular builds and CI pipeline from the actual code repositories.
- [ ] Confirm MySQL 8.4 configuration, migration application, backups and tested restore.
- [ ] Configure TLS, CORS, RBAC, admin MFA and webhook verification.
- [ ] Configure LiveKit, PayHere and object storage using approved credentials and sandbox tests.
- [ ] Verify environment-specific URLs, storage access controls and audit/event logs.
- [ ] Run smoke tests, rollback rehearsal, load and recovery tests.
- [ ] Obtain operational, finance/legal and product sign-off as applicable under BRD v6.2.2.
