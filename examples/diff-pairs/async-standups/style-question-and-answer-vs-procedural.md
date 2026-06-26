---
diff_pair_id: style-question-and-answer-vs-procedural-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: style
entry_a: question-and-answer
entry_b: procedural
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `question-and-answer` vs `procedural`

**Topic:** Should we adopt async-first standups?
**Axis varied:** style
**A:** `question-and-answer` - Sections are real reader questions in their natural phrasing, ordered by likelihood of being asked rather than by logical flow.
**B:** `procedural` - Task-first writing that takes a reader from "I don't know how" to "I did it" by organizing every decision around user goals, not system features.

## What to notice

Both examples address the same topic and (by default) share every axis other than style. 
The only deliberate variable is which style the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The style 
swap is the entire cause of those differences.

---

## A: `question-and-answer`

# Async-first standups: FAQ for the 30-day trial

## What if I forget to post?

Most days, no one will notice for a few hours. By 11am local your manager will ping you. If you forget twice in a week, the team lead will check in. The post is meant to take 90 seconds. If you are forgetting, the friction is probably not memory, it is that the format is not working for you. Tell us, do not just absorb the miss.

## How do blockers actually get resolved without the meeting?

Three fields, one of them is "blockers." If you have a blocker, you @mention the person who can unblock you in the same post. They get a notification. If they do not respond within their working hours, you escalate to the team channel. The standup meeting was not resolving blockers faster than this anyway. We checked: in the last 10 standups, 2 blockers were resolved in the meeting itself, the other 6 were resolved in side conversations afterward.

## I am new to the team. Does this work for me?

Honest answer: it is harder for new joiners and we know it. For your first 30 days, you get a 20-minute weekly sync with your onboarding buddy. Use it for the questions the standup used to surface for you. After 30 days, you will know who to ping for what, which is the actual skill the standup was teaching you, just slower.

## What about the social part? I liked seeing everyone.

This is the most common pushback and it is real. We are not removing all sync time. We are keeping the Friday team call (45 min, half social, half demos). The standup was never very social anyway, it was 11 people on mute waiting their turn. If you want more human contact than Friday provides, propose something. We will fund it.

## Do I have to post if I have nothing to report?

Yes, even one line. "No movement on X, picking up Y today, no blockers." The post is not just status, it is presence. Skipping creates ambiguity: did you not work, or did you forget to post? One line resolves that in 10 seconds.

## What if my manager wants more detail than three fields?

That is a one-on-one conversation, not a standup conversation. The three fields are for the team. If your manager needs more, they should be getting it in your weekly 1:1, not by reading every standup post.

## Will Priya and Arjun finally be in the loop?

That is the main reason we are trying this. They currently attend 3.2 of 5 sessions. With async, the floor for "being in the loop" stops being "you woke up at 9:30pm." We will measure this. If after 30 days they report still feeling out of the loop, the experiment failed even if attendance numbers look good.

## How will we know if it is working?

Four signals, measured at day 30:
1. Self-reported clarity on what teammates are working on (survey).
2. Self-reported attendance burden (especially for India-based engineers).
3. Time to blocker resolution (compared to a baseline we capture this week).
4. Number of "I did not know you were working on that" moments in retros.

## What if we hate it?

We go back. The proposal is a 30-day trial, not a permanent change. The reversal cost is one team meeting. Do not catastrophize and do not silently endure. Speak up at day 15.

## Can I still hop on a call if I want to?

Yes. Nothing prevents two people from getting on a Zoom to work through something. The thing we are removing is the mandatory daily group call, not the option to talk.

## Who do I talk to if I have a concern not covered here?

DM the team lead. Concerns shape the trial. The FAQ will be updated as new questions come in.

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
