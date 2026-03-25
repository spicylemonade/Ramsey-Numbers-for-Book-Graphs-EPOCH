# Novelty Report

## Round

- Verification phase: `review_round_1`

## Scope

This review checks the active claim surface in the repo against the repaired problem-local prior-art set. The novelty bar here is material scientific differentiation from the closest book-Ramsey work, not packaging cleanup or code hygiene.

Claim surface reviewed:

- `solution.py`
- `results/final_report.md`
- `results/swarm/director_brief.md`
- `results/research/hypothesis_ranking.md`
- `results/experiments/four_vertex_lift_known_steps.md`
- `results/experiments/four_vertex_lift_frontier.md`
- `results/experiments/pair_slack_benchmark.md`

Repo checks rerun in this round:

- `python -m unittest -v test_solution.py` passes all 6 tests.
- `python solution.py --verify-supported --limit 100` still reports `42 supported / 58 unsupported`.

## Claim-By-Claim Novelty Assessment

| major claim | closest paper or line of work | concrete overlap signal | novelty assessment |
| --- | --- | --- | --- |
| Root deterministic partial solver | Wesley, `Lower Bounds for Book Ramsey Numbers`, plus the small exact/computational witness line (`ShaoXuBoPan`, `BlackLevenRadz`, `LidickyMcKinleyPfenderSmallBooksWheels`, `VanOverbergheGithub`) | The root artifact returns only embedded exact witnesses, the embedded `n = 22` two-block tuple, and the known prime-power Paley-type family. The support table remains `42 supported / 58 unsupported` through `n <= 100`. | Not materially distinct as Ramsey research. This is a deterministic and verifier-safe packaging of known safe territory, not a new witness family, theorem, or frontier extension. Evidence: `results/literature/prior_art_review.md`, `results/verification/baseline_regression.md`, `results/verification/coverage_delta.md`, `results/verification/witness_source_audit.md`. |
| Fixed-old four-vertex lift / `n -> n+1` completion | Wesley's block-circulant plus SAT / IP / SMS computational line | The lane changes the search object by freezing old-old edges and solving only old-new/new-new incidences, but it is still an exact witness-search method in the same problem-local computational neighborhood. Its required known-step gate failed immediately on `20 -> 21` and `21 -> 22`. | This was the only initially plausible novelty candidate. It is not an accepted contribution in the current repo because the frozen-old formulation fails before any frontier witness is reached. The report should stay narrow, though: the data falsifies the frozen-old submodel, not every broader lift variant, because the relaxed rewiring control is still missing. Evidence: `results/experiments/four_vertex_lift_known_steps.md`, `results/experiments/four_vertex_lift_frontier.md`, `results/literature/prior_art_gap.md`, `results/verification/benchmark_report.md`. |
| Certificate-aligned pair-slack repair | Small exact / computational search line, plus the repo's archived surrogate local-search lane and Wesley's computational-method context | The method keeps the same two-block search family and changes the ranking objective to exact per-pair slack. On `24` and `50` it produces mixed scalar changes but no verified witness. | Weak differentiation only. This is an objective-function variant inside an existing search family, not a new constructive family or proof method. It is not materially distinct until it produces either a verifier-aligned benchmark win with clean accounting or a frontier witness. Evidence: `results/experiments/pair_slack_benchmark.md`, `results/research/pair_slack_repair_spec.md`, `results/literature/prior_art_gap.md`, `results/verification/benchmark_report.md`. |
| Composite-order orbit templates | Cyclic / block-circulant / difference-set / Paley / strongly-regular-graph line (`FaudreeRousseauSheehanStronglyRegular`, Wesley, `VanOverbergheGithub`) | The proposal remains close to known algebraic construction territory and can easily collapse into a repackaged low-orbit cyclic family. Current evidence is only a solved-range parity signal in coarse 1-WL classes. | Still speculative, not a demonstrated contribution. There is no frontier-adjacent compressed template, no predictive law on unsupported cases, and no verified advantage over the generic two-block family. Evidence: `results/research/composite_orbit_gate.md`, `results/analysis/exact_witness_features.json`, `results/research/hypothesis_ranking.md`. |
| Any broader theorem, upper-bound, or asymptotic claim | `On Ramsey Numbers for Books`, `The Ramsey number of books`, `Ramsey numbers of books and quasirandomness`, `Off-diagonal book Ramsey numbers`, `New upper bounds for Ramsey numbers of books`, `A note on Ramsey numbers involving large books` | These papers already occupy the theorem-level neighborhood for book-Ramsey claims. The repo adds no new proof, asymptotic estimate, upper bound, or exact theorem. | Not supported. Those papers define the correct boundary conditions for the area, but they do not support any broader mathematical novelty claim for the current artifact. Evidence: `results/literature/prior_art_watchlist.md`, `results/literature/prior_art_gap.md`, `results/literature/prior_art_review.md`. |

