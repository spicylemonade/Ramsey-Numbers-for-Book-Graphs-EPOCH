# Pair-Slack Repair Spec

## Objective
Use the verifier's exact per-pair slack as the search score.
- Edge slack: `(n-2) - common_neighbors` for each present edge.
- Non-edge slack: `(n-1) - common_nonneighbors` for each missing edge.
- A valid witness has minimum slack `>= 0`.

## Search Family
- Two-block family on `2m = 4n-2` vertices with `m = 2n-1`.
- `D22` is fixed to the complement of `D11` in `Z_m \ {0}`.
- `D12` keeps its target cardinality `n-1`.

## Move Scoring
- Exact mode: maximize minimum slack, then minimize total negative excess, then minimize violation count.
- Surrogate mode: minimize violation count, then minimize total negative excess, then maximize minimum slack.
- The exact mode is the baseline of interest; the surrogate mode is only the comparison target.

## Benchmark Set
- `n = 22` for sanity against a known exact witness.
- `n = 24` for the first unsupported even case above the published exact range.
- `n = 50` for the benchmark stress case highlighted externally.

## Scoreboard
- Verifier calls.
- Best achieved minimum slack.
- Total negative excess.
- Reproducibility under deterministic tie-breaking.
- Runtime.

## Guardrail
Belief propagation, message passing, or any other bridge-style repair is disallowed until this exact-slack baseline shows a verifier-aligned win over the surrogate baseline on the benchmark set.
