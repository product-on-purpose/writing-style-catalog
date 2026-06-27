---
entry_id: design-doc
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Tidemark Feedback Ranking Engine - Design Document

## Status

Accepted

## Problem

Small product teams accumulate customer feedback across support tickets, chat threads, survey exports, and notes from customer calls. The existing workflow to consolidate that scatter into a ranked roadmap is manual: read everything, copy items into a spreadsheet, and argue about priority in a meeting. The goal of Tidemark is to eliminate that step.

The ranking engine is the core subsystem. It must:

1. Accept normalized feedback items from multiple source connectors (the ingestion layer is designed separately; this doc covers ranking and output only).
2. Group items by recurring theme without requiring users to define themes upfront.
3. Score each theme so the output order is defensible to a product team - not just algorithmically consistent, but intuitively correct for a team comparing what customers asked for this month versus six months ago.
4. Produce a shareable read-only view that a team can send to stakeholders without requiring stakeholder sign-in.

Constraints that shape the solution space:

- Target teams are 2-20 people. The output must be usable without data science expertise.
- Input volume ranges from dozens to a few thousand items per sync depending on team size and how long feedback has been accumulating. The engine must handle both extremes with the same code path.
- The CLI runs locally (`tidemark sync`). Ranking may call a remote service for theme extraction, but the core scoring step must work without a persistent server.
- The shareable view (`tidemark share`) is a static URL. It cannot require authentication on the reader side.

## Proposed Design

### Data model

A normalized feedback item (produced by any source connector) carries:

```
FeedbackItem {
  id:         string    // stable across syncs
  source:     string    // connector id: "zendesk", "csv", "slack-channel"
  text:       string    // raw feedback text, max 4000 chars
  created_at: ISO8601   // original creation date, not import date
  tags:       string[]  // optional; connector may pass through existing labels
}
```

A theme groups one or more feedback items:

```
Theme {
  id:       string    // content-hash of the canonical phrase
  label:    string    // 3-7 word summary generated at extraction time
  items:    string[]  // FeedbackItem ids
  score:    number    // computed by the scoring step
  recency:  ISO8601   // created_at of the most recent item in this theme
}
```

### Theme extraction

Theme extraction is a remote call to a text-grouping endpoint. The input is a batch of FeedbackItem texts; the output is a mapping from item id to theme label. The local client:

1. Sends items in batches of 200.
2. Deduplicates by content hash before sending; items already present in the local store skip the extraction call entirely.
3. Writes extraction results to a local SQLite store (`~/.tidemark/store.db`) so subsequent syncs only send new items.

The extraction step does not assign scores. It returns labels and groupings only.

### Scoring

Scoring runs entirely locally after extraction returns. The score for a theme is:

```
score = frequency_weight * log(item_count + 1)
      + recency_weight  * decay(days_since_most_recent_item)
```

Default weights: `frequency_weight = 0.6`, `recency_weight = 0.4`. These are configurable in `.tidemark/config.toml` but ship with the defaults.

The `decay` function returns 1.0 for items created within the last 30 days and decreases to 0.0 at 365 days. The curve is linear.

Scores are recomputed on every sync. The local store caches item counts and recency values per theme so that scoring does not re-read all items.

### Shareable view generation

`tidemark share` produces a static JSON snapshot of the current ranked theme list and uploads it to a Tidemark-hosted CDN bucket. The command returns a URL of the form:

```
https://tidemark.io/view/<token>
```

The token is a 16-character base62 string derived from a hash of the workspace ID and the sync timestamp. Views are immutable: a new sync produces a new URL; the old URL continues to work until it expires (default: 90 days).

The view page is a pre-built static shell that fetches the JSON snapshot at load time. Readers do not need a Tidemark account. The shell is hosted at `tidemark.io/view/*` and served from the same CDN.

### Component boundaries

```
CLI (local)
  |
  +-- SourceConnectors[]     <- ingestion; designed separately
  |
  +-- ExtractionClient       <- remote call; batches FeedbackItems, returns Theme labels
  |
  +-- LocalStore (SQLite)    <- caches items, themes, extraction results
  |
  +-- ScoringEngine          <- runs locally; reads from LocalStore; writes scored Theme list
  |
  +-- ShareClient            <- uploads JSON snapshot; returns view URL
```

The CLI is the only entry point. There is no agent, daemon, or background sync.

## Alternatives Considered

### Scoring on the server, not the client

An earlier design computed scores server-side and returned a pre-ranked list alongside extraction results. This simplified local code but introduced a round-trip dependency for every sync and required the server to know each team's weight configuration.

Scoring moved to the client because the inputs (item counts, recency values) are already available locally after extraction, the computation is cheap, and keeping it local makes the weight configuration transparent. Teams can inspect and modify `.tidemark/config.toml` without trusting a server to honor it.

### Embedding-based clustering instead of a text-grouping API

An earlier spike used local sentence embeddings to cluster feedback before ranking. Clustering quality was acceptable for batches of a few hundred items but degraded on short support-ticket text (under 15 words) and required shipping a 200 MB model file with the CLI package.

The text-grouping API produces more consistent labels at short text lengths and removes the model weight from the install. The tradeoff is a remote dependency during extraction. Items extracted on a previous sync are never re-sent, so the dependency is absent for teams who sync daily against a stable feedback corpus.

### Mutable shareable views (live-updating URLs)

An earlier design updated the view JSON in place on each sync, so the same URL would reflect the latest rankings. This failed in user testing: stakeholders who bookmarked a link expected it to represent a moment in time, not a live feed, and two stakeholders in the same meeting were looking at different states of the same URL.

Immutable snapshots with new URLs on each sync resolved the ambiguity. The old URL remains accessible, which is useful for comparing how priorities shifted between syncs.

## Risks and Open Questions

**Extraction API availability on first sync.** The first sync for a new team sends all historical items. A team with years of accumulated feedback in a high-volume ticket tracker could send tens of thousands of items. The batch architecture handles this at the API level, but first-sync duration is unbounded from the user's perspective. Risk: the sync looks hung. Mitigation: progress output in the CLI (`tidemark sync --verbose`) and a clear completion signal. No timeout is applied to first syncs.

**SQLite concurrency.** The local store serializes writes. If a user runs `tidemark sync` and `tidemark share` simultaneously, the share command may read a partially-updated store. Current mitigation: the CLI prints a warning if the store is locked and exits rather than reading a partial state. Open question: whether a file lock is needed or whether the warning is sufficient for the target user base.

**Recency weight calibration.** The default weights (`frequency: 0.6`, `recency: 0.4`) were set based on feedback from the twenty-two teams in the early-access cohort. That cohort validated that the ranked output matched their intuition, but skewed toward teams with active support volumes. Teams that generate feedback in infrequent bursts - quarterly surveys, annual customer calls - may find the recency decay too aggressive. Open question: expose a decay half-life setting in config, or add a `--recency-mode` flag to sync.

**View expiry.** The 90-day default was chosen without data on how long stakeholders refer back to shared roadmap snapshots. If teams share views with stakeholders who return to them months later, 90 days may be too short. Open question: make expiry configurable per workspace, or extend the default after collecting post-launch usage data.
