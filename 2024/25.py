from modules.advent_of_code import solve
from modules.grid import Grid


# Start coding here
# ==========================================================================
def parse(data):
    locks = []
    keys = []
    for grid_input in data.split("\n\n"):
        grid = Grid.from_string(grid_input)
        combination = [x.count("#") - 1 for x in grid.columns()]
        if grid[0, 0] == "#":
            locks.append((combination, grid))
        else:
            keys.append((combination, grid))

    return locks, keys


def part_one(data):
    count = 0
    locks, keys = data
    for lock_combination, _ in locks:
        for key_combination, _ in keys:
            fits = True
            for i in range(len(lock_combination)):
                if lock_combination[i] + key_combination[i] > 5:
                    fits = False
                    break

            if fits:
                count += 1

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
