WORD = "XMAS"


def in_bounds(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    return True


def part1(input_):
    count = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    for row in range(len(input_)):
        for col in range(len(input_[0])):
            for dr, dc in directions:
                r = row
                c = col
                for letter in "XMAS!":
                    if letter == "!":
                        count += 1
                        break
                    if not in_bounds(input_, r, c):
                        break

                    if letter == input_[r][c]:
                        r += dr
                        c += dc
                    else:
                        break
    return count


def part2(input_):
    count = 0

    for row in range(1, len(input_) - 1):
        for col in range(1, len(input_[0]) - 1):
            if input_[row][col] != "A":
                continue
            elif (
                input_[row - 1][col - 1] == input_[row - 1][col + 1] == "M"
                and input_[row + 1][col - 1] == input_[row + 1][col + 1] == "S"
            ):
                count += 1
            elif (
                input_[row - 1][col + 1] == input_[row + 1][col + 1] == "M"
                and input_[row + 1][col - 1] == input_[row - 1][col - 1] == "S"
            ):
                count += 1
            elif (
                input_[row - 1][col - 1] == input_[row - 1][col + 1] == "S"
                and input_[row + 1][col - 1] == input_[row + 1][col + 1] == "M"
            ):
                count += 1
            elif (
                input_[row - 1][col + 1] == input_[row + 1][col + 1] == "S"
                and input_[row + 1][col - 1] == input_[row - 1][col - 1] == "M"
            ):
                count += 1
    return count


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")

    test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split()

    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
