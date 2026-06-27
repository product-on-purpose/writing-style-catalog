---
entry_id: how-to-guide
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# How to Communicate a Q3 Roadmap Cut to Stakeholders

## Before you begin

- The cut decision is made and has internal sign-off. Do not begin external communication while leadership alignment is still in progress.
- You have confirmed the specific reason for the cut. In the Insights case: the billing-system migration overran its timeline and consumed the engineering capacity originally allocated to the dashboard.
- You have a concrete stopgap offer ready. A promise to figure something out later is not a stopgap. For Insights, this means the CSV export is scoped and scheduled before outreach begins.
- You know which stakeholders received the original Q3 commitment. For Insights: the Sales team (who positioned the dashboard as a closing point for enterprise accounts) and the four key customer accounts who were given a delivery date directly.
- You have a replacement target date to offer. A deferral without a new date is a cancellation in the customer's mind. Confirm the Q1 2027 target with engineering before any external message goes out.

## Overview

This guide walks through the communication sequence for cutting Insights from the Q3 roadmap and notifying the stakeholders who were given the original delivery date. When you finish, you will have aligned your internal teams, delivered direct notice to each affected customer account, and set the expectations that carry through Q4 and into the Q1 re-commitment.

## Step 1: Lock the facts before drafting any message

You cannot communicate what you have not yet confirmed. Before writing a single sentence of external notice, verify three things: the reason (billing migration consumed the capacity), the stopgap (CSV export, releasing September 26), and the replacement commitment (full dashboard, Q1 2027, target March 13, 2027).

Successful outcome: you can answer "why did this happen," "what do customers get now," and "when does the real thing ship" without hedging or checking a document mid-call.

## Step 2: Brief sales before the customers hear anything

Sales positioned Insights as a closing point for enterprise accounts. They will field questions from customers before you finish sending notices. Give Jordan Park and the sales team a direct heads-up - a short call or a written message with the three confirmed facts - before any written notice goes out to accounts.

This step matters because a sales rep who is blindsided by a customer question is in a worse position than one who already knows the story. The goal is not just to inform; it is to give Jordan Park what is needed to speak to the cut confidently.

Successful outcome: Jordan Park confirms they have the facts and understand the plan before the customer notices go out.

## Step 3: Send written notice to the four key accounts

Draft a short, direct notice. The structure that works: name what changed, explain why without over-explaining, name the stopgap and how to access it, and give the Q1 target date. Do not apologize repeatedly or bury the news under framing paragraphs.

Send the notice to each account individually. A broadcast message signals that this is routine; these accounts were given a personal commitment, and the correction should match that register.

Successful outcome: each of the four accounts has received a written notice with the reason, the CSV export details, and the Q1 target date before you move to the next step.

## Step 4: Schedule calls for accounts that flagged dependency

Some accounts may have signaled a strong dependency on the Q3 date. A written notice is not enough for those accounts. Flag any such account to Jordan Park and get a call on the calendar this week. On the call, do not over-promise on Q1 scope. Confirm what the Q1 build includes (full dashboard with saved views and scheduled reports) and what the CSV export can do in the meantime.

Successful outcome: any account that flagged strong dependency has a call scheduled before the week ends.

## Step 5: Update the internal status report

After external notices are sent, update the Insights status report to reflect the new state: Red, Q3 cut, CSV export on track for September 26, Q1 kickoff October 6. Flag the March 13, 2027 target and ask leadership to confirm whether that date is cleared for use in customer-facing communications.

Successful outcome: leadership has confirmed the March 13 date, and the status report matches the message the four accounts received.

## Troubleshooting

**An account pushes back and asks whether the original Q3 date can be honored**

Do not relitigate the decision or offer a partial release to preserve the relationship. The billing migration is not optional, and the two missing pieces - saved-view persistence and scheduled-report delivery - are exactly what the account was sold. Acknowledge the impact directly, confirm the CSV export as the interim path, and hold the Q1 date. If the account signals a contract or renewal risk, escalate to leadership rather than making commitments outside your authority.

**Sales asks whether scope can be reduced to hit Q3**

The answer is no, and you should be specific: the billing migration required the capacity, and there is no remaining Q3 window for Insights work without risking the migration. Redirect the conversation to what Q1 includes and what the CSV export delivers now. Relitigating the capacity math does not help Sales or the customer.

**The CSV export misses its September 26 target**

The quarter closes September 30. A slip to the week of September 30 is within the buffer - it is recoverable. The risk is the billing production release on September 19. If that release surfaces regressions, engineering will triage those before returning to the CSV build. Watch the September 19 release closely and flag a potential export delay to Jordan Park as soon as the risk is concrete, not after the slip has already landed.

## Next steps

- After the billing migration stabilizes, begin the Q1 engineering design document for Insights. Owner: Maya Chen, start date October 6.
- Carry the four account names and their specific commitments into Q1 planning. The Q1 scope - full dashboard, saved views, scheduled reports - was set to match what was sold. Do not allow Q4 scope requests to expand Q1 without revisiting the schedule.
- When Q1 planning closes and capacity is confirmed, send each of the four accounts a follow-up note confirming the March 13 target is locked. That closes the loop the Q3 cut opened.
