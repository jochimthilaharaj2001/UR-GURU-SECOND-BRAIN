# Decision register — resolve before treating blueprint as authoritative

| Area | Blueprint proposal | BRD v6.2.2 / earlier discussion | Action |
|---|---|---|---|
| Database | SQL Server / SSMS / EF Core (blueprint pp. 1, 14–19) | Earlier team discussion mentioned MySQL; BRD OD-20 leaves final database pending | Confirm actual selected DB; do not migrate yet |
| MFA | Excluded from seven-day feature scope (pp. 1, 7) | BRD pp. 4, 8 says privileged users should have MFA | Record production security gap; obtain approval |
| Resources | No revision/version history (p. 7) | BRD pp. 4, 6 requires resource revisions and provenance | Track deferred requirement explicitly |
| XACT content | External Exam Munnodi adapter; no local question authoring (pp. 1, 11) | BRD pp. 6–7 specifies approvals, translations and immutable versions | Verify provider capabilities and legal rights; document gap |
| Team capacity | Blueprint says two-person plan (pp. 2, 21) | Current project discussion proposes six members, 3 backend + 3 frontend | Reassign work from approved tracker |
| Prices | Rs.100/hour and 20% are examples (pp. 1, 18) | BRD OD-03/05 pending | Never hardcode example commercial rates |
| Live and payments | Provider integration conditional (p. 22) | Earlier discussion chose LiveKit Cloud Build and PayHere Lite | Verify provider contracts and sandbox capabilities |
| Scope | Seven-day internal demo subset | BRD v6.2.2 is wider and not signed | Preserve BRD as baseline, log deferred gaps |

**Do not overwrite** core architecture, BRD, API tracker or approved rules based solely on this PDF.
