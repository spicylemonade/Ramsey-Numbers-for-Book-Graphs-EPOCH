# Four-Vertex Lift Known-Step Recovery

## Commands
```bash
python3 book_research.py lift --n-old 20 --timeout 60 --output results/experiments/lift_20_21.json
python3 book_research.py lift --n-old 21 --timeout 60 --output results/experiments/lift_21_22.json
```

## Results
- `20 -> 21`: status `INFEASIBLE`, runtime `3.009` seconds, auxiliary conjunction count `26856`.
- `21 -> 22`: status `INFEASIBLE`, runtime `3.594` seconds, auxiliary conjunction count `29544`.

## Interpretation
The exact fixed-old-graph completion model failed both known-step recovery targets under the stated budget. Under the director kill switch, that is enough to kill the champion lane before attempting `22 -> 23`.
