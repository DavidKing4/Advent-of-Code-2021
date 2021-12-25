f = open("input20.txt")
algo, raw_data = f.read().split("\n\n")
data = raw_data.split("\n")[:-1]
lv = {".": "0", "#": "1"}


def pad(data, pad_char=".", n=2):
    new_data = [
        [pad_char for _ in range(len(data[0]) + 2 * n)]
        for _ in range(len(data) + 2 * n)
    ]
    for x in range(len(data[0])):
        for y in range(len(data)):
            new_data[y + n][x + n] = data[y][x]
    return new_data


def enhance(algo, data, edge_char):
    new_data = [[edge_char for _ in range(len(data[0]))] for _ in range(len(data))]
    for x in range(len(data[0]) - 2):
        for y in range(len(data) - 2):
            raw_pix = [lv[c] for line in data[y : y + 3] for c in line[x : x + 3]]
            num = int("".join(raw_pix), 2)
            new_data[y + 1][x + 1] = algo[num]
    return [line[1:-1] for line in new_data[1:-1]]


def enhance_n(algo, data, n):
    data = pad(data)
    edge_char = "."
    for _ in range(n):
        data = enhance(algo, data, edge_char)
        if edge_char == "." and algo[0] == "#":
            edge_char = "#"
        elif edge_char == "#" and algo[511] == ".":
            edge_char = "."
        data = pad(data, edge_char, 2)
    return data


def part1(algo, data):
    data = enhance_n(algo, data, 2)
    count = 0
    for line in data:
        for c in line:
            if c == "#":
                count += 1
    return count


def part2(algo, data):
    data = enhance_n(algo, data, 50)
    count = 0
    for line in data:
        for c in line:
            if c == "#":
                count += 1
    return count


print(part1(algo, data))
print(part2(algo, data))
