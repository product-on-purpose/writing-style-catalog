---
diff_pair_id: tone-urgent-vs-candid-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: tone
entry_a: urgent
entry_b: candid
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Tone swap - `urgent` vs `candid`

**Topic:** Should we adopt async-first standups?
**Axis varied:** tone
**A:** `urgent` - Clarity under real pressure - the first sentence is the most important thing, and every word after it earns its place by not slowing the reader down.
**B:** `candid` - Names the uncomfortable truth directly - not harsh, but unwilling to pretend the hard thing is not there.

## What to notice

Both examples address the same topic and (by default) share every axis other than tone. 
The only deliberate variable is which tone the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The tone 
swap is the entire cause of those differences.

---

## A: `urgent`

Team,

We took a Sev-2 last night because our standup format is broken. We are changing it this week.

Here is what happened. At 10:47pm IST, the payments pipeline started dropping retries. Priya had flagged the underlying risk in Tuesday's standup. She said it at 9:45pm her time, into a meeting she joins after her kids are in bed, into a discussion that moved on in under 90 seconds because three Pacific engineers were also talking. Nobody wrote it down. Nobody owned it. Last night it broke, she was the only person who could fix it, and she was unreachable because she was asleep, like a person should be at 11pm.

This is not Priya's failure. This is our format failing in exactly the way the attendance data has been telling us it would. India sits at 3.2 of 5 standups. Blockers raised at the 14-minute mark of a meeting at 9:30pm IST are not blockers we have actually heard.

Effective Monday, we are running the async format. No more 9am Pacific daily call.

**What you do:**

1. Post in `#team-standup` by 10am your local time. Every working day.
2. Three fields: Shipped, In progress, Blocked or at risk.
3. Every blocker @mentions an owner. No owner, not a blocker.
4. If you see a blocker in your area, you respond same day.

**What I do:**

I read the channel by 11am Pacific. I escalate any unowned blocker within the hour. If I miss one, call me out in the channel.

We are running this for 30 days. We are not waiting for Q2 planning. We are not workshopping it. The data has been clear for a quarter and last night made it expensive.

Thursday at the old 9am Pacific slot, we have a 60-minute working session. First agenda item is the payments incident post-mortem. Second is anything else you have been waiting to surface in a real conversation instead of a meeting.

If you have a strong objection, tell me before Friday EOD. Otherwise we start Monday.

We owe Priya a format that hears her the first time.

---

## B: `candid`

Team,

I want to be direct about something: our daily standup is not delivering what it is supposed to deliver, and we need to change it.

Here is the honest picture. We have three engineers who join at 9:30pm their local time on most days - and when they cannot make it, they miss information that affects their work. We have engineers who post "same as yesterday" most Tuesdays because nothing has actually changed since Monday's standup. We have blockers that get mentioned in the meeting and then disappear because nobody wrote them down. The standup takes 14 minutes on average and the signal-to-noise ratio is not good.

I know this is not news to some of you. I have been aware of it for a while and I should have said something sooner.

Here is what I think we should do: replace the synchronous standup with an async format for 30 days. Three questions, answered in Slack by 10am local time: what shipped, what is in progress today, what is blocked or at risk. Blocked items require a @mention. I read the channel each morning and make sure blocks get resolved the same day.

This does not fix everything. If people do not post consistently, the format breaks. If I do not read the channel attentively, blocked items will pile up. I am asking for your participation and holding myself accountable to the same standard.

The synchronous meeting I want to preserve is Thursday working sessions - real collaboration, not status.

I would rather try this and learn than continue a format that is not working. We will review at 30 days and make a permanent call together.

Any questions, come find me.
