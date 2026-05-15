---
entry_id: status-report
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Async standup trial - Week 2 status report

**Period:** Days 8 to 14 of the 30-day trial
**Author:** Engineering manager
**Audience:** Director of engineering, team, peer EMs

## Headline

The trial is on track. Participation is up, blockers are getting resolved faster than under the sync model, and India engineers are now contributing every weekday for the first time in this team's history. Two friction points have surfaced and are tracked below.

## Progress this week

- **Post completion:** 47 of 55 expected posts arrived by the 10am local cutoff. That is 85.5 percent on-time, up from 78 percent in Week 1.
- **Blocker resolution:** Median time from `@mention` to first substantive reply was 18 minutes. P90 was 2 hours 40 minutes. Compare to the sync standup baseline, where blockers raised at 9am often did not get a real conversation until the afternoon.
- **India participation:** All 4 IST-based engineers posted every weekday this week. Under the sync model this group attended 3.2 out of 5 standups on average.
- **Time recovered:** With the sync standup gone, the team got back approximately 16 person-hours this week. The Thursday working session used 11 of those. Net recovery: 5 person-hours.

## What is next

- Run the Week 3 cycle without process changes. Holding the design stable so the retro data is comparable.
- Pull the first qualitative signal: 10-minute 1:1 with each engineer Thursday and Friday. One question only: "What do you want to keep, change, or kill after the trial?"
- Prep the retro deck for the Day 30 review. Skeleton landing in `docs/trial-retro.md` by EOD Tuesday.

## Blocked or at risk

- **At risk: async posts trending long.** Three engineers are writing 200+ word posts. The format is meant to be skimmed in under 60 seconds per teammate. Plan: share two exemplar posts in the channel pinned message and demo the three-bullet ceiling at the Thursday session.
- **At risk: on-call triage load.** The on-call engineer this week spent roughly 25 minutes per morning on `#team-standup` triage, higher than the 10 minute target. Likely cause: blockers are surfacing earlier and louder than they did in sync. Watching this for one more week before deciding if the on-call role needs to be split.

## Asks

- None this week.

## Next report

Week 3 status report will land in `#team-standup` and via email by EOD next Monday.
