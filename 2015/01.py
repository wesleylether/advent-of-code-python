from modules.advent_of_code import solve_one, solve_two, get_data

input_file = get_data()


# Start coding here
# ==========================================================================
def parse_input():
    return enumerate(input_file)


def part_one():
    count = 0
    for i, char in parse_input():
        count += 1 if char == "(" else -1

    return count


def part_two():
    count = {"a": 0, "b": 0}
    for i, char in parse_input():
        count["a"] += 1 if char == "(" else -1

        if count["a"] == -1 and count["b"] == 0:
            count["b"] = i + 1

    return count["b"]


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
