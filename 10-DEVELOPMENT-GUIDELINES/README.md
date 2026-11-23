> **Controlled-document rule:** DEV_2 is the final approver for changes to important Second Brain baseline documents, excluding `19-CHAT-MEMORY/`. See [Document Access Control Policy](DOCUMENT-ACCESS-CONTROL-POLICY.md) and [Git Branching and PR](Git-Branching-and-PR.md). GitHub branch rules must be configured separately.

# 10-DEVELOPMENT-GUIDELINES

**Purpose:** Shared coding, repository and review conventions.

**Status:** Required deliverables checklist — filenames are proposed; create each real file after its owner starts work.

| Needed file | Minimum contents | Status |
|---|---|---|
| `Repository-Structure.md` | Frontend, backend, database/migrations, docs directory conventions | ☐ Not supplied / verify |
| `Coding-Standards.md` | C# and TS linting, naming, validation, logging, error handling | ☐ Not supplied / verify |
| `Git-Branching-and-PR.md` | Branches, commit naming, PR checks, review/merge policy | Draft added; DEV_2 approval pending |
| `Local-Setup.md` | Developer prerequisites, env variables names, sample data, commands | ☐ Not supplied / verify |
| `Definition-of-Done.md` | Code review, tests, docs, API/DB updated, signoff | ☐ Not supplied / verify |
| `Secrets-and-Security.md` | No credentials in repo, permissions, reporting vulnerabilities | ☐ Not supplied / verify |

## Rules for this folder

- Do not mark a planned document as completed until its actual content is reviewed and version-controlled.
- Add owner, approval status, version/date and cross-references to the appropriate BRD requirements.
- Link to the canonical document instead of creating conflicting copies.
- When a policy or provider is pending, write `PENDING APPROVAL` rather than assuming a final value.
