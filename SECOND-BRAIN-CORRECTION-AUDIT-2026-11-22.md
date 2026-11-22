# UR GURU Second Brain correction audit — 22 November 2026

**Source:** uploaded `UR-GURU-SECOND-BRAIN.zip` and `UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`. Archive folder structure and original assets preserved. All corrections are documentation-level; **no code execution, vendor verification, approved DB migrations or UAT passes are claimed**.

## Corrected
1. Root README replaced with current scope and source hierarchy.
2. API source inventory counted from actual module files: **292 MVP**; draft DTO gaps tracked individually; Post-MVP 177 per index; deferred 52 not enumerated.
3. Legacy Exam Munnodi spec archived; active XACT gateway aligns to BRD R2/Bio/Maths.
4. LiveKit Build and PayHere Lite discussion choices recorded with explicit pending approval.
5. Database approval/migration gate added; no fabricated migrations.
6. MVP backlog populated with 292 proposed endpoint tasks and six-person *proposed* module split; 33 BRD UAT cases populated as **not executed**; 20 OD entries populated as **pending**.
7. Prior audit superseded; new SHA-256 file manifest added.

## Outstanding blockers (not safely fixable without decisions/evidence)
- All 292 endpoint-specific DTO/validation/error/status contracts need engineering and product sign-off.
- Missing authoritative list of 52 deferred endpoints; do not manufacture names.
- BRD remains an unsigned review candidate; OD-01–OD-20 require owner approval.
- DB engine, provider-specific schema and executable migrations not supplied.
- Vendor pricing/capabilities and compliance not independently verified.
- Real developer identity, estimates, start dates, test runs, CI/CD, deployment and release approval not supplied.
- Legacy supporting documents beyond corrected scope gateways may still contain historical wording; follow root source hierarchy, not stale claims.

## Validation
MVP parsed entries: **292** in **14** module files. Proposed backlog entries: **292**. UAT test definitions: **33**. Pending decisions: **20**. See `FILE-MANIFEST-SHA256.csv` for per-file integrity.
