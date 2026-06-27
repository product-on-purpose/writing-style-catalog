---
entry_id: pitch-deck
axis: format
topic_slug: morning-routine
topic_label: Designing a sustainable morning routine
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Slide 1: Problem

**The first hour of every weekday belongs to someone else's inbox**

- Wake at 6:30, phone in hand before feet touch the floor
- First 45 minutes: Slack, email, news - reactive before the day begins
- 7:30am: family starts (breakfast, school dropoff, lunches). 9am: work starts
- Arrive at the desk already behind, already drained, already a step behind my own intentions

Three attempts in the past year to "just stop using my phone in the morning." Each lasted four to six days. The pattern: removed a behavior, replaced it with nothing. The vacuum collapsed back.

---

## Slide 2: Solution

**A four-step protocol that owns the 6:30-7:30 window before the day can claim it**

1. Water - 500ml within 5 minutes of waking (glass on the nightstand the night before)
2. Light - 10 minutes outside or by an open window
3. Movement - 15 minutes: walk, stretch, or bodyweight
4. Planning - 10 minutes on paper, top three priorities for the day

Phone stays in the kitchen, plugged in, face down, until step 4 is done.

One structural rule: replace the behavior, do not just remove it. That is what the three previous failures missed.

---

## Slide 3: Why Now

**The 30-day test is complete. This is no longer a hypothesis.**

- The v3.0 protocol launched 2026-05-14 and ran through day 30
- Data is in hand - not projected, not planned, not aspirational
- ADR-001 (2026-05-14) committed to a review at day 30; today is that review
- The question is no longer "will this work?" The question is "do we extend, and on what terms?"

The decision point is now, not next month.

---

## Slide 4: How It Works

**One decision removed: the phone is not within reach, so there is nothing to resist**

The phone-in-the-kitchen rule is the structural load-bearing piece. Willpower is not the mechanism. Distance is.

Each morning logs one row in `log/days.csv`: date, wake time, steps completed, mood, notes. Retros happen weekly in `log/retros/`. The protocol is designed to be skipped and resumed, not abandoned on the first missed morning.

Travel breaks the protocol. That is a known gap. A travel variant is Month 2 work.

---

## Slide 5: Traction

**23 of 30 mornings completed. The phone deferral held at 93 percent.**

| Metric | Month 1 Result |
|---|---|
| Full protocol completion | 23 of 30 (76.7%) |
| 6:15 wake held | 19 of 30 (63.3%) |
| Phone deferred until step 4 | 28 of 30 (93.3%) |
| Most common mood | "Steady" (14 days) vs. pre-protocol "tired" and "rushed" |

Misses are explained: 3 travel days, 4 sick days, 4 Tuesdays. No silent-failure cliff - every miss has a traceable cause.

---

## Slide 6: What It Costs

**Sleep time, one unasked question, and a travel plan that does not exist yet**

- Bedtime shifted from 11:30pm to 10:30pm - partially achieved, not fully locked in
- Spouse's 6:45-7:15am coffee window runs inside the silent hour; conversation deferred to 7:15 by design
- The silent-hour arrangement has been tolerated, not explicitly agreed to - that conversation has not happened
- Travel: two of three trips attempted the protocol, both poorly; a travel variant must be written before the next trip
- Weekends: currently running the same protocol, verdict genuinely unclear

The accountability partner check-in threshold is 70 percent completion. Month 1 cleared it at 76.7.

---

## Slide 7: Team

**Three people the protocol depends on**

- Me - protocol owner; designs, logs, adjusts, runs the weekly retros
- Spouse - absorbs the early-morning silence and the earlier bedtime; has not raised friction, but has not been directly asked
- Accountability partner - committed to a check-in if monthly completion drops below 70 percent; condition was written into ADR-001 and has not triggered

The accountability partner condition is the external forcing function. It has held without needing to activate.

---

## Slide 8: Ask

**Two commitments for Month 2**

1. **Explicit family agreement by end of this week** - a 10-minute conversation with my spouse to confirm the silent hour and earlier bedtime are genuinely sustainable, not just tolerated. Do not assume. Ask.

2. **30-day extension with two additions** - continue through day 60 with a travel variant documented before the next trip and a written weekend rule (even if the rule is "same as weekdays").

Review at day 60. If completion drops below 70 percent before then, the accountability partner check-in triggers before any design change.
