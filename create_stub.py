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

    stub_content = """import re
import time
from collections import defaultdict, Counter, deque
from copy import deepcopy
from math import gcd

from modules.advent_of_code import get_input

start_time = time.time_ns()

input_file = get_input()
print(input_file)

end_time = time.time_ns()
duration = end_time - start_time
print(f"Time: {duration / 1_000_000.0}ms")
"""

    with open(filename, 'w') as file:
        file.write(stub_content)

    print(f"File {filename} created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: create <year> <day>")
    else:
        year = sys.argv[1]
        day = int(sys.argv[2])
        create_stub(year, day)