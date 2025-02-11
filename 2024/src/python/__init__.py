# Import your day modules
from . import day1, day2, day3, day4, day5, day6, day7  # Add more day imports as needed
from .download import download

# Expose functions
__all__ = ['run_day', 'download']  # Public API


def run_day(day: int):
    # Match the day to the corresponding solver
    match day:
        case 1:
            day1.solve()
        case 2:
            day2.solve()
        case 3:
            day3.solve()
        case 4:
            day4.solve()
        case 5:
            day5.solve()
        case 6:
            day6.solve()
        case 7:
            day7.solve()
        case _:
            print(f'No Python solution implemented for day {day}.')
