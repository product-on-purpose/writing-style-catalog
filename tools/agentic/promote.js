// tools/agentic/promote.js - RENDER harness (the promotion factory's render stage)
//
// WHAT
//   A Workflow-tool script (NOT a standalone CLI - it runs only through the Claude
//   Code Workflow tool). It renders each entry in `ENTRIES` across all 12 anchor
//   topics, writing one worked-sample file per (entry, topic) cell, so the entries
//   can then be promoted without failing the Gate 2 sample-count check.
//
// WHY IT MATTERS
//   An admitted entry must render on all 12 anchor topics (Gate 2). Drafts are
//   exempt, so you RENDER while still draft (validate stays green), THEN flip with
//   tools/promote.py. This harness is the render step. One isolated agent per cell
//   keeps the 12*N prose blocks out of the orchestrator's context and lets each cell
//   inherit the topic's shared scenario from the existing samples.
//
// AXIS
//   Set AXIS (or pass `args.axis`) to 'format', 'voice', 'tone', or 'style'. The axis
//   selects the taxonomy directory to read, the sample filename prefix to write
//   (`examples/vertical-slices/<topic>/<axis>-<id>.md`, which is the key
//   tools/promote.py already expects), the entry fields the agent is told to read,
//   and the forced-combo instruction. The 'format' path is unchanged from the
//   pre-axis version and is pinned by tests/agentic-harness.test.mjs against a
//   golden captured before the change.
//
// HOW IT WORKS
//   For each cell, one sonnet agent: (1) reads <axis dir>/<id>/ENTRY.md for the
//   entry's own structure; (2) reads three existing samples on the topic
//   (format-adr/readme/status-report.md) to inherit the SHARED SCENARIO - the named
//   people, situation, and dates every sample on that topic reuses - plus, on the
//   non-format axes, one sibling sample on the SAME axis for shape; (3) writes
//   examples/vertical-slices/<topic>/<axis>-<id>.md with the required frontmatter.
//   Forced combos (an eng format on a contemplative topic) are expected: apply the
//   entry's own structure or register to the topic's situation (precedent:
//   daily-rest-practice/format-adr.md renders an ADR for a personal rest decision,
//   and async-standups/voice-marketer.md renders marketing copy for an internal
//   process change).
//
// HOW TO RUN
//   1. Set AXIS and ENTRIES to the draft ids you are about to promote.
//   2. Invoke this file with the Workflow tool: Workflow({ scriptPath: ".../promote.js" }).
//   3. validate.py + a DATE GATE on any dated entries (see tools/agentic/README.md),
//      then tools/promote.py to flip, then counters + manifests + PR.
//
// GOTCHAS
//   - The 12 TOPICS below mirror tools/anchor_topics.py seed_pool(); keep them in
//     sync if the pool changes. Prose passed into agent prompts must avoid
//     YAML-style '' apostrophe doubling - that is a JS parse error inside a
//     single-quoted string.
//   - LLM_MODEL is stamped into every sample's frontmatter. It defaults to the value
//     the Stream-B Format renders carried, so the Format path stays byte-identical.
//     SET IT to the model actually doing the rendering before you run: the October
//     marketer renders, for instance, carry claude-sonnet-5-5.

import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

export const meta = {
  name: 'agentic-render',
  description: 'Render N entries on one axis across all 12 anchor topics (12*N worked samples), reusing each topic shared scenario',
  phases: [{ title: 'Render', detail: 'one agent per (entry, topic) cell writes a scenario-consistent sample' }],
}

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..')

const ARGS = (typeof args === 'undefined' || !args) ? {} : args

// The per-axis contract: where entries live, which of their fields carry the
// render instruction, which sibling sample shows the axis's own sample shape, and
// how to phrase a forced entry/topic pairing.
const AXES = {
  format: {
    dir: 'taxonomy/formats',
    readFields: 'its structure, tells, canonical_template, and llm_instruction_phrasing',
    houseRef: null,
    forcedCombo: 'an ADR applied to a personal decision still uses Status / Context / Decision / Consequences; render the real structure of the format on whatever situation this topic carries',
  },
  voice: {
    dir: 'taxonomy/voices',
    readFields: 'its language_patterns, tells, diction, default_pov, and llm_instruction_phrasing',
    houseRef: 'technical-writer',
    forcedCombo: 'the marketer voice renders on the contemplative topics without softening (precedent: async-standups/voice-marketer.md); render the real register of THIS voice on whatever situation this topic carries, and do not retreat to a generic one',
  },
  tone: {
    dir: 'taxonomy/tones',
    readFields: 'its markers, tells, spectrum, and llm_instruction_phrasing',
    houseRef: 'matter-of-fact',
    forcedCombo: 'a tone does not change because the occasion is awkward for it; render the real affect of THIS tone on whatever situation this topic carries, and do not drift to a neutral register',
  },
  style: {
    dir: 'taxonomy/styles',
    readFields: 'its structural_conventions, tells, reader_contract, and llm_instruction_phrasing',
    houseRef: 'comparison-contrast',
    forcedCombo: 'an analytical style applied to a ceremonial topic still follows its own structure; render the real shape of THIS style on whatever situation this topic carries',
  },
}

