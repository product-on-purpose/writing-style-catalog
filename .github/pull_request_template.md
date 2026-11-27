## Summary

<!-- What does this PR change, and why? Link the issue or entry proposal if one exists. -->

## Checklist (from CONTRIBUTING.md)

- [ ] `python tools/validate.py` passes with no errors
- [ ] `python -m pytest -q` passes
- [ ] No em-dashes (U+2014) or en-dashes (U+2013) in any file
- [ ] Commit messages follow Conventional Commits format

For new taxonomy entries additionally (see [The Entry Bar](https://github.com/product-on-purpose/writing-style-catalog/blob/main/CONTRIBUTING.md#the-entry-bar)):

- [ ] `review_status` is set to `draft` (never `stable` or `reference-quality`; those are maintainer-only)
- [ ] `tells` (5 to 7), `anti_patterns` (2 to 4), and `failure_modes` (2 to 3) carry real content, and each failure mode describes the entry over-hitting its own register
- [ ] Each `confusable_with` entry lists this entry back, and the body has an `### Often confused with` block for each one
- [ ] At least one worked sample on an anchor topic, under `examples/vertical-slices/`
- [ ] `python tools/build-indexes.py` was run after the change
