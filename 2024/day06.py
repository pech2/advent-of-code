from itertools import cycle


def in_grid(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    return True


def part1(input_):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    directions = cycle(directions)
    direction = next(directions)
    guard = (0, 0)
    grid = input_
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                guard = (i, j)
                break

    count = 0
    path = set()

    while in_grid(grid, guard[0], guard[1]):
        dr, dc = direction
        gr, gc = guard

        path.add((gr, gc))

        if not in_grid(grid, gr + dr, gc + dc):
            break
        if grid[gr + dr][gc + dc] == "#":
            direction = next(directions)
        else:
            guard = (gr + dr, gc + dc)

    return len(path)


def get_path(input_):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    directions = cycle(directions)
    direction = next(directions)
    guard = (0, 0)
    grid = input_
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                guard = (i, j)
                break

    count = 0
    path = set()

    while in_grid(grid, guard[0], guard[1]):
        dr, dc = direction
        gr, gc = guard

        path.add((gr, gc))

        if not in_grid(grid, gr + dr, gc + dc):
            break
        if grid[gr + dr][gc + dc] == "#":
            direction = next(directions)
        else:
            guard = (gr + dr, gc + dc)

    return path


def is_loop(input_, block):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    directions = cycle(directions)
    direction = next(directions)
    guard = (0, 0)
    grid = input_
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                guard = (i, j)
                break

    count = 0
    path = set()
    visited = set()

    while in_grid(grid, guard[0], guard[1]):
        dr, dc = direction
        gr, gc = guard

        path.add((gr, gc))
        visit = (gr, gc, dr, dc)
        if visit in visited:
            return True
        visited.add(visit)

        if not in_grid(grid, gr + dr, gc + dc):
            break
        if grid[gr + dr][gc + dc] == "#":
            direction = next(directions)
        elif gr + dr == block[0] and gc + dc == block[1]:
            direction = next(directions)
        else:
            guard = (gr + dr, gc + dc)

    return False


def part2(input_):
    path = get_path(input_)
    return sum(is_loop(input_, block) for block in path)


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")
    test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".strip().split(
        "\n"
    )

    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
