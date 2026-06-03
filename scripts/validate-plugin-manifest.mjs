#!/usr/bin/env node
// validate-plugin-manifest.mjs - zero-dependency plugin manifest validator.
//
// Asserts that the Claude Code plugin manifest, the self-hosted single-plugin
// marketplace, and every skill's SKILL.md frontmatter are well-formed, so a
// malformed manifest is caught here (and in the required `validate` CI job)
// rather than at the product-on-purpose registry's installability gate.
//
// Uses only Node built-ins (the repo has no root package.json, so there is no
// npm install step in CI).
//
// Usage:  node scripts/validate-plugin-manifest.mjs [--expect-version X.Y.Z]
//   --expect-version  also assert plugin.json version equals X.Y.Z (used on a
//                     v* tag push so the tag and the manifest cannot diverge).

import { readFileSync, existsSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const PLUGIN_NAME = "writing-style-catalog";
const SEMVER_RE = /^\d+\.\d+\.\d+$/;

const errors = [];
const fail = (msg) => errors.push(msg);

// --expect-version flag (optional).
let expectVersion = null;
const flagIdx = process.argv.indexOf("--expect-version");
if (flagIdx !== -1) expectVersion = process.argv[flagIdx + 1];

function readJson(relPath) {
  const abs = join(ROOT, relPath);
  if (!existsSync(abs)) {
    fail(`missing ${relPath}`);
    return null;
  }
  try {
    return JSON.parse(readFileSync(abs, "utf8"));
  } catch (e) {
    fail(`${relPath} is not valid JSON: ${e.message}`);
    return null;
  }
}

// --- plugin.json ---
const plugin = readJson(".claude-plugin/plugin.json");
if (plugin) {
  for (const field of ["name", "version", "description", "homepage", "repository", "license"]) {
    if (typeof plugin[field] !== "string" || plugin[field].trim() === "") {
      fail(`plugin.json: field \`${field}\` must be a non-empty string`);
    }
  }
  if (plugin.name !== PLUGIN_NAME) {
    fail(`plugin.json: name must be "${PLUGIN_NAME}" (got ${JSON.stringify(plugin.name)})`);
  }
  if (typeof plugin.version === "string" && !SEMVER_RE.test(plugin.version)) {
    fail(`plugin.json: version must be SemVer X.Y.Z (got ${JSON.stringify(plugin.version)})`);
  }
  if (!plugin.author || typeof plugin.author.name !== "string" || plugin.author.name.trim() === "") {
    fail("plugin.json: author.name is required");
  }
  if (!Array.isArray(plugin.keywords) || plugin.keywords.length === 0) {
    fail("plugin.json: keywords must be a non-empty array");
  }
  if (expectVersion && plugin.version !== expectVersion) {
    fail(`plugin.json: version ${JSON.stringify(plugin.version)} does not match expected ${JSON.stringify(expectVersion)}`);
  }
}

// --- self-hosted marketplace.json: the single plugin entry must agree with plugin.json ---
const market = readJson(".claude-plugin/marketplace.json");
if (market && plugin) {
  const entry = Array.isArray(market.plugins)
    ? market.plugins.find((p) => p && p.name === PLUGIN_NAME)
    : null;
  if (!entry) {
    fail(`marketplace.json: no plugins[] entry named "${PLUGIN_NAME}"`);
  } else {
    if (entry.version !== plugin.version) {
      fail(`marketplace.json: entry version ${JSON.stringify(entry.version)} != plugin.json version ${JSON.stringify(plugin.version)}`);
    }
    if (!entry.source || typeof entry.source !== "object") {
      fail("marketplace.json: entry.source must be an object");
    }
  }
}

// --- every skill's SKILL.md must carry name + description frontmatter ---
const skillsDir = join(ROOT, "skills");
if (existsSync(skillsDir)) {
  for (const name of readdirSync(skillsDir)) {
    const skillMd = join(skillsDir, name, "SKILL.md");
    if (!existsSync(skillMd)) continue;
    const text = readFileSync(skillMd, "utf8");
    const fm = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
    if (!fm) {
      fail(`skills/${name}/SKILL.md: missing YAML frontmatter`);
      continue;
    }
    const body = fm[1];
    if (!/^name:\s*\S/m.test(body)) fail(`skills/${name}/SKILL.md: frontmatter missing \`name\``);
    if (!/^description:\s*\S/m.test(body)) fail(`skills/${name}/SKILL.md: frontmatter missing \`description\``);
  }
}

if (errors.length === 0) {
  console.log("=== plugin manifest valid: all checks passed ===");
  process.exit(0);
}
for (const e of errors) console.error(`[FAIL] ${e}`);
console.error(`\n=== plugin manifest INVALID: ${errors.length} failing check(s) ===`);
process.exit(1);
