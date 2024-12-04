import re

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0

multiplies = re.findall(r"mul\((\d+){,3},(\d+){,3}\)", input_file)
for m in multiplies:
    p1 += int(m[0]) * int(m[1])

tokens = re.findall(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))", input_file)
skip_next = False
for token in tokens:
    if token == "don't()":
        skip_next = True
    elif token == "do()":
        skip_next = False
    elif token.startswith("mul("):
        if not skip_next:
            numbers = [int(n) for n in re.findall(r"\d{1,3}", token)]
            p2 += numbers[0] * numbers[1]

# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
