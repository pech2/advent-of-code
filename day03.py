def check(grid, row, col):
    for x in range(-1, 2):
        for y in range(-1, 2):
            new_row = x + row
            new_col = y + col
            if (
                new_row < 0
                or new_row >= len(grid)
                or new_col < 0
                or new_col >= len(grid[0])
            ):
                continue
            if not grid[new_row][new_col].isdigit() and grid[new_row][new_col] != ".":
                return True
    return False


def part1(f):
    grid = [line.strip() for line in f]
    parts = 0
    for row, line in enumerate(grid):
        valid = False
        num = 0
        for col, c in enumerate(line):
            if not c.isdigit():
                if valid:
                    parts += num
                valid = False
                num = 0
                continue
            if not valid:
                valid = check(grid, row, col)
            num = num * 10 + int(grid[row][col])
        if valid:
            parts += num
    return parts


def check_two(grid, row, col):
    one = False
    for x in range(-1, 2):
        for y in range(-1, 2):
            new_row = x + row
            new_col = y + col
            if (
                new_row < 0
                or new_row >= len(grid)
                or new_col < 0
                or new_col >= len(grid[0])
            ):
                continue
            if not grid[new_row][new_col].isdigit():
                continue
            if not one:
                one = True
            else:
                if y == 0:
                    return True
                elif grid[new_row][new_col - 1].isdigit():
                    continue
                else:
                    return True
    return False


def get_slice(grid, row, col):
    pass


def find_two(grid, row, col):
    slices = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            new_row = x + row
            new_col = y + col
            if (
                new_row < 0
                or new_row >= len(grid)
                or new_col < 0
                or new_col >= len(grid[0])
                or not grid[new_row][new_col].isdigit()
            ):
                continue
            left = right = new_col
            while left - 1 >= 0 and grid[new_row][left - 1].isdigit():
                left -= 1
            while right + 1 < len(grid[0]) and grid[new_row][right + 1].isdigit():
                right += 1
            slices.add((new_row, left, right))
    if len(slices) == 2:
        slice1 = slices.pop()
        slice2 = slices.pop()
        return int(grid[slice1[0]][slice1[1] : slice1[2] + 1]) * int(
            grid[slice2[0]][slice2[1] : slice2[2] + 1]
        )
    return 0


def part2(f):
    grid = [line.strip() for line in f]
    parts = 0
    for row, line in enumerate(grid):
        for col, c in enumerate(line):
            if c == "*":
                parts += find_two(grid, row, col)
    return parts


def main():
    filename = "day03.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
