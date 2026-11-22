# API Standards — Proposed, Pending Approval

- Versioned base prefix `/api/v1` follows the supplied tracker.
- Server enforces roles **and** resource ownership/membership. Hiding a UI control does not authorize access.
- Proposed success envelope: `{ "data": ..., "correlationId": "..." }`.
- Proposed error envelope: `{ "error": { "code": "...", "message": "...", "details": [] }, "correlationId": "..." }`.
- Standard HTTP statuses to review: 200, 201, 204, 400, 401, 403, 404, 409, 422, 429, 500.
- Payments, enrollment, refunds, XACT attempts and provider callbacks need explicit idempotency, audit and transaction rules.
- Gateway callbacks must be authenticated/revalidated before entitlements activate; the ledger is append-only.
- Exam deadlines, autosave and scoring are server-authoritative and version-snapshotted.
- Private resources use authorized short-lived links. Public approved demo previews do not expose source keys or paid content.
- No automatic language fallback for unapproved translations.

**These are working conventions, not BRD-approved DTO contracts.**
