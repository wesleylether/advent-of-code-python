from modules.advent_of_code import solve
from modules.list import List

ParsedData = tuple[List[tuple[int, int]], List[int]]


# Start coding here
# ==========================================================================
def parse(data) -> ParsedData:
    ranges_lines, id_lines = data.split("\n\n")
    ranges = List()
    for r in ranges_lines.splitlines():
        start, end = r.split("-")
        ranges.append((int(start), int(end)))

    return ranges, List([int(x) for x in id_lines.splitlines()])


def part_one(data: ParsedData):
    ranges, numbers = data

    count = 0
    for n in numbers:
        for r1, r2 in ranges:
            if r1 <= n <= r2:
                count += 1
                break
    return count


def part_two(data):
    ranges, _ = data

    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged_ranges = List()
    start, end = sorted_ranges[0]

    for next_start, next_end in sorted_ranges[1:]:
        if next_start <= end + 1:
            end = max(end, next_end)
        else:
            merged_ranges.append((start, end))
            start, end = next_start, next_end

    merged_ranges.append((start, end))
    return sum(end - start + 1 for start, end in merged_ranges)


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
