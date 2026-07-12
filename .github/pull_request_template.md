## Summary

<!-- What does this PR change, and why? Link the issue if one exists. -->

## Checklist (from CONTRIBUTING.md)

- [ ] `python tools/validate.py` passes with no errors
- [ ] `python -m pytest tests` passes
- [ ] No em-dashes (U+2014) or en-dashes (U+2013) in any file
- [ ] Commit messages follow Conventional Commits format

For new taxonomy entries additionally:

- [ ] At least one anchor example using the new entry (under `examples/vertical-slices/`)
- [ ] Schema validation passes for all modified entries
- [ ] `review_status` is set to `draft`
