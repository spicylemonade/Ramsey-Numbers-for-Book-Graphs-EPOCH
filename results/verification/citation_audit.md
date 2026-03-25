# Citation Audit

## Scope

- `research_paper.tex` is not present in this repo, so this audit treats `results/final_report.md` as the manuscript surface.
- Inputs reviewed: `sources.bib`, `results/research_context.md`, `results/literature/semantic_scholar_manifest.json`, `results/literature/prior_art_review.md`, `results/literature/prior_art_gap.md`, `results/verification/novelty_report.md`, `results/verification/verification_summary.md`, and the repo-local verification/experiment artifacts they rely on.
- This audit distinguishes two kinds of support:
  - repo-internal support: tests, experiment logs, provenance ledgers, and other local artifacts;
  - external bibliographic support: sources that can carry literature-facing or provenance-facing claims in a publication-style writeup.

## Executive Summary

- Most operational claims in the current report bundle are supported by repo-local evidence.
- Publication-traceable citation support is still inadequate:
  - there is no `\cite` / Pandoc-style citation syntax in the reviewed report surfaces;
  - `results/final_report.md` and `results/verification/verification_summary.md` contain no bibliography keys at all;
  - the bibliography is therefore mostly unattached to the prose that needs it.
- The highest-risk citation gap is provenance, not theorem context:
  - the graph6 witness bank for `n = 5..21`,
  - the tiny embedded exact witnesses for `n = 1, 2, 4`,
  - the embedded `n = 22` two-block witness
  all remain unresolved as external sources.
- Several BibTeX entries are too weak or too stale to carry publication-facing claims without repair, especially `LowerBoundsBookRamseyWesley2025`, `SMS`, `BlackLevenRadz`, `SCIP6`, and `VanOverbergheGithub`.
- `results/research_context.md` is stale as a citation guide: it still lists string-graph papers as the "Closest Prior Art" even though the repaired literature artifacts classify them as retrieval drift.

## Structural Findings

### High Severity

- The manuscript surface has no attached citations.
  - `results/final_report.md` has zero inline citation markers and zero bibliography-key mentions.
  - `results/verification/verification_summary.md` has zero inline citation markers and zero bibliography-key mentions.
  - `results/literature/prior_art_review.md`, `results/literature/prior_art_gap.md`, and `results/verification/novelty_report.md` discuss literature extensively, but still do so as plain prose rather than attached citations.
- Witness provenance is still unresolved for the exact witness bank.
  - `results/verification/witness_source_audit.md:22-34` explicitly says the small exact witnesses, graph6 bank, and `n = 22` two-block witness do not yet have frozen external provenance inside the repo.
  - Any publication-facing sentence that treats those witnesses as bibliographically settled is unsupported.

### Medium Severity

- The active prior-art narrative is inconsistent across artifacts.
  - `results/research_context.md:14-18` still names four string-graph papers as "Closest Prior Art".
  - The repaired watchlist and reviews instead classify those papers as required superficial comparisons or retrieval drift: `results/literature/prior_art_watchlist.md:27-32`, `results/literature/prior_art_review.md:18-24`, `results/literature/prior_art_gap.md:5-33`, `results/verification/novelty_report.md:7-27`.
  - This does not create a false theorem claim, but it does make the citation trail ambiguous.
- `sources.bib` is not wired into the current report surfaces.
  - Most keys appear only in literature bookkeeping files such as `results/literature/literature_snapshot.json` or `results/literature/prior_art_watchlist.md`, not in the final-facing prose.
  - `BlockCircRamseyGoedVanOver` and `Kissat` do not appear in the reviewed writeup surfaces at all.

## Claim Support Ledger

