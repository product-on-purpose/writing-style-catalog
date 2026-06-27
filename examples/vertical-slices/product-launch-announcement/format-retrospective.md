---
entry_id: retrospective
axis: format
topic_slug: product-launch-announcement
topic_label: Announcing a new product to an outside audience
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# Retrospective: Launch Sprint - Tidemark

## Date

July 7, 2026

## What Went Well

- **Early-access cohort produced clean pre-launch signal.** Twenty-two small teams ran the full feedback-to-roadmap loop before June 30 without filing a support request. The intake question asking each team to describe their current workflow surfaced the scatter pattern (spreadsheets, chat threads, ticket trackers) as the dominant pain point, confirming the framing we chose for the announcement.
- **Problem-led announcement framing held across channels without contradiction.** Press contacts who responded used our framing language back to us in their notes. No one tried to slot Tidemark into a roadmap-tool or feedback-tool category exclusively, which was the outcome we were trying to protect against.
- **Launch assets were ready several days before June 30.** Screenshots, the 90-second demo video, and the one-page product summary were in hand early enough for press contacts and community builders to prepare their own coverage before launch day.
- **Pricing was live before the landing page launched.** Prospective users could evaluate cost before committing to a signup, and no one landed on a "contact us for pricing" dead end. The free solo plan, $29/month team plan, and custom tier were all visible from day one.
- **Help documentation deployed as a single step on launch day.** Staging it in advance meant the team did not scramble to publish support articles after the product was already live.

## What Did Not Go Well

- **The sharing ask in the cohort offboarding email was buried.** The email led with account-transition logistics before reaching the request for cohort members to share their experience publicly. Several who did share said they almost skipped past it. The ask itself was clear; its placement was not.
- **The team had no agreed definition of a "quiet launch week."** When organic sharing moved slower than expected in the first 48 hours, the team spent time in a holding pattern. There were no documented criteria for what a quiet signal meant and what, if anything, to do about it at the 24-hour or 48-hour mark.
- **The free-plan infrastructure risk had no named owner before launch.** The usage threshold that would trigger a pricing review was documented in the status report, but who would pull and read the dashboard daily was not established. The monitoring setup existed; the accountability did not.

## What Will We Change

- [ ] Rewrite the cohort offboarding email so the sharing ask appears in the opening paragraph, ahead of account-transition logistics. - Owner: Marisol - By: August 1, 2026 (before next cohort offboards)
- [ ] Before the next launch, write a one-page "quiet launch" protocol that defines what we will do at 24, 48, and 72 hours regardless of reach signals. Treat silence as a state with a defined response. - Owner: Marisol - By: July 21, 2026
- [ ] Assign a named dashboard owner to any future free-tier experiment before the experiment begins, not after. Add this as a checklist item to the launch-readiness template. - Owner: engineering lead (confirm in July 14 team sync) - By: July 14, 2026

## Notes

The July 7 cohort feedback session revealed that several teams re-ranked items manually after receiving the automated ranking output. This may indicate the scoring logic needs either an explicit explanation of how weights are calculated or a user-facing weighting control. This finding does not belong in the launch retrospective's change column - it is scoped and ready for first patch release planning.
