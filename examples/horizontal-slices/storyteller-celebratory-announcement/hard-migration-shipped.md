---
entry_id: storyteller
axis: voice
topic_slug: hard-migration-shipped
topic_label: Celebrating the team shipping a hard migration
voice_id: storyteller
tone_id: celebratory
style_id: narrative-case-study
format_id: blog-post-long-form
author_type: llm
llm_model: claude-sonnet-4-6
review_status: draft
---

# The Migration Is Done

On Tuesday at 6:14 AM, Tomasz sent one message to the engineering channel: "old database is read-only."

Seven people across four time zones sent congratulations within four minutes. One sent a voice memo - fourteen seconds of clapping.

Eighteen months of work, landing.

## Before

In late 2022, Alloy ran on a PostgreSQL monolith in place since the company's second week. Every new feature had to negotiate with it before it could exist.

Schema change meant maintenance window meant downtime. Three to five migrations per quarter. The last one in Q3 2022 caused 22 minutes of unplanned downtime when a lock escalation blocked writes at peak. Forty-seven support tickets.

The deeper cost was slower. "Can we avoid a migration?" had become a real question in planning. Engineers were designing around the database instead of for users.

## The Turn

We decided to migrate to CockroachDB in February 2023. The constraint: we could not stop shipping while we did it.

Yuki built the dual-write layer - every change written simultaneously to both databases, old system remaining source of truth. It ran invisibly under every feature for six months. No user ever saw it.

The worst moment came in October 2023. A consistency check found 340,000 rows where the dual-write layer had dropped microsecond timestamp precision. Users wouldn't notice today; a compliance export in six months would. Three weeks of backfilling, no new features shipped. Preethi made that call without hesitation.

## What Shipped

Read-only flag at 6:14 AM. Health checks green across all three regions. By 7:00, Alloy ran entirely on CockroachDB.

No incident. No support ticket. No maintenance windows for the rest of the quarter - the new distributed database handles schema changes online.

First 30 days: 11 migrations, zero downtime, median 4 minutes. The old median was three days of coordination plus the window itself.

## The Principle

The migration is not interesting because of what it added. It is interesting because of what it removed - the tax the old system collected on every decision, and every engineer who learned to ask "can we avoid a migration?" instead of "what would serve the user."

The hardest things to ship are the ones nobody sees. The easiest to forget to celebrate.

We are not forgetting.
