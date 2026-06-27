---
entry_id: retrospective
axis: format
topic_slug: service-database-choice
topic_label: Choosing Postgres vs DynamoDB for a new service
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Retrospective: Sprint ending 2026-05-16 - Notification Service

## Date

2026-05-16

## Participants

Ana Rivera, Marcus, Priya, Jordan, Sam

## What Went Well

- **Time-boxed spike produced usable evidence.** The DynamoDB spike (`experiments/notify-ddb/`) was completed within its allocated window and gave the architecture meeting concrete findings (access-pattern fit confirmed; operational cost documented) rather than an inconclusive result.

- **The operational capacity framing gave the meeting a shared anchor.** Framing the decision around what a 4-person on-call rotation can realistically absorb turned "which DB is technically better" into a bounded, team-specific question. The Wednesday session reached a recommendation in one meeting.

- **Marcus and Ana aligned before the lock, not at it.** Rather than leaving the DynamoDB vs. Postgres tension for Priya to resolve, Marcus and Ana worked to a single recommendation overnight. The 11am sync closed cleanly on the first pass.

- **ADR-0023 came out of the architecture meeting as a draft, not as a follow-up task.** Having the ADR structure in the room meant the Wednesday session ended with a document rather than a verbal outcome that had to be transcribed later.

## What Did Not Go Well

- **Verbal sign-offs did not convert to written confirmations quickly enough.** Marcus's written agreement on the 5M events/day revisit threshold was still pending EOD Thursday, a full day after Wednesday's meeting. A verbal agreement is not a closed action item.

- **Evaluation criteria were defined informally and after the spike was already under way.** We ran the DynamoDB spike, then articulated the decision criteria (access-pattern fit, operational cost, reversibility) in the architecture meeting itself. Defining criteria before the spike would have shortened the meeting and reduced the risk of criteria shifting mid-evaluation.

- **The Slack-partnership deal is a forcing function the team cannot see.** If the deal closes earlier than the 12-month projection, we hit the Postgres revisit window ahead of schedule. Nobody on the team tracks deal timing, which meant this risk sat unowned until the retro surfaced it.

## What Will We Change

- [ ] For the next multi-option datastore evaluation: write a one-page decision matrix (criteria, weights, candidates) and share it before the spike begins - Owner: Ana - By: next architecture review kickoff
- [ ] Close verbal sign-offs from architecture meetings in writing on the same day, not the following day - Owner: decision driver (Ana for any ADR-0023 follow-ups) - By: immediate, starting now
- [ ] Priya sends a monthly one-liner to #notify-arch on Slack-partnership deal status so the team can adjust the 5M events/day revisit horizon if the timeline shifts - Owner: Priya - By: 2026-06-01

## Notes

- ADR-0023 is accepted as of the 2026-05-16 11am sync. The 5M events/day sustained threshold is the team's primary leading indicator for revisiting the Postgres path.
- Sprint planning ran at 2pm the same day and locked the first two weeks of build work. Retrospective action items carry into the next sprint's tracking board.
- The three action items above are the full commitment list; no additional items were added. Jordan and Sam carry no retro action items - their upcoming deliverables (dashboard metrics by 2026-05-22, schema spec by 2026-05-20) are tracked in sprint planning, not here.
