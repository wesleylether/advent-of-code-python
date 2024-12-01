from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
lines = input_file.split("\n")
p1 = 0
p2 = 0
LEFT = []
RIGHT = []
for line in lines:
    left, right = line.split()
    LEFT.append(int(left))
    RIGHT.append(int(right))

LEFT.sort()
RIGHT.sort()

for i in range(len(LEFT)):
    p1 += abs(LEFT[i] - RIGHT[i])
    p2 += LEFT[i] * RIGHT.count(LEFT[i])

# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
