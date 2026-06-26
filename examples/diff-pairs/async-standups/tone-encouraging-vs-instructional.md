---
diff_pair_id: tone-encouraging-vs-instructional-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: tone
entry_a: encouraging
entry_b: instructional
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Tone swap - `encouraging` vs `instructional`

**Topic:** Should we adopt async-first standups?
**Axis varied:** tone
**A:** `encouraging` - Speaks to capability and forward motion - not false praise, but genuine belief that the person can do the hard thing.
**B:** `instructional` - Patient, structured teaching that measures its own success by whether the reader can do the thing - not by how much it explains.

## What to notice

Both examples address the same topic and (by default) share every axis other than tone. 
The only deliberate variable is which tone the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The tone 
swap is the entire cause of those differences.

---

## A: `encouraging`

Team,

I have watched you show up to that 9am standup for two years, including the people who join at 9:30pm their time, including the people who push through the weeks where it clearly does not fit their day. That kind of reliability is worth naming. You are a team that keeps showing up even when the format is hard.

I want to try something different - not because the effort was wrong, but because I think there is a better way to direct it.

Moving to async standups is a change, and changes like this often feel awkward for the first week or two. You will post an update and wonder if anyone read it. You will hit a blocker and instinctively want to raise your hand in the meeting. That discomfort is normal, and it passes. The teams I have seen make this shift usually hit their stride by week three.

What you have already built is the part that is actually hard: a team that is honest about blockers, that calls out when something is at risk, that does not hide bad news until it becomes a crisis. That does not come from the standup format - that comes from the culture you have built. The format change does not touch that. It just gives it a better container.

Here is what I am asking: give the async format 30 days before you decide whether you like it. Post your updates, mention your blockers, read what your teammates post. If by week four it still does not feel right, we will talk about what to adjust.

You have already done the hard part. This is just changing the tool.

---

## B: `instructional`

# How the async standup works, starting Monday

Starting Monday, we are running a 30-day trial of async standups in place of the 9am Pacific sync meeting. This guide explains what is changing, what you need to do, and how to recognize a well-formed update. Read it once, then refer back as needed.

## What is changing

**Sync standup** (the daily 9am Pacific call) is paused for 30 days.

**Async standup** is a written daily update posted in `#team-standup`. "Async" here means there is no shared meeting time - each engineer posts on their own schedule within a window.

**Working session** is a new 60-minute Thursday slot in the same calendar block. This is for real coordination work, not status. Agenda will be posted Wednesday.

## What you need to do

1. **Post your update in `#team-standup` by 10am local time each working day.** Local means your local time, not Pacific. If you are in Bengaluru and start work at 9am IST, you post by 10am IST.
2. **Use the three-field format.** Each update has exactly three sections:
   - **Shipped:** What you completed since your last update. Link the PR or doc.
   - **In progress:** What you are working on today. One or two items, not a backlog dump.
   - **Blocked or at risk:** Anything that needs help. If empty, write "None."
3. **@mention the unblocker on every blocker.** A blocker without a name attached is not actionable. If you are not sure who to mention, mention your lead and they will route it.
4. **Read the channel once per day.** You do not need to read every update, but scan for @mentions of you and for blockers in your area.

## What a good update looks like

> **Shipped:** Auth retry logic merged (#4412).
> **In progress:** Migrating session cache to Redis, expect PR by EOD.
> **Blocked:** Need staging access for new region - @priya.

That is a complete update. Three lines, specific, one named owner on the blocker.

## What we are measuring

At day 30 we will review three things: blocker resolution time, participation rate across timezones, and whether the Thursday session is delivering coordination value. We will decide together whether to keep the format, revert, or adjust.

Questions go in the thread under Monday's kickoff post.
