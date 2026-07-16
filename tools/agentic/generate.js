// tools/agentic/generate.js - GENERATE harness (Stream-B breadth: new candidate entries)
//
// WHAT
//   A Workflow-tool script. Generates new DRAFT format ENTRY.md files, one isolated
//   agent per candidate, each blind to its siblings, mirroring the adr entry template
//   and reading its declared confusable neighbor before writing the disambiguation.
//
// WHY IT MATTERS
//   New entries are the riskiest content (a bad entry dilutes the catalog's moat), so
//   they go through the heaviest gate. The two things that drove the Codex revise-rate
//   from 6/6 to ~1/6 are baked in here: (1) the agent READS its confusable_with
//   neighbor's ENTRY.md before describing it (Step 1b); (2) the CANDIDATES author
//   supplies fixed, pre-validated cross-reference lists that fit the format's nature,
//   so the agent only writes prose and cannot invent or mis-pair ids.
//
// HOW IT WORKS
//   For each candidate, one sonnet agent reads taxonomy/formats/adr/ENTRY.md (the
//   template), reads each confusable neighbor's ENTRY.md, then writes
//   taxonomy/formats/<id>/ENTRY.md with the supplied frontmatter fields and a body
//   mirroring adr (## heading, description, ### Canonical template, When to use /
//   not, Pairs well with, Often confused with). All start review_status: draft.
//
// HOW TO RUN
//   1. Pre-validate the CANDIDATES: every id in pairs_well_with / avoid_with /
//      confusable_with / typical_voices / typical_tones MUST already exist in the
//      catalog (the deterministic gate will reject dangling refs). Choose pairs that
//      fit the format's nature (e.g. an opinion format that argues GETS
//      classical-argument; one that merely declares does NOT).
//   2. Invoke with the Workflow tool.
//   3. Gate: validate.py + build-indexes.py, then a cross-vendor Codex
//      distinguishability gate (see tools/agentic/README.md), apply fixes as targeted
//      edits, then build + counters + PR. New entries stay draft until promoted.
//
// GOTCHA
//   Prose fields (one_liner, concept) with apostrophes MUST be double-quoted JS
//   strings or backtick template literals. YAML-style '' doubling inside a single-
//   quoted JS string is a parse error.

import { fileURLToPath } from 'node:url'
import { dirname, resolve } from 'node:path'

export const meta = {
  name: 'agentic-generate',
  description: 'Generate N draft candidate FORMAT entries, each read-its-neighbor gated, mirroring the adr template',
  phases: [{ title: 'Generate', detail: 'one agent per candidate writes a schema-valid draft ENTRY.md' }],
}

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '../..')

// EDIT THIS: each candidate is pre-validated (all cross-ref ids must already exist).
// `concept` should embed the key contrast with the confusable neighbor.
const CANDIDATES = [
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

function ymlList(items) { return items.map((x) => "'" + x + "'").join(', ') }

function genPrompt(c) {
  const file = 'taxonomy/formats/' + c.id + '/ENTRY.md'
  const neighbors = c.confusable_with.map((n) => 'taxonomy/formats/' + n + '/ENTRY.md').join(' and ')
  return [
    'You are authoring ONE new catalog entry for the writing-style-catalog: a new FORMAT entry "' + c.id + '" (' + c.name + '). The repo root is ' + ROOT + ' and is your working directory; use repo-relative paths.',
    '',
    'Step 1: Read taxonomy/formats/adr/ENTRY.md IN FULL. Your output MUST mirror its frontmatter FIELD SET and body STRUCTURE exactly, changing only the content. Also skim schemas/format.schema.json and schemas/entry.universal.schema.json (tells/anti_patterns/failure_modes are required).',
    '',
    'Step 1b (CRITICAL - neighbor accuracy): Before writing anything about a confusable neighbor, OPEN AND READ ' + neighbors + '. Base every sentence about that neighbor on ITS OWN one_liner and description. Do NOT guess what the neighbor is; a mischaracterized neighbor is rejected.',
    '',
    'Step 2: Write ' + file + '. Frontmatter, in the adr field order:',
    '  id: ' + c.id + '   name: ' + c.name + '   axis: format   domain: ' + c.domain + '   family: ' + c.family,
    '  one_liner: ' + c.one_liner,
    '  CONCEPT to base the description on (keep the neighbor contrast accurate): ' + c.concept,
    '  description: |   (2 to 4 paragraphs)   canonical_template: |   (the format skeleton)',
    '  typical_voices: [' + ymlList(c.typical_voices) + ']   typical_tones: [' + ymlList(c.typical_tones) + ']   digital_or_print: ' + c.dp,
    '  USE EXACTLY THESE validated cross-reference lists (do NOT change, add, or invent ids):',
    '    pairs_well_with: [' + ymlList(c.pairs_well_with) + ']',
    '    avoid_with: [' + ymlList(c.avoid_with) + ']',
    '    confusable_with: [' + ymlList(c.confusable_with) + ']',
    '  when_to_use: (3 to 5 bullets)   when_not_to_use: (3 bullets)',
    '  tells: 5 to 7 strings naming the recognizable surface features.',
    '  anti_patterns: 2 to 4 {pattern, why} maps; include ONE that disambiguates from a confusable_with neighbor (described accurately, per Step 1b).',
    '  failure_modes: 2 to 3 {mode, mitigation} maps. RULE: a failure_mode is this format OVER-HITTING ITS OWN register, NEVER a generic misuse, a rule violation, or a neighbor-format move (those are anti_patterns). Do NOT name a neighbor inside a failure_mode.',
    '  CONSISTENCY: every id in pairs_well_with is compatible by construction; do NOT then write an anti_pattern or description clause that forbids one.',
    '  llm_instruction_phrasing: |   tags: (4 to 6 strings)   review_status: draft',
    '',
    'Step 3: Body, mirroring adr: a level-2 heading with the name, the description paragraphs, "### Canonical template" (fenced), "### When to use", "### When not to use", "### Pairs well with" (ids as inline-code), "### Often confused with" (a bold-led paragraph per confusable_with neighbor, described ACCURATELY per Step 1b).',
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
log('generate: wrote ' + wrote + '/' + CANDIDATES.length)
return { wrote, failed, ids: CANDIDATES.map((c) => c.id) }
