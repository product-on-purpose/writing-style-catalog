---
id: resume
name: Resume
axis: format
domain: professional
family: brief
one_liner: "A structured, scannable record of a person's professional experience, skills, and qualifications."
description: |
  A resume is a structured, scannable record of a person's professional experience, skills, and
  qualifications, organized for a recruiter to assess fit in seconds. Its defining quality is
  compression: it presents the candidate's history in the most efficient form possible, organized
  into reverse-chronological roles, bulleted accomplishments, and labeled credential sections,
  so a screener can locate the signal without reading prose. The document exists to answer one
  question: does this person have the background this role requires?

  What the resume does not do is argue. It presents evidence. The cover letter makes the case in
  prose; the resume is the record the case draws on. A candidate who embeds persuasive rhetoric
  inside a resume's bullet structure has confused the two documents: the resume's authority comes
  from its factual density, not from its rhetoric. Narrative connective tissue - transitions,
  explanations, hedges - dilutes that density and signals the candidate does not understand the
  format's purpose.

  The structural conventions of a resume are conventions for a reason: recruiters and applicant
  tracking systems process hundreds of documents with learned pattern expectations. Consistent date
  formatting, parallel bullet syntax, and standard section headers (Experience, Education, Skills)
  are not stylistic preferences but contracts with the reader. Departing from them forces the
  reader to slow down, which a resume cannot afford.

  Typical length: 400-700 words for most professionals; one page for early career, two pages
  acceptable for ten or more years of relevant history.
canonical_template: |
  [Full Name]
  [Email] | [Phone] | [LinkedIn or Portfolio URL] | [City, State]

  ## Experience

  [Job Title] | [Company Name] | [Start Month Year - End Month Year or Present]
  - [Action verb + what you did + measurable result]
  - [Action verb + what you did + measurable result]
  - [Action verb + what you did + measurable result]

  [Job Title] | [Company Name] | [Start Month Year - End Month Year]
  - [Action verb + what you did + measurable result]
  - [Action verb + what you did + measurable result]

  ## Education

  [Degree], [Major] | [Institution] | [Graduation Year]

  ## Skills

  [Category]: [Skill 1], [Skill 2], [Skill 3]
typical_voices:
  - direct-communicator
  - executive
typical_tones:
  - matter-of-fact
  - confident
digital_or_print: both
pairs_well_with:
  - direct-communicator
  - executive
  - matter-of-fact
  - confident
  - executive-summary
avoid_with:
  - confessional
  - reverent
  - playful
confusable_with:
  - cover-letter
when_to_use:
  - Applying for a job posting where a resume is requested or expected by the employer or recruiter
  - Submitting qualifications to a recruiter for initial screening before any conversation
  - Presenting credentials ahead of a networking meeting or informational interview when asked for background
  - Populating a professional portfolio or profile with a formal credentials document
  - Responding to any structured request for professional background that calls for a parseable, scannable form
when_not_to_use:
  - When a narrative framing of your work is needed - use a cover letter or bio instead
  - When initiating first contact with no posted opening and no shared context - the resume alone will not carry that ask
  - When the format requested is a CV, portfolio, or capability statement, which carry different structural conventions
tells:
  - 'Sections labeled with conventional headers: Experience, Education, Skills or close variants'
  - 'Reverse-chronological order within Experience: most recent role listed first'
  - 'Bullet points begin with past-tense action verbs; no subject pronoun ("I" or "We") in the bullets'
  - 'Dates formatted consistently, appearing on every role line alongside the company and title'
  - 'No narrative transitions or connective prose between entries'
  - 'Accomplishments quantified where possible: percentages, dollar amounts, headcount, time frames'
  - 'Contact information block at the top; no salutation, no closing, no signature'
anti_patterns:
  - pattern: 'Writing duty descriptions ("Responsible for managing the pipeline") instead of accomplishment bullets ("Reduced pipeline cycle time 30% by restructuring the intake process")'
    why: 'Duty descriptions tell the recruiter what the job was, not what the candidate did in it. Every applicant who held the same title had those duties; specific accomplishments are what differentiate this candidate from the field.'
  - pattern: 'Replacing accomplishment bullets with narrative prose paragraphs in order to "stand out"'
    why: 'Narrative paragraphs break the scannability contract. A recruiter spending seconds on a resume cannot parse prose at speed; bullets beginning with action verbs let the eye find signal fast. Prose in a resume disrupts the format''s core function.'
  - pattern: 'Padding bullets with advocacy or fit language - phrases like "passionate about innovation" or "eager to contribute to a collaborative culture"'
    why: 'The resume is a factual record, not a persuasive argument. The cover letter makes the case in prose, arguing from the resume''s evidence toward a specific ask. Mixing advocacy into the record muddies both documents: the resume loses credibility as evidence, and the argument loses force because it is not structured to carry one.'
  - pattern: 'Using a functional or skills-first layout to obscure an employment gap or non-linear career path'
    why: 'Recruiters and applicant tracking systems recognize functional formats as a signal that something is being hidden, and many systems cannot parse non-chronological layouts at all. A brief, honest explanation in the cover letter handles gaps more credibly than a structural maneuver that raises the same question.'
