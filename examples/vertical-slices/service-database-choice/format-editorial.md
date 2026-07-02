---
entry_id: editorial
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# The Boring Datastore Was the Right Call

*The Editorial Board - Lattice Notify Engineering*

The notification service will run on Postgres, not DynamoDB, and the reasoning behind that call deserves to be stated as standing policy, not filed away as a single decision. When a new access pattern argues for a new datastore, the burden of proof belongs to the datastore. It does not belong to the team that already knows how to run what it has.

The choice looked closer than it should have. The notification service needs to sustain 500K events a day at launch, with a 10x growth scenario on the table if the pending Slack-partnership deal closes within the year. DynamoDB fits that access pattern well: write-heavy, point-lookups by user, scales without an operator paged at 2 a.m. Postgres fits the team: eight backend engineers, a four-person on-call rotation, and years of production experience running exactly this kind of workload on exactly this kind of cluster. Marcus argued the DynamoDB case on its technical merits, and he was not wrong to. Ana argued the operational case, and Wednesday's architecture meeting confirmed which argument was load-bearing. The decision, recorded in ADR-0023, is Postgres: a new schema on the existing primary cluster, a job queue built on `pg_notify`, and a documented threshold - 5M events a day, sustained - at which the team revisits DynamoDB before pushing the Postgres path any further.

That threshold is the part worth generalizing. A four-person on-call rotation does not experience a second production datastore as a technology upgrade. It experiences it as a second runbook, a second monitoring surface, a second backup story, and a second debugging skillset that has to be current on every page, at every hour, for every engineer in the rotation. That cost does not show up in an access-pattern comparison, and it will not show up in a benchmark. It shows up at 2 a.m., months later, when the person on call has to remember how a system they rarely touch actually fails. Weighed against that, a growth scenario tied to a deal that has not closed is not a design input. It is a possibility, and possibilities belong in a threshold, not in an architecture.

The reversibility math backs the same conclusion. Outgrowing Postgres costs an estimated three to six weeks of migration work. Choosing DynamoDB and discovering the team needs cross-database joins after all costs a similar window, plus a team that spent that time learning the wrong tool for problems it did not have yet. When the cost of being wrong is roughly symmetric, the tie goes to the option the on-call rotation can already operate.

None of this makes DynamoDB the wrong technology. It makes it the wrong technology to adopt speculatively, ahead of the load that would justify it, by a team that would be learning it and operating it for the first time under production pressure. That distinction should outlive this one decision. We are asking every team facing a similar build to bring a number, not a vibe, to the datastore question: state the operational cost of the second surface plainly, name the threshold at which the access-pattern argument starts to win, and write that threshold into the ADR where it can be checked later instead of argued again from scratch. The notification service now has one. Every service that follows it should too.
