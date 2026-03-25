# Verification Summary

## Decision

DEEPEN

The current bundle is internally reproducible and honest about its boundary (`42 supported / 58 unsupported` through `n <= 100`), but it is not publication-ready. The evidence supports a deterministic partial solver plus negative results on the frozen-old lift formulation, not a materially new book-Ramsey contribution.

## Must-Fix Issues

1. Narrow the claim boundary in final-facing prose.
   - Do not present the work as a new construction, a general solver, or a validated four-vertex lift.
   - Safe framing for now: deterministic partial solver, reproducible verification bundle, and negative-result package.
2. Resolve external provenance for the witness payloads.
   - Freeze the upstream source for the tiny exact witnesses (`n = 1, 2, 4`), the graph6 bank (`n = 5..21`), and the embedded `n = 22` two-block witness.
   - This is a publication blocker, not a cosmetic citation gap.
3. Attach citations to the load-bearing literature and provenance claims, and repair weak bibliography entries.
   - `results/final_report.md` and the verification/literature summaries still describe prior art and provenance without attached citation syntax.
   - Repair or replace weak entries before using them in paper-facing text, especially `LowerBoundsBookRamseyWesley2025`, `SMS`, `BlackLevenRadz`, `SCIP6`, and `VanOverbergheGithub`.
4. Fix benchmark metric integrity before making any efficiency claim.
   - The pair-slack benchmark currently misreports `verifier_calls`; it is reporting accepted-round count rather than true verifier invocations.
   - `runtime_seconds` also excludes part of the end-to-end path.
   - Re-export the benchmark after correcting the harness.
5. Add the missing frontier and control experiments before claiming backup-lane strength.
   - Pair-slack needs the omitted `n = 23` case, a perturb-and-recover control at `n = 22`, and objective ablations that isolate the effect of `min_slack`.
   - The lift lane needs a relaxed control that allows bounded old-old rewiring; the current result falsifies only the fully frozen-old submodel.
6. Keep the novelty judgment negative until new evidence appears.
   - No bounded experiment produced a new verified frontier witness.
   - Pair-slack shows only mixed scalar improvement, and the orbit-template lane has not crossed its own gate.

## Optional Improvements

- Update `results/research_context.md` so the prior-art narrative matches the repaired literature artifacts and no longer treats the string-graph papers as the active closest comparison set.
- Add failure localization for pair-slack and a broader lift stress grid (`18 -> 19` through `21 -> 22`) so the negative results become diagnostic rather than purely descriptive.
- Replace moving provenance breadcrumbs with immutable commit permalinks or archived snapshots, and either wire unused bibliography keys into final-facing prose or drop them.
- Keep the pair-slack and orbit-template lanes explicitly exploratory until they produce a verifier-aligned win or a frontier-relevant structural result.
