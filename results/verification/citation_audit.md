# Citation Audit

## Scope

- Review round: `review_round_1`.
- `research_paper.tex` is not present in this repo, so this audit treats `results/final_report.md` as the manuscript-facing surface and also reviews:
  - `sources.bib`
  - `results/research_context.md`
  - `results/literature/semantic_scholar_manifest.json`
  - `results/verification/verification_summary.md`
  - `results/literature/prior_art_review.md`
  - `results/literature/prior_art_gap.md`
  - `results/verification/novelty_report.md`
  - the repo-local verification and experiment artifacts those files rely on.
- Focus: evidence traceability and citation support only. This audit does not comment on prose quality except where citation status changes what a claim is allowed to say.

## Executive Summary

- Most operational claims are backed by repo-internal evidence.
- Publication-facing citation support is still not ready:
  - `results/final_report.md:5-47`, `results/literature/prior_art_review.md:7-30`, and `results/literature/prior_art_gap.md:37-66` contain no citation syntax at all.
  - `results/verification/verification_summary.md:17-19` and `results/verification/novelty_report.md:21-25` mention BibTeX keys in prose, but raw key names are not a citation trail.
- The highest-risk blocker is witness provenance.
  - The small exact witnesses, the graph6 bank for `n = 5..21`, and the embedded `n = 22` two-block witness are internally reproducible but not externally frozen; see `results/verification/witness_source_audit.md:20-40`.
- `sources.bib` contains two likely corrupted or placeholder records and several weak publication-facing records:
  - likely corrupted / hallucinated metadata: `SMS`, `BlackLevenRadz`
  - weak or version-muddled records: `LowerBoundsBookRamseyWesley2025`, `SCIP6`, `VanOverbergheGithub`
- The manifest layer is not citation-grade.
  - `results/literature/semantic_scholar_manifest.json:3-244` still mixes polluted search history with contradictory zero-result queries for real problem-local titles.
  - `results/literature/literature_snapshot.json:18-187` repairs the watchlist, but the active `top_papers` and `code_artifacts` records still omit canonical identifiers such as DOI, arXiv ID, or URL.
- `results/research_context.md:14-18` is stale and should not be used as prior-art support until it is brought into line with the repaired watchlist in `results/literature/prior_art_watchlist.md:8-19`.

## Key Claim Support

### 1. Active artifact is a deterministic partial solver

- Claim surface:
  - `results/final_report.md:5-17`
  - `results/literature/prior_art_review.md:7-8`
  - `results/verification/novelty_report.md:21`
- Internal support:
  - `results/verification/baseline_regression.md:17-55`
  - `results/verification/coverage_delta.md:5-15`
  - `results/swarm/director_brief.md:3-6`
- Citation status:
  - Adequately supported for repo-internal reporting.
  - No external literature citation is required for the packaging claim itself.
  - The phrase "published prime-power family" in `results/final_report.md:7` does require a real literature citation to Wesley or equivalent source.

### 2. Supported territory is small exact witnesses, graph6 bank, `n = 22`, and the prime-power family

- Claim surface:
  - `results/final_report.md:11-15`
  - `results/literature/prior_art_review.md:12-16`
- Internal support:
  - `results/verification/witness_provenance.json`
  - `results/verification/witness_source_audit.md:7-34`
- Citation status:
  - Partially supported.
  - The prime-power family can be cited externally.
  - The exact source of the small exact witnesses, graph6 bank, and embedded `n = 22` tuple is still unresolved, so publication-facing prose must not imply those payloads are bibliographically frozen.

### 3. Wesley is the problem-local backbone and the current repo does not solve the full all-`n` problem

- Claim surface:
  - `results/final_report.md:21-24`
  - `results/literature/prior_art_review.md:9-16`
  - `results/literature/prior_art_gap.md:37-53`
- Internal support:
  - `results/literature/prior_art_watchlist.md:8-19`
  - `results/literature/literature_snapshot.json`
- Citation status:
  - Externally supportable, but currently under-cited.
  - The load-bearing Wesley paragraph in `results/literature/prior_art_review.md:9-13` is one of the most important missing citations in the repo.
  - The comparison against Rousseau-Sheehan, Conlon, Conlon-Fox-Wigderson, Chen-Lin, and Liu-Li is present as prose, not as attached citations.

### 4. The fixed-old four-vertex lift failed known-step recovery and pair-slack did not extend the frontier

