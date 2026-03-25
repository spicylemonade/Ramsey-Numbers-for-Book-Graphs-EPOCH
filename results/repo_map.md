# Repo Map

## Active Execution Path

- `solution.py` — `active`
  - Root submission artifact.
  - Exposes `solution(n: int) -> str`.
  - CLI path `python solution.py --verify-supported --limit 100` calls `_main()`, which calls `_supported_values()`, which repeatedly calls `solution()` and `_verify_book_constraints()`.
  - Imports only `argparse` and `itertools.product`.
- `test_solution.py` — `active`
  - Root regression harness.
  - Imports `solution as solver`.
  - Verifies deterministic output samples, the full supported/unsupported table for `n <= 100`, and import/codegen hygiene for the active root module.

The active execution path is explicitly the root pair `solution.py` and `test_solution.py`. No root code imports from `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/`.

## Repo Root

- `research_rubric.json` — `generated`
  - Pipeline status tracker for this research run.
- `TASK_researcher_attempt_1.md` — `generated`
  - Task handoff/instructions for the current researcher pass.
- `figures/` — `generated`
  - Empty publication-output directory in this run.
- `__pycache__/` — `generated`
  - Python bytecode cache.

## `.archivara/`

- `.archivara/concept_evolve.py` — `helper`
  - Structured concept-exploration helper used by the research pipeline.
  - Launches Codex child agents and writes artifacts under `results/concept_evolve/`.
- `.archivara/semantic_scholar.py` — `helper`
  - Semantic Scholar CLI/cache helper.
  - Updates `results/literature/semantic_scholar_manifest.json`.
- `.archivara/cache/semantic_scholar/*.json` — `generated`
  - Cached API responses.
- `.archivara/logs/*.log` — `generated`
  - Prior orchestrator/swarm logs from this workspace.

## `results/`

- `results/research_context.md` and `results/research_context.json` — `generated`
  - Current run context and progress summary.
- `results/literature/*.json|*.md` — `generated`
  - Literature snapshot, watchlist, gap notes, and manifest memory.
- `results/swarm/*.md|*.json` — `generated`
  - Director brief, hypotheses, tool routing, and falsifier notes.
- `results/verification/*.md|*.json` — `generated`
  - Verification artifacts for the active root solver.
- `results/concept_evolve/` — `generated`
  - Concept-evolution outputs and helper state.

## `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/`

- `solution.py` — `legacy`
  - Older deterministic packer variant inside the archive tree.
  - Not imported by the root execution path.
- `search.py`, `search_fast.py`, `search_np.py`, `search_v2.py` — `legacy`
  - Stochastic/heuristic search scripts; several import `random` and/or `numpy`.
- `solve.c`, `search.c`, `csearch.c`, `cs.c`, `check_all.c`, `check_all2.c` — `legacy`
  - C search/check programs from the archived exploration tree.
- `solve`, `search`, `csearch`, `cs`, `check_all`, `check_all2` — `legacy`
  - Built binaries from the archived C programs.
- `test_n4.py`, `test_n4_direct.py`, `test_n4_fast.py`, `test_n4_v2.py`, `test_small.py` — `legacy`
  - Archive-local experiments/tests.
- `README.md`, `lakefile.toml`, `lean-toolchain`, `lake-manifest.json`, `ARISTOTLE_SUMMARY_*`, `@PaxHeader` — `legacy`
  - Archive metadata and toolchain residue.

## Import / Execution Connections

- `test_solution.py -> solution.py`
- `solution.py` does not import any archive module, external binary, random source, or code-generation helper.
- `.archivara/concept_evolve.py -> results/concept_evolve/*`
- `.archivara/semantic_scholar.py -> results/literature/semantic_scholar_manifest.json`
- `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/*` is disconnected from the active root solver unless a user manually enters that tree.
