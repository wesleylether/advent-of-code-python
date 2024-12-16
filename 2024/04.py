from modules.advent_of_code import solve_one, solve_two, get_input
from modules.enums import Direction
from modules.grid import Grid

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return Grid.from_string(input_file)


def part_one():
    count = 0
    valid_range = ["M", "A", "S"]
    grid = parse_input()
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


def part_two():
    count = 0
    grid = parse_input()
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
solve_one(part_one)
solve_two(part_two)