- Claim surface:
  - `results/final_report.md:28-41`
  - `results/literature/prior_art_gap.md:61-66`
  - `results/verification/novelty_report.md:22-24`
- Internal support:
  - `results/experiments/four_vertex_lift_known_steps.md:9-14`
  - `results/experiments/pair_slack_benchmark.md:13-29`
  - `results/verification/benchmark_report.md:6-18`
  - `results/verification/coverage_delta.md:5-22`
- Citation status:
  - Strongly supported internally.
  - These claims mainly need explicit artifact references, not outside literature citations.
  - If these results are moved into a paper-style manuscript, they should cite the experiment artifacts directly rather than appearing as unsupported narrative.

### 5. Provenance remains unresolved for the embedded witness payloads

- Claim surface:
  - `results/final_report.md:45-47`
  - `results/literature/prior_art_review.md:13`
  - `results/verification/novelty_report.md:47-49`
  - `results/verification/verification_summary.md:14-19`
- Internal support:
  - `results/verification/witness_source_audit.md:20-40`
- Citation status:
  - Internally supported.
  - Externally blocked, not merely citation-missing.
  - `results/verification/novelty_report.md:49` currently cites `results/verification/citation_audit.md` as part of the evidence chain; that is circular and should be replaced with `results/verification/witness_source_audit.md` plus the eventual upstream provenance records.

## Missing Citations And Uncited Comparisons

- `results/final_report.md:21-24`
  - "The real local backbone is Wesley's lower-bound work together with the classical and asymptotic book-Ramsey literature" is a literature comparison with no attached citations.
  - Minimum source set to attach here:
    - Wesley for the almost-diagonal target and known solved territory,
    - Rousseau-Sheehan for the classical baseline,
    - at least one modern book-Ramsey paper from the Conlon / Conlon-Fox-Wigderson / Chen-Lin / Liu-Li line.
- `results/final_report.md:7,11-15`
  - "published prime-power family" needs a real citation.
  - "graph6 witness bank" and the embedded `n = 22` witness need exact upstream provenance, not just a generic bibliography entry.
- `results/literature/prior_art_review.md:9-13`
  - The Wesley theorem-and-method summary is load-bearing and currently uncited.
  - This paragraph should not rely on `sources.bib:1-6` in its current placeholder form.
- `results/literature/prior_art_gap.md:43-59`
  - The Rousseau-Sheehan / Conlon-family / small exact-computation comparison block is an uncited comparison section.
  - The problem is not that the paper names are wrong; the problem is that none of the named sources are actually attached to the claims.
- `results/verification/novelty_report.md:21-25`
  - The table mentions BibTeX keys such as `RousseauSheehanRamseyBooksOriginal` and `Conlon_BookRamsey`, but key names rendered as plain text are not citations.
- `results/verification/verification_summary.md:17-19`
  - This file correctly identifies weak entries, but it does so by naming keys in prose rather than by linking them to repaired bibliography data or citations in a manuscript surface.

## Weak Citations And Likely Citation Hallucinations

- `sources.bib:1-6` `LowerBoundsBookRamseyWesley2025`
  - Real source class, but weak and version-muddled.
  - The current record is only a note field.
  - The repo should choose one version and cite it consistently:
    - arXiv preprint `2410.03625` if the cited object is the 2024 preprint, or
    - the related journal article with DOI `10.1016/j.disc.2025.114913` if the cited object is the final journal version.
- `sources.bib:82-87` `BlackLevenRadz`
  - Likely corrupted / hallucinated metadata.
  - The current entry says `1996`, gives no venue, and uses first names that do not match the canonical publication metadata.
  - This is not safe to cite until repaired.
- `sources.bib:116-121` `SMS`
  - Likely placeholder / hallucinated metadata.
  - `author = {Anders and Others}` is not publication-grade metadata.
  - The entry lacks `booktitle`, venue data, page data, and DOI.
- `sources.bib:123-128` `SCIP6`
  - Weak placeholder tool citation.
  - It is too vague for formal bibliography use and appears stale relative to the official SCIP 6.0 report.
  - Fine as an internal reminder; not fine as a paper-facing citation without repair.
- `sources.bib:137-143` `VanOverbergheGithub`
  - Traceability breadcrumb only.
  - It points to a moving branch path, not an immutable commit, release, or archive snapshot.
  - That is not enough for witness provenance.

