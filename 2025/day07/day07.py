from functools import cache


def part1(text):
    beams = ["." for _ in range(len(text[0]))]
    count = 0
    for line in text:
        new_beams = ["." for _ in range(len(text[0]))]
        for i, (beam, pos) in enumerate(zip(beams, line)):
            if beam == "S" and pos == "^":
                count += 1
                new_beams[i - 1] = "S"
                new_beams[i + 1] = "S"
            elif beam == "S" or pos == "S":
                new_beams[i] = "S"
        beams = new_beams

    return count


def part2(text):
    beams = []
    for c in text[0]:
        if c == "S":
            beams.append(1)
        else:
            beams.append(0)

    for line in text[1:]:
        new_beams = [0 for _ in range(len(text[0]))]
        for i, (beam, pos) in enumerate(zip(beams, line)):
            if beam > 0 and pos == "^":
                new_beams[i - 1] += beams[i]
                new_beams[i + 1] += beams[i]
            elif beam > 0:
                new_beams[i] += beams[i]

        beams = new_beams

    return sum(beams)


def read():
    text = []
    with open("text") as f:
        for line in f:
            text.append(line)
    return text


if __name__ == "__main__":
    text = read()
    example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
    example = example.split("\n")

    out = part1(example)
    print("part 1 example", out)
    out = part1(text)
    print("part 1", out)

    out = part2(example)
    print("part 2 example", out)
    out = part2(text)
    print("part 2", out)
