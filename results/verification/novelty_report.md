# Novelty Report

## Scope

This review checks the active claim surface in the current repo against the repaired problem-local prior-art set. The novelty bar here is material scientific difference from known book-Ramsey work, not packaging hygiene. The active claim surface comes from the root artifact, the final report, and the ranked research lanes in:

- `solution.py`
- `results/final_report.md`
- `results/swarm/director_brief.md`
- `results/research/hypothesis_ranking.md`

Live repo checks still match the recorded verification bundle:

- `python -m unittest -v test_solution.py` passes all 6 tests.
- `python solution.py --verify-supported --limit 100` still reports `42 supported / 58 unsupported`.

## Claim-By-Claim Assessment

| major claim | closest paper or line of work | overlap signal | assessment |
| --- | --- | --- | --- |
| Root deterministic partial solver | Wesley, `Lower Bounds for Book Ramsey Numbers`; the exact small-case / witness-bank line (`ShaoXuBoPan`, `BlackLevenRadz`, `LidickyMcKinleyPfenderSmallBooksWheels`, `VanOverbergheGithub`) | The root solver emits only embedded exact witnesses and the known prime-power two-block family. Coverage does not move beyond the existing support table. | Not materially distinct as Ramsey research. This is an audited deterministic packaging of known safe territory, not a new construction. Evidence: `results/literature/prior_art_review.md`, `results/verification/baseline_regression.md`, `results/verification/coverage_delta.md`, `results/verification/witness_source_audit.md`. |
| Four-vertex lift / fixed-old `n -> n+1` completion | Wesley's block-circulant plus SAT/IP/SMS computational line | The search object is narrower than full search, but it remains an exact witness-search method in the same local computational neighborhood. The required known-step gate failed immediately. | Initially the only defensible novelty candidate. It does not survive Phase 4 because `20 -> 21` and `21 -> 22` were both `INFEASIBLE`. No accepted novelty claim remains from this lane. Evidence: `results/experiments/four_vertex_lift_known_steps.md`, `results/experiments/four_vertex_lift_frontier.md`, `results/literature/prior_art_gap.md`. |
| Certificate-aligned pair-slack repair | Small exact / computational search line; archived surrogate local-search heuristics; Wesley's computational methods context | This is a score-function change inside an existing search neighborhood, not a new witness family or proof method. Benchmarks are mixed and frontier-free. | Weak differentiation only. Exact slack improves `min_slack` on some cases, but it finds no verified witness and does not dominate the surrogate baseline across the verifier metrics that matter. Evidence: `results/experiments/pair_slack_benchmark.md`, `results/verification/benchmark_report.md`, `results/literature/prior_art_gap.md`. |
| Composite-order orbit templates | Cyclic / block-circulant / difference-set / Paley / strongly-regular-graph line (`FaudreeRousseauSheehanStronglyRegular`, Wesley, `VanOverbergheGithub`) | The proposal sits close to known algebraic construction territory and can easily collapse into "Paley again" unless the orbit signal is real. | Still speculative. The current feature mining shows only a coarse solved-range parity signal via 1-WL classes, not a frontier-relevant low-orbit template. Evidence: `results/research/composite_orbit_gate.md`, `results/analysis/exact_witness_features.json`, `results/research/hypothesis_ranking.md`. |
| Any broader theorem, upper-bound, or asymptotic claim | `RousseauSheehanRamseyBooksOriginal`, `Conlon_BookRamsey`, `ConlonFoxWigderson_RamseyBooksQuasirandomness`, `ConlonFoxWigderson_OffDiagonalBooks`, `ChenLinRamseyBookUpperBounds`, `LiuLiRamseyBooks` | These papers already define the correct theorem-level neighborhood. The repo does not add a new proof, asymptotic estimate, or exact theorem. | Not supported. These sources are claim-boundary context only; they do not license broader mathematical novelty for the current artifact. Evidence: `results/literature/prior_art_watchlist.md`, `results/literature/prior_art_gap.md`, `results/literature/prior_art_review.md`. |

## Required Superficial Comparisons

The four string-graph papers remain retrieval drift, not real novelty blockers:

- `String Graph Obstacles of High Girth and of Bounded Degree (2025)`
- `Quantum Based Grover's Algorithm and Graph Coloring in Unstructured Searches for Bit String Validation (2025)`
- `FSG: Fast String Graph Construction for De Novo Assembly (2016)`
- `A 1.9999-Approximation Algorithm for Vertex Cover on String Graphs (2024)`

They should be mentioned only to close the loop on retrieval error. They do not define the scientific novelty boundary for this repo. Evidence: `results/literature/prior_art_gap.md`, `results/swarm/falsifier.md`.

## Novelty Illusions

- "Python-only" is not the novelty. It fixes packaging contamination from the archived mixed-language path, but it does not create a new Ramsey construction.
- "Deterministic now" is not the same as "general algorithm." The supported domain remains bounded, and the unsupported frontier is unchanged.
- "Exact witness bank in code" is not new theory. The root artifact packages known exact territory and the known prime-power family rather than extending them.
- "Four-vertex lift" sounds like a novel construction program, but after known-step recovery fails it is only a falsified hypothesis, not a contribution.
- "Certificate-aligned slack" sounds stronger than heuristic tuning, but without a verified frontier witness it remains a narrow objective variant inside an existing search family.
- "Composite-order orbit templates" sounds like a new family, but the current evidence is only a coarse 1-WL parity split in solved cases, not a frontier-reaching structural law.

## Missing Gap Evidence

- The repo still lacks frozen external provenance for the tiny exact witnesses, the graph6 bank for `n=5..21`, and the embedded `n=22` two-block witness. That weakens any attempt to present the packaged witness territory as a publication-ready research contribution. Evidence: `results/verification/witness_source_audit.md`, `results/verification/citation_audit.md`.
- No bounded experiment produced a new verified witness for unsupported frontier values such as `23`, `24`, or `50`. Evidence: `results/verification/coverage_delta.md`, `results/verification/benchmark_report.md`.
- The four-vertex lift lane did not recover known adjacent witnesses, so there is no evidence that the fixed-old completion hypothesis captures real witness structure. Evidence: `results/experiments/four_vertex_lift_known_steps.md`.
- The pair-slack lane does not yet show a decisive verifier-aligned win over the surrogate baseline. On `24` and `50` the metrics remain mixed, and no verified witness appears. Evidence: `results/experiments/pair_slack_benchmark.md`.
- The orbit-template lane has not crossed its own gate. The current feature mining is descriptive rather than predictive, and no compressed frontier template has been demonstrated. Evidence: `results/research/composite_orbit_gate.md`.

## Safe Claim Boundary

The currently defensible contribution is narrower than a novelty-forward paper claim:

- The root artifact is a Python-only deterministic partial solver with explicit unsupported-input handling.
- The verification bundle is reproducible and honest about the `42 supported / 58 unsupported` split through `n <= 100`.
- The fixed-old four-vertex lift failed under its current exact formulation and budget.
- Exact pair-slack repair is, at most, a weak backup signal rather than a frontier advance.

That is a credible verification and negative-results package. It is not yet a materially distinct research contribution relative to the closest book-Ramsey prior art.

VERDICT: DEEPEN
