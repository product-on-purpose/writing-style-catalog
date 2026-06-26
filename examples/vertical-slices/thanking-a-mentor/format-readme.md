---
entry_id: readme
axis: format
topic_slug: thanking-a-mentor
topic_label: Writing to thank a mentor who shaped your career
author_type: llm
llm_model: claude-sonnet-4-6
review_status: reviewed
---

# put-forward

[![mentor-tenure](https://img.shields.io/badge/mentor%20tenure-10%20years-informational)](docs/acknowledgments.md)
[![patience-level](https://img.shields.io/badge/patience-exceptional-brightgreen)](docs/evidence.md)
[![career-impact](https://img.shields.io/badge/career%20impact-lasting-orange)](docs/outcomes.md)

> Assign the project they are not quite ready for. Stay close. Do not take over.

This is the practice Dana applied in my second year at the company. I did not have a name for it at the time. I have one now because I watched her use it on me, and last month I used it on someone I manage, and that is when I finally understood what it cost her to stay patient while I found my footing.

This README documents what she did and why it worked, so I can say thank you in a form that matches the scale of what I owe her.

## Install

Dana put me forward to lead the platform migration before I was ready. I told her I was not ready. She said I was closer than I thought, and she nominated me before I could finish arguing.

```bash
$ put-forward --nominate "me" --project "platform-migration" --lead true
Nominated. You start Monday.
Warning: confidence not required at install time.
```

She did not wait for my confidence. She supplied it on loan until I built my own.

## Quick start

The first three weeks were hard. I made decisions and reversed them. I asked Dana questions she had already answered. She answered them again. She attended the first two stakeholder meetings and said almost nothing. When I got something wrong in the third one, she corrected me afterward, not during.

```python
# Dana's approach, reconstructed a decade later
def mentor(report, project):
    nominate(report, project)   # before they feel ready
    stay_close(report)          # visible, available
    do_not_take_over()          # even when it would be faster
    correct_privately()         # always after, never during
    repeat_as_needed()
```

The project shipped. Slightly late, but it shipped. I led the post-mortem. Nobody needed to ask Dana to be there.

## Documentation

What that project made possible is hard to index precisely. The closest I can get:

- [the confidence to be in rooms I should not be in yet](docs/rooms.md)
- [a working model for what staying close without taking over looks like](docs/model.md)
- [the patience Dana spent on me across that quarter](docs/patience-ledger.md)
- [what I replicated last month when I put Micah forward for the infrastructure audit](docs/passing-forward.md)

The last item does not exist without Dana. That is the argument this README is making.

## Contributing

Last month I nominated Micah, a senior on my team, to lead an audit they were not quite ready for. I stayed close. I attended the first two review sessions. I did not take over when they reversed a call I would not have reversed.

The moment I recognized what I was doing, I went home and started writing this.

If you want to contribute to this pattern, the guide is one sentence: put someone forward before they feel ready, and do not take over while they find their footing.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Dana gave this to me without conditions. I did not earn it before she gave it. Ten years later I am passing it to Micah on the same terms.

I owe Dana a thank-you I should have written sooner. This is it.

See [LICENSE](LICENSE).