## Required Superficial Comparisons

The four string-graph papers remain retrieval drift rather than real novelty blockers:

- `String Graph Obstacles of High Girth and of Bounded Degree (2025)`
- `Quantum Based Grover's Algorithm and Graph Coloring in Unstructured Searches for Bit String Validation (2025)`
- `FSG: Fast String Graph Construction for De Novo Assembly (2016)`
- `A 1.9999-Approximation Algorithm for Vertex Cover on String Graphs (2024)`

They should be mentioned only to close the loop on the earlier retrieval error. They do not define the scientific novelty boundary for this repo. Evidence: `results/literature/prior_art_gap.md`, `results/swarm/falsifier.md`.

## Novelty Illusions And Weak Differentiation

- "Python-only" is not the novelty. It removes archive contamination from the old mixed C / Python path, but it does not create a new Ramsey construction.
- "Deterministic now" is not the same as "general algorithm." Unsupported values such as `23`, `24`, `50`, and `100` remain unsupported.
- "Exact witness bank in code" is not new theory. The root artifact packages known exact territory and the known prime-power family instead of extending either one.
- "Four-vertex lift" sounds like a new construction program, but the only implemented formulation is the frozen-old submodel, and that submodel fails its own known-step gate before frontier use.
- "Certificate-aligned slack" sounds stronger than heuristic tuning, but in the current repo it is still a ranking change within the same two-block local-search neighborhood.
- "Orbit templates" sounds like a new family, but the current evidence is descriptive solved-range symmetry, not a frontier-reaching structural result.

## Missing Gap Evidence

- The repo still lacks frozen external provenance for the tiny exact witnesses, the graph6 bank for `n = 5..21`, and the embedded `n = 22` two-block witness. That blocks any attempt to present the packaged witness territory as a publication-ready contribution. Evidence: `results/verification/witness_source_audit.md`, `results/verification/citation_audit.md`.
- No bounded experiment produced a new verified witness for unsupported frontier values such as `23`, `24`, or `50`. Evidence: `results/verification/coverage_delta.md`, `results/verification/benchmark_report.md`.
- The fixed-old lift lane did not recover known adjacent witnesses, so there is no evidence that the frozen-old completion hypothesis captures real witness structure. Evidence: `results/experiments/four_vertex_lift_known_steps.md`.
- The lift evidence is still formulation-narrow: there is no relaxed control with bounded old-old rewiring, so the current negative result does not justify a claim that lift-style approaches in general fail. Evidence: `results/verification/benchmark_report.md`.
- The pair-slack lane does not yet show a decisive verifier-aligned win over the surrogate baseline, and the current benchmark misreports `verifier_calls`, which weakens any efficiency-style differentiation claim. Evidence: `results/experiments/pair_slack_benchmark.md`, `results/verification/benchmark_report.md`.
- The orbit-template lane has not crossed its own gate. The current feature mining is descriptive rather than predictive, and no compressed frontier template has been demonstrated. Evidence: `results/research/composite_orbit_gate.md`.

## Safe Claim Boundary

The currently defensible contribution is narrower than a novelty-forward paper claim:

- The root artifact is a Python-only deterministic partial solver with explicit unsupported-input handling.
- The verification bundle is reproducible and honest about the `42 supported / 58 unsupported` split through `n <= 100`.
- The frozen-old four-vertex lift formulation is falsified on its two known-step recovery tests.
- Exact pair-slack repair is, at most, a weak exploratory backup signal rather than a frontier advance.

That is a credible verification and negative-results package. It is not yet a materially distinct research contribution relative to the closest book-Ramsey prior art.

VERDICT: DEEPEN
