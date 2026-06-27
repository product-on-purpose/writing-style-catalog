---
entry_id: runbook
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Roadmap Deprioritization Notification Runbook

## Overview

Use this runbook when a committed feature is being deferred and affected stakeholders - including external customers - must be notified with a consistent, sequenced set of communications before the original ship date passes.

## Prerequisites

- [ ] The deferral decision is final and has leadership sign-off
- [ ] A stopgap or alternative is scoped, dated, and confirmed by engineering
- [ ] The Q1 target date is cleared for external communication by leadership
- [ ] You have the full list of affected external accounts and the internal owner (customer success or sales) for each account
- [ ] The product lead and engineering lead have aligned on the technical facts in writing

## Procedure

1. **Write the internal decision record**
   Document the deferral, the reason (billing-system migration displaced Insights capacity), the stopgap (CSV export, target September 26), and the new commitment (Q1 2027, target March 13). Circulate to Maya Chen (product), Dario Reyes (engineering), and Jordan Park (customer success) for comment before proceeding.
   Expected output: Decision record is shared and no objections to the stated facts are raised within 24 hours.

2. **Confirm leadership sign-off on the external-facing date**
   Obtain written confirmation that the March 13, 2027 target is acceptable to include in customer-facing communications. Do not send external notices until this is in hand.
   Expected output: Written acknowledgment from leadership (Slack, email, or document comment) explicitly approving March 13, 2027 for external use.

3. **Brief the Sales team before any external notices go out**
   Share the decision record summary with Sales. Include the CSV export date (September 26), the Q1 target (March 13, 2027), and a note that no external communication goes out until after this briefing.
   Expected output: Sales acknowledges receipt and identifies any of the four accounts that need a direct call before written notice lands.

4. **Confirm the call list with Jordan Park**
   Collect from Sales the names of accounts flagged for a direct call. Coordinate with Jordan Park to schedule those calls before written notices go out to the flagged accounts.
   Expected output: Call schedule confirmed for high-dependency accounts. Each call has an owner and a scheduled time.

5. **Send written notice to all four affected accounts**
   Issue the written notification to each account covering: what changed (Insights dashboard deferred from Q3 2026), why (mandatory billing-system migration consumed the allocated engineering capacity), what is available now (CSV export of the underlying event data, September 26), and what is coming (full dashboard, Q1 2027, March 13 target). Send to all four accounts regardless of whether a direct call is scheduled.
   Expected output: Sent confirmation logged for each of the four accounts in your email client or CRM.

6. **Complete direct calls for flagged accounts**
   Conduct each call scheduled in step 4. Follow the written notice structure: what changed, why, stopgap, Q1 commitment. Do not offer scope additions or timeline concessions beyond what the written notice states.
   Expected output: Call completed and a brief summary logged in CRM for each account.

7. **Update the internal roadmap and project tracking**
   Mark Insights as deferred in the roadmap tool. Set the Q1 milestone to March 13, 2027. Add the CSV export as a Q3 delivery item with September 26 target and Dario Reyes as owner. Set customer outreach owner to Jordan Park.
   Expected output: Roadmap reflects Insights at Q1 2027 and CSV export at Q3 2026 with correct owners and dates.

## Verification

Confirm all four of the following before closing this runbook:

- All four affected accounts have received written notice.
- Sales holds a copy of the written notice and the September 26 CSV export date.
- Leadership has provided written sign-off on the March 13, 2027 date for external communications.
- The internal roadmap reflects Insights deferred to Q1 2027 and the CSV export as a Q3 2026 delivery item.

## Rollback

If the deferral decision reverses before any written notices are sent, halt at the current step and do not proceed. If written notice has already gone out to any account, send a correction to those same accounts immediately; the correction notice takes precedence over the original. Revert the roadmap to show Insights as an active Q3 commitment. Rollback is not reversible in the sense that sent communications cannot be unsent - a correction notice is the closest available recovery path, and it must be sent promptly.

## Escalation

If an affected account signals intent to escalate, pause outreach to that account and notify Maya Chen (product) and the account's Sales owner before taking any further action. Do not send additional written communications to that account until escalation handling is defined. For questions about the CSV export data format or the Q1 scope, direct contacts to insights@meridian.io.
