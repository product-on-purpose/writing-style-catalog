---
entry_id: readme
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# team-standup

A lightweight async standup process for distributed engineering teams. Built for the 11 of us spread across 4 timezones.

## Why this exists

Our sync standup at 9am Pacific meant 9:30pm IST for half the team. Attendance averaged 3.2/5 in India and 4.6/5 in the US. The 14-minute meeting produced roughly 4 minutes of signal, and none of it persisted beyond the call. This repo is the running process docs for the replacement.

## Quick start

If you joined the team today, here is the entire ritual:

1. Before 10am local time, post one message to `#team-standup`.
2. Use the three-field template (copy from below or use the `/standup` Slack shortcut).
3. If you are blocked, `@mention` the person who can unblock you in the same message.

That is it. No call. No status round-robin. No "I will let X speak to that."

## The template

```
Shipped:
 - <what landed since your last post>

In progress:
 - <what you are actively working on today>

Blocked or at risk:
 - <what is stuck, and who or what you need>
```

If a field is empty, write "nothing today." Skipping a field is fine on Fridays.

## How to read the channel

The on-call engineer scans `#team-standup` once between 10am and 11am Pacific. Their job is not to summarize; it is to make sure every `@mention` has a response within the workday. Anything not at-risk gets a thread reply only if a teammate has questions.

## The Thursday working session

The 60-minute slot that used to be 5 sync standups is now a single Thursday working session at 8am Pacific / 8:30pm IST. Agenda lives in `docs/thursday-agenda.md`. If there is nothing to discuss, we cancel by Wednesday 5pm Pacific.

## Trial period

We are running this for 30 days starting on the date of the v2.0 changelog entry. The retro doc is `docs/trial-retro.md`. If you have a strong opinion mid-trial, drop it there instead of in DMs.

## Links

- Process playbook: `docs/playbook.md`
- Trial retro: `docs/trial-retro.md`
- Slack channel: `#team-standup`
- Original RFC: `docs/rfc-async-standups.md`

## Maintainer

Engineering manager owns this repo. Pull requests welcome from any team member.
