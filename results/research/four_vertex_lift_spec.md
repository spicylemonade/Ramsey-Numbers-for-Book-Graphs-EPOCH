# Four-Vertex Lift Spec

## Fixed-Old-Graph Setting
- Input witness: a verified graph for `n` on `4n-2` vertices.
- Target witness: a graph for `n+1` on `4n+2` vertices.
- Restricted model: keep all old-old adjacencies fixed and solve only old-new and new-new incidences.

## Variables
- `old_new[u,a]` for each old vertex `u` and each of the four added vertices `a`.
- `new_new[a,b]` for the six adjacencies among the four added vertices.

## Recovery Targets
- Known-step recovery target 1: `20 -> 21`.
- Known-step recovery target 2: `21 -> 22`.
- Frontier target after recovery: `22 -> 23`.

## Objective
- Primary objective: satisfy the exact book constraints for `n+1` with the old witness frozen.
- Acceptance rule: only a verifier-approved completion counts; partial heuristic scores do not.

## Runtime Budget
- Per recovery attempt: 60 seconds in a single-threaded exact CP-SAT run.
- Frontier attempt budget: zero until the two known-step recoveries pass.

## Kill Switch
- If the fixed-old model fails on `20 -> 21` and `21 -> 22`, do not spend budget on `22 -> 23`.
- That kill switch comes directly from `results/swarm/director_brief.md`.

## Current Outcome
- `20 -> 21`: exact CP-SAT model returned `INFEASIBLE` in about 3 seconds.
- `21 -> 22`: exact CP-SAT model returned `INFEASIBLE` in about 4 seconds.
- The fixed-old-graph champion lane is therefore killed in its current form.
