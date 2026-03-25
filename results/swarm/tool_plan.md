# Tool Plan

## Baseline routing
- Treat the root `solution.py` as the active submission artifact. Treat `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/` as legacy-only context.
- Local shell checks are the source of truth for packaging and coverage. The current baseline command set is `python -m unittest -v test_solution.py` and `python solution.py --verify-supported --limit 100`.
- External search budget stays narrow and problem-local. The current watchlist drifted into irrelevant string-graph literature, so no wide query expansion is allowed without a blocker.

## Role routing and budget

### Orchestrator
- Primary tools: local repo reads, `rg`, `sed`, targeted `python` verification commands.
- Budget envelope: 30-60 minutes per synthesis pass; zero broad web-search budget by default.
- Deliverable: keep the supported/unsupported split explicit and prevent legacy archive evidence from contaminating claims about the root artifact.

### Researcher
- Primary tools: exact witness tables, `solution.py`, targeted SAT/IP or restricted construction code only after approval of a single hypothesis.
- Budget envelope: one champion experiment first, with a hard stop after the first falsifier check; no parallel frontier branching.
- Routing:
  - Champion path: four-vertex lift completion over old-new and new-new incidences.
  - Backup path: exact pair-slack repair baseline on `22`, `24`, and `50`.
  - Reserve path: composite-order orbit templates only if witness mining reveals a stable low-orbit signal.

### Falsifier
- Primary tools: exact verifier, targeted frontier cases, regression checks on known-step recovery.
- Budget envelope: 0.5 researcher day per hypothesis.
- Deliverable: kill a direction quickly if it fails known-step recovery, collapses into heuristic tuning, or overlaps the Paley/circulant lane without new substance.

### Writer
- Primary tools: local markdown artifacts and verified command outputs only.
- Budget envelope: one concise pass after each research cycle.
- Deliverable: phrase the artifact correctly as a deterministic partial solver plus frontier plan; never call it a full all-`n` solution unless coverage actually changes.

### Reviewer
- Primary tools: diff review, claim-to-evidence matching, local reruns of the baseline verification commands.
- Budget envelope: 30 minutes per review pass.
- Deliverable: block overclaims, stale plan text, and any mixing of root-artifact claims with legacy archive behavior.

### Citation auditor
- Primary tools: targeted literature lookup only if needed to repair the drifted watchlist.
- Budget envelope: at most 4-6 high-signal sources focused on book-Ramsey, exact witnesses, and symmetry-reduced SAT/IP search.
- Deliverable: replace irrelevant string-graph references with problem-local sources before any novelty-heavy writeup.

### Benchmark auditor
- Primary tools: `python -m unittest -v test_solution.py`, `python solution.py --verify-supported --limit 100`, and any future hypothesis-specific regression harness.
- Budget envelope: one full `n <= 100` sweep per milestone plus a small frontier set.
- Deliverable: maintain the deterministic support table, verify every claimed witness exactly, and report unsupported values explicitly instead of averaging them away.

## Current budget decision
- Do not spend more budget on proving that the root artifact is now Python-only and deterministic; that issue is already resolved by local tests.
- Spend the next research budget on extending coverage beyond the exact-witness and prime-power regime, starting with the four-vertex lift champion and using exact pair-slack repair as the first fallback.
