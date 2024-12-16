from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return input_file.splitlines()


def part_one():
    count = 0
    for line in parse_input():
        count += len(line) - len(eval(line))

    return count


def part_two():
    count = 0
    for line in parse_input():
        count += len(line.replace("\\", "\\\\").replace('"', '\\"')) - len(line) + 2

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
