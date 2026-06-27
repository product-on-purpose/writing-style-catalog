---
title: Stream-B Breadth - Status and Promotion Tracker
date: 2026-06-26
status: breadth-run complete; 57 drafts awaiting maintainer review
owner: maintainer (promotion decisions); agent (generation + gating)
related:
  - _agent-context/plans/2026-06-25-master-plan-hand-driven-generation.md (the production plan)
  - docs/internal/release-plans/plan_v0.3.0/adherence-gate-spec.md (the gate this rides)
  - CHANGELOG.md ([Unreleased])
---

# Stream-B Breadth: Status and Promotion Tracker

This is the master record of the Stream-B breadth program: what is complete, what is
awaiting your review, and what happens next. It is the single place to drive the
draft-to-stable promotion decision.

## Where things stand (2026-06-26)

- **Format axis: 72 entries = 15 stable + 57 draft.** (The other three axes are unchanged
  at 15 stable each, so the catalog is 117 entries total.)
- The 57 drafts were produced in **10 gated batches** (PRs #66 through #75), all merged to
  `main`. Each batch is six candidates; each candidate is one isolated subagent render,
  then two gates (below).
- **Every format family now has at least two worked entries.** The two families that were
  empty before this program - `professional/response` and `public/copy` - are filled.
- The docs site rebuilds and **auto-deploys on every push to `main`** (`.github/workflows/build-site.yml`),
  so all 72 formats are live now. Draft entries render a **"Draft - under review" callout**
  (added in this change) so visitors can tell drafts from the stable catalog.
- **The marketplace manifests (`library.json` / `plugin.json`) are deliberately unchanged.**
  They still advertise "60 curated entries"; drafts are not curated. They get bumped only
  when drafts are promoted (see Next).

## Complete: the full format inventory

Legend: no tag = **stable** (the reviewed baseline); `(draft)` = **awaiting promotion review**.

### professional
- **deliberation** - adr, prd, design-doc (draft), rfc (draft)
- **instruction** - readme, technical-reference, faq (draft), runbook (draft), how-to-guide (draft), user-manual (draft)
- **progress** - changelog-entry, daily-standup, meeting-notes, status-report, meeting-agenda (draft)
- **brief** - one-pager, project-brief (draft), pitch-deck (draft), proposal (draft), resume (draft), bio (draft)
- **appraisal** - postmortem (draft), retrospective (draft), performance-review (draft)
- **messaging** - email, slack-message, memo (draft)
- **outreach** - cold-outreach (draft), cover-letter (draft), recommendation-letter (draft)
- **response** - support-reply (draft), review-response (draft)

### public
- **broadcast** - blog-post-long-form, tweet-thread, press-release (draft), release-notes (draft), newsletter (draft), announcement (draft), listicle (draft), customer-story (draft)
- **copy** - landing-page (draft), ad-copy (draft), product-description (draft), testimonial (draft)
- **position** - whitepaper, op-ed (draft), manifesto (draft), open-letter (draft), editorial (draft)
- **accountability** - incident-report (draft), public-statement (draft)

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

## Awaiting your review: draft -> stable promotion

The 57 drafts are staged for a `draft -> stable` decision. The mechanics for promoting one:

1. Review the entry (and optionally re-run the Codex gate on it).
2. Set `review_status: stable` in its `ENTRY.md` (per the repo rule, only a maintainer does
   this; new entries start `draft`).
3. The moment it is `stable`, the Gate 2 *sample-count* check applies: it must render on all
   12 anchor topics (`tools/anchor_topics.py`). So promotion is gated on the next step.

You can promote in any grouping (by family, by confidence, a first tranche of the strongest,
etc.). There is no need to promote all 57 at once.

## Next (in dependency order)

1. **Promotion review** (yours): pick which drafts become stable.
2. **Render promoted formats across the 12 anchor topics** (agent, mechanical): for each
   promoted format, generate its 12 vertical-slice worked samples so it clears the Gate 2
   sample-count check. This is the same per-topic workflow used for the 720-sample matrix;
   it is free (subagents) and gated. Do this only for formats you actually promote.
3. **Update the marketplace manifests**: bump the curated counts in `library.json` /
   `plugin.json` to include the newly-stable formats (the manifest validator enforces
   plugin.json == library.json).
4. **Tag a release**: once the manifests reflect new stable content, cut the version bump +
   CHANGELOG roll-up + tag. Until promotion, there is nothing curated to release, so no tag.

## On paid CI / API (correction)

Earlier notes framed a "paid-CI generator-tier decision" as a pending lever. It is not. The
master plan fences the paid-API decision to three narrow triggers: a batch too large to
hand-drive, unattended contributor-PR admission, or pinned model/seed provenance for
*published* distinguishability scores. **None were hit.** All 60 breadth entries (batches
1-10) and the earlier 720-sample depth matrix were generated by free in-session subagents
and gated by the free cross-vendor Codex judge. The subagent factory was the whole point,
and it carried the entire run at zero marginal API cost. Paid CI remains fully fenced and is
not required for promotion, rendering, manifests, or release.

## Reproducing / continuing the generation loop

The per-batch loop (≈12-15 min each), if more breadth is ever wanted:

1. Edit `scratchpad/streamb.js` `CANDIDATES`: six pre-validated candidates, each with
   `id, name, domain, family, dp, one_liner, concept` (the concept embeds the
   neighbor contrast), `pairs_well_with, avoid_with, confusable_with, typical_voices,
   typical_tones`. Cross-ref ids must already exist; prose fields are DOUBLE-quoted JS
   strings (apostrophes break single-quoted JS).
2. `Workflow({scriptPath})` - six sonnet agents, each reads its neighbor's ENTRY.md and
   writes its own file.
3. `validate.py` + `build-indexes.py`; dispatch the Codex distinguishability gate; apply
   fixes as targeted edits.
4. `gen-site.mjs` + `cd site && npm run build`; bump the two README draft counters; commit
   (conventional, dash-free); PR; `gh pr checks --watch`; squash-merge; sync `main`.

**The breadth run is intentionally stopped** at 57 drafts: the remaining uncovered formats
are niche (examen, syllabus, abstract, grant-proposal, api-documentation, dedication,
benediction, podcast-script) or overlap existing entries, so further batches would trade
distinctiveness for raw count. Depth/promotion is the higher-value next lever.
