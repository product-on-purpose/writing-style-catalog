// Tests for scripts/gen-site.mjs (the zero-dependency Node site generator).
// Run: node --test tests/gen-site.test.mjs
//
// Replaces the former Python tests/test_generate_site_pages.py. Covers the
// hand-rolled YAML-subset parser, relative-link computation (no base literal),
// the DiffPair import depth for the site/src/content/docs location, the MDX
// prose escaper, the diff-pair section split, and end-to-end page counts.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

import {
  relUrl,
  parseFrontmatter,
  loadMarkdown,
  mdxEscapeProse,
  parseDiffPair,
  assertSafeOutRoot,
  generate,
} from '../scripts/gen-site.mjs';

const SCRIPT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', 'scripts', 'gen-site.mjs');

test('relUrl computes correct relative inter-page links', () => {
  // sibling axis under reference/
  assert.equal(relUrl('reference/voices/coach', 'reference/tones/warm'), '../../tones/warm/');
  // index page down to an entry
  assert.equal(relUrl('reference', 'reference/voices/coach'), 'voices/coach/');
  // diff-pair index to a diff-pair page
  assert.equal(relUrl('examples/diff-pairs', 'examples/diff-pairs/foo'), 'foo/');
  // entry page to a template (different top-level section)
  assert.equal(relUrl('reference/voices/coach', 'templates/adr'), '../../../templates/adr/');
  // template page back to its reference entry
  assert.equal(relUrl('templates/adr', 'reference/formats/adr'), '../../reference/formats/adr/');
  // child to ancestor index
  assert.equal(relUrl('examples/diff-pairs/foo', 'examples/diff-pairs'), '../');
});

test('parseFrontmatter handles literal block scalars', () => {
  const fm = parseFrontmatter('a: |\n  line one\n  line two\nb: scalar');
  assert.equal(fm.a, 'line one\nline two');
  assert.equal(fm.b, 'scalar');
});

test('parseFrontmatter handles block lists incl. quoted items with colons', () => {
  const fm = parseFrontmatter("xs:\n  - one\n  - two\nq:\n  - 'a: b \"c\"'");
  assert.deepEqual(fm.xs, ['one', 'two']);
  assert.deepEqual(fm.q, ['a: b "c"']);
});

test('parseFrontmatter does not swallow the key after a nested map', () => {
  const fm = parseFrontmatter('m:\n  k: v\n  j: w\nnext: x');
  assert.deepEqual(fm.m, { k: 'v', j: 'w' });
  assert.equal(fm.next, 'x');
});

test('parseFrontmatter keeps colons inside an inline scalar value', () => {
  const fm = parseFrontmatter('one_liner: A thing: with a colon');
  assert.equal(fm.one_liner, 'A thing: with a colon');
});

test('loadMarkdown normalizes CRLF and splits body', () => {
  const [fm, body] = loadMarkdown('---\r\nid: x\r\n---\r\n## Title\r\n\r\nText.\r\n');
  assert.equal(fm.id, 'x');
  assert.equal(body, '## Title\n\nText.\n');
});

test('mdxEscapeProse escapes < and { outside code, preserves code spans', () => {
  assert.equal(mdxEscapeProse('a < b {c}'), 'a &lt; b &lbrace;c}');
  assert.equal(mdxEscapeProse('keep `x < y` span'), 'keep `x < y` span');
});

test('parseDiffPair splits boundary sections and strips rule separators', () => {
  const raw = [
    '---',
    'diff_pair_id: t-a-vs-b',
    'entry_a: a',
    'entry_b: b',
    'axis_varied: tone',
    'topic_label: T',
    '---',
    '',
    '## What to notice',
    '',
    'notice text',
    '',
    '---',
    '',
    '## A: `a`',
    '',
    'passage a body',
    '',
    '---',
    '',
    '## B: `b`',
    '',
    'passage b body',
    '',
  ].join('\n');
  const dp = parseDiffPair(raw);
  assert.equal(dp.entry_a, 'a');
  assert.equal(dp.entry_b, 'b');
  assert.equal(dp.diff_pair_id, 't-a-vs-b');
  assert.equal(dp.what_to_notice, 'notice text');
  assert.equal(dp.passage_a, 'passage a body');
  assert.equal(dp.passage_b, 'passage b body');
});

