---
entry_id: proposal
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Async-First Standup Adoption
## Prepared for: Director of Engineering
## Prepared by: Engineering Manager
## Date: Q2 (before trial launch)

## Executive Summary

The engineering team's daily synchronous standup puts India-based engineers in a 9:30pm meeting, produces roughly 4 minutes of actionable signal in 14 minutes of call time, and leaves no searchable record of anything shared. This proposal recommends replacing it with a daily async update posted to `#team-standup` by 10am local time, paired with a weekly 60-minute Thursday working session at 8am Pacific (8:30pm IST) for discussions that require real-time exchange. Your approval is the single action needed to begin a 30-day trial with a structured retro at Day 30.

## The Problem

Your 11-engineer team now spans four timezones: US Pacific, US Eastern, UK, and India. The daily standup runs at 9am Pacific. For India-based engineers, that is 9:30pm local time.

Three costs are accumulating.

**Participation gap.** Q1 attendance data shows India-based engineers averaged 3.2 standup appearances per week out of 5, compared to 4.6 for US-based engineers. The gap is not disengagement; it is the clock.

**Signal loss with no durable record.** The standup averages 14 minutes. Roughly 4.2 minutes of that meeting changes someone's behavior - a blocker raised, a dependency flagged, a context shared. The remaining time is status that required no response from anyone. None of it is searchable afterward. Three incidents in the past quarter involved an engineer spending more than an hour on a problem that had already been solved and discussed in a prior standup. There was no record to check.

**Unequal burden.** A 14-minute meeting looks equal on paper. A 9:30pm mandatory call is not. The current format asks one group on the team to make a categorically different sacrifice than everyone else.

## Proposed Approach

Replace the synchronous standup with a daily async update posted to `#team-standup`. Each engineer posts by 10am their local time using a three-field template:

- **Shipped:** what completed in the last 24 hours
- **In progress:** current focus
- **Blocked or at risk:** anything that needs attention, with an @mention of the person who can resolve it

The on-call engineer - on the existing rotation - reads the channel by 9am Pacific and responds to any @mentions within 30 minutes during business hours. This replaces the meeting-facilitation duty the on-call already carries; no new role is created.

The synchronous slot is not simply removed. It converts into a 60-minute Thursday working session at 8am Pacific (8:30pm IST) for discussion that genuinely requires real-time exchange: architectural questions, live debugging, or issues a Slack thread cannot carry. If there is nothing to discuss by Wednesday at 5pm Pacific, the session is canceled.

This approach fits your team specifically because your four-timezone spread makes any single fixed synchronous slot inequitable, and your existing Slack infrastructure handles the async format without additional tooling. Geekbot and similar tools were evaluated and rejected: they add cost and tooling complexity that a pinned Slack template covers at no cost.

## Scope and Deliverables

**Included:**
- Process documentation pinned to `#team-standup`
- A three-field Slack message template, accessible via pinned message and a `/standup` Slack shortcut
- On-call reading responsibility added to the existing on-call rotation charter
- A 30-day trial period with weekly participation tracking
- A structured Day 30 retro document covering quantitative data (post completion rate, blocker resolution time) and qualitative feedback collected in 1:1s with each engineer

**Not included:**
- Any paid tooling or new Slack applications
- Changes to sprint ceremonies, retrospectives, or project tracking in Jira
- Any standup-adjacent process outside the daily update and the Thursday replacement session

## Timeline

- **Week 0 (3 business days from your approval):** Engineering manager finalizes process documentation, pins the Slack template, updates the on-call charter, and briefs the team at a single 30-minute sync call. Trial start date announced.
- **Day 1:** Trial begins. All engineers post their first async update. On-call engineer begins daily channel triage.
- **Week 2:** First pulse check on participation rate and median blocker resolution time against the Q1 sync baseline.
- **Day 30:** Full retro. Quantitative data reviewed, qualitative interviews complete, and a go/no-go decision made to adopt permanently, modify, or revert to the synchronous format.

## Team and Credentials

The engineering manager owns trial setup, process documentation, and the Day 30 retro. On-call channel-reading responsibility rotates across all 11 engineers on the existing schedule. No external facilitation or new headcount is required.

## Investment

There is no cash cost. The investment is time.

- 3 days of engineering manager time to document and set up the process before launch
- A daily 5-10 minute channel-reading task for the on-call engineer (replacing the meeting-facilitation task already on that rotation)
- Each engineer's time posting an async update: estimated 3-5 minutes per day

Net weekly effect: replacing a 14-minute meeting with a 5-minute update recovers roughly 9 minutes per engineer per day, approximately 16 person-hours per week across the team. The Thursday working session spends back 11 of those. Net recovery: 5 person-hours per week, assuming the Thursday session runs in full.

## Next Steps

Reply to this proposal to approve the 30-day trial. Once you confirm, the engineering manager will complete setup within three business days and announce the trial start date to the team. If you have conditions or modifications, name them in your reply and this proposal will be revised before launch.
