---
entry_id: technical-reference
axis: format
topic_slug: roadmap-deprioritization
topic_label: Telling stakeholders a committed feature is being cut this quarter
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Insights Dashboard - Delivery Change Record

Authoritative reference for the Q3 Insights scope change. Updated only when the underlying delivery plan changes.

**Status:** Active - issued Q3
**Applies to:** Sales team; key customers with Q3 Insights commitment
**Owner:** Product

---

## 1. Change Summary

| Field | Value |
|---|---|
| Feature | Insights analytics dashboard |
| Original commitment | Q3 (this quarter) |
| Revised target | Q1 (first quarter, next calendar year) |
| Q3 stopgap | Analytics CSV export, available by end of September |

---

## 2. Root Cause

The mandatory billing-system migration overran its projected scope and consumed the engineering capacity reserved for Insights in Q3.

| Factor | Detail |
|---|---|
| Migration type | Mandatory (infrastructure dependency; no scope reduction available) |
| Impact on Insights | Q3 engineering capacity insufficient for a complete release |
| Consequence of shipping on original date | Partially built product delivered to customers |
| Decision | Defer Insights to Q1; ship CSV export as Q3 stopgap |

---

## 3. Q3 Stopgap: Analytics CSV Export

A downloadable export of the underlying analytics dataset, available to all affected customers before the end of Q3.

### 3.1 Specification

| Field | Value |
|---|---|
| Availability date | End of September (end of Q3) |
| Access method | Download from account settings |
| Format | CSV, UTF-8 encoded |
| Data scope | Same dataset Insights would visualize |
| Refresh | On-demand snapshot; does not update after download |
| Granularity | One file per account, per request |

### 3.2 CSV Column Schema

| Column | Type | Description |
|---|---|---|
| `event_date` | date (YYYY-MM-DD) | Date the event occurred |
| `event_type` | string | Category of tracked event |
| `user_id` | string | Anonymized user identifier |
| `session_id` | string | Session containing the event |
| `value` | numeric | Quantitative value; interpretation depends on event_type |
| `properties` | JSON string | Additional metadata for the event |

### 3.3 Constraints

- No pre-aggregation or filtering is applied. The export contains the full account dataset.
- Computed aggregates and visualizations are not included. Customers perform their own analysis in a spreadsheet or BI tool.
- The export is not a live feed. For updated data, a new export must be requested.

---

## 4. Q1 Deliverable: Insights Dashboard

The full Insights analytics dashboard, rescheduled to Q1.

### 4.1 Specification

| Field | Value |
|---|---|
| Delivery target | Q1 (first quarter, next calendar year) |
| Scope | Original Insights specification; no features removed |
| Engineering allocation | Full Q1 allocation |
| Dependency | Billing migration complete by end of Q3 |

### 4.2 Constraints

- The Q1 target is contingent on the billing migration completing within Q3. If the migration extends beyond Q3, the Q1 target will be reassessed and this record will be updated.
- Customers who use the Q3 CSV export retain their downloaded data. Insights adds live, interactive analysis on top of the same dataset; it does not supersede or replace the export.

---

## 5. Key Dates

| Date | Event |
|---|---|
| End of September | CSV export available to all affected customers |
| End of Q3 | Billing migration projected to complete |
| Start of Q1 | Insights engineering resumes at full allocation |
| Q1 | Insights dashboard release target |

---

## 6. Notes

- **No partial Insights release in Q3.** A partially built product will not ship. The CSV export is the only Insights-related Q3 deliverable.
- **The CSV export does not substitute for Insights.** The export covers raw data only. Dashboards, filtering, and visualizations are not available until Q1.
- **Specification stability.** This record changes only when the delivery plan changes, not to clarify prose. Version: initial issue, Q3 scope change.

---

## 7. Contacts

| Topic | Contact |
|---|---|
| Customer commitments and account-level questions | Sales team |
| CSV export access and technical questions | Product support |
| Insights Q1 scope and roadmap questions | Product team |
