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

import {
  relUrl,
  parseFrontmatter,
  loadMarkdown,
  mdxEscapeProse,
  parseDiffPair,
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
  // 60 entries + 12 diff-pairs + 5 recipes + 15 templates = 92 counted pages.
  assert.equal(count, 92);

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
