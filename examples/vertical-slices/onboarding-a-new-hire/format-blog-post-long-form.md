---
entry_id: blog-post-long-form
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Onboarding a New Engineer: Start at the End

Most onboarding plans start where they should end. They begin with access requests and tool installations, work through codebase walkthroughs and architecture diagrams, stack meeting introductions on top of process explanations, and arrive somewhere in week two at the idea that maybe the new engineer should try something. By then, the person sitting across from you has been saturated with information and starved of action, and they are still not sure whether they are a visitor or a resident.

That order is backward. The moment that tells a new engineer whether they belong is not the welcome meeting and not the first day their laptop works. It is the first time they ship something real - something that goes through the team's actual process, touches code that matters, and lands in production. Everything else in the two weeks is infrastructure for that moment.

So when Priya showed up Monday morning, the question I asked myself first was not "what does she need to know?" It was "what does she need to ship by Friday of week two, and what would have to be true for that to happen?" That reversal changes almost every decision you make.

## The First Week Is Not About Productivity

If you are honest about what the first week is for, it is not productivity. A new engineer on a team that ships daily and runs an on-call rotation is not going to contribute meaningfully to either of those things in her first five days. She does not know the codebase well enough to review a pull request with confidence. She does not know the deployment process well enough to trust herself in it. She does not know which services talk to each other, which corners are clean and which are minefields, or where to look when something breaks.

That is not a failure of hiring - that is the nature of codebases and teams. They accumulate context. A new person starts with none of it, and the first week is about reducing the ambient anxiety of having none of it enough that she can actually pay attention.

Access and tooling matter here, but not for the reason most onboarding checklists frame them. The checklist framing is operational: she needs credentials to do her job. The human framing is more important: a person who spends her first two days unable to log in, waiting on access tickets, staring at a machine that will not connect to the build system - that person has spent two days being told, by friction, that the team was not quite ready for them. Even if no one meant it that way.

Get the access sorted before Monday. Not "create the tickets before Monday" - actually get it done. Repository access, the deployment pipeline, the ticket tracker, the chat tool, the documentation system, the on-call tooling. If there is a staging environment she should be able to push to, confirm she can push to it. This is a two-hour project done the Friday before she starts. It signals that her arrival was anticipated and that the team's operational machinery is already hers.

The codebase orientation is not a lecture. Walk her through one service - not all of them, one of them - in enough detail that she can follow a change from local development to production. Pick the service where her first change will live. The goal is not comprehensive understanding. The goal is "I know where to look when I need to understand something." That is enough for week one. Comprehensive understanding is a six-month project.

One more thing: put on-call on the calendar for her as a shadow, not a participant, starting in week two. She should see what it looks like before she is ever on it. But do not make week one about on-call preparation. The rotation exists to support the service; the first week exists to support her.

## Finding the Right First Change

The first real change is the critical design decision in any onboarding plan, and most people make it wrong in one of two directions. Either they pick something so small it feels like a test - fix this typo, update this config value, add this comment - which tells the new engineer that the team does not trust her with anything that matters. Or they pick something too large, something that requires understanding three services and a month of history, and she spends two weeks making progress she cannot quite see toward a change that does not quite land by the deadline.

The right first change is genuinely small and genuinely real. Small means: one service, one behavior, well-understood scope, reviewable in a single session. Real means: it matters to the team that this gets done, it touches the production codebase, and when it ships, something is better than it was.

Bug fixes that are clearly scoped work well. Small feature additions to an internal tool work well. Improvements to a test suite work well - this is underrated, because tests live at the edges of the codebase and teach a new engineer a great deal about how the team thinks about correctness. Documentation fixes in the codebase itself work less well, because they feel - and often are - purely accommodating to the new person rather than useful to the team.

Pair on the first change. This does not mean sitting next to her while she types. It means: you have already looked at the area of the codebase the change touches, you know where the tricky parts are, you are available when she hits them, and you have agreed that you will review her pull request with the attention of someone who cares about the outcome rather than just the onboarding milestone. The pairing makes the change real. It is the difference between doing a practice run in a simulator and flying with someone who will catch you if you reach for the wrong lever.

