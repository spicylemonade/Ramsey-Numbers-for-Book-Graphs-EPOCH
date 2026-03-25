# Implementation Alignment

## Champion

- `four_vertex_lift`
  - Start from adjacent verified witnesses and search only the old-new/new-new completion space for `n -> n + 1`.
  - This matches `results/swarm/director_brief.md` and `results/swarm/hypotheses.json`.

## Backup

- `pair_slack_repair`
  - Score moves by exact verifier-aligned pair slack instead of heuristic bad-book counts or annealing-style surrogate objectives.

## Reserve

- `composite_orbit_templates`
  - Keep composite-order orbit-compressed templates in reserve until exact witness mining shows a stable low-orbit signal.

## Why Implementation Starts With The Four-Vertex Lift

- The current root artifact already resolves the user’s packaging complaint: it is Python-only and deterministic on its supported domain.
- The unresolved scientific problem is coverage, not language hygiene.
- The four-vertex lift is the narrowest frontier extension that uses the strongest existing evidence in the repo: adjacent verified witnesses through `n = 22`.
- Legacy stochastic search is explicitly deprioritized because it can return good-looking but unproven candidates and recreates the exact failure mode the user objected to.
- Paley repackaging is also deprioritized because the current root solver already exposes the known prime-power family; rerunning that lane does not address unsupported values such as `23`, `24`, `50`, or `100`.
- The next implementation budget should therefore go to known-step recovery (`20 -> 21`, `21 -> 22`) under the restricted lift model, with pair-slack repair kept as the first fallback if that falsifier fails.
