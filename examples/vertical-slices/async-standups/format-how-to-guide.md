---
entry_id: how-to-guide
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to run an async standup trial for a distributed engineering team

## Before you begin

- You have a Slack workspace with a channel you can create or repurpose (#team-standup is this team's name)
- You have mapped each engineer's local timezone and know what the current sync standup time translates to on their clock
- You have a shared docs space for the trial retro and the Thursday agenda
- You know who is currently on the meeting facilitation rotation - that person becomes the first on-call channel reader

## Overview

This guide walks you through running a 30-day async standup trial. When you finish, you will have a running async standup channel with a posted template, a functional on-call reading rotation, a weekly working session replacing the old sync slot, and a retro framework for deciding whether to make the change permanent.

## Step 1: Map the timezone cost of your current standup

Before changing anything, you need to understand what problem you are solving. The sync standup imposes an unequal time burden across timezones, and that asymmetry usually stays invisible until you write it down explicitly.

List each engineer with their local timezone, then calculate what the current meeting time looks like on their clock. For this team, 9am Pacific is 9:30pm IST - a fact that shows up in attendance data as apparent disengagement rather than as a scheduling problem. The India engineers averaged 3.2 standup appearances per week while US engineers averaged 4.6. The gap is timezone cost, not commitment.

You have done this step when you can hand someone the timezone translation table and they understand immediately why the attendance numbers look the way they do.

## Step 2: Set up #team-standup with the three-field template

Create a dedicated Slack channel and pin a message at the top with the posting template:

```
Shipped:
 - <what landed since your last post>

In progress:
 - <what you are actively working on today>

Blocked or at risk:
 - <what is stuck, and who or what you need>
```

Also pin the house rules alongside the template: post by 10am your local time, @mention the person who can unblock you if you have a blocker, and write "nothing today" rather than skipping a field. If your Slack workspace supports it, configure a /standup shortcut that pre-fills the template.

You have done this step when at least three engineers can name the three fields without looking at the pin.

## Step 3: Define the on-call reading rotation

The async channel only functions if someone is accountable for ensuring blocked items get a response before end of business. That is the on-call reader role.

Assign it to the same engineers who currently facilitate the sync standup. Their new job: scan #team-standup between 10am and 11am Pacific each day, confirm that every @mention in a Blocked field has received a first response, and escalate anything unresolved. The role is triage, not editorial - they are not summarizing status or synthesizing updates. Budget 10 minutes per morning.

You have done this step when the first on-call engineer can explain their daily job without using the word "summarize."

## Step 4: Replace the sync meeting slot with a Thursday working session

Do not eliminate the meeting time without replacing the coordination and social functions it carries. The async channel handles status; the Thursday session handles everything that genuinely requires real-time exchange.

Schedule a 60-minute session on Thursday at the least-bad time across your timezone spread. For this team that is 8am Pacific / 8:30pm IST - a late evening for IST engineers, but once per week is a different burden from daily at 9:30pm. Keep a rolling agenda in a shared doc (docs/thursday-agenda.md). If the agenda is empty by Wednesday 5pm Pacific, cancel and give the time back.

You have done this step when the Thursday session fills with real discussion and the team stops calling it standup.

## Step 5: Frame the trial and set the retro date

A trial framing changes how engineers participate. When people know an experiment will be evaluated on explicit criteria, they engage with the process rather than waiting for it to be declared a success.

Send a team message naming the trial length (30 days), what you are specifically testing, the date of the retro, and where to drop observations mid-trial (docs/trial-retro.md). State clearly that if the retro data argues for reverting, you will revert. The trial only generates useful information if everyone believes you mean that.

You have done this step when someone asks "what happens at day 30?" and you can point them to the retro doc and the evaluation criteria without hesitating.

## Step 6: Track post completion and blocker resolution week by week

Collect weekly numbers so the Day 30 retro has something to compare. Two signals matter: post completion rate (posts received by the 10am local cutoff divided by posts expected) and blocker resolution time (minutes from @mention to first substantive reply in the thread).

This team's Week 2 results give you a reference point: on-time post completion at 85.5 percent (47 of 55 expected posts), median blocker resolution at 18 minutes. Those are not targets - they are what this team established. Collect your own numbers and compare them to your sync standup baseline.

You have done this step when you can walk into the Day 30 retro with two to three weeks of weekly numbers and a qualitative data point from each engineer.

## Troubleshooting

**Posts are getting too long.** If engineers are writing 200-word updates, the channel stops being skimmable in under 60 seconds. Share two exemplary short posts in the pinned message and reinforce the three-bullet ceiling at the Thursday session. The template fields are prompts for bullets, not headers for paragraphs.

**The on-call reader is over their time budget.** A 25-minute morning triage usually means blockers are surfacing earlier than the old sync model expected - which is actually the system working. Watch for another week before changing the rotation. If it persists, consider whether the on-call role needs a secondary backup rather than restructuring the whole rotation.

**Engineers are running decisions in post threads.** Async standup threads are for clarifications, not for the kinds of conversations that used to happen after standup. If you see a 10-message thread under a blocked item, add a house rule to the pin: threads for quick questions, everything else to a DM or Thursday agenda. Decision-weight conversations in a standup thread are a sign that the Thursday session needs a broader agenda or a lower cancellation threshold.

**A timezone cluster goes quiet.** Check whether the 10am local cutoff is achievable for that group. If their workday starts at or after 10am local, the cutoff is structurally impossible. Adjust the window for that cluster rather than treating low compliance as a participation problem.

## Next steps

At Day 30, run the retro against the criteria you set in Step 5. The quantitative data from Step 6 answers whether blockers are resolving faster and whether participation is more equitable across timezones. The qualitative signal from pre-retro 1:1s answers whether engineers feel the loss of daily sync contact.

If the retro supports making the switch permanent, record the decision in an ADR (see docs/rfc-async-standups.md for this team's original decision record). Update the #team-standup pin to remove the trial language and archive the old sync calendar invite.

If the retro argues against it, you have 30 days of data explaining exactly what failed. Use it to shape the next iteration rather than reverting to the baseline without a plan.