test('generate emits the expected page set with relative links and no base literal', () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'gen-site-'));
  const count = generate(tmp);
  // The v0.1.0 baseline generated 92 pages (60 entries + 12 diff-pairs +
  // 5 recipes + 15 templates). The catalog grows release over release, so
  // assert the floor rather than a point count that goes stale with every
  // added entry.
  assert.ok(count >= 92, `expected at least 92 generated pages, got ${count}`);

  const coach = fs.readFileSync(path.join(tmp, 'reference/voices/coach.mdx'), 'utf8');
  assert.match(coach, /import \{ Tabs, TabItem \} from '@astrojs\/starlight\/components';/);
  // xref links are relative (no base, no leading slash on the target)
  assert.match(coach, /\]\(\.\.\/\.\.\/tones\/warm\/\)/);

  // A diff-pair page imports DiffPair at the site/src/content/docs depth.
  const dpDir = path.join(tmp, 'examples/diff-pairs');
  const dpFile = fs.readdirSync(dpDir).find((f) => f.endsWith('.mdx'));
  const dp = fs.readFileSync(path.join(dpDir, dpFile), 'utf8');
  assert.match(dp, /import DiffPair from '\.\.\/\.\.\/\.\.\/\.\.\/components\/DiffPair\.astro';/);

  // No generated file bakes the Pages base literal (clause 14.7).
  const walk = (d) =>
    fs.readdirSync(d).flatMap((n) => {
      const f = path.join(d, n);
      return fs.statSync(f).isDirectory() ? walk(f) : [f];
    });
  for (const f of walk(tmp)) {
    assert.equal(fs.readFileSync(f, 'utf8').includes('/writing-style-catalog'), false, `base literal leaked into ${f}`);
  }
  fs.rmSync(tmp, { recursive: true, force: true });
});

test('the generator source contains no hardcoded base literal', () => {
  const src = fs.readFileSync(SCRIPT, 'utf8');
  assert.equal(src.includes('/writing-style-catalog'), false);
});

test('parseFrontmatter parses inline (flow) lists', () => {
  assert.deepEqual(parseFrontmatter('pairs_well_with: [warm, candid]').pairs_well_with, ['warm', 'candid']);
  assert.deepEqual(parseFrontmatter('xs: []').xs, []);
});

test('parseFrontmatter folds > scalars (newlines to spaces, blank line breaks)', () => {
  assert.equal(parseFrontmatter('o: >\n  line one\n  line two').o, 'line one line two');
  assert.equal(parseFrontmatter('o: >\n  para one\n\n  para two').o, 'para one\n\npara two');
});

test('assertSafeOutRoot refuses output roots that would delete source', () => {
  const repoRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
  // The repo root, a source dir, and clearing-collides-with-source all refused.
  assert.throws(() => assertSafeOutRoot(repoRoot), /refusing to generate/i);
  assert.throws(() => assertSafeOutRoot(path.join(repoRoot, 'examples')), /refusing to generate/i);
  assert.throws(() => assertSafeOutRoot(path.join(repoRoot, 'taxonomy')), /refusing to generate/i);
  // The default site content root and a throwaway temp dir are allowed.
  assert.doesNotThrow(() => assertSafeOutRoot(path.join(repoRoot, 'site', 'src', 'content', 'docs')));
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'gen-safe-'));
  assert.doesNotThrow(() => assertSafeOutRoot(tmp));
  fs.rmSync(tmp, { recursive: true, force: true });
});

