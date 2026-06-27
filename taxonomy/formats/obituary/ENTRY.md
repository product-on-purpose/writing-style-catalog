---
id: obituary
name: Obituary
axis: format
domain: ceremonial
family: tribute
one_liner: A written death notice that records a life for the public - who the person was, what they did, and who survives them.
description: |
  An obituary is the written death notice that records a life for the public: who the person was, what
  they did, who survives them, and where and when the service will be held. Published in newspapers,
  funeral home listings, and community archives, it is the lasting factual record of a death and the
  life that preceded it. Its purpose is completeness - to make the public record accurate and retrievable
  for anyone who needs it, now or decades later.

  The format is biographical by design. It opens with full name, age, and date and place of death, then
  moves through the life in chronological or thematic order: birth and origins, education and career,
  personal life and faith, and any notable achievements. It closes with survivors listed by name and
  relationship and service details for the community. Every section serves the record: the biographical
  narrative makes the life retrievable as history, the survivor list honors the living, and the service
  information serves the people who want to attend or send condolences.

  Unlike a eulogy, which is spoken and selects two or three moments to make the person present one more
  time, an obituary is published, comprehensive, and biographical. It carries the facts of a life in
  compressed, dignified prose and serves as the lasting public record of the death. Where a eulogy
  chooses the detail that carries emotional weight, an obituary covers the life. The craft is
  compression, not selection: fitting the whole of a life into readable prose that leaves nothing
  essential out. Typical length is 200 to 500 words for a standard death notice and 500 to 1000 words
  for a full-length obituary in a regional newspaper or publication.
canonical_template: |
  [FULL NAME], [AGE], of [CITY, STATE], died [DATE] at [LOCATION].

  ## Opening character sentence (optional)
  [One sentence that gives a sense of who this person was]

  ## Biographical narrative
  [Birth and origins]
  [Education and career]
  [Personal life - faith, interests, community involvement]

  ## Survivors
  [FIRST NAME] is survived by [list of survivors by name and relationship].

  ## Service information
  [Services will be held on DATE at TIME at LOCATION.]

  ## Memorial contributions (optional)
  [In lieu of flowers, the family requests contributions to NAME.]
typical_voices:
  - journalist
  - storyteller
typical_tones:
  - reverent
  - matter-of-fact
digital_or_print: both
pairs_well_with:
  - journalist
  - storyteller
  - reverent
  - matter-of-fact
  - chronological-narrative
avoid_with:
  - playful
  - skeptical
  - urgent
confusable_with:
  - eulogy
when_to_use:
  - Announcing a death to the public in a newspaper, funeral home listing, or community archive
  - Creating a lasting biographical record retrievable by people who did not know the person personally
  - When factual completeness and chronological accuracy matter more than emotional resonance
  - When the piece will be published and must stand alone as the public record without a speaker
  - When the audience includes strangers or distant acquaintances who need the facts of the life
when_not_to_use:
  - When the goal is to make the person emotionally present for a grieving audience already assembled
  - When the piece will be delivered orally at a memorial service
  - When the writer has access to rich personal memory and the occasion calls for spoken tribute rather than comprehensive record
tells:
  - 'Opens with full name, age, and date and place of death in the first sentence'
  - 'Biographical narrative in chronological order covers birth, education, career, and personal life'
  - 'Survivors listed by name and relationship in a dedicated section'
  - 'Service information - date, time, and location - appears near or at the end'
  - 'Third person throughout with no speaker or narrator present in the text'
  - 'Compressed dignified prose that favors completeness over emotional selection'
  - 'Memorial contribution information follows the service details when present'
anti_patterns:
  - pattern: 'Selecting two or three specific emotional moments and writing toward resonance instead of biographical completeness'
    why: 'This slides into the territory of the eulogy, which is spoken and selects the moments that make the person present one more time; an obituary is published and owes the reader a factual account of the whole life, not a curated emotional experience.'
  - pattern: 'Listing every credential, committee membership, and award without a prose thread to connect them'
    why: 'A bare enumeration of achievements produces a resume, not a life record; the obituary earns its place through compressed narrative that threads facts into a readable account.'
  - pattern: 'Relying on generic honorifics ("devoted spouse," "tireless servant") in place of concrete biographical detail'
    why: 'Superlatives are interchangeable across any subject and add nothing to the public record; at least one concrete specific - the job held for thirty years, the town they never left - does more work than a string of adjectives.'
  - pattern: 'Omitting survivors or service information in favor of a longer biographical section'
    why: 'The obituary serves a practical community function; readers need to know who survives and where the service is held, and stripping these elements turns the piece into a profile rather than a death notice.'
