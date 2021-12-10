from copy import deepcopy

f = open("input9.txt")
all_data = [line for line in f.read().strip().split("\n")]
count = 0

for x in range(len(all_data)):
    for y in range(len(all_data[0])):
        for i in [-1, 1]:
            if x + i >= 0:
                if x + i < len(all_data):
                    if all_data[x][y] >= all_data[x + i][y]:
                        break
            if y + i >= 0:
                if y + i < len(all_data[0]):
                    if all_data[x][y] >= all_data[x][y + i]:
                        break
        else:
            count += 1 + int(all_data[x][y])


def flow(map, fluid):
    for x in range(len(map)):
        for y in range(len(map[0])):
            for i in [-1, 1]:
                if x + i >= 0 and x + i < len(map):
                    if map[x + i][y] < map[x][y]:
                        fluid[x + i][y] += fluid[x][y]
                        fluid[x][y] = 0
                        break
                if y + i >= 0 and y + i < len(map[0]):
                    if map[x][y + i] < map[x][y]:
                        fluid[x][y + i] += fluid[x][y]
                        fluid[x][y] = 0
                        break
    return fluid


def flat(t):
    return [x for y in t for x in y]


def part2(map):
    fluid = [[1] * len(map[0]) for _ in range(len(map))]
    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "9":
                fluid[x][y] = 0
    while True:
        new_fluid = flow(map, deepcopy(fluid))
        if all([x1 == x2 for x1, x2 in zip(flat(fluid), flat(new_fluid))]):
            break
        fluid = new_fluid
    sizes = [x for y in fluid for x in y]
    sizes.sort(reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


print(count)
print(part2(all_data))
