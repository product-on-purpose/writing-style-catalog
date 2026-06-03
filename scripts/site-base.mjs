// site-base.mjs - the single source for this site's GitHub Pages base path.
//
// Clause 14.7: the base literal lives exactly once, in site/astro.config.mjs.
// Any validator that needs the base (check-rendered-links.mjs resolves
// base-absolute hrefs against it) MUST derive it from that one source rather than
// redeclare the literal: a second copy can drift, and a wrong base makes the link
// check pass while the live site 404s. So this helper reads the base out of
// site/astro.config.mjs at runtime.
//
// (pm-skills, the donor of the link validators, hardcodes BASE = '/pm-skills' in
// check-rendered-links.mjs with a "keep in sync" comment; that duplicate is the
// family's one live 14.7 violation. This port deliberately avoids importing it.)

import { readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const CONFIG = path.join(ROOT, 'site', 'astro.config.mjs');

// Return the configured base with a leading slash and no trailing slash, e.g.
// '/writing-style-catalog'. The (^|\s)base: anchor avoids matching `baseUrl:`
// (editLink) or a `base` substring inside a longer key. Throws if the base cannot
// be found, so a refactor that renames or removes it fails loudly here instead of
// silently checking links against the wrong base.
export function siteBase() {
  const cfg = readFileSync(CONFIG, 'utf8');
  const m = cfg.match(/(^|\s)base:\s*(['"])(.*?)\2/);
  if (!m) {
    throw new Error(`site-base: could not find a base literal in ${CONFIG}`);
  }
  let base = m[3].trim();
  if (!base.startsWith('/')) base = '/' + base;
  return base.replace(/\/+$/, '');
}
