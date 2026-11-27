// tools/agentic/generate.js - GENERATE harness (breadth: new candidate entries)
//
// WHAT
//   A Workflow-tool script. Generates new DRAFT ENTRY.md files on ONE axis, one
//   isolated agent per candidate, each blind to its siblings, mirroring that
//   axis's template entry and reading its declared confusable neighbor before
//   writing the disambiguation.
//
// WHY IT MATTERS
//   New entries are the riskiest content (a bad entry dilutes the catalog's moat), so
//   they go through the heaviest gate. The two things that drove the Codex revise-rate
//   from 6/6 to ~1/6 are baked in here: (1) the agent READS its confusable_with
//   neighbor's ENTRY.md before describing it (Step 1b); (2) the CANDIDATES author
//   supplies fixed, pre-validated cross-reference lists that fit the entry's nature,
//   so the agent only writes prose and cannot invent or mis-pair ids.
//
// AXIS
//   Set AXIS (or pass `args.axis`) to 'format', 'voice', 'tone', or 'style'. The
//   axis selects the taxonomy directory, the template entry the output mirrors, the
//   axis schema, and the axis-specific frontmatter fields the prompt asks for. The
//   'format' path is unchanged from the pre-axis version and is pinned by
//   tests/agentic-harness.test.mjs against a golden captured before the change.
//
//   Each axis carries DIFFERENT candidate fields, because the axis schemas differ:
//     format: domain, family, dp, typical_voices, typical_tones
//     voice:  family, diction, sentence_style, default_pov, typical_tones
//     tone:   spectrum, spectrum_position, nn_g_profile
//     style:  frame, classical_mode
//   Every axis also needs id, name, one_liner, concept, pairs_well_with, avoid_with,
//   confusable_with.
//
// HOW IT WORKS
//   For each candidate, one sonnet agent reads the axis template ENTRY.md, reads each
//   confusable neighbor's ENTRY.md, then writes <axis dir>/<id>/ENTRY.md with the
//   supplied frontmatter fields and a body mirroring the template (## heading,
//   description, the axis's own structural section, When to use / not, Pairs well
//   with, Often confused with). All start review_status: draft.
//
// HOW TO RUN
//   1. Pre-validate the CANDIDATES: every id in pairs_well_with / avoid_with /
//      confusable_with / typical_voices / typical_tones MUST already exist in the
//      catalog (the deterministic gate will reject dangling refs). Choose pairs that
//      fit the entry's nature (e.g. an opinion format that argues GETS
//      classical-argument; one that merely declares does NOT).
//   2. Invoke with the Workflow tool.
//   3. Gate: validate.py + build-indexes.py, then a cross-vendor Codex
//      distinguishability gate (see tools/agentic/README.md), apply fixes as targeted
//      edits, then build + counters + PR. New entries stay draft until promoted.
//
// GOTCHAS
//   - Prose fields (one_liner, concept) with apostrophes MUST be double-quoted JS
//     strings or backtick template literals. YAML-style '' doubling inside a single-
//     quoted JS string is a parse error.
//   - A confusable neighbor may live on ANOTHER axis (the `procedural` style declares
//     the `technical-reference` format, and that format declares both back). Write a
//     cross-axis neighbor as { id, axis } instead of a bare string, so the prompt
//     points the agent at the right directory. A bare string resolves inside the
//     candidate's own axis.
//   - Entry ids are GLOBAL across all four axes (validate.py keys one flat id_map by
//     id alone), so a new id must not collide with an existing id on any axis.

import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

export const meta = {
  name: 'agentic-generate',
  description: 'Generate N draft candidate entries on one axis, each read-its-neighbor gated, mirroring that axis template',
  phases: [{ title: 'Generate', detail: 'one agent per candidate writes a schema-valid draft ENTRY.md' }],
}

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..')

function ymlList(items) { return items.map((x) => "'" + x + "'").join(', ') }

