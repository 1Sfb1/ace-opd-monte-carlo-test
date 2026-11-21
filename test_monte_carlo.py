import math
import unittest

from monte_carlo import estimate_pi, is_in_unit_circle


class IsInUnitCircleTest(unittest.TestCase):
    def test_point_on_the_edge_counts(self):
        self.assertTrue(is_in_unit_circle(1.0, 0.0))
        self.assertTrue(is_in_unit_circle(0.0, -1.0))

    def test_point_inside_and_outside(self):
        self.assertTrue(is_in_unit_circle(0.5, 0.5))
        self.assertTrue(is_in_unit_circle(-0.6, -0.6))
        self.assertFalse(is_in_unit_circle(0.8, 0.8))

    def test_returns_a_bool(self):
        self.assertIsInstance(is_in_unit_circle(0.1, 0.1), bool)


class EstimatePiTest(unittest.TestCase):
    def test_example_from_the_assignment(self):
        self.assertEqual(estimate_pi(4, 42), 3.0)

    def test_same_seed_gives_same_result(self):
        self.assertEqual(estimate_pi(1000, 7), estimate_pi(1000, 7))

    def test_many_points_are_close_to_pi(self):
        self.assertAlmostEqual(estimate_pi(100_000, 1), math.pi, delta=0.02)

    def test_rejects_a_non_positive_n(self):
        with self.assertRaises(ValueError):
            estimate_pi(0, 1)


if __name__ == "__main__":
    unittest.main()
