---
id: press-release
name: Press Release
axis: format
domain: public
family: broadcast
one_liner: 'A formal external announcement in news style: dateline, headline, a strong lead, a quote, and boilerplate.'
description: |
  The press release is a standardized broadcast format built to travel - from source to journalist
  to audience without editorial rewriting. Its discipline is the inverted pyramid: every piece of
  information is ranked by newsworthiness, with the most significant facts in the opening sentence.
  A reader who stops after the lead knows who, what, when, where, and why. A reader who finishes
  has the full story, an attributable quote, and the institutional context to file or publish
  without a follow-up call.

  The format's constraints are not arbitrary. The dateline fixes the announcement in time and
  geography. The headline frames the news angle in active voice. The mandatory quote provides a
  spokesperson voice without requiring the recipient to interview anyone. The boilerplate "About"
  paragraph belongs at the end precisely because it matters least to the story. The three-hash
  closing marker (###) signals to an editor that nothing follows - a convention that dates to
  wire-service teletype and survives because it is still useful.

  Releases travel through layers of reception - PR wire, editorial inbox, news desk - and each
  layer applies additional compression. The format's formality is a signal that the content has
  been legally cleared, approved, and is safe to quote as issued. That institutional signal is as
  important as the content itself. A release that reads like ad copy tells editors that the sender
  does not understand the convention and cannot supply accurate, quotable text.

  Typical length: 300-500 words.
canonical_template: |
  FOR IMMEDIATE RELEASE
  [OR: EMBARGOED UNTIL [DATE/TIME]]

  [HEADLINE: News-style subject-verb-object; present tense; 10 words or fewer]

  [SUBHEAD: One-line amplifier of the headline - optional]

  CITY, Month DD, YYYY - [Lead paragraph: the full story in 2-3 sentences. Who did what, when,
  where, and why it matters. News first - no setup.]

  [Body paragraph 2: Most important supporting detail.]

  [Body paragraph 3: Secondary context, additional element, or background.]

  "[Attributable quote in spokesperson voice - adds interpretation or enthusiasm that straight
  news prose cannot carry.]" said [Full Name], [Title], [Organization].

  [Optional second quote from a partner, customer, or analyst.]

  [Closing paragraph: Forward-looking statement, availability, call to action, or next milestone.]

  About [Organization]
  [Boilerplate: 2-4 sentences describing the organization for readers encountering it for
  the first time.]

  ###

  Media Contact:
  [Name]
  [Title]
  [Email]
  [Phone]
typical_voices:
  - journalist
  - executive
typical_tones:
  - confident
  - matter-of-fact
digital_or_print: both
pairs_well_with:
  - journalist
  - executive
  - confident
  - matter-of-fact
avoid_with:
  - confessional
  - playful
  - devotional-reflection
  - pastoral
confusable_with:
  - blog-post-long-form
  - whitepaper
when_to_use:
  - Announcing a product launch, company milestone, partnership, or significant hire to external media
  - Distributing news via a wire service or media list for republication
  - Creating a citable, on-the-record artifact that journalists or analysts can quote directly
  - Anchoring a coordinated media campaign with a single authoritative source document
  - Building a historical archive of public announcements in a company newsroom or press room
when_not_to_use:
  - Internal communications, team updates, or all-hands announcements that have no external news angle
  - Thought leadership, opinion, or educational content better served by a blog post or whitepaper
  - Crisis communications requiring a conversational, empathetic tone rather than a formal news format
tells:
  - 'FOR IMMEDIATE RELEASE (or EMBARGOED UNTIL) header at the top of the document'
  - 'Dateline in ALL-CAPS CITY format followed by the date and a dash preceding the lead paragraph'
  - 'Lead paragraph answers who, what, when, where, and why in the first 2-3 sentences with no setup'
  - 'At least one attributed quote from a named executive or spokesperson'
  - 'Boilerplate "About [Organization]" section positioned at the close before contact information'
  - 'Three-hash closing marker (###) signaling the end of copy'
  - 'Media contact block with name, title, email, and phone for press inquiries'
anti_patterns:
  - pattern: 'Burying the news by opening with company background, mission, or product history before stating what happened'
    why: 'The lead exists to deliver the news immediately; editors who cannot find the news angle in the first paragraph discard the release without reading further.'
  - pattern: 'Loading the copy with superlatives and promotional language such as "innovative," "revolutionary," or "best-in-class"'
    why: 'Journalists strip or rewrite promotional copy; a release full of adjective-heavy claims signals that the sender does not understand news conventions and cannot produce quotable material.'
  - pattern: 'Including a quote that was written entirely by the communications team with no meaningful input from the attributed executive'
    why: 'The quote is the only place in the format where a subjective voice is expected; generic or fabricated quotes are editorially useless, create legal risk, and editors may call to verify.'
  - pattern: 'Using the format for a product deep-dive, opinion piece, or internal update that has no external, time-bound news angle'
    why: 'That collapses the distinction between this format and the confusable blog-post-long-form or whitepaper; a press release without a hard news hook is a misapplication of the broadcast format.'