failure_modes:
  - mode: 'Over-catalogs - the obituary becomes so exhaustive, listing every committee membership, every award, and every date, that the person disappears into an inventory of facts the prose cannot carry'
    mitigation: 'Compression is the core skill; include what reveals the life, not every verifiable fact, and use prose to thread the details into a readable account rather than enumerating them.'
  - mode: 'Over-formalizes - the prose becomes so ceremonially dignified that the person''s actual character is flattened into generic honorifics and any person could fit the text'
    mitigation: 'Anchor the dignity in at least one or two concrete specifics - the job they held, the neighborhood they never left - rather than relying entirely on adjective-driven tributes.'
  - mode: 'Collapses into notice - compresses so aggressively that the biographical narrative shrinks to a sentence or two, leaving only name, date, and service information; the practical function is served but the life record is not'
    mitigation: 'The biographical narrative should be the longest section; if the obituary reads like a bare death notice, expand the biographical paragraph even if it means trimming the credentials list.'
llm_instruction_phrasing: |
  Write as an obituary. Open with the full name, age, and date and place of death in the first sentence.
  Move through the life in compressed biographical prose: origins and birth, education and career,
  personal life and faith, and any significant achievements. List survivors by name and relationship in
  a dedicated section, then close with service details (date, time, and location). Write in the third
  person throughout; no speaker or narrator should appear in the text. Favor completeness over emotional
  selection - the obituary is the lasting public record of the death, not a curated tribute. Use
  dignified, matter-of-fact prose that carries the facts without embellishment or excessive sentiment.
  Keep the biographical narrative as the longest section; practical details serve the record but do not
  replace it. Typical length is 200 to 500 words for a death notice or 500 to 1000 words for a full
  obituary.
tags:
  - ceremonial
  - memorial
  - tribute
  - death-notice
  - biographical
  - public-record
review_status: draft
---

## Obituary

An obituary is the written death notice that records a life for the public: who the person was, what they did, who survives them, and where and when the service will be held. Published in newspapers, funeral home listings, and community archives, it is the lasting factual record of a death and the life that preceded it. Its purpose is completeness - to make the public record accurate and retrievable for anyone who needs it, now or decades later.

The format is biographical by design. It opens with full name, age, and date and place of death, then moves through the life in chronological or thematic order: birth and origins, education and career, personal life and faith, and any notable achievements. It closes with survivors listed by name and relationship and service details for the community. Every section serves the record: the biographical narrative makes the life retrievable as history, the survivor list honors the living, and the service information serves the people who want to attend or send condolences.

### Canonical template

```
[FULL NAME], [AGE], of [CITY, STATE], died [DATE] at [LOCATION].

## Opening character sentence (optional)
[One sentence that gives a sense of who this person was]

## Biographical narrative
[Birth and origins]
[Education and career]
[Personal life - faith, interests, community involvement]

## Survivors
[FIRST NAME] is survived by [list of survivors by name and relationship].

## Service information
[Services will be held on DATE at TIME at LOCATION.]

## Memorial contributions (optional)
[In lieu of flowers, the family requests contributions to NAME.]
```

### When to use

Announcing a death to the public in a newspaper, funeral home listing, or community archive; creating a lasting biographical record retrievable by people who did not know the person personally; when factual completeness and chronological accuracy matter more than emotional resonance; when the piece will be published and must stand alone as the public record without a speaker; when the audience includes strangers or distant acquaintances who need the facts of the life.

### When not to use

When the goal is to make the person emotionally present for a grieving audience already assembled; when the piece will be delivered orally at a memorial service; when the writer has access to rich personal memory and the occasion calls for spoken tribute rather than comprehensive record.

### Pairs well with

`journalist`, `storyteller`, `reverent`, `matter-of-fact`, `chronological-narrative`

### Often confused with

**eulogy**: A eulogy is a tribute spoken at a funeral or memorial service that honors a person through specific, concrete memory rather than abstract praise. Its purpose is not to summarize a life but to make the person present one more time by recounting the moments - a phrase they always used, a choice they made when no one was watching - that carry them forward. An obituary is its complement, not its replacement: published rather than spoken, comprehensive rather than selective, and built to serve readers who need the factual record, not the assembled mourners who need the person back in the room one more time.
