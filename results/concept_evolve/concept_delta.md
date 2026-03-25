# Concept Delta

## Suggestion

- Mine the verified witness bank for structure before spending more search budget.
- Kill the fixed-old-graph four-vertex lift quickly if it cannot recover known steps.
- Benchmark an exact verifier-aligned pair-slack objective against the archived surrogate-style baseline before entertaining more elaborate repair ideas.

## Implementation

- Added `book_research.py` with deterministic `features`, `lift`, and `pair-slack` experiment entry points.
- Ran exact known-step lift experiments on `20 -> 21` and `21 -> 22`.
- Ran deterministic pair-slack benchmarks on `n = 22`, `24`, and `50` in both exact and surrogate modes.
- Strengthened `test_solution.py` with an explicit repo-root module path assertion.
- Fixed the feature/provenance consistency issue so `results/analysis/exact_witness_features.json` now tags `n = 3` as `prime_power_family`.
- Hardened the active-path guardrails in [solution.py](/home/archivara/work/repo/solution.py) so unsupported inputs explicitly advertise that no heuristic or mixed-language fallback is used.
- Expanded [test_solution.py](/home/archivara/work/repo/test_solution.py) to check unsupported-case messaging, forbid `numpy` and `ortools` style fallback tokens, and assert that the archive README labels that tree as historical `legacy-only` context.
- Tightened the archive label in [790a8891-d60d-46f1-8aef-84f720d59562_aristotle/README.md](/home/archivara/work/repo/790a8891-d60d-46f1-8aef-84f720d59562_aristotle/README.md) and recorded the rerun evidence in [results/verification/root_submission_hygiene.md](/home/archivara/work/repo/results/verification/root_submission_hygiene.md).

## Result

- The active root solver remains Python-only and deterministic.
- `python -m unittest -v test_solution.py` passes.
- `python solution.py --verify-supported --limit 100` still verifies the `42 supported / 58 unsupported` split.
- Direct probes of `n = 23`, `24`, `50`, and `100` all fail explicitly with `ValueError` instead of silently guessing.
- The root regression harness now fails if the archive stops being labeled `legacy-only`, making the root-vs-archive boundary harder to blur.
- The fixed-old-graph four-vertex lift failed both known-step recovery targets and is killed in its current form.
- The exact pair-slack objective improved worst-case slack on `24` and `50`, but did not produce a new verified witness.
- The post-verification `concept_evolve iterate` pass promoted `exact_slack_certificate` as the recurrent champion bridge.
- Coverage did not move beyond the existing deterministic support table.

## Novelty Delta

- No new constructive all-`n` result was obtained.
- The only defensible novelty delta from this pass is negative-space evidence: the fixed-old completion lane fails its own known-step gate, and exact slack is somewhat more verifier-aligned than the surrogate objective without yet changing the frontier.
- The new hygiene work is not a mathematical novelty claim; it is regression hardening so the resolved pure-Python/deterministic boundary cannot silently drift back toward archive contamination.