| claim surface | support status | support source(s) | citation issue |
| --- | --- | --- | --- |
| `results/final_report.md:5-17` active artifact is Python-only, deterministic, partial, and currently `42 supported / 58 unsupported` over `n <= 100` | supported for internal use | `results/verification/baseline_audit.md:6-11`, `results/verification/baseline_regression.md:31-55`, `results/verification/witness_provenance.json` | supported by repo evidence, but uncited in the report |
| `results/final_report.md:11-15` supported territory is small exact witnesses + graph6 bank + `n = 22` two-block + prime-power family | partially supported | `results/verification/witness_provenance.json`, `results/verification/witness_source_audit.md:7-34` | implementation fact is supported, but external provenance for the graph6 bank / tiny witnesses / `n = 22` witness is unresolved |
| `results/final_report.md:21-24` repaired literature pass demoted string-graph papers and promoted Wesley/book-Ramsey sources; lane ranking is `four_vertex_lift`, `pair_slack_repair`, `composite_orbit_templates` | supported, but only as internal synthesis | `results/literature/literature_snapshot.json:13-17,18-217`, `results/literature/prior_art_review.md:18-27,43-53`, `results/swarm/director_brief.md:8-25`, `results/swarm/hypotheses.json` | uncited comparison language; no attached citation to Wesley or the book-Ramsey watchlist |
| `results/final_report.md:28-34` four-vertex lift failed known-step recovery and pair-slack remained weak | supported for internal use | `results/experiments/four_vertex_lift_known_steps.md:9-14`, `results/experiments/pair_slack_benchmark.md:13-29`, `results/verification/benchmark_report.md:6-21` | experiment claims are correct but uncited in the final report |
| `results/final_report.md:45-47` provenance remains unresolved and runtime logs are not publication-grade benchmarks | supported | `results/verification/witness_source_audit.md:20-40`, `results/verification/baseline_regression.md:50-55` | should cite these artifacts explicitly if the report is shared externally |
| `results/literature/prior_art_review.md:9-16` Wesley is the main backbone and proves the exact `n <= 20` plus prime-power regime | partially supported | `results/literature/literature_snapshot.json:18-29`, `sources.bib:1-6` | literature-facing theorem claim is not attached to a real citation in the prose; current BibTeX record is only a placeholder manuscript note |
| `results/literature/prior_art_gap.md:43-59` and `results/verification/novelty_report.md:31-49` compare the repo against Rousseau-Sheehan, Conlon, Conlon-Fox-Wigderson, Chen-Lin, Liu-Li, and small exact/computational sources | partially supported | `sources.bib:8-114`, `results/literature/literature_snapshot.json:30-167` | these are uncited comparisons; source names are present, but no citation syntax ties claims to records |
| `results/research_context.md:14-18` the string-graph papers are the closest prior art | not supported as the active citation position | contradicted by `results/literature/prior_art_watchlist.md:27-32`, `results/literature/prior_art_review.md:18-24`, `results/verification/novelty_report.md:7-27` | stale context summary; should not be used as a citation-support artifact |

## Missing Citations And Uncited Comparisons

- `results/final_report.md:21-24`
  - Needs attached citations for:
    - Wesley as the closest problem-local source,
    - the classical book-Ramsey baseline,
    - the asymptotic/problem-local book papers,
    - the internal swarm artifacts that justify the lane ranking.
- `results/literature/prior_art_review.md:10-13`
  - The strongest literature-facing claim in the repo states that Wesley proves the almost-diagonal result for `n <= 20` and the prime-power family while not solving all `n`.
  - That sentence currently has no citation attached even though it is one of the most load-bearing statements in the writeup.
- `results/literature/prior_art_gap.md:43-59`
  - The comparisons to Rousseau-Sheehan, Conlon, Conlon-Fox-Wigderson, Chen-Lin, Liu-Li, and the small exact/computational sources are all uncited comparisons.
- `results/verification/novelty_report.md:31-49`
  - The overlap/differentiation discussion names the right papers, but it still does not cite them.
- Any claim about the origin of the graph6 bank or the `n = 22` tuple is still citation-blocked rather than merely citation-missing.
  - The issue is not "forgot to cite".
  - The issue is "the upstream source has not been pinned yet".

## Weak Citations And Likely Citation Hallucinations

