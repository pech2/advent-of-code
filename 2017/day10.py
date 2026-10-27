def part1(input):
    input = [int(x) for x in input.split(",")]
    arr = [int(x) for x in range(256)]
    pos = 0
    skip = 0

    for x in input:
        left = pos
        right = (pos + x - 1) % len(arr)
        for _ in range(x // 2):
            arr[left], arr[right] = arr[right], arr[left]
            left = (left + 1) % len(arr)
            right = (right - 1) % len(arr)

        pos += x + skip
        pos %= len(arr)
        skip += 1

    return arr[0] * arr[1]


def part2(input):
    suffix = [17, 31, 73, 47, 23]
    input = [ord(x) for x in input] + suffix
    arr = [int(x) for x in range(256)]
    pos = 0
    skip = 0

    for _ in range(64):
        for x in input:
            left = pos
            right = (pos + x - 1) % len(arr)
            for _ in range(x // 2):
                arr[left], arr[right] = arr[right], arr[left]
                left = (left + 1) % len(arr)
                right = (right - 1) % len(arr)

            pos += x + skip
            pos %= len(arr)
            skip += 1

    dense_hash = []
    for i in range(16):
        dense = 0
        for j in range(16):
            dense ^= arr[i * 16 + j]
        dense_hash.append(hex(dense)[2:].zfill(2))

    return "".join(dense_hash)


input = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"

print(part1(input))
print("part2", part2("1,2,4"))
print("part2", part2("102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"))
