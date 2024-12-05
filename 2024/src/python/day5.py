# Import packages
import numpy as np
import networkx as nx


def read_input(file: str) -> str:
    """
    Read input file
    """

    # Split on two newlines
    split = file.split('\n\n')

    # Return as list
    rules = np.genfromtxt(split[0].split('\n'), delimiter='|', dtype=int)
    allpages = [
        np.genfromtxt(page.split(','), dtype=int) for page in split[1].split('\n')[:-1]
    ]

    return rules, allpages


def buildGraph(rules: np.ndarray) -> nx.DiGraph:
    """
    Build graph from rules
    """

    # Create graph
    graph = nx.DiGraph()

    # Add edges
    for rule in rules:
        graph.add_edge(rule[0], rule[1])

    return graph


def sortUpdate(page: np.ndarray, graph: nx.DiGraph):
    """
    Sort page based on graph
    """

    # Build the subgraph
    subgraph = graph.subgraph(page)

    # Get the topological sort
    return np.array(list(nx.topological_sort(subgraph)))


def part1(data: tuple) -> int:
    """
    Part 1
    """

    # Unpack data
    graph = buildGraph(data[0])

    return sum([p[len(p) // 2] for p in data[1] if np.all(p == sortUpdate(p, graph))])


def part2(data: tuple) -> int:
    """
    Part 2
    """

    # Unpack data
    graph = buildGraph(data[0])

    return sum(
        [
            ps[len(p) // 2]
            for p in data[1]
            if not np.all(p == (ps := sortUpdate(p, graph)))
        ]
    )


test_data_str = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def solve():
    # Define test data
    test_data = read_input(test_data_str)

    # Test
    assert part1(test_data) == 143
    assert part2(test_data) == 123

    # # Get input
    with open('data/input5.py.txt') as file:
        data = read_input(file.read())

    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
