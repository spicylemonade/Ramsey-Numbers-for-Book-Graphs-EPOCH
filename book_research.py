from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from ortools.sat.python import cp_model

import solution


def _adjacency_to_masks(adjacency: str, order: int) -> list[int]:
    masks = [0] * order
    index = 0
    for right in range(order):
        for left in range(right):
            if adjacency[index] == "1":
                masks[left] |= 1 << right
                masks[right] |= 1 << left
            index += 1
    return masks


def _source_tag_for_n(n: int) -> str:
    if n in solution._small_exact_witnesses():
        return "small_exact"
    if n in solution._exact_two_block_witnesses():
        return "exact_two_block"
    if n in solution._exact_graph6_witnesses():
        return "exact_graph6"
    q = 2 * n - 1
    if q % 4 == 1 and solution._prime_power(q) is not None:
        return "prime_power_family"
    return "unsupported"


def _wl_summary(masks: list[int]) -> dict[str, object]:
    order = len(masks)
    colors = [mask.bit_count() for mask in masks]
    while True:
        signatures = []
        for vertex in range(order):
            neighbor_colors = Counter(
                colors[other]
                for other in range(order)
                if (masks[vertex] >> other) & 1
            )
            signatures.append((colors[vertex], tuple(sorted(neighbor_colors.items()))))

        palette: dict[tuple[object, ...], int] = {}
        refined: list[int] = []
        for signature in signatures:
            if signature not in palette:
                palette[signature] = len(palette)
            refined.append(palette[signature])

        if refined == colors:
            break
        colors = refined

    class_sizes = sorted(Counter(colors).values(), reverse=True)
    return {
        "class_count": len(set(colors)),
        "class_sizes": class_sizes,
    }


def extract_exact_witness_features() -> dict[str, object]:
    features: dict[str, object] = {}
    for n in range(1, 23):
        adjacency = solution.solution(n)
        order = 4 * n - 2
        ok, message = solution._verify_book_constraints(adjacency, n)
        if not ok:
            raise RuntimeError(
                f"n={n} failed verification during feature extraction: {message}"
            )

        masks = _adjacency_to_masks(adjacency, order)
        full_mask = (1 << order) - 1
        nonmasks = [(~mask) & (full_mask ^ (1 << vertex)) for vertex, mask in enumerate(masks)]

        degree_histogram = Counter(mask.bit_count() for mask in masks)
        edge_slack = Counter()
        nonedge_slack = Counter()
        edge_saturated = 0
        nonedge_saturated = 0
        max_edge_common = 0
        max_nonedge_common_non = 0
        edge_pairs = 0
        nonedge_pairs = 0

        for right in range(order):
            for left in range(right):
                if (masks[left] >> right) & 1:
                    edge_pairs += 1
                    common = (masks[left] & masks[right]).bit_count()
                    slack = (n - 2) - common
                    edge_slack[str(slack)] += 1
                    edge_saturated += int(slack == 0)
                    max_edge_common = max(max_edge_common, common)
                else:
                    nonedge_pairs += 1
                    common_non = (nonmasks[left] & nonmasks[right]).bit_count()
                    slack = (n - 1) - common_non
                    nonedge_slack[str(slack)] += 1
                    nonedge_saturated += int(slack == 0)
                    max_nonedge_common_non = max(max_nonedge_common_non, common_non)

        source_tag = _source_tag_for_n(n)
        features[str(n)] = {
            "order": order,
            "source_tag": source_tag,
            "degree_multiset": sorted(mask.bit_count() for mask in masks),
            "degree_histogram": {
                str(degree): degree_histogram[degree]
                for degree in sorted(degree_histogram)
            },
            "edge_pairs": edge_pairs,
            "nonedge_pairs": nonedge_pairs,
            "edge_saturated_pairs": edge_saturated,
            "nonedge_saturated_pairs": nonedge_saturated,
            "edge_slack_histogram": {
                key: edge_slack[key] for key in sorted(edge_slack, key=int)
            },
            "nonedge_slack_histogram": {
                key: nonedge_slack[key] for key in sorted(nonedge_slack, key=int)
            },
            "max_edge_common_neighbors": max_edge_common,
            "max_nonedge_common_nonneighbors": max_nonedge_common_non,
            "wl_refinement": _wl_summary(masks),
        }

    return {
        "generated_at": "2026-03-25T00:00:00Z",
        "scope": "Verified exact witnesses emitted by root solution.py through n=22",
        "fields": [
            "degree_multiset",
            "degree_histogram",
            "edge_saturated_pairs",
            "nonedge_saturated_pairs",
            "edge_slack_histogram",
            "nonedge_slack_histogram",
            "wl_refinement",
        ],
        "notes": [
            "Edge slack is (n-2) minus the common-neighbor count for each present edge.",
            "Non-edge slack is (n-1) minus the common-nonneighbor count for each missing edge.",
            "wl_refinement is a coarse 1-WL color-refinement summary used as an orbit proxy, not an automorphism computation.",
        ],
        "witnesses": features,
    }