test('generate clears stale generated files before writing', () => {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'gen-clean-'));
  const stale = path.join(tmp, 'reference', 'voices', 'zzz-stale.mdx');
  fs.mkdirSync(path.dirname(stale), { recursive: true });
  fs.writeFileSync(stale, 'stale', 'utf8');
  generate(tmp);
  assert.equal(fs.existsSync(stale), false, 'stale generated file should be removed');
  assert.equal(fs.existsSync(path.join(tmp, 'reference', 'voices', 'coach.mdx')), true);
  fs.rmSync(tmp, { recursive: true, force: true });
});

// ---------------------------------------------------------------------------
// scripts/gen-reference.mjs - Markdown table-cell escaping
//
// The generated schema reference puts each field's `description` into a table
// cell, so an unescaped pipe would break out of the cell. The first draft
// escaped pipes but not backslashes, which CodeQL flagged
// (js/incomplete-sanitization) and which is a real defect: a description ending
// in a backslash before a pipe still produced a cell break, because the
// backslash escaped the escape.
//
// Order is the whole fix. Backslashes first, then pipes; the reverse re-escapes
// the backslashes just added.
// ---------------------------------------------------------------------------

const escapeCell = (s) =>
  s.replace(/\s+/g, ' ').replace(/\\/g, '\\\\').replace(/\|/g, '\\|').trim();

// True when an ODD number of backslashes precedes a pipe, i.e. the pipe is live.
const hasLivePipe = (s) => /(^|[^\\])(\\\\)*\|/.test(s);

test('gen-reference: table escaping leaves no live pipe', () => {
  for (const probe of [
    'plain text',
    'has | pipe',
    'ends with backslash \\',
    'backslash then pipe \\|',
    'many \\\\| pipes || here',
  ]) {
    assert.equal(hasLivePipe(escapeCell(probe)), false, `live pipe survived: ${probe}`);
  }
});

test('gen-reference: escaping pipes alone is insufficient (the flagged bug)', () => {
  const pipeOnly = (s) => s.replace(/\s+/g, ' ').replace(/\|/g, '\\|').trim();
  // The exact shape CodeQL objected to: a trailing backslash neutralises the
  // escape the old version added, leaving the pipe live.
  assert.equal(hasLivePipe(pipeOnly('backslash then pipe \\|')), true);
  assert.equal(hasLivePipe(escapeCell('backslash then pipe \\|')), false);
});

test('gen-reference: escaping collapses newlines so a cell cannot end its row', () => {
  assert.equal(escapeCell('line one\nline two'), 'line one line two');
});

test('gen-reference: writes both pages into a clean tree', () => {
  // Deliberately NOT a staleness check. The reference pages are gitignored
  // generated output, regenerated on every build alongside the catalog pages,
  // so "the committed pages have drifted" is not a state that can exist. An
  // earlier version of this test asserted exactly that and passed locally only
  // because the pages happened to be present; CI, checking out clean, was
  // correct to fail it.
  const res = spawnSync(
    process.execPath,
    [path.resolve(path.dirname(SCRIPT), 'gen-reference.mjs')],
    { encoding: 'utf8' }
  );
  assert.equal(res.status, 0, `gen-reference failed:\n${res.stdout}${res.stderr}`);

  const outDir = path.resolve(
    path.dirname(SCRIPT), '..', 'site', 'src', 'content', 'docs', 'reference'
  );
  for (const name of ['schema.md', 'scripts.md']) {
    const body = fs.readFileSync(path.join(outDir, name), 'utf8');
    assert.match(body, /^---\ntitle: /, `${name} needs Starlight frontmatter`);
    assert.match(body, /GENERATED by scripts\/gen-reference\.mjs/, `${name} needs the banner`);
  }
  // The schema page must reflect the real contract, not a stale copy of it.
  const schemaPage = fs.readFileSync(path.join(outDir, 'schema.md'), 'utf8');
  assert.match(schemaPage, /entry\.universal\.schema\.json/);
  assert.match(schemaPage, /llm_instruction_phrasing/, 'a required field is missing');
});
