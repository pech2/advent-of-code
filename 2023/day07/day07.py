strengths = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
strengths2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def part1(f):
    row_rank_bid = []
    for i, row in enumerate(f):
        hand, bid_amount = row.split(" ")

        rank = []
        rank.append(sorted([hand.count(x) for x in set(hand)], reverse=True))
        rank.append([len(strengths) - strengths.index(x) for x in hand])
        rank.append(bid_amount)

        row_rank_bid.append(rank)

    row_rank_bid.sort(key=lambda x: (x[0], x[1]))

    total = 0
    for i, (_, _, bid) in enumerate(row_rank_bid, start=1):
        total += i * int(bid)
    return total


def part2(f):
    row_rank_bid = []
    for i, row in enumerate(f):
        hand, bid_amount = row.split(" ")

        rank = []

        wild_hand = [x for x in hand if x != "J"]
        if not wild_hand:
            wild_hand = ["A", "A", "A", "A", "A"]
        while len(wild_hand) < 5:
            wild_hand.append(max(set(wild_hand), key=wild_hand.count))

        rank.append(sorted([wild_hand.count(x) for x in set(wild_hand)], reverse=True))
        rank.append([len(strengths2) - strengths2.index(x) for x in hand])
        rank.append(bid_amount)

        row_rank_bid.append(rank)

    row_rank_bid.sort(key=lambda x: (x[0], x[1]))
    print(row_rank_bid)
    total = 0
    for i, (_, _, bid) in enumerate(row_rank_bid, start=1):
        total += i * int(bid)
    return total


def main():
    filename = "day07.example"
    filename = "day07.input"

    with open(filename) as f:
        print(part1(f))

    with open(filename) as f:
        print(part2(f))


if __name__ == "__main__":
    main()
