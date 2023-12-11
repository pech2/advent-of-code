def part1(f):
    grid = []
    for line in f:
        grid.append(line.strip())
    rows = set()
    cols = set()
    for i, row in enumerate(grid):
        if all(cell == "." for cell in row):
            rows.add(i)
    for i, col in enumerate(zip(*grid)):
        if all(cell == "." for cell in col):
            cols.add(i)

    galaxies = []
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == "#":
                galaxies.append((row, col))

    total = 0

    for i, galaxy in enumerate(galaxies):
        for pair in galaxies[i + 1 :]:
            distance = 0
            row_a, row_b = galaxy[0], pair[0]
            if row_a > row_b:
                row_a, row_b = row_b, row_a
            while row_a < row_b:
                distance += 1
                row_a += 1
                if row_a in rows:
                    distance += 1

            col_a, col_b = galaxy[1], pair[1]
            if col_a > col_b:
                col_a, col_b = col_b, col_a
            while col_a < col_b:
                distance += 1
                col_a += 1
                if col_a in cols:
                    distance += 1

            total += distance
    return total


def part2(f):
    grid = []
    for line in f:
        grid.append(line.strip())
    rows = set()
    cols = set()
    for i, row in enumerate(grid):
        if all(cell == "." for cell in row):
            rows.add(i)
    for i, col in enumerate(zip(*grid)):
        if all(cell == "." for cell in col):
            cols.add(i)

    galaxies = []
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == "#":
                galaxies.append((row, col))

    total = 0

    for i, galaxy in enumerate(galaxies):
        for pair in galaxies[i + 1 :]:
            distance = 0
            row_a, row_b = galaxy[0], pair[0]
            if row_a > row_b:
                row_a, row_b = row_b, row_a
            while row_a < row_b:
                distance += 1
                row_a += 1
                if row_a in rows:
                    distance += 999999

            col_a, col_b = galaxy[1], pair[1]
            if col_a > col_b:
                col_a, col_b = col_b, col_a
            while col_a < col_b:
                distance += 1
                col_a += 1
                if col_a in cols:
                    distance += 999999

            total += distance
    return total


def main():
    filename = "day11.example"
    filename = "dayb.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
