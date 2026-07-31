---
diff_pair_id: tone-encouraging-vs-instructional-onboarding-a-new-hire
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
axis_varied: tone
entry_a: encouraging
entry_b: instructional
generator: tools/diff-pair-generator.py
review_status: reviewed
---

# Diff Pair: Tone swap - `encouraging` vs `instructional`

**Topic:** Getting a new engineer productive in their first two weeks
**Axis varied:** tone
**A:** `encouraging` - Speaks to capability and forward motion - not false praise, but genuine belief that the person can do the hard thing.
**B:** `instructional` - Patient, structured teaching that measures its own success by whether the reader can do the thing - not by how much it explains.

## What to notice

Note first that these two renders are not even addressed to the same person, which is itself
the lesson.

**A writes to Priya.** "Priya, Starting on a team that ships every day and runs a live on-call
rotation is genuinely hard. The codebase is someone else's mental model, the rituals feel
opaque." It names the difficulty in order to make it survivable, and its work is on her belief
that she can do this.

**B writes to her manager.** "Getting Priya productive in two weeks requires you to front-load
access and context, then shift quickly to doing," followed by a numbered week one. It works on
the path, not on anyone's confidence.

**The sharpest single tell is the addressee.** Given one prompt, the encouraging register
reached for the person who needs heart and the instructional register reached for the person who
needs a sequence. Neither choice was stated in the topic; the tone selected its own reader.

**The practical consequence:** encouraging prose aimed at someone who needed steps reads as
empty, and instructional prose aimed at someone who needed heart reads as cold. Choosing the
tone is partly choosing who you are actually writing to.

---

## A: `encouraging`

Priya,

Starting on a team that ships every day and runs a live on-call rotation is genuinely hard. The codebase is someone else's mental model, the rituals feel opaque, and the tooling is new. None of that is a signal about you - it is just what week one looks like when the team has been running for a while without you.

Here is how the next two weeks are going to go.

Week one is entirely about standing up. By Friday you should have all your access working, your local environment running, and a solid read on how the service maps to the parts of the codebase you will touch. I will walk you through the ownership map on Tuesday so you know who to ask for what - that alone will make the second week significantly less disorienting.

The goal for week two is a real change in production. Not a tutorial exercise - an actual fix or small improvement that matters to the team. You will pick it from the backlog with me, we will pair on the approach, and you will drive it through the deploy. The daily-ship cadence means you will see it live before the week is out.

You can do this because you have already done the hard part: you showed up, you are asking the right questions, and you are paying attention to how the system actually behaves rather than how it is supposed to behave. That is the skill that makes engineers effective here. The rest is orientation.

By the end of two weeks you will have a working mental model of the service, a shipped change with your name on it, and a clear sense of who owns what. You are further along than you feel right now.

---

## B: `instructional`

Getting Priya productive in two weeks requires you to front-load access and context, then shift quickly to doing.

**Week one: foundation**

1. Before her first stand-up, give Priya credentials for every system she needs: the version-control host, the deployment pipeline, the ticket tracker, and the on-call tool. If any access requires a request queue - a system where permissions must be approved by a separate team - submit the request the Friday before she starts. Delays here block everything else in week one.

2. On day one, run a ninety-minute codebase walkthrough. Cover the service boundary - the edge at which your team's ownership ends and another team's begins - mapping which services your team owns and where the handoffs to other teams sit.

3. On day two, pair with her to locate two things in the codebase: where a change she could own lives, and what the deploy path looks like from commit to production.

**Week two: shipping**

4. Before week two begins, pick the change she will ship. It must be real - not a tutorial exercise - and scoped to a single file or function. If completing it requires understanding more than two service boundaries, it is too large for this slot.

5. Pair through the entire cycle: writing the code, opening the pull request, responding to review, and watching the deploy. Do not hand off during review.

6. After the change ships, name the on-call rotation explicitly: when her first shift starts, who to page if something breaks, and what the escalation path - the ordered list of contacts to try in sequence - looks like.

Belonging follows from step six. Once Priya has shipped real work and knows who holds what, she has the same operating facts as the rest of the team.
