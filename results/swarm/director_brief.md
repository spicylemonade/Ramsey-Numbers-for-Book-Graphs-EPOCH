# Director Brief

## Current state
- The user's complaint about mixed C/Python and probabilistic fallback is resolved for the active root artifact. `solution.py` is Python-only, deterministic, and the root tests pass.
- The real unresolved issue is coverage. `python solution.py --verify-supported --limit 100` confirms 42 supported values and 58 explicit `ValueError` rejections, so the root submission is a deterministic partial solver, not a full all-`n` algorithm.
- The archived `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/` tree still contains C and random-search files. Treat that tree as legacy evidence only and do not conflate it with the root submission.

## Champion direction
- Champion: four-vertex lift from the exact witness ladder.
- Why this wins: it is the cleanest novelty move that does not overlap the known exact-witness packaging or the known prime-power Paley family. It exploits the strongest unused repo asset, adjacent verified witnesses, and attacks the benchmark at the smallest natural step, `n -> n + 1`, instead of restarting full search on `4n - 2` vertices.
- Fast falsifier: hold the old graph fixed and ask a restricted SAT/IP model to recover known steps such as `20 -> 21` and `21 -> 22`. If it cannot reproduce known adjacent witnesses, stop before spending serious budget on `22 -> 23`.
- Exact next experiment for the researcher: extract saturated pair data and coarse orbit summaries from the exact witness bank, encode a completion model over only old-new and new-new incidences, recover known steps first, then attempt `22 -> 23`.

## Backup direction
- Backup: certificate-aligned pair-slack repair.
- Why it stays alive: it is less novel than the champion, but it has the fastest kill path and directly addresses the failure mode exposed by the legacy heuristic artifact, namely optimizing scores that do not match the verifier's actual yes/no condition.
- Exact next experiment for the researcher: benchmark exact max-slack repair against the old surrogate objective on `n = 22, 24, 50`, using verifier calls, best achieved slack margin, and reproducibility as the only scoreboard. Do not escalate to belief propagation unless the plain exact-slack baseline already wins.

## Held in reserve
- Composite-order orbit-compressed search is the third line. It attacks the real unsupported frontier, especially even `n > 20` and odd composite cases, but it overlaps more heavily with the known cyclic/block-circulant/difference-set lane and should only get budget after witness mining shows a stable low-orbit signal.

## Guardrails
- Do not claim the prompt is fully solved. The correct current claim is: the repo now has a Python-only deterministic artifact that returns verified witnesses on its supported domain and refuses unsupported inputs.
- Do not spend budget re-packaging small exact witnesses or the prime-power Paley family as if that were new.
- Do not revive unrestricted stochastic search just because it is easy to run. If the lift direction fails, move to exact pair-slack baselines, not back to annealing.
