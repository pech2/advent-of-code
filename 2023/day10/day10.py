def valid_move(grid, row, col):
    moves = []

    if row - 1 >= 0 and grid[row][col] in "|LJS" and grid[row - 1][col] in "|7F":
        moves.append((row - 1, col))
    if row + 1 < len(grid) and grid[row][col] in "|7FS" and grid[row + 1][col] in "|LJ":
        moves.append((row + 1, col))
    if col - 1 >= 0 and grid[row][col] in "-J7S" and grid[row][col - 1] in "-LF":
        moves.append((row, col - 1))
    if (
        col + 1 < len(grid[0])
        and grid[row][col] in "-LFS"
        and grid[row][col + 1] in "-J7"
    ):
        moves.append((row, col + 1))
    return moves


def part1(f):
    grid = []
    for line in f:
        grid.append(line.strip())
    start_row = start_col = 0
    for row, line in enumerate(grid):
        col = line.find("S")
        if col != -1:
            start_row = row
            start_col = col
            break

    distances = {}
    length = 0
    neighbors = [(start_row, start_col)]
    while neighbors:
        new_neighbors = []
        for neighbor in neighbors:
            if neighbor in distances:
                continue
            distances[neighbor] = length

            for n in valid_move(grid, neighbor[0], neighbor[1]):
                if n in distances:
                    continue
                new_neighbors.append(n)
        length += 1
        neighbors = new_neighbors

    return max(distances.values())


def part2(f):
    pass


def main():
    filename = "day10.example"
    filename = "day.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
