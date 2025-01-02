from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data):
    count = 0
    for line in data.splitlines():
        count += len(line) - len(eval(line))

    return count


def part_two(data):
    count = 0
    for line in data.splitlines():
        count += len(line.replace("\\", "\\\\").replace('"', '\\"')) - len(line) + 2

    return count


# Answers
# ==========================================================================
solve(part_one)
solve(part_two)
