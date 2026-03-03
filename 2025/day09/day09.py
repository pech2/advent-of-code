from collections import defaultdict, deque
from functools import cache

def part1(text):
    machines = [parse_line(line) for line in text]
    count = 0

    for machine in machines:
        final_state, buttons, _ = machine
        if all([c == "." for c in final_state]):
            continue

        final_state = "".join(final_state)
        state = deque([[["." for _ in range(len(final_state))], 1]])

        while state:
            old_state, machine_count = state.popleft()

            for button in buttons:
                new_state = old_state[:]
                for num in button:
                    if new_state[num] == ".":
                        new_state[num] = "#"
                    else:
                        new_state[num] = "."

                if "".join(new_state) == final_state:
                    count += machine_count
                    state = None
                    break
                state.append([new_state, machine_count +1])            

    return count


def part2(text):
    machines = [parse_line(line) for line in text]
    count = 0

    for machine in machines:
        _, buttons, final_state = machine
        final_state = tuple(final_state)
        if sum(final_state) == 0:
            continue
        
        state = deque([[[0 for _ in range(len(final_state))], 0]])
        visited = set()

        while state:
            old_state, machine_count = state.popleft()
            machine_count += 1

            for button in buttons:
                new_state = list(old_state)

                for num in button:
                    new_state[num]+=1
                new_state = tuple(new_state)
                if new_state == final_state:
                    count += machine_count
                    state = None
                    break
                valid = True
                for i, j in zip(new_state, final_state):
                    if i > j:
                        valid = False
                        break

                if valid and new_state not in visited:
                    visited.add(new_state)
                    state.append([new_state, machine_count])
    return count


def read():
    text = []
    with open("text") as f:
        for line in f:
            text.append(line)
    return text

def parse_line(line):
    lights = []
    buttons = []
    joltages = []

    i = 0
    while i < len(line):
        if line[i] == "[":
            j = i
            while j < len(line) and line[j+1] !="]":
                j += 1
                lights.append(line[j])
            i = j+1
        elif line[i] == "(":
            j = i
            while j < len(line) and line[j] != ")":
                j += 1
            wiring = line[i+1:j]
            buttons.append([int(x) for x in wiring.split(",")])
            i = j+1
        elif line[i] == "{":
            j = i
            while j < len(line) and line[j] != "}":
                j += 1
            joltage = line[i+1:j]
            joltages.append([int(x) for x in joltage.split(",")])
            i = j+1
        else:
            i += 1
    return [lights, buttons, joltages[0]]

if __name__ == "__main__":
    text = read()
    example = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""
    example = example.split("\n")

    # out = part1(example)
    # print("part 1 example", out)
    # out = part1(text)
    # print("part 1", out)

    out = part2(example)
    print("part 2 example", out)
    out = part2(text)
    print("part 2", out)
