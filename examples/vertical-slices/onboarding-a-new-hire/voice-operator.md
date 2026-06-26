---
entry_id: operator
axis: voice
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Priya started Monday. She needs to ship a real change by end of week two. Here is how we make that happen.

**Day 1: Access and tooling**

Tomasz owns the access runbook. He walks Priya through it the morning she arrives. By noon she has working credentials for the code repo, the ticket tracker, the deployment system, and the chat tool. If any provisioning request takes more than two hours, Tomasz pages the platform team directly - not a ticket, a page. By 5pm, Priya can clone the primary service repo, run the test suite, and read the deployment log for the last three releases. Those are the three checks. If she cannot do all three, we stop and fix the blocker before anyone goes home.

**Days 2-3: Orientation**

I walk Priya through the service map on day two. We start with the boundary between the ingestion service and the processing service - that is where most production incidents originate. She reads the last five postmortems before we meet. She already knows the shape of what breaks before I explain the system.

On day three, Priya pairs with Kenji on a ticket tagged good-first-change. Kenji drives. Priya asks questions. She reads the deployment runbook before anything ships.

**Week 2: First real change**

Priya picks the ticket. Kenji reviews. She drives the deployment herself and watches the dashboards through the full five-minute post-deploy window. The change does not need to be large. It needs to be real.

On day ten, Priya joins the on-call rotation as a shadow with Kenji as backup. By day fourteen she knows who owns what and what number to call when it breaks.

**The human side**

Kenji takes Priya to lunch on day three. I check in one-on-one at the end of each week - not a status call, a real conversation. We name the things that are hard. Functional and welcome are not the same state, and both are on the plan.
