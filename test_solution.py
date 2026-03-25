import unittest
from pathlib import Path

import solution as solver


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

    def test_solution_module_has_no_codegen_or_random_fallbacks(self) -> None:
        source = Path(solver.__file__).read_text()
        for token in ["subprocess", "os.system", "ctypes", "cffi", "gcc", "clang", "random"]:
            with self.subTest(token=token):
                self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
