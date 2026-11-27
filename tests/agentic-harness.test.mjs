// Tests for the axis-parameterized tools/agentic/* Workflow harnesses.
//
// Two jobs:
//
//   1. PIN THE FORMAT PATH. Each harness is checked against a golden prompt in
//      tests/golden-outputs/agentic/, captured from the harness as it stood BEFORE
//      the Stream-C axis generalization. A byte-for-byte match is what makes
//      "existing Format behavior unchanged" a machine-checkable claim rather than an
//      assertion. Never recapture those goldens from the current code.
//
//   2. COVER THE NEW AXES. The voice, tone, and style paths are checked for the
//      things that would silently produce a broken entry or an unreachable sample:
//      the taxonomy directory, the template entry that exists on disk, the axis
//      schema, the axis value written into frontmatter, the sample filename key
//      tools/promote.py reads, and cross-axis confusable resolution.

import { test } from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync, existsSync } from 'node:fs'
import { resolve } from 'node:path'

import { runHarness, normalizeRoot, REPO_ROOT } from './helpers/load-harness.mjs'
import {
  FORMAT_CANDIDATE, VOICE_CANDIDATE, TONE_CANDIDATE, STYLE_CANDIDATE,
  DEDUP_GROUP_TONE,
} from './fixtures/agentic-fixtures.mjs'

const HARNESS = {
  generate: resolve(REPO_ROOT, 'tools/agentic/generate.js'),
  render: resolve(REPO_ROOT, 'tools/agentic/promote.js'),
  dedup: resolve(REPO_ROOT, 'tools/agentic/dedup.js'),
}

const AXES = ['format', 'voice', 'tone', 'style']

const AXIS_DIR = {
  format: 'taxonomy/formats',
  voice: 'taxonomy/voices',
  tone: 'taxonomy/tones',
  style: 'taxonomy/styles',
}

// The repo has no .gitattributes, so a Windows checkout with core.autocrlf=true
// rewrites a committed golden to CRLF while the harness always builds prompts with
// LF. Comparing after normalizing line endings keeps the test byte-exact in every
// way that matters and portable across checkouts.
function lf(text) {
  return text.replaceAll('\r\n', '\n')
}

function golden(name) {
  return lf(readFileSync(resolve(REPO_ROOT, 'tests/golden-outputs/agentic', name), 'utf8'))
}

function joined(prompts) {
  return lf(prompts.map((p) => normalizeRoot(p)).join('\n===PROMPT===\n') + '\n')
}

// ---------------------------------------------------------------------------
// 1. The Format path is unchanged
// ---------------------------------------------------------------------------

test('generate.js emits the pre-axis Format prompt byte for byte', async () => {
  const r = await runHarness(HARNESS.generate)
  assert.equal(r.prompts.length, 1)
  assert.equal(joined(r.prompts), golden('generate-format.txt'))
})

test('promote.js emits the pre-axis Format render prompts byte for byte', async () => {
  const r = await runHarness(HARNESS.render)
  assert.equal(r.prompts.length, 12, 'one prompt per anchor topic')
  assert.equal(joined(r.prompts), golden('render-format.txt'))
})

test('dedup.js emits the pre-axis Format audit prompt byte for byte', async () => {
  const r = await runHarness(HARNESS.dedup)
  assert.equal(r.prompts.length, 1)
  assert.equal(joined(r.prompts), golden('dedup-format.txt'))
})

test('format stays the default axis when no args are passed', async () => {
  for (const [name, file] of Object.entries(HARNESS)) {
    const r = await runHarness(file)
    assert.equal(r.result.axis, 'format', `${name} should default to the format axis`)
  }
})

// ---------------------------------------------------------------------------
// 2. Every harness declares a pure-literal meta and loads under the runtime shape
// ---------------------------------------------------------------------------

