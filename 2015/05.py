import re

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0

for string in input_file.split():
    if re.search(r"(..).*\1", string) and re.search(r"(.).\1", string):
        p2 += 1

    vowels = re.findall(r"[aeiou]", string)
    if len(vowels) < 3:
        continue
    if not re.search(r"(.)\1", string):
        continue
    if re.search(r"ab|cd|pq|xy", string):
        continue
    p1 += 1


# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
