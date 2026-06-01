---
entry_id: email
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Email - Database Decision Recommendation

**To:** Priya Shah <priya@latticenotify.com>
**Cc:** Marcus Chen <marcus@latticenotify.com>
**From:** Ana Rivera <ana@latticenotify.com>
**Date:** 2026-05-14 4:12pm Pacific
**Subject:** Notification service datastore - recommending Postgres, decision needed by Friday

Priya - recommending we go with Postgres for the notification service, and asking you to lock the decision in our 11am Friday sync so the team can plan next sprint.

Background: yesterday's architecture meeting compared Postgres (extend our current cluster, add a `pg_notify`-backed job queue) against DynamoDB (new datastore, better access-pattern fit for our 500K events/day launch load). Marcus and I aligned on a single recommendation overnight.

Why Postgres: our 8 backend engineers and 4-person on-call rotation already operate it at our scale. Adopting DynamoDB doubles the operational surface and we have no rollback plan if it goes wrong. The access-pattern advantage Marcus correctly identified is real but smaller than the operational cost at our current team size. We have a documented 5M events/day revisit threshold; if the Slack deal lands and we cross it, we have ~3 months of warning to plan a migration. Full reasoning is in ADR-0023 (draft) - link in #notify-arch.

What I need from you:
- Confirm the decision is locked at our 11am Friday sync so I can mark ADR-0023 Accepted before sprint planning at 2pm
- Confirm I should communicate the decision out to the broader engineering team in Friday's all-hands update

Happy to walk through the reasoning in detail before Friday if useful - I have a 30-min slot open at 9am or 1:30pm tomorrow.

Ana
