from functools import cache

def part1(text):
    count = 0
    width = len(text[0].strip().split())

    cols = [[] for _ in range(width)]

    for i, line in enumerate(text[:-1]):
        nums = line.strip().split()
        for j, num in enumerate(nums):
            cols[j].append(num)

    for i, sign in enumerate(text[-1].strip().split()):
        col_count = int(cols[i][0])
        if sign == "*":
            for num in cols[i][1:]:
                col_count *= int(num)
        else:
            for num in cols[i][1:]:
                col_count += int(num)
        
        count += col_count
    return count


def part2(text):
    count = 0
    cols = []
    new_col = []

    for i in range(len(text[0])):
        num = []
        for j in range(len(text)-1):
            num.append(text[j][i])
        

        if not ''.join(num).strip().isnumeric():
            cols.append(new_col)
            new_col = []
        else:
            num = int(''.join(num))
            new_col.append(num)    
    cols.append(new_col)

    for i, sign in enumerate(text[-1].strip().split()):
        col_count = cols[i][0]
        if sign == "*":
            for num in cols[i][1:]:
                col_count *= int(num)
        else:
            for num in cols[i][1:]:
                col_count += int(num)
        
        count += col_count
    return count

def read():
    text = []
    with open("text") as f:
        for line in f:
            text.append(line)
    return text


if __name__ == "__main__":
    text = read()
    example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """
    example = example.split("\n")

    out = part1(example)
    print("part 1 example", out)
    out = part1(text)
    print("part 1", out)

    out = part2(example)
    print("part 2 example", out)
    out = part2(text)
    print("part 2", out)
