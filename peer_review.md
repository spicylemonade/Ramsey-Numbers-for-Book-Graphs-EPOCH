# Peer Review

## Major Findings

1. Missing manuscript artifacts are a hard blocker. `research_paper.tex` and `research_paper.pdf` are absent from the repo, so the package fails both completeness and compilation requirements outright. This also conflicts with `results/research_context.md:7-8`, which claims that the paper draft and compilation stage were completed.

2. The active root solver resolves the mixed-language/probabilistic complaint only partially. The root `solution.py` is Python-only and deterministic, but it is still not a valid general answer to the stated prompt because it explicitly raises `ValueError` on unsupported inputs (`solution.py:35-39`). The saved report already admits this (`results/final_report.md:11-17`), and my rerun confirmed the same `42 supported / 58 unsupported` split through `n <= 100`.

3. Citation accuracy fails the zero-tolerance bar. Several `sources.bib` entries are not merely sparse; they are wrong enough to be unusable in a paper-facing bibliography. The most serious failures are `LowerBoundsBookRamseyWesley2025` (`sources.bib:1-5`), `BlackLevenRadz` (`sources.bib:82-86`), `SMS` (`sources.bib:116-120`), `SCIP6` (`sources.bib:123-127`), `Kissat` (`sources.bib:130-134`), and `EpochBookGraphsBenchmark` (`sources.bib:153-158`).

4. Benchmark integrity is weaker than the benchmark tables imply. `results/verification/benchmark_report.md:23-36` documents that pair-slack `verifier_calls` is mislabeled and that the stored runtimes are not end-to-end wall-clock measurements. That does not prove fabrication, but it does mean the current benchmarking surface is not publication-grade.

5. Novelty is not demonstrated. The active artifact packages known exact witnesses plus the known prime-power Paley/block-circulant family; the only potentially novel lane, the frozen-old four-vertex lift, fails its own known-step gate (`20 -> 21` and `21 -> 22` both infeasible), and the exact pair-slack lane produces only mixed scalar improvements without any new witness or coverage gain.

6. Figure quality fails by absence. `figures/` is empty, so there are no publication-quality figures to evaluate and the package cannot satisfy the figure requirement.

## Local Verification Rerun

- `python -m unittest -v test_solution.py`: passed all 6 tests.
- `python solution.py --verify-supported --limit 100`: reproduced the same `42 supported / 58 unsupported` split.
- Direct calls to `solution(23)`, `solution(24)`, `solution(50)`, and `solution(100)` all raised `ValueError`.
- The numbers reported in `results/experiments/pair_slack_benchmark.md` and `results/experiments/four_vertex_lift_known_steps.md` match the saved JSON artifacts, but the benchmark-report audit is correct that some cost metrics are mislabeled.

These reruns confirm that the active repo-root artifact is now Python-only and deterministic, so the specific mixed-language/probabilistic complaint is resolved for the root submission path. They also confirm that the actual combinatorial prompt remains unsolved for many inputs.

## Scores

| Criterion | Score | Basis |
| --- | ---: | --- |
| Completeness | 1 | No `research_paper.tex`; no paper sections; no references section in manuscript form. |
| Technical Rigor | 2 | The repo contains exact verification and some bounded experiments, but there is no paper-level method section with equations, and the experiment controls/ablations are inadequate. |
| Results Integrity | 2 | The saved markdown tables match the saved JSON outputs, but benchmark accounting defects and the false “paper compiled” context note materially weaken integrity. |
| Citation Accuracy | 1 | Multiple bibliography records are incorrect or non-canonical, and there is no real in-text citation surface to audit because the manuscript is missing. |
| Compilation | 1 | There is no LaTeX source or compiled PDF to build or inspect. |
| Writing Quality | 2 | The markdown reports are generally clear, but they do not amount to a coherent scientific manuscript and still contain stale or contradictory framing. |
| Figure Quality | 1 | `figures/` is empty. |
| Novelty & Creative Contribution | 1 | No new construction family, no new theorem, no frontier witness, and no experimentally validated CE-driven contribution. |

## Citation Verification Report

Repo-wide note: there is no `research_paper.tex`, and repo search found no LaTeX `\cite{...}` commands to audit. The current manuscript-facing surfaces mostly mention sources in prose or by raw BibTeX key, which is not an acceptable citation trail.

