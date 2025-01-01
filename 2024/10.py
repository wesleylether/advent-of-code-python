from modules.advent_of_code import solve
from modules.grid import Grid, GridValueType, GridOrientation


# Start coding here
# ==========================================================================
def parse(data):
    return Grid.from_string(data, GridValueType.Int)


def check_neighbours(grid, visited, level, position):
    count = 0
    for neighbour in grid.neighbors(
        position,
        GridOrientation.Horizontal | GridOrientation.Vertical,
    ):
        if level == 8 and neighbour[0] == 9:
            visited.add(neighbour[1])
            count += 1
            continue

        if level + 1 == neighbour[0]:
            count += check_neighbours(grid, visited, neighbour[0], neighbour[1])

    return count


def part_one(data):
    count = 0
    grid = data
    visited = set()

    for item, position in grid:
        if len(visited) > 0:
            count += len(visited)
            visited = set()

        if item == 0:
            check_neighbours(grid, visited, item, position)

    return count


def part_two(data):
    count = 0
    grid = data
    visited = set()

    for item, position in grid:
        if len(visited) > 0:
            visited = set()

        if item == 0:
            count += check_neighbours(grid, visited, item, position)

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
