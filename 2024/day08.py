from collections import defaultdict


def part1(input_):
    ant = defaultdict(list)

    for row in range(len(input_)):
        for col in range(len(input_[0])):
            if input_[row][col] == ".":
                continue
            ant[input_[row][col]].append((row, col))

    locations = set()
    for v in ant.values():
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                l, r = i, j
                if v[r][1] < v[l][1]:
                    r, l = l, r
                x = v[r][0] - v[l][0]
                y = v[r][1] - v[l][1]

                anti1 = (v[l][0] - x, v[l][1] - y)
                anti2 = (v[r][0] + x, v[r][1] + y)

                if 0 <= anti1[0] < len(input_) and 0 <= anti1[1] < len(input_[0]):
                    locations.add(anti1)

                if 0 <= anti2[0] < len(input_) and 0 <= anti2[1] < len(input_[0]):
                    locations.add(anti2)

    return len(locations)


def part2(input_):
    ant = defaultdict(list)

    for row in range(len(input_)):
        for col in range(len(input_[0])):
            if input_[row][col] == ".":
                continue
            ant[input_[row][col]].append((row, col))

    locations = set()
    for v in ant.values():
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                l, r = i, j
                if v[r][1] < v[l][1]:
                    r, l = l, r
                x = v[r][0] - v[l][0]
                y = v[r][1] - v[l][1]

                tr, tc = v[l][0], v[l][1]
                while 0 <= tr < len(input_) and 0 <= tc < len(input_[0]):
                    locations.add((tr, tc))
                    tc -= y
                    tr -= x

                tr, tc = v[r][0], v[r][1]
                while 0 <= tr < len(input_) and 0 <= tc < len(input_[0]):
                    locations.add((tr, tc))
                    tc += y
                    tr += x

    return len(locations)


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")
    test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".strip().split(
        "\n"
    )

    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
