---
diff_pair_id: voice-friendly-mentor-vs-coach-onboarding-a-new-hire
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
axis_varied: voice
entry_a: friendly-mentor
entry_b: coach
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Voice swap - `friendly-mentor` vs `coach`

**Topic:** Getting a new engineer productive in their first two weeks
**Axis varied:** voice
**A:** `friendly-mentor` - A warm, patient voice that assumes the reader is capable but new, explaining concepts by building from what they already know.
**B:** `coach` - A facilitative voice that builds capacity through questions and reflection, acknowledges complexity before offering direction, and creates space without abandoning the reader.

## What to notice

Both are addressed to the person running the onboarding, not to Priya, and both are warm. They
differ on whether the reader is handed an answer or a diagnosis.

**A gives the answer and names the trap.** "Getting Priya from 'where's the bathroom' to 'I
shipped a real change' in two weeks is achievable. You just need to resist one temptation:
front-loading everything you know." The reader leaves with a rule they can apply on Monday.

**B slows the reader down before any plan exists.** "Getting Priya through her first two weeks
is more complicated than it looks, and it's worth pausing before you build the schedule. Here's
what's actually happening:" and then a reading of Priya's situation rather than a prescription
for it.

**The sharpest single tell is what the first paragraph promises.** A promises an outcome and one
thing to avoid. B promises that the reader's model of the problem is incomplete. Only one of
those can be acted on immediately, and only one of them will survive a Priya who is unlike the
Priya the writer imagined.

---

## A: `friendly-mentor`

Getting Priya from "where's the bathroom" to "I shipped a real change" in two weeks is achievable. You just need to resist one temptation: front-loading everything you know.

Think of it like teaching someone to drive. You do not start with traction physics. You start with: ignition, mirrors, gear, go. Priya needs a working mental model first - the complete picture comes after she has one to build on.

**Week one: ground, then orient**

Start with access and tooling on day one. Not the full tour - just access. She needs to read the codebase, run the service locally, and get into the chat tool and ticket tracker. Spend the first morning on those three things and you've already avoided the most common new-hire stall: two days blocked on a missing permission.

Once she can see the system running, walk her through one request out loud - from the point it enters the service to the point a response goes back. Do it in a call, not a document. Why a call? Because you'll see the moment a concept lands, and that's your cue to move on.

The part that usually trips people up on a service-oriented backend is not the code itself - it's why the services are split the way they are. Name that gap directly: "The boundaries feel arbitrary at first. They'll make sense once you've seen a few on-call incidents."

**Week two: pair on something real**

Now that she has a mental map of the system, pick a small issue together. Something with a narrow blast radius - a label fix, a missing validation, a config adjustment. Walk through it with her, but let her drive. Your job is to name the landmines, not clear them for her.

When she pushes that first change, make a small moment of it. Shipping is how engineers start to feel real on a team. Belonging is not something you can tell someone to feel; it happens when they do something that matters.

---

## B: `coach`

Getting Priya through her first two weeks is more complicated than it looks, and it's worth pausing before you build the schedule.

Here's what's actually happening: Priya is navigating two things at once. She is trying to learn how your system works, and she is trying to figure out whether she belongs here. Those are not the same problem, and it's worth asking which one your current plan is actually solving.

Before you decide what to put in front of her, ask yourself: what does she most need to feel safe enough to ask a question? Access and tooling matter, but they're not the answer to that. The on-call rotation, the daily ship cadence, the fact that things go wrong and people respond quickly - those are all real signals to a new person. What story are you helping her build about what it means when something breaks?

One way to think about the two-week arc is as two separate problems you're solving in sequence. The first week is about removing friction: credentials, the local dev environment, a mental model of the codebase's seams. The second week is about momentum - getting her into a real change with you beside her, not ahead of her.

What does "beside her" mean to you? There's a difference between pairing because you want to check her work and pairing because you want to watch how she thinks. One of those builds her capacity. The other builds your confidence in her, which is a different thing.

Who on the team is Priya most likely to feel safe interrupting? Think about how you can surface that relationship deliberately rather than leaving it to chance.

By the end of week two, the goal isn't a flawless change. It's a change that is real, that she can point to, and that she navigated with enough support to feel the process working. What would you need to have set up for that to happen?