// The per-axis contract: where entries live, what the output mirrors, which schema
// governs it, and which frontmatter fields the prompt must ask for.
const AXES = {
  format: {
    dir: 'taxonomy/formats',
    templateId: 'adr',
    schema: 'schemas/format.schema.json',
    bodySection: '"### Canonical template" (fenced)',
    taxonomyFields: (c) => '   domain: ' + c.domain + '   family: ' + c.family,
    axisFieldLines: (c) => [
      '  description: |   (2 to 4 paragraphs)   canonical_template: |   (the format skeleton)',
      '  typical_voices: [' + ymlList(c.typical_voices) + ']   typical_tones: [' + ymlList(c.typical_tones) + ']   digital_or_print: ' + c.dp,
    ],
  },
  voice: {
    dir: 'taxonomy/voices',
    templateId: 'marketer',
    schema: 'schemas/voice.schema.json',
    bodySection: '"### Language patterns"',
    taxonomyFields: (c) => '   family: ' + c.family + (c.subfamily ? '   subfamily: ' + c.subfamily : ''),
    axisFieldLines: (c) => [
      '  description: |   (2 to 4 paragraphs)',
      '  language_patterns: (5 to 7 strings naming observable sentence structures, word choices, and rhythms)',
      '  diction: ' + c.diction + '   sentence_style: ' + c.sentence_style + '   default_pov: ' + c.default_pov + '   typical_tones: [' + ymlList(c.typical_tones) + ']',
    ],
  },
  tone: {
    dir: 'taxonomy/tones',
    templateId: 'empathetic',
    schema: 'schemas/tone.schema.json',
    bodySection: '"### Markers"',
    taxonomyFields: () => '',
    axisFieldLines: (c) => [
      '  description: |   (2 to 4 paragraphs)',
      '  markers: (5 to 7 strings naming observable textual signals of this tone; minimum 3)',
      '  spectrum: ' + c.spectrum + '   spectrum_position: ' + c.spectrum_position + '   nn_g_profile: ' + c.nn_g_profile,
    ],
  },
  style: {
    dir: 'taxonomy/styles',
    templateId: 'comparison-contrast',
    schema: 'schemas/style.schema.json',
    bodySection: '"### Structural conventions"',
    taxonomyFields: () => '',
    axisFieldLines: (c) => [
      '  description: |   (2 to 4 paragraphs)',
      '  structural_conventions: (5 to 7 strings naming the structure rules this style imposes; minimum 1)',
      '  frame: ' + c.frame + '   classical_mode: ' + c.classical_mode + '   evidence_types: (2 to 4 strings)   reader_contract: (one sentence stating what the reader gets)',
    ],
  },
}

// EDIT THIS: the axis the candidates below belong to, or pass `args.axis`.
const ARGS = (typeof args === 'undefined' || !args) ? {} : args
const AXIS = ARGS.axis || 'format'

// EDIT THIS: each candidate is pre-validated (all cross-ref ids must already exist).
// `concept` should embed the key contrast with the confusable neighbor. Pass
// `args.candidates` to supply them from outside instead of editing this array.
const CANDIDATES = ARGS.candidates || [
  {
    id: 'example-id', name: 'Example Name', domain: 'professional', family: 'brief', dp: 'digital',
    one_liner: "A one-line description of what this format is.",
    concept: "Two to four sentences of what the format is and why it earns its place, ending with the contrast against its confusable neighbor.",
    pairs_well_with: ['some-voice', 'some-tone', 'some-style'],
    avoid_with: ['some-voice', 'some-tone'],
    confusable_with: ['some-format'],
    typical_voices: ['some-voice', 'some-voice'], typical_tones: ['some-tone', 'some-tone'],
  },
]

function axisConfig(axis) {
  const cfg = AXES[axis]
  if (!cfg) throw new Error('generate: unknown axis "' + axis + '"; expected one of ' + Object.keys(AXES).join(', '))
  return cfg
}

// A neighbor is either a bare id on the candidate's own axis, or { id, axis }.
function neighborId(n) { return typeof n === 'string' ? n : n.id }
function neighborPath(n, axis) {
  return (typeof n === 'string' ? axisConfig(axis).dir : axisConfig(n.axis).dir) + '/' + neighborId(n) + '/ENTRY.md'
}

