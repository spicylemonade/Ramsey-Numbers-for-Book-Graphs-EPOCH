# Pair-Slack Benchmark

## Commands
```bash
python3 book_research.py pair-slack --n 22 --rounds 1 --mode exact --output results/experiments/pair_slack_22_exact.json
python3 book_research.py pair-slack --n 22 --rounds 1 --mode surrogate --output results/experiments/pair_slack_22_surrogate.json
python3 book_research.py pair-slack --n 24 --rounds 2 --mode exact --output results/experiments/pair_slack_24_exact.json
python3 book_research.py pair-slack --n 24 --rounds 2 --mode surrogate --output results/experiments/pair_slack_24_surrogate.json
python3 book_research.py pair-slack --n 50 --rounds 1 --mode exact --output results/experiments/pair_slack_50_exact.json
python3 book_research.py pair-slack --n 50 --rounds 1 --mode surrogate --output results/experiments/pair_slack_50_surrogate.json
```

## Results Table
| n | mode | runtime_s | verifier_calls | min_slack | violation_count | total_negative_excess | verified |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 22 | exact | 1.831 | 2 | 0 | 0 | 0 | True |
| 22 | surrogate | 1.832 | 2 | 0 | 0 | 0 | True |
| 24 | exact | 5.13 | 3 | -2 | 48 | 68 | False |
| 24 | surrogate | 5.08 | 3 | -7 | 16 | 88 | False |
| 50 | exact | 47.555 | 2 | -12 | 80 | 652 | False |
| 50 | surrogate | 47.339 | 2 | -14 | 72 | 556 | False |

## Interpretation
- `n=22` is a sanity case: both modes preserve the exact witness.
- `n=24`: the exact-slack mode improves the primary worst-case slack from `-7` to `-2` and reduces total negative excess from `88` to `68`, but it increases the raw violation count from `16` to `48` and still does not find a valid witness.
- `n=50`: the exact-slack mode improves the primary worst-case slack from `-14` to `-12`, but both violation count and total negative excess are worse than the surrogate run, so the signal is especially weak.

## Conclusion
The exact-slack objective shows a mixed signal that is positive only on the primary `min_slack` objective. That is not a decisive verifier win, so the lane remains only a weak backup and does not extend the supported frontier.
