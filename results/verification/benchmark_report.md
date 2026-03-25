# Benchmark Report

## Scope
This `review_round_1` audit is limited to Phase 4 benchmark quality: baselines, controls, ablations, error analysis, and stress coverage. The question here is not whether the experiments were run, but what the current artifacts justify for publication-facing claims.

## What Was Actually Benchmarked
- Four-vertex lift:
  - `book_research.py` tests one exact feasibility model with all old-old adjacencies frozen and only `old_new` and `new_new` variables free.
  - The only executed cases are `20 -> 21` and `21 -> 22`.
  - Both returned `INFEASIBLE` under the 60-second budget, in `3.009s` and `3.594s`, respectively.
  - `22 -> 23` was not attempted because the fixed-old kill switch fired first.
- Pair-slack repair:
  - `book_research.py` runs exhaustive one-neighborhood local search inside the restricted two-block family from one deterministic seed per `n`.
  - The only benchmarked orders are `22`, `24`, and `50`.
  - `n = 22` preserves the embedded exact witness in both modes.
  - `n = 24` shows a mixed result: exact improves `min_slack` from `-7` to `-2` and lowers total negative excess from `88` to `68`, but raises violation count from `16` to `48`.
  - `n = 50` shows only a weak primary-objective gain: exact improves `min_slack` from `-14` to `-12` while both secondary metrics get worse.
- Coverage impact:
  - no new verified witness;
  - no change to the existing `42 supported / 58 unsupported` split over `n <= 100`.

## Metric Integrity
- Pair-slack currently misreports `verifier_calls`.
  - `_candidate_metrics()` runs `solution._verify_book_constraints()` for the seed candidate and every swap candidate.
  - The exported `verifier_calls` field increments only once per accepted round, so the JSON and markdown tables report round count, not verifier invocations.
- Under the current implementation, the true verifier-invocation counts are:

| n | rounds completed | reported `verifier_calls` | actual verifier invocations per mode |
| --- | ---: | ---: | ---: |
| 22 | 1 | 2 | 573 |
| 24 | 2 | 3 | 1369 |
| 50 | 1 | 2 | 3051 |

- `n = 22` is an especially weak efficiency datapoint because the seed is already verified at round 0, but the loop still exhausts the full one-swap neighborhood before it notices there is no improvement. Most of the recorded work there is redundant post-verification search, not repair.
- Pair-slack `runtime_seconds` starts after the seed candidate has already been scored, so it is not end-to-end wall time.
- Lift `runtime_seconds` starts only after the full CP-SAT model has been built, so it is solver time rather than command wall time.
- Because pair-slack exhaustively scans the same neighborhood in both modes before updating, the current benchmark does not support an efficiency claim. It supports only comparison of final objective values under equal exhaustive local search.

## Missing Baselines And Controls
- Pair-slack `n = 22` is only an identity sanity check. The seed is already the exact witness, so success there does not demonstrate repair ability.
- The benchmark set omits `n = 23`, the first unsupported odd composite case above the exact range and an obvious falsifier target.
- Pair-slack uses one deterministic seed construction per `n`. There is no control over:
  - perturbed exact witnesses;
  - alternative algebraic or residue-based seeds;
  - fixed random starts;
  - an exact SAT/IP baseline on the same two-block family.
- The lift lane benchmarks only the fully frozen-old formulation. There is no relaxed control with bounded old-old rewiring, so the current negative result falsifies only that submodel.
- The lift rubric asked for commands, seeds if any, runtime, verifier-call counts, and outcomes for the known-step runs. The current artifact logs commands, runtime, and outcomes, but not verifier-call-style accounting.
- The pair-slack rubric/spec asked for verifier calls, runtime, and reproducibility under deterministic tie-breaking. The current artifact has the mislabeled verifier-call field and only single runs, so reproducibility is inferred from the deterministic code path rather than demonstrated by rerun evidence.
- `results/experiments/experiment_manifest.json` is also weaker than a publication-quality rerun record for pair-slack. It stores one schematic command with brace expansion and an ellipsis instead of the six exact invocations and output paths used to generate the saved JSON files.

## Missing Ablations
- The pair-slack comparison changes all three ranking terms at once:
  - exact: maximize `min_slack`, then minimize total negative excess, then minimize violation count;
  - surrogate: minimize violation count, then minimize total negative excess, then maximize `min_slack`.
