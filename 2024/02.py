from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
p1 = 0
p2 = 0

for report in input_file.split("\n"):
    numbers = [int(n) for n in report.split(" ")]

    def check_numbers(nums):
        if all(nums[i] < nums[i + 1] <= nums[i] + 3 for i in range(len(nums) - 1)):
            return True
        elif all(nums[i] > nums[i + 1] >= nums[i] - 3 for i in range(len(nums) - 1)):
            return True

        return False

    if check_numbers(numbers):
        p1 += 1
        p2 += 1
        continue

    for i in range(len(numbers)):
        sublist = numbers[:i] + numbers[i + 1 :]
        if check_numbers(sublist):
            p2 += 1
            break

# Print the answers here
# ==========================================================================
answer_part_one(p1)
answer_part_two(p2)

# End of Code
# ==========================================================================
timer.end_timer()
