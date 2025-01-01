from collections import deque

from modules.advent_of_code import solve
from modules.helpers import dd


# Start coding here
# ==========================================================================
def parse(data):
    gates_input, connections_input = data.split("\n\n")
    gates = {}
    for line in gates_input.splitlines():
        gate, output = line.split(": ")
        gates[gate] = int(output)

    connections = {}
    for line in connections_input.splitlines():
        operation, out = line.split(" -> ")
        left, operation, right = operation.split(" ")
        connections[out] = left, operation, right

    return gates, connections


def evaluate(gates, connections):
    wire_values = gates.copy()

    evaluate_connections = deque(connections.items())
    while evaluate_connections:
        output, (a, ops, b) = evaluate_connections.popleft()
        try:
            match ops:
                case "AND":
                    wire_values[output] = wire_values[a] & wire_values[b]
                case "OR":
                    wire_values[output] = wire_values[a] | wire_values[b]
                case "XOR":
                    wire_values[output] = wire_values[a] ^ wire_values[b]
        except KeyError:
            evaluate_connections.append((output, (a, ops, b)))

    return wire_values


def part_one(data):
    gates, connections = data

    wire_values = evaluate(gates, connections)

    binary_number = "".join(
        [
            str(x[1])
            for x in sorted(
                filter(lambda x: x[0].startswith("z"), wire_values.items()), reverse=True
            )
        ]
    )

    return int(binary_number, 2)


def part_two(data):
    gates, connections = data

    def make_gate(char, num):
        return char + str(num).rjust(2, "0")

    def verify_z(gate, num):
        if gate not in connections:
            return False
        a, operation, b = connections[gate]
        if operation != "XOR":
            return False
        if num == 0:
            return sorted([a, b]) == ["x00", "y00"]
        return (
            verify_intermediate_xor(a, num)
            and verify_carry_bit(b, num)
            or verify_intermediate_xor(b, num)
            and verify_carry_bit(a, num)
        )

    def verify_intermediate_xor(gate, num):
        if gate not in connections:
            return False
        a, operation, b = connections[gate]
        if operation != "XOR":
            return False
        return sorted([a, b]) == [make_gate("x", num), make_gate("y", num)]

    def verify_carry_bit(wire, num):
        if wire not in connections:
            return False
        a, operation, b = connections[wire]
        if num == 1:
            if operation != "AND":
                return False
            return sorted([a, b]) == ["x00", "y00"]
        if operation != "OR":
            return False
        return (
            verify_direct_carry(a, num - 1)
            and verify_recarry(b, num - 1)
            or verify_direct_carry(b, num - 1)
            and verify_recarry(a, num - 1)
        )

    def verify_direct_carry(gate, num):
        if gate not in connections:
            return False
        a, operation, b = connections[gate]
        if operation != "AND":
            return False
        return sorted([a, b]) == [make_gate("x", num), make_gate("y", num)]

    def verify_recarry(gate, number):
        if gate not in connections:
            return False
        a, operation, b = connections[gate]
        if operation != "AND":
            return False
        return (
            verify_intermediate_xor(a, number)
            and verify_carry_bit(b, number)
            or verify_intermediate_xor(b, number)
            and verify_carry_bit(a, number)
        )

    def verify(num):
        return verify_z(make_gate("z", num), num)

    def progress():
        i = 0

        while True:
            if not verify(i):
                break
            i += 1

        return i

    swaps = []

    for _ in range(4):
        baseline = progress()
        connection_a, connection_b = None, None
        for connection_a in connections:
            for connection_b in connections:
                if connection_a == connection_b:
                    continue
                connections[connection_a], connections[connection_b] = (
                    connections[connection_b],
                    connections[connection_a],
                )
                if progress() > baseline:
                    break
                connections[connection_a], connections[connection_b] = (
                    connections[connection_b],
                    connections[connection_a],
                )
            else:
                continue
            break
        swaps += [connection_a, connection_b]

    return ",".join(sorted(swaps))


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
