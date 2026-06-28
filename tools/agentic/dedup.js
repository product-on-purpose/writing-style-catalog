// tools/agentic/dedup.js - DE-DUP AUDIT harness (whole-corpus distinguishability gate)
//
// WHAT
//   A Workflow-tool script. Audits the catalog for thin distinctions and quality
//   issues by FAMILY CLUSTER - one auditor per cluster reads every member together
//   and flags any pair a careful reader could confuse, plus per-entry quality nits.
//
// WHY IT MATTERS
//   The per-entry generation gate only checks an entry against its ONE declared
//   confusable neighbor. Distinguishability is not local: two entries can each be
//   distinct from their declared neighbor yet be near-duplicates of each other, and
//   that collision is invisible to the per-entry gate (it is never run on the pair).
//   Auditing by family cluster - the taxonomic slot competitors actually share - is
//   the granularity that surfaces these cross-batch collisions. Run this after any
//   breadth program and before promotion; it materially de-risks draft->stable.
//
// HOW IT WORKS
//   For each cluster, one high-effort agent reads all member ENTRY.md files and
//   returns structured findings: flagged_pairs (a, b, same_family, severity, why,
//   fix) and quality_notes (entry, issue, fix). The orchestrator aggregates and
//   sorts by severity. Feed the fixes to tools/agentic/remediate.js, then re-gate
//   the medium/high collisions with a cross-vendor check.
//
// HOW TO RUN
//   1. Regenerate GROUPS from the CURRENT family map. Group every format by
//      domain/family (read frontmatter from taxonomy/formats/*/ENTRY.md; do NOT read
//      taxonomy.json - it is a slim index that omits confusable_with and nests
//      domain/family). Tag each member (S) stable or (D) draft for the auditor.
//   2. Invoke with the Workflow tool.
//   3. Apply fixes via remediate.js; re-run a focused cross-vendor check on the
//      medium/high pairs to confirm RESOLVED (gate -> remediate -> re-gate).

export const meta = {
  name: 'agentic-dedup-audit',
  description: 'Whole-corpus de-dup + quality audit, one auditor per family cluster',
  phases: [{ title: 'Audit', detail: 'one auditor per family-cluster flags thin distinctions + quality issues' }],
}

const ROOT = 'E:/Projects/product-on-purpose/writing-style-catalog'

// EDIT THIS: regenerate from the current family map. Each group is one or more
// family clusters; members carry (S)=stable / (D)=draft.
const GROUPS = [
  {
    id: 'example-cluster',
    families: {
      'professional/deliberation': ['adr (S)', 'prd (S)', 'design-doc (S)', 'rfc (S)'],
    },
  },
]

const CLUSTER_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  properties: {
    group: { type: 'string' },
    flagged_pairs: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: {
          a: { type: 'string' },
          b: { type: 'string' },
          same_family: { type: 'boolean' },
          severity: { type: 'string', enum: ['high', 'medium', 'low'] },
          why: { type: 'string', description: 'the specific overlapping lines/claims' },
          fix: { type: 'string', description: 'which entry to sharpen and how' },
        },
        required: ['a', 'b', 'same_family', 'severity', 'why', 'fix'],
      },
    },
    quality_notes: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        properties: { entry: { type: 'string' }, issue: { type: 'string' }, fix: { type: 'string' } },
        required: ['entry', 'issue', 'fix'],
      },
    },
    verdict: { type: 'string' },
  },
  required: ['group', 'flagged_pairs', 'quality_notes', 'verdict'],
}

function auditPrompt(g) {
  const famLines = Object.entries(g.families).map(([fam, members]) => '  - ' + fam + ': ' + members.join(', ')).join('\n')
  const ids = Object.values(g.families).flat().map((m) => m.split(' ')[0])
  const paths = ids.map((id) => 'taxonomy/formats/' + id + '/ENTRY.md').join('\n  ')
  return [
    'You are a de-duplication and quality auditor for the writing-style-catalog. Working directory: ' + ROOT + '.',
    '',
    'Audit this cluster (S = stable baseline, D = draft under review):',
    famLines,
    '',
    'READ ALL of these files in full before judging:',
    '  ' + paths,
    '',
    'CHECK 1 - DE-DUP (the main job). Within each family, every pair must be mutually distinguishable. The catalog was generated in batches where each entry was only checked against its ONE declared confusable neighbor, so same-family collisions may have slipped through. Flag a pair if a careful reader could not tell which entry produced a given piece of writing, OR the two would yield near-identical output for a realistic task, OR their descriptions/tells/templates substantially overlap. Give same_family, severity, the specific overlapping lines (why), and a concrete fix (which entry to sharpen, how). If you suspect a near-duplicate with a format NOT in your list, flag it with same_family=false and name it.',
    '',
    'CHECK 2 - QUALITY (quality_notes). Flag any single entry with: an internal inconsistency (a pairs_well_with id its own anti_pattern forbids), a weak or duplicative anti_pattern/failure_mode, a failure_mode that names a neighbor format instead of describing the format over-hitting its own register, or a canonical_template that does not match the description.',
    '',
    'CHECK 3 - INTEGRITY (quality_notes). Flag any fabricated statistic, invented named authority presented as real, or any em-dash (U+2014) / en-dash (U+2013).',
    '',
    'Be specific and conservative: only flag genuine problems. A subtle-but-real distinction the entries draw clearly is a PASS. Do not edit files - report only, via the structured output.',
  ].join('\n')
}

phase('Audit')
const results = await parallel(GROUPS.map((g) => () => agent(auditPrompt(g), { label: 'audit:' + g.id, phase: 'Audit', schema: CLUSTER_SCHEMA, effort: 'high' })))
const groups = results.filter(Boolean)
const rank = { high: 0, medium: 1, low: 2 }
const allPairs = groups.flatMap((r) => (r.flagged_pairs || []).map((p) => ({ ...p, group: r.group }))).sort((a, b) => rank[a.severity] - rank[b.severity])
const allQuality = groups.flatMap((r) => (r.quality_notes || []).map((q) => ({ ...q, group: r.group })))
log('audit: ' + allPairs.length + ' pair flags, ' + allQuality.length + ' quality flags across ' + groups.length + ' clusters')
return { clusters: groups.map((r) => ({ group: r.group, verdict: r.verdict })), flagged_pairs: allPairs, quality_notes: allQuality, totals: { pairs: allPairs.length, quality: allQuality.length, clusters: groups.length } }
