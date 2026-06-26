---
entry_id: pragmatic-architect
axis: voice
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

The goal for Priya's first two weeks is one shipped change to production, not orientation theater. I've seen two failure modes here: access limbo on day one where she can't do anything for three days while tickets sit in queues, and pairing that never converts to ownership. We avoid both with deliberate sequencing.

**Week one is infrastructure.** Get access provisioned before Monday morning, not during it. That means repository access, deployment credentials, and a working local environment verified by someone who ran it last week, not written six months ago. I will own the day-one walkthrough personally - not delegate it to a doc - because the questions that surface tell me what the setup guide is missing. The cost is an hour of my time; the failure mode of skipping it is Priya blocked for a day debugging stale instructions.

Pair her with one owner per service for context, not a parade of introductions. More than three "here's how this thing works" sessions in a week is cognitive overhead with no throughput benefit. The constraint here is working memory, not goodwill.

**The first change should be real but low-blast-radius.** A config tweak, a missing test, a small refactor in a service she has already read. Not a tutorial task. Tutorial tasks don't teach deployment mechanics - they teach nothing except that the team gives new engineers fake work. The negative: a real change might surface a gap in our onboarding coverage. That is information we want.

**On the belonging question:** it depends on whether she is included in on-call prep before she is on-call. Bring her into the weekly incident review as an observer starting week two. She reads the timeline, hears how we reason about failure, sees that blame is not the move. That signals membership more reliably than any all-hands introduction.

We debrief at end of week two. If she hasn't shipped, we find where the plan broke, not where she did.
