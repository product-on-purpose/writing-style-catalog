---
entry_id: first-principles-derivation
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-5-5
review_status: reviewed
---

Priya starts on Monday, June 22. Before choosing how to onboard her, this piece lists what we take as given, derives a plan from those premises alone, and names the one premise the plan cannot survive losing.

**Premises**

Grant or refuse each one separately. Nothing below is built on a premise you have not seen.

- **P1.** The team deploys to production every day. This is an observation about our own cadence.
- **P2.** A new engineer cannot see most of her own blockers until someone who knows the system is standing next to her. A missing VPN certificate step is an example: she does not know it is missing, only that nothing works.
- **P3.** A new engineer who is stuck and unsure of her standing will usually wait rather than interrupt busy teammates. This is an observation from earlier hires, not a measurement.
- **P4.** By the end of week three, how a new engineer feels about her place on the team has largely been set by what happened, or failed to happen, before then.
- **P5.** A buddy's time is not free. Input: we estimate the buddy loses 30 to 40 percent of their output in week one and 15 to 20 percent in week two.
- **P6.** Priya stays out of the on-call rotation for her first 30 days, so nothing she changes in two weeks may carry on-call risk.

**Derivation**

*Step 1, from P1.* A change merged and deployed inside her first ten working days is possible, because the pipeline imposes no delay of its own. The open question is what stops it from happening.

*Step 2, from P2 and P3.* Blockers are invisible to her, and she will not announce them. So a blocker can sit unreported for as long as nobody is beside her. The delay between her first day and her first change is therefore set by how long her blockers go unseen, and not by how hard the change is.

*Step 3, from Step 2.* The way to shorten that delay is to put a person who can see the blockers next to her during the first days. That person must be named in advance, because an unnamed role is a role nobody fills when the sprint gets busy.

*Step 4, from P4 and Step 1.* Since the feeling of belonging is largely set by week three, and a deployed change is possible inside week two, a first change that lands in week two reaches her before the setting happens. A change that lands in week four arrives after it. The first change should therefore be fixed before she arrives, so that it is ready on day one and does not wait for her to find one.

*Step 5, from P6 and Step 4.* The pre-scoped change must touch one service and carry no on-call risk if it goes wrong. This narrows the choice to a small, bounded task, which Mei and Arjun can pick before June 22.

*Step 6, from P5, with the arithmetic done here.* Over ten working days, a buddy who gives 30 to 40 percent in week one and 15 to 20 percent in week two spends 5 x 0.30 + 5 x 0.15 = 2.25 days at the low end and 5 x 0.40 + 5 x 0.20 = 3.0 days at the high end. At the midpoints, 5 x 0.35 + 5 x 0.175 is about 2.6 days. The whole plan costs between two and a quarter and three buddy-days. That is real, and it must be written into sprint planning, or the cost is paid silently and the plan fails without anyone deciding it should.

*Step 7, from Steps 3, 4, 5 and 6.* The plan that follows from the premises has four parts. A named buddy, Arjun, owns access and tooling checks in days one and two. A first change is scoped before the start date. Priya drives it, Arjun reviews and pairs on blockers, and she runs the deploy herself. The buddy's reduced capacity is budgeted in the sprint, in advance.

**Conclusion**

A named buddy plus a pre-scoped, low-risk first change, merged in week two and costing about two and a half buddy-days, is what these premises entail. Priya's first pull request is due Wednesday, July 1, and the merge Friday, July 3.

**The premise to push on**

The load-bearing premise is P2. Steps 2 and 3 rest on it, and Steps 4 to 7 rest on those. If new engineers can in fact see and report their own blockers, then the buddy buys little, the cost in P5 is not worth paying, and a written runbook with a pre-scoped task would reach the same result for less. P4 is the second place to push: if belonging is not largely settled by week three, the urgency of a week-two change falls away, though the case for removing hidden blockers survives it. P5 is an estimate, and if it were double, Step 6 would give roughly four and a half to six days, and the plan would need a cheaper form of the buddy role.
