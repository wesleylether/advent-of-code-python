from collections import Counter, deque

from toolz import pipe

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================
def parse(data):
    disk = []
    index = 0

    for i, n in enumerate(data):
        if i % 2:
            for _ in range(int(n)):
                disk.append(None)
        else:
            for _ in range(int(n)):
                disk.append(index)
            index += 1

    return disk


def rearrange_disk(disk):
    n_none = disk.count(None)
    for _ in range(len([x for x in disk if x is not None])):
        try:
            first_none_index = disk.index(None)
            disk = disk[:first_none_index] + [disk[-1]] + disk[first_none_index + 1 : -1]
        except ValueError:
            pass

    return disk + [None] * n_none


def max_adjacent_none(lst):
    max_count = 0
    current_count = 0

    for item in lst:
        if item is None:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0

    return max_count


def rearrange_disk_fragments(disk):
    counter = Counter(disk)
    queue = deque(disk)

    def none_count_on_index(i):
        index = i
        count = 0
        while queue[index] is None:
            index += 1
            count += 1

        return count

    for num, count in reversed(counter.items()):
        if queue.index(num) < queue.index(None):
            break

        if max_adjacent_none(queue) < count:
            continue

        if num is not None:
            none_index = queue.index(None)
            count_index = none_count_on_index(none_index)
            while count > count_index:
                none_index = queue.index(None, none_index + count_index)
                count_index = none_count_on_index(none_index)

            n_index = queue.index(num)
            if n_index > none_index:
                for x, y in zip(
                    range(n_index, n_index + count), range(none_index, none_index + count)
                ):
                    queue[x], queue[y] = queue[y], queue[x]

    return list(queue)


def get_checksum(disk):
    result = 0
    for i, n in enumerate(disk):
        if n is not None:
            result += i * int(n)
    return result


def part_one(data):
    return pipe(
        data,
        rearrange_disk,
        get_checksum,
    )


def part_two(data):
    return pipe(
        data,
        rearrange_disk_fragments,
        get_checksum,
    )


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
