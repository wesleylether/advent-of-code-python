from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data):
    count = 0
    for i, char in enumerate(data):
        count += 1 if char == "(" else -1

    return count


def part_two(data):
    count = {"a": 0, "b": 0}
    for i, char in enumerate(data):
        count["a"] += 1 if char == "(" else -1

        if count["a"] == -1 and count["b"] == 0:
            count["b"] = i + 1

    return count["b"]


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
