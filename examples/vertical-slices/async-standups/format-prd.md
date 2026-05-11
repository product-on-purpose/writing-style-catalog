---
entry_id: prd
axis: format
topic_slug: async-standups
topic_label: Should we adopt async-first standups?
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Async Standup Bot - Product Requirements

## Problem Statement

Engineering teams using Slack for team communication have no structured way to run async standups within the tool they already use. Current approaches require either a separate SaaS product (Geekbot, Standuply), which adds cost and context-switching, or a manual template posted to a channel, which requires someone to enforce the format and generates no structured data. Teams that need to review standup history, track blocker patterns, or report on team activity cannot do so without manually reading thread-by-thread.

The users who feel this most are engineering managers and team leads at companies with distributed teams (at least two timezones). They run standups daily. They need blockers to surface and resolve without requiring a meeting. They cannot afford a per-seat SaaS subscription for a feature they could implement natively.

## Goals

- Enable any Slack workspace to run structured async standups with no external tool
- Reduce time-to-resolution for blockers by routing them to the named person via direct @mention
- Produce a structured weekly digest that engineering leads can use for 1:1 and planning prep
- Support teams of 4 to 50 engineers without configuration complexity

## Non-Goals

- This release does not replace synchronous standup tooling (Zoom, Meet integrations)
- This release does not include time-tracking or sprint velocity metrics
- This release does not support custom standup prompts in v1 - the three-field template is fixed
- This release is not intended for non-engineering teams (sales, marketing standup formats are different)

## User Stories

- As a team lead, I want to configure a standup channel and prompt schedule once so that I am not manually reminding my team to post each day
- As an engineer, I want to post my standup update in a format that takes less than two minutes so that the daily ritual does not feel like overhead
- As an engineer with a blocker, I want my blocker to reach the specific person who can help so that I am not waiting for them to notice it in a channel they may not read attentively
- As a team lead, I want a weekly summary of standup activity so that I can see blocker patterns and prepare for 1:1s without reading 50 individual posts

## Success Metrics

- Average time from blocker posted to first response from @mentioned person: target under 30 minutes during business hours
- Daily participation rate: target 85% of team posts on any given weekday
- Setup time: a team lead can configure and launch a standup channel in under 10 minutes
- Weekly digest open rate: target 70% of team leads open the digest within 24 hours of delivery

## Open Questions

- Does the bot need to handle engineers across more than two timezones in a single team? If so, how does the "post by 10am local" constraint work when "local" varies by 13 hours?
- Should the bot send direct reminders to engineers who have not posted by their deadline, or only post a channel reminder?
- What happens when someone is out of office - does the bot need OOO awareness, or does the team handle this manually?
- Is there a meaningful integration with GitHub or Jira that would let the bot pre-populate the "shipped" field from closed PRs or resolved tickets?
