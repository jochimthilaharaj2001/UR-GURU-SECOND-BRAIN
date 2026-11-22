# Privacy, Guardian Consent, Academic Rights and Content Rules

> **Document status:** DEVELOPMENT REFERENCE — BRD V6.2.2 is a consolidated review candidate, **NOT stakeholder-approved**. All derived rules remain subject to sign-off. The technical design and implementation contracts are not frozen.

## Scope and design caution
Guardian contact and consent touchpoints are allowed where required; **full guardian dashboard is future scope**. BRD V6.2.2 does not approve collecting NIC from all students, a fixed guardian age threshold or specific retention periods.

## Main rules
| Rule ID | Requirement (review baseline) | BRD source | Related UAT | Approval gate |
|---|---|---|---|---|
| UG-RULE-064 | Apply server-side role-based and object ownership/authorized-membership checks to protected operations; hiding UI alone is insufficient. | BRD §4 p.4 | AC-21 | Review baseline |
| UG-RULE-065 | Student must not read other students’ profiles, payments, results, resources or class assets without authorization. | BRD §4 p.4, §6.5 p.6 | AC-11, AC-21 | Review baseline |
| UG-RULE-066 | Guardian contact is used for consent/communications where legally applicable; no full guardian dashboard in current scope. | BRD §4 p.4, §2 p.3 | AC-04 | Review baseline |
| UG-RULE-067 | Where consent is legally required, preserve a revocable purpose-specific event, exact policy version and protected evidence. | BRD §6.1 p.5 | AC-04 | Pending policy OD-15 |
| UG-RULE-068 | Do not require NIC from every minor by default; NIC format validation is not government verification. | BRD §6.1 p.5 | AC-03 | Pending policy OD-19 |
| UG-RULE-069 | Restrict teacher identity/evidence, moderation notes and student viewing behavior from public listings or demo playback. | BRD §4 p.4, §6.2–6.3 p.5 | AC-06, AC-31 | Review baseline |
| UG-RULE-070 | Source reproduction, translations, adaptation, teacher media and demo videos must have documented rights before publication. | BRD §3 p.3, §8.1 p.6, §14 p.10 | AC-16, AC-31 | Pending policy OD-02/OD-07 |
| UG-RULE-071 | Separate public approved demo delivery from entitlement-gated private resources and XACT explanation assets. | BRD §6.3 p.5, §10 p.8 | AC-11, AC-31 | Review baseline |
| UG-RULE-072 | Avoid irreversible deletion of ledger entries, scored attempts and legally retained investigation data; use approved retention/archival rules. | BRD §10 p.8 | AC-20, AC-25 | Pending policy OD-15 |
| UG-RULE-073 | Child safety complaints must remain confidential, auditable and restricted to authorized safeguarding handlers. | BRD §4 p.4, §9 p.7 | AC-27 | Review baseline |
| UG-RULE-074 | Tamil/Sinhala/English scientific formulae, units, diagrams and answer options must be legible and accessible in supported browsers. | BRD §3 p.3, §11 p.8 | AC-28 | Review baseline |

## Cross-cutting acceptance
- URL guessing cannot access another student's private resource or attempt.
- Teacher/private guardian information must not leak into discovery or notifications.
- Consent withdrawal and rights withdrawal remain logged and access-controlled.
- Academic content versions are independently approved per medium.

## Open legal decisions
**OD-02**, **OD-07**, **OD-12**, **OD-15**, **OD-19**. Legal review is required for rights, consent thresholds, safeguarding and retention.
