---
entry_id: public-statement
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

**Lattice Notify - Statement on the June 3 Notification Delivery Disruption**
June 4, 2026

Lattice Notify's notification service runs on PostgreSQL, and after reviewing what happened on June 3, we are keeping it there. The service was slow to deliver notifications for a little over two hours because a database configuration limit was set too low for the traffic we saw that day, not because PostgreSQL was the wrong platform, and that limit has already been corrected.

From 2:17 PM to 4:37 PM UTC on June 3, roughly two hours and twenty minutes, in-app, email, and Slack notifications were delayed for every active workspace on the Lattice Notify platform. No notifications were lost or sent twice, but for that window, the people who depend on our customers' products to notify them did not get notified when they should have. A surge of new workspace activity pushed the number of simultaneous operations against our notification database past the limit we had configured for it, and once that limit was hit, new notifications could not be accepted or sent until we intervened. A two-hour gap in notification delivery is a real problem for the teams who build on us and the people those teams serve. We are sorry for the disruption, and we are not treating it as minor.

We reduced the number of workers writing to the database to relieve pressure, which restored delivery at reduced speed within about an hour, then raised the configured operation limit to bring throughput back to normal and cleared the backlog of 14,200 queued notifications by 4:37 PM UTC. Since then, Jordan has been working on two fixes due June 10: raising that operation limit again, to twice our observed peak hourly rate, and adding hourly write-rate monitoring to our on-call dashboard. Ana is reviewing whether our launch capacity assumptions account for bursts like the one on June 3, with findings due June 17. Ana and Marcus are confirming, by June 24, whether the volume threshold we set for revisiting this database choice is still the right signal, or whether we need an additional one based on how concentrated the load gets within a given hour.

We chose PostgreSQL for this service because it let us build and run it with the team and the operational habits we already trust, and June 3 was a failure of capacity planning inside that choice, not a reason to abandon it. We will post an update once the monitoring and capacity work above is done. Until then, the standard we are holding ourselves to is the one we set when we made this decision: notification delivery that is reliable, on infrastructure we understand well enough to fix quickly when it breaks.

Ana Rivera
Tech Lead
Lattice Notify
