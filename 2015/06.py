import re

from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    data = []
    for line in input_file.splitlines():
        action = re.findall(r"toggle|turn on|turn off", line)[0]
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        data.append((action, x1, y1, x2, y2))

    return data


def part_one():
    grid = Grid(1000, 1000, 0)
    for action, x1, y1, x2, y2 in parse_input():
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == "toggle":
                    grid[x, y] = 1 if grid[x, y] == 0 else 0
                elif action == "turn on":
                    grid[x, y] = 1
                elif action == "turn off":
                    grid[x, y] = 0

    return grid.count_value(1)


def part_two():
    grid = Grid(1000, 1000, 0)
    for action, x1, y1, x2, y2 in parse_input():
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == "toggle":
                    grid[x, y] += 2
                elif action == "turn on":
                    grid[x, y] += 1
                elif action == "turn off":
                    grid[x, y] = max(0, grid[x, y] - 1)

    return grid.sum_values()


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
