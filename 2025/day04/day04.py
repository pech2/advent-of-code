from functools import cache


def part1(text):
    count = 0
    for i in range(1, len(text) - 1):
        for j in range(1, len(text[0]) - 1):
            if text[i][j] != "@":
                continue
            valid = count_neighbors(text, i, j)
            if valid:
                count += 1
    return count


def part2(text):
    count = 0
    new_text = []
    while True:
        new_text = ["." * len(text[0])]
        for i in range(1, len(text) - 1):
            new_line = ["."]
            for j in range(1, len(text[0]) - 1):
                if text[i][j] != "@":
                    new_line.append(text[i][j])
                    continue
                valid = count_neighbors(text, i, j)
                if valid:
                    count += 1
                    new_line.append(".")
                else:
                    new_line.append("@")
            new_line.append(".")
            new_text.append("".join(new_line))
        new_text.append("." * len(text[0]))

        change = False

        for line1, line2 in zip(text, new_text):
            if line1 != line2:
                change = True
        if not change:
            return count
        text = new_text


def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            count += grid[x + i][y + j] == "@"
    return count < 4


def process_input(text):
    length = len(text[0]) + 2
    out = ["." * length]
    for line in text:
        out.append("." + line + ".")
    out.append("." * length)
    return out


def read():
    text = []
    with open("text") as f:
        for line in f:
            text.append(line.strip())
    return text


if __name__ == "__main__":
    text = read()
    example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    example = example.split("\n")
    example = process_input(example)
    print(example)
    out = part1(example)
    print("part 1 example", out)

    text = process_input(text)
    out = part1(text)
    print("part 1", out)

    # 1286
    # 3649

    out = part2(example)
    print("part 2 example", out)
    out = part2(text)
    print("part 2", out)
