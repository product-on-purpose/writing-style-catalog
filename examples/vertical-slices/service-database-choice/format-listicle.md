---
entry_id: listicle
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# 6 Reasons We Picked Postgres Over DynamoDB for Our Notification Service

I walked into Wednesday's architecture meeting expecting to lose the argument. DynamoDB fit the notification service's access pattern on paper: write-heavy traffic, point-lookups by user ID, scaling nobody has to babysit. We still shipped on Postgres, and here's what actually tipped it, now recorded in ADR-0023 for anyone facing the same fork.

1. **Our on-call rotation only has four people.**
   Eight backend engineers, four of us on rotation, and every new datastore adds a second runbook, a second monitoring surface, and a second debugging skillset on top of the one we already carry. I have paid that tax before on a different project and still remember what it did to my sleep. Postgres kept the rotation one datastore deep.

2. **We were sizing for a deal that hadn't closed.**
   The case for DynamoDB leaned on a 10x growth scenario tied to the pending Slack-partnership deal. Designing around the bigger, uncertain number instead of the smaller, certain one (500K events a day at launch) optimizes for a future that might not show up. If the deal closes, we revisit; until then, we build for the traffic we actually have.

3. **Every join we needed was already in SQL.**
   Notifications don't live alone; they join against users, accounts, and workspaces in the same monolith Postgres already serves. Keeping the new `notifications` schema in the primary cluster meant those joins stayed plain SQL instead of a fan-out across two systems. DynamoDB's fit for the access pattern was real, but it would have pushed every cross-entity query into application code.

4. **The DynamoDB spike wasn't wasted effort.**
   Marcus built the spike in `experiments/notify-ddb/`, and it did what a good spike should: confirmed DynamoDB handles our write-heavy, point-lookup pattern natively, and put a real number on the operational cost of adding it. He made the stronger technical argument, and I still think he was right about the fit. Losing that argument didn't waste the work; if we ever cross the revisit threshold, his spike is the starting point, not a fresh investigation.

5. **We wrote down the number that changes our mind.**
   Instead of leaving "revisit DynamoDB" as a someday, ADR-0023 names a threshold: 5M events a day, sustained. Below it, the operational simplicity of one datastore wins by default. At or above it, the decision reopens automatically instead of depending on someone remembering to raise it.

6. **Shipping on familiar ground bought us three weeks.**
   Nobody on the team had run DynamoDB in production; everybody had run Postgres at this scale before. That gap alone was worth an estimated three weeks to first production traffic, because we weren't learning a new operational model while also hitting a launch date. Familiar tools are a legitimate input to a datastore decision, not a concession to laziness.

If you're staring at the same fork, run the spike on the option you're tempted by, then ask who's actually on call for the answer you don't pick. The database that wins is rarely the one with the better fit on paper - it's the one your team can operate at 3am.
