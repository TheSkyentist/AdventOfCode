# Import packages
import os
import requests


def download(day: int, year: int = 2024) -> None:
    """
    Download data from Advent of Code website
    """

    # File where data will be stored
    file = f'data/input{day}.py.txt'

    if os.path.exists(file):
        print(f'Python data for day {day} already downloaded.')
        return

    # URL to download data from
    url = f'https://adventofcode.com/{year}/day/{day}/input'

    # Get session cookie
    with open(f'aoc_{year}_session.txt') as f:
        session_cookie = f.read().strip()

    # Request data
    try:
        response = requests.get(url, cookies={'session': session_cookie})
    except Exception as e:
        print(f'Error downloading Python data for day {day}: {e}')

    # Check if response is 404
    if response.status_code == 404:
        print(f'Python data for day {day} is not available.')
        return

    # Save data to file
    with open(file, 'w') as f:
        f.write(response.text)
    print(f'Python data for day {day} downloaded.')
