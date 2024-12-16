import os
import sys


def create_stub(year, day):
    directory = f"{year}"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = f"{directory}/{day:02d}.py"
    if os.path.exists(filename):
        print(f"File {filename} already exists.")
        return

    stub_content = """
import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid
from modules.helpers import dd, ddd, pp

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file


def part_one():
    count = 0
    data = parse_input()
    dd(data)
    
    return count


def part_two():
    count = 0
    data = parse_input()
    
    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)

"""
    with open(filename, "w") as file:
        file.write(stub_content)

    print(f"File {filename} created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: create <year> <day>")
    else:
        create_stub(int(sys.argv[1]), int(sys.argv[2]))
