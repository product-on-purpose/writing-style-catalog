---
diff_pair_id: voice-columnist-vs-journalist-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: voice
entry_a: columnist
entry_b: journalist
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Voice swap - `columnist` vs `journalist`

**Topic:** Should we adopt async-first standups?
**Axis varied:** voice
**A:** `columnist` - An opinionated, recurring perspective - the writer who has a recognizable stance, makes arguments in public, and is willing to be quoted on it.
**B:** `journalist` - A reporting voice that attributes claims to sources and arranges facts in a sequence the reader can follow, resisting editorializing while still making the story work.

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

## B: `journalist`

At 9:32pm on a Tuesday in Bengaluru, Priya logged in for standup. Her son was finally asleep. The Slack call started a minute later, and the first thing she heard was a Pacific engineer asking, "Wait, can we go back, I missed who owns the migration?" Priya muted herself. "By the time it gets to me," she told me later, "there are about three minutes left and I have already heard every important thing twice."

This is the third week I have been reporting on the team's standup question. The proposal on the table is concrete: drop the daily 9am Pacific sync, replace it with an async post in #team-standup by 10am local, three fields, blockers @mentioned. The Thursday slot becomes a 60-minute working session. Thirty-day trial, with a revert clause that several engineers asked me to emphasize is not symbolic.

The numbers, as the team has gathered them: attendance for the three engineers in India averages 3.2 out of 5 weekly. For the six in US Pacific and Eastern, it is 4.6. The standup runs 14 minutes; engineers I spoke with estimated, independently, that about 4 of those minutes carry information they could not have gotten from a Slack post. One engineer, who asked not to be named because he likes the standup, said the social aspect mattered more than the information aspect. "I see my team's faces. That is not nothing."

Aakash, a senior engineer in Hyderabad, made a different point. "Last month we re-debugged a deployment problem that Marco had already solved. He told us in standup. The standup ended. The knowledge ended." Marco, in San Francisco, confirmed the story and added that he could not remember which week he had said it.

The 30-day trial begins Monday. The metrics that will determine whether it continues have not been fully specified, which two engineers flagged as a risk. The proposal's author, the engineering manager, told me she would publish them by Friday. "If we are going to run an experiment," she said, "we should know what we are measuring."

The team will revisit on day 31.
