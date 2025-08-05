from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def part_one(data):
    target = int(data)
    houses = [0] * (target // 10)

    for elf in range(1, len(houses)):
        for house in range(elf, len(houses), elf):
            houses[house] += elf * 10

    for house, presents in enumerate(houses):
        if presents >= target:
            return house, presents
    return None


def part_two(data):
    target = int(data)
    houses = [0] * (target // 11)

    for elf in range(1, len(houses)):
        visit_count = 0
        for house in range(elf, len(houses), elf):
            if visit_count >= 50:
                break
            houses[house] += elf * 11
            visit_count += 1

    for house, presents in enumerate(houses):
        if presents >= target:
            return house, presents
    return None


# Answers
# ==========================================================================
# solve(part_one)
solve(part_two)
