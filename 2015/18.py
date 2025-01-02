from modules.advent_of_code import solve
from modules.grid import Grid


# Start coding here
# ==========================================================================
def parse(data, **_):
    return Grid.from_string(data)


def part_one(data, steps):
    grid = data

    for _ in range(steps):
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


def part_two(data, steps):
    grid = data
    grid[0, 0] = "#"
    grid[0, grid.height - 1] = "#"
    grid[grid.width - 1, 0] = "#"
    grid[grid.width - 1, grid.height - 1] = "#"

    for _ in range(steps):
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
solve(part_one, parse, steps=100)
solve(part_two, parse, steps=100)
