import argparse
import os
import sys
from datetime import datetime

from modules.advent_of_code import get_data


def create_stub(year: int, day: int, create_test_yaml=False):
    create_directories(year)

    puzzle_file = f"{year}/{day:02d}.py"

    if create_file(
        """import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import solve
from modules.grid import Grid
from modules.helpers import dd, ddd, pp
from modules.list import List

# Start coding here
# ==========================================================================
def parse(data):
    return data


def part_one(data):
    count = 0
    dd(data)
    
    return count


def part_two(data):
    count = 0
    dd(data)
    
    return count


# Answers
# ==========================================================================
solve(part_one, parse)
# solve(part_two, parse)
""",
        puzzle_file,
    ):
        print(f"Puzzle File {puzzle_file} created successfully.")

    get_data(year, day)

    if create_test_yaml:
        test_file = f"input/{year}/{day:02d}.yaml"

        if create_file(
            """part_one:
    -   data: &data |
            <example>
        answer: 0
        # args:
        #     - 0
        # kwargs:
        #     key: value

part_two:
    -   data: *data
        answer: 0
        # args:
        #     - 0
        # kwargs:
        #     key: value
""",
            test_file,
        ):
            print(f"Test yaml file {puzzle_file} created successfully.")


def create_directories(year):
    directory = f"{year}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    test_directory = f"input/{year}"
    if not os.path.exists(test_directory):
        os.makedirs(test_directory)


def create_file(content, filename) -> bool:
    if os.path.exists(filename):
        print(f"File {filename} already exists.")
        return False

    with open(filename, "w") as file:
        file.write(content)

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", default=datetime.now().year)
    parser.add_argument("--day", default=datetime.now().day)
    parser.add_argument("--test", action="store_true")
    args = parser.parse_args()
    create_stub(int(args.year), int(args.day), bool(args.test))
