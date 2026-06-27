---
entry_id: design-doc
axis: format
topic_slug: remote-work-policy
topic_label: Arguing a public position on return-to-office
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Anchor-Day Hybrid Policy - Implementation Design Document

## Status

In Review

## Problem

The organization has adopted a structured hybrid work arrangement (ADR-0012): two mandatory anchor days per week (Tuesday and Thursday) for all non-remote-designated employees, with the remaining three days fully flexible.

The ADR records the decision. This document works through how to implement it as an operational system - the policy schema, the components that must interoperate, the exception approval workflow, and the tracking mechanism needed to keep anchor days from eroding into suggestions.

Three constraints shape the implementation space:

**Dual-track authority gap.** Facilities and HR are running independent workstreams on different timelines. Facilities has already communicated a room-booking policy premised on five-day potential attendance. HR has not yet published guidance. These two systems must interoperate before the all-hands announcement on July 3. Currently, they will contradict each other on that date.

**Enforcement drift as the primary failure mode.** ADR-0012 named this explicitly: the risk is not defiance, it is quiet erosion. Anchor days become suggestions when no one tracks attendance and managers do not hold the line. An implementation that relies entirely on manager discretion will not hold past the first quarter.

**Unknown exception volume.** A non-trivial number of employees hold remote-eligible designations, documented medical accommodations, or relocation arrangements made before the policy existed. The exception approval path must be defined before July 3, not retrofitted under pressure once requests start arriving in volume.

## Proposed Design

### Policy schema

Each employee record carries three implementation-relevant fields:

| Field | Values | Authoritative owner |
|---|---|---|
| `location_type` | `anchor-required` / `remote-eligible` / `pending-review` | HR; set at hire, updated by manager + people team |
| `anchor_exception_status` | `none` / `approved` / `expired` | Exception workflow |
| `anchor_compliance_period` | Current quarter | Resets quarterly |

Employees with `location_type: remote-eligible` are excluded from anchor day requirements. All others default to `anchor-required`. The `pending-review` state covers new hires during their first two weeks and employees whose role classification is under active review.

### Components

**HR system (authoritative source).** Owns `location_type` for all employees and all exception records. Publishes a daily export to the room-booking system so attendance expectations reflect current headcount and exception status. This export is the primary interface between the Facilities and HR workstreams.

**Room-booking system (Facilities-owned).** Must ingest the daily HR export to calculate expected anchor-day attendance by building and floor. Must stop operating on a five-day attendance assumption before July 3. Reads `anchor_exception_status` to correctly handle rooms booked by or for exempt employees on anchor days.

**Manager dashboard (people team-owned).** Displays per-direct-report anchor compliance for the current quarter. Aggregates to trend data (consistent, inconsistent, never) rather than individual session logs - the purpose is drift detection, not surveillance. Visible to the manager and people team; not visible to skip-levels by default.

**Exception workflow.** Employee submits through the HR portal with a reason category (role reclassification, medical, caregiver, relocation, other). Manager reviews and approves or escalates within five business days. People team countersigns. Exceptions are time-bounded at one quarter maximum and must be renewed. Expired exceptions revert `anchor_exception_status` to `none` automatically, with a five-business-day notification before expiry.

### Data flows

```
HR system
  --> daily export --> Room-booking system (headcount + exception flags)
  --> read API    --> Manager dashboard (compliance status per employee)
  --> exception records (read/write for exception workflow)

Exception workflow
  --> status update --> HR system: anchor_exception_status field
  --> notification  --> Manager dashboard: exception flag on affected employee
```

### Facilities-HR interface contract

The daily export format and field definitions for `location_type` and `anchor_exception_status` must be agreed between Facilities and HR before July 3. The schema above proposes the fields; both teams should ratify the names and values. Neither team should replicate the other's authoritative data - the export is a read, not a copy.

## Alternatives Considered

**Manager discretion only (no tracking infrastructure).** Trust managers to enforce anchor days and handle exceptions informally, with no central system. Rejected because ADR-0012 already named enforcement drift as the primary failure mode. A system with no visibility into compliance cannot detect drift until it is already complete. Compliance becomes a function of individual manager relationships, which resolves inconsistently across the organization.

**Extend the existing Facilities badging system.** Use badge-swipe data from the current system, which was built for five-day attendance tracking, to measure anchor day presence. Rejected because the badging system has no integration with HR's `location_type` field. It would record swipes without knowing which employees are anchor-required versus remote-eligible, producing compliance data that cannot be acted on and cannot handle exceptions accurately.

**Self-reported attestation.** Employees self-report attendance via the HR portal; managers confirm. Rejected because self-attestation with manager confirmation adds friction for compliant employees and is trivially gamed by non-compliant ones. It also concentrates the enforcement burden on managers, which reinforces the drift risk rather than counteracting it.

## Risks and Open Questions

**Facilities-HR authority gap (high, before July 3).** If the room-booking system is not updated to reflect anchor-day headcount expectations before the all-hands announcement, employees will encounter booking constraints that contradict the policy they just heard. This is the most immediate risk and requires a named decision owner by June 28 - the date of the executive sponsor briefing.

**Exception volume spike at launch.** The workflow above assumes steady-state volume. A significant proportion of the workforce submitting exceptions in the first two weeks will produce a backlog under the five-business-day review window. The people team should define triage criteria before July 3 and communicate expected response times to employees when the policy is announced.

**Quarterly reset behavior for standing accommodations.** Exceptions expire at the quarter boundary and must be renewed. Employees with medical or caregiver accommodations that will not change quarter to quarter face recurring renewal overhead. Open question: should long-term accommodations be renewable annually, with the quarterly reset applying only to role-classification and relocation exceptions?

**Manager dashboard timing.** The dashboard does not need to launch on July 3 alongside the policy, but delay creates a blind spot. If the dashboard ships after Q3 begins, it should cover the full quarter retroactively, or the first quarter will have no drift signal. If it cannot be retroactive, the launch date should be treated as the start of the first measured quarter and communicated to managers explicitly.

**New hires after July 3.** The Manager FAQ (target: June 27) should include an onboarding section covering anchor day expectations. New hires who arrive after the policy is live will infer expected behavior from peer behavior, which may already be drifting by the time they join.

## Appendix

### Field value definitions

`location_type: anchor-required` - Employee works from a geography with office access and has no approved exception. Expected on-site Tuesdays and Thursdays.

`location_type: remote-eligible` - Role was designated remote at hire, or has been formally reclassified by manager and people team. No anchor day obligation.

`location_type: pending-review` - Classification is under active review, or employee is within their first two weeks. Anchor day expectation is advisory during this state.

`anchor_exception_status: approved` - Active approved exception. Duration and reason category are stored in the exception record; the field itself carries only the status.

`anchor_exception_status: expired` - Exception period lapsed without renewal. System reverts to `anchor-required` behavior. Manager and employee receive notification five business days before expiry.
