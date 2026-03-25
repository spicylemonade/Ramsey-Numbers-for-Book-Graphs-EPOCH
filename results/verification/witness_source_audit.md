# Witness Source Audit

## Scope

This audit traces the witness payloads embedded in the active root `solution.py`. It distinguishes internal code provenance from external literature provenance and lists unresolved entries explicitly.

## Root Internal Provenance

- `n = 1, 2, 4`
  - Stored directly in `solution.py::_small_exact_witnesses`.
- `n = 5..21`
  - Stored as graph6 payloads in `solution.py::_exact_graph6_witnesses`.
  - Decoded by `solution.py::_graph6_to_adjacency_string`.
- `n = 22`
  - Stored as the exact two-block tuple in `solution.py::_exact_two_block_witnesses`.
  - Realized by `solution.py::_cyclic_two_block`.
- Prime-power family values in the current supported table
  - Generated on demand by `solution.py::_prime_power`, `solution.py::_field_model`, and `solution.py::_paley_two_block`.

## External Provenance Status

- Small exact witnesses (`n = 1, 2, 4`)
  - External paper/appendix provenance is not recorded in the repo.
  - Status: unresolved.
- Graph6 witness bank (`n = 5..21`)
  - The repo contains the payloads but not the paper, appendix, or benchmark page from which they were copied.
  - Status: unresolved.
- Exact two-block witness (`n = 22`)
  - The repo contains the parameter tuple but not an explicit citation to the originating paper, appendix, or benchmark page.
  - Status: unresolved.
- Prime-power family
  - The code matches the documented Paley-type two-block construction family used by the active solver.
  - A problem-local citation should still be added to `sources.bib` before any publication-facing writeup.
  - Status: partially resolved at the method level, but not yet bibliographically frozen in this repo.

## Consequence

- The active root solver is verifier-safe on its supported domain.
- The exact external bibliographic source of several embedded exact witnesses is not yet proven from repo-local evidence alone.
- Any future paper-style report should cite the exact source of the graph6 bank and the `n = 22` two-block witness instead of treating the embedded payloads as self-authenticating.
