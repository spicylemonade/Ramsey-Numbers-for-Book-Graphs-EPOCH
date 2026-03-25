# Coverage Delta

## Baseline Versus Current

- Baseline support over `n <= 100`: `42 supported / 58 unsupported`
- Current support over `n <= 100`: `42 supported / 58 unsupported`
- Delta: no coverage change

## Interpretation

- The current work fixed packaging and verification concerns:
  - active root artifact is Python-only,
  - active root artifact is deterministic,
  - unsupported values fail explicitly instead of using heuristic fallback.
- The current work did **not** extend the supported frontier.

## Unsupported Examples Still Present

- `23`
- `24`
- `50`
- `100`
