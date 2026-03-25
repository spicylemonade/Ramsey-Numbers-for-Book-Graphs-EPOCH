# Hypothesis Bridge

## 1. Belief-Propagation Repair on the Pair-Slack Hypergraph
- Title: Treat unsupported book-Ramsey instances like LDPC decoding rather than local edge flipping.
- Closest prior art: the repo already suggests exact pair-slack repair and certificate-driven search, but still frames the search state as a graph with violated pairs rather than as a sparse factor graph over constraints.
- Why it is different: coding-theory message passing would push local repair signals through edge-pair and non-edge-pair constraints, so updates are driven by structured “check-node” pressure instead of annealing scores or generic SAT branching.
- Falsifiable prediction: on the first hard cases `n = 23, 24, 50`, belief-propagation-guided decimation will reduce the number of exact verifier calls needed to reach a valid witness or prove a template dead end, compared with the current max-slack/local-search style baselines.
- Required experiments: build the pair-slack factor graph for two-block and orbit-compressed templates; compare BP-guided decimation against current local search and SAT warm starts on `n = 23, 24, 50`; log verifier calls, best slack margin, and solve rate.

## 2. Semidefinite Seed Design for Orbit-Compressed Witnesses
- Title: Use SDP-style matrix completion as a seed generator for block-circulant book witnesses.
- Closest prior art: current local directions emphasize Paley-style algebra, exact witness lookup, and orbit-compressed SAT/IP search.
- Why it is different: this borrows from semidefinite relaxation and inverse design, treating the signed adjacency matrix as a constrained completion problem whose rounded solution seeds the discrete solver with globally balanced pair counts instead of random or hand-coded starts.
- Falsifiable prediction: SDP-rounded seeds will enter exact SAT/IP search with smaller maximum pair-slack violations than random seeds or raw Paley-like lifts on unsupported composite/even targets, especially `n = 24` and `n = 50`.
- Required experiments: formulate an SDP over signed two-block or multi-orbit templates; round the relaxed solution into discrete difference classes; compare initial slack histograms and downstream exact-solver performance against random and heuristic seeds.

## 3. Construction DSL Search from Small Exact Witnesses
- Title: Learn a tiny program language of graph lifts instead of searching edge sets directly.
- Closest prior art: the repo already points toward four-vertex lifts and mining exact witnesses for orbit structure, but not toward explicit program synthesis.
- Why it is different: this imports syntax-guided program synthesis ideas, searching over a DSL of operations such as block duplication, orbit toggling, residue-class masks, and four-vertex extensions, with the verifier acting as the semantic checker.
- Falsifiable prediction: a compact DSL fitted on exact witnesses up to `n = 22` will rediscover held-out supported cases and generate better warm starts for `n = 23` and `n = 24` than unrestricted edge-level search under the same time budget.
- Required experiments: define a minimal construction DSL; perform leave-one-out recovery on known exact witnesses; measure whether synthesized programs transfer useful structure to unsupported cases better than random initializations or plain circulant templates.
