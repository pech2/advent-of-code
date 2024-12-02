def part1(input_):
    pass


def part2(input_):
    pass


def load_file(filename):
    with open("filename") as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")

    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
