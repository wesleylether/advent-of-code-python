from functools import lru_cache

from modules.advent_of_code import solve


# ==========================================================================
def parse(data, _):
    return sorted(map(int, data.splitlines()))


def part_one(data, eggnog):
    @lru_cache(maxsize=None)
    def count_combinations(target, index):
        if target == 0:
            return 1
        if target < 0 or index == len(data):
            return 0
        return count_combinations(target - data[index], index + 1) + count_combinations(
            target, index + 1
        )

    return count_combinations(eggnog, 0)


def part_two(data, eggnog):
    @lru_cache(maxsize=None)
    def count_minimum_combinations(target, index, used):
        if target == 0:
            return used
        if target < 0 or index == len(data):
            return float("inf")
        return min(
            count_minimum_combinations(target - data[index], index + 1, used + 1),
            count_minimum_combinations(target, index + 1, used),
        )

    @lru_cache(maxsize=None)
    def count_exact_combinations(target, index, used, min_used):
        if target == 0:
            return 1 if used == min_used else 0
        if target < 0 or index == len(data):
            return 0
        return count_exact_combinations(
            target - data[index], index + 1, used + 1, min_used
        ) + count_exact_combinations(target, index + 1, used, min_used)

    min_containers = count_minimum_combinations(eggnog, 0, 0)
    return count_exact_combinations(eggnog, 0, 0, min_containers)


# Answers
# ==========================================================================
solve(part_one, parse, 150)
solve(part_two, parse, 150)
