---
diff_pair_id: voice-friendly-mentor-vs-product-thinker-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: voice
entry_a: friendly-mentor
entry_b: product-thinker
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Voice swap - `friendly-mentor` vs `product-thinker`

**Topic:** Should we adopt async-first standups?
**Axis varied:** voice
**A:** `friendly-mentor` - A warm, patient voice that assumes the reader is capable but new, explaining concepts by building from what they already know.
**B:** `product-thinker` - A product manager's voice that leads with "why" before "what," centers user outcomes over implementation, and asks what job the reader is trying to do.

## What to notice

Both examples address the same topic and (by default) share every axis other than voice. 
The only deliberate variable is which voice the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The voice 
swap is the entire cause of those differences.

---

## A: `friendly-mentor`

You have probably been in that standup. Twelve people on a Zoom call. Someone shares their screen to demo a bug they hit. Three people are clearly doing something else. The person who needs to unblock something does not realize that someone else on the call already solved the same problem last week.

That is not a standup problem. That is a coordination problem wearing a standup costume.

Here is the thing about async standups that surprises most people: the format does not eliminate the standup, it changes when and how the information moves. Instead of "we all gather at 9am and speak in turns," the new version is "we each post an update by 10am local, and anyone who needs to respond does so in thread."

The part that trips most people up is this: they think async means slower. It often means faster. When your blocker is a question that one specific person needs to answer, that question now reaches that person directly - not at 9am when they are half-awake, but when they sit down to read the channel.

What you do need to think through is structure. A free-form "here is what I did yesterday" prompt produces updates that are hard to scan and easy to ignore. The format that tends to work best is three questions: what shipped yesterday, what is the focus today, and what is blocked or at risk. Short answers, not essays. The discipline is in the brevity.

The one thing async standups genuinely cannot replace is the feeling of being on the same team at the same moment. If your team has low cohesion, adding a daily async ritual will not fix it. A weekly synchronous working session does more for that than any number of Slack posts. Use async for status. Use synchronous time for actual collaboration.

Start with a two-week trial. You will know pretty quickly whether it is working.

---

## B: `product-thinker`

Before we decide on the format, it is worth asking what job our engineers are hiring the standup to do. Listen to how people describe it and a few jobs surface: "I want to know if anyone is stuck so I can help." "I want to surface my own blocker without sending a 1:1 ping." "I want to know what is shipping this week so I am not surprised." Those are real jobs. The current 9am Pacific meeting is doing a mediocre version of all of them, and for our India teammates, it is failing the most basic job of all: being attendable.

The Q1 attendance numbers are not just a fairness issue, they are a product signal. When a third of your users only adopt your product 64% of the time and the other two-thirds adopt it 92% of the time, something about the offering is misaligned with the users it underserves. The standup is a product. The engineers are the users. We have a usability problem in one of our three primary segments.

The Priya incident is the kind of story I would put in a research deck. She diagnosed a 401 error in real time. Five hours later, another engineer hit the same error and spent 45 minutes re-solving it, because the original diagnosis had evaporated into a Zoom transcript no one can search. That is the job-to-be-done of "I want to find out if this has been solved before," and our current format does not serve it. An async post in #team-standup with a 401 in it is findable forever.

The async-first format addresses both the equity job and the searchability job in one move. It risks under-serving the connection job, which is real and which I do not want to dismiss. The Thursday working session is the hedge: a deliberate space for the kind of unstructured exchange that a status meeting was never the right container for anyway.

What does success look like? Three measures: blocker mention rate goes up (people feel safer surfacing them in writing), India attendance and contribution converges with the rest of the team, and we cut at least one duplicated debugging incident in the 30-day window. Run it. Watch the users. Decide on the data.
