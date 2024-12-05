from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0
for line in input_file.split("\n"):
    p1 += len(line) - len(eval(line))
    p2 += len(line.replace("\\", "\\\\").replace('"', '\\"')) - len(line) + 2

# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
