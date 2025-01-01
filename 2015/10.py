from modules.advent_of_code import solve_one, solve_two, get_data

input_file = get_data()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file


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


def part_one():
    count = input_file
    for _ in range(40):
        count = look_and_say(count)
    return len(count)


def part_two():
    count = input_file
    for _ in range(50):
        count = look_and_say(count)
    return len(count)


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
