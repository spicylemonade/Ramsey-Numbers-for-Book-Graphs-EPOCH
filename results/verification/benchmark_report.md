# Benchmark Report

## Scope
This report consolidates the bounded Phase 4 experiments against the actual frontier rather than only theorem-backed warm-up values.

## Lift Lane
- Exact fixed-old-graph recovery failed on `20 -> 21` and `21 -> 22`.
- Because both known-step checks failed under budget, the lift lane was killed before `22 -> 23`.

## Pair-Slack Lane
- On `24`, the exact-slack objective materially improved the primary worst-case slack objective and reduced total negative excess, but it increased raw violation count and did not reach a verified witness.
- On `50`, the exact-slack objective improved worst-case slack slightly, but both violation count and total negative excess were worse than the surrogate baseline, so the signal is weak.
- On `22`, both modes preserved the exact witness and served only as a sanity check.

## Coverage Impact
- Phase 4 did not change the previously verified support table.
- See `results/verification/baseline_regression.md` and `results/verification/coverage_delta.md` for the repo-wide `42 supported / 58 unsupported` split over `n <= 100`.
- The important stress cases `23`, `24`, and `50` remain unsupported.

## Benchmark Conclusion
The bounded experiment bundle did not produce a new verified witness beyond the existing deterministic support table. The only positive signal is that exact slack tracks the primary `min_slack` objective better on some unsupported cases, but the full verifier metric set remains mixed and too weak to change claim language.

## Cross-References
- Experimental details: `results/experiments/four_vertex_lift_known_steps.md`, `results/experiments/four_vertex_lift_frontier.md`, `results/experiments/pair_slack_benchmark.md`.
- Novelty boundary: `results/verification/novelty_report.md`.
- Citation boundary: `results/verification/citation_audit.md`.
- Final approved wording: `results/verification/verification_summary.md`.
