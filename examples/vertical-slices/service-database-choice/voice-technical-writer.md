---
entry_id: technical-writer
axis: voice
topic_slug: service-database-choice
topic_label: How to choose between Postgres and DynamoDB for a new service
author_type: llm
llm_model: claude-opus-4-7
generated_at: "2026-05-16"
review_status: reviewed
---

## Technical Writer on: Choosing between Postgres and DynamoDB

Use this guide to compare Postgres and DynamoDB for the Lattice Notify notification service. Bring the completed comparison to the architecture meeting on Wednesday at 2pm Pacific.

### Before you start

Confirm the following facts about the service:

- Expected volume at launch: 500K events per day
- Growth scenario: 10x within 12 months if the Slack partnership closes
- Current ops surface: Postgres only, supported by a four-person on-call rotation
- Decision deadline: Friday

### Compare the options

Evaluate each candidate against the same four criteria.

1. **Fit for access pattern.** Describe how the notification service reads and writes data. Note whether the pattern is key-lookup, range scan, or relational join.
2. **Operational load.** List the new monitoring, alerting, backup, and on-call procedures the team must own.
3. **Team skill.** Rate the team's current proficiency on a 1-5 scale. Note who would lead the learning effort.
4. **Reversibility.** Estimate the rework cost if the team migrates away from this option in six months.

### Record the comparison

For each option, write one paragraph per criterion. Keep paragraphs to three sentences. Cite the source of any volume or latency numbers.

| Criterion | Option A: Postgres | Option B: DynamoDB |
|---|---|---|
| Access pattern fit | | |
| Operational load | | |
| Team skill | | |
| Reversibility | | |

### Make the recommendation

State the recommendation in one sentence. Follow with the two strongest reasons. List the open questions that would change the recommendation if answered differently.

Send the completed document to Ana, Marcus, and Priya by end of day Tuesday.

**Note:** If you cannot complete the comparison by Tuesday, message Priya before Wednesday morning. Do not delay the Friday decision by arriving at the meeting with an incomplete comparison.
