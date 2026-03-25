# Benchmark Report

## Scope
This audit is limited to Phase 4 benchmark quality: baselines, controls, ablations, error analysis, and stress coverage. It asks what the current experiment artifacts actually justify for publication-facing claims.

## What Was Actually Measured
- Fixed-old four-vertex lift:
  - `20 -> 21`: exact CP-SAT returned `INFEASIBLE` in `3.009s`.
  - `21 -> 22`: exact CP-SAT returned `INFEASIBLE` in `3.594s`.
  - `22 -> 23` was not attempted because the predeclared kill switch fired first.
- Pair-slack repair:
  - `n = 22`: exact and surrogate both preserved the embedded exact witness.
  - `n = 24`: exact improved `min_slack` from `-7` to `-2`, reduced total negative excess from `88` to `68`, increased violation count from `16` to `48`, and still failed verification.
  - `n = 50`: exact improved `min_slack` from `-14` to `-12`, but both violation count and total negative excess were worse than surrogate, and both failed verification.
- Coverage impact:
  - no new verified witness;
  - no support-table change beyond the existing `42 supported / 58 unsupported` split over `n <= 100`.

## Metric Integrity Problem
The pair-slack benchmark currently misreports `verifier_calls`.

- In `book_research.py`, `_candidate_metrics()` calls the exact verifier for the seed candidate and for every swap candidate in the exhaustive neighborhood.
- The exported `verifier_calls` field increments only once per accepted round, so the JSON and markdown tables report round count, not verifier invocations.
- Under the current implementation, the true verifier-invocation counts are:

| n | rounds completed | reported `verifier_calls` | actual verifier invocations per mode |
| --- | ---: | ---: | ---: |
| 22 | 1 | 2 | 573 |
| 24 | 2 | 3 | 1369 |
| 50 | 1 | 2 | 3051 |

- Because both modes exhaustively scan the same neighborhood before updating, the current benchmark does **not** support any claim about verifier-call efficiency. At most it supports comparison of final objective values under equal exhaustive local search.
- `runtime_seconds` also starts after the seed candidate has already been evaluated, so it is slightly short of true end-to-end runtime.

## Missing Baselines And Controls
- Pair-slack `n = 22` is only an identity sanity check. The seed is already the embedded exact witness, so success there does not show repair capability.
- The benchmark omits `n = 23`, which is the first unsupported frontier case and one of the explicit falsifier targets named elsewhere in the repo.
- Pair-slack uses only one deterministic seed construction per `n`. There is no control against:
  - perturbed exact witnesses;
  - alternative algebraic or residue-based seeds;
  - fixed-seed random starts;
  - an exact SAT/IP baseline on the same two-block family.
- The lift lane tests only the most restrictive formulation: old-old adjacencies are completely frozen. There is no relaxed control that allows bounded old-old rewiring, so the negative result kills only the frozen-old submodel.
- The lift benchmark is also missing the metric bundle promised in the rubric: the report contains runtime and status, but no reproducibility log and no verifier-call-style accounting.

## Missing Ablations
- The pair-slack comparison changes three ranking terms at once:
  - exact: maximize `min_slack`, then minimize total negative excess, then minimize violation count;
  - surrogate: minimize violation count, then minimize total negative excess, then maximize `min_slack`.
- That is not a clean ablation. The current evidence does not isolate whether the observed `min_slack` gain comes from prioritizing `min_slack` itself or from the changed tie-break order.
- The pair-slack search family is not ablated:
  - `D22` is fixed as the complement of `D11`;
  - only single `D11` pair swaps and single `D12` swaps are allowed;
  - there is no multi-swap, mixed-move, or seed-family ablation.
- The lift lane lacks the key formulation ablation between:
  - fully frozen old-old edges;
  - partially rewired old-old edges;
  - less constrained exact search on the same target order.

## Missing Error Analysis And Stress Tests
- Pair-slack logs only three scalar failure metrics plus five worst constraints. It does not analyze whether failures are:
  - edge-driven or non-edge-driven;
  - concentrated in `l0`, `l1`, or cross-layer constraints;
  - localized to a small orbit-like subset or spread broadly.
- Without that error analysis, the mixed signal on `n = 24` and `n = 50` is descriptive but not diagnostic.
- `n = 50` gets only one improvement round per mode, while `n = 24` gets two. That is not enough to support convergence or scaling claims.
- There is no perturb-and-recover stress test at `n = 22`; the benchmark never asks either objective to repair a damaged known witness.
- There is no broader lift stress grid such as `18 -> 19`, `19 -> 20`, `20 -> 21`, `21 -> 22`, so the current data does not show whether the frozen-old failure is universal or onset-specific.
- There is still zero direct frontier evidence on `22 -> 23`.

## Publication-Quality Boundary
- Supported claim:
  - the fixed-old exact completion model is falsified on the two tested known steps;
  - the exact pair-slack objective shows only a mixed scalar improvement within the current exhaustive two-block local-search harness.
- Unsupported claim:
  - that four-vertex lifts in general fail;
  - that exact pair-slack improves verifier efficiency;
  - that the backup lane is robust on the frontier;
  - that Phase 4 extends coverage or produces a new witness.

The publication-facing conclusion therefore has to stay narrow: no new verified witness, no coverage extension, strong evidence against the frozen-old lift formulation, and only weak mixed evidence for the exact pair-slack objective.

## Falsifiable Next Tests
1. Fix the pair-slack metric accounting and re-export the benchmark with true verifier invocations. Under the current exhaustive neighborhood, the counts should be `573` for `n = 22`, `1369` for `n = 24`, and `3051` for `n = 50` per mode; any different value means the harness changed.
2. Add the missing `n = 23` benchmark with the same exact-versus-surrogate comparison and a budget matched to `n = 24`. If exact slack is genuinely better aligned, it should improve `min_slack` without simultaneously worsening both secondary metrics.
3. Replace the trivial `n = 22` sanity case with a perturb-and-recover control: start from the exact witness, apply 1-, 2-, and 4-move damage, and compare recovery quality between objectives.
4. Run objective ablations on `n = 24` and `n = 50`: `min_slack` only, `min_slack` plus total negative excess, and violation-count-first with identical tie-breaks. This isolates the causal effect of the primary objective term.
5. Add a relaxed lift control on `20 -> 21` and `21 -> 22` that permits a bounded number of old-old rewires. If the relaxed model succeeds while the frozen model stays infeasible, the obstruction is the freeze assumption rather than the broader lift idea.
6. Expand the lift stress grid to at least `18 -> 19`, `19 -> 20`, `20 -> 21`, and `21 -> 22`. A clean monotone failure onset would support a scale-related obstruction; scattered outcomes would point to witness-specific effects instead.
