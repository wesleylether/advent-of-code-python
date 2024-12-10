import re

from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

pattern = re.compile(r"(\w+): (\d+)")
parse_line = lambda line: [(n, int(v)) for n, v in re.findall(pattern, line)]
data = list(map(parse_line, input_file.splitlines()))

check_1 = lambda name, val: val == MFCSAM[name]
check_2 = lambda name, val: (
    val > MFCSAM[name]
    if name in ("cats", "trees")
    else val < MFCSAM[name] if name in ("pomeranians", "goldfish") else val == MFCSAM[name]
)

solve = lambda data, func: next(i for i, line in enumerate(data, 1) if all(func(*p) for p in line))

# Print the answers here
# ==========================================================================
answer_part_one(solve(data, check_1))
answer_part_two(solve(data, check_2))

# End of Code
# ==========================================================================
timer.end_timer()
