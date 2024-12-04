# Import packages
import numpy as np


def read_input() -> list[np.ndarray]:
    """
    Read input file
    """
    with open('data/input2.py.txt') as f:
        return [np.array([int(x) for x in line.split()]) for line in f]


def isSafe(row: np.ndarray) -> bool:
    """
    Check if row is safe
    """
    diff = np.diff(row)
    absdiff = np.abs(diff)

    return np.logical_and.reduce(
        [np.all(absdiff >= 1), np.all(absdiff <= 3), np.unique(np.sign(diff)).size == 1]
    )


def part1() -> None:
    """
    Part 1
    """

    # Read input
    data = read_input()

    # Total number of safe rows
    solution = sum(isSafe(row) for row in data)

    print('Part 1:', solution)


def part2() -> None:
    """
    Part 2
    """

    # Read input
    data = read_input()

    def isSafeDampened(row: np.ndarray) -> bool:
        # If row isn't safe
        if not isSafe(row):
            # Iterate over all possible subsets
            for i in range(0, row.size):
                # If subset is safe
                if isSafe(np.delete(row, i)):
                    return True
            # If no subset is safe
            return False

        else:
            return True

    solution = sum(isSafeDampened(row) for row in data)

    print('Part 2:', solution)


def solve():
    part1()
    part2()