The review conversation is part of the onboarding. When you review her first pull request, you are not just checking the code. You are modeling how the team thinks about changes. What do you comment on? What do you let go? What question do you ask instead of stating the answer? This is the first time she gets to see the team's taste expressed directly toward her work, and it either feels like engagement or it feels like judgment. How you write your review comments matters.

## The Velocity Trap

This is the part that teams with daily shipping and on-call rotations get wrong most often, including teams that otherwise onboard thoughtfully.

A team that ships every day has a visible, ambient pace. The ticket tracker churns. The deployment log rolls. People talk in the chat tool about changes that went out that morning, incidents that happened last night, decisions that were made in a meeting she was not part of. She can see all of this. On day three, Priya can see that her teammates have shipped several things and she has shipped nothing, and the part of her brain that tracks social safety starts doing math she did not ask it to do.

You do not manage this by telling her not to worry about it. You manage it by making her work visible. Give her a short list - two or three things - that she is explicitly working on this week. Put it somewhere she can check items off. The list is not about productivity management. It is about giving her concrete evidence that she is making progress in a place where progress is otherwise hard to see.

Similarly, the on-call rotation can feel like a permanent weight hanging over a new engineer. She does not know the services well enough to debug an incident confidently. She knows she will be on call someday, and she does not know when, and she does not know if she will be good at it. The antidote is specificity. Tell her: you are shadowing the rotation for the next two weeks, you will have a primary partner for your first several stints after that, and there is a documented playbook for the most common alerts. Then show her the playbook. Let her read it before she needs it.

The broader point is that arriving into a high-velocity environment feels like arriving into a river. The current is moving and you are standing in it. The way you make that feel safe is not by slowing the river. It is by giving the new person a handhold - something to grip while they find their footing. Access sorted before day one, a clear first task, visible progress, and explicit on-call scaffolding are the handholds. They do not slow the team down. They are just the architecture of belonging in a fast environment.

## Who Owns What, and Why She Needs to Know

Onboarding guides often treat ownership maps as operational logistics. She needs to know who owns a given service because if something breaks in that service she needs to know who to call. That is true, but it is not the most important reason to make ownership legible early.

The more important reason is that a person who understands ownership understands the team's structure of intention. She can see who cares about what, where the centers of gravity are, which areas are being actively developed versus maintained at steady state. That map tells her where she can have opinions that will be heard, where to bring her own ideas, and whose perspective to seek before proposing a change in a given area.

This matters for belonging in a way that feels abstract until it is not. A new engineer who does not know the ownership map tends to either avoid proposing things - because she does not know if it is her place - or propose things without context - because she does not know whose territory she is in. Both patterns create friction that can look like the person does not fit, when what is actually true is that the team did not make the map available to her.

Spend thirty minutes in the second week walking through ownership with her. Not the org chart - the actual codebase ownership, including the parts that are genuinely ambiguous or contested. Ambiguity is not a defect to hide from a new person. It is context. She will learn more about how the team actually works from one honestly ambiguous ownership conversation than from a week of clean documentation.

And then ask her a question. Not a test - a real question. Something like: "Which of the services we have talked about feels most interesting to you and why?" This signals that she is not just being onboarded into a static structure. She has opinions worth having. The team is curious about them.

## What Happens at the Merge

The end of week two, Priya merges her first pull request. The CI passes, the deployment runs, and something in production is different because she touched it. That moment is quick - a few minutes in a workday full of other things. She probably feels a mix of relief and something harder to name.

What happened in that moment is what you were building toward for two weeks. Not the change itself - the change is small. What happened is that the process became hers. She knows how to get a change into the repository. She knows who looks at it. She knows what the deployment looks like. She knows that when something breaks she has a path to getting help. She has done the thing the team does, and she has done it for real.

That is the difference between functioning and belonging. Belonging is not a feeling you produce by being warm enough in the welcome meeting, though warmth matters. It is a feeling that accumulates from evidence - evidence that the work is yours to do, that the team is yours to be part of, that your presence here was anticipated and is wanted. The two weeks of setup, the careful first task, the pairing, the ownership conversation, the on-call scaffolding - all of it is manufacturing that evidence.

By Friday of week two, Priya should not feel like she has finished onboarding. She should feel like she has started.
