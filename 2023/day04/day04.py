from collections import defaultdict


def count_wins(line):
    winning_nums, nums = line.split(":")[1].split("|")
    winning_nums = set(
        int(x) for x in winning_nums.strip().split(" ") if x.strip() != ""
    )
    nums = nums.strip().split(" ")
    wins = 0
    for num in nums:
        num = num.strip()
        if num and int(num) in winning_nums:
            wins += 1
    return wins


def part1(f):
    score = 0

    for line in f:
        wins = count_wins(line)
        if wins == 0:
            continue
        score += 2 ** (wins - 1)
    return score


def part2(f):
    cards = defaultdict(lambda: 1)

    for i, card in enumerate(f, 1):
        wins = count_wins(card)

        cards[i] = cards[i]
        for copys in range(i + 1, i + 1 + wins):
            cards[copys] += cards[i]

    return sum(cards.values())


def main():
    filename = "day04.example"
    # filename = "day04.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
