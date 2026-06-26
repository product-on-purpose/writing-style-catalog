---
entry_id: question-and-answer
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## What does Priya need to actually do work on Day 1?

Access first, then context. Before she arrives, provision her accounts for the code host, the deployment system, the chat tool, and the ticket tracker. Nothing stalls a first day like waiting on an approval chain that could have been handled the Friday before.

Day 1 ends when she can pull the main repository, run the service locally, and read recent deploys. She does not need to understand the codebase yet - just know where it lives and that her machine can reach it.

## When should she write her first line of production code?

By the end of day three, if possible. The instinct to protect a new engineer with a long orientation usually backfires. A week of reading documentation and sitting in meetings without touching anything erodes confidence without building it.

Pair her on a small change in week one: a configuration fix, a test gap, a logging line. Size does not matter. What matters is that she opens a pull request, gets feedback, and watches it deploy. That cycle, experienced once, is worth more than a day of orientation. (See "How do I pick her first solo task?" for her week-two target.)

## How do I pick her first solo task?

Look for a change that is small, self-contained, and genuinely useful - not a cleanup task invented for training purposes. Engineers can tell the difference, and it matters to them.

Good candidates: a missing error message that real users hit, a test that was skipped when the code shipped, a small behavior a bug report flagged and nobody got to. Bad candidates: anything requiring context across three services, anything on the current sprint's critical path.

Assign it by end of week one so she can ask questions that actually matter while you are still pairing.

## When does she join on-call, and how do I prepare her?

Not in week two. On-call requires knowing what to do when things break, and that knowledge only comes from having shipped a few things first.

The right preparation is a written runbook she can read in advance, a shadowing shift where she watches someone else handle a page, and one explicit conversation about who to call at 2am if she is stuck. That conversation matters more than the runbook. A reasonable target for her first solo shift is six to eight weeks in.

## How do I know if she feels like she belongs, not just functions?

Watch for whether she volunteers opinions in planning meetings, asks questions that are not purely task-related, and says "we" when talking about team decisions. An engineer who belongs speaks as a member; one still arriving speaks as a visitor.

If those signals are absent by the end of week two, do not wait. Have the direct conversation: what is unclear, what feels uncomfortable, who she has not met yet. The social side often stalls not from hostility but from nobody explicitly making room.
