---
entry_id: landing-page
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Ship notifications your customers actually see

**In-app, email, and Slack delivery in one SDK, running on infrastructure we already trust with our own production traffic.**

Lattice Notify is the notification layer for teams who would rather ship their product than build a delivery pipeline. Drop in one SDK and your app can send in-app, email, and Slack alerts within days, on infrastructure our own engineers already trust with their own production traffic. No queue to build, no fanout system to design, no second database for your team to learn.

## What you get

- **Ship in days, not a quarter.** Integrate the NotifyClient SDK and start sending in-app, email, and Slack notifications without building a queue, a fanout system, or a delivery pipeline yourself.
- **Alerts that actually arrive.** Sub-second p95 delivery, already proven at 500K events a day in our own production traffic, so your users see the moment that matters when it happens.
- **One less system for your team to run.** The pipeline runs on infrastructure we already operate in production. You are not adopting a second database or standing up a new on-call rotation to support it.

You are not the first traffic this pipeline has carried. It runs on the same production Postgres cluster we already operate for Lattice Notify's core product, handling 500K events a day today with a documented path past 5 million. We picked boring, proven infrastructure on purpose, and our own 4-person on-call rotation is the first line of defense on it, every day, before your traffic ever touches it.

## The question every team asks before switching

**What happens when we outgrow you?**

We asked ourselves the same question before we picked our own database, and we answered it with a number instead of a guess. The pipeline runs comfortably at 500K events a day today, we have a documented plan for the next order of magnitude, and we chose infrastructure our own on-call team already trusts over a system optimized for one access pattern and untested at 2 a.m. If your traffic grows, our scaling plan grows with it. You are not the one who finds our limits.

**[ Request early access ]**

Two minutes to request access. We will follow up to schedule your onboarding call before general availability opens.

## Frequently asked

**When can we start sending real traffic?**
Early access opens on a rolling basis over the next few weeks, ahead of general availability. Teams who request access now get the first onboarding slots.

**What channels are supported at launch?**
In-app, email, and Slack, all through one SDK integration. Additional channels ship after general availability.

**Do we need to change our own infrastructure to use this?**
No. You call the SDK. Everything downstream, including queueing, delivery, storage, and retries, is ours to run and own.

**[ Request early access ]**

Six weeks from now this is live. The teams who get in during early access are the ones who shape how it works.
