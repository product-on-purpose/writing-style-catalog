---
title: Stream-B Promotion Proposal - recommended draft-to-stable tranches
date: 2026-06-28
status: Wave 1 (v0.4.0) and Wave 2 (v0.5.0 release-prep) both promoted; Hold-20 deferred
author: agent (recommendation only; promotion is the maintainer's call)
related:
  - docs/internal/release-plans/stream-b-breadth-status.md (the inventory + gate record)
  - docs/internal/release-plans/promotion-and-release-runbook.md (the step-by-step to execute a wave)
  - _local/marketing-release (the PM/builder beachhead this proposal leans on)
---

# Stream-B Promotion Proposal

> **Status (2026-07-01): Wave 1 and Wave 2 are both promoted.** The 14 eng/PM-core formats shipped in
> **v0.4.0**. All 23 Wave 2 formats (10 professional + 13 public, 276 samples, date-gated) are now
> `stable`; release-prep for **v0.5.0** is next. **Hold-20** (personal, ceremonial, contemplative)
> stays deferred to a future audience-expansion release. The original recommendation is preserved
> below as the decision record.

57 draft format candidates were staged for a `draft -> stable` decision. They had each cleared
a per-entry distinguishability gate AND a whole-corpus de-dup audit, so quality and
distinctness were not the question. The remaining questions were strategic: **which formats earn
a permanent stable slot (sharpening the catalog rather than diluting it), and in what order**,
given that promoting one is not free - a stable entry must render on all 12 anchor topics to
clear the Gate 2 sample-count check.

This is a recommendation. Promotion is the maintainer's call; adjust any line freely. (Promotion
is now executed with `tools/promote.py`, the guarded flip - see Mechanics below.)

## The principle behind the recommendation

1. **Promote along the beachhead first.** The catalog's stated wedge is PMs and builders
   (church-tech / devotional content is explicitly out of beachhead scope). The professional
   and public formats are the coherent "work writing" expansion of the existing stable set
   (which is already PM/eng-centric: adr, prd, readme, one-pager, status-report, etc.).
   Promoting these sharpens the catalog's identity; promoting personal/ceremonial/contemplative
   formats now would broaden its advertised identity past the wedge before that is the goal.
2. **Phase by confidence and rendering cost.** Each promoted format costs ~12 anchor-topic
   renders. Two waves keep each release batch shippable and let the promotion+render pipeline
   prove out on a focused first set.
3. **Hold, do not discard.** The held formats are high quality. Holding them as drafts keeps
   them visible (marked "under review" on the site) and ready for a deliberate audience-expansion
   release later. Nothing is thrown away.

## Recommendation at a glance

| Bucket | Count | What | Status |
|---|---|---|---|
| **Wave 1 - the eng/PM core** | 14 | Decision docs, ops, product comms | **DONE - released as v0.4.0** |
| **Wave 2 - the rest of professional + public** | 23 | Marketing, correspondence-at-work, opinion | **DONE - releasing as v0.5.0** |
| **Hold** | 20 | personal + ceremonial + contemplative (off-beachhead; promote in a future audience-expansion release) | deferred |

## Wave 1 (14): the eng/PM core - DONE (v0.4.0)

The highest-frequency documents for the beachhead, extending the existing stable professional set.

| Format | Family | Why it earns a permanent slot |
|---|---|---|
| `design-doc` | deliberation | Specs an implementation once the decision to build is made. Core eng artifact. |
| `rfc` | deliberation | Proposes a change and invites disagreement before deciding. Core eng. |
| `postmortem` | appraisal | Blameless incident analysis to root cause. Ubiquitous in eng/ops. |
| `retrospective` | appraisal | Cadence-based team-process reflection. Core agile ritual. |
| `incident-report` | accountability | Public-facing technical-disruption account with timeline. Core ops. |
| `runbook` | instruction | Execute-under-pressure operational procedure. Core ops. |
| `how-to-guide` | instruction | Teaches a learner one task end to end (the Diataxis tutorial quadrant). Core docs. |
| `faq` | instruction | Anticipates and answers recurring questions once for everyone. Core docs/support. |
| `meeting-agenda` | progress | Pre-meeting plan: topics, time, intended outcomes. Universal at work. |
| `proposal` | brief | Pitches a piece of work or a deal for approval, with terms. Core PM/consulting. |
| `project-brief` | brief | Aligns a team at kickoff (goal/scope/constraints/success). Core PM. |
| `pitch-deck` | brief | Persuasive slide narrative to win a decision. Core PM/startup. |
| `announcement` | broadcast | Direct product/company news to the affected audience. Core product comms. |
| `release-notes` | broadcast | Version-anchored, changelog-curated user-facing notes. Core product. |

