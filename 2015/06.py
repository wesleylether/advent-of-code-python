import re

from modules.advent_of_code import solve
from modules.grid import Grid


# Start coding here
# ==========================================================================
def parse(data):
    d = []
    for line in data.splitlines():
        action = re.findall(r"toggle|turn on|turn off", line)[0]
        x1, y1, x2, y2 = map(int, re.findall(r"\d+", line))
        d.append((action, x1, y1, x2, y2))

    return d


def part_one(data):
    grid = Grid(1000, 1000, 0)
    for action, x1, y1, x2, y2 in data:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == "toggle":
                    grid[x, y] = 1 if grid[x, y] == 0 else 0
                elif action == "turn on":
                    grid[x, y] = 1
                elif action == "turn off":
                    grid[x, y] = 0

    return grid.count_value(1)


def part_two(data):
    grid = Grid(1000, 1000, 0)
    for action, x1, y1, x2, y2 in data:
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
solve(part_one, parse)
solve(part_two, parse)
