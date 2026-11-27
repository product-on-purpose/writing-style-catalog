// Shared inputs for the tools/agentic/* prompt tests.
//
// These fixtures are the frozen inputs the golden prompt files in
// tests/golden-outputs/agentic/ were captured from. The Format goldens were
// captured from the pre-axis-parameterization harnesses (the commit before the
// Stream-C axis generalization), so a byte-for-byte match proves the Format
// path still emits exactly the prompt it emitted before.
//
// Do NOT edit a fixture without recapturing the goldens it feeds, and do not
// recapture a Format golden from the current code: the whole point of the
// Format goldens is that they predate the change.

export const FORMAT_CANDIDATE = {
  id: 'fixture-format', name: 'Fixture Format', domain: 'professional', family: 'brief', dp: 'digital',
  one_liner: "A one-line description of what this format is.",
  concept: "Two to four sentences of what the format is and why it earns its place, ending with the contrast against its confusable neighbor.",
  pairs_well_with: ['technical-writer', 'matter-of-fact', 'executive-summary'],
  avoid_with: ['pastoral', 'playful'],
  confusable_with: ['one-pager'],
  typical_voices: ['technical-writer', 'executive'], typical_tones: ['matter-of-fact', 'confident'],
}

export const VOICE_CANDIDATE = {
  id: 'fixture-voice', name: 'Fixture Voice', family: 'care',
  one_liner: "A one-line description of what this voice is.",
  concept: "Two to four sentences of what the voice is and why it earns its place, ending with the contrast against its confusable neighbor.",
  pairs_well_with: ['warm', 'narrative-case-study'],
  avoid_with: ['urgent'],
  confusable_with: ['friendly-mentor'],
  diction: 'plain and unhurried', sentence_style: 'Long sentences that do not rush to a point',
  default_pov: 'first-person', typical_tones: ['warm', 'reverent'],
}

export const TONE_CANDIDATE = {
  id: 'fixture-tone', name: 'Fixture Tone',
  one_liner: "A one-line description of what this tone is.",
  concept: "Two to four sentences of what the tone is and why it earns its place, ending with the contrast against its confusable neighbor.",
  pairs_well_with: ['storyteller', 'narrative-case-study'],
  avoid_with: ['urgent'],
  confusable_with: ['celebratory'],
  spectrum: 'warmth', spectrum_position: 0.7, nn_g_profile: 'neutral',
}

export const STYLE_CANDIDATE = {
  id: 'fixture-style', name: 'Fixture Style',
  one_liner: "A one-line description of what this style is.",
  concept: "Two to four sentences of what the style is and why it earns its place, ending with the contrast against its confusable neighbor.",
  pairs_well_with: ['researcher', 'matter-of-fact'],
  avoid_with: ['playful'],
  confusable_with: ['classical-argument', { id: 'technical-reference', axis: 'format' }],
  frame: 'argumentative', classical_mode: 'argumentation',
}

// One render cell: (entry id, topic slug, topic label).
export const RENDER_CELL = ['fixture-format', 'async-standups', 'Whether the team should move to async-first standups']

export const DEDUP_GROUP = {
  id: 'fixture-cluster',
  families: {
    'professional/deliberation': ['adr (S)', 'prd (S)', 'design-doc (S)', 'rfc (S)'],
  },
}

export const DEDUP_GROUP_TONE = {
  id: 'fixture-tone-cluster',
  families: {
    'tone/warmth': ['warm (S)', 'empathetic (S)', 'celebratory (S)', 'fixture-tone (D)'],
  },
}
