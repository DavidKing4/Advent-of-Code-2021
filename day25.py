from copy import deepcopy

f = open("input25.txt")
cucumber = [list(x) for x in f.read().split("\n")[:-1]]


def move_east(cucumber):
    new_cucumber = deepcopy(cucumber)
    for y in range(len(cucumber)):
        for x in range(l := len(cucumber[y])):
            if cucumber[y][x] == ">" and cucumber[y][(x + 1) % l] == ".":
                new_cucumber[y][x] = "."
                new_cucumber[y][(x + 1) % l] = ">"
    return new_cucumber


def move_south(cucumber):
    new_cucumber = deepcopy(cucumber)
    for y in range(l := len(cucumber)):
        for x in range(len(cucumber[y])):
            if cucumber[y][x] == "v" and cucumber[(y + 1) % l][x] == ".":
                new_cucumber[y][x] = "."
                new_cucumber[(y + 1) % l][x] = "v"
    return new_cucumber


def part1(cucumber):
    c = 0
    while True:
        old_cucumber = deepcopy(cucumber)
        cucumber = move_east(cucumber)
        cucumber = move_south(cucumber)
        # for line in cucumber:
        #     print(line)
        # print()
        # for line in old_cucumber:
        #     print(line)
        c += 1
        if all(
            [
                x1 == x2
                for y1, y2 in zip(cucumber, old_cucumber)
                for x1, x2 in zip(y1, y2)
            ]
        ):
            return c


print(part1(cucumber))
