# Baseline Audit

## Scope
This audit separates claims about the active root artifact from behavior that exists only in the archived `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/` tree. It is a baseline evidence audit, not a performance benchmark.

## Root Artifact
- Active path: root `solution.py` plus `test_solution.py`, with the imported module path asserted by `test_solution_module_is_repo_root_solution_file`.
- Language/runtime: Python-only, deterministic, no shell-out, no random fallback.
- Verified support table over `n <= 100`: `42 supported / 58 unsupported`.
- Representative unsupported values: `23`, `24`, `50`, `100`.
- Unsupported inputs fail explicitly with `ValueError`.

## Legacy Archive
- Archived files still include C search and stochastic Python search helpers.
- They are useful only as historical evidence about prior search attempts, not as evidence about the active submission artifact.
- Any review that mixes archive behavior with root-artifact claims is contaminated.

## Provenance Controls
- `results/verification/witness_provenance.json` tracks the source category for every `n <= 100` and now lists `_field_model` in the prime-power generation path.
- `results/verification/witness_source_audit.md` records that external provenance for the graph6 bank and the `n=22` two-block witness is still unresolved.
- `results/analysis/exact_witness_features.json` now tags `n=3` consistently as `prime_power_family` instead of mixing it with the graph6 bank.

## What This Audit Does Not Claim
- The baseline regression runtime is not a controlled benchmark.
- The root artifact is not an all-`n` construction.
- The unresolved external provenance entries are not silently promoted into publication-ready citations.

## Baseline Conclusion
The root artifact resolves the user's mixed-language/probabilistic complaint for the active submission path but not the coverage problem. It is a deterministic partial solver, not an all-`n` construction.
