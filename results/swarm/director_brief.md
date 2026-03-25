# Director Brief

## Verified current state
- Local rerun on 2026-03-25: `python -m unittest -v test_solution.py` passed all 6 tests.
- Local rerun on 2026-03-25: `python solution.py --verify-supported --limit 100` again showed 42 supported values and 58 unsupported values through `n <= 100`.
- The user's packaging complaint is resolved for the active repo-root artifact. `solution.py` is Python-only, deterministic, and refuses unsupported inputs with `ValueError`.
- The same complaint is still valid if someone points at the archived `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/` tree, which still contains C and stochastic search files. That tree must stay labeled as legacy-only context.
- The actual blocker is coverage, not packaging hygiene. The root artifact is an honest deterministic partial solver, not a valid all-`n` answer to the stated prompt.

## Champion direction
- Champion: counterexample-guided orbit refinement over symmetry-compressed templates.
- Why this wins: it is the strongest live novelty lane that still uses the verified witness bank and the exact verifier, but does not overlap too heavily with the known exact-witness packaging or the known Paley/block-circulant family. It also avoids the fatal flaw in the frozen-old four-vertex lift by allowing the representation itself to refine rather than holding the old graph fixed.
- Fast falsifier: hold out supported cases `n = 20, 21, 22`; start from coarse two-block and dihedral templates; require recovery or a decisive template-death certificate with fewer verifier calls than the exact pair-slack baseline. If two held-out cases fail, kill the lane.
- Exact next experiment for the researcher: mine orbit summaries and pair-saturation types from the verified witness bank through `n = 22`, define a deterministic template lattice, translate verifier failures into refinement clauses, and run leave-one-out recovery on the held-out supported cases before touching `n = 23` or `n = 24`.

## Backup direction
- Backup: deterministic exact pair-slack repair baseline.
- Why it stays alive: it is less novel than the champion, but it is the cleanest control against the legacy heuristic artifact and the fastest way to tell whether a new representation is actually better than a verifier-aligned local objective.
- Exact next experiment for the researcher: freeze the exact-slack implementation and deterministic tie-breaking, then benchmark only against the old surrogate objective on `n = 22`, `24`, and `50`, using verifier calls, best achieved slack margin, and reproducibility as the scoreboard.

## Not selected
- Fixed-old four-vertex lift is not selected. Its current form is already killed by the known-step checks: `20 -> 21` and `21 -> 22` both came back infeasible. Do not spend more budget there unless the representation is materially relaxed, in which case it becomes a new hypothesis rather than a continuation.
- Composite-order or Paley-like template variants are not selected as the main plan because they overlap too heavily with the known cyclic/block-circulant lane unless witness mining first shows a stable low-orbit signal that current templates miss.
- Do not spend further budget proving that the root solver is Python-only and deterministic. That issue is already closed by test. Spend the next budget only on extending coverage beyond the exact-witness and prime-power regime.

## Claim guardrail
- The only acceptable current claim is: the repo contains a Python-only deterministic artifact that returns verified witnesses on its supported domain and refuses unsupported inputs.
- Do not claim that the original all-`n` prompt has been solved until the unsupported set is eliminated or a mathematically justified full-family construction is in hand.