| BibTeX key | Status | Verification outcome |
| --- | --- | --- |
| `LowerBoundsBookRamseyWesley2025` | Incorrect | The work is real, but this record does not match a canonical version. Web verification shows a 2024 arXiv preprint and a journal version in *Discrete Mathematics* with DOI `10.1016/j.disc.2025.114913`; the current entry mixes versions, omits venue/DOI/URL, and uses an ambiguous year. |
| `RousseauSheehanRamseyBooksOriginal` | Verified | Title, authors, journal, year, volume, and pages match the 1978 *Journal of Graph Theory* paper. |
| `Conlon_BookRamsey` | Verified | David Conlon, “The Ramsey number of books,” *Advances in Combinatorics* (2019), DOI `10.19086/aic.10808`. |
| `ConlonFoxWigderson_RamseyBooksQuasirandomness` | Verified | Title, authors, venue, year, volume, number, and pages match the *Combinatorica* paper. |
| `ConlonFoxWigderson_OffDiagonalBooks` | Verified | Title, authors, venue, year, volume, number, pages, and DOI match the *Combinatorics, Probability and Computing* paper. |
| `ChenLinRamseyBookUpperBounds` | Verified | Title, authors, venue, year, paper number, and DOI match the *European Journal of Combinatorics* paper. |
| `LiuLiRamseyBooks` | Verified | Title, authors, venue, year, paper number, and DOI match the *Electronic Journal of Combinatorics* paper. |
| `LidickyMcKinleyPfenderSmallBooksWheels` | Verified | The listed arXiv preprint exists with the stated title and authors. This is an older preprint citation because a journal version now exists, but the preprint itself is real. |
| `ShaoXuBoPan` | Verified | The paper exists in JCMCC volume 75 (2010) with the listed title/authors; the BibTeX entry is sparse but corresponds to a real source. |
| `BlackLevenRadz` | Incorrect | A real paper exists, but not as cited here. Web verification points to a 2011 JCMCC paper with authors Kevin Black, Daniel E. Leven, and Stanislaw P. Radziszowski; the current entry has the wrong year, wrong author names, and no venue/pages. |
| `FaudreeRousseauSheehanStronglyRegular` | Verified | Title, authors, journal, year, pages, and DOI match. |
| `WJWThesis` | Verified | William J. Wesley’s 2023 UC Davis dissertation exists under this title. |
| `BlockCircRamseyGoedVanOver` | Verified | Title, authors, venue, year, pages, and DOI match the *Discrete Applied Mathematics* paper. |
| `SMS` | Incorrect | The real paper exists, but this record is not accurate. The correct paper is by Markus Kirchweger and Stefan Szeider, at CP 2021 / LIPIcs 210, with DOI `10.4230/LIPIcs.CP.2021.34`; `author = {Anders and Others}` is plainly unusable. |
| `SCIP6` | Incorrect | A real SCIP 6.0 report/product exists, but this entry is not canonical: the authorship is wrong/incomplete, the year is not tied to a specific official citation record, and there is no report identifier or URL. |
| `Kissat` | Incorrect | The solver-description document exists and the title/authors/year are real, but the current entry omits the venue/proceedings information needed for a correct citation record. |
| `VanOverbergheGithub` | Verified | The GitHub path resolves. However, it is a moving branch path rather than an immutable archival reference, so it is inadequate as final witness provenance. |
| `Ramsey_Research_Software` | Verified | The GitHub repository exists and the cited commit resolves. |
| `EpochBookGraphsBenchmark` | Incorrect | The consulted benchmark page exists, but the current title/year metadata are not a clean match to the actual page and the entry provides no resolving URL in the BibTeX itself. |

Because multiple entries are incorrect, incomplete, or version-muddled, the citation-accuracy criterion fails regardless of the verified subset.

## Novelty Assessment

This package does not currently contribute a genuinely new Ramsey-theoretic result. The active root solver is a deterministic wrapper around known safe territory: embedded exact witnesses, an embedded `n = 22` two-block witness, and the known prime-power Paley/block-circulant family. That is useful artifact hygiene, but it is not a new construction. The only lane with even modest novelty potential, the frozen-old four-vertex lift, fails immediately on its own positive controls (`20 -> 21` and `21 -> 22`). The pair-slack lane changes the scoring rule inside an existing restricted two-block search family and does not reach a new verified witness. The CE layer also does not rescue the novelty claim: repo-wide inspection found no `experimental_result` field in the concept-tree `concept.json` files, so the concept-evolution artifacts read as planning scaffolding rather than experimentally grounded creative contributions. On the standard required here, this is a verification/negative-results package, not a novel combinatorial advance.

## Overall Verdict

**DEEPEN**

This must be `DEEPEN`, not merely `REVISE`, because the novelty score is 1 and the missing novelty is not a superficial presentation issue. There are also substantial quality problems, but even if those were repaired, the package would still lack a publication-level new contribution.

## What Must Change

1. Produce a real manuscript. Add `research_paper.tex`, compile it to PDF, and include the required sections: Abstract, Introduction, Related Work, Method, Experiments, Results, Discussion, Conclusion, and References.

2. Stop presenting the current solver as if it answers the original prompt. Either deliver an actual deterministic construction for all required `n`, or explicitly reframe the work as a partial solver plus negative-results study.

3. Repair every incorrect bibliography entry and attach citations where claims are actually made. At minimum, fix the Wesley, Black-Leven-Radziszowski, SMS, SCIP, Kissat, and Epoch entries before any manuscript-facing submission.

4. Freeze witness provenance. The graph6 bank, the tiny exact witnesses, and the embedded `n = 22` tuple need immutable upstream sources, not just working code payloads or moving repository paths.

5. Fix benchmark accounting and rerun the saved experiments. `verifier_calls` must report real verifier invocations, runtimes must be end-to-end, and the benchmark set needs the missing controls already identified in `results/verification/benchmark_report.md`, especially `n = 23`, perturb-and-recover tests, objective ablations, and a relaxed lift control.

6. Add real figures or drop any claim to publication-ready experimental presentation. An empty `figures/` directory is not acceptable at this stage.

7. To become genuinely novel in this domain, the next round needs at least one of the following:
   - a new deterministic construction family covering unsupported cases;
   - a new verified frontier witness on a currently unsupported case such as `n = 23`, `24`, or `50`;
   - a theorem/proof/structural obstruction that materially extends the Wesley / Paley / block-circulant line;
   - an experimentally validated new search formulation that beats known baselines on frontier cases with clean controls and accounting.

Without one of those, the best honest framing is a careful negative-results and verification artifact, not a publishable novelty-forward Ramsey paper.
