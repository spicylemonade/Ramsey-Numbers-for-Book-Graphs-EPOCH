# Prior Art Watchlist

## Status
- Primary watchlist repaired on 2026-03-25.
- The prior attempt drifted into string-graph retrieval noise; those papers are retained only for required superficial comparison.
- The active problem-local watchlist is now book-Ramsey-specific.

## Problem-Local Core
- `Lower Bounds for Book Ramsey Numbers` (William J. Wesley, 2025): closest source for the exact `R(B_{n-1},B_n)` target; proves `n <= 20` and the prime-power family, uses block-circulant witnesses plus SAT/IP/SMS.
- `On Ramsey Numbers for Books` (`RousseauSheehanRamseyBooksOriginal`, 1978): classical upper-bound and baseline construction source.
- `The Ramsey number of books` (`Conlon_BookRamsey`, 2019): direct asymptotic/problem-local book source.
- `Ramsey numbers of books and quasirandomness` (`ConlonFoxWigderson_RamseyBooksQuasirandomness`, 2022): problem-local structural source.
- `Off-diagonal book Ramsey numbers` (`ConlonFoxWigderson_OffDiagonalBooks`, 2023): direct off-diagonal book-Ramsey source.
- `New upper bounds for Ramsey numbers of books` (`ChenLinRamseyBookUpperBounds`, 2024): problem-local upper-bound source.
- `A note on Ramsey numbers involving large books` (`LiuLiRamseyBooks`, 2024): large-book context.
- `Small Ramsey numbers for books, wheels, and generalizations` (`LidickyMcKinleyPfenderSmallBooksWheels`, 2024): nearby small-case computational work.
- `Computation of some generalized Ramsey numbers` (`ShaoXuBoPan`, 2010): small exact computation source.
- `New Bounds on Some Ramsey Numbers` (`BlackLevenRadz`, 1996): small exact/critical-graph source.
- `Strongly regular graphs and finite Ramsey theory` (`FaudreeRousseauSheehanStronglyRegular`, 1982): construction overlap via strongly regular graphs.
- `Algebraic and Boolean Methods for Computation and Certification of Ramsey-type Numbers` (`WJWThesis`, 2023): methods and certification context.

## Code And Benchmark Artifacts
- `VanOverbergheGithub`: `circulant-Ramsey/tree/master/RamseyGraphs/Books` witness archive.
- `Ramsey_Research_Software`: problem-local Ramsey search software repository.
- `EPOCH FrontierMath open problem: Ramsey book graphs`: benchmark framing for the warm-up `n=25` case and the open `n=50` challenge.

## Required Superficial Comparisons
These are kept only because the rubric requires explicit comparison. They are not problem-local prior art.
- `String Graph Obstacles of High Girth and of Bounded Degree (2025)`
- `Quantum Based Grover's Algorithm and Graph Coloring in Unstructured Searches for Bit String Validation (2025)`
- `FSG: Fast String Graph Construction for De Novo Assembly (2016)`
- `A 1.9999-Approximation Algorithm for Vertex Cover on String Graphs (2024)`

## Novelty Questions
- How is any new claim materially different from the Wesley block-circulant / SAT / IP / SMS line?
- How is any new claim materially different from the classical Rousseau-Sheehan upper-bound / Paley baseline?
- Can the repo show novelty beyond packaging exact witnesses and the known prime-power family?
- Does the four-vertex-lift lane recover `20 -> 21` and `21 -> 22` before any frontier claim is made?
- Does the exact-slack lane beat a surrogate-objective baseline on `22`, `24`, and `50` before it is treated as a live novelty claim?

