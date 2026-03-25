# Verification Summary

## Round

- Verification phase: `review_round_1`

## Decision

DEEPEN

The current bundle is reproducible and mostly honest about its operational boundary, but it is not yet ready for publication-facing acceptance or for a lighter revise-only pass. The blocking issues are not just prose or bibliography cleanup: the witness provenance chain is still incomplete, the pair-slack benchmark has metric-accounting defects and missing controls, and no experiment has produced a new verified frontier witness or a materially distinct book-Ramsey result.

## Must-Fix Issues

1. Narrow the claim surface to what the artifacts actually support.
   - Keep the safe boundary to: a deterministic partial solver, a reproducible `42 supported / 58 unsupported` split through `n <= 100`, a negative result for the fully frozen-old lift formulation on `20 -> 21` and `21 -> 22`, and a mixed exploratory signal for exact pair-slack.
   - Remove or soften any wording that implies a new construction family, a general solver, a validated lift program, or a publication-ready novelty claim.

2. Close external provenance for the witness payloads before presenting the supported range as publication-grade.
   - Freeze the upstream source for the small exact witnesses, the graph6 bank for `n = 5..21`, and the embedded `n = 22` two-block witness.
   - Use immutable provenance records such as archived snapshots, appendices, or exact commit permalinks rather than moving repository paths.

3. Repair the citation trail on the manuscript-facing surfaces.
   - Add actual citations where prior-art and provenance comparisons are made in `results/final_report.md`, `results/literature/prior_art_review.md`, and `results/literature/prior_art_gap.md`.
   - Repair or replace weak bibliography entries before they are used in final-facing prose, especially the Wesley source record, the SAT Modulo Symmetries citation, the Black-Leven-Radziszowski record, and any stale solver or GitHub placeholders.

4. Fix benchmark metric integrity and re-export the saved pair-slack results.
   - Correct `verifier_calls` so it reports true verifier invocations rather than accepted-round count.
   - Measure runtime as end-to-end wall time for the scored run, not only the post-seed or post-model-build segment.
   - Re-export the existing benchmark outputs after the accounting fix so later comparisons are not built on mislabeled cost data.

5. Add the missing controls needed to justify any claim about the backup lane.
   - Benchmark pair-slack on `n = 23`, which is the first obvious unsupported frontier-adjacent falsifier.
   - Replace the trivial `n = 22` identity sanity check with perturb-and-recover controls from a damaged known witness.
   - Run objective ablations so the effect of `min_slack` is separated from tie-break-order changes.
   - Split move-family controls where possible, especially within-layer versus cross-layer moves, because the current failures appear under-localized in the saved artifacts.

6. Do not generalize the lift negative result beyond the tested formulation.
   - The current evidence falsifies the fully frozen-old exact completion model only.
   - Add at least one relaxed control with bounded old-old rewiring, plus a positive-control recovery case, before making broader lift-style claims.

7. Keep the novelty verdict negative unless new evidence changes the boundary.
   - No run extended the verified coverage frontier.
   - Exact pair-slack produced mixed scalar changes rather than a decisive verifier-aligned win.
   - Composite-order orbit templates remain speculative and have not crossed a frontier-relevant gate.

## Optional Improvements

- Add richer failure diagnostics to the pair-slack artifacts, including slack histograms and counts by constraint family, so the remaining obstruction is localized rather than summarized by a few scalars.
- Expand the lift stress grid to include earlier adjacent steps such as `18 -> 19` and `19 -> 20`, which would clarify whether the frozen-old failures are onset-specific or more systematic.
- Clean stale literature side files and research-context summaries so the repaired watchlist is the only active prior-art narrative.
- Replace schematic experiment-manifest commands with the exact invocations and output paths used to generate the saved benchmark files.

## Next-Round Gate

This work should stay in `DEEPEN` until the provenance chain is frozen, citations are attached at the actual comparison points, benchmark accounting is repaired, and at least the minimum missing controls (`n = 23`, perturb-and-recover, objective ablations, relaxed lift control) have been run. If those changes are completed without producing a new witness or stronger structural result, the package can still be reframed as a rigorous negative-results and verification artifact, but it is not there yet.
