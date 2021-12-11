from copy import deepcopy

f = open("input11.txt")
data = [line for line in f.read().split("\n")[:-1]]
octopi = [[0] * len(data[0]) for _ in range(len(data))]

for i in range(len(data)):
    for j in range(len(data[0])):
        octopi[i][j] = int(data[i][j])


def take_step(octopi, count, first_step):
    directions = [(1, 0), (1, 1), (-1, 0), (-1, 1), (0, 1), (1, -1), (0, -1), (-1, -1)]
    nines = [[False] * len(octopi[0]) for _ in range(len(octopi))]
    for x in range(len(octopi)):
        for y in range(len(octopi)):
            if octopi[x][y] != -1 and first_step:
                octopi[x][y] += 1
            if octopi[x][y] > 9:
                nines[x][y] = True
    for x in range(len(nines)):
        for y in range(len(nines[0])):
            if nines[x][y]:
                for d in directions:
                    if x + d[0] < len(octopi) and 0 <= x + d[0]:
                        if y + d[1] < len(octopi[0]) and 0 <= y + d[1]:
                            if octopi[x + d[0]][y + d[1]] != -1:
                                octopi[x + d[0]][y + d[1]] += 1
                count += 1
                octopi[x][y] = -1
    if any([x > 9 for y in octopi for x in y]):
        return take_step(deepcopy(octopi), count, False)
    else:
        return octopi, count


def part1(octopi, steps):
    count = 0
    for _ in range(steps):
        octopi, t = take_step(deepcopy(octopi), 0, True)
        count += t
        for x in range(len(octopi)):
            for y in range(len(octopi)):
                if octopi[x][y] == -1:
                    octopi[x][y] = 0
    return count


def part2(octopi):
    step = 0
    while True:
        octopi, _ = take_step(deepcopy(octopi), 0, True)
        step += 1
        if sum([x for y in octopi for x in y]) == (-1 * len(octopi) * len(octopi[0])):
            return step
        for x in range(len(octopi)):
            for y in range(len(octopi)):
                if octopi[x][y] == -1:
                    octopi[x][y] = 0


print(part1(deepcopy(octopi), 100))
print(part2(deepcopy(octopi)))
