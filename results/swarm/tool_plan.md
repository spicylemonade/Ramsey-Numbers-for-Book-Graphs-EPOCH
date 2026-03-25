# Tool Plan

## Baseline truth sources
- Active submission path: repo-root `solution.py`.
- Legacy-only context: `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/`.
- Baseline verification commands for every milestone:
  - `python -m unittest -v test_solution.py`
  - `python solution.py --verify-supported --limit 100`
- Verified in this synthesis pass on 2026-03-25:
  - all 6 unit tests passed;
  - the support table remained 42 supported / 58 unsupported through `n <= 100`.
- Budget rule: synthesize existing specialist output first; do not re-run broad literature searches or wide frontier sweeps unless a blocker forces it.

## Role routing and budget

### Orchestrator
- Primary tools: local repo reads, `rg`, `sed`, baseline verification commands, and markdown/JSON diffs.
- Budget envelope: 30-45 minutes per coordination pass; zero broad web-search budget by default.
- Routing: keep claims about the repo-root artifact separate from the archived mixed-language tree; gate all frontier work through one champion lane and one backup only.

### Researcher
- Primary tools: exact witness bank, repo-root verifier, and one approved hypothesis implementation path at a time.
- Budget envelope: one champion experiment first, with a hard stop at the first kill switch; no parallel frontier branching.
- Routing:
  - champion path: counterexample-guided orbit refinement over symmetry-compressed templates;
  - backup path: deterministic exact pair-slack repair baseline on `n = 22`, `24`, and `50`;
  - reserve path: dual-shaped low-orbit seeding only after the champion and backup verdicts are in.

### Falsifier
- Primary tools: exact verifier, hold-out recovery harness, and the supported/unsupported regression set.
- Budget envelope: 0.5 researcher day per hypothesis.
- Routing:
  - champion kill test: held-out recovery on `n = 20`, `21`, and `22`, with verifier-call comparison against pair-slack;
  - backup kill test: require a clean deterministic win over the surrogate objective on `n = 22`, `24`, and `50`;
  - stop immediately on two held-out failures, no verifier-call advantage, or collapse into heuristic parameter tuning.

### Writer
- Primary tools: local markdown artifacts and verified command outputs only.
- Budget envelope: one concise pass after each milestone.
- Routing: describe the current artifact as a deterministic partial solver plus coverage-extension plan; always include the supported/unsupported split; never blur root-artifact claims with archive behavior.

### Reviewer
- Primary tools: diff review, claim-to-evidence matching, and reruns of the baseline verification commands.
- Budget envelope: 30 minutes per review pass.
- Routing: block any overclaim that says the full prompt is solved, any stale text that still treats the packaging complaint as open on the root artifact, and any claim that cites the archive tree as if it were the active submission path.

### Citation Auditor
- Primary tools: narrow problem-local source checks only when a writeup needs repair.
- Budget envelope: at most 4-6 high-signal source checks per milestone.
- Routing: prioritize book-Ramsey, exact-witness, symmetry-reduced SAT/IP, and benchmark sources; do not spend budget on the irrelevant string-graph retrieval drift except to label it as drift.

### Benchmark Auditor
- Primary tools: `python -m unittest -v test_solution.py`, `python solution.py --verify-supported --limit 100`, and any future deterministic hypothesis-specific regression harness.
- Budget envelope: one full `n <= 100` sweep per milestone plus a very small frontier set.
- Routing: treat unsupported values as first-class outputs, verify determinism and exact constraint checking for every claimed witness, and reject any benchmark summary that averages unsupported cases away.

## Immediate budget decision
- Packaging hygiene is no longer the main research spend. The root artifact already resolves the mixed-language and probabilistic complaint.
- Coverage is the blocker. Spend the next budget on the champion hold-out recovery gate for counterexample-guided orbit refinement, with deterministic exact pair-slack as the mandatory control.
- Do not revive the frozen-old four-vertex lift or broad stochastic search unless a materially new hypothesis is written down first.
