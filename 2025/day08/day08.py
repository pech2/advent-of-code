def part1(text):
    max_area = 0
    points = []

    for line in text:
        x, y = line.split(",")
        x = int(x)
        y = int(y)
        for px, py in points:
            width = abs(px - x) + 1
            height = abs(py - y) + 1
            max_area = max(max_area, width * height)
        points.append((x, y))
    return max_area


def part2(text):
    max_area = 0
    points = []
    row_min = {}
    row_max = {}
    prev_y = int(text[0].split(",")[1])

    for line in text:
        x, y = line.split(",")
        x = int(x)
        y = int(y)

        if y not in row_min:
            row_min[y] = x
        if y not in row_max:
            row_max[y] = x
        row_min[y] = min(row_min[y], x)
        row_max[y] = max(row_max[y], x)

        up = min(y, prev_y)
        down = max(y, prev_y)

        for i in range(up, down):
            if i not in row_min:
                row_min[i] = x
            if i not in row_max:
                row_max[i] = x
            row_min[i] = min(row_min[i], x)
            row_max[i] = max(row_max[i], x)

        prev_y = y
        points.append((x, y))

    for i in range(len(points)):
        x, y = points[i]
        for j in range(i + 1, len(points)):
            px, py = points[j]

            width = abs(px - x) + 1
            height = abs(py - y) + 1
            area = width * height

            up = min(y, py)
            down = max(y, py)
            left = min(x, px)
            right = max(x, px)

            for row in range(up, down + 1):
                if row not in row_min:
                    area = 0
                    break
                if left < row_min[row] or right > row_max[row]:
                    area = 0
                    break

            max_area = max(max_area, area)
    return max_area


def read():
    text = []
    with open("text") as f:
        for line in f:
            text.append(line)
    return text


if __name__ == "__main__":
    text = read()
    example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
    example = example.split("\n")

    out = part1(example)
    print("part 1 example", out)
    out = part1(text)
    print("part 1", out)

    out = part2(example)
    print("part 2 example", out)
    out = part2(text)
    print("part 2", out)
