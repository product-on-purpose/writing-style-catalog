---
entry_id: definitional
axis: style
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

A live-system rebuild is a project defined by one constraint that makes everything else harder: the system being replaced must remain operational throughout the build. That constraint is not incidental to the work - it is the definition of the work. Remove it and you have a different kind of project entirely.

Vantable's checkout rebuild ran under this constraint for fourteen months. The team's mandate was to fix a chronic cart-abandonment problem that had accumulated across product generations. The fix required rebuilding the checkout from scratch while every customer kept purchasing throughout. Those two requirements held simultaneously, and their combination produces the facets that define this category of work:

**Dual load.** The team maintained two systems at once - patching the old checkout in production while building the new one - without letting either deteriorate from divided attention. A project that feels half as hard is usually carrying only one load.

**Commitment under uncertainty.** At two points - month four and month eleven - earlier decisions had foreclosed paths that turned out to be necessary. Priya Osei and Marcus Vela made the calls to adapt rather than unwind: expensive, disruptive, correct. A live rebuild does not let you restart. It lets you adapt in place.

**An invisible finish.** Sloane Adeyemi ran the final rollout in segments over four days, routing traffic incrementally rather than staging a single all-or-nothing switch. The checkout held under peak load. Customers encountered nothing. When this kind of work is done correctly, that is exactly what done looks like from outside.

**What does not count**

A team that rebuilds a system on a staging environment and then deploys during a scheduled maintenance window is not doing a live rebuild, even if the deployment is risky. The distinguishing condition is sustained parallel operation, not a high-stakes cutover moment. A team that runs two versions behind a feature flag while allowing the old one to degrade is doing a phased deprecation. The old system must be held to production standards throughout.

The Vantable project slipped its launch twice. Both slips arose from the same source: the production constraint changed the requirements in ways the plan had not accommodated. A project that slips because the production constraint keeps evolving is exhibiting the defining characteristic of its category.

A live-system rebuild is complete when the replacement runs at full production load, the old system is decommissioned, and no user encountered the seam. The Vantable team reached that state at the end of the fourteenth month. What makes the achievement worth naming precisely is that this class of project is survivable - and this team has now demonstrated what surviving it actually requires.
