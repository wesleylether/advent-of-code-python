from modules.advent_of_code import solve
from modules.list import List


# Start coding here
# ==========================================================================
def parse(data):
    left = List()
    right = List()
    for line in data.splitlines():
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()
    return left, right


def part_one(data):
    count = 0
    left, right = data

    for i in range(len(left)):
        count += abs(left[i] - right[i])

    return count


def part_two(data):
    count = 0
    left, right = data

    for i in range(len(left)):
        count += left[i] * right.count(left[i])

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
