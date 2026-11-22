# BRD → API traceability

BRD v6.2.2 pages 4–7 and 11 define the functional scope and architecture mapping. The MVP workbook contains a `BRD Mapping` column per API; preserve that mapping when updating documentation.

| BRD | Concern | Expected module family |
|---|---|---|
| BR-01/02/21/22 | Identity, onboarding, safeguarding | Identity, Profiles, Safeguarding |
| BR-03/04/05 | Discovery, optional demo, classes, live | Catalog, Classes, Media, LiveSessions |
| BR-06 | Orders, refunds, earnings, payouts | Commerce, Payouts |
| BR-07 | Protected materials | LearningResources, Media |
| BR-11/18 | XACT question bank, practice, mocks | QuestionBank, Assessment |
| BR-19 | Teacher papers and assignments | Assessment |
| BR-20 | Explanation videos | Media, QuestionBank |
| BR-13/14/24 | Notifications, review, audit, support | Notifications, AuditReporting, Safeguarding |

**Check actual endpoint-to-BRD mappings in the workbook.** This table is module-level guidance, not a substitute for row-by-row validation. ERD v1.2 remains proposed and requires schema approval.
