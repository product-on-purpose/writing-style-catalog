---
entry_id: editorial
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# The Buddy Model Should Be Policy, Not a Pilot

*Northlane Systems Engineering - Editorial*

Every team at Northlane Systems, not just backend engineering, should onboard new hires with a named buddy and a scoped first task ready before day one. The documentation-only plan some teams are still weighing instead should not become policy anywhere in engineering.

The instinct behind that alternative is easy to understand. Hiring is picking back up across the industry, documentation scales in a way a senior engineer's attention does not, and a wiki page costs nothing to maintain next to two weeks of a buddy's focus. Backend engineering does not have to guess how the trade-off plays out. It has been running the alternative for a while, and the pattern keeps holding.

Priya Rao, the newest engineer on backend services, is the latest case. She joined the team on June 22 under the protocol it documented as ADR-0023: a named buddy, Arjun Nair, assigned from her first morning, an access checklist he owned, and a first real change scoped and waiting for her before she started. Her access and a working local environment were live by Monday afternoon of week one. She traced a live production request through the system before the week was out and could navigate the three services she would touch without hand-holding by then. In week two she opened her first pull request on July 1 and had it reviewed and merged by July 3, closing the two-week onboarding window on schedule, the same shape the protocol has produced before.

Documentation-only onboarding produces a different, well-known pattern instead. A new hire spends week one solving access problems alone, reluctant to interrupt busy teammates, and ships a first change in week three or four, if that. By then, whether they feel they belong has already been decided by the silence of the weeks before it. Documentation answers only the questions a writer thought to anticipate. It cannot tell a new engineer which part of the system matters this week, or which failure mode is common enough to worry about. A named buddy can, because he is there to be asked.

None of this is free, and it should not be sold as free. Arjun gave up real hours across those two weeks that he would otherwise have spent on his own work: an estimated 30-40% of his capacity in week one, 15-20% in week two. Sprint planning has to absorb that cost rather than pretend it away. But the cost does not disappear when a buddy is replaced with a wiki page. It only moves, unmeasured, into the weeks a new hire spends stuck and unsure whether a question is worth interrupting someone for. The belonging that follows is not a line item documentation can produce at all: Priya contributed to Friday's team sync in week one, and three teammates opened conversations with her that had nothing to do with the onboarding plan.

We are making this policy for every team at Northlane Systems, not a practice one part of engineering happens to run well. Every new hire gets a named buddy and a first real task scoped before their start date. Sprint planning books the buddy's reduced capacity as a known cost, not a surprise it discovers later. The documentation-only plan, whatever its appeal in a planning meeting, does not become policy anywhere in engineering. A wiki page can back up an onboarding plan. It cannot be one.
