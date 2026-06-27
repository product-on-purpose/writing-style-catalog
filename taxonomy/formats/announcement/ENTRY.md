---
id: announcement
name: Announcement
axis: format
domain: public
family: broadcast
one_liner: A direct message telling an audience about something new or changing, in the organization's own voice.
description: |
  An announcement is a direct message that tells an audience - customers, users, a community, or a
  company - about something new or changing: a launch, a milestone, a policy, a change of plans.
  It leads with the news, explains what the change means for the reader, and closes with a clear
  next step. The audience is the end reader, not a journalist who will reshape the message before
  passing it on.

  That directness is what gives the announcement its character. The tone is the organization's own
  voice: human, clear, and addressed to people who have a stake in the news. There is no dateline
  to fix the document in a news-wire geography, no boilerplate to orient a reporter to the
  company's history, and no attributed quote supplied for a journalist to lift. The writer speaks
  directly to the people who will act on the news.

  The format's essential structure is simple: state the news, explain what it means, and point to
  what comes next. That directness is not simplicity - it is discipline. A well-written
  announcement respects that the reader already knows the organization and wants the substance
  quickly, without the setup and ceremony of formats designed to survive in a newsroom.

  Typical length: 150-400 words.
canonical_template: |
  [Subject line / headline: what happened, in plain language]

  [Opening paragraph: the news, stated directly. What changed, launched, ended, or started.]

  [Body paragraph: what this means for the reader. Specific impact, benefits, or consequences.]

  [Supporting paragraph (optional): relevant context, timeline, availability, or background detail.]

  [Closing: next step for the reader - what they should do, where to go, or when more is coming.]
typical_voices:
  - executive
  - product-thinker
typical_tones:
  - confident
  - candid
digital_or_print: both
pairs_well_with:
  - executive
  - product-thinker
  - confident
  - candid
  - executive-summary
avoid_with:
  - confessional
  - reverent
  - skeptical
confusable_with:
  - press-release
  - release-notes
when_to_use:
  - Announcing a product launch, new feature, or availability change directly to customers or users
  - Communicating a policy update, pricing change, or operational change to the affected audience
  - Marking a company milestone - funding, partnership, or team news - addressed to the community
  - Notifying users or customers of a change that requires their attention or action
  - Delivering internal company news directly to employees when a direct, news-first format is appropriate
when_not_to_use:
  - When the goal is media coverage and a journalist needs to repackage the news - use a press release instead
  - When the content requires extended argument, evidence, or development - use a blog post or whitepaper
  - When the communication is exploratory, informal, or conversational rather than news-bearing
tells:
  - 'Leads with the news in the first sentence, with no preamble, scene-setting, or organizational background'
  - 'Written in the organization''s own voice, addressed directly to the reader - "you/your" phrasing is common'
  - 'No dateline, no media contact block, no boilerplate "About" section'
  - 'Closes with a concrete next step or call to action for the reader'
  - 'Minimal length: no more than what is needed to state the news and explain its impact'
  - 'Single, clear subject: one thing announced per document, not a digest or roundup'
anti_patterns:
  - pattern: 'Burying the news behind organizational context, mission statements, or founder story before stating what happened'
    why: 'The reader opened the announcement to learn what changed; delay signals that the writer is not confident the news stands on its own.'
  - pattern: 'Applying press-release conventions - dateline, attributed executive quotes, media contact block, boilerplate "About" section - when writing directly to an audience rather than journalists'
    why: 'A press release is a formal, journalist-addressed format built for newsroom intermediaries; its structural signals tell a reporter the content is cleared and ready to republish, which is not what a direct audience needs to receive.'
  - pattern: 'Ending without a next step or call to action'
    why: 'An announcement exists to move the reader toward a link, a date, a decision, or an action; without a closing direction, the reader is left uncertain what to do with the information.'
  - pattern: 'Announcing multiple unrelated items in a single document'
    why: 'An announcement has one subject; combining a product launch with a policy change and a team update diffuses the news and forces the reader to hold too many things at once.'
