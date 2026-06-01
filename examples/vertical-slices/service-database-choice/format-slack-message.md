---
entry_id: slack-message
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Slack message - #notify-arch channel

**Posted by Ana, 2026-05-14 4:18pm**

> Recommending Postgres for the notification service. Need sign-off from Marcus and Priya by EOD Thursday so we can lock at Friday 11am and plan the sprint at 2pm.
>
> - Both options handle 500K events/day at launch. DynamoDB fits the access pattern better; Postgres fits our 4-person on-call rotation better.
> - Adding a second datastore at 8 backend engineers is the load-bearing concern. Marcus and I aligned on this last night.
> - Revisit threshold: 5M events/day sustained (covers the 10x Slack-deal scenario with ~3 months warning).
> - Full reasoning in ADR-0023 draft: https://wiki.latticenotify.com/adr/0023
>
> @marcus please confirm the revisit threshold language works for you. @priya please confirm the 11am Friday sync is locked. Thread for discussion.
