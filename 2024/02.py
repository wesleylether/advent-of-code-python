from modules.advent_of_code import solve
from modules.list import List


# Start coding here
# ==========================================================================
def parse(data):
    return [List(map(int, line.split())) for line in data.splitlines()]


def check_numbers(nums):
    if all(nums[i] < nums[i + 1] <= nums[i] + 3 for i in range(len(nums) - 1)):
        return True
    elif all(nums[i] > nums[i + 1] >= nums[i] - 3 for i in range(len(nums) - 1)):
        return True

    return False


def part_one(data):
    count = 0
    for numbers in data:
        if check_numbers(numbers):
            count += 1

    return count


def part_two(data):
    count = 0
    for numbers in data:
        if check_numbers(numbers):
            count += 1
            continue

        for i in range(len(numbers)):
            sublist = numbers[:i] + numbers[i + 1 :]
            if check_numbers(sublist):
                count += 1
                break

    return count


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
