digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def lowest_index(line):
    max_index = float("inf")
    max_num = ""
    for digit, val in digits.items():
        index = line.find(digit)
        if index != -1 and max_index > index:
            max_num = val
            max_index = index
    return max_num


def highest_index(line):
    max_index = float("-inf")
    max_num = ""
    for digit, val in digits.items():
        index = line.rfind(digit)
        if index != -1 and max_index < index:
            max_num = val
            max_index = index
    return max_num


def star1():
    with open("day01.input") as lines:
        nums = 0
        for line in lines:
            line = [c for c in line if c.isdigit()]
            nums += int(line[0] + line[-1])

    print(nums)


def star2():
    with open("day01.input") as lines:
        nums = 0
        for line in lines:
            nums += int(lowest_index(line) + highest_index(line))

        print(nums)


if __name__ == "__main__":
    star1()
    star2()
