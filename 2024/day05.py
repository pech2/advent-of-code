from collections import defaultdict


def part1(input_):
    graph = defaultdict(set)

    count = 0
    for line in input_:
        if "|" in line:
            parent, child = line.split("|")
            parent = int(parent)
            child = int(child)
            graph[child].add(parent)
        if "," in line:
            nums = [int(x) for x in line.split(",")]

            prereq = set()
            valid = True
            for num in nums:
                if num in prereq:
                    valid = False
                    break

                prereq |= graph[num]

            if valid:
                count += nums[len(nums) // 2]

    return count


def part2(input_):
    graph = defaultdict(set)
    reverse_graph = defaultdict(set)
    count = 0
    for line in input_:
        if "|" in line:
            parent, child = line.split("|")
            parent = int(parent)
            child = int(child)
            graph[child].add(parent)
            reverse_graph[parent].add(child)
        if "," in line:
            nums = [int(x) for x in line.split(",")]

            prereq = set()
            valid = True
            for num in nums:
                if num in prereq:
                    valid = False
                    break
                prereq |= graph[num]
            if not valid:
                degrees = defaultdict(int)

                for num in nums:
                    degrees[num] = sum(1 for x in graph[num] if x in nums)
                    print(num, [x for x in graph[num] if x in nums])

                zeroes = [num for num, count in degrees.items() if count == 0]

                order = []

                while zeroes:
                    node = zeroes.pop()
                    order.append(node)
                    for child in reverse_graph[node]:
                        if child not in nums:
                            continue
                        degrees[child] -= 1
                        if degrees[child] == 0:
                            zeroes.append(child)

                count += order[len(order) // 2]

    return count


def load_file(filename):
    with open(filename) as f:
        input_ = f.read().strip().split("\n")

    return input_


def main():
    input_ = load_file("day.input")
    test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip().split(
        "\n"
    )

    print(part1(input_))

    print(part2(input_))


if __name__ == "__main__":
    main()
