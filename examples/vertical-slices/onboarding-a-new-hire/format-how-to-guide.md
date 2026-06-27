---
entry_id: how-to-guide
axis: format
topic_slug: onboarding-a-new-hire
topic_label: Getting a new engineer productive in their first two weeks
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to run the two-week new-engineer onboarding protocol

## Before you begin

- You are the named onboarding DRI or buddy for this hire. One person owns this; split ownership does not work.
- The new engineer's start date is confirmed and you know it at least five business days in advance.
- You have sprint authority to commit 30-40% of your week-one capacity and 15-20% of your week-two capacity to this work. If you do not, block the protocol until that is resolved.
- You have access to the access request portal, the team's `good-first-issue` ticket backlog, and the `#backend-services` chat channel.

## Overview

This guide walks you through the two-week protocol for getting a new backend engineer - in this case Priya - from day-one access gaps to a merged pull request and a first production deploy. When you finish, Priya will have a working local environment, a read of the codebase, one real change shipped, and the social footing to keep going without a buddy.

## Step 1: Pre-scope the first change before day one

If you wait until Priya arrives to pick her first ticket, week two loses a day of setup. The team needs to decide in advance.

Browse the `good-first-issue` backlog and identify a ticket that touches one service and one data model, has a test that can be written in under an hour, and carries no on-call risk if something goes wrong. Note it as Priya's week-two task and confirm with the team that it will not be picked up by someone else in the interim.

You have done this step correctly when you can name the ticket, say what it changes, and explain why it is safe for a new engineer to own.

## Step 2: Open access on day one (days 1-2)

Access gaps on day one are the single most common cause of a new engineer feeling invisible before week one ends. Your job is to make sure Priya leaves day one with every credential and channel already working.

Request any of the following that are not yet provisioned through the IT portal:

- Source control org membership
- VPN credentials and SSO setup
- CI/CD pipeline access
- Observability platform (logs, traces, metrics)
- On-call rotation viewer (she does not go on-call until week five)
- Secret manager read access for staging
- Chat channels: `#backend-services`, `#incidents`, `#deployments`, `#team-random`

Walk Priya through the bootstrap script yourself rather than handing her a doc and walking away:

```bash
git clone git@source.example.internal:backend/services.git
cd services
./scripts/bootstrap.sh
```

Then run the quick-start together and confirm the smoke test passes:

```bash
make start-local
make smoke-test
```

You have done this step correctly when `smoke-test` passes and Priya can describe what each access item does. A credential she has but does not understand is a gap that surfaces later.

## Step 3: Run week-one orientation (days 3-5)

The goal of week one is orientation, not output. Three things need to happen before Friday.

**Trace the system.** Sit with Priya as she reads `docs/architecture-overview.md` and `docs/service-map.md`, then open the observability platform and trace one real production request together - from the API gateway to the data store. This makes the architecture concrete rather than abstract.

**Introduce the owners.** Pull up `docs/ownership.md` and identify the three teammates whose services Priya will most likely touch. Facilitate brief one-on-ones early in the week - these matter more than any doc.

**Watch a deploy.** Arrange for Priya to pair with whoever is on-call for at least one daily deploy before Friday. Watching it once removes most of the mystery.

You have done this step correctly when Priya can navigate the codebase without prompting and can describe the ownership structure of the services she will touch.

## Step 4: Hold the Friday week-one check-in

A structured check-in prevents small gaps from becoming blockers that you only discover on Monday of week two.

On Friday afternoon, sit with Priya for thirty minutes. Cover three questions: Is anything blocked? Can she navigate the codebase independently? Is there anything missing from the access list? Write down what she says - not your interpretation of it.

If anything is blocked, own the resolution before end of day Friday. If staging access is still pending (the infra queue can be slow), flag it explicitly: Priya needs her own staging credentials before the on-call alert drill scheduled for week two.

You have done this step correctly when you have a written note of any open items and a named next action for each one.

## Step 5: Hand off the first real change (week two, day one)

Handing off a pre-scoped task on the first day of week two is what makes the rest of the protocol work. If the task is not ready, the week drifts.

Open the ticket you identified in Step 1 and walk Priya through it: what it changes, why the service behaves the way it does, and what a correct outcome looks like. Then hand it to her. She drives from here.

You have done this step correctly when Priya opens her branch the same day and can explain the change to a third person without your help.

## Step 6: Pair on review and lead the first deploy

Priya should have a pull request open by Wednesday of week two. Your role is reviewer and pairing support - not co-author.

Review the PR with the same standards you would apply to any teammate's change. Note what is working as well as what needs revision. When the PR is approved, Priya does the deploy. Arjun can pair as additional support if she wants it, but she owns the controls.

You have done this step correctly when the change is merged, Priya's name is in the deployment log, and she can describe what the deploy process does.

## Step 7: Run the two-week retrospective

On Friday of week two, hold a thirty-minute retrospective with Priya. The functional close is straightforward: confirm the PR is merged, confirm access is complete, and identify any remaining gaps.

The belonging question matters more and is easier to skip. Ask it directly: does she feel she belongs on the team, or does she feel she is functioning on the team? These are different. Functional progress does not answer the belonging question.

You have done this step correctly when you have a written answer to both questions and a plan for anything still open.

## Troubleshooting

**Access request stuck in the infra queue.** Do not wait. Submit the request and set a calendar reminder for two business days out. If it is not resolved, escalate through the engineering manager. Staging access in particular must be live before any on-call drill.

**The pre-scoped ticket was picked up or blocked before week two.** Find a replacement before Monday morning of week two. Apply the same criteria: one service, one data model, safe to fail. Do not let Priya start week two without a task in hand.

**Priya is not navigating the codebase independently by end of week one.** Extend the orientation window by two to three days before moving to the first change. Do not push the week-two protocol forward if the week-one foundation is not solid - the first change will become a frustration rather than a success.

**Sprint pressure is pulling you away.** Surface this to the engineering manager immediately. The protocol requires 30-40% of your week-one capacity. If the sprint does not account for this, the onboarding fails quietly and the cost lands elsewhere.

## Next steps

Once the two-week window closes, the formal onboarding is done but the relationship usually is not. The buddy relationship tends to become an informal mentorship channel - treat that as expected rather than scope creep.

The next formal milestone is week five, when Priya joins the on-call rotation. Before then, schedule the on-call briefing (alert routing and escalation drill) and confirm she has reviewed `docs/on-call-runbook.md`.

For the reasoning behind this protocol's design choices, see the team ADR on structured guided pairing.
