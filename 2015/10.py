from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def look_and_say(sequence):
    result = ""
    i = 0
    while i < len(sequence):
        count = 1
        while i + 1 < len(sequence) and sequence[i] == sequence[i + 1]:
            i += 1
            count += 1
        result += str(count) + sequence[i]
        i += 1
    return result


def part_one(data, steps):
    count = data
    for _ in range(steps):
        count = look_and_say(count)
    return len(count)


def part_two(data, steps):
    count = data
    for _ in range(steps):
        count = look_and_say(count)
    return len(count)


# Answers
# ==========================================================================
solve(part_one, None, 40)
solve(part_two, None, 50)
