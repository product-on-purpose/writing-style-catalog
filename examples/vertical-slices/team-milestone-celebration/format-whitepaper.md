---
entry_id: whitepaper
axis: format
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Running the Old Rail While Building the New One
## Lessons from Fourteen Months of Parallel-Run Checkout Replacement at Meridian Commerce

**Authors:** Technology Division, Meridian Commerce
**Published:** June 2024

---

## Executive Summary

Between March 2023 and May 2024, the Meridian Commerce technology team executed a complete rebuild of the company's checkout flow while keeping the existing system in uninterrupted production operation. The rebuild was initiated to resolve a chronic cart-abandonment problem that had resisted two years of incremental repair. It concluded, fourteen months later, with a successful cutover sustained under peak seasonal load.

The program slipped its launch date twice. It produced two events that qualified as near-misses - situations in which a defect or a configuration failure reached the edge of customer impact before being caught and resolved. Both were caught. Both produced improvements to the program's design that carried through to the final launch.

This document sets out the central position the team developed over those fourteen months: rebuilding mission-critical transactional infrastructure without downtime is not primarily a technical problem. The technical patterns for parallel-run replacement are known and tractable. The organizational challenges - maintaining two systems simultaneously for over a year, absorbing schedule slips without cutting scope, sustaining the judgment required to catch near-misses at the end of a long program when fatigue is highest - are the actual determinants of whether this class of project succeeds.

The implications for organizations planning comparable work are practical and specific. They are detailed in the Implications and Recommendations section of this document and summarized here:

- The parallel-run architecture is the right approach for zero-downtime replacement of critical transactional infrastructure. Teams should commit to it with accurate expectations about its sustained operational cost.
- Launch slips in programs of this type should be understood as the quality standard working correctly, not as evidence of planning failure. Organizations should build governance structures that absorb slips rather than convert them into scope-cutting pressure.
- The final phase of a parallel-run replacement carries the highest risk and the most fatigued team. It requires dedicated staffing and active management, not the default assumption that the program is nearly done.

---

## Introduction

Checkout is where everything a commerce company does resolves to a transaction. The marketing effort, the product catalog, the logistics investment - all of it culminates in the moment a customer decides to complete a purchase. A checkout platform that performs poorly is not an engineering problem with a narrow blast radius. It is a business problem with a direct line to revenue, and it is a customer experience problem with direct consequences for whether customers return.

Meridian Commerce knew for two years before this program began that its checkout platform was underperforming. Cart abandonment rates remained elevated well above the company's historical baseline, with session instrumentation data showing the drop-off concentrated at the payment step. Repeated interventions - interface changes, payment partner integrations, targeted performance optimizations - moved the numbers modestly without resolving the underlying pattern.

By early 2023, the product and engineering leadership arrived at a conclusion that had been building for some time: the platform's architecture made it structurally resistant to the kind of improvement required. The abandonment problem was not a feature problem or a performance-tuning problem. It was a system design problem. The only path to resolving it was to rebuild.

In March 2023, the program began.

---

## Background: The Diagnosis That Justified a Rebuild

Before the program was authorized, the engineering team conducted a structured diagnosis of the existing checkout platform. The goal was to determine whether the abandonment problem could be resolved through incremental improvement or whether it required a complete architectural replacement.

The diagnosis identified three structural problems that collectively justified the rebuild decision.

The first was the payment orchestration layer. The existing system handled payment retries and fallback routing in a way that produced inconsistent state under specific failure conditions. These conditions were infrequent enough that they had not caused visible incidents at historical traffic volumes. But the pattern meant the system's failure modes would become less predictable as load increased - and as the business grew, load was increasing.

The second was session management. The platform's checkout sessions were coupled to server-side resources in a way that made horizontal scaling unreliable. Under peak load, this coupling produced the performance degradation that was visible to customers: slow page transitions at the payment step, timeout errors that returned customers to earlier points in the flow, and inconsistent state recovery when sessions were interrupted.

The third was the data model. Loyalty points, gift card balances, and deferred payment options had been integrated over three separate engineering cycles, each using a different approach to order finalization. The resulting ambiguity was manageable in a system where experienced engineers understood the history. It was not maintainable at scale, and it was not transferable to engineers who had not lived through the original integration decisions.

Incremental repair was considered and ruled out. The three structural problems were interconnected. Addressing the payment orchestration layer without also addressing session management would not resolve the load-dependent failures. Addressing both without addressing the data model would leave the order finalization ambiguity in place. The problems had to be addressed together, or the investment in addressing any one of them would be captured only partially.

The decision to rebuild was made in March 2023. The program was scoped for eleven months, with a target launch in February 2024.

---

## The Architecture Decision: Two Systems Running in Parallel

The most consequential decision of the program was made before the first line of new code was written: the new checkout platform would be built alongside the existing one, in a parallel-run configuration, rather than replacing it in a hard cutover.

