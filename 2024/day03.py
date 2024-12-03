import re


def part1(input_):
    sum_ = 0
    pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)")
    for match_ in pattern.finditer(input_):
        sum_ += int(match_.group(1)) * int(match_.group(2))
    return sum_


def part2(input_):
    sum_ = 0
    do_ = True
    pattern = re.compile(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)|(do\(\))|(don't\(\))")
    for match_ in pattern.finditer(input_):
        if not match_.group(3) and not match_.group(4) and do_:
            sum_ += int(match_.group(1)) * int(match_.group(2))
        elif match_.group(3):
            do_ = True
        elif match_.group(4):
            do_ = False
    return sum_


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip()

    return input_


def main():
    input_ = load_file("day.input")
    test_input = (
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    )

    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