## Concrete Repairs To Make

1. Replace `LowerBoundsBookRamseyWesley2025` with a canonical record.
   - If citing the preprint: use arXiv `2410.03625`.
   - If citing the journal article: use DOI `10.1016/j.disc.2025.114913`.
   - Do not mix preprint and journal metadata in one skeletal entry.

2. Replace `SMS` with the actual CP 2021 citation.
   - Markus Kirchweger and Stefan Szeider.
   - "SAT Modulo Symmetries for Graph Generation."
   - 27th International Conference on Principles and Practice of Constraint Programming (CP 2021), LIPIcs 210, DOI `10.4230/LIPIcs.CP.2021.34`.

3. Repair `BlackLevenRadz` before using it anywhere.
   - Canonical metadata point to:
   - Kevin Black, Daniel Leven, and Stanislaw P. Radziszowski.
   - "New Bounds on Some Ramsey Numbers."
   - *Journal of Combinatorial Mathematics and Combinatorial Computing*, Volume 78 (2011), pp. 213-222.

4. Repair `SCIP6` if solver-stack discussion remains in scope.
   - Use the official SCIP 6.0 report rather than the current `SCIP Team` placeholder.
   - If solver tooling is not part of the manuscript claim surface, remove the entry instead of carrying a weak citation.

5. Freeze the graph6 witness bank to an immutable provenance source.
   - Best case: cite the actual paper appendix or dataset that contains the witness payloads.
   - Acceptable fallback: the exact commit permalink or archived snapshot for the `circulant-Ramsey/RamseyGraphs/Books` path actually used to source the payloads.

6. Freeze the embedded `n = 22` two-block witness to its real upstream source.
   - The repo currently proves that the tuple works.
   - It does not yet prove where the tuple came from.

7. Attach citations where the literature comparisons actually occur.
   - Highest-value insertion points:
     - `results/final_report.md:21-24`
     - `results/literature/prior_art_review.md:9-16`
     - `results/literature/prior_art_gap.md:43-59`
     - `results/verification/novelty_report.md:21-25`

## Manifest And Metadata Limits

- `results/literature/semantic_scholar_manifest.json:47-133`
  - The manifest still records giant task-prompt queries and other polluted retrieval history from the earlier drifted run.
  - That history is useful for debugging retrieval, but it is not a canonical citation source.
- `results/literature/semantic_scholar_manifest.json:225-243`
  - The manifest logs `0` results for real problem-local titles such as "On Ramsey numbers for books" and "New upper bounds for Ramsey numbers of books".
  - Those lines should not be interpreted as evidence that the papers lack identifiers or are unavailable.
- `results/literature/literature_snapshot.json:18-187`
  - The repaired snapshot correctly surfaces the right watchlist, but the active records store only lightweight title/author/year/notes fields.
  - If this snapshot is meant to support later citation automation, it should carry canonical identifiers such as DOI, arXiv ID, and stable URLs.
- `results/concept_evolve/tree/phase_2_baseline/witness_provenance_controls/literature.json:7-9`
  - This provenance-control side file still stores `paperId: "unknown"` for `On Ramsey Numbers for Books`.
- `results/concept_evolve/tree/003_witness-provenance-ledger/literature.json:7-9`
  - This file still carries an unrelated string-graph paper.
  - Until those side files are cleaned, they should not be treated as citation support artifacts.

## Lower-Priority Traceability Cleanup

- `results/research_context.md:14-18` still lists four string-graph papers as "Closest Prior Art" even though the repaired literature package treats them as retrieval drift only; compare `results/literature/prior_art_watchlist.md:27-32`.
- `sources.bib:130-135` `Kissat` is incomplete and currently not used by the reviewed manuscript-facing surfaces. Repair it if solver citations stay in scope, otherwise drop it.
- `sources.bib:106-114` `BlockCircRamseyGoedVanOver` is also not wired into the reviewed claim surfaces. Unused keys are not a direct citation failure, but they make the bibliography look more finished than the prose actually is.

## Bottom Line

- Internal evidence traceability is mostly adequate.
- External citation traceability is not yet publication-ready.
- The main blockers are:
  - missing attached citations for the load-bearing literature comparisons,
  - unresolved external provenance for the embedded witness payloads,
  - weak or corrupted bibliography records that should not be treated as paper-ready.