This decision required the company to operate two fully functional checkout systems simultaneously for the duration of the program. Production traffic would remain on the existing system until the new system had been validated against a defined criteria set. At that point, traffic would be migrated in controlled increments - a defined percentage at a time, with fallback mechanisms available at each threshold - until the new system was carrying the full load and the old one could be decommissioned.

The alternative - a hard cutover on a fixed date, with the old system replaced overnight - was discussed and rejected. A hard cutover would have required a maintenance window measured in hours. For a commerce platform, a maintenance window of that length had a direct and calculable revenue cost. It also meant that any defect discovered after the cutover was a production incident affecting real customers with no fast rollback available. The parallel-run model eliminated that risk by design: the old system remained live throughout the migration, and reverting to it at any threshold required only a traffic routing change.

The decision was right. It was also the source of nearly all of the program's difficulty.

Running two systems in parallel creates a sustained operational burden that compounds over time. Every change to the existing system - to fix a bug, to accommodate a payment partner change, to address a performance regression - must be evaluated for whether a corresponding change is required in the new system. Every production incident in the existing system draws engineering attention away from the new one. The team maintaining both systems operates under a split cognitive load that does not diminish as the program progresses.

By month six - September 2023 - the team had absorbed a dual-system maintenance burden that had not been fully represented in the original program estimate. The estimate had accounted for the parallel build. It had not fully accounted for the ongoing cost of keeping the existing system stable for eleven months while a replacement was developed. That cost was real, and it was carried by the people on the team rather than appearing as a tracked line item in a project plan.

---

## What Happened Across Fourteen Months

### The Build Phase: March to October 2023

The first eight months of the program proceeded according to plan in its technical dimensions. The team rebuilt the payment orchestration layer using an explicit state-machine model that made retry and fallback behavior deterministic and testable. Session management was redesigned from the ground up to decouple checkout state from server-side resources. The data model was replaced with a unified order finalization schema that handled loyalty, gift cards, and deferred payment with consistent semantics.

By October 2023, the new system was running in shadow mode - receiving copies of production requests, processing them against the new architecture, and returning results that were compared against what the existing system produced. Discrepancies were logged, investigated, and resolved. The shadow comparison data was the primary evidence of readiness, and it was the mechanism through which the first near-miss was caught.

### The First Near-Miss: October 2023

Three days before a limited production rollout was scheduled to begin, a senior engineer reviewing shadow comparison logs identified an anomaly in orders that combined loyalty redemption with gift card balances. Under a specific sequence of conditions - a split order involving both instruments, followed by a payment processor timeout at finalization - the new system was resolving the order to a finalized state with incorrect attribution between the loyalty ledger and the gift card balance.

The error did not affect the customer-visible total. It affected backend reconciliation. Left in production, it would have produced accounting discrepancies that were difficult to trace and impossible to correct without retroactive adjustment.

The engineer flagged the issue at 11 PM on a Thursday. By Saturday morning, two additional engineers had identified the root cause in the finalization logic and deployed a corrected version to the shadow environment. The rollout was delayed by four weeks while additional test cases were written to cover the class of conditions that had exposed the defect.

The original December 2023 launch target was moved to February 2024.

### The Second Near-Miss and the Second Slip: February 2024

The February 2024 rollout began on schedule. Traffic was shifted to the new system in ten-percent increments. The first three increments completed without incident. At the 40% threshold, the team encountered a problem that had not appeared in shadow testing.

At reduced load, the existing system's caching behavior changed in ways that had not been anticipated. The caches had been tuned for full production traffic. At the load level corresponding to 60% of normal volume on the existing system - the result of 40% having moved to the new system - certain cache expiry patterns began producing stale state in the existing system's fallback path.

This mattered because the new system's circuit breakers were configured conservatively during the rollout window: they tripped on anomalies that would not have triggered a trip under normal operation. Each trip redirected traffic to the existing system's fallback path, which was now producing stale state due to the caching issue, which created the conditions for another circuit breaker trip. The cascade was self-reinforcing.

An infrastructure engineer caught the pattern at 2 AM on a Saturday during what was not an assigned monitoring shift. Her written analysis, produced over three hours and shared with the team at 6 AM, identified the caching parameter, traced the feedback loop precisely, and outlined two resolution approaches with their respective tradeoffs.

The team paused the rollout, corrected the caching configuration in the existing system, validated the correction across a range of simulated traffic levels, and planned a restart. The February 2024 target was not met. The launch was rescheduled for May 2024.

### The Final Cutover: May 2024

The May 2024 rollout incorporated everything the team had learned from the February attempt. The migration schedule was more gradual. The existing system's caching behavior had been validated under a range of traffic levels before the migration began. The fallback path between the two systems had been tested explicitly under the conditions that had caused the February cascade.

The cutover was scheduled during a period of elevated traffic. This was deliberate. The team had concluded that validating the new system under low-traffic conditions gave high confidence in scenarios the system would rarely face, while validating under load gave confidence in the scenarios the system would face regularly. The progressive migration structure - with a live fallback available at each traffic threshold - made the load-period cutover operationally safe.

