import re

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
for line in input_file.split():
    numbers = re.match(r"(\d+)x(\d+)x(\d+)", line.strip())
    l, w, h = int(numbers.group(1)), int(numbers.group(2)), int(numbers.group(3))

    lw = l * w
    lh = l * h
    wh = w * h

    p1 += 2 * (lw + lh + wh) + min(lw, lh, wh)

    sides = [l, w, h]
    sides.sort()
    p2 += 2 * (sides[0] + sides[1]) + l * w * h


# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
