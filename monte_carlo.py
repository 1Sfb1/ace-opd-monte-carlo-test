"""Estimate pi with a Monte Carlo simulation in the unit square."""
import random


def is_in_unit_circle(x, y):
    """Return True when (x, y) lies inside or on the unit circle around the origin."""
    return x * x + y * y <= 1


def estimate_pi(n, seed):
    """Estimate pi from n random points in the unit square, reproducibly for a given seed."""
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")
    rng = random.Random(seed)
    inside = 0
    for _ in range(n):
        x = rng.random()
        y = rng.random()
        if is_in_unit_circle(x, y):
            inside += 1
    return 4 * inside / n


if __name__ == "__main__":
    for n in (100, 10_000, 1_000_000):
        print(n, estimate_pi(n, 42))
