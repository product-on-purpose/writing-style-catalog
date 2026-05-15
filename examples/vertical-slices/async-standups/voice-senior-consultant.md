---
entry_id: senior-consultant
axis: voice
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

Before recommending a structural change, it is worth asking what job the current standup is being hired to do. In my experience, daily standups perform some combination of four functions: status broadcasting, blocker surfacing, coordination of dependencies, and team cohesion. These are distinct jobs. A single ritual rarely does all four well, and the right design depends on which function is load-bearing for this team.

The data you have shared is suggestive. Attendance asymmetry (3.2/5 for India versus 4.6/5 for US) tells me the cohesion function is already compromised for roughly a quarter of the team. The 14-minute average with an estimated 4 minutes of signal suggests the status-broadcast function is operating at low information density. The recurring rediagnosis of previously-solved problems indicates that whatever is happening verbally is not being captured durably, which is the canonical failure mode of synchronous-only knowledge work in distributed teams.

The strongest read of the data suggests that the standup, as currently structured, is primarily delivering cohesion to the six engineers in US timezones at the cost of the three in India and, secondarily, the two in the UK. The other three jobs (status, blockers, coordination) are being delivered inefficiently to everyone.

The proposed redesign is sensible because it separates the jobs. Async posts handle status and blockers, with the additional benefit of persistence (which addresses the rediagnosis problem). The 60-minute Thursday working session, properly structured, can carry the coordination and cohesion load. I would, however, flag two design questions the current proposal does not resolve.

First, what is the Thursday session actually for? "Working session" is a placeholder. Without an explicit purpose - dependency mapping, deep-dive on one issue, architectural discussion - it will default to "longer standup," which optimizes nothing. I would recommend the manager publish an intent for that hour before the trial begins.

Second, what is the @mention discipline for blockers? Async surfacing only works if the @mentioned engineer commits to a response SLA. Without one, blockers will sit in the channel and the rediagnosis problem will simply migrate.

Recommendation: proceed with the trial. Before Monday, specify (a) Thursday session purpose, (b) blocker response SLA, and (c) the two or three metrics that will inform the day-30 decision. The revert clause is good practice; treat it as a real option, not a face-saver.
