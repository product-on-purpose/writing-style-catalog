# GATE 1 review ledger

> The audit trail for the v1.0 `review_status` review (GATE 1). Packets are
> generated working artifacts under gitignored `_local/review-packets/`; this
> file is the tracked record of what was actually decided and why.
>
> Regenerate packets with `python tools/review_packet.py`.

**Rule:** an entry may only be `stable` after a maintainer has read it. Until then it carries `machine-verified`: it passes every enforced check and has not been read (ADR 0021). Promote a read entry with `python tools/promote.py --reviewed <id>` and record the decision here; `draft` is always the honest fallback for one that should not ship. Entries are never relabelled upward to make a gate go green: if a reading is required before a milestone and cannot be finished, the milestone slips.

**Scope:** 97 entries awaiting a maintainer reading (`review_status: machine-verified`). 3 carry at least one flag.

## Decisions

| Entry | Axis | Flags | Decision | Date | Notes |
|---|---|---|---|---|---|
| `ad-copy` | format | - | | | |
| `adr` | format | - | | | |
| `announcement` | format | - | | | |
| `bio` | format | - | | | |
| `blog-post-long-form` | format | - | | | |
| `candid` | tone | - | | | |
| `caregiver` | voice | - | | | |
| `celebratory` | tone | - | | | |
| `changelog-entry` | format | - | | | |
| `chronological-narrative` | style | - | | | |
| `classical-argument` | style | - | | | |
| `coach` | voice | - | | | |
| `cold-outreach` | format | - | | | |
| `columnist` | voice | - | | | |
| `comparison-contrast` | style | - | | | |
| `confessional` | tone | - | | | |
| `confident` | tone | - | | | |
| `cover-letter` | format | 1 | | | |
| `customer-story` | format | - | | | |
| `daily-standup` | format | - | | | |
| `decision-log` | style | - | | | |
| `definitional` | style | - | | | |
| `design-doc` | format | - | | | |
| `devotional-entry` | format | - | | | |
| `devotional-reflection` | style | - | | | |
| `dialectic` | style | - | | | |
| `diataxis-explanation` | style | - | | | |
| `diplomatic` | tone | - | | | |
| `direct-communicator` | voice | - | | | |
| `editorial` | format | 1 | | | |
| `email` | format | - | | | |
| `empathetic` | tone | - | | | |
| `encouraging` | tone | - | | | |
| `executive` | voice | - | | | |
| `executive-summary` | style | - | | | |
| `faq` | format | - | | | |
| `friendly-mentor` | voice | - | | | |
| `how-to-guide` | format | - | | | |
| `incident-report` | format | - | | | |
| `instructional` | tone | - | | | |
| `journalist` | voice | - | | | |
| `landing-page` | format | - | | | |
| `layered-disclosure` | style | - | | | |
| `listicle` | format | - | | | |
| `manifesto` | format | - | | | |
| `matter-of-fact` | tone | - | | | |
| `meeting-agenda` | format | - | | | |
| `meeting-notes` | format | - | | | |
| `memo` | format | - | | | |
| `narrative-case-study` | style | - | | | |
| `newsletter` | format | - | | | |
| `one-pager` | format | - | | | |
| `op-ed` | format | 1 | | | |
| `open-letter` | format | - | | | |
| `operator` | voice | - | | | |
| `pastoral` | voice | - | | | |
| `performance-review` | format | - | | | |
| `pitch-deck` | format | - | | | |
| `playful` | tone | - | | | |
| `postmortem` | format | - | | | |
| `pragmatic-architect` | voice | - | | | |
| `prd` | format | - | | | |
| `press-release` | format | - | | | |
| `problem-solution` | style | - | | | |
| `procedural` | style | - | | | |
| `product-description` | format | - | | | |
| `product-thinker` | voice | - | | | |
| `project-brief` | format | - | | | |
| `proposal` | format | - | | | |
| `public-statement` | format | - | | | |
| `question-and-answer` | style | - | | | |
| `readme` | format | - | | | |
| `recommendation-letter` | format | - | | | |
| `release-notes` | format | - | | | |
| `researcher` | voice | - | | | |
| `resolute` | tone | - | | | |
| `resume` | format | - | | | |
| `retrospective` | format | - | | | |
| `reverent` | tone | - | | | |
| `review-response` | format | - | | | |
| `rfc` | format | - | | | |
| `runbook` | format | - | | | |
| `senior-consultant` | voice | - | | | |
| `skeptical` | tone | - | | | |
| `slack-message` | format | - | | | |
| `socratic-inquiry` | style | - | | | |
| `status-report` | format | - | | | |
| `storyteller` | voice | - | | | |
| `support-reply` | format | - | | | |
| `technical-reference` | format | - | | | |
| `technical-writer` | voice | - | | | |
| `testimonial` | format | - | | | |
| `tweet-thread` | format | - | | | |
| `urgent` | tone | - | | | |
| `user-manual` | format | - | | | |
| `warm` | tone | - | | | |
| `whitepaper` | format | - | | | |
