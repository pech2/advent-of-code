from collections import defaultdict


def part1(f):
    left = []
    right = []
    for line in f:
        line_split = line.split()
        if len(line_split) != 2:
            continue
        left.append(line_split[0])
        right.append(line_split[1])
    left.sort()
    right.sort()

    distance = 0
    for l, r in zip(left, right):
        distance += abs(int(l) - int(r))

    return distance


def part2(f):
    left = defaultdict(int)
    right = defaultdict(int)

    for line in f:
        line_split = line.split()
        if len(line_split) != 2:
            continue
        left[int(line_split[0])] += 1
        right[int(line_split[1])] += 1

    similarity = 0
    for num in left.keys():
        similarity += num * left[num] * right[num]

    return similarity


def main():
    filename = "day01.input"
    # filename = "dayb.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
