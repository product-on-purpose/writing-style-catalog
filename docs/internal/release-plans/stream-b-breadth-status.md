---
title: Stream-B Breadth - Status and Promotion Tracker
date: 2026-06-28
status: Wave 1 + Wave 2A (professional, 10) promoted; 33 drafts awaiting review; Wave 2B (public, 13) next -> v0.5.0
owner: maintainer (promotion decisions); agent (generation + gating)
related:
  - docs/internal/release-plans/stream-b-promotion-proposal.md (the wave plan; Wave 1 DONE)
  - docs/internal/release-plans/promotion-and-release-runbook.md (the step-by-step promote + release)
  - docs/internal/agentic-generation-spec.md (the factory design + canonical gate prompts)
  - tools/agentic/README.md (how to run each harness)
  - _agent-context/plans/2026-06-25-master-plan-hand-driven-generation.md (the production plan)
  - CHANGELOG.md
---

# Stream-B Breadth: Status and Promotion Tracker

This is the master record of the Stream-B breadth program: what is complete, what is
awaiting your review, and what happens next. It is the single place to drive the
draft-to-stable promotion decision.

## Where things stand (2026-07-01)

- **Format axis: 72 entries = 39 stable + 33 draft.** (The other three axes are unchanged
  at 15 stable each, so the catalog is 117 entries total = **84 stable + 33 draft**.)
- **Wave 1 is promoted and released.** The 14 eng/PM-core formats (see the promotion proposal)
  are now `stable`, each rendered across all 12 anchor topics (168 worked samples) and
  date-gated, and shipped as **v0.4.0** (tag pushed; GitHub Release published by `release.yml`).
  Format stable count went 15 -> 29; catalog curated count 60 -> 74.
- **Wave 2A (professional, 10) is promoted.** user-manual, resume, bio, performance-review, memo,
  cold-outreach, cover-letter, recommendation-letter, support-reply, review-response are now
  `stable`, each rendered across all 12 anchor topics (120 worked samples) and date-gated. Format
  stable count went 29 -> 39; catalog curated count 74 -> 84. Ships in **v0.5.0** with Wave 2B.
