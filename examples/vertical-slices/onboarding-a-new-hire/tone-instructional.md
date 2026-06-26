---
entry_id: instructional
axis: tone
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

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
