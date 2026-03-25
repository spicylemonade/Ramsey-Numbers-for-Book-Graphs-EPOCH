# Prior Art Gap Analysis

This file was repaired on 2026-03-25 after the literature snapshot drifted into generic string-graph retrieval noise. It now records both the required superficial comparisons and the actual book-Ramsey gap.

## A. Required Superficial Comparisons

### 1. String Graph Obstacles of High Girth and of Bounded Degree (2025)
- Why it was retrieved: token overlap on `graph`, `string`, and `algorithm`.
- Actual topic: string-graph structure, not book-Ramsey witness construction.
- Differentiation hypothesis: no substantive overlap with the triangular book Ramsey problem.
- Evidence artifact(s): `results/literature/literature_snapshot.json`, `results/swarm/falsifier.md`.
- Pivot decision: no pivot; treat as retrieval drift only.

### 2. Quantum Based Grover's Algorithm and Graph Coloring in Unstructured Searches for Bit String Validation (2025)
- Why it was retrieved: token overlap on `graph`, `solution`, and `bit string`.
- Actual topic: quantum / coloring workflow unrelated to book-Ramsey constructions.
- Differentiation hypothesis: no problem-local overlap.
- Evidence artifact(s): `results/literature/literature_snapshot.json`, `results/swarm/falsifier.md`.
- Pivot decision: no pivot; treat as retrieval drift only.

### 3. FSG: Fast String Graph Construction for De Novo Assembly (2016)
- Why it was retrieved: token overlap on `graph`, `string`, and `construction`.
- Actual topic: bioinformatics string-graph construction.
- Differentiation hypothesis: no book-Ramsey overlap.
- Evidence artifact(s): `results/literature/literature_snapshot.json`, `results/swarm/falsifier.md`.
- Pivot decision: no pivot; treat as retrieval drift only.

### 4. A 1.9999-Approximation Algorithm for Vertex Cover on String Graphs (2024)
- Why it was retrieved: token overlap on `graph` and `algorithm`.
- Actual topic: approximation algorithms on string graphs.
- Differentiation hypothesis: no substantive overlap with the planned witness-construction directions.
- Evidence artifact(s): `results/literature/literature_snapshot.json`, `results/swarm/falsifier.md`.
- Pivot decision: no pivot; treat as retrieval drift only.

## B. Problem-Local Gap

### 1. Lower Bounds for Book Ramsey Numbers (Wesley)
- Why it is close: exact same almost-diagonal target `R(B_{n-1},B_n)` with block-circulant, SAT, IP, and SMS methods.
- Differentiation hypothesis: before Phase 4, the strongest novelty candidate was a fixed-old-graph `n -> n+1` completion model rather than repackaging exact witnesses or the prime-power family.
- Evidence artifact(s): `results/swarm/director_brief.md`, `results/swarm/hypotheses.json`, `results/experiments/lift_20_21.json`, `results/experiments/lift_21_22.json`.
- Pivot decision: current root artifact is not novel theory; the fixed-old-graph four-vertex lift failed the known-step kill switch and should be treated as killed in its current form.

### 2. On Ramsey Numbers for Books (Rousseau-Sheehan)
- Why it is close: classical upper-bound source for the almost-diagonal case and the baseline algebraic lower-bound territory.
- Differentiation hypothesis: any future novelty must extend beyond the classical upper-bound / Paley baseline, not restate it.
- Evidence artifact(s): `results/literature/prior_art_review.md`, `results/verification/verification_summary.md`.
- Pivot decision: no pivot needed; keep as baseline theorem context.

### 3. Problem-local asymptotic book papers (Conlon; Conlon-Fox-Wigderson; Chen-Lin; Liu-Li)
- Why they are close: they are genuine book-Ramsey sources and form the correct mathematical neighborhood for claims about books.
- Differentiation hypothesis: these papers are theory/upper-bound/asymptotic context; they do not justify new constructive witness claims by themselves.
- Evidence artifact(s): `results/literature/literature_snapshot.json`, `results/verification/novelty_report.md`.
- Pivot decision: no pivot; use them as claim-boundary and context sources.

### 4. Small exact/computational sources (Shao-Xu-Bo-Pan; Black-Leven-Radz; Lidicky-McKinley-Pfender-Van Overberghe)
- Why they are close: they are the nearest overlap for small exact witness search and heuristic claims.
- Differentiation hypothesis: exact-slack repair is methodologically different only in a narrow sense because it scores moves with the verifier's exact per-pair slack under deterministic tie-breaking rather than a surrogate violation count; that difference matters scientifically only if it beats the surrogate baseline on `22`, `24`, and `50`.
- Evidence artifact(s): `results/experiments/pair_slack_benchmark.md`, `results/verification/benchmark_report.md`.
- Pivot decision: keep alive only as a weaker backup lane; current bounded benchmark shows mixed objective improvements but no frontier witness.

## C. Post-Experiment Update
- Four-vertex lift known-step recovery was run as an exact fixed-old-graph completion experiment.
- `20 -> 21` returned `INFEASIBLE` in about three seconds.
- `21 -> 22` returned `INFEASIBLE` in about four seconds.
- Under the director kill switch, that is enough to kill the champion lane in its current fixed-old-graph form before spending budget on `22 -> 23`.
- Exact pair-slack repair produced a better worst-case slack than the surrogate-style baseline on `24` and `50`, but neither run found a valid witness, so it remains a weaker fallback rather than a verified coverage extension.
