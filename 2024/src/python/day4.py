# Import packages
import numpy as np
from itertools import product


def read_input(file: str) -> str:
    """
    Read input file
    """
    lines = file.strip().split('\n')
    return np.array([list(line) for line in lines])


def part1(grid: np.ndarray) -> int:
    """
    Part 1
    """

    # Define search term
    search = np.array(list('XMAS'))

    # Iterate over dimensions
    total = 0
    for i in range(grid.shape[0]):
        # Get slices
        row = grid[i, :]
        column = grid[:, i]
        up_dag = np.diag(grid, i)
        low_dag = np.diag(grid, -i)
        up_rev_dag = np.diag(np.fliplr(grid), i)
        low_rev_dag = np.diag(np.fliplr(grid), -i)

        # If middle slices, don't double up
        if i == 0:
            slices = [row, column, up_dag, up_rev_dag]
        else:
            slices = [row, column, up_dag, low_dag, up_rev_dag, low_rev_dag]

        # Iterate over slices
        for sl in slices:
            # Handle when window is bigger than slice
            if sl.size < 4:
                continue

            # Get windows
            windows = np.lib.stride_tricks.sliding_window_view(sl, len(search))

            # Iterate over substrings
            for sub in [search, search[::-1]]:
                matches = np.all(windows == sub, axis=1)
                total += matches.sum()

    return total

def part2(grid: np.ndarray) -> int:
    """
    Part 2
    """

    # Find indices of all As
    inds = np.argwhere(grid == 'A')

    # Exclude those on the edge of the grid
    bad = np.logical_or.reduce(
        [inds[:, i] == j for i, j in product(range(2), [0, grid.shape[0] - 1])]
    )
    inds = inds[~bad]

    # Iterate over indices
    total = 0
    for x, y in inds:
        # Get adjacent corners
        rows = [x - 1, x - 1, x + 1, x + 1]
        cols = [y - 1, y + 1, y + 1, y - 1]

        # Get corner array
        corners = ''.join(grid[rows, cols])

        # Check if corner is an X-MAS
        xmas = np.logical_or.reduce(
            [corners == 'SSMM', corners == 'MSSM', corners == 'MMSS', corners == 'SMMS']
        )
        if xmas:
            total += 1

    return total


test_data_str = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def solve():

    # Define test data
    test_data = read_input(test_data_str)

    # Test
    assert part1(test_data) == 18
    assert part2(test_data) == 9

    # Get input
    with open('data/input4.py.txt') as file:
        data = read_input(file.read())

    print('Part 1:', part1(data))
    print('Part 2:', part2(data))