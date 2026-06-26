---
entry_id: decision-log
axis: style
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

## Context

Small product teams - early-stage companies without a dedicated product manager - typically manage customer feedback across three or more tools simultaneously: a chat tool for inbound messages, a ticket tracker for engineering requests, and a spreadsheet where someone collects and loosely ranks what keeps coming up. The person responsible for the roadmap rebuilds that spreadsheet by hand each planning cycle, pulling from scattered sources and making priority calls without a shared record of the reasoning. When pressed on why an item ranked where it did, the answer is typically "we kept hearing it" - a memory, not a record. The output that gets shared with stakeholders is a list, not a ranked roadmap with the feedback behind it.

There is no shortage of feedback. The problem is that it lives in fragments, and no existing tool was built specifically to collect those fragments, rank them, and produce a shareable output with the reasoning visible.

## Options

Three approaches were on the table during product definition.

**Integration layer on existing trackers.** Add ranking fields to whatever ticket tracker the team already uses. This meets teams where they are, but leaves the output fragmented inside the tracker - nothing produces a roadmap that can be shared and explained outside the tool.

**Full analytics platform.** Ingest raw feedback data, apply quantitative scoring, and output weighted priority lists. More rigorous, but requires structured input most small teams do not have. The setup cost was disproportionate for the team size this was built for.

**Lightweight intake-and-ranking product.** Accept feedback from any source as freeform input, surface recurring themes, let the team rank and weight them, and export a shareable roadmap. Low setup friction, works regardless of existing tooling. The risk: teams may resist adding a new tool, so the output value has to justify the switch.

## Criteria

Two constraints governed the evaluation: the tool must work without clean structured data as a prerequisite, and it must produce output a team can share with a non-technical stakeholder without a walk-through. A secondary goal was to keep setup friction low enough for a team that does not have a dedicated PM.

## Decision

We built the third option. The integration approach did not solve the output problem - stakeholders still received a ticket list, not a roadmap. The analytics platform addressed rigor but not accessibility; it was built for teams with data pipelines, not teams with a folder of customer notes.

Tidemark is the lightweight option. Paste or import feedback from wherever it lives, surface what keeps appearing, rank the clusters against each other, and export a roadmap that shows priority alongside the feedback behind it. It launches next week. Teams can sign up at tidemark.io.
