def search(grid, row, col, height, visited, distinct=True):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return 0
    if grid[row][col] != height:
        return 0
    if height == 9 and (row, col) not in visited:
        if not distinct:
            visited.add((row, col))
        return 1
    return (
        search(grid, row + 1, col, height + 1, visited, distinct)
        + search(grid, row - 1, col, height + 1, visited, distinct)
        + search(grid, row, col + 1, height + 1, visited, distinct)
        + search(grid, row, col - 1, height + 1, visited, distinct)
    )


def part1(input_):
    grid = [[int(x) for x in row] for row in input_]

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                continue
            count += search(grid, row, col, 0, set())
    return count


def part2(input_):
    grid = [[int(x) for x in row] for row in input_]

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                continue
            count += search(grid, row, col, 0, set(), distinct=False)
    return count


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")
    test = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".strip().split(
        "\n"
    )
    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
