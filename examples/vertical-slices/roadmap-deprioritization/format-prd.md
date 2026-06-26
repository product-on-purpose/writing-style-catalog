---
entry_id: prd
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Insights Analytics Dashboard - Q3 Delivery Revision and Bridge Plan

**Status:** Revised plan  
**Date:** September 2025  
**Author:** Product Management  
**Audience:** Sales leadership and key customer stakeholders

---

## Problem Statement

Sales reps and account managers field analytics requests from customers multiple times per week. Customers want to know how their teams are using the product: who logs in, which features they engage with, and where sessions stall. Currently, customers must contact support to get usage summaries or wait for quarterly business reviews. This manual reporting loop creates a three-to-five-day turnaround and places a recurring dependency on the customer success team for data that customers should be able to pull themselves.

The Insights analytics dashboard was scoped and committed for Q3 to solve this problem directly. It was designed as a purpose-built in-product view giving customers self-serve access to their usage data, filterable by date range, user cohort, and feature area.

In July, a mandatory billing-system migration was escalated to the highest internal priority. The migration required input validation, audit-trail logging, and downstream reconciliation work that had not been visible during the original capacity plan. By August it was clear the migration would consume the remaining engineering bandwidth allocated to Insights for the quarter. Shipping Insights on the original Q3 date would mean shipping without date filtering, without cohort segmentation, and without the data export layer. That is not a useful analytics product; it is a half-built screen that generates confusion and support tickets rather than value.

This document defines the revised delivery plan: what ships by end of Q3, what ships in Q1, and how we will measure whether the interim solution keeps customers unblocked.

---

## Goals

**Q3 (ship by September 30)**

- Customers can download a structured CSV export of their full usage dataset directly from within the product, without contacting support or waiting for a quarterly business review.
- The export covers the core data fields from the Insights Phase 1 scope: login events, feature-level engagement, and session counts, broken down by user and date.
- The export surface is accessible from the account settings area, requires no support ticket or admin intervention, and works for any account currently on the Insights waitlist.
- At least 75% of waitlisted key customer accounts confirm in a follow-up conversation that the export meets their minimum reporting needs as a bridge.

**Q1 (ship by March 31 next year)**

- The full Insights dashboard ships with all Phase 1 scope intact: date-range filtering, cohort segmentation, feature-level engagement views, and in-product chart rendering.
- No Phase 1 features are removed or reduced relative to the original Q3 commitment; the timeline moves, the scope does not.
- Sales has a demo environment available no later than February 1 to support Q1 pipeline and renewal conversations.

---

## Non-Goals

- **No partial Insights UI in Q3.** Shipping a partially functional dashboard creates customer-facing confusion and inflates support volume. If any screen is not production-ready, it does not ship. The Q3 deliverable is the CSV export only.
- **No custom export formats.** The CSV export is a single structured file with a fixed column layout. Customizable column selection, multi-sheet formats, and format variant options are out of scope for the bridge release.
- **No scheduled or recurring exports.** Customers trigger the export manually. Automated delivery, email scheduling, and API-based export access are Phase 2 features and are not pulled forward to fill the gap.
- **No visualization layer in Q3.** Customers analyze the export in their own spreadsheet or BI tool. We are not building or bundling charting capability as part of the bridge release.
- **No scope reduction on Insights Phase 1 for Q1.** The Q1 target is the complete Phase 1 feature set as originally defined. Nothing is removed to make the rescheduled commitment easier to hit.

---

## User Stories / Jobs-to-be-Done

**Sales rep (internal stakeholder)**

- As a sales rep managing a renewal conversation, I want to show a customer their engagement trend over the past quarter so that I can anchor the discussion in actual usage data rather than anecdote.
- As a sales engineer preparing a business review, I want to pull a customer's usage export without filing an internal data request so that I can build the report without waiting several days on the data team.

**Customer account admin (key customer stakeholder)**

- As a customer account admin, I want to download my organization's usage data as a file I can open in a spreadsheet or load into our internal tools so that I can build the monthly report my manager requests without depending on the vendor to generate it for me.
- As a customer data analyst, I want structured export data I can join to our own operational records so that I can see where product engagement correlates with our own team's outcomes.
- As a customer success lead, I want to see which product areas my team uses most so that I can identify gaps in adoption before our next internal training cycle.

---

## Success Metrics

**Q3 (CSV Export Bridge)**

- Adoption: 70% of waitlisted key customer accounts download at least one export within 30 days of the feature going live.
- Support deflection: No support tickets requesting a manual usage pull from any account that has access to the export, measured over the final four weeks of Q3.
- Sales enablement: Sales team rates the CSV export as adequate as an interim substitute in an internal survey conducted in early October (target: 75% or higher).

**Q1 (Full Insights Release)**

- Activation: 60% of eligible accounts open the Insights dashboard at least once within 30 days of launch.
- Engagement depth: Median session includes at least two distinct filter interactions (date range, cohort, or feature area), indicating customers are exploring the data rather than opening and immediately leaving.
- Support baseline: No increase in usage-reporting support tickets relative to the Q3 CSV-export period, measured in the first four weeks after launch.

---

## Open Questions

1. **Which key customer accounts are on the waitlist, and has every account been contacted directly?** This document assumes sales leads have a confirmed list. If any waitlisted account has not been personally notified before this plan is shared more broadly, that account should receive a direct conversation first, not a document.

2. **What is the data freshness of the CSV export?** The current assumption is a daily batch refresh. If customers expect near-real-time data, the batch cadence will create mismatched expectations. The product UI must surface the data lag explicitly, and that lag must be confirmed by engineering before the feature is announced.

3. **Does the export include historical data predating the feature launch?** The assumption is a 12-month lookback. If engineering can only provide data from the export go-live date forward, customers trying to build historical trend reports will face a gap that makes the export significantly less useful. This must be confirmed and communicated before any customer announcement goes out.

4. **Is the Q1 delivery date firm, given the billing migration tail work?** The assumption is that migration work completes by mid-October and does not extend into Q4. If remaining migration tasks slip, Q1 Insights capacity could be affected again. Engineering should flag this risk no later than the October planning checkpoint so Sales has time to set expectations accordingly.

5. **What threshold defines "half-built" in a future scenario?** The decision not to ship a partial dashboard in Q3 was made on the basis that the missing features were the specific ones customers were promised. But the threshold was not written down. The Q4 planning review should define criteria for when a partial release is acceptable versus when a deferral is required, so the next decision is not made under time pressure from scratch.