def _parse_adjacency_matrix(adjacency: str, order: int) -> list[list[int]]:
    matrix = [[0] * order for _ in range(order)]
    index = 0
    for right in range(order):
        for left in range(right):
            bit = 1 if adjacency[index] == "1" else 0
            matrix[left][right] = bit
            matrix[right][left] = bit
            index += 1
    return matrix


def run_four_vertex_lift(n_old: int, timeout_seconds: float) -> dict[str, object]:
    n_new = n_old + 1
    old_adjacency = solution.solution(n_old)
    old_order = 4 * n_old - 2
    new_order = 4 * n_new - 2
    old_matrix = _parse_adjacency_matrix(old_adjacency, old_order)

    model = cp_model.CpModel()
    old_new = [
        [model.NewBoolVar(f"old_new_{old_vertex}_{new_slot}") for new_slot in range(4)]
        for old_vertex in range(old_order)
    ]
    new_new = {
        (left, right): model.NewBoolVar(f"new_new_{left}_{right}")
        for left in range(4)
        for right in range(left + 1, 4)
    }

    auxiliary_count = 0

    def and_var(literals: list[cp_model.IntVar]) -> cp_model.IntVar:
        nonlocal auxiliary_count
        auxiliary_count += 1
        variable = model.NewBoolVar(f"and_{auxiliary_count}")
        for literal in literals:
            model.AddImplication(variable, literal)
        model.AddBoolOr([variable] + [literal.Not() for literal in literals])
        return variable

    def edge_literal(left: int, right: int) -> int | cp_model.IntVar:
        if left > right:
            left, right = right, left
        if right < old_order:
            return old_matrix[left][right]

        right_slot = right - old_order
        if left < old_order:
            return old_new[left][right_slot]

        left_slot = left - old_order
        return new_new[min(left_slot, right_slot), max(left_slot, right_slot)]

    new_degrees = [
        sum(old_new[old_vertex][slot] for old_vertex in range(old_order))
        + sum(
            new_new[min(slot, other), max(slot, other)]
            for other in range(4)
            if other != slot
        )
        for slot in range(4)
    ]
    for slot in range(3):
        model.Add(new_degrees[slot] <= new_degrees[slot + 1])

    def common_terms(
        left: int,
        right: int,
        complement: bool,
    ) -> tuple[int, list[cp_model.IntVar]]:
        constant = 0
        terms: list[cp_model.IntVar] = []
        for witness in range(new_order):
            if witness == left or witness == right:
                continue

            first = edge_literal(left, witness)
            second = edge_literal(right, witness)

            if complement:
                first = (1 - first) if isinstance(first, int) else first.Not()
                second = (1 - second) if isinstance(second, int) else second.Not()

            if isinstance(first, int) and isinstance(second, int):
                constant += int(first and second)
            elif isinstance(first, int):
                if first:
                    terms.append(second)
            elif isinstance(second, int):
                if second:
                    terms.append(first)
            else:
                terms.append(and_var([first, second]))

        return constant, terms

    for right in range(new_order):
        for left in range(right):
            edge = edge_literal(left, right)
            edge_constant, edge_terms = common_terms(left, right, complement=False)
            nonedge_constant, nonedge_terms = common_terms(left, right, complement=True)
            edge_expr = edge_constant + sum(edge_terms) if edge_terms else edge_constant
            nonedge_expr = (
                nonedge_constant + sum(nonedge_terms)
                if nonedge_terms
                else nonedge_constant
            )

            if isinstance(edge, int):
                if edge:
                    model.Add(edge_expr <= n_new - 2)
                else:
                    model.Add(nonedge_expr <= n_new - 1)
            else:
                model.Add(edge_expr <= n_new - 2).OnlyEnforceIf(edge)
                model.Add(nonedge_expr <= n_new - 1).OnlyEnforceIf(edge.Not())

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = timeout_seconds
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = 0

    started = time.time()
    status = solver.Solve(model)
    elapsed = time.time() - started

    result = {
        "n_old": n_old,
        "n_new": n_new,
        "old_order": old_order,
        "new_order": new_order,
        "status": solver.StatusName(status),
        "runtime_seconds": round(elapsed, 3),
        "auxiliary_count": auxiliary_count,
        "timeout_seconds": timeout_seconds,
    }

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        matrix = [row[:] for row in old_matrix]
        for row in matrix:
            row.extend([0] * 4)
        matrix.extend([[0] * new_order for _ in range(4)])

        for old_vertex in range(old_order):
            for new_slot in range(4):
                value = solver.Value(old_new[old_vertex][new_slot])
                matrix[old_vertex][old_order + new_slot] = value
                matrix[old_order + new_slot][old_vertex] = value

        for left in range(4):
            for right in range(left + 1, 4):
                value = solver.Value(new_new[left, right])
                matrix[old_order + left][old_order + right] = value
                matrix[old_order + right][old_order + left] = value

        bits: list[str] = []
        for right in range(new_order):
            for left in range(right):
                bits.append("1" if matrix[left][right] else "0")
        adjacency = "".join(bits)
        ok, message = solution._verify_book_constraints(adjacency, n_new)
        result["verification"] = {"ok": ok, "message": message}
        result["adjacency"] = adjacency
    else:
        result["verification"] = {"ok": False, "message": "no completion returned"}

    return result


