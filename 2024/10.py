from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid, GridValueType, GridOrientation

input_file = get_input()

# todo: fix this mess to separate the two parts

# Start coding here
# ==========================================================================
grid = Grid.from_string(input_file, GridValueType.Int)
count = 0


def check_neighbours(visited, level, position):
    global count

    for neighbour in grid.neighbors(
        position,
        GridOrientation.Horizontal | GridOrientation.Vertical,
    ):
        if level == 8 and neighbour[0] == 9:
            visited.add(neighbour[1])
            count += 1
            continue

        if level + 1 == neighbour[0]:
            check_neighbours(visited, neighbour[0], neighbour[1])


def part_one():
    count = 0
    visited = set()

    for item, position in grid:
        if len(visited) > 0:
            count += len(visited)
            visited = set()

        if item == 0:
            check_neighbours(visited, item, position)

    return count


def part_two():
    global count

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
