# Git Collaboration Rules — Proposed

- Feature branches: `feature/devN-short-description`; merge by pull request into the agreed integration branch.
- DEV 3 and DEV 4 own separate student feature folders; coordinate changes to shared student routes, auth and shell.
- DEV 5 owns teacher feature UI; DEV 6 owns admin portal UI. Shared UI/API clients require review from their designated maintainer.
- DEV 1 and DEV 2 coordinate database migrations and shared backend contracts; no concurrent conflicting migrations.
- PR checklist: linked task/API ID, affected screens, loading/empty/error states, role/ownership checks, unit/integration tests, and no secrets committed.
- Changes to BRD, ERD, API contracts or security rules require designated owner review; do not silently rewrite controlled baselines.
- This ZIP excludes the source `.git` directory; retain the actual Git repository and history locally when applying these docs.
