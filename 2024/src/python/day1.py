# Import packages
import numpy as np


def read_input() -> np.ndarray:
    """
    Read input file
    """
    return np.genfromtxt('data/input1.py.txt', dtype=int)


def part1() -> None:
    """
    Part 1
    """

    # Read input
    data = read_input()

    # Calculate solution
    solution = np.abs(np.diff(np.sort(data, axis=0), axis=1)).sum()

    print('Part 1:', solution)


def part2() -> None:
    """
    Part 2
    """

    # Read input
    x, y = read_input().T

    # Get unique
    u = np.intersect1d(x, y)

    # Compute total
    total = np.sum([i * (x == i).sum() * (y == i).sum() for i in u])

    print('Part 2:', total)


def solve():
    part1()
    part2()
