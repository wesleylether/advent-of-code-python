from modules.advent_of_code import Timer, answer_part_one, answer_part_two, get_input

timer = Timer()
input_file = get_input()
timer.start_timer()

# Start coding here
# ==========================================================================
values = {v: 1 for v in input_file.split()}
# print(values)

index = 0
while index < 75:
    index += 1
    print(f"Index: {index}")

    new_values = {}

    def append_dict(key, value):
        if key in new_values.keys():
            new_values[key] += value
        else:
            new_values[key] = value

    for item, count in values.items():
        if item == "0":
            append_dict("1", count)
        elif len(item) % 2 == 0:
            mid = len(item) // 2
            l = int(item[:mid])
            r = int(item[mid:])
            append_dict(str(l), count)
            append_dict(str(r), count)
        else:
            append_dict(str(int(item) * 2024), count)

    values = new_values
    # print(values)
    if index == 25:
        answer_part_one(sum(values.values()))

# Print the answers here
# ==========================================================================
answer_part_two(sum(values.values()))

# End of Code
# ==========================================================================
timer.end_timer()
