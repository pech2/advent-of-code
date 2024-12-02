def dec(row):
    for i in range(1, len(row)):
        if row[i] > row[i - 1] and 1 <= abs(row[i] - row[i - 1]) <= 3:
            continue
        else:
            return False
    return True


def inc(row):
    for i in range(1, len(row)):
        if row[i] < row[i - 1] and 1 <= abs(row[i] - row[i - 1]) <= 3:
            continue
        else:
            return False
    return True


def part1(input_):
    count = 0

    for report in input_:
        report = [int(x) for x in report.split()]
        if dec(report) or inc(report):
            count += 1

    return count


def part2(input_):
    count = 0

    for report in input_:
        report = [int(x) for x in report.split()]
        if dec(report) or inc(report):
            count += 1
        else:
            for i in range(len(report)):
                if dec(report[:i] + report[i + 1 :]) or inc(
                    report[:i] + report[i + 1 :]
                ):
                    count += 1
                    break

    return count


def load_file(filename):
    input_ = []
    with open(filename) as f:
        for line in f:
            input_.append(line)
    return input_


def main():
    input = load_file("day.input")

    #     input = """7 6 4 2 1
    # 1 2 7 8 9
    # 9 7 6 2 1
    # 1 3 2 4 5
    # 8 6 4 4 1
    # 1 3 6 7 9"""
    #     input = input.split("\n")

    print(part1(input))

    print(part2(input))


if __name__ == "__main__":
    main()
