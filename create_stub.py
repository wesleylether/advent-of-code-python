import os
import sys


def create_stub(year, day):
    create_directories(year)

    puzzle_file = f"{year}/{day:02d}.py"

    create_file(
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
solve(part_two, parse)
""",
        puzzle_file,
    )

    test_file = f"input/{year}/{day:02d}.yaml"

    create_file(
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
    )

    print(f"Files {puzzle_file} and {test_file} created successfully.")


def create_directories(year):
    directory = f"{year}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    test_directory = f"input/{year}"
    if not os.path.exists(test_directory):
        os.makedirs(test_directory)


def create_file(content, filename):
    if os.path.exists(filename):
        print(f"File {filename} already exists.")
        return

    with open(filename, "w") as file:
        file.write(content)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: create <year> <day>")
    else:
        create_stub(int(sys.argv[1]), int(sys.argv[2]))
