#!/usr/bin/env node
// check-no-dashes.mjs - fail if any tracked authored text file contains an
// em-dash (U+2014) or en-dash (U+2013). House rule (family + this repo): use a
// plain hyphen, " - ", or restructure. This is the CI enforcement of the
// .pre-commit-config.yaml no-em-dashes hook: a contributor who bypasses
// pre-commit (git commit --no-verify) can otherwise land a dash, because the
// pre-commit hook is local and advisory while CI is the gate.
//
// The forbidden characters are built from their code points, so this checker
// never embeds the literals it bans - it passes its own scan and the pre-commit
// hook.
//
// Scope: tracked files (via `git ls-files`, so the gitignored generated catalog,
// node_modules, and dist are excluded by construction) whose extension is an
// authored-text or first-party source type, minus docs/internal/ and _LOCAL/.
//
// docs/internal/ is excluded NOT because house style spares it (it does not - the
// ADRs and plan docs there are team-authored prose the rule governs), but because
// its markdown is already dash-scanned by tools/validate.py (check_no_em_dashes,
// which rglobs taxonomy/, examples/, docs/, and the site content root) in the same
// CI workflow; excluding it here avoids redundant coverage and the trap of failing
// CI on an imported reference artifact this repo is told not to modify. _LOCAL/ is
// gitignored research scratch. This check adds the coverage validate.py lacks:
// repo-root .md (README, AGENTS.md, CONTRIBUTING.md, ...) and the source/config
// types (.mjs/.ts/.astro/.css/.yml/.py), so the house rule reaches script and
// tooling source, not just rendered docs.
//
// Usage: node scripts/check-no-dashes.mjs
// Exit:  0 = clean; 1 = one or more dashes found.

import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const EM_DASH = String.fromCharCode(0x2014);
const EN_DASH = String.fromCharCode(0x2013);
const SCAN = /\.(md|mdx|mjs|ts|astro|css|ya?ml|py)$/;
const SKIP_PREFIX = ['docs/internal/', '_LOCAL/'];

function trackedFiles() {
  const out = execFileSync('git', ['ls-files'], { cwd: ROOT, encoding: 'utf8' });
  return out.split('\n').map((s) => s.trim()).filter(Boolean);
}

const hits = [];
for (const rel of trackedFiles()) {
  if (!SCAN.test(rel)) continue;
  if (SKIP_PREFIX.some((p) => rel.startsWith(p))) continue;
  let text;
  try {
    text = readFileSync(path.join(ROOT, rel), 'utf8');
  } catch {
    continue;
  }
  if (text.includes(EM_DASH) || text.includes(EN_DASH)) hits.push(rel);
}

console.log('=== Em/en-dash check ===');
if (hits.length === 0) {
  console.log('PASS: no em-dashes (U+2014) or en-dashes (U+2013) in tracked authored text.');
  process.exit(0);
}
console.log(`FAIL: ${hits.length} file(s) contain an em-dash or en-dash; use a hyphen, " - ", or restructure:`);
for (const h of hits) console.log(`  ${h}`);
process.exit(1);
