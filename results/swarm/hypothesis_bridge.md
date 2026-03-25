# Hypothesis Bridge

Pivot away from the current BP/SDP/DSL overlap. The strongest bridge candidates should exploit the verified witness bank and exact verifier, but borrow structure from more distant fields than local search, semidefinite seeding, or construction-program enumeration.

## 1. Delsarte-MacWilliams Dual Shaping for Low-Orbit Witnesses
- Title: Use coding-theory dual spectra to design book-Ramsey templates before any edge-level search.
- Closest prior art: the repo already has Paley/two-block finite-field constructions, orbit-compressed search, and an SDP-seeding idea; the overlap is only at the level of using a low-dimensional template.
- Why it is different: the pivot is to association-scheme and coding-theory dual variables, not matrix relaxations or residue heuristics. Instead of guessing difference sets directly, solve for admissible correlation spectra over cyclic or dihedral classes and round those spectra into candidate templates. That makes the seed generator a discrete dual-certificate problem rather than a continuous SDP or a local swap search.
- Falsifiable prediction: on `n = 23`, `24`, and `50`, dual-shaped seeds will start with strictly better verifier-aligned slack profiles than the current Paley-style or pair-slack seeds, and at least one of those cases will admit a smaller exact-search neighborhood after rounding.
- Required experiments: formulate an LP over orbit-count or correlation variables for two-block and small multi-orbit templates; fit and round spectra using the verified witness bank through `n = 22`; compare initial slack histograms, restricted-search dimension, and final solve rate against the current seed candidate and Paley-family starts.

## 2. Counterexample-Guided Orbit Refinement
- Title: Treat witness search like CEGAR over symmetry-compressed graph templates.
- Closest prior art: this touches the repo's exact pair-slack repair and deterministic-submission DSL directions, but those still optimize or enumerate inside a fixed representation once the template is chosen.
- Why it is different: the bridge is formal verification rather than local optimization. Start from a coarse abstract domain such as two-block, dihedral, or small orbit partitions; let the exact verifier return violating pair types; then refine only the abstract template dimensions needed to separate those counterexamples. This pivots away from polishing the killed fixed-old lift and away from flat neighborhood search.
- Falsifiable prediction: for held-out supported cases near the frontier and for unsupported `n = 23` and `24`, CEGAR-style refinement will reach either a verified witness or a proof that the template family is dead using fewer exact verifier calls than pair-slack local repair on the same starting family.
- Required experiments: define an abstract template lattice over orbit partitions and pair-type budgets; lift verifier failures into abstract counterexample clauses; run leave-one-out recovery on known supported cases such as `n = 20`, `21`, and `22`; then compare verifier calls, runtime, and template-pruning rate on `n = 23` and `24` against pair-slack repair.

## 3. Sparse Support Tomography on Residue Classes
- Title: Use compressed-sensing style support recovery to find which orbit classes actually control the worst violations.
- Closest prior art: the nearest overlap is pair-slack repair plus orbit-compressed search, because both already assume that only a structured subset of edge classes matters.
- Why it is different: the pivot is experimental design and sparse recovery rather than greedy repair. Apply a deterministic batch of perturbations to `d11` and `d12` residue classes around a seed, measure the resulting exact slack deltas, and recover a small influence support before launching exact search. That is a stronger claim than “swap promising classes”: it assumes the repair signal is sparse and should be identified first.
- Falsifiable prediction: on `n = 24` and `50`, a recovered support of at most about 10 influential residue classes will produce better min-slack progress per exact verifier call than the unrestricted pair-slack neighborhood, and if the support is not sparse the hypothesis dies quickly.
- Required experiments: build a deterministic perturbation matrix over residue classes around the current exact-slack seed; record verifier-aligned slack responses; recover influential classes with a fixed sparse-recovery procedure; rerun exact search restricted to that subspace; compare min-slack trajectory, verifier calls, and solve rate against the current pair-slack benchmark.
