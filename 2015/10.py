from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()


# Start coding here
# ==========================================================================
def look_and_say(sequence):
    result = ""
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            i += 1
            count += 1
        result += str(count) + sequence[i]
        i += 1
    return result


p1 = input_file
for _ in range(40):
    p1 = look_and_say(p1)
answer_part_one(len(p1))
timer.end_timer()

timer.start_timer()
p2 = input_file
for _ in range(50):
    p2 = look_and_say(p2)
answer_part_two(len(p2))
timer.end_timer()
