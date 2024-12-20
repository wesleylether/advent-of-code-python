from modules.advent_of_code import solve_two, get_input, solve_one
from modules.grid import Grid

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return Grid.from_string(input_file)


def part_one():
    grid = parse_input()

    for _ in range(100):
        new_grid = Grid(grid.width, grid.height, ".")
        for v, pos in grid:
            neighbors = grid.adjacent(pos)
            on = sum([1 for n in neighbors if n == "#"])
            if v == "#":
                new_grid[pos] = "#" if on in [2, 3] else "."
            else:
                new_grid[pos] = "#" if on == 3 else "."
        grid = new_grid

    return grid.count_value("#")


def part_two():
    grid = parse_input()
    grid[0, 0] = "#"
    grid[0, grid.height - 1] = "#"
    grid[grid.width - 1, 0] = "#"
    grid[grid.width - 1, grid.height - 1] = "#"

    for _ in range(100):
        new_grid = Grid(grid.width, grid.height, ".")
        for v, pos in grid:
            if pos in [
                (0, 0),
                (0, grid.height - 1),
                (grid.width - 1, 0),
                (grid.width - 1, grid.height - 1),
            ]:
                new_grid[pos] = "#"
                continue

            neighbors = grid.adjacent(pos)
            on = sum([1 for n in neighbors if n == "#"])
            if v == "#":
                new_grid[pos] = "#" if on in [2, 3] else "."
            else:
                new_grid[pos] = "#" if on == 3 else "."
        grid = new_grid

    return grid.count_value("#")


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
