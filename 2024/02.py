from modules.advent_of_code import solve_one, solve_two, get_input

input_file = get_input()


# Start coding here
# ==========================================================================
def parse_input():
    return [list(map(int, line.split())) for line in input_file.splitlines()]


def check_numbers(nums):
    if all(nums[i] < nums[i + 1] <= nums[i] + 3 for i in range(len(nums) - 1)):
        return True
    elif all(nums[i] > nums[i + 1] >= nums[i] - 3 for i in range(len(nums) - 1)):
        return True

    return False


def part_one():
    count = 0
    for numbers in parse_input():
        if check_numbers(numbers):
            count += 1

    return count


def part_two():
    count = 0
    for numbers in parse_input():
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
solve_one(part_one)
solve_two(part_two)
