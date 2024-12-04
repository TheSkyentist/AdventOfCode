# Import packages
import regex as re


def read_input() -> str:
    """
    Read input file
    """
    with open('data/input3.py.txt') as f:
        return f.read()


def part1() -> None:
    """
    Part 1
    """

    # Read input
    memory = read_input()

    # Get regex pattern
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')

    # Print matches
    matches = pattern.findall(memory)

    # Multiplication pairs
    pairs = [tuple(map(int, match[4:-1].split(','))) for match in matches]

    # Get solution
    solution = sum(x * y for x, y in pairs)

    print('Part 1:', solution)


def part2() -> None:
    """
    Part 2
    """

    # Read input
    memory = read_input()

    # Get regex pattern
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')

    # Print matches
    matches = pattern.findall(memory)

    # Get rid of matches
    control = True
    good_matches = []
    for match in matches:
        if match == 'do()':
            control = True
        elif match == "don't()":
            control = False
        elif control:
            good_matches.append(match)

    # Multiplication pairs
    pairs = [tuple(map(int, match[4:-1].split(','))) for match in good_matches]

    # Get solution
    solution = sum(x * y for x, y in pairs)

    print('Part 2:', solution)


def solve():
    part1()
    part2()
