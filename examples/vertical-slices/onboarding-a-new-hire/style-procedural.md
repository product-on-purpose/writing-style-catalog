---
entry_id: procedural
axis: style
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Get Priya from day one to shipping her first real change by the end of week two.

**Before you begin**

- Priya's start date is confirmed as the coming Monday.
- You have permissions to request accounts on her behalf in the version control system, the ticket tracker, the deployment pipeline, and the monitoring dashboard.
- A small, scoped ticket sits unassigned in the backlog - one that touches a real code path but where a mistake reverts cleanly.
- One team member besides yourself is available to pair with Priya during week two.

**Week one: access, tooling, and orientation**

1. Submit account access requests for Priya in the version control system, the ticket tracker, the deployment pipeline, and the monitoring dashboard. Do this on Friday before her start date.

   Expected outcome: All four accounts are active by Monday morning, or by Tuesday at the latest.

2. Send Priya a welcome message in the chat tool before she logs in on Monday. Include the internal wiki URL, the onboarding checklist, and a link to your calendar so she can book time with you.

3. Walk through the team's local development setup guide with Priya on Monday morning. Sit with her rather than handing off the document.

   Expected outcome: Her local environment runs the service and she can reach a development endpoint.

4. Trace the path of one recent pull request with Priya, from the entry point to the response. Skip the full directory tour.

   Expected outcome: She can describe what the service does and where the code for one flow lives.

5. Walk Priya through the on-call runbook: who owns each service, how alerts route, and who to call if she is ever paged before she feels ready.

   Expected outcome: She understands the rotation schedule and knows she is not exposed alone.

6. Have Priya submit a pull request that adds her name to the team roster file - she types the commit message, creates the PR, and merges it.

   Expected outcome: She has walked the full deployment path before she owns a real change.

**Week two: first real change**

The pairing partner's role is to answer questions, not to type the solution. Agree on this with the partner before the session begins.

7. Assign Priya the pre-selected ticket and introduce her to her pairing partner.

8. Have Priya manage her own pull request - she writes the description, assigns reviewers, and responds to comments herself.

9. When the change ships, post an acknowledgment in the team chat that names the ticket and names Priya.

   Expected outcome: The team sees her as a contributor, not an observer.

Priya has shipped a real change to production and the team has recognized it; the two-week onboarding is complete.
