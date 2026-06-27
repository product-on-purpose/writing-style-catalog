---
entry_id: project-brief
axis: format
topic_slug: async-standups
topic_label: Whether the team should move to async-first standups
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Async-First Standup Trial - Project Brief

## Goal

Run a 30-day async standup trial with the full 11-person engineering team to determine whether replacing the synchronous daily standup with structured async posts in #team-standup delivers equitable participation across four timezones and persistent, searchable status records.

## Background

The engineering team has grown from 6 to 11 engineers across four timezones over 18 months. The current 9am Pacific standup lands at 9:30pm IST, creating a structural disadvantage for India-based engineers: they averaged 3.2 attendances per week in Q1 compared to 4.6 for US-based engineers. The 14-minute meeting produces an average of 4.2 minutes of content that changes anyone's behavior; the remainder is status that requires no response and does not persist after the call.

## Scope

### In scope

- Design and document the async standup process, including the three-field template (Shipped / In progress / Blocked or at risk), the 10am local posting window, and the on-call triage role
- Run the 30-day trial with all 11 engineers
- Track participation rate, blocker resolution time, and time recovered across the trial period
- Collect qualitative feedback at the mid-point and at the Day 30 retro
- Decide whether to adopt, adjust, or revert based on trial data

### Out of scope

- Tooling changes beyond Slack templates (no standup bots or third-party apps during the trial)
- Changes to any sprint ceremony other than the daily standup
- External communication about this change to stakeholders outside the engineering org during the trial

## Constraints

- The trial runs for exactly 30 days without mid-cycle process changes, so week-over-week data is comparable
- No new tooling is approved for this initiative; the format uses Slack only
- The Thursday working session must fit within the existing 60-minute standup calendar block already held by the team

## Success Criteria

- On-time post rate reaches or exceeds 90 percent of expected daily posts by week 3
- India-based engineers post every weekday at a rate matching or exceeding US-based engineers
- Median time from @mention to first substantive reply is at or below the blocker resolution baseline from the sync standup
- The team votes at the Day 30 retro to continue, adopt permanently, or make a named adjustment rather than revert

## Team

- Owner: Engineering manager (accountable for the trial design and the adopt/adjust/revert call)
- Contributors: All 11 engineers (daily posting), on-call engineer rotation (daily triage)
- Informed: Director of engineering, peer engineering managers
