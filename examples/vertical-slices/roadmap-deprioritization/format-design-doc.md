---
entry_id: design-doc
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Insights CSV Export - Design Document

## Status

Draft - September 12, 2026
Owner: Dario Reyes (engineering)

## Problem

ADR-0027 established that the Insights dashboard will not ship in Q3 because the billing-system migration consumed all available engineering capacity. The ADR commits to shipping a CSV export of the Insights data layer before September 30 as a stopgap, giving the four key accounts access to their data while the full dashboard is built in Q1 2027.

This document specifies how the CSV export will be implemented. The constraints that shape the solution space:

- **Timeline.** Backend endpoint must be complete by September 19; frontend integration and QA by September 24; release on September 26. September 30 is a hard deadline - there is no slip past end of quarter.
- **Staffing.** Dario Reyes is the sole engineering owner. One engineer, two weeks of capacity.
- **Data availability.** The underlying event data is already queryable from the existing analytics database. No new data collection, pipeline work, or schema additions are required.
- **Self-serve requirement.** Exports must complete without support involvement. Any flow requiring manual triggering by the team, a waiting period longer than a few seconds on typical accounts, or a follow-up communication to retrieve the file is out of scope for this timeline.
- **Scope boundary.** This is a stopgap, not a preview of the Q1 dashboard. It must not require infrastructure that would overlap with or create dependencies on the Q1 Insights build starting October 6.

## Proposed Design

The export is a synchronous streaming HTTP endpoint attached to the existing data access layer.

### Request flow

1. The user navigates to **Settings > Data and Analytics > Export** in the Meridian web app.
2. A "Download CSV" button issues a `GET /api/v1/insights/export` request with the user's session cookie.
3. The server authenticates the request through the existing session middleware, resolves the account ID, and delegates to `ExportService`.
4. `ExportService` opens a cursor on `EventQueryRepository` scoped to the resolved account ID and begins streaming rows.
5. The HTTP response is returned with `Content-Type: text/csv` and `Content-Disposition: attachment; filename="insights-{account_id}-{export_date}.csv"`, writing rows in chunks as the cursor advances.
6. The stream closes when the cursor is exhausted. No temporary file is written to disk; no object storage is involved.

### CSV schema

Each row represents one event. Column order is fixed:

```
user_id           UUID of the user who triggered the event
event_name        The recorded action (e.g., page_view, feature_used)
event_timestamp   UTC timestamp, ISO 8601 format (e.g., 2026-09-01T14:32:00Z)
session_id        UUID grouping events within a single session
plan_tier         The account plan active at the time of the event
```

The header row is always emitted first. All string fields are quoted. Timestamps are always UTC with no localization. The export covers all events from account creation through the end of the previous calendar day (UTC).

### Component boundaries

Three components are involved. Two are new; one is pre-existing and requires no modification.

- **`ExportController`** (new): Thin HTTP handler. Validates the authenticated session, resolves the account ID from the session context, and delegates to `ExportService`. Pipes the streaming response back to the client. Returns `200` on success; returns a structured error response if the account cannot be resolved or the repository query fails. Contains no business logic.
- **`ExportService`** (new): Owns the export logic. Opens a cursor on `EventQueryRepository`, iterates rows, serializes each to a CSV line, and writes to the response writer. Emits the header row before the first data row. Enforces the export scope: all events through end of previous calendar day, UTC.
- **`EventQueryRepository`** (existing): Already used by internal analytics tooling and the billing migration audit queries. Wraps the analytics database. `ExportService` calls `queryAllByAccount(accountId, endDate)` on this interface. No modifications to the repository.

### Authentication and authorization

The endpoint sits behind the existing session middleware that guards all `/api/v1` routes. No new auth logic is introduced. Users can only export data for the account attached to their session. Cross-account access is not possible through this interface.

### Frontend

The Settings page gains one new section: **Data and Analytics**. It contains a single "Download CSV" button. The button is disabled while a request is in flight and re-enabled on response. A browser-native download dialog handles file receipt on completion. Error states (export failure, session expiry) surface as inline text below the button. No other UI changes are in scope.

## Alternatives Considered

### Async generation with email delivery

Generate the CSV in a background job and email the user a download link when complete. This is the standard pattern when generation can take minutes or when file sizes are large enough that a synchronous response would time out.

Rejected. The implementation requires a background job queue, transient file storage, and an outbound email trigger - none of which are plumbed for this endpoint today. Adding that infrastructure would consume time the team does not have before September 26 and would create a dependency on the email delivery stack for a feature that will be superseded in Q1. The synchronous streaming approach fits within the two-week window without new infrastructure.

### Pre-generated daily exports in object storage

Generate each account's export nightly and serve downloads from a stable per-account URL. Reduces per-request compute cost; downloads are always fast.

Rejected. Requires a nightly generation job, IAM scoping per account, and pre-signed URL generation on download. The object storage bucket structure would likely overlap with infrastructure the Q1 Insights build will want to own and design for its own purposes. Introducing it now as a stopgap creates unplanned technical debt for the Q1 team. The synchronous approach requires no shared infrastructure.

### Paginated export across multiple smaller files

Break the export into daily or monthly segments and let users download each independently.

Rejected for this scope. Most accounts will not produce file sizes that require chunking. Pagination adds UI complexity - which segments are available, which have been downloaded, how to merge them for analysis - that is out of proportion to the two-week timeline. If large-account export proves problematic after launch, pagination can be added as a patch before Q1 without altering the schema or the endpoint contract.

## Risks and Open Questions

**Large account file sizes.** Accounts with several years of event history may produce exports in the range of 50-100 MB. Synchronous streaming handles this without in-memory accumulation, but client-side download behavior at that file size should be validated during QA. If any of the four key accounts are known to have high event volume, test against representative data before September 24.

**Billing release regressions.** The billing-system migration goes to production the week of September 19. The CSV backend endpoint is due the same week. If production regressions surface and require Dario Reyes's attention, frontend integration and QA may slip from September 24 toward September 30. September 30 is a hard deadline; there is one week of float, but it should be treated as a wall, not a buffer.

**Rate limiting.** No decision has been made on how frequently a user can trigger exports. For the Q3 release, no rate limiting is applied. If high-frequency export requests become a load concern after launch, a per-account daily limit can be added as a patch; no schema or API contract change is required to do so.

**Q1 data contract.** The column schema defined here represents the canonical shape of the Insights event data that the Q1 dashboard will visualize. The Q1 engineering design document (kickoff October 6) should treat these columns and the `EventQueryRepository` interface as established contracts and build on them rather than defining a parallel data model. Divergence here would require a migration before the dashboard ships.
