# Import packages
import io
import numpy as np


def read_input(file) -> list[np.ndarray]:
    """
    Read input file
    """
    return [np.array([int(x) for x in line.split()]) for line in file]


def isSafe(row: np.ndarray) -> bool:
    """
    Check if row is safe
    """
    absdiff = np.abs(diff := np.diff(row))

    return np.logical_and.reduce(
        [np.all(absdiff >= 1), np.all(absdiff <= 3), np.unique(np.sign(diff)).size == 1]
    )


def part1(data: list[np.ndarray]) -> int:
    """
    Part 1
    """

    # Total number of safe rows
    return sum(isSafe(row) for row in data)


def part2(data: list[np.ndarray]) -> int:
    """
    Part 2
    """

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

    return sum(isSafeDampened(row) for row in data)


test_data_str = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def solve():
    # Define test data
    test_data = read_input(io.StringIO(test_data_str))
    assert part1(test_data) == 2
    assert part2(test_data) == 4

    # Get input
    with open('data/input2.py.txt') as f:
        data = read_input(f)

    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