export function genPrompt(c, axis = AXIS, root = ROOT) {
  const cfg = axisConfig(axis)
  const file = cfg.dir + '/' + c.id + '/ENTRY.md'
  const neighbors = c.confusable_with.map((n) => neighborPath(n, axis)).join(' and ')
  return [
    'You are authoring ONE new catalog entry for the writing-style-catalog: a new ' + axis.toUpperCase() + ' entry "' + c.id + '" (' + c.name + '). The repo root is ' + root + ' and is your working directory; use repo-relative paths.',
    '',
    'Step 1: Read ' + cfg.dir + '/' + cfg.templateId + '/ENTRY.md IN FULL. Your output MUST mirror its frontmatter FIELD SET and body STRUCTURE exactly, changing only the content. Also skim ' + cfg.schema + ' and schemas/entry.universal.schema.json (tells/anti_patterns/failure_modes are required).',
    '',
    'Step 1b (CRITICAL - neighbor accuracy): Before writing anything about a confusable neighbor, OPEN AND READ ' + neighbors + '. Base every sentence about that neighbor on ITS OWN one_liner and description. Do NOT guess what the neighbor is; a mischaracterized neighbor is rejected.',
    '',
    'Step 2: Write ' + file + '. Frontmatter, in the ' + cfg.templateId + ' field order:',
    '  id: ' + c.id + '   name: ' + c.name + '   axis: ' + axis + cfg.taxonomyFields(c),
    '  one_liner: ' + c.one_liner,
    '  CONCEPT to base the description on (keep the neighbor contrast accurate): ' + c.concept,
    ...cfg.axisFieldLines(c),
    '  USE EXACTLY THESE validated cross-reference lists (do NOT change, add, or invent ids):',
    '    pairs_well_with: [' + ymlList(c.pairs_well_with) + ']',
    '    avoid_with: [' + ymlList(c.avoid_with) + ']',
    '    confusable_with: [' + ymlList(c.confusable_with.map(neighborId)) + ']',
    '  when_to_use: (3 to 5 bullets)   when_not_to_use: (3 bullets)',
    '  tells: 5 to 7 strings naming the recognizable surface features.',
    '  anti_patterns: 2 to 4 {pattern, why} maps; include ONE that disambiguates from a confusable_with neighbor (described accurately, per Step 1b).',
    '  failure_modes: 2 to 3 {mode, mitigation} maps. RULE: a failure_mode is this ' + axis + ' OVER-HITTING ITS OWN register, NEVER a generic misuse, a rule violation, or a neighbor-' + axis + ' move (those are anti_patterns). Do NOT name a neighbor inside a failure_mode.',
    '  CONSISTENCY: every id in pairs_well_with is compatible by construction; do NOT then write an anti_pattern or description clause that forbids one.',
    '  llm_instruction_phrasing: |   tags: (4 to 6 strings)   review_status: draft',
    '',
    'Step 3: Body, mirroring ' + cfg.templateId + ': a level-2 heading with the name, the description paragraphs, ' + cfg.bodySection + ', "### When to use", "### When not to use", "### Pairs well with" (ids as inline-code), "### Often confused with" (a bold-led paragraph per confusable_with neighbor, described ACCURATELY per Step 1b).',
    '',
    'REQUIREMENTS:',
    '- Valid YAML. Escape an apostrophe inside a single-quoted YAML scalar by doubling it.',
    '- HARD RULE: no em-dashes (U+2014) or en-dashes (U+2013); use " - ". The write is rejected if they appear.',
    '- Use ONLY the provided cross-reference ids.',
    '- After writing successfully, return ONLY "' + c.id + ' OK".',
  ].join('\n')
}

phase('Generate')
const results = await parallel(CANDIDATES.map((c) => () => agent(genPrompt(c), { label: 'gen:' + c.id, phase: 'Generate', model: 'sonnet' })))
const wrote = results.filter(Boolean).length
const failed = CANDIDATES.filter((c, i) => !results[i]).map((c) => c.id)
log('generate(' + AXIS + '): wrote ' + wrote + '/' + CANDIDATES.length)
return { axis: AXIS, wrote, failed, ids: CANDIDATES.map((c) => c.id) }