failure_modes:
  - mode: 'Over-hypes: the announcement tips from direct news into promotional copy, loading every paragraph with superlatives, "we''re thrilled," and "game-changing" language until the news itself is obscured by performed enthusiasm'
    mitigation: 'Check every evaluative adjective; if removing it loses no factual content, remove it. The announcement earns trust by stating the news plainly, not by performing excitement about it.'
  - mode: 'Over-explains: the announcement pads the news with so much context, history, and background that the directness the format is built for disappears, and the reader has to work to find the actual news'
    mitigation: 'Locate the sentence where the news first appears; if it is not the opening sentence, cut or move everything before it. The reader needs to understand what the change means for them, not the story of how it came to be.'
llm_instruction_phrasing: |
  Write as a direct announcement addressed to the affected audience in the organization's own
  voice. Do not use press-release conventions: no dateline, no attributed quotes for a journalist
  to lift, no boilerplate "About" section, no media contact block. Open with the news in the
  first sentence - no preamble, no mission statement, no background before the fact. Follow with
  what the change means for the reader specifically. Add supporting detail only if it is necessary
  to understand the news or act on it. Close with a clear next step: a link, a date, a decision,
  or an action. Keep the length to what the news requires - 150 to 400 words is typical. State
  the news plainly; do not inflate it with superlatives, "excited to announce," or promotional
  adjectives that a reader would have to discount.
tags:
  - announcement
  - broadcast
  - public-communications
  - product-launch
  - change-communication
review_status: draft
---

## Announcement

An announcement is a direct message that tells an audience - customers, users, a community, or a company - about something new or changing: a launch, a milestone, a policy, a change of plans. It leads with the news, explains what the change means for the reader, and closes with a clear next step. The audience is the end reader, not a journalist who will reshape the message before passing it on.

That directness is what gives the announcement its character. The tone is the organization's own voice: human, clear, and addressed to people who have a stake in the news. There is no dateline to fix the document in a news-wire geography, no boilerplate to orient a reporter to the company's history, and no attributed quote supplied for a journalist to lift. The writer speaks directly to the people who will act on the news.

The format's essential structure is simple: state the news, explain what it means, and point to what comes next. That directness is not simplicity - it is discipline. A well-written announcement respects that the reader already knows the organization and wants the substance quickly, without the setup and ceremony of formats designed to survive in a newsroom.

### Canonical template

```
[Subject line / headline: what happened, in plain language]

[Opening paragraph: the news, stated directly. What changed, launched, ended, or started.]

[Body paragraph: what this means for the reader. Specific impact, benefits, or consequences.]

[Supporting paragraph (optional): relevant context, timeline, availability, or background detail.]

[Closing: next step for the reader - what they should do, where to go, or when more is coming.]
```

### When to use

Announcing a product launch, new feature, or availability change directly to customers or users. Communicating a policy update, pricing change, or operational change to the affected audience. Marking a company milestone - funding, partnership, or team news - addressed to the community. Notifying users or customers of a change that requires their attention or action. Delivering internal company news directly to employees when a direct, news-first format is appropriate.

### When not to use

When the goal is media coverage and a journalist needs to repackage the news - use a press release instead. When the content requires extended argument, evidence, or development - use a blog post or whitepaper. When the communication is exploratory, informal, or conversational rather than news-bearing.

### Pairs well with

`executive`, `product-thinker`, `confident`, `candid`, `executive-summary`

### Often confused with

**press-release**: A press release is a formal external announcement in news style - with a dateline, headline, attributed spokesperson quotes, a boilerplate "About" section, and a media contact block - built for journalists to republish without needing to interview anyone. It travels through layers of reception (PR wire, editorial inbox, news desk), and its formality signals that the content is legally cleared and safe to quote as issued. An announcement addresses the affected audience directly, in the organization's own voice, with no intermediary to persuade; it carries none of the structural signals a newsroom needs, because no newsroom is in the chain.

**release-notes**: An announcement is a single-subject news message in the organization's own voice - it states a piece of news, explains what it means for the reader, and closes with a next step. Release notes are version-anchored, multi-item, and curated from a changelog into scannable grouped sections (New, Improved, Fixed) under a version identifier. Use an announcement when a single piece of news warrants a direct message to the audience; use release notes when a versioned software release has multiple changes to communicate.
