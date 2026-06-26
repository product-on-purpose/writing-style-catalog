---
diff_pair_id: style-socratic-inquiry-vs-diataxis-explanation-async-standups
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
axis_varied: style
entry_a: socratic-inquiry
entry_b: diataxis-explanation
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Style swap - `socratic-inquiry` vs `diataxis-explanation`

**Topic:** Should we adopt async-first standups?
**Axis varied:** style
**A:** `socratic-inquiry` - Advances by asking questions the reader answers in their own head - the conclusions are inferences, not assertions.
**B:** `diataxis-explanation` - The Diataxis "Explanation" mode - oriented toward understanding rather than action, building a conceptual model for the reader.

## What to notice

Both examples address the same topic and (by default) share every axis other than style. 
The only deliberate variable is which style the writing was rendered through. Read both 
and ask: where does the framing change? Where does the vocabulary change? What does the 
reader take away from A that they would not take away from B, and vice versa? The style 
swap is the entire cause of those differences.

---

## A: `socratic-inquiry`

# Questions to ask before changing the standup

Before the team votes on async-first, sit with these questions. Some have clean answers. Some do not, and that is the point.

## What is the standup actually for?

Pause on this one. The original intent was "remove blockers fast." Is that still what happens? When you count the last ten standups, how many ended with a blocker actually being removed in the meeting? If the number is low, what is the meeting now doing instead?

## Who is not in the room?

The 9am Pacific call lands at 9:30pm in Bangalore. Priya and Arjun attend 3.2 of 5 sessions. When they miss, where does their context go? When the US-based engineers attend 4.6 of 5, whose questions get answered first? If the meeting were redesigned around the people most often absent, what would change?

## What would survive if we kept nothing else?

Imagine you delete the standup tomorrow. What part of it would you immediately reinvent? Is it the status update, the human contact, the moment of accountability, or the place where blockers surface? If the answer is "the human contact," is a written post a replacement, or a different thing entirely?

## Where does the status live now?

The standup is 14 minutes. Roughly 4 of those minutes carry signal. The other 10 are connective tissue: throat clearing, context resetting, waiting for the next speaker. After the call ends, where does the signal go? If a senior engineer joins next month and asks "what did the team work on last sprint?", what artifact answers them?

## Is "blocker" a real word here?

The async proposal asks people to @mention blockers. But what counts as a blocker? Is it a thing you cannot proceed without? A thing slowing you down? A thing you would mention if asked but would not interrupt anyone over? If three people define it three ways, what happens to the @mentions?

## Could both formats be wrong?

The conversation has narrowed to sync versus async. Are those the only two options? What about sync twice a week and async the other three days? What about sync only when someone has a blocker that needs the group? What about no standup at all, and a different ritual for connection? Have you considered why the choice keeps presenting itself as binary?

## What would you learn from a 30-day trial that you cannot learn by talking about it?

If the team ran async for 30 days, what would you measure? Attendance is easy to count, but attendance is not the question. What would tell you whether the change is working? If you cannot name the signal in advance, what does that mean about the proposal?

## What are you afraid will happen?

Name it. The fear is usually more specific than the objection. Is it that people will feel less connected? That junior engineers will get lost? That something will fail silently and no one will notice for a week? Each fear points at something the new format would need to handle. Which fears are you carrying, and which is the team carrying for you?

---

## B: `diataxis-explanation`

## Why Async Standups Work the Way They Do

An async standup is not a standup without the video call. It is a different kind of coordination mechanism, built on different assumptions about when and how information should move.

To understand why the distinction matters, it helps to understand what a standup is actually trying to accomplish. The daily standup has two functions that usually coexist in the same meeting without being separated: status visibility (who is doing what, what is blocked) and team cohesion (the daily ritual of shared presence, the sense of a team operating together). Synchronous standups do both at once because everyone is in the room at the same time. Async standups separate them.

The status-visibility function works differently in async format because information becomes persistent and addressable. In a synchronous standup, a blocker mentioned verbally reaches everyone in the room, but only for the duration of the sentence. The person who can resolve it must remember it, and the people who might have the same problem next must either have been present or get told separately. In an async channel, the same information is posted, searchable, and accessible to anyone on the team regardless of timezone or work schedule. The blocker reaches the right person not because they were present but because they are mentioned directly.

The team-cohesion function does not transfer to async in the same way, and this is why async-only teams sometimes feel fragmented. Daily synchronous standups create what anthropologists call "phatic communion" - interaction whose function is social bonding rather than information transfer. "How's it going?" is not a request for information; it is a gesture of acknowledgment. Async updates can approximate some of this through informal additions to the update template, but a Slack thread is not a room. The teams that sustain cohesion in async-first environments almost always supplement their async standup with a different synchronous ritual - a weekly working session, a monthly retrospective - that exists specifically for the cohesion function that async cannot provide.

The reason async standups often produce higher-quality status information than synchronous ones is cognitive: writing forces more clarity than speaking. A person who says "working on the auth refactor" in a standup has technically satisfied the format. A person writing the same update often notices the vagueness before they post it and adds the detail that makes it useful. The act of writing creates a moment of reflection that verbal turn-taking does not.
