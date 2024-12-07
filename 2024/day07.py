def r(test, nums):
    if not nums:
        return [0]
    n = nums[0]
    next_nums = r(test, nums[1:])
    return [n + num for num in next_nums if n + num <= test] + [
        n * num for num in next_nums if n * num <= test
    ]


def part1(input_):
    count = 0
    for line in input_:
        value, nums = line.split(":")
        value = int(value)
        nums = [int(x) for x in nums.strip().split(" ")]
        if value in r(value, nums[::-1]):
            count += value

    return count


def r2(test, nums):
    if len(nums) == 1:
        return [nums[0]]
    n = nums[0]
    next_nums = r2(test, nums[1:])
    return (
        [n + num for num in next_nums if n + num <= test]
        + [n * num for num in next_nums if n * num <= test]
        + [
            int(str(num) + str(n))
            for num in next_nums
            if int(str(num) + str(n)) <= test
        ]
    )


def part2(input_):
    count = 0
    for line in input_:
        value, nums = line.split(":")
        value = int(value)
        nums = [int(x) for x in nums.strip().split(" ")]
        if value in r2(value, nums[::-1]):
            count += value

    return count


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")
    test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
        "\n"
    )

    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
