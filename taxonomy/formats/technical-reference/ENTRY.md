---
id: technical-reference
name: Technical Reference
axis: format
domain: professional
family: instruction
one_liner: A stable lookup document designed for repeated return visits. Optimized for scanning over reading. The reader arrives with a specific question; the format serves that question.
description: |
  Technical reference is not written to be read start to finish. It is written to be consulted.
  The reader arrives with a specific question - what are the parameters for this function? what
  does this error mean? what are the valid values for this field? - and the reference document
  should answer that question in the fewest possible steps. Every structural decision in a
  technical reference document serves the returning reader, not the first-time reader. Headers
  are navigation. Tables beat prose for structured data. Examples beat explanation.

  The authority of a technical reference comes from its precision and stability. Precision means
  every statement is accurate and complete for its scope - not approximately right, not rounded
  for readability. Stability means the document changes only when the underlying system changes,
  not to improve the prose. A reader who bookmarks a section of a reference document is trusting
  that section to remain findable and accurate. That trust is the contract the format creates.

  Technical reference is distinct from tutorials and how-to guides. A tutorial walks a newcomer
  through a concept; a how-to guide walks a practitioner through a task. A reference document
  assumes the reader already knows what they want to do and needs the exact specification to
  do it. Mixing tutorial prose into a reference document - adding context, motivation, and
  explanation that the experienced reader will skip - is the most common way reference documents
  fail the readers who rely on them most.
canonical_template: |
  # [Component / Function / Concept Name]

  [One sentence: what this is and what it does. No background.]

  ## Syntax / Signature
  ```
  [Exact syntax or function signature]
  ```

  ## Parameters / Fields / Options
  | Name | Type | Required | Description |
  |------|------|----------|-------------|
  | [name] | [type] | [yes/no] | [concise description] |

  ## Returns / Output
  [What is returned or produced - type and structure]

  ## Examples
  ```[language]
  [Working minimal example]
  ```
  [Optional: second example showing edge case or variation]

  ## Notes / Constraints
  - [Important limitation, gotcha, or version note]

  ## See Also
  - [Related component or concept] - [link or cross-reference]
typical_voices:
  - technical-writer
  - pragmatic-architect
typical_tones:
  - matter-of-fact
  - instructional
digital_or_print: digital
pairs_well_with:
  - technical-writer
  - pragmatic-architect
  - matter-of-fact
  - instructional
  - diataxis-explanation
avoid_with:
  - columnist
  - pastoral
  - warm
  - playful
  - narrative-case-study
confusable_with:
  - diataxis-explanation
  - how-to-tutorial
when_to_use:
  - Documenting an API, library, CLI, or configuration schema that practitioners will consult repeatedly
  - Providing an authoritative specification for a component's inputs, outputs, and constraints
  - Reference material that experienced users navigate by scanning, not by reading
  - Documentation that must remain stable across software versions with explicit change notation
  - Content where precision and completeness matter more than readability or approachability
when_not_to_use:
  - Introducing a concept or technology to someone encountering it for the first time
  - Guiding a practitioner through a specific task step by step
  - Explaining the reasoning behind a design decision
  - Communication with non-technical stakeholders who need context, not specification
  - Documentation that will be read once and discarded
llm_instruction_phrasing: |
  Write as technical reference documentation. Optimize for scanning, not reading start to finish.
  Every section should be findable via its header. Use tables for structured data (parameters,
  options, fields). Lead each entry with a one-sentence definition - no background or motivation.
  Include at least one working code example. State constraints and limitations as explicit notes,
  not as caveats buried in prose. Do not explain why the system works this way - state precisely
  how it works. Assume the reader already knows what they want to do and needs the specification
  to do it.
tags:
  - reference
  - technical
  - api-docs
  - lookup
  - stable
  - scannable
  - digital
review_status: stable
---

## Technical Reference

Technical reference is not written to be read start to finish. It is written to be consulted. The reader arrives with a specific question - what are the parameters for this function? what does this error mean? what are the valid values for this field? - and the reference document should answer that question in the fewest possible steps. Every structural decision in a technical reference document serves the returning reader, not the first-time reader. Headers are navigation. Tables beat prose for structured data. Examples beat explanation.

The authority of a technical reference comes from its precision and stability. Precision means every statement is accurate and complete for its scope - not approximately right, not rounded for readability. Stability means the document changes only when the underlying system changes, not to improve the prose. A reader who bookmarks a section of a reference document is trusting that section to remain findable and accurate. That trust is the contract the format creates.

Technical reference is distinct from tutorials and how-to guides. A tutorial walks a newcomer through a concept; a how-to guide walks a practitioner through a task. A reference document assumes the reader already knows what they want to do and needs the exact specification to do it. Mixing tutorial prose into a reference document - adding context, motivation, and explanation that the experienced reader will skip - is the most common way reference documents fail the readers who rely on them most.

### Canonical template

```
# [Component / Function / Concept Name]

[One sentence: what this is and what it does. No background.]

## Syntax / Signature
```
[Exact syntax or function signature]
```

## Parameters / Fields / Options
| Name | Type | Required | Description |
|------|------|----------|-------------|
| [name] | [type] | [yes/no] | [concise description] |

## Returns / Output
[What is returned or produced - type and structure]

## Examples
```[language]
[Working minimal example]
```
[Optional: second example showing edge case or variation]

## Notes / Constraints
- [Important limitation, gotcha, or version note]

## See Also
- [Related component or concept] - [link or cross-reference]
```

### When to use

Technical reference belongs on any API, library, CLI tool, or configuration schema that practitioners consult repeatedly. Use it when the reader is experienced with the domain and arrives with a specific question, when precision and completeness matter more than approachability, and when the document needs to stay stable and findable across software versions.

### When not to use

Reference format is wrong for introducing someone to a concept for the first time, guiding a practitioner step by step through a task, or explaining the reasoning behind a design decision. It is also wrong for non-technical stakeholders who need context, and for one-time documentation that will not be consulted again.

### Pairs well with

`technical-writer`, `pragmatic-architect`, `matter-of-fact`, `instructional`, `diataxis-explanation`

### Often confused with

**diataxis-explanation**: A Diataxis explanation document teaches conceptual understanding - it is oriented toward learning and can include motivation, analogy, and context. A technical reference document is oriented toward lookup - it assumes understanding and prioritizes precision and scannability over explanation.

**how-to-tutorial**: A how-to guide walks a practitioner through a specific task with sequential steps toward a defined goal. A technical reference document is a stable specification that a practitioner consults while doing a task - it does not guide; it answers.
