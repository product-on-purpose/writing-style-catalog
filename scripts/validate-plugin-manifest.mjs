#!/usr/bin/env node
// validate-plugin-manifest.mjs - zero-dependency plugin manifest validator.
//
// Asserts that the canonical plugin manifest (library.json, the family
// Standard's Section 5 artifact), the Claude Code native manifest
// (.claude-plugin/plugin.json, kept consistent with library.json by hand),
// and every skill's SKILL.md frontmatter are well-formed and agree with each
// other and with the components on disk, so a malformed or drifted manifest
// is caught here (and in the required `validate` CI job) rather than at the
// product-on-purpose registry's installability gate. Also asserts that no
// embedded self-listing marketplace reappears (the Standard's Section 12
// anti-pattern; the external product-on-purpose/agent-plugins registry is the
// one source of listing truth).
//
// Uses only Node built-ins (the repo has no root package.json, so there is no
// npm install step in CI).
//
// Usage:  node scripts/validate-plugin-manifest.mjs [--expect-version X.Y.Z]
//   --expect-version  also assert the manifest version equals X.Y.Z (used on a
//                     v* tag push so the tag and the manifest cannot diverge).

import { readFileSync, existsSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const ROOT = join(dirname(fileURLToPath(import.meta.url)), "..");
const PLUGIN_NAME = "writing-style-catalog";
const SEMVER_RE = /^\d+\.\d+\.\d+$/;
const TIERS = ["universal", "convergent", "advanced"];
const STATUSES = ["active", "deprecated", "experimental"];

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

// Minimal frontmatter reader: returns { name, description, metadataVersion }
// from a SKILL.md, or null when the frontmatter block is missing.
function readSkillFrontmatter(absPath) {
  const text = readFileSync(absPath, "utf8");
  const fm = text.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!fm) return null;
  const body = fm[1];
  const name = body.match(/^name:\s*(\S.*)$/m)?.[1]?.trim() ?? null;
  const description = body.match(/^description:\s*(\S.*)$/m)?.[1]?.trim() ?? null;
  let metadataVersion = null;
  if (/^metadata:\s*$/m.test(body)) {
    metadataVersion =
      body.match(/^[ \t]+version:\s*["']?([^"'\s]+)["']?\s*$/m)?.[1] ?? null;
  }
  return { name, description, metadataVersion };
}

// --- library.json: the canonical manifest (family Standard, Section 5) ---
const library = readJson("library.json");
if (library) {
  for (const field of ["name", "version", "description", "standard", "tier"]) {
    if (typeof library[field] !== "string" || library[field].trim() === "") {
      fail(`library.json: field \`${field}\` must be a non-empty string`);
    }
  }
  if (library.name !== PLUGIN_NAME) {
    fail(`library.json: name must be "${PLUGIN_NAME}" (got ${JSON.stringify(library.name)})`);
  }
  if (typeof library.version === "string" && !SEMVER_RE.test(library.version)) {
    fail(`library.json: version must be SemVer X.Y.Z (got ${JSON.stringify(library.version)})`);
  }
  if (typeof library.tier === "string" && !TIERS.includes(library.tier)) {
    fail(`library.json: tier must be one of ${TIERS.join("|")} (got ${JSON.stringify(library.tier)})`);
  }
  if (expectVersion && library.version !== expectVersion) {
    fail(`library.json: version ${JSON.stringify(library.version)} does not match expected ${JSON.stringify(expectVersion)}`);
  }
  // Component index: every entry's path/name/version/status must match disk.
  const skills = library.components?.skills;
  if (!Array.isArray(skills) || skills.length === 0) {
    fail("library.json: components.skills must be a non-empty array");
  } else {
    for (const entry of skills) {
      const label = `library.json: components.skills[${JSON.stringify(entry?.name)}]`;
      if (typeof entry?.name !== "string" || entry.name.trim() === "") {
        fail(`${label}: \`name\` must be a non-empty string`);
        continue;
      }
      if (typeof entry.path !== "string" || !existsSync(join(ROOT, entry.path))) {
        fail(`${label}: path ${JSON.stringify(entry.path)} does not exist on disk`);
        continue;
      }
      if (!SEMVER_RE.test(entry.version ?? "")) {
        fail(`${label}: version must be SemVer X.Y.Z (got ${JSON.stringify(entry.version)})`);
      }
      if (!TIERS.includes(entry.tier)) {
        fail(`${label}: tier must be one of ${TIERS.join("|")} (got ${JSON.stringify(entry.tier)})`);
      }
      if (!STATUSES.includes(entry.status)) {
        fail(`${label}: status must be one of ${STATUSES.join("|")} (got ${JSON.stringify(entry.status)})`);
      }
      const dirName = entry.path.split("/").at(-2);
      if (dirName !== entry.name) {
        fail(`${label}: parent directory ${JSON.stringify(dirName)} must equal the component name`);
      }
      const fmData = readSkillFrontmatter(join(ROOT, entry.path));
      if (!fmData) {
        fail(`${label}: ${entry.path} has no YAML frontmatter`);
      } else {
        if (fmData.name !== entry.name) {
          fail(`${label}: frontmatter name ${JSON.stringify(fmData.name)} must equal the component name`);
        }
        if (fmData.metadataVersion !== entry.version) {
          fail(`${label}: frontmatter metadata.version ${JSON.stringify(fmData.metadataVersion)} must equal the manifest version ${JSON.stringify(entry.version)}`);
        }
      }
    }
  }
}

