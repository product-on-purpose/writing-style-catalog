---
diff_pair_id: tone-candid-vs-resolute-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: tone
entry_a: candid
entry_b: resolute
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Tone swap - `candid` vs `resolute`

**Topic:** Should we adopt async-first standups?
**Axis varied:** tone
**A:** `candid` - Names the uncomfortable truth directly - not harsh, but unwilling to pretend the hard thing is not there.
**B:** `resolute` - The tone of having stopped deliberating - the decision is made and the writing is now about acting on it.

## What to notice

Both examples address the same topic and (by default) share every axis other than tone. 
The only deliberate variable is which tone the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The tone 
swap is the entire cause of those differences.

---

## A: `candid`

Team,

I want to be direct about something: our daily standup is not delivering what it is supposed to deliver, and we need to change it.

Here is the honest picture. We have three engineers who join at 9:30pm their local time on most days - and when they cannot make it, they miss information that affects their work. We have engineers who post "same as yesterday" most Tuesdays because nothing has actually changed since Monday's standup. We have blockers that get mentioned in the meeting and then disappear because nobody wrote them down. The standup takes 14 minutes on average and the signal-to-noise ratio is not good.

I know this is not news to some of you. I have been aware of it for a while and I should have said something sooner.

Here is what I think we should do: replace the synchronous standup with an async format for 30 days. Three questions, answered in Slack by 10am local time: what shipped, what is in progress today, what is blocked or at risk. Blocked items require a @mention. I read the channel each morning and make sure blocks get resolved the same day.

This does not fix everything. If people do not post consistently, the format breaks. If I do not read the channel attentively, blocked items will pile up. I am asking for your participation and holding myself accountable to the same standard.

The synchronous meeting I want to preserve is Thursday working sessions - real collaboration, not status.

I would rather try this and learn than continue a format that is not working. We will review at 30 days and make a permanent call together.

Any questions, come find me.

---

## B: `resolute`

Decision: we are moving to async standups. Trial starts Monday and runs thirty days. Here is the rollout.

**Daily updates.** Post in #team-standup by 10am your local time. Three fields, in this order:
- Shipped: what landed since your last update
- In progress: what you are actively working on today
- Blocked-or-at-risk: anything stuck or trending stuck, with an @mention of the person who can unblock you

If you are out, post "out today" - no other fields needed.

**Sync time.** The 9am Pacific slot is gone. In its place: 60-minute working session, Thursdays, 8am Pacific / 8:30pm IST. Agenda posted Wednesday EOD by the engineer rotating in as facilitator. This is for decisions, design review, and active unblocking - not status.

**Coverage.** I will read #team-standup every morning and flag anything that needs escalation. Tech leads do the same for their pillar. If a blocker sits without an answer for one business day, it comes to me.

**Trial guardrails.** We are not relitigating this for thirty days. If something is breaking, raise it in the Thursday session or DM me directly. At day 30 we run a fifteen-minute retro with three questions: posting rate, signal quality, India sentiment. We make the keep-or-revert call from that retro, not from corridor conversations.

**What I am not doing.** I am not asking for opinions on the format, the field names, or the time of the Thursday session. We can adjust those at day 30 if needed. For now we run the protocol as written so we are measuring one thing.

Monday morning, post your first update. India team - you write first because your morning is earliest. The rest of us pick it up from there.

Thanks for the work on this. Let us go.
