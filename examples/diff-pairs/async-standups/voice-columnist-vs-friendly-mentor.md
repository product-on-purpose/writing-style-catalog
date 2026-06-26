---
diff_pair_id: voice-columnist-vs-friendly-mentor-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: voice
entry_a: columnist
entry_b: friendly-mentor
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Voice swap - `columnist` vs `friendly-mentor`

**Topic:** Should we adopt async-first standups?
**Axis varied:** voice
**A:** `columnist` - An opinionated, recurring perspective - the writer who has a recognizable stance, makes arguments in public, and is willing to be quoted on it.
**B:** `friendly-mentor` - A warm, patient voice that assumes the reader is capable but new, explaining concepts by building from what they already know.

## What to notice

Both examples address the same topic and (by default) share every axis other than voice. 
The only deliberate variable is which voice the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The voice 
swap is the entire cause of those differences.

---

## A: `columnist`

The daily standup is the cargo cult of distributed engineering. We kept the ritual long after the conditions that made it sensible stopped applying, and now we perform it every morning like we are summoning the sprint gods.

I have been in tech long enough to remember when standups actually worked. Small co-located teams, everyone within earshot of the whiteboard, the 15 minutes was genuinely the fastest way to sync. That world is mostly gone. Today's team is three timezones, four countries, and a mix of contractors and full-timers who start their day at different hours. The synchronous standup we hold onto is not optimized for that team. It is a nostalgia product.

The recent wave of companies - GitLab being the most documented example - moving to fully async standups is not just a pandemic artifact. It is a belated acknowledgment that the format should follow the team's actual structure, not the team's imagined ideal structure.

The counterargument is social cohesion: synchronous meetings build relationships, and daily standups are one of the few team rituals in a distributed environment. I grant this. I have seen async-first teams that feel like strangers to each other. The standup as a water-cooler substitute has real value.

But the answer to that is not to keep a broken coordination meeting alive for social purposes. The answer is a weekly synchronous working session where people actually collaborate on something - which builds far more relationship than serial status reporting at 9am.

Async standups are not a silver bullet. A bad team that posts bad updates asynchronously is still a bad team. But a good team using async standups will recover two hours a week and stop penalizing whoever lives on the wrong side of the timezone line.

Kill the synchronous standup. Build something better in its place.

---

## B: `friendly-mentor`

You have probably been in that standup. Twelve people on a Zoom call. Someone shares their screen to demo a bug they hit. Three people are clearly doing something else. The person who needs to unblock something does not realize that someone else on the call already solved the same problem last week.

That is not a standup problem. That is a coordination problem wearing a standup costume.

Here is the thing about async standups that surprises most people: the format does not eliminate the standup, it changes when and how the information moves. Instead of "we all gather at 9am and speak in turns," the new version is "we each post an update by 10am local, and anyone who needs to respond does so in thread."

The part that trips most people up is this: they think async means slower. It often means faster. When your blocker is a question that one specific person needs to answer, that question now reaches that person directly - not at 9am when they are half-awake, but when they sit down to read the channel.

What you do need to think through is structure. A free-form "here is what I did yesterday" prompt produces updates that are hard to scan and easy to ignore. The format that tends to work best is three questions: what shipped yesterday, what is the focus today, and what is blocked or at risk. Short answers, not essays. The discipline is in the brevity.

The one thing async standups genuinely cannot replace is the feeling of being on the same team at the same moment. If your team has low cohesion, adding a daily async ritual will not fix it. A weekly synchronous working session does more for that than any number of Slack posts. Use async for status. Use synchronous time for actual collaboration.

Start with a two-week trial. You will know pretty quickly whether it is working.
