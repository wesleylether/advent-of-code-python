from modules.advent_of_code import solve
from modules.enums import Direction
from modules.grid import Grid


# Start coding here
# ==========================================================================
def parse(data):
    return Grid.from_string(data)


def part_one(data):
    count = 0
    valid_range = ["M", "A", "S"]
    grid = data
    for letter, position in grid:
        if letter == "X":
            for direction in Direction:
                for step in range(1, 4):
                    dx = direction.value[0] * step + position[0]
                    dy = direction.value[1] * step + position[1]
                    try:
                        next_letter = grid[dx, dy]
                    except IndexError:
                        break

                    if next_letter != valid_range[step - 1]:
                        break

                    if step == 3:
                        count += 1

    return count


def part_two(data):
    count = 0
    grid = data
    for letter, position in grid:
        if letter == "A":
            try:
                top_left = grid[position[0] - 1, position[1] - 1]
                top_right = grid[position[0] + 1, position[1] - 1]
                bottom_left = grid[position[0] - 1, position[1] + 1]
                bottom_right = grid[position[0] + 1, position[1] + 1]
            except IndexError:
                continue

            if top_left == bottom_left == "M" and top_right == bottom_right == "S":
                count += 1

            if top_left == bottom_left == "S" and top_right == bottom_right == "M":
                count += 1

            if top_left == top_right == "M" and bottom_left == bottom_right == "S":
                count += 1

            if top_left == top_right == "S" and bottom_left == bottom_right == "M":
                count += 1

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
