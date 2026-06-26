---
diff_pair_id: format-daily-standup-vs-status-report-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: daily-standup
entry_b: status-report
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `daily-standup` vs `status-report`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `daily-standup` - A brief daily status communication with three fixed sections - done, next, blockers. Surfaces information and flags what needs action. Not a progress report; a coordination tool.
**B:** `status-report` - A periodic async update covering progress since the last report, what is next, and what is blocked - the working unit of distributed-team visibility.

## What to notice

Both examples address the same topic and (by default) share every axis other than format. 
The only deliberate variable is which format the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The format 
swap is the entire cause of those differences.

---

## A: `daily-standup`

**#team-standup - Devon Park - Tue May 27, 9:42am PT (day 9 of trial)**

**Shipped**
- Rate-limiter rollout to staging; 0 errors over 18h soak
- PR #4412 merged (auth token rotation runbook)

**In progress**
- Production rollout of rate-limiter, gated behind `rl_v2` flag, 5% traffic by EOD
- Pairing with Aditi 10am PT on the IST-hour metrics dashboard

**Blocked / at risk**
- Waiting on @sara for sign-off on the rotation runbook before I close the parent ticket (not urgent, EOW is fine)
- (meta) Async format participation was 9/11 yesterday - @oliver and @emma did not post. Oliver was on-call handoff, fine. Emma I will DM. Flagging so @maya has visibility before the day-15 pulse.

---

## B: `status-report`

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
