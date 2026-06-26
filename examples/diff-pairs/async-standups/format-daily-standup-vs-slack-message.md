---
diff_pair_id: format-daily-standup-vs-slack-message-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: format
entry_a: daily-standup
entry_b: slack-message
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Format swap - `daily-standup` vs `slack-message`

**Topic:** Should we adopt async-first standups?
**Axis varied:** format
**A:** `daily-standup` - A brief daily status communication with three fixed sections - done, next, blockers. Surfaces information and flags what needs action. Not a progress report; a coordination tool.
**B:** `slack-message` - A short, async-first message designed for team channels - direct, scannable, and respectful of the reader's attention in a high-volume feed.

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

## B: `slack-message`

**Proposal: try async standups for 30 days starting May 19**

Our 9am standup is hard on the India team and the info disappears after each call. Want to run an experiment:

- Each person posts to #team-standup by 10am local time (3 fields: shipped / in progress / blocked)
- Blocked items @mention the person who can unblock
- On-call reads the channel by 9am PT and responds to blocks within 30 min
- We keep Thursday 3pm as a real working session for anything that needs live discussion

@priya @arjun @deepa - this gets you out of 9:30pm standups. Want to hear your reaction first.

:thread: Drop thoughts in thread by Friday and I will send a final plan Monday.