failure_modes:
  - mode: 'Over-compresses until bullets become telegraphic fragments - "Led initiative, +18%" - with no recoverable context about what was led, what 18% measured, or why the result mattered'
    mitigation: 'Each bullet should carry three elements: the action, the context, and the result. A number without a story cannot be evaluated. Expand the bullet until a reader who does not know the candidate can place the achievement.'
  - mode: 'Quantification overdrive - every bullet forces a metric even where none is meaningful, producing noise like "Attended 12 team meetings" or "Responded to 100% of emails within 24 hours"'
    mitigation: 'Quantify accomplishments where the number is evidence of scale or impact. A metric that does not distinguish a strong performer from a weak one adds noise rather than signal. Remove manufactured metrics; replace with qualitative specificity or a stronger accomplishment.'
  - mode: 'Structure dominance - the resume becomes a rigid taxonomy of labeled sections and sub-sections that fragments a coherent career into unconnected atoms, losing any sense of progression or throughline'
    mitigation: 'Structure is a service to the reader, not an end in itself. If a significant result or a non-obvious career move disappears inside perfect parallel formatting, a brief parenthetical or a reordered bullet can restore the throughline without breaking scannability.'
llm_instruction_phrasing: |
  Write as a resume. The output is a structured, scannable credentials document organized for a
  recruiter to assess fit in seconds. Use conventional section headers: Experience, Education,
  Skills (or close variants). In the Experience section, list roles in reverse-chronological order,
  most recent first. Write each accomplishment as a bullet beginning with a past-tense action verb;
  do not use a subject pronoun. Quantify results where the number is meaningful evidence of scale
  or impact; do not manufacture metrics. Write no narrative prose, no transitions, no rhetorical
  advocacy. The resume presents evidence; it does not argue. Persuasive claims and fit language
  belong in a cover letter, not here. Place contact information at the top. Hold to one page for
  early-career candidates, two pages for ten or more years of relevant history.
tags:
  - professional
  - hiring
  - credentials
  - job-search
  - structured-document
review_status: stable
---

## Resume

A resume is a structured, scannable record of a person's professional experience, skills, and qualifications, organized for a recruiter to assess fit in seconds. Its defining quality is compression: it presents the candidate's history in the most efficient form possible, organized into reverse-chronological roles, bulleted accomplishments, and labeled credential sections, so a screener can locate the signal without reading prose. The document exists to answer one question: does this person have the background this role requires?

What the resume does not do is argue. It presents evidence. The cover letter makes the case in prose; the resume is the record the case draws on. A candidate who embeds persuasive rhetoric inside a resume's bullet structure has confused the two documents: the resume's authority comes from its factual density, not from its rhetoric. Narrative connective tissue - transitions, explanations, hedges - dilutes that density and signals the candidate does not understand the format's purpose.

The structural conventions of a resume are conventions for a reason: recruiters and applicant tracking systems process hundreds of documents with learned pattern expectations. Consistent date formatting, parallel bullet syntax, and standard section headers (Experience, Education, Skills) are not stylistic preferences but contracts with the reader. Departing from them forces the reader to slow down, which a resume cannot afford.

### Canonical template

```
[Full Name]
[Email] | [Phone] | [LinkedIn or Portfolio URL] | [City, State]

## Experience

[Job Title] | [Company Name] | [Start Month Year - End Month Year or Present]
- [Action verb + what you did + measurable result]
- [Action verb + what you did + measurable result]

[Job Title] | [Company Name] | [Start Month Year - End Month Year]
- [Action verb + what you did + measurable result]
- [Action verb + what you did + measurable result]

## Education

[Degree], [Major] | [Institution] | [Graduation Year]

## Skills

[Category]: [Skill 1], [Skill 2], [Skill 3]
```

### When to use

Applying for a job posting where a resume is requested or expected by the employer or recruiter; submitting qualifications to a recruiter for initial screening before any conversation; presenting credentials ahead of a networking meeting or informational interview when asked for background; populating a professional portfolio or profile with a formal credentials document; responding to any structured request for professional background that calls for a parseable, scannable form.

### When not to use

When a narrative framing of your work is needed - use a cover letter or bio instead; when initiating first contact with no posted opening and no shared context - the resume alone will not carry that ask; when the format requested is a CV, portfolio, or capability statement, which carry different structural conventions.

### Pairs well with

`direct-communicator`, `executive`, `matter-of-fact`, `confident`, `executive-summary`

### Often confused with

**cover-letter**: A cover letter is a letter accompanying an application that makes the case for one specific person for one specific role. It connects the applicant's experience to the posting's stated needs, in the applicant's own voice, and asks for the interview. Where a resume presents facts in parallel bullets organized for scanning, a cover letter argues from those facts in prose - mapping specific history onto specific job demands and closing with a direct request for the interview. The cover letter makes the case; the resume is the factual record the case draws on. The two documents work together: mixing persuasive argument into resume bullets, or listing credentials in a cover letter as though it were a second resume, weakens both.