Rendering cost: 14 x 12 = ~168 anchor-topic samples (a few free workflow runs; the agent does it).

## Wave 2 (23): the rest of professional + public - DONE (v0.5.0)

Grouped by family; all beachhead-relevant, slightly broader or lower-frequency than Wave 1.

- **instruction**: `user-manual`
- **brief**: `resume`, `bio`
- **appraisal**: `performance-review`
- **messaging**: `memo`
- **outreach**: `cold-outreach`, `cover-letter`, `recommendation-letter`
- **response**: `support-reply`, `review-response`
- **broadcast**: `press-release`, `newsletter`, `listicle`, `customer-story`
- **copy**: `landing-page`, `ad-copy`, `product-description`, `testimonial`
- **position**: `op-ed`, `editorial`, `manifesto`, `open-letter`
- **accountability**: `public-statement`

Rendering cost: 23 x 12 = ~276 samples.

## Hold (20): off-beachhead, promote in a later audience-expansion release

High quality, but they serve audiences beyond the PM/builder wedge (and the contemplative cluster
is explicitly off-beachhead per the marketing plan). Keep as drafts.

- **personal/correspondence**: `thank-you-note`, `apology`, `condolence-note`, `invitation`, `love-letter`
- **personal/essay**: `personal-essay`, `personal-statement`, `memoir-excerpt`
- **ceremonial/tribute**: `eulogy`, `toast`, `obituary`, `wedding-vows`, `acceptance-speech`, `commencement-speech`
- **contemplative/devotion**: `prayer`, `sermon`, `blessing`, `guided-meditation`
- **contemplative/journal**: `journal-entry`, `gratitude-journal`

**Reconsider-early candidates within Hold:** if you want some general-writing coverage in the
stable catalog now, the universally-needed members are `thank-you-note`, `apology`, and
`journal-entry` (and `personal-statement` for the applications use case). These are the strongest
case for jumping the queue.

## Per-format flags (from the de-dup audit)

- `op-ed` + `editorial` are now distinct (post-audit: op-ed = named author's personal stake,
  editorial = collective institutional judgment). Promote both, or just `op-ed` if you want a
  single opinion format - it is the more universally needed of the two.
- `user-manual` is now clearly separated from the stable `technical-reference` (organized by
  feature/task vs by function/endpoint/field). Safe to promote.
- `design-doc` + `rfc` are distinct on decision-state (rfc = decision not yet made; design-doc =
  decision made, specs the build). Promote both.
- Several Wave-1 formats have a Wave-2 confusable neighbor (e.g. `announcement` <-> `press-release`,
  `incident-report` <-> `public-statement`). Promoting the neighbor a wave later is fine - the
  cross-reference resolves either way - but promoting each confusable pair together reads cleaner.

## Mechanics + sequence (per wave)

Render FIRST (while draft, Gate-2-exempt), THEN flip - that order is the whole reason `validate.py`
stays green throughout, and `tools/promote.py` enforces it (it refuses to flip an unrendered entry).
The full step-by-step is the [promotion-and-release runbook](promotion-and-release-runbook.md); in
brief:

1. Maintainer approves the wave (and any line edits).
2. Render each across the 12 anchor topics while still draft: edit `FORMATS` in
   `tools/agentic/promote.js`, run it with the Workflow tool, then `python tools/validate.py`
   (green - drafts are exempt).
3. Date-gate the dated formats (one `general-purpose` agent per format vs the real calendar; ~30%
   of dated samples slip), and apply any fixes with `tools/agentic/remediate.js`.
4. Flip: `python tools/promote.py <ids>` (transactional, guarded - sets `review_status: stable`
   only when all 12 samples exist).
5. `python tools/build-indexes.py`; bump the README counters (x4) and the curated counts in
   `library.json` / `plugin.json` (the manifest validator enforces parity); re-run `validate.py`
   (Gate 2 now active for the wave), `validate-plugin-manifest.mjs`, and the site build.
6. Cut the release: version bump + CHANGELOG roll-up + tag (`release.yml` publishes the GitHub
   Release on the tag push).

**Wave 2 is complete.** Counter deltas realized: stable 74 -> 97, Format stable 29 -> 52, vertical
samples 888 -> 1164, total worked examples 917 -> 1193, drafts 43 -> 20 (exactly the Hold-20).
Recommended next action: cut the **v0.5.0** release per the runbook (version bump + CHANGELOG
roll-up + tag). After that, **Hold-20** is a deliberate later audience-expansion decision, not a
default next step.
