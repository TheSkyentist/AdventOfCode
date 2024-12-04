# Import packages
import argparse
import importlib
from python.download import download


def main():
    # Create parser
    parser = argparse.ArgumentParser(description='Advent of Code 2024 in Python')

    # Add arguments
    parser.add_argument('day', type=int, help='Day to solve')
    parser.add_argument('--year', type=int, default=2024, help='Year of Advent of Code')

    # Parse arguments
    args = parser.parse_args()

    # Download data
    download(args.day, args.year)

    # Dynamically import the solution module
    try:
        module_name = f'py.day{args.day}'
        solution_module = importlib.import_module(module_name)

        # Call the solve() function
        if hasattr(solution_module, 'solve'):
            solution_module.solve()
        else:
            print(f'Python solve not implemented for day {args.day}.')
    except ModuleNotFoundError:
        print(f'Python code for day {args.day} not found.')
    except Exception as e:
        print(f'An error occurred for python code for day {args.day}, {e}.')


if __name__ == '__main__':
    main()
