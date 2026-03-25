# Prior Art Review

## Purpose
This document is the bounded Phase 1 literature and concept-tree synthesis for rubric `item_005`. It integrates outputs from the `explorer`, `citation_auditor`, `novelty_checker`, and `integrator` passes and records that the existing generic ConceptEvolve cards under `results/concept_evolve/tree/` do not yet satisfy the required `phase_1_problem/` path.

## Active Repo Baseline
The active submission artifact is the root `solution.py`, not the archived Aristotle worktree. It is Python-only, deterministic, verifier-backed on its supported domain, and explicitly rejects unsupported inputs. The remaining issue is coverage rather than packaging: the current support sweep over `n <= 100` still yields `42 supported / 58 unsupported`, with representative unsupported values `23`, `24`, `50`, and `100`.

## Closest Problem-Local Prior Art
The Wesley paper is the real backbone. It proves `R(B_{n-1},B_n) = 4n-1` for all `n <= 20` and for the infinite family where `2n-1` is a prime power congruent to `1 mod 4`, using a two-block Paley-type / block-circulant construction. It also uses SAT and integer programming to obtain additional lower bounds and SMS to enumerate small critical graphs. Critically, it does **not** provide a general all-`n` construction, and it says the all-`n` pattern is conjectural rather than solved.

## What The Repo Already Repackages
The current root solver is not a new general construction. It packages three known territories: small exact witnesses embedded directly in the repo, an exact graph6 witness bank, and the published prime-power two-block family. The theorem-backed portion is the prime-power family and the exact `n <= 20` range from Wesley. The embedded `n = 21` and `n = 22` witnesses are verifier-safe in code, but their external bibliographic provenance is still unresolved in this repo and should not be described as new theory.

## Where The Real Gap Starts
After removing the known exact bank and the prime-power family, the scientific gap is the unsupported frontier: even `n > 20` and odd composite values where `2n-1` is not a prime power. The current repo still uses the exact witness bank as lookup material, not as a source of structural hypotheses. That is the gap the Phase 1 review narrows.

## Required Drift Table
| paper | why retrieved | actual topic | overlap with planned direction | decision |
| --- | --- | --- | --- | --- |
| String Graph Obstacles of High Girth and of Bounded Degree (2025) | generic token overlap on `graph` and `algorithm` | string-graph structure | superficial only | retrieval drift; not a pivot trigger |
| Quantum Based Grover's Algorithm and Graph Coloring in Unstructured Searches for Bit String Validation (2025) | generic token overlap on `graph`, `solution`, and `bit string` | quantum / graph-coloring workflow | superficial only | retrieval drift; not a pivot trigger |
| FSG: Fast String Graph Construction for De Novo Assembly (2016) | generic token overlap on `graph`, `string`, and `construction` | bioinformatics string graphs | superficial only | retrieval drift; not a pivot trigger |
| A 1.9999-Approximation Algorithm for Vertex Cover on String Graphs (2024) | generic token overlap on `graph` and `algorithm` | approximation on string graphs | superficial only | retrieval drift; not a pivot trigger |

## Novelty Position Of The Planned Direction
The integrated Phase 1 decision remains: champion `four-vertex lift`, backup `pair-slack repair`, reserve `composite-order orbit templates`. The four-vertex lift is different from Wesley's theorem-backed Paley/block-circulant lane because it changes the search object to a fixed-old-graph `n -> n+1` completion over old-new and new-new incidences. It is also different from generic SAT/IP search from scratch because the old witness is held fixed. The fastest falsifier is exactly the one already recorded in the director brief: recover `20 -> 21`, then `21 -> 22`, before spending budget on `22 -> 23`.

## Citation And Claim Firewall
Allowed claim language for the current root artifact is: deterministic partial solver on supported inputs. Disallowed claim language is: general all-`n` constructive solution, novel exact-witness theory, or any statement that treats the graph6 bank and the `n = 22` witness as bibliographically frozen. The graph6 bank provenance and the `n = 22` two-block source remain unresolved in the current repo.

## Phase 1 Concept-Tree Handoff
The required `results/concept_evolve/tree/phase_1_problem/` package should at minimum contain the following rows.

| concept | why different from closest prior art | easiest falsifier | first experiment | overlap risk |
| --- | --- | --- | --- | --- |
| `four_vertex_lift_known_step_recovery` | searches fixed-old completions instead of full-graph/block-circulant witnesses | fail `20 -> 21` or `21 -> 22` recovery | exact fixed-old CP-SAT recovery | moderate overlap with SAT/IP search, but still distinct in object |
| `pair_slack_certificate_baseline` | optimizes exact verifier-aligned slack instead of surrogate bad-count objectives | no win over surrogate objective on `22/24/50` | deterministic pair-slack benchmark | high overlap with heuristic tuning unless benchmark win appears |
| `composite_order_orbit_templates` | targets unsupported composite cases directly instead of stretching prime-power Paley machinery | no low-orbit signal in exact witness features | witness-feature mining plus orbit gate | overlaps with cyclic/block-circulant work if not constrained tightly |

The existing generic tree does not satisfy this path requirement and is only a precursor.

## Integrated Decision
The repo currently packages known exact and prime-power territory, while the previous watchlist was drifted. The first defensible novelty budget went to four-vertex known-step recovery, but the fixed-old-graph version already failed its kill switch. Pair-slack repair remains as the weaker fallback, and composite-order orbit templates stay gated behind structural evidence from the witness bank.

## Appendix: Claim To Evidence Map
| claim | evidence |
| --- | --- |
| active root artifact is deterministic and partial | `results/verification/verification_summary.md`, `results/verification/baseline_regression.md` |
| known solved territory is `n <= 20` plus the prime-power family | Wesley paper source, `solution.py`, `results/verification/witness_provenance.json` |
| graph6 bank and `n=22` witness provenance are unresolved | `results/verification/witness_source_audit.md` |
| four named string-graph papers are retrieval drift | `results/literature/literature_snapshot.json`, `results/swarm/falsifier.md` |
| four-vertex lift is the only initially defensible novelty lane | `results/swarm/director_brief.md`, `results/swarm/hypotheses.json` |

