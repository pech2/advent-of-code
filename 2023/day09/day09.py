def get_differences(nums):
    diffs = []
    for prev, cur in zip(nums, nums[1:]):
        diffs.append(cur - prev)
    return diffs


def part1(f):
    total = 0
    for line in f:
        nums = [int(x) for x in line.split()]
        diffs = get_differences(nums)
        stack = [nums[0]]
        while any(diff != 0 for diff in diffs):
            stack.append(diffs[0])
            diffs = get_differences(diffs)

        line_sum = 0
        while stack:
            line_sum = stack.pop() - line_sum
        total += line_sum
    return total


def part2(f):
    pass


def main():
    filename = "day.example"
    filename = "dayb.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
