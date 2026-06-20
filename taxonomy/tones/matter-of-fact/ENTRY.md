---
id: matter-of-fact
name: Matter of Fact
axis: tone
one_liner: States what is true without editorial coloring - neither cold nor warm, just accurate.
description: |
  Matter-of-fact is the tone of the briefing that gets the decision made. It does not
  editorialize. It does not boost or undermine. It presents the situation as it is, trusting the
  reader to have the appropriate response. This tone is not cold - cold is a deliberate
  withdrawal of warmth. Matter-of-fact simply has no agenda about how the reader should feel.

  Where warm tone says "this is a really exciting opportunity," matter-of-fact says "this is an
  opportunity." Where candid tone says "I will be honest with you - this is harder than it
  looks," matter-of-fact says "this is harder than it looks" (without marking itself as candid).
  The difference is the absence of meta-commentary on the communication itself.

  Matter-of-fact tone works best when the content is serious or technical enough that tonal
  performance would feel inappropriate, or when the writer wants to convey that they are giving
  a straight account with no spin.
markers:
  - Declarative sentences without hedging
  - 'No intensifiers: not "very important" but "important"'
  - 'No mood markers: not "unfortunately" or "excitingly" - just the fact'
  - Active voice stating what is
  - 'No meta-commentary on the communication: not "I want to be clear" but just the clear statement'
  - Neutral sentence endings - statements close, not questions or emphatics
spectrum: neutral-expressive
nn_g_profile: neutral
pairs_well_with:
  - pragmatic-architect
  - operator
  - candid
avoid_with:
  - warm
  - encouraging
  - reverent
confusable_with:
  - candid
when_to_use:
  - Status updates and progress reports
  - Incident reports and technical documentation
  - Briefings where editorializing would be inappropriate
  - Any context where spin would reduce credibility
  - Handoffs and summaries requiring only facts
when_not_to_use:
  - Condolences or emotional support
  - Celebration and recognition writing
  - Persuasion and fundraising
  - Onboarding where tone helps retention
  - Coaching or feedback contexts requiring warmth
tells:
  - 'Declarative sentences without hedging'
  - 'No intensifiers: "important," not "very important"'
  - 'No mood markers: not "unfortunately" or "excitingly," just the fact'
  - 'Active voice stating what is'
  - 'No meta-commentary on the communication ("I want to be clear"), just the clear statement'
  - 'Neutral sentence endings: statements close, not questions or emphatics'
anti_patterns:
  - pattern: 'Marking the honesty explicitly ("I want to be direct with you") before the statement'
    why: 'That is candid, which frames its own truth-telling; matter-of-fact has no frame at all and simply states the truth without commenting on the act of stating it.'
  - pattern: 'Letting the writer''s certainty or conviction color the claim'
    why: 'That is confident, which carries an explicit affect; matter-of-fact is affect-neutral and reports the fact without staking the writer''s position on it.'
  - pattern: 'Slipping in intensifiers or mood words ("unfortunately," "thankfully," "really")'
    why: 'Those editorialize how the reader should feel; matter-of-fact has no agenda about the reader''s response and trusts them to react appropriately on their own.'
failure_modes:
  - mode: 'Over-neutralizes into coldness, reading as a deliberate withdrawal of warmth rather than its absence'
    mitigation: 'Remember the tone has no agenda about feeling, including no agenda to seem detached; state the fact plainly without performing distance. Coldness is a stance, and matter-of-fact takes no stance at all.'
  - mode: 'Over-neutralizes until salience is flattened, reporting a critical fact in the same affectless register as a trivial one so the reader cannot tell what matters'
    mitigation: 'Neutrality means not coloring the reader''s reaction, not hiding consequence; let selection and order (what is stated first, what is included) carry the weight the tone refuses to add with mood words.'
llm_instruction_phrasing: |
  Write in a matter-of-fact tone. State what is true without editorial coloring - no
  intensifiers, no mood markers, no meta-commentary on the communication itself. Do not say
  "I want to be clear" - just be clear. Do not say "unfortunately" - just state the consequence.
  No "very," no "really," no "exciting." Declarative sentences. Active voice. Trust the reader
  to have the appropriate response without your coaching.
tags:
  - neutral
  - accurate
  - direct
  - professional
  - unboosted
review_status: stable
---

## Matter of Fact

Matter-of-fact is the tone of the briefing that gets the decision made. It does not editorialize. It does not boost or undermine. It presents the situation as it is, trusting the reader to have the appropriate response. This tone is not cold - cold is a deliberate withdrawal of warmth. Matter-of-fact simply has no agenda about how the reader should feel.

Where warm tone says "this is a really exciting opportunity," matter-of-fact says "this is an opportunity." Where candid tone says "I will be honest with you - this is harder than it looks," matter-of-fact says "this is harder than it looks" (without marking itself as candid). The difference is the absence of meta-commentary on the communication itself.

Matter-of-fact tone works best when the content is serious or technical enough that tonal performance would feel inappropriate, or when the writer wants to convey that they are giving a straight account with no spin.

### Markers

- Declarative sentences without hedging
- No intensifiers: not "very important" but "important"
- No mood markers: not "unfortunately" or "excitingly" - just the fact
- Active voice stating what is
- No meta-commentary on the communication: not "I want to be clear" but just the clear statement
- Neutral sentence endings - statements close, not questions or emphatics

### When to use

Status updates, incident reports, technical documentation, briefings, and any context where editorializing would undermine credibility.

### When not to use

Condolences, celebrations, persuasion, emotional support, and coaching contexts where tone aids retention and engagement.

### Pairs well with

`pragmatic-architect`, `operator`, `candid`

### Often confused with

**candid**: Candid names the meta-communication explicitly - "I want to be direct with you" - and then says the hard thing. Matter-of-fact simply states the truth without marking it. Candid has an explicit frame; matter-of-fact has no frame at all.
