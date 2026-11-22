# Open Requirements and Approval Decisions — BRD v6.2.2

> **UR GURU Second Brain — Development reference**  
> Source: [`UR_GURU_Full_Corrected_BRD_v6.2.2.pdf`](./UR_GURU_Full_Corrected_BRD_v6.2.2.pdf), consolidated corrected edition, 19 November 2026.  
> **Document status:** DRAFT EXTRACTION from BRD v6.2.2; source itself is a **review candidate pending stakeholder sign-off**.  
> **Use:** Requirements analysis / development planning; not independent approval or an executed test record.

## Why these decisions are open

The source BRD states **stakeholder sign-off still required**, product owner **TBD**, and ERD v1.2 **proposed** (pp. 1, 8, 11–12). It does not approve pricing, providers, guardian policies, copyright, NIC checks, demo-rights rules, database engine or launch order. **All listed items remain `PENDING APPROVAL` unless a separate signed decision is supplied.**

## Official open decision register (OD-01–OD-20)

| ID | Decision required | Suggested owner (BRD) | Potential impact | Status |
|---|---|---|---|---|
| OD-01 | Teacher evidence and screening policy | Product / Legal / Operations | R1 teacher approval | PENDING APPROVAL |
| OD-02 | Demo rights/ownership, upload/approval SLA, public preview rules, free duration/count and optional viewer analytics/consent | Product / Legal / Operations | R1 DemoVideo | PENDING APPROVAL |
| OD-03 | Commission rate/base, taxes, charges and revenue recognition | Sponsor / Finance | R1 financial calculations | PENDING APPROVAL |
| OD-04 | Refunds, partial refunds, dispute, earnings and payout rules | Finance / Legal | R1 finance + cancellations | PENDING APPROVAL |
| OD-05 | Payment provider, callbacks, settlements, recurring features and quotation | Finance / Engineering | R1 checkout/payments | PENDING APPROVAL |
| OD-06 | Live classroom, demo/CDN provider, recording permissions and cost envelope | Engineering / Product / Finance | R1 live/media services | PENDING APPROVAL |
| OD-07 | Question reproduction/translation/adaptation and teacher video rights | Legal / Academic | R2 XACT launch | PENDING APPROVAL |
| OD-08 | Five-year question inventory by subject, topic, language and diagram coverage | Academic Lead | R2 content coverage | PENDING APPROVAL |
| OD-09 | Academic answer-key/video review and correction/regrade SLA | Academic Lead | R2 governance and scoring | PENDING APPROVAL |
| OD-10 | Mock timers, marks, attempts, negative scoring, expiration and answer reveal | Academic / Product | R2 exam behavior | PENDING APPROVAL |
| OD-11 | Difficulty/topic quotas and translated-option QA | Academic | R2 mock generation | PENDING APPROVAL |
| OD-12 | Teacher explanation-video compensation, IP ownership, withdrawal and revenue sharing | Finance / Legal | R2 teacher media | PENDING APPROVAL |
| OD-13 | XACT free allowance, packs/subscriptions and pricing | Sponsor / Finance | R2 monetization | PENDING APPROVAL |
| OD-14 | Future native applications, institutions and teacher Pro features | Sponsor / Product | Future | PENDING APPROVAL |
| OD-15 | Minor thresholds, guardian permissions, PDPA/privacy and retention | Legal / Safeguarding | R0 privacy and operations | PENDING APPROVAL |
| OD-16 | Staffing, release dates, cloud budget, capacity and NFR SLA | Sponsor / PM / Engineering | All release approvals | PENDING APPROVAL |
| OD-17 | XACT brand and Bio/Maths first; later streams | Product Owner | Current scope sign-off | PENDING APPROVAL |
| OD-18 | R1/R2 production sequence versus existing XACT pilot | Sponsor / Product Owner | Release sequencing | PENDING APPROVAL |
| OD-19 | NIC need, official verification route, alternatives and retention | Product / Legal | R0 identity | PENDING APPROVAL |
| OD-20 | Final web/backend/database selections, environments and ERD v1.2 schema approval | Engineering / Sponsor | Architecture/migrations | PENDING APPROVAL |

## Specific unresolved implementation questions called out in the BRD

| Question | Why it must not be assumed | Source | Suggested linked decision |
|---|---|---|
| Must a prospective demo viewer log in, or is anonymous free viewing allowed? | The BRD explicitly leaves viewer login/access and privacy sign-off open. | §6.3, p. 5 | OD-02, OD-15 |
| How is a real student identity verified, and is NIC required for minors? | NIC pattern validation is not government verification; minors must not be forced by default. | §6.1, p. 5 | OD-19 |
| What Bio/Maths subject combinations are eligible? | Academic Lead must approve exact allowed combinations. | §3, p. 3 | OD-17 / Academic Lead review |
| Which approved languages have available content for each syllabus subject? | No automatic fallback to an unapproved language. | §3, pp. 3, 6 | OD-08, OD-11 |
| What is the actual approval-ready ERD and SQL schema? | ERD v1.2 and DDL rules are proposed; types/FKs/unique constraints need technical sign-off. | §10, Appendix C, pp. 7–8, 12 | OD-20 |
| Can XACT launch before marketplace R1? | BRD expressly retains marketplace-first dependency pending a different approved decision. | §2, p. 3 | OD-18 |
| What are official autosave/reconnect, grading and deadline parameters? | Mechanism is defined, configurable timer/grace/attempt details are not finalized. | §8.2, pp. 6–7 | OD-10 |
| What is the guardian consent and retention policy? | Requires legal/purpose-specific decision and evidence rules. | §6.1, §10, pp. 5, 7–8 | OD-15 |

## Decision management procedure

For each approval, capture: decision ID, approved choice, affected BR/AC IDs, approver, role, date, contract/policy version, impact on UI/API/DB/tests, residual risks and a link to signed evidence. Only then set status to APPROVED and update downstream documents. Do not infer approvals from a prototype, ERD candidate or this extracted register.

**Current open statuses above are transcribed from the uploaded BRD review candidate, not checked against any later signed records.**
