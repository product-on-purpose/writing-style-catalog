---
entry_id: runbook
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# On-Call Triage: Daily Async Standup (#team-standup)

## Overview

Scan #team-standup for the day's posts, confirm every @mention has a substantive response, and escalate any unresolved blockers - run this once daily between 10am and 11am Pacific on any day you are the designated on-call engineer.

## Prerequisites

- [ ] You are listed as on-call for this week (confirm in #on-call-schedule)
- [ ] You have access to #team-standup in Slack
- [ ] You have 20-30 minutes available between 10am and 11am Pacific today
- [ ] You have checked the team calendar for any PTO that reduces today's expected post count

## Procedure

1. **Open #team-standup** and filter to messages posted since yesterday's triage session.
   Expected output: A set of posts from team members. The full team is 11 engineers across US Pacific, US Eastern, UK, and India timezones. Subtract anyone confirmed on PTO to get today's expected headcount.

2. **Tally posts against today's expected headcount.**
   Expected output: A count. If fewer than 80 percent of expected posts have arrived and it is past 10:30am Pacific, continue to step 3. Otherwise skip to step 4.

3. **Send a direct message to each engineer who has not posted.** Use this text: "Hey, no standup post yet today - any blockers?"
   Expected output: A reply or a channel post within the hour. If no reply after 60 minutes and the engineer is not on PTO, go to Escalation.

4. **Read every post in full.** Identify every @mention that appears inside a "Blocked or at risk" field.
   Expected output: A list (possibly empty) of @mentioned names tied to a specific blocker. Posts with no @mention in that field require no immediate action beyond step 6.

5. **Reply in thread to each @mention.** For each blocked item, respond with one of: a resolution, a diagnostic question, or a handoff naming the person who can unblock them.
   Expected output: Every @mention has a thread reply from you. Target completion within 30 minutes of your first read of the channel.

6. **Scan for "at risk" items with no @mention.** Identify any at-risk line where the engineer did not tag a resolver.
   Expected output: A list (possibly empty) of at-risk items with no owner named.

7. **Reply in thread on each unowned at-risk item.** Ask whether the engineer needs help and whether you should loop in a specific person.
   Expected output: A thread is open on every unowned at-risk item. You do not need to resolve it yourself at this step.

8. **Post a triage summary in #on-call-log.** Format: "Standup triage [date]: [N] posts received, [N] blockers found, [N] resolved, [N] escalated."
   Expected output: A message visible to the engineering manager confirming triage is complete for the day.

## Verification

Every @mention in today's #team-standup posts has a thread reply from you. Every at-risk item with no @mention has a thread reply asking whether help is needed. Your summary message is posted in #on-call-log.

## Rollback

Not applicable. Triage is a read-and-respond procedure with no reversible system state. If you replied to the wrong thread or gave incorrect guidance, post a correction reply in the same thread immediately.

## Escalation

- **Blocker you cannot resolve:** Tag the engineering manager in the thread with one sentence describing the blocker and why you are escalating.
- **Engineer unreachable after 60 minutes and not on PTO:** Send a direct message to the engineering manager with the engineer's name and last known context.
- **At-risk item that could affect the Thursday working session agenda:** Add it to `docs/thursday-agenda.md` and notify the engineering manager.
- **Process questions not covered here:** Check `docs/playbook.md` first. If still unresolved, ask in #on-call-schedule.
