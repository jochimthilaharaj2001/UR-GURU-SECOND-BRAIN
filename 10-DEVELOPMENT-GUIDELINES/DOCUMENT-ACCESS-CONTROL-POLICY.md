# DOCUMENT ACCESS CONTROL POLICY — DEV_2 Approval Authority

**Version:** 1.1 | **Date:** 2026-11-23 | **Status:** Team policy draft — DEV_2 approval assigned by project instruction; repository administrator must enable GitHub enforcement.

## Scope and authority

This policy governs changes to **controlled project baseline documents** in UR GURU Second Brain. **DEV_2 (Document Control Owner)** is the sole final approver and merger of controlled-document changes. DEV_1 and DEV_3–DEV_6 may propose changes through a pull request, but may not directly modify approved baselines on the protected default branch. This is an approval restriction, not a ban on submitting corrections.

**Exception:** `19-CHAT-MEMORY/` is outside this DEV_2-only controlled-document restriction. Each developer may maintain their own `DEV_X/` work logs and context; shared decisions still require coordination. Other repository permissions and privacy rules remain applicable.

## Folder rules

| Folder | Controlled baseline change | Routine developer contribution |
|---|---|---|
| `01-PROJECT-OVERVIEW/` | DEV_2 approval required | Propose via PR |
| `02-BRD-AND-REQUIREMENTS/` | DEV_2 approval required; stakeholder sign-off remains separate | Review/comment via PR |
| `03-SYSTEM-ARCHITECTURE/` | DEV_2 approval required | Propose via PR |
| `04-TECHNICAL-ARCHITECTURE/` | DEV_2 approval required | Propose via PR |
| `05-USER-JOURNEYS/` | DEV_2 approval required for approved journeys | Drafts via PR |
| `06-UI-UX-DESIGN/` | DEV_2 approval required for approved UI baseline/mappings | Draft designs via PR |
| `07-DATABASE-DESIGN/` | DEV_2 approval required for ERD/schema/migration baseline | Migration proposals via PR |
| `08-API-DOCUMENTATION/` | DEV_2 approval required for approved API inventory/contracts | API drafts via PR |
| `09-BUSINESS-RULES/` | DEV_2 approval required | Propose via PR |
| `10-DEVELOPMENT-GUIDELINES/` | DEV_2 approval required | Propose via PR |
| `11-SPRINT-AND-TASKS/` | DEV_2 approval for scope/ownership/baseline plans | Assigned task status updates via PR |
| `12-TESTING/` | DEV_2 approval for approved UAT/acceptance baseline | QA evidence/test drafts via PR |
| `13-DECISION-LOG/` | DEV_2 approval for accepted ADRs and decisions | Decision proposals via PR |
| `14-DEPLOYMENT/` | DEV_2 approval for production configs/release policy | Runbook drafts via PR |
| `15-ISSUES-AND-CHANGELOG/` | DEV_2 approval for controlled change records | Issue entries via PR |
| Other non-memory folders | DEV_2 approval for approved project baselines | Assigned work via PR |
| `19-CHAT-MEMORY/` | **Excluded from DEV_2-only policy** | Each developer edits own DEV_X folder; shared entries coordinated |

## Mandatory workflow

1. Developer creates `feature/...` or `docs/...` branch; never pushes directly to protected `main`.
2. Open PR describing affected files, BRD requirement IDs, API/UI/DB/test impact and reason for change.
3. DEV_2 reviews and approves controlled changes; DEV_2 performs/authorizes merge.
4. BRD, legal, finance, product or architecture decisions needing stakeholder sign-off **still need that sign-off**; DEV_2 cannot replace it.
5. Update decision log, affected cross-references, version and changelog when approved.
6. Emergency fixes follow the same recorded approval path; repository administrators must not silently bypass protection.

## GitHub enforcement (administrator setup required)

- Replace `@REPLACE_WITH_DEV1_GITHUB_USERNAME` in `.github/CODEOWNERS` with DEV_2's actual GitHub username/team; until then ownership is a **placeholder**, not enforceable.
- Enable branch protection/ruleset for `main`: require pull request, require code owner review, block force pushes/deletions, dismiss stale approvals, restrict bypass actors and direct pushes, and require passing checks where configured.
- Configure repository permissions so other developers cannot bypass the protected branch. GitHub ruleset features and available restrictions depend on repository plan/organization settings.
- **CODEOWNERS alone does not block edits or merges.** Only correctly configured GitHub permissions + branch rules provide enforcement.
- Do not commit `.git/` history/configuration in shared ZIP distributions.

## Current scope safeguard

BRD v6.2.2 remains the controlled requirements reference; the 104 API MVP list is an implementation scope and must not be mistaken for deletion of deferred BRD requirements. API/DTO/schema/UI coverage changes need explicit impact review.
