# Import packages
import numpy as np
import networkx as nx


def read_input(file: str) -> str:
    """
    Read input file
    """
    lines = file.strip().split('\n')
    return np.array([list(line) for line in lines])


def walkgrid(grid: np.ndarray) -> np.ndarray:
    # Find the guard
    guard = np.argwhere(grid == '^')[0]

    # Get grid dimensions
    height, width = grid.shape

    # Define guard direction
    v = np.array([-1, 0])

    # While the guard is in the grid
    while True:
        # Get the next position
        gv = guard + v

        # If the next position is out of bounds
        if np.logical_or.reduce(
            [0 > gv[0], gv[0] >= height, 0 > gv[1], gv[1] >= width]
        ):
            if not grid[tuple(guard)] == '^':
                grid[tuple(guard)] = 'X'
            break

        # If the next position is an obstruction
        elif grid[tuple(gv)] == '#':
            # Rotate to the left
            v = np.array([v[1], -v[0]])

        # Otherwise, recolor the point
        else:
            if not grid[tuple(guard)] == '^':
                grid[tuple(guard)] = 'X'

            # Move to the next position
            guard = gv

    # Count the number of points
    return grid


def isloop(grid: np.ndarray) -> bool:
    # Create directed graph
    graph = nx.DiGraph()

    # Find the guard
    guard = np.argwhere(grid == '^')[0]

    # Get grid dimensions
    height, width = grid.shape

    # Define guard direction
    v0 = np.array([-1, 0])
    v = v0

    # While the guard is in the grid
    while True:
        # Get the next position
        gv = guard + v

        # If the next position is out of bounds
        if np.logical_or.reduce(
            [0 > gv[0], gv[0] >= height, 0 > gv[1], gv[1] >= width]
        ):
            return False
            break

        # If the next position is an obstruction
        elif grid[tuple(gv)] == '#':
            # Rotate to the left
            v = np.array([v[1], -v[0]])

        # Otherwise, recolor the point
        else:

            # Check if edge is already in the graph
            if graph.has_edge(tuple(guard), tuple(gv)):
                return True

            # Record the edge
            graph.add_edge(tuple(guard), tuple(gv))

            # Move to the next position
            guard = gv

    # Check for loops
    return False


def part1(grid: np.ndarray) -> int:
    """
    Part 1
    """
    # Add 1 for the guard spot
    return np.sum(walkgrid(grid) == 'X') + 1


def part2(grid: np.ndarray) -> int:
    """
    Part 2
    """
    # Get possible positions for the barrier
    walked = walkgrid(grid)

    # Iterate over possible positions
    total = 0
    for barrier in np.argwhere(walked == 'X'):
        # Copy the grid
        grid_copy = np.copy(grid)

        # Place the barrier
        grid_copy[tuple(barrier)] = '#'

        # Check for loops
        if isloop(grid_copy):
            total += 1

    return total


test_data_str = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def solve():
    # Define test data
    test_data = read_input(test_data_str)

    # Test
    assert part1(test_data) == 41
    assert part2(test_data) == 6

    # Get input
    with open('data/input6.py.txt') as file:
        data = read_input(file.read())

    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