def _rotation_count(mask: int, shift: int, width: int) -> int:
    full_mask = (1 << width) - 1
    shift %= width
    rotated = ((mask << shift) | (mask >> (width - shift))) & full_mask
    return (mask & rotated).bit_count()


def _sigma_count(mask_a: int, mask_b: int, total: int, width: int) -> int:
    return sum(
        1
        for element in range(width)
        if ((mask_a >> element) & 1) and ((mask_b >> ((total - element) % width)) & 1)
    )


@dataclass(frozen=True)
class TwoBlockCandidate:
    m: int
    d11_pairs: tuple[int, ...]
    d12_values: tuple[int, ...]

    @property
    def d11_set(self) -> set[int]:
        return set(self.d11_pairs)

    @property
    def d12_set(self) -> set[int]:
        return set(self.d12_values)

    def d22_set(self) -> set[int]:
        return set(range(1, self.m)) - self.d11_set

    def d11_mask(self) -> int:
        return sum(1 << value for value in self.d11_pairs)

    def d22_mask(self) -> int:
        return sum(1 << value for value in self.d22_set())

    def d12_mask(self) -> int:
        return sum(1 << value for value in self.d12_values)

    def nd12_mask(self) -> int:
        return ((1 << self.m) - 1) ^ self.d12_mask()


def _mask_from_values(values: set[int]) -> int:
    return sum(1 << value for value in values)


