---
entry_id: manifesto
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# The Boring Infrastructure Manifesto

*Ana Rivera, on behalf of the notification-service team - Lattice Notify Engineering*

We almost adopted a second production database this month for reasons that sounded airtight in a design review and stopped sounding airtight the moment someone asked who would carry the pager for it. We did not adopt it. But coming that close, on a team that already knew better, told us this was not a one-time lapse in judgment. It is a pattern, and until now we had never written down what stops it. This is that document.

## What we believe

**We build for the team we have.** Eight backend engineers hold a four-person on-call rotation for everything Lattice Notify runs in production. Every system we add is a system one of those four people operates half-asleep during an incident, not a system judged once in a design review and forgotten. We size our architecture to the roster we have, not the team a future deal might buy us.

**We design for the load we can measure.** Five hundred thousand notification events a day is real traffic, arriving now. Ten times that is a scenario tied to a Slack partnership that has not closed. A scenario earns a plan and a number to watch. It does not earn a vote equal to the traffic already hitting our servers.

**We put a number on every "not yet."** Five million events a day, sustained, is when we reopen the DynamoDB question for the notification service. We do not relitigate a decision from memory in a hallway conversation six months from now, and we do not pretend the decision is permanent either. We write the number down once, and we honor it when it arrives.

**We price reversibility before we commit.** Outgrowing Postgres costs us three to six weeks of migration we can see coming and plan around. That is the number that let us commit with confidence. We do not choose a direction whose cost of being wrong we have not already named.

**We say the other side's best argument out loud.** Marcus built the strongest technical case in the room for DynamoDB's fit with our access pattern. We said so, in the same meeting where we chose Postgres anyway. A team that cannot state its opponent's best argument has not tested its own belief, it has only repeated it to itself.

**Every decision gets one owner and one document.** ADR-0023 exists so Priya, Marcus, Sam, and Jordan all know exactly what we decided, why, and what has to happen before we decide differently. A decision that lives only in a meeting is a decision the team will make again, worse, under more pressure, with fewer of the people who made the first case still in the room.

## What we stand against

We stand against choosing infrastructure for the design review instead of the pager. We stand against sizing systems for a deal that has not closed while the load that has already arrived waits for a plan. We stand against decisions that live in one meeting and evaporate the moment someone changes teams. We stand against treating "best tool for the access pattern" as a complete answer, when it is one input into a larger one. We stand against collecting a datastore for every access pattern until the on-call rotation is defending four unfamiliar systems at three in the morning instead of one familiar one.

## What we stand for

We stand for operational simplicity as a requirement we weigh first, not a tiebreaker we reach for last. We stand for a documented threshold attached to every deferred decision, not a future argument replayed from scratch. We stand for one owner and one written record per decision, so the team six months from now inherits a reason, not just a result. We stand for naming the argument we did not take, on the record, so the decision can be reopened honestly when the world changes, not reopened out of frustration or forgetting. We stand for choosing the tool that turns our team's existing competence into an advantage over the tool that turns that same competence into a rebuild.

## What we're committing to

Starting now, every datastore or major infrastructure decision at Lattice Notify Engineering gets this same treatment, not only the ones that happen to involve a database. A written threshold. A named owner. An ADR that outlives the meeting where the decision got made. The counter-argument, stated in full, on the record.

We are asking something specific of the people closest to this one. Sam and Jordan: when you build the `notifications` schema and wire the on-call dashboard to watch it, treat the five-million mark as a commitment we will act on, not a number we wrote down to end a meeting. Priya: when you lock this Friday, hold the ADR as the actual contract, not a summary of what got said. Marcus, and every engineer who brings the next exciting tool into a design review: make the boring case first, out loud, before you make the exciting one. If the boring case cannot survive being said out loud, it was never the boring case. It was habit, wearing the boring case's clothes.

We are not only choosing Postgres today. We are choosing, from today forward, to be a team that can tell you exactly why.