- `sources.bib:1-6` `LowerBoundsBookRamseyWesley2025`
  - Real source class, but weak record.
  - The entry is only a manuscript note.
  - A canonical replacement now appears to exist: the arXiv preprint `2410.03625` and a final ScienceDirect / Discrete Mathematics record for "Lower bounds for book Ramsey numbers".
- `sources.bib:116-121` `SMS`
  - Likely garbled citation record.
  - `author = {Anders and Others}` is placeholder-quality metadata, not a stable bibliographic record.
  - If this source is kept, replace it with the actual Kirchweger-Szeider metadata for either the CP 2021 paper or the later journal version.
- `sources.bib:82-87` `BlackLevenRadz`
  - Likely garbled or stale record.
  - It has no venue, no DOI, and no page data.
  - The current `1996` note-only form is too weak to carry any concrete claim and appears inconsistent with the actual `JCMCC` volume-78 record.
- `sources.bib:123-128` `SCIP6`
  - Weak software citation.
  - It is acceptable only as tooling context, not as support for mathematical claims.
  - The metadata are too lightweight for a formal bibliography and appear to lag the actual 2018 release report for version 6.0.
- `sources.bib:137-143` `VanOverbergheGithub`
  - Provenance-relevant but weak.
  - It points at a moving branch path instead of an immutable commit, release, or archived snapshot.
  - Good enough for a local breadcrumb, not good enough for frozen provenance.
- `sources.bib:153-159` `EpochBookGraphsBenchmark`
  - Scope-limited citation.
  - This supports benchmark framing only.
  - It does not support theorem claims, provenance claims, or claims that a witness is correct.

## Most Important Concrete Sources To Add Or Repair

1. Replace `LowerBoundsBookRamseyWesley2025` with the canonical Wesley record.
   - Preprint fallback: `arXiv:2410.03625`.
   - Prefer the final journal record if that is the version actually being cited: "Lower bounds for book Ramsey numbers", `Discrete Mathematics`, DOI `10.1016/j.disc.2025.114913`.
2. Freeze the exact upstream source for the graph6 witness bank (`n = 5..21`).
   - Best case: a paper appendix or dataset with those exact witness payloads.
   - Acceptable fallback: an immutable commit permalink or archive snapshot for the `circulant-Ramsey` `Books` directory.
3. Freeze the exact upstream source for the embedded `n = 22` two-block witness.
   - The repo currently proves only that the tuple works, not where it came from.
4. Repair `SMS` with a full conference citation.
   - This entry is currently too placeholder-like to trust.
   - The likely replacement is Markus Kirchweger and Stefan Szeider, "SAT Modulo Symmetries for Graph Generation" (CP 2021 / LIPIcs), or the later journal version "SAT Modulo Symmetries for Graph Generation and Enumeration" (`ACM TOCL`, 2024, DOI `10.1145/3670405`), depending on which source is actually intended.
5. Repair `BlackLevenRadz` with the correct paper metadata before using it in any publication-facing argument.
   - The current entry appears to correspond to Kevin Black, Daniel Leven, and Stanislaw Radziszowski, "New Bounds on Some Ramsey Numbers", `JCMCC` 78 (2011), pp. 213-222.
6. Repair `SCIP6` if solver-stack discussion remains in scope.
   - The relevant official record is the 2018 report "The SCIP Optimization Suite 6.0" rather than the current lightweight team placeholder.
   - Otherwise remove it from the bibliography to avoid clutter.
7. Attach inline citations to the literature-facing comparisons.
   - Especially the Wesley/Rousseau-Sheehan/Conlon-family comparison block in `prior_art_review.md`, `prior_art_gap.md`, `novelty_report.md`, and the summary paragraph in `final_report.md`.

## Bottom Line

- Internal evidence traceability is mostly adequate.
- External citation traceability is not yet publication-ready.
- The main blockers are:
  - missing attached citations for the load-bearing literature claims,
  - unresolved provenance for the embedded witness data,
  - several weak or garbled BibTeX records that should be repaired before the repo is treated as a paper-ready source bundle.
