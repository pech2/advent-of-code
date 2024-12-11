from collections import defaultdict


def solve(input_, blinks=6):
    nums = input_.split()
    c = defaultdict(int)
    for num in nums:
        c[num] += 1

    for _ in range(blinks):
        d2 = defaultdict(int)
        for k, v in c.items():
            num = str(int(k))
            if int(num) == 0:
                d2["1"] += v
            elif len(num) % 2 == 0:
                d2[num[: len(num) // 2]] += v
                d2[num[len(num) // 2 :]] += v
            else:
                d2[str(int(num) * 2024)] += v
        c = d2

    return sum(c.values())


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")[0]
    test = "125 17"
    print(solve(input_, 25))

    print(solve(input_, 75))


if __name__ == "__main__":
    main()
