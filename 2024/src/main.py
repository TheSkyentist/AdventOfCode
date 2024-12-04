# Import packages
import argparse
from python import download, run_day

def main():
    # Create parser
    parser = argparse.ArgumentParser(description='Advent of Code 2024 in Python')

    # Add arguments
    parser.add_argument('day', type=int, help='Day to solve')
    parser.add_argument('--year', type=int, default=2024, help='Year of Advent of Code')

    # Parse arguments
    args = parser.parse_args()

    # Download data
    if download(args.day, args.year):

        # Run Solution
        run_day(args.day)

if __name__ == '__main__':
    main()
