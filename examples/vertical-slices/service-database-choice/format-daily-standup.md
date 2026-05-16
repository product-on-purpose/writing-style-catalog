---
entry_id: daily-standup
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: 2026-05-16
review_status: reviewed
---

# Standup - Ana, 2026-05-14

**Done**
- Wrote up the operational-capacity case for Postgres ahead of yesterday's 2pm architecture meeting
- Walked Marcus through the on-call cost model; he agrees the framing is fair
- Posted the draft decision to #notify-arch for the wider team to react to before Friday

**Next**
- Finalize ADR-0023 (Postgres for notification service) for review today
- Spec out the `notification_jobs` schema and `pg_notify` listener for the Friday sprint plan
- 30-min sync with Priya at 11am to confirm the decision is locked for sprint planning

**Blockers**
- Need Marcus to sign off on the 5M events/day revisit threshold in the ADR before I mark it Accepted. Asked in #notify-arch; if no response by 3pm I will DM him directly. Priya needs the decision locked by EOD Friday so we do not slip the sprint.