failure_modes:
  - mode: 'Over-formalizes - the release becomes so stiff and institutional that human voice disappears; every sentence is passive, the quote reads like committee output, and no reader would believe a real person said it'
    mitigation: 'The press release is formal but it is still news, not a legal filing. The lead should be active voice. Read the lead and the quote aloud; if they fail the "would a radio anchor read this?" test, rewrite for directness.'
  - mode: 'Over-announces - treats every clause as equally important, loads every paragraph with claims, and loses the inverted pyramid discipline so the editor cannot tell what the story is'
    mitigation: 'Rank every paragraph by the question "what happens if this is cut?" If nothing important is lost, cut it or move it to boilerplate. The first paragraph must stand alone as the complete story.'
llm_instruction_phrasing: |
  Write as a press release in standard news format. Structure the document as follows: open with
  FOR IMMEDIATE RELEASE, then a dateline (CITY, Month DD, YYYY), then a headline in active voice
  that states the news in 10 words or fewer. Write a lead paragraph that answers who, what, when,
  where, and why in 2-3 sentences with no setup - news first. Follow with body paragraphs in
  inverted pyramid order, most newsworthy first. Include at least one attributed quote from a
  named spokesperson that adds interpretation or enthusiasm in a human voice; the quote should not
  simply restate what the body already says. Close with a boilerplate "About [Organization]"
  paragraph, a three-hash marker (###), and a media contact block. Use active voice throughout.
  Do not use superlatives, promotional adjectives, or language that a journalist would have to
  strip before publication.
tags:
  - press-release
  - public-relations
  - news
  - broadcast
  - media
  - announcement
review_status: stable
---

## Press Release

The press release is a standardized broadcast format built to travel - from source to journalist to audience without editorial rewriting. Its discipline is the inverted pyramid: every piece of information is ranked by newsworthiness, with the most significant facts in the opening sentence. A reader who stops after the lead knows who, what, when, where, and why. A reader who finishes has the full story, an attributable quote, and the institutional context to file or publish without a follow-up call.

The format's constraints are not arbitrary. The dateline fixes the announcement in time and geography. The headline frames the news angle in active voice. The mandatory quote provides a spokesperson voice without requiring the recipient to interview anyone. The boilerplate "About" paragraph belongs at the end precisely because it matters least to the story. The three-hash closing marker (###) signals to an editor that nothing follows - a convention that dates to wire-service teletype and survives because it is still useful.

Releases travel through layers of reception - PR wire, editorial inbox, news desk - and each layer applies additional compression. The format's formality is a signal that the content has been legally cleared, approved, and is safe to quote as issued. That institutional signal is as important as the content itself. A release that reads like ad copy tells editors that the sender does not understand the convention and cannot supply accurate, quotable text.

### Canonical template

```
FOR IMMEDIATE RELEASE
[OR: EMBARGOED UNTIL [DATE/TIME]]

[HEADLINE: News-style subject-verb-object; present tense; 10 words or fewer]

[SUBHEAD: One-line amplifier of the headline - optional]

CITY, Month DD, YYYY - [Lead paragraph: the full story in 2-3 sentences. Who did what,
when, where, and why it matters. News first - no setup.]

[Body paragraph 2: Most important supporting detail.]

[Body paragraph 3: Secondary context, additional element, or background.]

"[Attributable quote in spokesperson voice - adds interpretation or enthusiasm that
straight news prose cannot carry.]" said [Full Name], [Title], [Organization].

[Optional second quote from a partner, customer, or analyst.]

[Closing paragraph: Forward-looking statement, availability, call to action, or next milestone.]

About [Organization]
[Boilerplate: 2-4 sentences describing the organization for readers encountering it
for the first time.]

###

Media Contact:
[Name]
[Title]
[Email]
[Phone]
```

### When to use

Announcing a product launch, company milestone, partnership, or significant hire to external media. Distributing news via a wire service or media list for republication. Creating a citable, on-the-record artifact that journalists or analysts can quote directly. Anchoring a coordinated media campaign with a single authoritative source document. Building a historical archive of public announcements in a company newsroom or press room.

### When not to use

Internal communications, team updates, or all-hands announcements that have no external news angle. Thought leadership, opinion, or educational content better served by a blog post or whitepaper. Crisis communications requiring a conversational, empathetic tone rather than a formal news format.

### Pairs well with

`journalist`, `executive`, `confident`, `matter-of-fact`

### Often confused with

**blog-post-long-form**: A blog post develops a perspective, argument, or narrative over multiple sections and invites the reader into a sustained piece of thinking. A press release reports a time-bound event and expects the reader to stop at any paragraph without losing the story; it is not an essay and does not develop ideas across sections.

**whitepaper**: A whitepaper makes a sustained argument backed by data, research, or technical detail, typically to educate or persuade a sophisticated audience over many pages. A press release announces a single event to media for republication; it does not develop an argument or ask the reader to work through evidence.
