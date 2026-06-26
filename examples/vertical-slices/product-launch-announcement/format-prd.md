---
entry_id: prd
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Tidemark v1.0 - Product Requirements

**Status**: `launch-ready` | **Author**: Priya Osei, Product | **Version**: 1.0 | **Target launch**: July 3, 2026

---

## Problem Statement

Small product teams - typically two to fifteen people - that conduct regular customer conversations face a structural failure: feedback arrives in fragments. A customer flags an issue in a support thread. A founder takes notes in a document during a sales call. A designer hears a pattern in a user interview and pastes a quote into a chat channel. Each signal is captured somewhere, but nowhere are they gathered, compared, and ranked against each other.

The PM or founder who owns the roadmap becomes the manual integration layer. They read across all these sources, de-duplicate in their head, and try to construct a priority order in a spreadsheet or a notes file. This process is lossy. It is slow. And it is invisible to the rest of the team: the engineer picking up the next sprint and the designer shaping the next flow cannot see what the feedback actually said or why the priorities landed where they did.

The result is three compounding problems:

1. Signal gets dropped because no one has bandwidth to re-read every source before a planning meeting.
2. Prioritization decisions look arbitrary to people who were not in every conversation.
3. Roadmaps drift from what customers actually said, because the synthesis lives in one person's working memory.

This pattern repeats every planning cycle for teams of this size. The bottleneck is not collecting feedback - it is synthesizing it into something a whole team can act on and defend.

---

## Goals

1. A team member can go from a pile of raw feedback themes to a ranked, shareable roadmap in under 30 minutes of active work.
2. The ranked themes are visible to every team member involved in prioritization decisions, without requiring a meeting or a forwarded file.
3. The reasoning behind the rank order is attached to the roadmap and travels with it, so that anyone who reads the roadmap can understand why it prioritized as it did.

---

## Non-Goals

For the v1.0 launch, Tidemark will not solve the following:

- **Integrations with external tools.** Feedback ingestion is manual or via CSV import only. Connectors to the ticket tracker, chat tool, CRM, or survey platform are deferred to a future release.
- **Automated AI synthesis of raw transcripts.** Tidemark does not process raw interview recordings or unstructured text. Users bring already-synthesized themes; the product helps them prioritize and share, not extract.
- **Enterprise authentication and access controls.** Single sign-on, role-based permissions, and multi-workspace administration are out of scope. Tidemark v1.0 is designed for teams of two to fifteen.
- **Analytics or usage data as a prioritization input.** Rank order is derived from the criteria the team sets, not from behavioral telemetry or product analytics feeds.
- **Notification or calendar integrations.** Alerts and reminders exist inside the product only. No email or calendar hooks in this release.

---

## User Stories / Jobs-to-be-Done

**Primary user: PM or founder on a small team**

- As a PM, I want to add the themes I pulled from customer conversations so that I have them in one place rather than distributed across documents and chat threads.
- As a PM, I want to apply my team's prioritization criteria to each theme so that the rank order reflects our actual decision framework, not a generic default.
- As a PM, I want to generate a shareable view of the ranked roadmap so that I can send it to engineers, leadership, and customers without reformatting.
- As a PM, I want to attach the source evidence behind each theme so that anyone reading the roadmap can trace a priority back to specific customer language.

**Secondary user: engineer or designer reviewing the roadmap**

- As an engineer, I want to see the reasoning behind each ranked priority so that I understand why we are building this item and not another one.
- As a designer, I want to add a newly discovered feedback theme to an existing roadmap without restructuring the whole document, so that the roadmap stays current without requiring PM intervention for every update.

**Secondary user: customer stakeholder receiving a shared roadmap**

- As a customer who gave feedback, I want to see how my input shaped the team's priorities so that I know my voice was heard and I can stay engaged with the product.

---

## Success Metrics

We will assess v1.0 success at 60 days post-launch against the following:

**Activation**
- The share of new signups who create at least one ranked roadmap within 7 days of signup. Baseline will be established from the first two cohort weeks; the target will be set once we have that baseline.

**Retention**
- Teams that created a roadmap in week 1 return to the product at least once in weeks 3 through 6.

**Shareability**
- The majority of teams that complete a ranked roadmap generate at least one shared link.

**Satisfaction proxy**
- In the first post-launch user survey, the ratio of respondents who say Tidemark replaced their previous feedback-synthesis process to those who say it did not exceeds 2 to 1.

**Failure signals** - these would trigger a priority reassessment:
- More than a third of users who start a roadmap abandon it before completing the ranking step.
- Inbound support volume about connecting to external tools exceeds a threshold suggesting that manual import is a real blocker, not merely an inconvenience.

---

## Open Questions

The following assumptions are load-bearing and have not been validated. Each is a risk that could require a pivot.

1. **Manual import is acceptable at launch.** The working hypothesis is that teams will tolerate pasting themes because the painful step is synthesis and prioritization, not collection. This has not been tested with high-volume teams that handle more than a few dozen feedback inputs per week.

2. **The PM or founder is the right primary user.** Discovery interviews skewed toward PMs and early-stage founders. We have not confirmed the value proposition holds for teams where a designer or an engineer owns the roadmap process.

3. **Sharing outside the team is a genuine use case, not an edge case.** Multiple discovery interviewees mentioned sending roadmaps to customers. We are building the shared-link feature on that signal, but we have not verified that outbound sharing is common enough at this stage to be a required capability versus a value-add.

4. **"Ranked roadmap" maps to a shared mental model.** Tidemark uses "ranked" to mean ordered by user-defined prioritization criteria. Several discovery participants used "ranked" to mean sequenced by delivery date. The distinction affects how the output is labeled and explained during onboarding. The terminology has not been tested with a naive user.

5. **30 minutes is achievable with the current onboarding flow.** The 30-minute activation goal is a hypothesis derived from the number of steps in the flow. No moderated usability test has been run end-to-end. If the first cohort data shows median time significantly above 30 minutes, onboarding is the first place to investigate.

---

**Owner**: Priya Osei | **Last updated**: June 26, 2026 | **Status**: `launch-ready`