// --- plugin.json: the Claude Code native manifest must agree with library.json ---
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
  if (library) {
    for (const field of ["name", "version", "description"]) {
      if (plugin[field] !== library[field]) {
        fail(`plugin.json: \`${field}\` has drifted from library.json (plugin.json ${JSON.stringify(plugin[field])} != library.json ${JSON.stringify(library[field])})`);
      }
    }
  }
}

// --- no embedded self-listing marketplace (Standard Section 12 anti-pattern) ---
if (existsSync(join(ROOT, ".claude-plugin/marketplace.json"))) {
  fail(
    ".claude-plugin/marketplace.json must not exist: the plugin is listed solely in the external product-on-purpose/agent-plugins registry (removed per the Standard's Section 12; see CHANGELOG)"
  );
}

// --- every skill's SKILL.md must carry name + description + metadata.version,
//     and its name must equal its parent directory (Bronze: name == dir) ---
const skillsDir = join(ROOT, "skills");
if (existsSync(skillsDir)) {
  for (const name of readdirSync(skillsDir)) {
    const skillMd = join(skillsDir, name, "SKILL.md");
    if (!existsSync(skillMd)) continue;
    const fmData = readSkillFrontmatter(skillMd);
    if (!fmData) {
      fail(`skills/${name}/SKILL.md: missing YAML frontmatter`);
      continue;
    }
    if (!fmData.name) fail(`skills/${name}/SKILL.md: frontmatter missing \`name\``);
    if (!fmData.description) fail(`skills/${name}/SKILL.md: frontmatter missing \`description\``);
    if (fmData.name && fmData.name !== name) {
      fail(`skills/${name}/SKILL.md: frontmatter name ${JSON.stringify(fmData.name)} must equal the directory name "${name}"`);
    }
    if (!fmData.metadataVersion || !SEMVER_RE.test(fmData.metadataVersion)) {
      fail(`skills/${name}/SKILL.md: frontmatter metadata.version must be SemVer X.Y.Z (got ${JSON.stringify(fmData.metadataVersion)})`);
    }
  }
}

if (errors.length === 0) {
  console.log("=== plugin manifest valid: all checks passed ===");
  process.exit(0);
}
for (const e of errors) console.error(`[FAIL] ${e}`);
console.error(`\n=== plugin manifest INVALID: ${errors.length} failing check(s) ===`);
process.exit(1);