- That is not a clean ablation. The current evidence does not isolate whether the observed `min_slack` gain comes from prioritizing `min_slack` itself or from the changed tie-break order.
- The pair-slack search family is not ablated:
  - `D22` is fixed as the complement of `D11`;
  - `D12` cardinality is fixed at `n - 1`;
  - only single `D11` pair swaps and single `D12` swaps are allowed;
  - there is no multi-swap, mixed-move, or seed-family ablation.
- The saved final states make one omitted ablation especially important: audit-side recomputation shows that the remaining negative slacks at `n = 24` and `n = 50` are all within-layer, so the harness should separate `D11`-only from `D12`-only neighborhoods. Without that split, it is unclear whether cross-layer moves are already solved and the residual obstruction is entirely within-layer.
- The lift lane lacks formulation ablations between:
  - fully frozen old-old edges;
  - partially rewired old-old edges;
  - other relaxed exact models on the same target order.

## Missing Error Analysis And Stress Tests
- Pair-slack exports only three scalar failure metrics and five worst constraints per round. It does not report full slack histograms or counts by family (`edge_l0`, `edge_l1`, `edge_cross`, `nonedge_l0`, `nonedge_l1`, `nonedge_cross`).
- Audit-side recomputation on the final `n = 24` and `n = 50` candidates shows a concrete hidden diagnostic: all negative slacks are within-layer (`edge_l0`, `edge_l1`, `nonedge_l0`, `nonedge_l1`), while cross-layer constraints are nonnegative. The benchmark artifacts do not surface this, so the failures remain under-localized.
- `n = 50` gets only one improvement round per mode, while `n = 24` gets two. That is not enough to support convergence or scaling claims.
- There is no perturb-and-recover stress test at `n = 22`; the benchmark never asks either objective to repair a damaged known witness.
- There is no broader lift stress grid such as `18 -> 19`, `19 -> 20`, `20 -> 21`, `21 -> 22`, so the current data does not show whether frozen-old infeasibility is universal or onset-specific.
- There is still zero direct frontier evidence on `22 -> 23`.

## Publication-Quality Boundary
- Supported claim:
  - the exact frozen-old completion model is falsified on the two tested known-step recoveries;
  - the exact pair-slack objective shows only a mixed scalar improvement inside the current exhaustive two-block local-search harness.
- Unsupported claim:
  - that four-vertex lifts in general fail;
  - that exact pair-slack improves verifier efficiency;
  - that the backup lane is frontier-ready;
  - that Phase 4 extends coverage or produces a new witness.

The current evidence is therefore insufficient for publication-quality positive claims. The strongest defensible framing is a narrow negative result for the frozen-old lift formulation plus a weak mixed-signal note for the exact pair-slack objective.

## Falsifiable Next Tests
1. Fix pair-slack metric accounting and re-export the unchanged benchmark. If the harness is unchanged, `verifier_calls` should become `573` for `n = 22`, `1369` for `n = 24`, and `3051` for `n = 50` per mode.
2. Add the missing `n = 23` benchmark with the same exact-versus-surrogate neighborhood and a budget matched to `n = 24`. If exact slack is genuinely better aligned, it should improve `min_slack` without simultaneously worsening both secondary metrics.
3. Replace the trivial `n = 22` sanity case with perturb-and-recover controls: start from the exact witness, apply 1-, 2-, and 4-move damage, and compare recovery quality and rounds-to-recovery between objectives.
4. Run objective ablations on `n = 24` and `n = 50`: `min_slack` only, `min_slack` then total negative excess, and violation-count-first with matched tie-break order. This isolates the causal effect of the primary objective term.
5. Add move-family and seed-family controls on `n = 23`, `n = 24`, and `n = 50`: current residue seed, at least one alternative algebraic seed, fixed random starts, and separate `D11`-only versus `D12`-only neighborhoods. If the within-layer diagnosis is real, most of the recoverable `min_slack` gain should come from the within-layer side of the search rather than cross-layer moves.
6. Add a relaxed lift control on `20 -> 21` and `21 -> 22` that permits a bounded number of old-old rewires, and add at least one satisfiable deletion-derived recovery case as a positive control. If the positive control fails, the encoding is suspect; if it succeeds while the frozen model remains infeasible on the saved witnesses, the obstruction is more credibly the freeze assumption.
7. Expand the lift stress grid to at least `18 -> 19`, `19 -> 20`, `20 -> 21`, and `21 -> 22`. A monotone failure onset would support a scale-related obstruction; scattered outcomes would point to witness-specific effects instead.
