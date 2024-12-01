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

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
print(input_file)




# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()

"""
    with open(filename, "w") as file:
        file.write(stub_content)

    print(f"File {filename} created successfully.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: create <year> <day>")
    else:
        create_stub(int(sys.argv[1]), int(sys.argv[2]))
