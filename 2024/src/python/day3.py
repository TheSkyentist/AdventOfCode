# Import packages
import regex as re
from operator import mul
from functools import reduce

def part1(memory: str) -> int:
    """
    Part 1
    """

    # Get regex pattern
    pattern = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

    # Multiplication pairs
    return sum(reduce(mul, map(int, match.groups())) for match in pattern.finditer(memory))
    
def part2(memory: str) -> int:
    """
    Part 2
    """

    # Append do() to start and split on don't
    split_memory = ("do()" + memory).split("don't()")

    # Regex pattern
    pattern = re.compile(r"do\(\)(.*)", re.DOTALL)
    search = [re.search(pattern, sm) for sm in split_memory]

    for s in search:
        print(s)
        if s is None:
            break
            

    return sum(part1(s.group(1)) for s in search)


def solve():
    # Define test data
    test_data_1 = (
        'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
    )
    test_data_2 = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )

    assert part1(test_data_1) == 161
    assert part2(test_data_2) == 48

    # Get input
    with open('data/input3.py.txt') as file:
        data = file.read()

    print('Part 1:', part1(data))
    print('Part 2:', part2(data))
