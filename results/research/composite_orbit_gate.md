# Composite-Orbit Gate

## Decision
`composite_orbit_templates` stays reserved. The current exact witness feature file does show a coarse parity-structured symmetry signal, but it is not yet strong enough to justify spending implementation budget on orbit-compressed search.

## Evidence From `results/analysis/exact_witness_features.json`
- Odd exact witnesses from `n=5` through `n=21` are coarse 1-WL single-class graphs in this bank.
- Even exact witnesses from `n=6` through `n=22` mostly split into two equal-sized 1-WL classes.
- That is a real regularity signal, but it is still only a coarse solved-range pattern rather than direct evidence that unsupported composite frontier cases admit a low-orbit template.

## Minimum Evidence Required Before Budget Is Spent
- A stable orbit or autocorrelation pattern that predicts unsupported composite cases rather than only re-describing the solved parity split.
- At least one compressed template that explains a frontier-adjacent case better than the generic two-block family.
- A verifier-aligned advantage on one of `23`, `24`, or `50`.

## Current Gate Result
- Coarse 1-WL signal summary: odd-class counts [1, 1, 1, 1, 1, 1, 1, 1, 1], even-class counts [2, 2, 2, 2, 2, 2, 2, 2, 2].
- Gate status: remain reserved until a stronger low-orbit or autocorrelation signature is mined.
