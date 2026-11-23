# Engineering Rules — Proposed

Source: Blueprint pages 8–23.

1. Preserve existing solution/repositories and modular monolith; do not rebuild starter code without inspection.
2. API base `/api/v1` is a proposal; reconcile endpoints, DTOs and OpenAPI with actual implementation.
3. Server-side role and object-level authorization. Never rely on hiding frontend elements.
4. Verify payment webhooks; protect against replay, duplicate settlements and overbooking. Batch cap proposed at 20.
5. Paid enrollment/entitlement only after verified payment; demo video is free and optional.
6. Private teacher NIC documents, learning resources and protected live join tokens; never commit secrets.
7. XACT uses licensed Exam Munnodi API data; do not expose answer keys before submission or invent difficulty metadata.
8. UTC storage, Asia/Colombo display, stable validation errors, idempotent autosave and submissions.
9. SQL migrations only after inspecting actual DbContext, entities and existing migrations.
10. Seven-day target is an internal demo. Production release requires security, child-safety, privacy, payment and recovery gates.
