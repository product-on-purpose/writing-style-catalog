---
entry_id: meeting-agenda
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Notification Service - Database Decision - Wednesday 2026-05-13
Time: 2:00 PM - 3:00 PM | 60 min
Location / Link: https://meet.latticenotify.com/notify-arch-0513
Attendees: Ana Rivera, Marcus, Priya, Jordan, Sam

## Agenda

1. DynamoDB spike readout (15 min) - discuss
   Marcus walks through experiments/notify-ddb/ findings: write-heavy access pattern fit, read consistency model, and the operational surface that comes with adopting a net-new datastore on a 4-person on-call rotation.

2. Postgres path overview (10 min) - discuss
   Ana covers the proposed schema (notifications), pg_notify job queue, read replica plan, and the 5M events/day revisit threshold where we would reconsider.

3. Operational cost comparison (10 min) - discuss
   Side-by-side: on-call runbooks, monitoring surface, incident debugging, and team DynamoDB ramp time versus existing Postgres familiarity. The 4-person rotation is the binding constraint; this item surfaces the numbers.

4. Datastore decision: Postgres or DynamoDB (20 min) - decide
   Group works to a single recommendation for Priya to lock in the Friday 11am sync. If consensus arrives early, use remaining time to assign draft owners for ADR-0023.

5. Wrap and owners (5 min) - update
   Confirm who writes the ADR-0023 draft, who circulates the Friday lock invite, and when Marcus posts written sign-off to #notify-arch.

## Pre-reading

- DynamoDB spike notes: experiments/notify-ddb/README.md
- Draft ADR-0023 context section (Ana posting to #notify-arch by Tuesday EOD)
- Notification service PRD (from Priya, in #notify-arch)

## Questions or additions

Add agenda items to #notify-arch by Tuesday 5 PM or DM Ana Rivera.
