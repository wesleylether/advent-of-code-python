from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    left = []
    right = []
    for line in input_file.splitlines():
        left, right = line.split()
        left.append(int(left))
        right.append(int(right))

    left.sort()
    right.sort()
    return left, right


def part_one():
    count = 0
    left, right = parse_input()

    for i in range(len(left)):
        count += abs(left[i] - right[i])

    return count


def part_two():
    count = 0
    left, right = parse_input()

    for i in range(len(left)):
        count += left[i] * right.count(left[i])

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
