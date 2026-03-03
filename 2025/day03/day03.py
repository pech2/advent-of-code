from functools import cache

def part1(text):
    count = 0
    
    for line in text:
        
        max_ = line[:2]
        for i, j in enumerate(line[:-1]):
            max_ = max(max_, j + max(line[i+1:]))
        count += int(max_)
    return count

def part2(text):
    count = 0
    for line in text:
        count += int(r(line, 12))
    return count


@cache
def r(line, count):
    if not line or count == 0: return ""
    if len(line) < count: return ""

    max_ = "0" * count
    for i in range(len(line)):
        num = line[i] + r(line[i+1:], count-1)
        if int(max_) < int(num) and len(num) == count:
            max_ = num
    return max_

def read():
    text = []
    with open("text") as f:
        for line in f:
            text.append(line.strip())
    return text

if __name__ == "__main__":
    text = read()
    example = """987654321111111
811111111111119
234234234234278
818181911112111"""

    example = example.split("\n")

    out = part1(example)
    print("part 1 example", out)
    out = part1(text)
    print("part 1", out)

    out = part2(example)
    print("part 2 example", out)
    out = part2(text)
    print("part 2", out)