At the 40% threshold, a concurrency issue in the address validation service appeared that had not been visible in shadow testing or in the February rollout attempt. The team diagnosed, patched, and revalidated within sixteen hours. The full cutover completed on schedule. The new system held under the highest traffic volume it had seen, including a marketing-driven spike on the second day of the rollout that exceeded the load test design parameters by a meaningful margin.

---

## What This Work Required of the Team

The program's outcome was a technical success. Recording it honestly requires also recording what that success cost.

Fourteen months is a long time to ask a team to maintain two parallel systems, absorb two schedule slips, catch two near-misses in the final third of a long program, and execute a rollout that had to be paused and restarted before it could be completed. The people who did this work did it while carrying a dual-system maintenance load that had been underrepresented in the original estimate, and while communicating changed timelines to stakeholders who had legitimate reasons to expect the program to be further along.

The two near-misses were caught by individuals acting beyond their assigned scope. One was reviewing shadow comparison logs at 11 PM during a period she was not scheduled to monitor. One was watching production dashboards through the night during a phase that did not have formal overnight coverage. Those catches made the difference between a clean launch record and two production incidents. They are not a staffing model to institutionalize. They are evidence that the final phases of programs of this type routinely require more deliberate support than this one had been given.

The people on this team did the work that was required, at the level of quality the problem demanded, for the full fourteen months the problem required. That is what the outcome is built on, and it should be named plainly.

---

## Implications and Recommendations

### For Teams Planning Parallel-Run Replacements

The parallel-run architecture is the right approach for replacing mission-critical transactional infrastructure without downtime. There is no other approach that provides equivalent customer protection during the transition. Teams should commit to it with accurate expectations about its sustained operational cost.

The cost of running two systems in parallel does not front-load. It compounds. The dual-system maintenance burden does not decrease as the new system matures. Program estimates should include an explicit, time-extended line item for old-system operations throughout the replacement period. The alternative - allowing the cost to be absorbed by the team as untracked work - has a human cost that affects program output.

Shadow mode validation is the technical mechanism that makes parallel-run replacement viable. The investment required to build shadow routing, dual instrumentation, and comparison tooling in the first sixty days of a program of this type pays for itself many times over. The first near-miss in this program was caught by shadow comparison data. Without that data, it would have reached production.

### For Organizations Governing These Programs

Schedule slips in parallel-run replacement programs should be understood as the quality standard working correctly, not as evidence of planning failure. Both slips in this program were the direct result of catching real defects or configuration failures before they reached customers. An organization that responds to slips with pressure to cut scope will find, in programs of this type, that scope cuts allow those defects to reach production instead.

The governance posture that served this program treated slips as information - evidence that the team's standards were holding - rather than as failures requiring correction. That posture required active communication at the executive level, not passive support for the program in the abstract. Engineering leadership communicated the reasons for each slip with specificity and held the organization's expectations in accurate alignment with program reality. That is harder than offering reassurance, and it is the necessary model for programs of this scope and duration.

### For Engineering Leaders Managing the Final Phase

The final phase of a parallel-run replacement carries the highest risk in the program and the most fatigued team. The structural conditions are unfavorable: the team has been carrying a sustained burden for months, the pressure to complete is at its peak, and the risk of missing something consequential is elevated. Both near-misses in this program occurred in the final third of the fourteen-month window.

The final phase should be resourced and managed as its own distinct program phase, not as the tail of the build phase. This means keeping senior engineers available and off new work during the rollout window. It means building explicit monitoring capacity for overnight and weekend coverage rather than relying on individuals' unassigned vigilance. It means treating the live traffic migration as a distinct operation with its own risk artifacts and escalation paths.

---

## Conclusion

The Meridian Commerce checkout rebuild is complete. The new system is in production, carrying full load, and performing against the abandonment benchmarks that motivated the program in March 2023. The cart-abandonment problem that started this work has resolved in line with the team's projections.

The open questions are the ones that follow every major platform replacement. The new system will accumulate technical debt over time; the question is whether the organization invests in it before that debt becomes structural again. The team that built it holds deep knowledge of its design; the question is how that knowledge is documented and transferred as people and roles change. The governance posture that absorbed two schedule slips without cutting scope was not the organization's default behavior; the question is whether it becomes the default, or whether it was particular to the individuals and circumstances of this program.

These are the right questions to hold after a success of this kind. They are not comfortable questions, but they are the ones that determine whether the work done here compounds into lasting organizational capability or remains a single episode.

What is not an open question: whether the work was worth doing, and whether the team did it well. Both are true. The team carried something genuinely heavy for fourteen months - between March 2023 and May 2024 - maintained its standards when the easier path was to lower them, caught the things that needed catching, and delivered what it had committed to deliver. The record should say so clearly, because work of this kind does not always speak for itself.
