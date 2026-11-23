# MVP verification checklist — draft

- [ ] Map implemented endpoints to the 104-API register and BRD requirement IDs; document deferred gaps.
- [ ] Validate request/response DTOs, HTTP errors, RBAC and object ownership for each endpoint.
- [ ] Test student/teacher/admin flows including loading, empty, error and success states.
- [ ] Verify no demo watch requirement, trial booking, or demo-created entitlement.
- [ ] Verify payment webhook authentication, duplicate handling, seat limits and refund/ledger consistency.
- [ ] Verify live join authorization and session expiration.
- [ ] Verify XACT autosave, deadline enforcement, immutable scoring and duplicate submission.
- [ ] Validate subject selection constraints and no automatic paid enrollment.
- [ ] Run migrations against clean MySQL database and confirm actual DbContext/schema consistency.
- [ ] Test backup/restore, logs, alerting, secret handling and role-specific negative cases.
- [ ] Record UAT evidence and stakeholder approval; unchecked items are not passed tests.