// EDIT THIS: the axis the ids below belong to, or pass `args.axis`.
const AXIS = ARGS.axis || 'format'

// EDIT THIS: the draft entry ids to render (then promote). Or pass `args.entries`.
const ENTRIES = ARGS.entries || ['example-format-id']

// EDIT THIS before every run: the model that will actually render these samples.
// It is stamped into each sample's `llm_model` frontmatter field.
const LLM_MODEL = ARGS.llmModel || 'claude-sonnet-4-6'

// The 12 anchor topics (slug, label) - keep in sync with tools/anchor_topics.py.
const TOPICS = [
  ['service-database-choice', 'Choosing Postgres vs DynamoDB for a new service'],
  ['async-standups', 'Whether the team should move to async-first standups'],
  ['roadmap-deprioritization', 'Telling stakeholders a committed feature is being cut this quarter'],
  ['onboarding-a-new-hire', 'Getting a new engineer productive in their first two weeks'],
  ['remote-work-policy', 'Arguing a public position on return-to-office'],
  ['product-launch-announcement', 'Announcing a new product to an outside audience'],
  ['morning-routine', 'Designing a sustainable morning routine'],
  ['thanking-a-mentor', 'Writing to thank a mentor who shaped your career'],
  ['retirement-send-off', "Marking a long-serving colleague's departure"],
  ['team-milestone-celebration', 'Marking the team shipping a hard, long project'],
  ['daily-rest-practice', 'Reflecting on keeping a discipline of rest'],
  ['a-hard-year-in-review', 'A personal year-end reckoning with a difficult year'],
]

function axisConfig(axis) {
  const cfg = AXES[axis]
  if (!cfg) throw new Error('render: unknown axis "' + axis + '"; expected one of ' + Object.keys(AXES).join(', '))
  return cfg
}

export function cellPrompt(id, slug, label, axis = AXIS, root = ROOT, model = LLM_MODEL) {
  const cfg = axisConfig(axis)
  const file = 'examples/vertical-slices/' + slug + '/' + axis + '-' + id + '.md'
  const houseLines = cfg.houseRef
    ? [
      '  examples/vertical-slices/' + slug + '/' + axis + '-' + cfg.houseRef + '.md',
      'The first three samples are your source for the SCENARIO. The fourth is a sibling on the SAME axis: read it for sample shape and length only, never for its ' + axis + '.',
    ]
    : []
  return [
    'You are rendering ONE worked example for the writing-style-catalog: the ' + axis.toUpperCase() + ' "' + id + '" applied to the anchor topic "' + slug + '" (' + label + '). Working directory: ' + root + ' (use repo-relative paths).',
    '',
    'Step 1: Read ' + cfg.dir + '/' + id + '/ENTRY.md - ' + cfg.readFields + '.',
    '',
    'Step 2: Read these EXISTING samples on this topic to learn the SHARED SCENARIO (the specific situation, named people, concrete details, and dates that every sample on this topic reuses) and the house style:',
    '  examples/vertical-slices/' + slug + '/format-adr.md',
    '  examples/vertical-slices/' + slug + '/format-readme.md',
    '  examples/vertical-slices/' + slug + '/format-status-report.md',
    ...houseLines,
    'Your sample MUST use the SAME scenario - same people, same situation, same specifics and dates - so it is directly comparable to the other samples on this topic. Do NOT invent a different situation.',
    '',
    'Step 3: Write the file ' + file + '. Apply the "' + id + '" ' + axis + ' faithfully to the shared scenario of this topic, even when the pairing is unusual (' + cfg.forcedCombo + '). Frontmatter, exactly these fields:',
    '---',
    'entry_id: ' + id,
    'axis: ' + axis,
    'topic_slug: ' + slug,
    'topic_label: ' + label,
    'author_type: llm',
    'llm_model: ' + model,
    'review_status: reviewed',
    '---',
    'Then a blank line and the worked sample body.',
    '',
    'REQUIREMENTS:',
    '- Reuse the people, situation, and specifics from the existing scenario; stay consistent with any dates/weekdays the existing samples use (do not introduce contradictory dates).',
    '- HARD RULE: no em-dashes (U+2014) or en-dashes (U+2013); use " - " (space hyphen space). The write is REJECTED if they appear.',
    '- No fabricated statistics and no real-company / real-person claims; keep details internal and first-person/low-fabrication, matching the existing samples.',
    '- Match the length and density typical of this ' + axis + ' (per its ENTRY.md).',
    '- After writing the file, return ONLY "' + id + '@' + slug + ' OK". Do not return the file content.',
  ].join('\n')
}

const CELLS = []
for (const id of ENTRIES) for (const [slug, label] of TOPICS) CELLS.push({ id, slug, label })

phase('Render')
const results = await parallel(CELLS.map((c) => () => agent(cellPrompt(c.id, c.slug, c.label), { label: c.id + '@' + c.slug, phase: 'Render', model: 'sonnet' })))
const wrote = results.filter(Boolean).length
const failed = CELLS.filter((c, i) => !results[i]).map((c) => c.id + '@' + c.slug)
log('render(' + AXIS + '): wrote ' + wrote + '/' + CELLS.length + ' samples')
return { axis: AXIS, wrote, failed, cells: CELLS.length }