- The original 57 drafts were produced in **10 gated batches** (PRs #66 through #75), all merged
  to `main`. Each batch is six candidates; each candidate is one isolated subagent render, then
  two gates (below). 24 of those 57 have since been promoted (Wave 1 + Wave 2A), leaving **33 draft**.
- **Every format family now has at least two worked entries.** The two families that were
  empty before this program - `professional/response` and `public/copy` - are filled.
- The docs site rebuilds and **auto-deploys on every push to `main`** (`.github/workflows/build-site.yml`),
  so all 72 formats are live now. Draft entries render a **"Draft - under review" callout** so
  visitors can tell drafts from the stable catalog.
- **The marketplace manifests (`library.json` / `plugin.json`) now advertise 84 curated entries**
  (bumped at each promotion wave; the manifest validator enforces `plugin.json` == `library.json`).
  The remaining 33 drafts are not curated and are excluded from the count until promoted.
- **The production method is now tracked tooling.** What was ephemeral scratchpad scripts is now
  `tools/agentic/` (Workflow templates) + `tools/promote.py` (the guarded, transactional
  draft->stable flip), with the design in `docs/internal/agentic-generation-spec.md` and the
  operational steps in `docs/internal/release-plans/promotion-and-release-runbook.md`.

## Complete: the full format inventory

Legend: no tag = **stable** (the reviewed baseline); `†` = **promoted in Wave 1 (v0.4.0)**;
`‡` = **promoted in Wave 2A (v0.5.0)**; `(draft)` = **awaiting promotion review**.

### professional
- **deliberation** - adr, prd, design-doc †, rfc †
- **instruction** - readme, technical-reference, faq †, runbook †, how-to-guide †, user-manual ‡
- **progress** - changelog-entry, daily-standup, meeting-notes, status-report, meeting-agenda †
- **brief** - one-pager, project-brief †, pitch-deck †, proposal †, resume ‡, bio ‡
- **appraisal** - postmortem †, retrospective †, performance-review ‡
- **messaging** - email, slack-message, memo ‡
- **outreach** - cold-outreach ‡, cover-letter ‡, recommendation-letter ‡
- **response** - support-reply ‡, review-response ‡

### public
- **broadcast** - blog-post-long-form, tweet-thread, press-release (draft), release-notes †, newsletter (draft), announcement †, listicle (draft), customer-story (draft)
- **copy** - landing-page (draft), ad-copy (draft), product-description (draft), testimonial (draft)
- **position** - whitepaper, op-ed (draft), manifesto (draft), open-letter (draft), editorial (draft)
- **accountability** - incident-report †, public-statement (draft)

### personal
- **correspondence** - thank-you-note (draft), condolence-note (draft), apology (draft), invitation (draft), love-letter (draft)
- **essay** - personal-essay (draft), memoir-excerpt (draft), personal-statement (draft)

### ceremonial
- **tribute** - eulogy (draft), toast (draft), obituary (draft), wedding-vows (draft), acceptance-speech (draft), commencement-speech (draft)

### contemplative
- **devotion** - devotional-entry, prayer (draft), guided-meditation (draft), sermon (draft), blessing (draft)
- **journal** - journal-entry (draft), gratitude-journal (draft)

## How each draft was gated (so review can lean on it)

Every candidate passed two gates before merge:

1. **Deterministic gate (`tools/validate.py`, 7 checks + Gate 2).** Schema validity,
   taxonomy membership (the domain/family is real), cross-references all resolve, no
   em/en-dashes, and the pedagogical-substance bar (tells + anti_patterns + failure_modes
   present and non-trivial). Drafts are exempt from the Gate 2 *sample-count* check (12
   worked samples per entry) by design - that requirement attaches at promotion, not draft.
2. **Cross-vendor distinguishability gate (Codex, via `codex:codex-rescue`).** For each
   candidate the judge reads the entry AND its declared `confusable_with` neighbor's own
   `ENTRY.md`, then checks: neighbor accuracy (the disambiguation describes the neighbor as
   the neighbor describes itself), failure-mode discipline (each failure_mode is the format
   over-hitting its OWN register, never a misuse or a neighbor move), pairs consistency (no
   `pairs_well_with` entry that the format's own anti_patterns forbid), integrity (no
   fabricated stats or invented authorities), and the dash rule.

Revise rate by batch (3-10 this session): 6/6, 2/6, 0/6, 2/6, 2/6, 2/6, 1/6, 1/6. The two
prompt changes that drove it down: each agent reads its neighbor's file before describing
it, and pairs are chosen to fit the format's nature up front. Every flagged item was fixed
in place (targeted edits, never regeneration) and re-validated.

**What review still owes that the gates do not cover:** the gates prove each entry is
schema-valid, internally consistent, and *distinguishable from its nearest neighbor*. They
do not certify that a format *earns a permanent slot in the stable catalog* (the "breadth
dilutes the moat" judgment), nor that the canonical template and llm_instruction_phrasing
are the best possible. Those are the promotion call.

## Awaiting your review: the remaining 43 drafts

The 43 remaining drafts are staged for a `draft -> stable` decision. Promotion is now a guarded,
tooled flow (not a hand-edit of `review_status`):

1. Review the entry (and optionally re-run the Codex distinguishability gate on it).
2. Render it across all 12 anchor topics while it is still `draft` (drafts are Gate-2-exempt, so
   `validate.py` stays green during the render): edit `FORMATS` in `tools/agentic/promote.js` and
   run it with the Workflow tool.
3. Flip it with `python tools/promote.py <ids>`. This is the maintainer action that sets
   `review_status: stable`. It is transactional and **refuses to flip any entry that is not yet
   rendered on all 12 topics**, so it cannot leave `main` red on the Gate 2 sample-count check.

You can promote in any grouping (by family, by confidence, a first tranche of the strongest,
etc.). The recommended grouping is the wave plan in the promotion proposal.

## Next (in dependency order)

1. **Wave 2** (the next promotion): the 23 remaining professional + public drafts. See the
   [promotion proposal](stream-b-promotion-proposal.md) for the exact list, and the
   [promotion-and-release runbook](promotion-and-release-runbook.md) for the step-by-step. In
   brief: render (`tools/agentic/promote.js`) -> validate -> date-gate the dated formats ->
   flip (`tools/promote.py`) -> bump counters + manifests -> validate (Gate 2 active) -> build ->
   PR -> cut **v0.5.0**. Counter deltas: stable 74 -> 97, Format stable 29 -> 52, vertical samples
   888 -> 1164, drafts 43 -> 20.
2. **Hold-20** (a later, deliberate audience-expansion release): the 20 personal / ceremonial /
   contemplative drafts. Off the PM/builder beachhead - promote when broadening the advertised
   identity is the goal, not before.
3. **Marketplace registry re-pin** (separate manual step, in `product-on-purpose/agent-plugins`):
   re-pin the registry entry to each new release tag after it ships.

## On paid CI / API (correction)

Earlier notes framed a "paid-CI generator-tier decision" as a pending lever. It is not. The
master plan fences the paid-API decision to three narrow triggers: a batch too large to
hand-drive, unattended contributor-PR admission, or pinned model/seed provenance for
*published* distinguishability scores. **None were hit.** All 57 breadth candidates (batches
1-10), the 14 Wave-1 promotions with their 168 rendered samples, and the earlier 720-sample
depth matrix were generated by free in-session subagents and gated by the free cross-vendor
Codex judge. The subagent factory was the whole point, and it carried the entire run at zero
marginal API cost. Paid CI remains fully fenced and is not required for promotion, rendering,
manifests, or release.

## Reproducing / continuing the generation loop

The breadth loop is now a tracked harness, `tools/agentic/generate.js` (the "Add new entries"
loop A in `tools/agentic/README.md`; design in `docs/internal/agentic-generation-spec.md`). If
more breadth is ever wanted (≈12-15 min per batch):

1. Edit `tools/agentic/generate.js` `CANDIDATES`: pre-validated candidates, each with
   `id, name, domain, family, dp, one_liner, concept` (the concept embeds the neighbor
   contrast), `pairs_well_with, avoid_with, confusable_with, typical_voices, typical_tones`.
   Cross-ref ids must already exist; prose fields are DOUBLE-quoted JS strings or backticks
   (YAML-style `''` doubling breaks single-quoted JS).
2. `Workflow({ scriptPath: "tools/agentic/generate.js" })` - one read-its-neighbor sonnet agent
   per candidate writes its own file.
3. `validate.py` + `build-indexes.py`; dispatch the Codex distinguishability gate (one
   `codex:codex-rescue` agent; canonical prompt in the spec); apply fixes with
   `tools/agentic/remediate.js` or targeted edits.
4. `gen-site.mjs` + `cd site && npm run build`; bump the two README draft counters; commit
   (conventional, dash-free); PR; `gh pr checks --watch`; squash-merge; sync `main`.

**The breadth run was intentionally stopped** at 57 candidates (43 still draft after Wave 1):
the remaining uncovered formats are niche (examen, syllabus, abstract, grant-proposal,
api-documentation, dedication, benediction, podcast-script) or overlap existing entries, so
further batches would trade distinctiveness for raw count. Promotion (depth) is the higher-value
next lever.
