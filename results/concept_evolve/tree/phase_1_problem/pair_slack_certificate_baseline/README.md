# Concept: pair_slack_certificate_baseline

- Topic Context: Use exact verifier-aligned pair slack as the repair objective instead of heuristic bad-count surrogates.
- Domains: combinatorics, search

## Distinguishing Angle
- Why different from closest prior art: Changes the search score to the exact per-pair certificate margin.
- Easiest falsifier: No verifier-aligned win over a surrogate baseline on 22, 24, and 50.
- First experiment: Deterministic hill-climb benchmark in the two-block family.
- Overlap risk: High overlap with heuristic retuning if the benchmark does not improve frontier margins.
