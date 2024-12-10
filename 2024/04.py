from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input
from modules.grid import Grid

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
directions = {
    "right": (1, 0),
    "left": (-1, 0),
    "down": (0, 1),
    "up": (0, -1),
    "down-right": (1, 1),
    "up-left": (-1, -1),
    "up-right": (1, -1),
    "down-left": (-1, 1),
}
valid_range = ["M", "A", "S"]

grid = Grid.from_string(input_file)
for letter in grid:
    current = grid.current

    if letter == "X":
        for direction in directions.keys():
            for step in range(1, 4):
                dx = directions[direction][0] * step + current[0]
                dy = directions[direction][1] * step + current[1]
                try:
                    next_letter = grid[dx, dy]
                except IndexError:
                    break

                if next_letter != valid_range[step - 1]:
                    break

                if step == 3:
                    p1 += 1
answer_part_one(p1)
timer.end_timer()

timer.start_timer()

p2 = 0
grid = Grid.from_string(input_file)
for letter in grid:
    current = grid.current

    if letter == "A":
        try:
            top_left = grid[current[0] - 1, current[1] - 1]
            top_right = grid[current[0] + 1, current[1] - 1]
            bottom_left = grid[current[0] - 1, current[1] + 1]
            bottom_right = grid[current[0] + 1, current[1] + 1]
        except IndexError:
            continue

        if top_left == bottom_left == "M" and top_right == bottom_right == "S":
            p2 += 1

        if top_left == bottom_left == "S" and top_right == bottom_right == "M":
            p2 += 1

        if top_left == top_right == "M" and bottom_left == bottom_right == "S":
            p2 += 1

        if top_left == top_right == "S" and bottom_left == bottom_right == "M":
            p2 += 1

answer_part_two(p2)
timer.end_timer()
