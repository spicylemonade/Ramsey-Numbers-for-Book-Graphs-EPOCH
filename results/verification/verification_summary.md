# Verification Summary

## Approved Claim Language

The repo currently contains a Python-only deterministic root artifact that returns verified witnesses on its supported domain and explicitly rejects unsupported inputs. It does not currently solve the all-`n` triangular-book prompt.

## Verified Facts

- Root `solution.py` imports only Python standard-library modules and does not invoke code generation, shell compilation, or randomness.
- Root `test_solution.py` now checks:
  - deterministic repeated outputs,
  - exact verification of supported samples,
  - the full supported/unsupported table for `n <= 100`,
  - import hygiene and absence of obvious codegen/random fallback tokens.
- `python solution.py --verify-supported --limit 100` reproduces the current domain split:
  - supported: `42` values,
  - unsupported: `58` values.

## Disallowed Claim Language

- Do not say the full prompt is solved for arbitrary `n`.
- Do not cite the archived `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/` C or stochastic search files as evidence about the active root submission.

## Remaining Frontier

- The unresolved issue is coverage beyond the embedded exact witnesses and the known prime-power family.
- Immediate frontier examples still unsupported by the active root artifact include `n = 23`, `24`, `50`, and `100`.
