# Citation Audit

## Scope

This audit covers the literature, experiment, and final-summary artifacts produced in this run:
- `results/literature/literature_snapshot.json`
- `results/literature/prior_art_review.md`
- `results/literature/prior_art_gap.md`
- `results/verification/baseline_audit.md`
- `results/verification/benchmark_report.md`
- `results/verification/novelty_report.md`
- `results/final_report.md`
- `results/verification/verification_summary.md`

## Bibliography Status

- `sources.bib` exists and currently contains `19` entries.
- The bibliography is deep enough for this run's scope: problem-local book-Ramsey papers, small-case computational sources, and the code/benchmark artifacts actually consulted.

## Claims Adequately Supported For Internal Use

- The active root artifact is Python-only, deterministic, and partial.
- The verified support table over `n <= 100` is `42 supported / 58 unsupported`.
- Wesley is the main problem-local backbone for the prime-power/block-circulant family and the modern lower-bound context.
- The fixed-old four-vertex lift failed its known-step gate, and the exact pair-slack baseline did not produce a new witness.

## Remaining Citation Or Provenance Gaps

- The external bibliographic provenance of the embedded graph6 witness bank for `n = 5..21` is still unresolved in repo-local form. This is documented in `results/verification/witness_source_audit.md`, and publication-facing prose must not pretend those entries are frozen.
- The embedded exact two-block witness for `n = 22` is verifier-safe in code but still lacks a fully frozen external citation inside the repo. Do not describe it as a new result or as bibliographically settled.
- The tiny exact witnesses for `n = 1`, `2`, and `4` are locally embedded and verified, but their external source trail is not yet pinned in `sources.bib`.
- `LowerBoundsBookRamseyWesley2025` is currently represented as a consulted manuscript/preprint entry. If a canonical journal or arXiv citation is needed for external publication, replace the placeholder note with the final bibliographic record.
- `SMS`, `SCIP6`, and the benchmark/code entries are sufficient for internal audit trails, but some metadata remains lightweight. They should not carry theorem claims by themselves.
- The benchmark page entry supports workload framing only. It does not support mathematical claims about validity or optimality.

## Publication Gate

- No current final artifact relies on the unresolved witness-provenance entries to claim a new theorem or full solution.
- Before external publication, the graph6 bank, the `n = 22` witness, and the tiny exact witnesses should either receive precise citations or be described only as repo-embedded verified data with unresolved upstream provenance.

## Cross-References

- Provenance ledger: `results/verification/witness_provenance.json`
- Source audit: `results/verification/witness_source_audit.md`
- Experiment evidence: `results/verification/benchmark_report.md`
- Novelty boundary: `results/verification/novelty_report.md`
- Claim-language gate: `results/verification/verification_summary.md`
