---
entry_id: technical-reference
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Tidemark

Tidemark is a feedback consolidation and prioritization tool that ingests customer input from multiple sources, groups items into themes, and produces a single ranked, shareable roadmap artifact for small product teams.

`status: public beta` `launch: 2026-07-08` `pricing: free during beta`

---

## Core Concepts

| Concept | Definition |
|---------|------------|
| Workspace | Top-level container for one product's feedback corpus and its active roadmap. One workspace per product. |
| Feedback item | A discrete unit of customer input: a request, complaint, or observation, with an associated source label and timestamp. |
| Theme | A labeled cluster of semantically similar feedback items, assigned automatically on ingest and editable by workspace members. |
| Signal weight | Aggregate numeric score for a theme, calculated from item count, source multipliers, and submitter segment multipliers. |
| Ranked roadmap | The primary output artifact: themes sorted by signal weight, with supporting item count and a shareable public URL. |

---

## Supported Input Sources

| Source type | Method | Required fields |
|-------------|--------|-----------------|
| Spreadsheet export | CSV file upload (5 MB max) | `date`, `text` |
| Survey export | CSV file upload | One response per row; multi-question surveys parsed into one item per question |
| Email | Forward to workspace ingest address | Subject line and body parsed as a single item |
| Plain text | Paste or `.txt` upload | One feedback item per line |
| Webhook | POST to workspace REST endpoint | See Webhook payload schema below |

Optional field supported by all methods: `submitter_id` (string). Providing this field enables per-submitter segment scoring.

---

## Output Types

| Output | Format | Notes |
|--------|--------|-------|
| Ranked roadmap | In-app view + shareable URL | URL is public to anyone with the link in v1.0 |
| Snapshot export | CSV or PDF | Captures current sort order and item counts at export time |
| Weekly digest | Email | Top themes since last digest; recipient list configured per workspace |

---

## Webhook Payload Schema

`POST https://ingest.tidemark.io/v1/workspaces/{workspace_id}/items`

```json
{
  "source": "string (required)",
  "text": "string (required)",
  "date": "ISO 8601 string (optional; defaults to receipt timestamp)",
  "submitter_id": "string (optional)",
  "tags": ["string (optional array)"]
}
```

The endpoint returns HTTP 202 on receipt. Processing is asynchronous; item appearance in the ranked roadmap is not guaranteed within the same request lifecycle.

`source` is a free-form label that identifies the originating channel (e.g., `"support"`, `"sales-call"`, `"nps-survey"`). Source labels that match a configured weight rule receive the corresponding multiplier; unmatched labels default to 1.0.

---

## Minimum CSV Structure

The smallest valid file upload:

```
date,text
2026-05-01,I can't find where to add a second team member
2026-05-03,Would love bulk export to PDF
2026-05-08,Can we import our existing spreadsheet?
```

Additional columns are ignored. Rows missing `date` or `text` are skipped and reported in the upload summary.

---

## Scoring Model

Signal weight is calculated per theme after each ingest run:

```
signal_weight = sum(item_base_score * source_multiplier * segment_multiplier)
  for each item in theme
```

| Parameter | Default | Configurable |
|-----------|---------|--------------|
| `item_base_score` | 1.0 | No (v1.0) |
| `source_multiplier` | 1.0 | Yes - set per source label in workspace settings |
| `segment_multiplier` | 1.0 | Yes - set per submitter segment in workspace settings |

Segment assignment requires `submitter_id` on the item and a matching segment rule in workspace settings. Items without `submitter_id` use the default segment multiplier.

---

## Capability Comparison

| Capability | Spreadsheet | Ticket tracker | Tidemark |
|------------|-------------|----------------|---------|
| Multi-source ingestion | Manual copy-paste | Manual or per-tool connector | Native across all source types |
| Automatic theme grouping | No | No | Yes |
| Signal-weighted ranking | Manual formula | No | Yes - configurable multipliers |
| Shareable roadmap URL | No | Requires separate export step | Yes - live URL, always current |
| Audit trail to source items | Manual | Partial | Yes - each theme links to its items |

---

## Constraints and Limitations

- v1.0 supports one active roadmap per workspace. Separate product lines require separate workspaces.
- Automatic theme grouping is English-language only in v1.0.
- Shareable roadmap URLs are accessible to anyone with the link. Password protection is not available in v1.0.
- Webhook delivery is not retried on failure. The ingest endpoint returns HTTP 202 on receipt, not on processing completion. Poll the roadmap or use the digest to confirm items appear.
- File upload limit is 5 MB per file. Larger corpora should use the webhook endpoint in batches.
- The scoring model does not incorporate revenue, churn, or contract-value data in v1.0. All items have equal base scores.
- Theme labels assigned automatically are editable but not versioned. Editing a label does not trigger recalculation of signal weight.

---

## Access and Availability

Beta workspaces are provisioned within one business day of request.

Request access: `tidemark.io/early-access`

Beta workspace members can invite additional members via workspace settings. There is no seat limit during the beta period.

---

## See Also

- Webhook Reference - full payload schema, authentication headers, error codes, and rate limits
- Scoring Model Guide - configuring source multipliers and submitter segment rules
- Export Formats - CSV column schema and PDF layout specification
- Workspace Settings - ingest address, team member roles, digest cadence, and weight rules
- Roadmap Sharing - URL permission model, snapshot behavior, and planned access controls