def _constraint_slacks(candidate: TwoBlockCandidate, n: int) -> list[tuple[str, int]]:
    m = candidate.m
    d11 = candidate.d11_set
    d22 = candidate.d22_set()
    d12 = candidate.d12_set
    nd12 = set(range(m)) - d12

    d11_mask = candidate.d11_mask()
    d22_mask = candidate.d22_mask()
    d12_mask = candidate.d12_mask()
    nd12_mask = candidate.nd12_mask()

    slacks: list[tuple[str, int]] = []
    for difference in range(1, m):
        count_d12 = _rotation_count(d12_mask, difference, m)
        if difference in d11:
            common = _rotation_count(d11_mask, difference, m) + count_d12
            slacks.append((f"edge_l0_{difference}", (n - 2) - common))
            common_non = _rotation_count(d11_mask, difference, m) + _rotation_count(
                nd12_mask,
                difference,
                m,
            )
            slacks.append((f"nonedge_l1_{difference}", (n - 1) - common_non))
        else:
            common = _rotation_count(d22_mask, difference, m) + count_d12
            slacks.append((f"edge_l1_{difference}", (n - 2) - common))
            common_non = _rotation_count(d22_mask, difference, m) + _rotation_count(
                nd12_mask,
                difference,
                m,
            )
            slacks.append((f"nonedge_l0_{difference}", (n - 1) - common_non))

    for difference in range(m):
        if difference in d12:
            common = _sigma_count(d11_mask, d12_mask, difference, m) + _rotation_count(
                d12_mask,
                difference,
                m,
            )
            common -= sum(
                1
                for value in range(m)
                if ((d12_mask >> value) & 1) and ((d11_mask >> ((value - difference) % m)) & 1)
            )
            common = _sigma_count(d11_mask, d12_mask, difference, m) + sum(
                1
                for value in range(m)
                if ((d12_mask >> value) & 1) and ((d22_mask >> ((value - difference) % m)) & 1)
            )
            slacks.append((f"edge_cross_{difference}", (n - 2) - common))
        else:
            common_non = _sigma_count(d22_mask, nd12_mask, difference, m) + sum(
                1
                for value in range(m)
                if ((nd12_mask >> value) & 1) and ((d11_mask >> ((value - difference) % m)) & 1)
            )
            slacks.append((f"nonedge_cross_{difference}", (n - 1) - common_non))

    return slacks


def _candidate_metrics(candidate: TwoBlockCandidate, n: int) -> dict[str, object]:
    slacks = _constraint_slacks(candidate, n)
    min_slack = min(slack for _, slack in slacks)
    violation_count = sum(1 for _, slack in slacks if slack < 0)
    total_negative_excess = sum(-slack for _, slack in slacks if slack < 0)
    worst_constraints = [
        {"constraint": name, "slack": slack}
        for name, slack in sorted(slacks, key=lambda item: (item[1], item[0]))[:5]
    ]
    adjacency = solution._cyclic_two_block(
        candidate.m,
        set(candidate.d11_pairs),
        set(candidate.d12_values),
        candidate.d22_set(),
    )
    verified, message = solution._verify_book_constraints(adjacency, n)
    return {
        "min_slack": min_slack,
        "violation_count": violation_count,
        "total_negative_excess": total_negative_excess,
        "verified": verified,
        "verify_message": message,
        "worst_constraints": worst_constraints,
    }


def _objective_key(metrics: dict[str, object], mode: str) -> tuple[int, int, int]:
    min_slack = int(metrics["min_slack"])
    violation_count = int(metrics["violation_count"])
    total_negative_excess = int(metrics["total_negative_excess"])
    if mode == "exact":
        return (min_slack, -total_negative_excess, -violation_count)
    return (-violation_count, -total_negative_excess, min_slack)


