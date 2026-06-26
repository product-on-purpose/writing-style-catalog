---
diff_pair_id: style-diataxis-explanation-vs-procedural-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: style
entry_a: diataxis-explanation
entry_b: procedural
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `diataxis-explanation` vs `procedural`

**Topic:** Should we adopt async-first standups?
**Axis varied:** style
**A:** `diataxis-explanation` - The Diataxis "Explanation" mode - oriented toward understanding rather than action, building a conceptual model for the reader.
**B:** `procedural` - Task-first writing that takes a reader from "I don't know how" to "I did it" by organizing every decision around user goals, not system features.

## What to notice

Both examples address the same topic and (by default) share every axis other than style. 
The only deliberate variable is which style the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The style 
swap is the entire cause of those differences.

---

## A: `diataxis-explanation`

## Why Async Standups Work the Way They Do

An async standup is not a standup without the video call. It is a different kind of coordination mechanism, built on different assumptions about when and how information should move.

To understand why the distinction matters, it helps to understand what a standup is actually trying to accomplish. The daily standup has two functions that usually coexist in the same meeting without being separated: status visibility (who is doing what, what is blocked) and team cohesion (the daily ritual of shared presence, the sense of a team operating together). Synchronous standups do both at once because everyone is in the room at the same time. Async standups separate them.

The status-visibility function works differently in async format because information becomes persistent and addressable. In a synchronous standup, a blocker mentioned verbally reaches everyone in the room, but only for the duration of the sentence. The person who can resolve it must remember it, and the people who might have the same problem next must either have been present or get told separately. In an async channel, the same information is posted, searchable, and accessible to anyone on the team regardless of timezone or work schedule. The blocker reaches the right person not because they were present but because they are mentioned directly.

The team-cohesion function does not transfer to async in the same way, and this is why async-only teams sometimes feel fragmented. Daily synchronous standups create what anthropologists call "phatic communion" - interaction whose function is social bonding rather than information transfer. "How's it going?" is not a request for information; it is a gesture of acknowledgment. Async updates can approximate some of this through informal additions to the update template, but a Slack thread is not a room. The teams that sustain cohesion in async-first environments almost always supplement their async standup with a different synchronous ritual - a weekly working session, a monthly retrospective - that exists specifically for the cohesion function that async cannot provide.

The reason async standups often produce higher-quality status information than synchronous ones is cognitive: writing forces more clarity than speaking. A person who says "working on the auth refactor" in a standup has technically satisfied the format. A person writing the same update often notices the vagueness before they post it and adds the detail that makes it useful. The act of writing creates a moment of reflection that verbal turn-taking does not.

---

## B: `procedural`

# How to roll out an async standup in your team

This guide walks a team lead through replacing a synchronous daily standup with an async update across four timezones. It is written for a lead running an 11-person engineering team distributed across US Pacific, US Eastern, UK, and India.

## Prerequisites

Before you start, confirm the following:

- Your team has a shared Slack workspace (or equivalent) where you can create a dedicated channel.
- You have a recurring sync meeting slot you can repurpose. You will not delete it - you will reuse the time.
- You have at least two weeks of attendance data showing the cost of the current schedule. This makes the case if anyone resists.
- Your manager is informed. Async standups are not controversial, but they look like a meeting being cancelled, and that is a thing managers like to know.

## Steps

### 1. Create the channel

Create `#team-standup` in Slack. Set the channel description to: "Daily async standup. Post by 10am your local time. Three fields: Shipped, In progress, Blocked or at risk."

### 2. Pin the template

Pin a message to the channel with the exact three-field template:

```
Shipped: [what merged or shipped in the last 24h]
In progress: [what you are working on today]
Blocked or at risk: [what is stuck, @mention who can unblock]
```

A pinned template removes the need for anyone to remember the format.

### 3. Announce the 30-day trial

Post in the team channel that the team will run async standups for 30 days, with a revert option. Name the start date. Name the success criteria: blocker resolution time, channel engagement, team survey.

### 4. Cancel the daily sync

Cancel the recurring 9am Pacific standup on the calendar. Do not just stop attending. Cancelling the invite signals the change is real.

### 5. Create the Thursday working session

Add a recurring 60-minute Thursday meeting at a time that works for all four timezones. This is your new sync slot. Use it for discussion that needs real-time exchange.

### 6. Post first, ask others second

On day one, post your own update by 9am Pacific before anyone else. Modeling is faster than instructing.

### 7. @mention blockers explicitly

When you see a blocked item without an @mention, reply in thread and ask who owns it. Do this for the first week. After that the pattern is self-sustaining.

## Confirming it worked

After 30 days, check three things:

- Median time from "Blocked" post to first reply from the unblocker. Target: under 2 hours during overlap windows.
- Number of team members posting at least 4 of 5 weekdays. Target: 9 of 11.
- A short survey: "Do you have more or less context on what your teammates are doing than 30 days ago?"

If two of three are positive, keep the change. If two of three are negative, revert and write up what you learned.
