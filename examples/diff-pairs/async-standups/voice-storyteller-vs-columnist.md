---
diff_pair_id: voice-storyteller-vs-columnist-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: voice
entry_a: storyteller
entry_b: columnist
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Voice swap - `storyteller` vs `columnist`

**Topic:** Should we adopt async-first standups?
**Axis varied:** voice
**A:** `storyteller` - A voice that carries meaning through character, scene, and concrete moment, trusting the reader to extract the principle from the specifics.
**B:** `columnist` - An opinionated, recurring perspective - the writer who has a recognizable stance, makes arguments in public, and is willing to be quoted on it.

## What to notice

Both examples address the same topic and (by default) share every axis other than voice. 
The only deliberate variable is which voice the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The voice 
swap is the entire cause of those differences.

---

## A: `storyteller`

The Slack channel had forty-seven new messages when Priya opened her laptop. It was 9:47pm in Bengaluru. The standup had ended without her, again. Outside her window, an autorickshaw passed. Inside, her son turned over in his sleep and made the small sound he sometimes made.

She scrolled.

Marco had shipped the cache invalidation fix. Good. There was a thread about the migration she had been waiting on for two weeks, and it ended with a shrug emoji from someone in London. She did not know what the shrug meant. Above the shrug, Dev had written, "I'll pick this up tomorrow." Below the shrug, nobody had replied. Priya read the thread twice. She still did not know what the shrug meant.

She typed, "Hey - is the migration unblocked or not?" Then she deleted it. Then she typed it again. Then she closed the laptop.

In San Francisco, Marco had just gotten back from lunch. He saw Priya's question come in, then disappear, then come in again. He thought about answering. He thought about how the standup had ended forty minutes ago and how he had explained the migration status during it. He thought about how Priya had not been there. He thought about how Priya had not been there last Tuesday, either, or the Tuesday before. He thought about what time it was in Bengaluru.

He typed, "Yes - unblocked. I'll write it up properly in a doc tonight your time so it's there when you start."

In Bengaluru, Priya had already gone to make tea. When she came back, the message was waiting.

She read it twice. Then she opened a new document and started writing down everything she had figured out about the migration over the last two weeks, the parts that had only ever lived in her head, the parts she had been planning to say in standup but had never quite gotten to. The document grew. The autorickshaw came back the other way.

At her standup the next morning - the proposed new one, the asynchronous one, posted by 10am local - she would paste the link.

---

## B: `columnist`

The daily standup is the cargo cult of distributed engineering. We kept the ritual long after the conditions that made it sensible stopped applying, and now we perform it every morning like we are summoning the sprint gods.

I have been in tech long enough to remember when standups actually worked. Small co-located teams, everyone within earshot of the whiteboard, the 15 minutes was genuinely the fastest way to sync. That world is mostly gone. Today's team is three timezones, four countries, and a mix of contractors and full-timers who start their day at different hours. The synchronous standup we hold onto is not optimized for that team. It is a nostalgia product.

The recent wave of companies - GitLab being the most documented example - moving to fully async standups is not just a pandemic artifact. It is a belated acknowledgment that the format should follow the team's actual structure, not the team's imagined ideal structure.

The counterargument is social cohesion: synchronous meetings build relationships, and daily standups are one of the few team rituals in a distributed environment. I grant this. I have seen async-first teams that feel like strangers to each other. The standup as a water-cooler substitute has real value.

But the answer to that is not to keep a broken coordination meeting alive for social purposes. The answer is a weekly synchronous working session where people actually collaborate on something - which builds far more relationship than serial status reporting at 9am.

Async standups are not a silver bullet. A bad team that posts bad updates asynchronously is still a bad team. But a good team using async standups will recover two hours a week and stop penalizing whoever lives on the wrong side of the timezone line.

Kill the synchronous standup. Build something better in its place.
