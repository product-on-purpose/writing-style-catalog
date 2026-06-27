---
title: Stream-B Promotion Proposal - recommended draft-to-stable tranches
date: 2026-06-27
status: proposal - awaiting maintainer decision
author: agent (recommendation only; promotion is the maintainer's call)
related:
  - docs/internal/release-plans/stream-b-breadth-status.md (the inventory + gate record)
  - _local/marketing-release (the PM/builder beachhead this proposal leans on)
---

# Stream-B Promotion Proposal

57 draft format candidates are staged for a `draft -> stable` decision. They have each cleared
a per-entry distinguishability gate AND a whole-corpus de-dup audit, so quality and
distinctness are not the question. The remaining questions are strategic: **which formats earn
a permanent stable slot (sharpening the catalog rather than diluting it), and in what order**,
given that promoting one is not free - a stable entry must render on all 12 anchor topics to
clear the Gate 2 sample-count check.

This is a recommendation. Promotion (setting `review_status: stable`) is the maintainer's call;
adjust any line freely.

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

| Bucket | Count | What |
|---|---|---|
| **Wave 1 - promote now** | 14 | The eng/PM core: decision docs, ops, product comms |
| **Wave 2 - promote next** | 23 | The rest of professional + public (marketing, correspondence-at-work, opinion) |
| **Hold** | 20 | personal + ceremonial + contemplative (off-beachhead; promote in a future audience-expansion release) |

## Wave 1 - promote now (14): the eng/PM core

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

## Wave 2 - promote next (23): the rest of professional + public

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

1. Maintainer approves the wave (and any line edits).
2. Agent sets `review_status: stable` on the approved entries.
3. Agent renders each across the 12 anchor topics (the free per-topic vertical-slice workflow),
   so they clear the Gate 2 sample-count check. `validate.py` will fail for a stable entry that
   is not yet rendered, so promotion + render ship together.
4. Agent bumps the curated counts in `library.json` / `plugin.json` to include the newly-stable
   formats (the manifest validator enforces parity).
5. Cut the release: version bump + CHANGELOG roll-up + tag.

Recommended first action: approve (or edit) **Wave 1**, and the agent will promote + render +
manifest it as one release-ready batch.
