# Root Submission Hygiene Verification

## Scope

This note verifies the user's specific complaint against the active repo-root submission path:

- no mixed C/Python execution path,
- no probabilistic or heuristic fallback,
- explicit failure on unsupported inputs instead of guessing.

The legacy archive under
`790a8891-d60d-46f1-8aef-84f720d59562_aristotle/` still exists for provenance,
but it is not the active submission artifact.

## Commands Rerun On 2026-03-25

### 1. Root regression suite

Command:

```bash
python -m unittest -v test_solution.py
```

Observed result:

- `7` tests passed.
- The regression suite now checks:
  - the imported module is the repo-root [solution.py](/home/archivara/work/repo/solution.py),
  - the active solver has no `subprocess`, `ctypes`, `cffi`, `gcc`, `clang`, `random`, `numpy`, `ortools`, or `cp_model` fallback,
  - unsupported inputs raise `ValueError` with explicit unsupported wording,
  - the archive README marks that tree as historical `legacy-only` context.

### 2. Supported-domain sweep

Command:

```bash
python solution.py --verify-supported --limit 100
```

Observed result:

- Supported through `n <= 100`:
  - `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 27, 31, 37, 41, 45, 49, 51, 55, 57, 61, 63, 69, 75, 79, 85, 87, 91, 97, 99]`
- Unsupported through `n <= 100`:
  - `[23, 24, 26, 28, 29, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 43, 44, 46, 47, 48, 50, 52, 53, 54, 56, 58, 59, 60, 62, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 83, 84, 86, 88, 89, 90, 92, 93, 94, 95, 96, 98, 100]`

This exactly matches the previously frozen `42 supported / 58 unsupported` split.

### 3. Direct unsupported-case probes

Command:

```bash
python - <<'PY'
import solution
for n in [23, 24, 50, 100]:
    try:
        solution.solution(n)
    except Exception as exc:
        print(f"{n}: {type(exc).__name__}: {exc}")
PY
```

Observed result:

- `23`, `24`, `50`, and `100` each raised `ValueError`.
- The message explicitly says those inputs are unsupported and are rejected instead of being guessed by heuristic or mixed-language fallback.

## Outcome

- The active root submission artifact is Python-only and deterministic.
- The repo now has a regression check that guards the archive boundary explicitly.
- The legacy archive remains present, but its README now marks it as `legacy-only` context and the root tests assert that wording.
- The original mixed-language/probabilistic complaint is resolved for the active repo-root submission path.

## Remaining Limitation

- This verification does **not** solve the mathematical coverage problem.
- The active solver remains a deterministic partial artifact: it refuses unsupported values instead of returning an unverified witness.
