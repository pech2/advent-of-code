from collections import deque


def part1(input_):
    empty = deque()

    disk = []

    space = False
    id = 0
    for blocks in input_:
        block_value = id
        if space:
            block_value = "."
        for _ in range(int(blocks)):
            if space:
                empty.append(len(disk))
            disk.append(block_value)
        if not space:
            id += 1
        space = not space

    while empty:
        index = empty.popleft()
        while disk and disk[-1] == ".":
            disk.pop()
        if index >= len(disk):
            break
        disk[index] = disk.pop()

    count = 0
    for i, block in enumerate(disk):
        if block == ".":
            break
        count += i * block

    return count


def part2(input_):
    empty = deque()

    disk = []

    space = False
    id = 0
    for blocks in input_:
        block_value = id
        if space:
            block_value = "."
        for _ in range(int(blocks)):
            if space:
                empty.append(len(disk))
            disk.append(block_value)
        if not space:
            id += 1
        space = not space

    left_space = 0
    right_block = len(disk) - 1

    while right_block >= 0:
        while right_block >= 0 and disk[right_block] == ".":
            right_block -= 1
        left_block = right_block
        while left_block >= 0 and disk[left_block - 1] == disk[right_block]:
            left_block -= 1
        left_space = 0

        while left_space < left_block:
            while left_space < left_block and disk[left_space] != ".":
                left_space += 1
            if left_space >= left_block:
                break
            right_space = left_space
            while right_space < left_block and disk[right_space + 1] == ".":
                right_space += 1
            if right_space - left_space >= right_block - left_block:
                for i in range(left_block, right_block + 1):
                    disk[left_space], disk[left_block] = disk[left_block], "."
                    left_space += 1
                    left_block += 1
                break

            left_space = right_space + 1
        right_block = left_block - 1

    count = 0
    for i, block in enumerate(disk):
        if block == ".":
            continue
        count += i * block

    return count


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip()

    return input_


def main():
    input_ = load_file("day.input")

    test = """2333133121414131402"""
    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
