import ast
import unittest
from pathlib import Path

import solution as solver


EXPECTED_SUPPORTED_UP_TO_100 = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    25,
    27,
    31,
    37,
    41,
    45,
    49,
    51,
    55,
    57,
    61,
    63,
    69,
    75,
    79,
    85,
    87,
    91,
    97,
    99,
]

EXPECTED_UNSUPPORTED_UP_TO_100 = [
    23,
    24,
    26,
    28,
    29,
    30,
    32,
    33,
    34,
    35,
    36,
    38,
    39,
    40,
    42,
    43,
    44,
    46,
    47,
    48,
    50,
    52,
    53,
    54,
    56,
    58,
    59,
    60,
    62,
    64,
    65,
    66,
    67,
    68,
    70,
    71,
    72,
    73,
    74,
    76,
    77,
    78,
    80,
    81,
    82,
    83,
    84,
    86,
    88,
    89,
    90,
    92,
    93,
    94,
    95,
    96,
    98,
    100,
]


class SolutionTests(unittest.TestCase):
    def test_supported_samples_are_deterministic_and_verified(self) -> None:
        samples = [1, 2, 3, 4, 5, 13, 22, 25]
        for n in samples:
            with self.subTest(n=n):
                first = solver.solution(n)
                second = solver.solution(n)
                self.assertEqual(first, second)

                order = 4 * n - 2
                self.assertEqual(len(first), order * (order - 1) // 2)

                ok, message = solver._verify_book_constraints(first, n)
                self.assertTrue(ok, message)

    def test_unsupported_samples_raise_value_error(self) -> None:
        for n in [23, 24, 50, 100]:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    solver.solution(n)

    def test_supported_domain_up_to_100_is_stable(self) -> None:
        supported, unsupported = solver._supported_values(100)
        self.assertEqual(supported, EXPECTED_SUPPORTED_UP_TO_100)
        self.assertEqual(unsupported, EXPECTED_UNSUPPORTED_UP_TO_100)

    def test_solution_module_is_repo_root_solution_file(self) -> None:
        expected = Path(__file__).resolve().with_name("solution.py")
        self.assertEqual(Path(solver.__file__).resolve(), expected)

    def test_solution_module_has_pure_python_import_hygiene(self) -> None:
        source = Path(solver.__file__).read_text()
        tree = ast.parse(source)
        allowed_imports = {"__future__", "argparse", "itertools"}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    root = alias.name.split(".")[0]
                    with self.subTest(import_name=alias.name):
                        self.assertIn(root, allowed_imports)
            elif isinstance(node, ast.ImportFrom):
                module = (node.module or "").split(".")[0]
                with self.subTest(import_from=node.module):
                    self.assertIn(module, allowed_imports)

    def test_solution_module_has_no_codegen_or_random_fallbacks(self) -> None:
        source = Path(solver.__file__).read_text()
        for token in [
            "subprocess",
            "os.system",
            "ctypes",
            "cffi",
            "gcc",
            "clang",
            "random",
        ]:
            with self.subTest(token=token):
                self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
