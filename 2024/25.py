from modules.advent_of_code import solve_one, solve_two, get_input
from modules.grid import Grid

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    locks = []
    keys = []
    for grid_input in input_file.split("\n\n"):
        grid = Grid.from_string(grid_input)
        combination = [x.count("#") - 1 for x in grid.columns()]
        if grid[0, 0] == "#":
            locks.append((combination, grid))
        else:
            keys.append((combination, grid))

    return locks, keys


def part_one():
    count = 0
    locks, keys = parse_input()
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


def part_two():
    count = 0
    data = parse_input()

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
