# Hypothesis Negative Space

Local context first:
- `results/literature/gap_frontier.md` is only a scaffold, so the strongest local guidance comes from `results/swarm/gap_map.md`, `results/swarm/falsifier.md`, and the current deterministic solver state.
- `results/swarm/director_brief.md` was not present in the repo at inspection time.
- The over-explored lanes are already clear: published Paley / prime-power constructions, appendix witness lookup, and generic stochastic local search from scratch.

## Direction 1: Four-Vertex Lift Rather Than From-Scratch Search
- Hypothesis: the exact witnesses form a recursive family where an `n` witness can often be extended to an `n + 1` witness by adding four vertices and solving only the induced old-new/new-new pattern subject to pairwise slack constraints.
- Why this attacks negative space: every target instance differs by exactly four vertices, but the current search culture mostly restarts on the full `4n - 2` edge set. That ignores the strongest local prior the repo has: verified witnesses for adjacent values of `n`.
- What prior work appears to have skipped: no artifact here treats the transition `n -> n + 1` as the primary object of study, even though that is the smallest nontrivial step in the benchmark.
- Testable next step: for each exact witness up to `n = 21`, record which old-old pairs are saturated, then solve a small SAT / IP extension problem over the four new vertices and the old-new incidence classes.
- Angle to avoid: do **not** repeat generic warm-start tabu over all edges. If the method still mutates the whole graph with a heuristic score, it has collapsed back into the same search family.

## Direction 2: Optimize Exact Pair Slack, Not Surrogate “Bad Book” Counts
- Hypothesis: the hard unsupported instances fail because a small fraction of edge/non-edge pairs sit exactly at the book threshold, so a solver that tracks per-pair slack and repairs the worst certificates should scale better than degree-based or aggregate-violation heuristics.
- Why this attacks negative space: the legacy code optimized loose surrogate scores and degree targets. That is cheap, but it does not align tightly with the verifier’s actual yes/no condition.
- What prior work appears to have skipped: there is no evidence in the repo that the search objective was redesigned around exact witness certificates, margin distributions, or adversarial pair sets.
- Testable next step: maintain bitset-based exact slacks for all pairs, prioritize moves that reduce the maximum violated margin, and benchmark against the old total-violation objective on the first unsupported cases `n = 22, 24, 50`.
- Angle to avoid: do **not** polish annealing/tabu parameters on the old objective. That only improves an over-explored heuristic, not the underlying mismatch between the score and the theorem condition.

## Direction 3: Composite-Order Orbit Search Instead of Full Paley or Full Graph Search
- Hypothesis: unsupported odd composite and even cases may admit low-orbit witnesses in cyclic/product groups that are not true finite-field Paley graphs but still satisfy the same pair-count inequalities after orbit compression.
- Why this attacks negative space: the current artifact has a sharp gap between “prime-power algebra works” and “everything else is unsupported.” That suggests the missing structure is not necessarily full randomness; it may be algebra on the wrong state space.
- What prior work appears to have skipped: the local pipeline treats composite `2n - 1` mostly as failed Paley territory or a cue for unrestricted search, rather than searching directly over orbit variables in `Z_m`, `Z_a x Z_b`, or two-block polycirculant templates.
- Testable next step: mine the exact witnesses for orbit structure and autocorrelation signatures, then fit SAT / ILP models over difference classes rather than over all `O(n^2)` edges.
- Angle to avoid: do **not** repackage quadratic residues on non-prime-power orders and call it new. The point is to search compressed composite-order templates, not to stretch Paley beyond where its proof machinery actually applies.

## Overlap Pivots
- If a proposal is mostly “use Paley again,” it overlaps the known prime-power family and should be rejected.
- If a proposal is mostly “search longer with randomness,” it overlaps the legacy mixed-language artifact and should be rejected.
- If a proposal uses the exact witnesses only as lookup tables, it misses the strongest transferable signal currently available in the repo.
