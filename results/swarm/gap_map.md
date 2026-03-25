# Gap Map

Scope: negative-space around the triangular book graph task after reading the local research artifacts first, then checking the recent book-Ramsey paper and the published witness data needed to make the solver deterministic.

## 1. Even `n > 20` is still the thinnest, most under-served frontier
- Concrete gap: the deterministic artifact now covers `n <= 20` exactly and the published Paley-type family covers cases where `2n - 1` is a prime power congruent to `1 mod 4`, but that leaves the large even range with no clean general construction.
- Why this is genuinely under-served: most available structure is algebraic and favors odd `n`; the remaining even cases are where the current repo immediately loses proof support.
- Failure mode: heuristic local search can emit plausible witnesses for even `n` without any guarantee that the run found one for the right reason, or that it would reproduce under the verifier.
- Next experiment: make even `n` its own benchmark track and run certificate-backed SAT/IP search by residue class instead of folding it into a generic random search bucket.

## 2. Odd composite `n` outside the prime-power line lack a structural explanation
- Concrete gap: odd `n` with composite `2n - 1` beyond the exact small range are also unsupported, even though they are close in shape to the solved prime-power family.
- Why this is under-served: they are not the headline cases in the literature, but they are the first places where a “Paley-like for all `n`” conjecture has to become a real construction rather than a slogan.
- Failure mode: the previous artifact blurred this distinction by treating all odd `n` as roughly the same and then hiding the hard ones behind probabilistic search.
- Next experiment: normalize the exact witnesses for the small composite cases and compare their difference-set statistics against the prime-power family to see which algebraic identities survive without a field.

## 3. Small exact witnesses are available, but the repo is not learning from them
- Concrete gap: the exact witness range `n <= 20` is currently being used only as lookup data, not as a source of hypotheses about degree patterns, block structure, or automorphisms that might extrapolate.
- Why this is under-served: appendix data is easy to consume operationally and easy to ignore scientifically.
- Failure mode: the code had a hard jump from “known exact” to “stochastic fallback,” which means there was no middle layer where exact graphs were mined for transferable structure.
- Next experiment: derive per-witness features such as degree multisets, block-circulant fits, orbit decompositions, and correlation tables, then cluster the exact witnesses before searching new cases.

## 4. Proof-carrying solver packaging is weaker than witness discovery
- Concrete gap: the main artifact problem was not just “find a graph,” but “ship a Python-only deterministic solver that is honest about what is and is not proved.”
- Why this is under-served: search pipelines optimize for discovery speed, while verifier-safe packaging, provenance, and exact checking are treated as cleanup work.
- Failure mode: the previous script mixed Python with generated C and used probabilistic search, so it could appear to solve the task while actually depending on hidden compilation and luck.
- Next experiment: require every new witness source to come with a stable encoding, an exact checker, and a provenance tag saying whether it is theorem-backed, appendix-backed, or only heuristic.

## 5. Retrieval drift is still a measurable pipeline bug
- Concrete gap: the watchlist/frontier artifacts drifted into irrelevant “string graph” literature because the initial query terms were too generic.
- Why this is under-served: retrieval is often treated as clerical setup, but here it materially distorts what looks novel and what looks already covered.
- Failure mode: budget gets burned surveying unrelated graph-string papers while the actual book-Ramsey / block-circulant / SAT / IP neighborhood stays thin.
- Next experiment: replace generic seeds with problem-local queries centered on `book Ramsey`, `critical graph`, `block-circulant`, `SAT`, `integer programming`, and `B_{n-1}, B_n`, then score drift explicitly.
