---
entry_id: how-to-guide
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to Choose Between Postgres and DynamoDB for a New Service

## Before you begin

- You have a new service in design or early build, and it needs a persistent data store.
- You know your team's current operational footprint: which datastores you already run in production and who is on call for them.
- You have a rough estimate of your launch-day write and read volume, even if uncertain.
- You have a technical lead and a product owner who can sign off on the decision before build work begins.

## Overview

This guide walks you through the process the Lattice Notify team used to choose between Postgres and DynamoDB for their notification service. By the end, you will have a decision recommendation backed by a documented rationale, a revisit threshold, and a clear owner - ready to lock in before sprint planning.

## Step 1: Document the access pattern the new service actually needs

Before comparing databases, be specific about what your service will ask of its data store. Vague requirements ("high write volume," "fast reads") let both options look equal when they are not.

Write down the three most common operations your service will run: the shape of the write (one record per event, bulk inserts, etc.), the shape of the read (point lookup by user ID, range scan by time, cross-table join), and whether those operations are ever coupled in a single request.

For the notification service, Marcus documented this during the DynamoDB spike in `experiments/notify-ddb/`: writes are single-row inserts keyed by `user_id`, reads are point lookups to deliver to a user's inbox, and there are no ad-hoc scans at query time. DynamoDB fits this pattern well. Postgres requires a secondary index on `user_id` but handles it cleanly.

A successful outcome at this step is a one-paragraph statement you can read aloud in a meeting that describes the access pattern without using the word "normal."

## Step 2: Audit your team's operational capacity

Your database choice is not only a technical question - it is a staffing question. Adding a second datastore means a second runbook, a second monitoring surface, a second backup and restore story, and a second skill set every engineer on call must carry.

List what you already run in production and who owns the on-call procedures. Then calculate what adding the new option would cost: new documentation, new alerts, new training, and the cognitive overhead of debugging two systems instead of one.

The Lattice Notify team had 8 backend engineers and a 4-person on-call rotation already operating Postgres. Ana surfaced this at the Wednesday architecture meeting: the cost was not hypothetical - the team had measured it in a prior workstream. DynamoDB's access-pattern fit was real, but the operational cost of introducing it was equally real. Ana's point carried the meeting.

A successful outcome is a short list of the actual engineers who would carry the additional on-call burden, with an honest statement of whether that cost is absorbable at current headcount.

## Step 3: Scope your growth scenario and name the uncertainty in it

Pick the growth scenario you are designing for and be explicit about what has to be true for it to materialize. The common failure is designing for the large scenario when only the small scenario is certain - paying the complexity cost up front for a future that may not arrive.

Write down your launch-day volume and your 12-month projection, then name the external event that drives the gap. If the gap depends on a deal, a launch, or a partnership that has not closed, say so explicitly.

The notification service launched at 500K events per day. A 10x growth scenario existed if the pending Slack-partnership deal closed. Priya confirmed at the Friday lock sync that the deal had not closed. The team accepted Postgres for the certain scenario and documented a 5M events/day revisit threshold to trigger reconsideration when the uncertain scenario arrived.

A successful outcome is two rows: "Certain scenario: [volume]" and "Uncertain scenario: [volume, depends on: named event]."

## Step 4: Compare reversibility, not just fit

Both options are likely recoverable. Make that explicit. Knowing the migration cost in both directions changes the decision from "which is better" to "which direction is easier to undo if we are wrong."

Estimate the rework window if you choose option A and later need option B, and the rework window in the other direction. Include team-learning costs, not just code changes.

The Lattice Notify team put this at 3 to 6 weeks of rework in either direction. The asymmetry was small, which meant the operational cost surfaced in Step 2 could be the deciding factor rather than fear of lock-in. Neither choice was a trap.

A successful outcome is a sentence that starts: "If we choose X and are wrong, we pay approximately Y weeks of rework" for each option.

## Step 5: Make the recommendation and record a revisit threshold

Collect the outputs from the previous steps - access pattern, operational cost, growth certainty, reversibility - and write a single recommended option with a one-paragraph rationale. Include a specific metric at which the decision should be revisited. Not "when we get big," but a number with an owner.

The notification service team chose Postgres, with a `notifications` schema in the existing primary cluster, a `pg_notify`-backed job queue, and a `notification_jobs` table for worker tracking. The revisit threshold was 5M events/day sustained, tracked on the on-call dashboard owned by Jordan. Marcus signed off on the revisit threshold language by EOD Thursday. Priya recorded the final decision before Friday's 2pm sprint planning.

A successful outcome is an ADR (the notification service produced ADR-0023) accepted before the first sprint of build work begins.

## Troubleshooting

**The team cannot agree because both options look equally good.** This usually means the access-pattern analysis in Step 1 is still vague, or the growth scenario in Step 3 has not been separated from its dependencies. Return to those steps and force specificity. If genuine uncertainty remains, treat reversibility (Step 4) as the tiebreaker and choose the option the team can undo more cheaply.

**One team member has strong conviction for the option you are not choosing.** Do not smooth over the disagreement - document it. The ADR should record the competing view and explain why the deciding factor outweighed the fit argument. Marcus's case for DynamoDB appears in ADR-0023 even though Postgres won. A team member who sees their position accurately recorded is more likely to commit to the chosen direction than one whose argument was dismissed.

**You cannot get a decision-maker to lock the choice before build work starts.** This is a scheduling problem, not a technical one. Frame the cost: every week of build before the decision locks is potential rework. Put the decision meeting on the calendar first - the Lattice Notify team scheduled the Wednesday architecture meeting and the Friday lock sync before any schema work began.

## Next steps

- Draft the ADR and circulate it for review before sprint planning. ADR-0023 is the model for this scenario.
- Define the schema and queue for the chosen option. For the notification service, Sam owned the `notifications` schema and `notification_jobs` table spec, with delivery targeted by 2026-05-20.
- Add the revisit threshold metric to your monitoring dashboard. Jordan added queue depth and write rate to the on-call dashboard by 2026-05-22.
- Schedule first internal end-to-end traffic as a forcing function. The notification service targeted 2026-05-29 for first production traffic on the Postgres path.
