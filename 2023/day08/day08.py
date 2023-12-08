from itertools import cycle


def part1(f):
    instructions = cycle(f.readline().strip())
    f.readline()
    steps = 0
    nodes = {}

    for line in f:
        node, branches = line.split("=")
        left, right = branches.strip()[1:-1].split(",")
        nodes[node.strip()] = (left.strip(), right.strip())

    cur = "AAA"
    for direction in instructions:
        if cur == "ZZZ":
            return steps
        steps += 1
        if direction == "L":
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
    return steps


def part2(f):
    instructions = [0 if c == "L" else 1 for c in f.readline().strip()]
    f.readline()
    nodes = {}
    positions = []

    for line in f:
        node, branches = line.split("=")
        left, right = branches.strip()[1:-1].split(",")
        node = node.strip()

        if node[-1] == "A":
            positions.append(node)
        nodes[node.strip()] = (left.strip(), right.strip())

    step_lengths = []

    for position in positions:
        steps = 0

        for direction in cycle(instructions):
            if position[-1] == "Z":
                step_lengths.append(steps)
                break
            position = nodes[position][direction]
            steps += 1

    num = step_lengths.pop()
    while step_lengths:
        num = least_common_multiple(num, step_lengths.pop())
    return num


def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    return a * b // greatest_common_divisor(a, b)


def main():
    filename = "day08.example"
    filename = "day08.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