def _seed_candidate(n: int) -> TwoBlockCandidate:
    m = 2 * n - 1
    if n == 22:
        exact = solution._exact_two_block_witnesses()[22]
        _, d11, d12 = exact
        return TwoBlockCandidate(m, tuple(sorted(d11)), tuple(sorted(d12)))

    pair_target_size = n - 1 if n % 2 == 1 else n - 2
    pair_target = pair_target_size // 2
    pair_representatives = list(range(1, (m + 1) // 2))
    preferred_pairs = []
    fallback_pairs = []
    residues = {
        (value * value) % m
        for value in range(m)
        if (value * value) % m not in {0}
    }
    for representative in pair_representatives:
        mate = m - representative
        bucket = preferred_pairs if representative in residues or mate in residues else fallback_pairs
        bucket.append(representative)
    chosen_representatives = (preferred_pairs + fallback_pairs)[:pair_target]
    d11_pairs = tuple(
        sorted(
            element
            for representative in chosen_representatives
            for element in (representative, m - representative)
        )
    )

    preferred_d12 = sorted(residues)
    all_d12 = preferred_d12 + [value for value in range(m) if value not in residues]
    d12_values = tuple(sorted(all_d12[: n - 1]))
    return TwoBlockCandidate(m, d11_pairs, d12_values)


def _swap_d11(candidate: TwoBlockCandidate, remove_pair: int, add_pair: int) -> TwoBlockCandidate:
    d11 = set(candidate.d11_pairs)
    m = candidate.m
    for value in (remove_pair, m - remove_pair):
        d11.remove(value)
    for value in (add_pair, m - add_pair):
        d11.add(value)
    return TwoBlockCandidate(m, tuple(sorted(d11)), candidate.d12_values)


def _swap_d12(candidate: TwoBlockCandidate, remove_value: int, add_value: int) -> TwoBlockCandidate:
    d12 = set(candidate.d12_values)
    d12.remove(remove_value)
    d12.add(add_value)
    return TwoBlockCandidate(candidate.m, candidate.d11_pairs, tuple(sorted(d12)))


def run_pair_slack_benchmark(
    n: int,
    max_rounds: int,
    mode: str,
) -> dict[str, object]:
    candidate = _seed_candidate(n)
    metrics = _candidate_metrics(candidate, n)
    timeline = [
        {
            "round": 0,
            **metrics,
        }
    ]

    representatives = list(range(1, (candidate.m + 1) // 2))
    verifier_calls = 1
    started = time.time()

    for round_index in range(1, max_rounds + 1):
        current_key = _objective_key(metrics, mode)
        best_candidate = candidate
        best_metrics = metrics
        best_key = current_key

        current_pairs = {min(value, candidate.m - value) for value in candidate.d11_pairs}
        missing_pairs = [rep for rep in representatives if rep not in current_pairs]
        present_pairs = sorted(current_pairs)
        for remove_pair in present_pairs:
            for add_pair in missing_pairs:
                next_candidate = _swap_d11(candidate, remove_pair, add_pair)
                next_metrics = _candidate_metrics(next_candidate, n)
                next_key = _objective_key(next_metrics, mode)
                if next_key > best_key:
                    best_candidate = next_candidate
                    best_metrics = next_metrics
                    best_key = next_key

        present_d12 = list(candidate.d12_values)
        missing_d12 = [value for value in range(candidate.m) if value not in candidate.d12_set]
        for remove_value in present_d12:
            for add_value in missing_d12:
                next_candidate = _swap_d12(candidate, remove_value, add_value)
                next_metrics = _candidate_metrics(next_candidate, n)
                next_key = _objective_key(next_metrics, mode)
                if next_key > best_key:
                    best_candidate = next_candidate
                    best_metrics = next_metrics
                    best_key = next_key

        candidate = best_candidate
        metrics = best_metrics
        verifier_calls += 1
        timeline.append(
            {
                "round": round_index,
                **metrics,
            }
        )
        if best_key == current_key:
            break
        if metrics["verified"]:
            break

    elapsed = time.time() - started
    return {
        "n": n,
        "mode": mode,
        "runtime_seconds": round(elapsed, 3),
        "verifier_calls": verifier_calls,
        "final_metrics": metrics,
        "d11": list(candidate.d11_pairs),
        "d12": list(candidate.d12_values),
        "timeline": timeline,
    }


def _write_json(payload: dict[str, object], path: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, indent=2) + "\n")


def _main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    features_parser = subparsers.add_parser("features")
    features_parser.add_argument("--output", required=True)

    lift_parser = subparsers.add_parser("lift")
    lift_parser.add_argument("--n-old", type=int, required=True)
    lift_parser.add_argument("--timeout", type=float, default=60.0)
    lift_parser.add_argument("--output", required=True)

    slack_parser = subparsers.add_parser("pair-slack")
    slack_parser.add_argument("--n", type=int, required=True)
    slack_parser.add_argument("--rounds", type=int, default=5)
    slack_parser.add_argument(
        "--mode",
        choices=["exact", "surrogate"],
        required=True,
    )
    slack_parser.add_argument("--output", required=True)

    args = parser.parse_args()

    if args.command == "features":
        _write_json(extract_exact_witness_features(), args.output)
    elif args.command == "lift":
        _write_json(run_four_vertex_lift(args.n_old, args.timeout), args.output)
    else:
        _write_json(run_pair_slack_benchmark(args.n, args.rounds, args.mode), args.output)


if __name__ == "__main__":
    _main()
