# Falsifier Memo

## Bottom Line
- The user's original complaint is valid against the legacy Aristotle worktree: it includes compiled C search (`solve.c`, `search.c`) and stochastic search helpers (`search.py`, `search_np.py`, `search_fast.py`, `search_v2.py`).
- That complaint is **not** valid against the active submission artifact at the repo root. `solution.py` is now Python-only and deterministic.
- The stronger remaining failure is coverage. The active solver does **not** solve the all-`n` prompt; it is a partial deterministic certificate packer that supports:
  - exact embedded witnesses for `n <= 22`;
  - the published prime-power family for odd `n` with `2n - 1` a prime power.
- Local verification across `n <= 100` shows 42 supported inputs and 58 explicit failures. Any claim that the task is fully solved for arbitrary `n` would be false.

## Resolved Versus Unresolved
- Resolved: active `solution.py` imports only `itertools`; there is no runtime dependency on C, shelling out, or randomness.
- Resolved: repeated calls on the same `n` return identical adjacency strings.
- Resolved: every currently supported `n <= 100` passes an exact verifier for the book constraints.
- Resolved: unsupported inputs raise `ValueError` instead of silently returning an unverified heuristic witness.
- Unresolved: the prompt asks for an algorithm taking `n` as input, and the active artifact still rejects 58 values in `1..100`, including `n = 23, 24, 50, 100`.
- Unresolved: the legacy mixed-language stochastic files remain in the archive tree and can still confuse reviewers if they are cited as evidence.

## Easiest Ways the Current Hypothesis Fails
- **Overclaiming the result**: the artifact is only a partial solver. If someone phrases it as "the triangular-book prompt is solved," the claim fails immediately on unsupported even `n > 20` and unsupported odd composite cases.
- **Rehash accusation on the small range**: the `n <= 20` branch is just packaging exact witness data, not a new construction.
- **Rehash accusation on the infinite family**: the prime-power branch is the known algebraic two-layer / Paley-type family, not a novel idea.
- **Benchmark cherry-picking**: showing only `n = 25` or other prime-power cases hides the hard frontier; `n = 50` is the obvious stress test because it is unsupported here.
- **Archive contamination**: if the old C or random-search files are presented without a clear "legacy only" label, a reviewer can reasonably conclude the artifact is still mixed-language or heuristic.

## Missing Controls
- A machine-readable provenance map for each witness:
  - embedded exact witness;
  - theorem-backed algebraic construction;
  - unsupported / no certificate.
- A clearer provenance tag inside the emitted artifact itself, so callers do not have to infer the witness source from code inspection.
- A coverage table in the artifact itself, so reviewers do not have to infer the supported domain from failures or separate test output.
- A provenance check for the graph6 payloads, since the current script trusts the embedded strings once decoded.

## Benchmark Traps
- Measuring success only on theorem-backed instances and calling it broad empirical validation.
- Treating stochastic search success in the archive as if it established verifier-safe correctness for the active submission.
- Reporting average-case search behavior instead of worst-case deterministic guarantee.
- Confusing "fast witness generation on supported `n`" with "meets the prompt for all `n <= 100`."
- Running exact verification only on small instances; that can hide finite-field bugs in larger prime-power cases.

## Novelty Illusions
- "Python implementation" is not the novelty; it is packaging hygiene.
- "Deterministic now" is not the same as "general constructive breakthrough."
- "We use finite fields / Paley ideas" is not new without a new family beyond the published prime-power line.
- "We solved many values up to 100" is weak if the missing values are exactly the structurally hard frontier.
- The current local literature watchlist drifted into irrelevant string-graph papers; any novelty claim built on that watchlist is easy to dismiss as retrieval error rather than real prior-art separation.

## Literature Branches That Would Invalidate Weak Claims
- Book-Ramsey exact-bound papers and their appendix witness tables.
- The Wesley et al. line combining exact small-`n` results with the infinite prime-power family.
- SAT / integer-programming / symmetry-breaking critical-graph search for lower bounds.
- Cyclic, block-circulant, difference-set, and Paley-style algebraic constructions.
- Benchmark/open-problem writeups that explicitly separate the solved warm-up regime from still-open challenge instances such as `n = 50`.

## External Anchors Worth Respecting
- Wesley et al. explicitly frame the small exact cases and the prime-power family as the substantive proved territory, with SMS and integer programming doing the heavy lifting on many exact values. That makes it very hard to sell the current solver as a new construction rather than a repackaging of known witnesses plus a known algebraic family.
- The Epoch book-graphs benchmark page explicitly separates the "all `n <= 21` plus an infinite family" regime from the single hard challenge instance `n = 50`. If this repo claims a general fix while still rejecting `50`, the benchmark itself refutes the framing.

## Concrete Adversarial Position
- Acceptable claim: "This repo now contains a Python-only deterministic artifact that returns verified witnesses when they are theorem-backed or explicitly embedded, and refuses unsupported inputs."
- Unacceptable claim: "This repo now gives a general algorithm for the full prompt."
- Best falsification target going forward: even `n > 20`, then odd composite `n` with `2n - 1` not a prime power.

## Local Evidence Logged
- `python solution.py` now completes quickly and reports the supported set:
  - `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 27, 31, 37, 41, 45, 49, 51, 55, 57, 61, 63, 69, 75, 79, 85, 87, 91, 97, 99]`
- Unsupported examples verified locally:
  - `23 -> ValueError`
  - `24 -> ValueError`
  - `50 -> ValueError`
  - `100 -> ValueError`
- The exact verifier in `solution.py` was upgraded to a bitset implementation so these regression checks are cheap enough to run routinely.
