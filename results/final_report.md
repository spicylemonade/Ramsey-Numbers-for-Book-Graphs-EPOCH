# Final Report

## Active Artifact

The active submission path is the repo-root `solution.py` with `test_solution.py`. The archived `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/` tree still contains historical C and stochastic search code, but that archive is not part of the active root artifact evaluated here.

The active root solver is Python-only, deterministic, and verifier-backed on its supported domain. It returns a witness adjacency string only when the witness is already backed by the embedded exact bank or the published prime-power family, and it raises `ValueError` on unsupported inputs instead of guessing.

## Verified Baseline

The root verification sweep over `n <= 100` remains `42 supported / 58 unsupported`. The supported territory consists of:
- small embedded exact witnesses,
- the embedded graph6 witness bank,
- the embedded exact two-block witness at `n = 22`,
- the prime-power family where `2n - 1` is a prime power congruent to `1 mod 4`.

This fixes the original mixed-language/probabilistic complaint for the active submission path, but it does not solve the full all-`n` prompt.

## Research Direction

The repaired literature pass showed that the earlier string-graph watchlist was mostly retrieval drift. The real local backbone is Wesley's lower-bound work together with the classical and asymptotic book-Ramsey literature. After aligning with the saved swarm briefs, the run ranked:
1. `four_vertex_lift` as the champion lane,
2. `pair_slack_repair` as the backup lane,
3. `composite_orbit_templates` as the reserve lane.

## Experiments

The champion lane was tested first as an exact fixed-old-graph completion problem. Both known-step recovery targets failed quickly:
- `20 -> 21`: `INFEASIBLE`
- `21 -> 22`: `INFEASIBLE`

Under the predeclared kill switch, that killed the fixed-old four-vertex lift before any `22 -> 23` frontier attempt.

The backup lane benchmarked an exact verifier-aligned pair-slack objective against a surrogate-style baseline on `n = 22`, `24`, and `50`. The exact objective preserved the known `n = 22` witness and improved worst-case slack margins on `24` and `50`, but it still did not produce a valid witness on either unsupported case.

## Outcome

Coverage did not move beyond the existing deterministic support table. The strongest honest conclusion is therefore:
- the active root artifact is a deterministic partial solver;
- the fixed-old four-vertex lift is killed in its current form;
- the exact pair-slack lane remains only a weak backup signal, not a frontier breakthrough.

## Limitations

- The repo still does not provide a full all-`n` construction.
- External provenance remains unresolved for the graph6 bank, the tiny exact witnesses, and the embedded `n = 22` two-block witness.
- The baseline runtime logs are regression evidence, not publication-grade performance benchmarks.

## Next Steps

- Freeze external provenance for the embedded witness bank before any publication-facing release.
- If frontier work continues, move to a stronger exact formulation than the fixed-old completion model.
- Keep bridge-style or BP-style repair ideas gated until a verifier-aligned exact baseline produces a real frontier win.
