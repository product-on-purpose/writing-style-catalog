---
entry_id: status-report
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Status Report - Notification Service

**Period:** 2026-05-10 to 2026-05-16
**Author:** Ana Rivera (tech lead)
**Status:** Green

## Headline

Datastore decision (Postgres vs DynamoDB) concluded at Wednesday's architecture meeting; recommendation is Postgres, lock pending Friday 11am sync with Priya. Sprint planning Friday 2pm assumes lock-in, no slippage on the 6-week ship target.

## Done this period

- Completed the DynamoDB spike (`experiments/notify-ddb/`) - confirmed it fits the access pattern; documented the operational cost
- Ran the Wednesday 2pm architecture meeting with Ana, Marcus, Priya, Jordan, Sam; produced meeting notes and the draft ADR-0023
- Marcus and Ana aligned overnight on a single recommendation (Postgres) and the 5M events/day revisit threshold language
- Posted the recommendation to #notify-arch and emailed Priya for the Friday lock
- Drafted the notification service PRD with Priya (linked in ADR-0023)

## Up next

- Lock the datastore decision in the 2026-05-16 11am sync; mark ADR-0023 Accepted
- Sprint planning 2026-05-16 2pm to commit the first two weeks of build work
- Sam delivers `notifications` schema + `notification_jobs` table spec by 2026-05-20
- Jordan adds queue depth and write rate to the on-call dashboard by 2026-05-22
- First end-to-end internal traffic on the Postgres path by 2026-05-29

## Blocked / risks

- **Not blocked.** Marcus's sign-off on the revisit threshold is pending but I have his verbal agreement; written confirmation expected by EOD Thursday.
- **Risk - low:** If the Slack-partnership deal closes faster than the 12-month projection, we hit the 5M events/day revisit window earlier than planned. Mitigation: Priya tracks deal timing in the partnership review cadence and gives the team 30 days of warning. No action needed this period.
- **Risk - low:** Postgres partitioning work at the 3M events/day mark is real and on the roadmap. Owner: Ana. Currently scheduled for Q4 if growth tracks projection.

## Asks

- **Priya:** please confirm the 11am Friday sync is locked on the calendar.
- **Engineering leadership:** please review ADR-0023 by Monday so we can publish to the wider eng team and close the decision loop.
