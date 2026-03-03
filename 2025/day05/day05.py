from functools import cache

def process(text):
    pass

def part1(text):
    ranges = []
    count = 0

    for line in text:
        if "-" in line:
            left, right = line.split("-")
            ranges.append([int(left), int(right)])
        elif line == "":
            continue
        else:
            for left, right in ranges:
                if left <= int(line) <= right:
                    count += 1
                    break
    return count


def part2(text):
    ranges = []
    count = 0
    for line in text:
        if "-" in line:
            left, right = line.split("-")
            ranges.append([int(left), int(right)])
        if line == "":
            break
    ranges.sort()
    merged = [ranges[0]]
    for left, right in ranges[1:]:
        prev_left, prev_right = merged[-1]
        if prev_left <= left <= prev_right:
            merged.pop()
            merged.append([prev_left, max(prev_right, right)])
        else:
            merged.append([left,right])
    count = 0

    for left, right in merged:
        count += right-left+1
    return count

def read():
    text = []
    with open("text") as f:
        for line in f:
            text.append(line.strip())
    return text


if __name__ == "__main__":
    text = read()
    example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
    example = example.split("\n")

    out = part1(example)
    print("part 1 example", out)
    out = part1(text)
    print("part 1", out)

    out = part2(example)
    print("part 2 example", out)
    out = part2(text)
    print("part 2", out)
