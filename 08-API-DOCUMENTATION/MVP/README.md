# UR GURU — MVP API Documentation (Proposed Contracts)

**Baseline:** UR_GURU_MVP_API_LIST_BRD_v6.2.2.xlsx (MVP APIs sheet) + UR_GURU_Full_Corrected_BRD_v6.2.2.pdf.

**Status:** DRAFT / CONTRACT REVIEW. API methods, endpoints, descriptions, roles, assignments and BRD mapping are transcribed from the source tracker. Request/response DTO shapes are NOT provided by that tracker or approved by the BRD; placeholders below must be completed and signed off before implementation. Do not treat placeholders as approved contracts.

**System:** Responsive Student and Teacher web applications; separate Admin web portal. Backend intended ASP.NET Core modular monolith (project direction, not signed BRD vendor choice). XACT is the assessment brand. Demo is an optional free prerecorded video; never a live trial booking. Subject selection is not enrollment.

## Shared contract conventions (engineering proposals, not BRD-approved)

- Base path is taken from tracker `/api/v1`; authenticate using server-verified identity and enforce object-level ownership/membership.
- Proposed success envelope: `{ "data": ..., "correlationId": "..." }`. This is a design proposal, not a guarantee.
- Proposed error envelope: `{ "error": { "code": "...", "message": "...", "details": [] }, "correlationId": "..." }`.
- Typical HTTP statuses: 200/201/204 success, 400 validation, 401 unauthenticated, 403 forbidden, 404 missing or concealed resource, 409 conflict, 422 business rule, 429 rate limit, 500 server error. Endpoint-specific status codes require review.
- Write operations affecting payments, enrollments, attempts, notifications and external providers must be assessed for idempotency, transactional integrity and audit logging.
- Never expose private file paths, sensitive personal data, payment credentials or other students' results.
- Public demo playback must not require booking, payment, enrollment or watch completion. XACT scoring and deadline are server-authoritative.

## Documentation workflow

1. Confirm BRD traceability and UI screen mapping for each API.
2. Approve request DTO, response DTO, validation and error codes.
3. Approve authorization matrix and data entity mappings.
4. Add example requests/responses and tests (positive, negative, permission, concurrency, idempotency).
5. Review architecture/ERD and record approval date and owner.

