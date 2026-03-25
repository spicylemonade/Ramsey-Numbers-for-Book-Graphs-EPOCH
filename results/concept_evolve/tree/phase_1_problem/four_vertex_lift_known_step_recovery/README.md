# Concept: four_vertex_lift_known_step_recovery

- Topic Context: Test whether a verified witness for n can be completed to a verified witness for n+1 by adding exactly four vertices and solving only the new incidences.
- Domains: combinatorics, constraint_programming

## Distinguishing Angle
- Why different from closest prior art: Changes the search object from full witness generation to fixed-old-graph completion.
- Easiest falsifier: Infeasible or timeout on the known steps 20->21 and 21->22.
- First experiment: Exact CP-SAT completion with the old witness frozen.
- Overlap risk: Moderate overlap with SAT/IP search, but still different in object and variables.
