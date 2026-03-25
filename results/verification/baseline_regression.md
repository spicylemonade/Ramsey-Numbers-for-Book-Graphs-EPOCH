# Baseline Regression

- Date (UTC): 2026-03-25
- Python: `3.10.17`
- Active artifact under test: root `solution.py`
- Legacy archive excluded from the execution path: `790a8891-d60d-46f1-8aef-84f720d59562_aristotle/`

## Command

```bash
python -m unittest -v test_solution.py
```

## Output

```text
test_solution_module_has_no_codegen_or_random_fallbacks (test_solution.SolutionTests) ... ok
test_solution_module_has_pure_python_import_hygiene (test_solution.SolutionTests) ... ok
test_supported_domain_up_to_100_is_stable (test_solution.SolutionTests) ... ok
test_supported_samples_are_deterministic_and_verified (test_solution.SolutionTests) ... ok
test_unsupported_samples_raise_value_error (test_solution.SolutionTests) ... ok

----------------------------------------------------------------------
Ran 5 tests in 1.405s

OK
```

## Command

```bash
python solution.py --verify-supported --limit 100
```

## Output

```text
supported up to 100: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 25, 27, 31, 37, 41, 45, 49, 51, 55, 57, 61, 63, 69, 75, 79, 85, 87, 91, 97, 99]
unsupported up to 100: [23, 24, 26, 28, 29, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 43, 44, 46, 47, 48, 50, 52, 53, 54, 56, 58, 59, 60, 62, 64, 65, 66, 67, 68, 70, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 83, 84, 86, 88, 89, 90, 92, 93, 94, 95, 96, 98, 100]
```

## Baseline Table

- Supported count: `42`
- Unsupported count: `58`
- Split: `42 supported / 58 unsupported`

## Notes

- The active root solver is deterministic on every supported input up to `n = 100`.
- Unsupported values fail explicitly with `ValueError`; there is no fallback to probabilistic search or generated C code in the active root module.
- The user’s packaging complaint remains true only for the archived legacy tree, not for the active root execution path.
