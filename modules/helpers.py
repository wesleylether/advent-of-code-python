import pprint


def pp(*args):
    pprint.pp(*args)


def dd(*args):
    print(*args)
    exit()


def ddd(*args):
    pprint.pp(*args)
    exit()


def generate_number_distributions(total, divisions):
    possible_numbers = range(1, total)
    combinations = []

    def find_combinations(current, rest):
        if len(current) == divisions:
            if sum(current) == total:
                combinations.append(tuple(current))
            return
        for num in rest:
            find_combinations(current + [num], rest)

    find_combinations([], list(possible_numbers))

    return sorted(combinations, key=lambda x: (sum(x), tuple(x)))
