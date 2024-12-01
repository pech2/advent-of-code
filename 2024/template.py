def part1(input_):
    pass


def part2(input_):
    pass


def load_file(filename):
    input_ = []
    with open(filename) as f:
        for line in f:
            input_.append(line)
    return input_


def main():
    input1 = load_file("day.input")
    input2 = load_file("day.input")

    print(part1(input1))

    print(part2(input2))


if __name__ == "__main__":
    main()
