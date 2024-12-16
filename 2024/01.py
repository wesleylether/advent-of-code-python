from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    l = []
    r = []
    for line in input_file.splitlines():
        left, right = line.split()
        l.append(int(left))
        r.append(int(right))

    l.sort()
    r.sort()
    return l, r


def part_one():
    count = 0
    l, r = parse_input()

    for i in range(len(l)):
        count += abs(l[i] - r[i])

    return count


def part_two():
    count = 0
    l, r = parse_input()

    for i in range(len(l)):
        count += l[i] * r.count(l[i])

    return count


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