test('every harness exports a pure-literal meta with a phases entry per phase', async () => {
  for (const [name, file] of Object.entries(HARNESS)) {
    const r = await runHarness(file)
    assert.ok(r.meta, `${name}: meta was not captured`)
    assert.equal(typeof r.meta.name, 'string')
    assert.equal(typeof r.meta.description, 'string')
    assert.ok(Array.isArray(r.meta.phases) && r.meta.phases.length >= 1)

    // The Workflow tool requires meta to be a pure literal: no variables, calls,
    // spreads, or interpolation. Catch the easy violations in the source text.
    const literal = r.source.match(/^export const meta = \{[\s\S]*?\n\}$/m)
    assert.ok(literal, `${name}: meta literal not found at column 0`)
    // A plus sign can legitimately appear inside a description string, so the
    // check targets the constructs the runtime actually forbids.
    assert.ok(!/[`]|\$\{|\.\.\./.test(literal[0]), `${name}: meta must not interpolate or spread`)

    // Each phase() title must have a matching meta.phases entry.
    const titles = r.meta.phases.map((p) => p.title)
    for (const used of r.phases) assert.ok(titles.includes(used), `${name}: phase "${used}" is not in meta.phases`)
  }
})

// Built from code points so this test file itself stays free of the characters it
// forbids; the pre-commit hook scans every file in the repo, tests included.
const EM_DASH = String.fromCharCode(0x2014)
const EN_DASH = String.fromCharCode(0x2013)

test('no harness source carries an em-dash or en-dash', () => {
  for (const [name, file] of Object.entries(HARNESS)) {
    const src = readFileSync(file, 'utf8')
    assert.ok(!src.includes(EM_DASH), `${name}: contains an em-dash`)
    assert.ok(!src.includes(EN_DASH), `${name}: contains an en-dash`)
  }
})

// ---------------------------------------------------------------------------
// 3. All four axes are supported, and their on-disk targets exist
// ---------------------------------------------------------------------------

test('generate.js supports all four axes and points at a template that exists', async () => {
  const candidates = {
    format: FORMAT_CANDIDATE, voice: VOICE_CANDIDATE, tone: TONE_CANDIDATE, style: STYLE_CANDIDATE,
  }
  for (const axis of AXES) {
    const c = candidates[axis]
    const r = await runHarness(HARNESS.generate, { args: { axis, candidates: [c] } })
    assert.equal(r.prompts.length, 1)
    const p = r.prompts[0]

    assert.ok(p.startsWith(`You are authoring ONE new catalog entry for the writing-style-catalog: a new ${axis.toUpperCase()} entry "${c.id}"`), `${axis}: wrong opening`)
    assert.ok(p.includes(`Step 2: Write ${AXIS_DIR[axis]}/${c.id}/ENTRY.md.`), `${axis}: wrong output path`)
    assert.ok(p.includes(`axis: ${axis}`), `${axis}: frontmatter axis not set`)
    assert.ok(p.includes(`schemas/${axis}.schema.json`), `${axis}: wrong axis schema`)
    assert.ok(p.includes('review_status: draft'), `${axis}: entries must start as drafts`)

    // The template the output mirrors must be a real entry on this axis.
    const template = p.match(/^Step 1: Read (\S+) IN FULL\./m)
    assert.ok(template, `${axis}: Step 1 does not name a template`)
    assert.ok(template[1].startsWith(AXIS_DIR[axis] + '/'), `${axis}: template is not on this axis`)
    assert.ok(existsSync(resolve(REPO_ROOT, template[1])), `${axis}: template ${template[1]} does not exist`)
  }
})

test('generate.js asks for the axis-specific required frontmatter fields', async () => {
  const expected = {
    format: ['canonical_template', 'digital_or_print', 'typical_voices'],
    voice: ['language_patterns', 'diction', 'default_pov', 'family: care'],
    tone: ['markers', 'spectrum', 'nn_g_profile'],
    style: ['structural_conventions', 'frame', 'reader_contract'],
  }
  const candidates = {
    format: FORMAT_CANDIDATE, voice: VOICE_CANDIDATE, tone: TONE_CANDIDATE, style: STYLE_CANDIDATE,
  }
  for (const axis of AXES) {
    const r = await runHarness(HARNESS.generate, { args: { axis, candidates: [candidates[axis]] } })
    for (const field of expected[axis]) {
      assert.ok(r.prompts[0].includes(field), `${axis}: prompt should ask for ${field}`)
    }
  }
  // domain is a format-only field (ADR 0010 section 2); it must not leak.
  for (const axis of ['voice', 'tone', 'style']) {
    const r = await runHarness(HARNESS.generate, { args: { axis, candidates: [candidates[axis]] } })
    assert.ok(!/\bdomain: /.test(r.prompts[0]), `${axis}: must not ask for a domain`)
  }
  // Tones and styles carry no family either.
  for (const axis of ['tone', 'style']) {
    const r = await runHarness(HARNESS.generate, { args: { axis, candidates: [candidates[axis]] } })
    assert.ok(!/\bfamily: /.test(r.prompts[0]), `${axis}: must not ask for a family`)
  }
})

test('generate.js resolves a cross-axis confusable neighbor to the right directory', async () => {
  // The style axis really does declare a format neighbor: `procedural` and
  // `diataxis-explanation` both list `technical-reference`.
  const r = await runHarness(HARNESS.generate, { args: { axis: 'style', candidates: [STYLE_CANDIDATE] } })
  const p = r.prompts[0]
  assert.ok(p.includes('taxonomy/styles/classical-argument/ENTRY.md'), 'same-axis neighbor should resolve in taxonomy/styles')
  assert.ok(p.includes('taxonomy/formats/technical-reference/ENTRY.md'), 'cross-axis neighbor should resolve in taxonomy/formats')
  // The id list written into frontmatter stays a flat list of bare ids.
  assert.ok(p.includes("confusable_with: ['classical-argument', 'technical-reference']"))
})

test('promote.js writes the sample key tools/promote.py reads, for every axis', async () => {
  for (const axis of AXES) {
    const r = await runHarness(HARNESS.render, { args: { axis, entries: ['fixture-entry'] } })
    assert.equal(r.prompts.length, 12, `${axis}: should render all 12 anchor topics`)
    const p = r.prompts[0]
    assert.ok(/Step 3: Write the file examples\/vertical-slices\/[a-z-]+\/(format|voice|tone|style)-fixture-entry\.md\./.test(p), `${axis}: wrong sample path`)
    assert.ok(p.includes(`${axis}-fixture-entry.md`), `${axis}: sample prefix must be the axis`)
    assert.ok(p.includes(`axis: ${axis}`), `${axis}: sample frontmatter axis not set`)
    assert.ok(p.includes(`Step 1: Read ${AXIS_DIR[axis]}/fixture-entry/ENTRY.md`), `${axis}: wrong entry path`)
  }
})

test('promote.js gives the non-format axes a sibling sample that exists on all 12 topics', async () => {
  for (const axis of ['voice', 'tone', 'style']) {
    const r = await runHarness(HARNESS.render, { args: { axis, entries: ['fixture-entry'] } })
    for (const p of r.prompts) {
      const ref = p.match(new RegExp(`^ {2}(examples/vertical-slices/[a-z-]+/${axis}-[a-z-]+\\.md)$`, 'm'))
      assert.ok(ref, `${axis}: no same-axis sibling sample offered`)
      assert.ok(existsSync(resolve(REPO_ROOT, ref[1])), `${axis}: sibling sample ${ref[1]} does not exist`)
    }
  }
})

test('promote.js stamps a configurable llm_model into every sample', async () => {
  const r = await runHarness(HARNESS.render, { args: { axis: 'voice', entries: ['x'], llmModel: 'claude-sonnet-5-5' } })
  for (const p of r.prompts) assert.ok(p.includes('llm_model: claude-sonnet-5-5'))
})

test('promote.js always reads the three format scenario anchors, which exist on all 12 topics', async () => {
  const r = await runHarness(HARNESS.render, { args: { axis: 'tone', entries: ['x'] } })
  for (const p of r.prompts) {
    for (const anchor of ['format-adr.md', 'format-readme.md', 'format-status-report.md']) {
      const m = p.match(new RegExp(`^ {2}(examples/vertical-slices/[a-z-]+/${anchor.replace('.', '\\.')})$`, 'm'))
      assert.ok(m, `missing scenario anchor ${anchor}`)
      assert.ok(existsSync(resolve(REPO_ROOT, m[1])), `scenario anchor ${m[1]} does not exist`)
    }
  }
})

test('dedup.js audits the right directory and uses cluster wording on the flat axes', async () => {
  for (const axis of AXES) {
    const groups = axis === 'format' ? undefined : [DEDUP_GROUP_TONE]
    const r = await runHarness(HARNESS.dedup, { args: { axis, groups } })
    assert.equal(r.prompts.length, 1)
    const p = r.prompts[0]
    assert.ok(p.includes(AXIS_DIR[axis] + '/'), `${axis}: members not read from the axis directory`)
    const word = axis === 'format' || axis === 'voice' ? 'family' : 'cluster'
    assert.ok(p.includes(`Within each ${word},`), `${axis}: should group by ${word}`)
    assert.ok(p.includes(`a near-duplicate with a ${axis} NOT in your list`), `${axis}: axis noun not substituted`)
  }
})

// ---------------------------------------------------------------------------
// 4. An unknown axis fails loudly rather than writing into the wrong tree
// ---------------------------------------------------------------------------

test('every harness rejects an unknown axis', async () => {
  for (const [name, file] of Object.entries(HARNESS)) {
    await assert.rejects(
      () => runHarness(file, { args: { axis: 'formats' } }),
      /unknown axis "formats"/,
      `${name}: should reject an unknown axis`,
    )
  }
})
