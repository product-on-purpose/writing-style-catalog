---
id: toast
name: Toast
axis: format
domain: ceremonial
family: tribute
one_liner: A short, warm tribute delivered aloud to celebrate a living person or a happy occasion.
description: |
  A toast is a brief spoken tribute that celebrates a person or occasion, usually ending with raised
  glasses. Unlike a prepared lecture or a memoir, the toast is built for the room: it speaks to
  everyone present but carries meaning because it draws on something specific about the person being
  honored. That specificity - one story, one quality, one moment - is what lifts a toast above
  generic well-wishing.

  The format has two acts. The first act sets the table: it names the person or occasion, orients
  the room, and introduces the story or quality that will anchor the tribute. The second act
  delivers the payoff: it lands on why this person or this moment matters, then closes with a
  clear, spoken invitation to raise a glass. The invitation is not optional - it is the structural
  signal that transforms a monologue into a shared ritual.

  A toast should feel warm and present, not eulogy-dark or speech-formal. Humor is welcome when it
  is gentle and specific, not aimed at embarrassing the subject. The test for any detail included
  is whether it makes the subject feel seen and celebrated - not whether it makes the speaker look
  witty. Typical length is 150-300 words; longer risks losing the room before the glasses go up.

canonical_template: |
  # Toast: [Person or Occasion]

  ## Opening
  [Name the person or occasion. Orient the room briefly - who you are and your relationship to
  the subject.]

  ## The Story or Quality
  [One specific anecdote, memory, or quality that captures why this person or occasion matters.
  Be particular: a named moment, a real detail, not a generic virtue.]

  ## The Landing
  [Connect the story back to the celebration. Say what you wish for them, or what this moment
  means.]

  ## The Invite
  [The closing line that invites the room to raise a glass. "Please join me in raising a glass
  to [Name]." or equivalent.]
typical_voices:
  - storyteller
  - friendly-mentor
typical_tones:
  - celebratory
  - warm
digital_or_print: both
pairs_well_with:
  - storyteller
  - friendly-mentor
  - celebratory
  - warm
  - playful
  - narrative-case-study
avoid_with:
  - skeptical
  - matter-of-fact
  - urgent
confusable_with:
  - eulogy
when_to_use:
  - Wedding receptions, rehearsal dinners, or engagement parties
  - Retirement celebrations and farewell gatherings for living honorees
  - Award dinners and milestone birthday or anniversary events
  - Any gathering where a specific person or shared achievement deserves public recognition
  - Team celebrations where one person's contribution needs to be named aloud
when_not_to_use:
  - Memorial services or funerals, where a eulogy is the appropriate form
  - Formal presentations where the audience expects structured argument or evidence
  - Settings where raising a glass would be inappropriate or logistically impossible
tells:
  - 'Warm, specific anecdote or named quality anchors the body of the tribute'
  - 'Direct address to the person being honored by name early in the piece'
  - 'Short structure: opening, story, landing, invite - usually under 300 words'
  - 'A closing line that explicitly invites the room to raise a glass'
  - 'Humor is gentle and celebratory, aimed at affection rather than exposure'
  - 'The speaker addresses both the subject and the assembled guests as a shared audience'
anti_patterns:
  - pattern: 'Turning the toast into a roast by landing on the subject''s embarrassments or flaws rather than celebrating them'
    why: 'A toast''s contract with the room is celebration; humor that makes the subject wince breaks that contract and leaves the raised glass feeling hollow.'
  - pattern: 'Filling the body with generic virtues without a single specific story or named moment'
    why: 'Generic praise signals the speaker does not know the subject well; specificity is what makes a toast feel like it could only have been given by this person about this person.'
  - pattern: 'Running long - treating the toast as an open slot for a full speech rather than a short tribute'
    why: 'The room is waiting to raise a glass; a toast that keeps them seated past its natural end loses the goodwill earned in the opening.'
  - pattern: 'Delivering a tone of mourning, retrospective loss, or grief rather than celebration'
    why: 'That is the register of a eulogy, which honors someone who has died and permits grief as its emotional center; a toast honors the living and must land on joy, not sorrow.'
failure_modes:
  - mode: 'The warmth over-hits and tips into sentimentality - every detail becomes weepy, humor disappears, and the room loses the lightness that lets a celebration feel shared'
    mitigation: 'Keep at least one specific, lightly humorous beat; if every paragraph brings the speaker close to tears, trim until the warmth reads as affection rather than grief.'
  - mode: 'The celebration over-hits and tips into a variety-show monologue - the speaker keeps adding stories and callbacks until the tribute becomes a performance about the speaker''s own wit rather than the subject'
    mitigation: 'Test every element against the subject: if removing a joke or detail would leave the toast clearer or warmer, cut it.'
llm_instruction_phrasing: |
  Write as a Toast. The format is short and warm - typically 150-300 words - and is built for
  spoken delivery to a room of people who love or respect the person being honored. Structure it
  in four moves: open by naming the person or occasion and your relationship to them; bring one
  specific story or quality that captures why this person or moment matters (be particular - a
  real detail, not a generic virtue); land on what you wish for them or what this celebration
  means; close with a clear invitation to raise a glass. Keep humor gentle and aimed at
  celebrating, not embarrassing. Do not run long - the room is waiting to drink together, and a
  short toast that lands cleanly outperforms a long one every time.
tags:
  - ceremonial
  - spoken
  - tribute
  - celebration
  - wedding
  - milestone
review_status: draft
---

## Toast

A toast is a brief spoken tribute that celebrates a person or occasion, usually ending with raised glasses. Unlike a prepared lecture or a memoir, the toast is built for the room: it speaks to everyone present but carries meaning because it draws on something specific about the person being honored. That specificity - one story, one quality, one moment - is what lifts a toast above generic well-wishing.

The format has two acts. The first act sets the table: it names the person or occasion, orients the room, and introduces the story or quality that will anchor the tribute. The second act delivers the payoff: it lands on why this person or this moment matters, then closes with a clear, spoken invitation to raise a glass. The invitation is not optional - it is the structural signal that transforms a monologue into a shared ritual.

A toast should feel warm and present, not eulogy-dark or speech-formal. Humor is welcome when it is gentle and specific, not aimed at embarrassing the subject. The test for any detail included is whether it makes the subject feel seen and celebrated - not whether it makes the speaker look witty. Typical length is 150-300 words; longer risks losing the room before the glasses go up.

### Canonical template

```
# Toast: [Person or Occasion]

## Opening
[Name the person or occasion. Orient the room briefly - who you are and your relationship to
the subject.]

## The Story or Quality
[One specific anecdote, memory, or quality that captures why this person or occasion matters.
Be particular: a named moment, a real detail, not a generic virtue.]

## The Landing
[Connect the story back to the celebration. Say what you wish for them, or what this moment
means.]

## The Invite
[The closing line that invites the room to raise a glass. "Please join me in raising a glass
to [Name]." or equivalent.]
```

### When to use

Wedding receptions, rehearsal dinners, or engagement parties; retirement celebrations and farewell gatherings for living honorees; award dinners and milestone birthday or anniversary events; any gathering where a specific person or shared achievement deserves public recognition; team celebrations where one person's contribution needs to be named aloud.

### When not to use

Memorial services or funerals, formal presentations where the audience expects argument or evidence, settings where raising a glass would be inappropriate or logistically impossible.

### Pairs well with

`storyteller`, `friendly-mentor`, `celebratory`, `warm`, `playful`, `narrative-case-study`

### Often confused with

**eulogy**: A eulogy is a formal tribute delivered at a funeral or memorial service for someone who has died. Its emotional register permits grief, loss, and retrospective mourning, and its typical length runs 600-900 words. A toast, by contrast, honors the living and must land on joy - the shared raised glass is a forward-looking act of celebration, not commemoration.
