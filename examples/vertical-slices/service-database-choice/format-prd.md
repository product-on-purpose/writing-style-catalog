---
entry_id: prd
axis: format
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

# Lattice Notify Notification Service - Product Requirements

**Author:** Priya Shah (PM)
**Engineering lead:** Ana Rivera
**Date:** 2026-05-14
**Sprint target:** 2026-05-25 week
**Decision dependency:** Datastore choice (Postgres vs DynamoDB) locked at the 11am Friday 2026-05-16 sync; this PRD assumes Postgres per ADR-0023.

## Problem Statement

Lattice Notify users currently receive product activity (mentions, comments, status changes) only through the monolith's polling-based feed. The feed updates every 60 seconds, which our users have rated 3.1/5 on responsiveness in the last two quarterly NPS cycles. Account-level usage data shows that customers on larger teams (>50 seats) churn 2.3x more often than smaller teams, and churn interviews consistently surface "I missed something important because the notification was late" as a top-three reason.

The product needs a real-time notification system - sub-second delivery for in-app surface, sub-5-second delivery for email and Slack push - that serves the 500K notification events/day Lattice Notify generates today, with headroom for the 10x growth scenario over the next 12 months if our Slack-partnership deal closes.

## Goals

- Deliver in-app notifications with p95 latency under 1 second from event to surface
- Deliver email and Slack push notifications with p95 latency under 5 seconds
- Support the 500K events/day launch volume at the SLOs above with no manual intervention from the on-call rotation
- Increase notification responsiveness NPS subscore from 3.1 to 4.0 within 90 days of launch
- Ship to general availability within 6 weeks of sprint kickoff

## Non-Goals

- Notification preferences UI beyond the existing per-channel toggles (deferred to next quarter)
- Push notifications to native mobile apps (no mobile clients exist yet)
- Cross-workspace notification routing (single-workspace scope for v1)
- Historical notification search beyond 90 days (use existing audit log for older items)
- Replacing the polling feed (it stays as a fallback for the first 90 days post-launch)

## User Stories / Jobs-to-be-Done

- As a Lattice Notify user on a team of 100, when a teammate mentions me in a comment, I want the notification to appear in my in-app inbox within a second so I can respond before the conversation moves on.
- As an admin on a team of 200, when a workspace-wide status change occurs, I want to receive a single consolidated notification within 5 seconds so my inbox is not buried.
- As an on-call engineer at Lattice Notify, when notification volume spikes 5x, I want the system to absorb the load without paging me so I can keep my night.
- As a Lattice Notify product manager, when the Slack-partnership deal closes and traffic grows 10x, I want a documented decision point about when to revisit the datastore choice so we are not blindsided by a scaling wall.

## Success Metrics

- p95 in-app notification latency under 1 second, measured continuously and reported in the weekly status report
- p95 email and Slack push latency under 5 seconds
- Notification responsiveness NPS subscore reaches 4.0 within 90 days of launch
- Zero data-loss incidents in the first 90 days of production
- On-call pages attributable to the notification service: under 2 per month after the first 30 days

## Open Questions

- At what sustained event volume should we revisit the Postgres vs DynamoDB decision? ADR-0023 proposes 5M events/day; this PRD inherits that threshold pending Friday lock-in.
- Should notification preferences live in the notification service's database or stay in the monolith user table? Ana to propose by sprint kickoff.
- What is the deprecation path for the polling feed after the 90-day fallback window? Priya to draft a follow-up PRD by 2026-06-15.
- How do we handle the partnership-deal trigger if it lands before we cross the 5M revisit threshold? Open with Priya and the partnerships team; not blocking this release.
