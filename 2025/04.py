from modules.advent_of_code import solve
from modules.grid import Grid
from modules.list import List

ParsedData = Grid


# Start coding here
# ==========================================================================
def parse(data) -> ParsedData:
    return Grid.from_string(data)


def part_one(data: ParsedData):
    count = 0
    for rol, position in data:
        adjacent = 0
        for a in data.adjacent(position):
            if a == "@":
                adjacent += 1

        if adjacent < 4 and rol == "@":
            count += 1

    return count


def part_two(data):
    count = 0
    grid = data
    changed = True

    while changed:
        changed = False
        removed = List()
        for rol, position in grid:
            adjacent = 0
            for a in data.adjacent(position):
                if a == "@":
                    adjacent += 1

            if adjacent < 4 and rol == "@":
                count += 1
                removed.append(position)

        if removed.length() > 0:
            changed = True
            for position in removed:
                grid[position] = "."

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
