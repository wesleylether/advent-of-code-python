from functools import lru_cache

from modules.advent_of_code import solve_one, solve_two, get_data

input_file = get_data()


# Start coding here
# ==========================================================================
def parse_input():
    return sorted(map(int, input_file.splitlines()))


def part_one():
    containers = parse_input()

    @lru_cache(maxsize=None)
    def count_combinations(target, index):
        if target == 0:
            return 1
        if target < 0 or index == len(containers):
            return 0
        return count_combinations(target - containers[index], index + 1) + count_combinations(
            target, index + 1
        )

    return count_combinations(150, 0)


def part_two():
    containers = parse_input()

    @lru_cache(maxsize=None)
    def count_minimum_combinations(target, index, used):
        if target == 0:
            return used
        if target < 0 or index == len(containers):
            return float("inf")
        return min(
            count_minimum_combinations(target - containers[index], index + 1, used + 1),
            count_minimum_combinations(target, index + 1, used),
        )

    @lru_cache(maxsize=None)
    def count_exact_combinations(target, index, used, min_used):
        if target == 0:
            return 1 if used == min_used else 0
        if target < 0 or index == len(containers):
            return 0
        return count_exact_combinations(
            target - containers[index], index + 1, used + 1, min_used
        ) + count_exact_combinations(target, index + 1, used, min_used)

    min_containers = count_minimum_combinations(150, 0, 0)
    return count_exact_combinations(150, 0, 0, min_containers)


# Answers
# ==========================================================================
solve_one(part_one)
solve_two(part_two)
