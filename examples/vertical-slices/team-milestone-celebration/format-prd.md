---
entry_id: prd
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Checkout Platform v2 - Product Requirements

*This document was written at the start of the project and revised at each major phase gate. It is being distributed now, at launch, as the official record of what this team set out to build and why. Fourteen months later, every goal on this list has been met.*

## Problem Statement

Customers trying to complete a purchase on Meridian Commerce fail to reach the confirmation screen at an unacceptable rate. The abandonment rate in the final payment step has averaged above 30 percent for two years - a number that remained stubbornly high despite repeated incremental fixes to the existing flow.

The existing checkout system was built in 2018 on a framework the rest of the engineering org has since moved away from. Over five years of patch work, it accumulated state management that no engineer could fully trace, third-party integrations that could not be upgraded without risk of breaking payment, and a session model that failed silently under load. The result is a system that works most of the time but fails in ways that are difficult to observe, difficult to reproduce, and impossible to fix without touching things that should not be touched.

The failure is not random. Abandonment spikes on high-traffic days, when mobile users attempt to switch payment methods mid-flow, and when customers return to a session after leaving for more than 20 minutes. These are precisely the moments when completing a purchase matters most. The system fails the customer when the customer needs it to hold.

## Goals

- Reduce final-step cart abandonment to below 15 percent, measured over a rolling 30-day window, within 60 days of full rollout
- Achieve a mobile checkout completion rate within 3 percentage points of desktop, closing a gap that has persisted since mobile traffic exceeded desktop
- Reduce the median time from payment entry to confirmation to under 4 seconds on a standard connection
- Enable the platform team to ship checkout improvements on a weekly cycle, without a full regression pass before each release, by establishing clear integration contracts between checkout and downstream services

## Non-Goals

The following are explicitly out of scope for this release. Each deserves its own initiative and its own requirements document.

- Guest checkout and account consolidation: The current distinction between guest and registered checkout is out of scope. Changing the account model while rebuilding the payment flow would double the risk surface. This project delivers a rebuilt flow for existing account types only.
- New payment methods: Adding buy-now-pay-later, additional digital wallets, or alternative payment rails is not in scope. The goal is to fix the foundation, not to expand it while it is being replaced.
- Internationalization: Currency handling, tax calculation, and localization for non-US markets are out of scope. The rebuilt platform should make internationalization achievable; it does not need to deliver it.
- Checkout analytics redesign: The current analytics instrumentation is inadequate, but redesigning the measurement layer is a separate initiative. This project will preserve existing events and add session-level logging sufficient for the success metrics above. It will not deliver a new analytics product.
- Cutting over before the new system has proven itself: The old checkout remains in production and handles 100 percent of traffic until the new one has been validated under real conditions. Migrating prematurely to hit a date is explicitly not a goal.

## User Stories / Jobs-to-be-Done

- As a customer completing a purchase, I want the checkout flow to hold my payment details and cart state reliably across a brief interruption, so that I can return and complete my purchase without starting over
- As a customer on a mobile device, I want to switch between payment methods without losing my place, so that I can use the method that is right for this purchase without abandoning the cart
- As an ops associate investigating a failed order, I want a clear, queryable record of what happened during a checkout session, so that I can confirm what the customer experienced and make the right call on escalation
- As an engineer shipping a checkout improvement, I want a defined contract between the checkout surface and the services behind it, so that I can scope a change with confidence about what I am responsible for and what I am not

## Success Metrics

Progress on these metrics will be evaluated at 30 days and 60 days post-full-rollout. The 60-day read is the definitive one; the 30-day read is a leading indicator.

- Final-step abandonment rate below 15 percent (primary metric)
- Mobile-to-desktop completion gap below 3 percentage points
- Median payment-to-confirmation time under 4 seconds at the 50th percentile; under 10 seconds at the 95th percentile under peak load
- Zero silent failure modes: any checkout session that fails must produce a logged, queryable event within 5 seconds of failure
- Engineering cycle time: a contained change touching a single integration point should be deployable without a full regression pass

## Open Questions

*These questions were unresolved when this document was first written. Answers discovered during the project are noted.*

**1. Can the old and new checkout systems run in parallel without creating inconsistent order state?**
The plan calls for long-lived parallel operation, but the data model had not been audited for conflicts at the time this was written. *Resolved: The data model required a migration that was not in the original scope. The team identified this in month two and negotiated the additional work before it became a crisis.*

**2. What does peak load look like for the new system?**
The existing system has never been load-tested at scale because any test risked destabilizing production. The new system needs to be validated before traffic is migrated, but the ceiling is unknown. *Resolved: Load testing was built into the rollout plan. The system held through the two highest-traffic days of the year - the first during the incremental rollout and the second at full traffic - without a performance incident.*

**3. Will new integration contracts break existing downstream consumers?**
Several services consume checkout events in ways that are undocumented. A silent contract change could break order processing without visible checkout errors. *Resolved: The team ran a four-week audit of downstream consumers before cutting the first integration contract. Two consumers required coordinated changes. Both were completed before the first traffic migration.*

**4. What is the rollback plan if the new system degrades during rollout?**
Traffic migration will be incremental, but the rollback path was not designed at the time of this writing. *Resolved: Rollback capability was built before the first traffic migration. It was exercised twice in staging and once during a production near-miss in month eleven. Both times it worked. The month-eleven incident is the reason the first launch date slipped.*

**5. Who owns the decision to cut over fully, and what evidence is required?**
There is no named decision-owner or defined evidence threshold for the final traffic migration. *Resolved: Rania Osei, the platform lead, was named as the decision owner in month four. The threshold was defined as 30 days at 80 percent traffic with abandonment tracking below target. The cutover decision was hers. She made it on the third attempt, with the data in hand.*

---

*Checkout Platform v2 shipped to 100 percent of traffic on March 14, 2025.*

*Fourteen months of parallel operation. Two near-misses that tested the rollback path and confirmed it worked. Two launch dates that slipped because the evidence was not there yet, and a lead who called that correctly both times. A peak-load window the system held cleanly on its first real test at full traffic.*

*The five open questions above were answered the hard way. That is what the work cost, and what it took.*
