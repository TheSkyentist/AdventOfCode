# Import packages
import io
import numpy as np


def read_input(generator) -> np.ndarray:
    """
    Read input file
    """
    return np.genfromtxt(generator, dtype=int)


def part1(data: np.ndarray) -> int:
    """
    Part 1
    """
    return np.abs(np.diff(np.sort(data, axis=0), axis=1)).sum()


def part2(data: np.ndarray) -> int:
    """
    Part 2
    """

    # Read input
    x, y = data.T

    # Compute total
    return np.sum([i * (x == i).sum() * (y == i).sum() for i in np.intersect1d(x, y)])


# Define test data
test_data_str = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def solve():
    # Define test data
    test_data = read_input(io.StringIO(test_data_str))

    # Test
    assert part1(test_data) == 11
    assert part2(test_data) == 31

    # Get input
    data = read_input('data/input1.py.txt')

    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
