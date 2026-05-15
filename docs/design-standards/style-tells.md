# Style Tells to Avoid

A "style tell" is a writing pattern that signals low-effort or LLM-generated content. The catalog has explicit positions on which tells to avoid in entry prose, body copy, and examples. Some are enforced by tooling; others are editorial.

This page is the reference list. Some tells are universal (always avoid); others depend on context (avoid in entry prose but acceptable in examples that demonstrate informal voices).

---

## Enforced by tooling

### Em-dashes and en-dashes

The characters U+2014 (em-dash) and U+2013 (en-dash) are forbidden anywhere in the repo. Use " - " (space-hyphen-space) instead. Restructuring the sentence is usually a better fix than the substitution.

The rule is enforced by a pre-commit hook and by the `validate.py` linter. The reasoning is captured in ADR-0005: em-dashes are the most reliable indicator of LLM-generated prose, and consistent hyphen use across the repo signals deliberate authorship.

This rule has no exceptions. Even quoted text and pasted templates get cleaned up.

---

## Universally avoided

### Trifold padding

The pattern "not just X, but Y, and Z" rarely earns its three beats. Most uses can be cut to one of the three terms without losing content. When all three are needed, restructure into a normal sentence or a list.

### Hedged enthusiasm

Phrases like "really exciting opportunity," "incredibly powerful tool," "deeply meaningful work" do no work in technical or professional prose. They tell the reader to feel something rather than letting the content earn the feeling.

The fix: cut the adverb-adjective stack. Either the noun stands on its own ("opportunity," "tool," "work") or the prose has not made the case yet.

### Generic adjective bundles

Watch for clusters of adjectives that pattern as filler: "seamlessly," "robust," "powerful," "elegant," "transformative." Each of these can be the right word in a specific sentence; the tell is when they appear in clusters with no specific content backing them up.

The fix: replace the adjective with the specific fact that earns it. "Seamless" becomes "no manual configuration required."

### Opener cliches

"In today's fast-paced world," "more than ever before," "as we navigate the complexities of," and their relatives are signals that the writer has not figured out how to start. Cut the opener and begin with the first specific sentence.

### Buried lead

The most important sentence appears in paragraph three instead of paragraph one. This is a structural failure as much as a stylistic one. The entry's `description` field should put the load-bearing claim in the first sentence.

---

## Avoided in entry prose, acceptable in examples

These patterns are forbidden in entry bodies and the `description`, `one_liner`, and `llm_instruction_phrasing` fields. They are acceptable in example files when the example is demonstrating a voice or tone that uses them.

### Conspicuous personality

Wink emojis, exclamation points, "let's dive in," "buckle up." These belong in `playful` and `celebratory` examples, not in entry prose that defines what those tones are.

### Imperative urgency that the situation does not earn

"You MUST," "absolutely critical," "do not miss." Belongs in `urgent` tone examples when the situation actually is urgent. Does not belong in entry prose, where the urgency is performed rather than real.

### Personal anecdote

"When I was building..." or "I remember the first time..." Belongs in `columnist` voice examples. Does not belong in entry prose, which is documentation, not commentary.

---

## Specific to format and structure

### Tables of three when a sentence would do

A two-column table with two rows and "good vs bad" headers is almost always a sentence trying to look like a table. Use tables when there are at least four rows of structured data.

### Headers that summarize the next sentence

If the next sentence after the header restates the header, one of them is redundant. Cut the redundant one. Usually the header should stay and the sentence should jump straight to the content.

### Bullets without parallel structure

A bullet list where the first bullet is a noun phrase, the second is a full sentence, and the third is a question reads as if it was assembled from different drafts. Decide on the structure and apply it consistently within a list.

---

## When in doubt

Read the entry's `description` and `llm_instruction_phrasing` fields aloud. If you cannot say them without affectation, the prose has a tell that the page form is hiding. Rewrite until the spoken version sounds like a real person writing real documentation.

The catalog's authority is built one entry at a time. Tells erode it; specificity restores it.
