---
entry_id: decision-log
axis: style
topic_slug: team-milestone-celebration
topic_label: Marking the team shipping a hard, long project
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Milestone Record: Checkout Rebuild - Project Meridian Closed

**Date of record:** November 14, 2024
**Project:** Checkout system rebuild (codename: Meridian)
**Authors:** Maya Reyes (team lead), with contributions from Sam Chen and Dev Nakamura

---

### Context

The checkout system that Meridian replaced was seven years old, written before the current payment processor existed, and maintained by accretion rather than design. Cart abandonment had grown to a rate that required explanation in every planning cycle. Internal analysis traced the largest contributor to friction in the address and payment confirmation steps, both places where the old system had accumulated conflicting state.

In September 2022, leadership chose to rebuild rather than patch. That choice is recorded in the original project charter. This record marks the decisions made during the rebuild - the turns that determined whether it shipped and in what condition.

### Options at the critical turns

**Near-miss one (month four): schema migration.** The new system required a breaking change to the order-state schema. The options on the table: migrate all historical records and block launch; run dual schemas indefinitely; accept a translation layer for records before a cutoff date. Dev Nakamura surfaced a fourth option - a read-time shim with asynchronous backfill. This was not in the original design and required the team to carry it through six months of parallel operation before it could be retired.

**Near-miss two (month nine): payment gateway behavior mismatch.** The payment processor's sandbox diverged from its production behavior on timeout handling. Options: delay integration testing until production access was confirmed; mock the divergent behavior and document the known gap; pursue early production access through a vendor escalation. Sam Chen made the call to escalate. It took six weeks and consumed team capacity at a difficult moment. It also eliminated a class of unknown failure before launch.

**Launch slips (months eleven and thirteen).** The team slipped twice. Both times the stated reason was the same: the rollback path under partial rollout did not meet the standard the team had committed to. The standard: rollback completable within fifteen minutes at any traffic split, by a single on-call engineer, without a secondary approval. That bar was not met until week two of month fourteen.

### Criteria

Two constraints held throughout: the existing system could not degrade for customers already mid-flow during any transition, and the new system had to hold under the highest observed traffic in the prior year before full cutover was permitted.

### Decision

The team held both constraints. The final rollout ran under peak load and held.

This record names what that cost: fourteen months of parallel maintenance, two near-misses absorbed by individuals rather than by process, and two launch slips made against real pressure to ship. Maya Reyes, Sam Chen, and Dev Nakamura named the options when naming them was uncomfortable. That is what this milestone marks.
