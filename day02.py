RED = 12
GREEN = 13
BLUE = 14


def valid_game(line):
    games = line.split(":")[1].split(";")

    for game in games:
        for hand in game.split(","):
            hand = hand.strip()
            if "red" in hand:
                if int(hand.split(" ")[0]) > RED:
                    return False
            if "green" in hand:
                if int(hand.split(" ")[0]) > GREEN:
                    return False
            if "blue" in hand:
                if int(hand.split(" ")[0]) > BLUE:
                    return False
    return True


def part1(f):
    games = 0
    for i, line in enumerate(f, start=1):
        if valid_game(line):
            games += i
    return games


def power_game(line):
    games = line.split(":")[1].split(";")
    red = 0
    blue = 0
    green = 0
    for game in games:
        for hand in game.split(","):
            hand = hand.strip()
            if "red" in hand:
                red = max(red, int(hand.split(" ")[0]))
            if "green" in hand:
                green = max(green, int(hand.split(" ")[0]))
            if "blue" in hand:
                blue = max(blue, int(hand.split(" ")[0]))
    return red * green * blue


def part2(f):
    power = 0
    for line in f:
        power += power_game(line)
    return power


def main():
    with open("day02.txt") as f:
        print(part1(f))
    with open("day02.txt") as f:
        print(part2(f))


if __name__ == "__main__":
    main()
