---
entry_id: how-to-guide
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to Mark the End of a Long-Running Project Launch

## Before you begin

- The project has shipped and you have at least a few days of post-launch data showing the system held. For Project Halyard, that threshold was the weekend of June 14-15, when the rebuilt checkout held through peak load without incident. Marking a milestone before you know whether the launch is stable risks recognizing something that may still need to be rolled back.
- You have a list of the specific decisions that determined whether the launch succeeded - not job titles, but names and what each person actually did. Halyard's close-out required knowing that Dani Rowe called the March hold when the February near-miss was not fully resolved, that Marcus Teel filed the February bug on his own initiative rather than marking it low severity, and that Jordan Osei rewrote the payment callback handler rather than patching around it.
- You have access to the incident records, slip notices, and decision logs from the full project run. For a fourteen-month project, this material will not be reconstructed from memory.

## Overview

This guide covers how to close out and mark a long-running project launch in a way that recognizes the real work - not just the shipping date, but the decisions made under pressure and the work that does not appear in velocity charts. When you finish, you will have a close-out record that the team, their managers, and anyone who joins the project later can use to understand what actually happened and why the launch held.

## Step 1: Pull the full timeline before memory compresses it

Long projects collapse in retrospect. Within a week of shipping, "we had two near-misses" will replace the actual memory of February and April. Within a month, even that detail will blur.

Gather the incident tickets, slip notices, decision logs, and post-mortems before the team disperses. For Halyard, that means the February cart-state mismatch report, the April race condition findings, and each launch-date change notice that went to stakeholders across the fourteen-month run.

A successful outcome at this step: you have a dated sequence of events with enough detail that someone who was not on the project can follow it. The Halyard ADR and final status report are examples of what this looks like in practice - they name events, dates, and the people behind them, not just the outcome.

## Step 2: Name the specific decisions and the people behind them

Generic recognition does not transfer. Recognition that names what a specific person did and why it mattered does transfer - and it transfers to the people who manage them.

Go through your timeline and identify the decisions that determined whether the launch succeeded. For Halyard, those decisions include: Dani Rowe calling the March hold when the schedule pressure was real; Marcus Teel filing the February bug when he could have moved on; Jordan Osei rewriting the callback handler when a smaller patch was available and tempting; Sam Wickfield holding the regression bar on June 9 when every hour of delay felt enormous.

Write each decision in one to two sentences: who made it, what the visible pressure was at the time, and what would have happened if they had chosen the easier path. If you cannot write it that specifically, return to your timeline records. The specificity is what makes this recognition accurate rather than ceremonial.

## Step 3: Choose a format that matches the scope

A project that ran fourteen months and caught two near-misses before production is not a sprint retrospective. A standard retro format will not do it justice - that is why the Halyard status report explicitly flagged a separate format for the June 30 session.

Consider the following:

- If the architectural decision and its tradeoffs are the primary story, update or record an ADR. Halyard's ADR-0017 documents the parallel-run approach, the expected costs, and the actual consequences at close-out.
- If the team needs to process what happened together over the full arc, run a retrospective with extended scope - structured around project phases rather than sprints. Block at least two hours for a fourteen-month run.
- If the primary audience is managers and stakeholders who were not running the work day to day, write a close-out record that names what the team did in terms visible to people outside the delivery work. The Halyard status report's "Asks" section is an example.

Pick one as the primary artifact. You may produce more than one, but there should be a single document that is the authoritative record of the project's arc. Decide before the retrospective runs, so the session output has a clear destination.

## Step 4: Run the close-out session before the window closes

Schedule the retrospective while the team is still intact and the launch is recent. Halyard targeted June 30 - seventeen days after the June 13 cutover. That window is approximately right for a project of this length: enough time for the dust to settle and the first peak weekend to pass, not so much time that people have mentally moved on.

Share the timeline from Step 1 with participants before the session so the time in the room focuses on meaning and synthesis rather than reconstruction. Open with what was supposed to happen, then move to what actually happened and what each divergence cost or prevented.

At the close of the session, confirm in the room who is writing the summary and when it will be circulated. An unrecorded retrospective is the same as no retrospective for anyone who joins the team later.

## Step 5: Archive the record where it will be found

The close-out documents belong in the project's permanent archive, not in a channel that will scroll off or a status report that was current in June. For Halyard, the project archive holds the full timeline, the two near-miss post-mortems, and documentation of both slip decisions - linked from the checkout-reflow README so any new team member can find the record from the project's entry point.

Tag or link the retrospective from the project's main documentation index. If someone needs to understand why the checkout flow is structured the way it is eighteen months from now, they should be able to reach the ADR and the close-out record from the README in one step.

## Troubleshooting

**The timeline is already compressing and you cannot reconstruct the sequence.**
Pull the git log, incident tickets, and stakeholder communications. The sequence lives in those records even when memory has already smoothed it. For Halyard, the phase-by-phase rollout chart in the README shows the structure at a glance; the detailed record of each phase is in the near-miss post-mortems.

**The team does not see why a retrospective is necessary - the project shipped.**
The retrospective is not a post-mortem. It is a record of what the team learned about running a parallel-track migration, catching near-misses before production, and holding a schedule under external pressure. That learning does not transfer to the next project unless it is written down. Shipping is a reason to run the retrospective, not a reason to skip it.

**Recognition is landing as generic praise and the team is not responding to it.**
Return to Step 2. Generic praise is not recognition. Recognition names what a specific person did and why the outcome was different because of it. If the response is flat, the recognition is probably still at the "great work" level rather than at the level of the actual decisions.

## Next steps

- Review the outcome measurement once the data is available. For Halyard, Mia Chen's analytics team targeted July 7 for the first post-launch cart-abandonment baseline. That number is the measurement that confirms whether the decision recorded in ADR-0017 was correct. Read it in the context of the parallel-period attribution noise the status report flagged.
- Complete the decommission on schedule. Halyard's legacy checkout was scheduled for July 14, following the 30-day archive window. The close-out is not finished until the old system is gone and the archive window closes cleanly.
- Carry the practices forward explicitly. The parallel-run approach, the near-miss process, and the discipline of holding launch dates on engineering judgment rather than deadline pressure are reusable. Document them as named practices the team can point to on the next project, not just as things that happened on this one.
