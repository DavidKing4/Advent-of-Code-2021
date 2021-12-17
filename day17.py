f = open("input17.txt")
raw_data = f.read()[:-1]

raw_x, raw_y = raw_data[13:].split(", ")
x = [int(x) for x in raw_x[2:].split("..")]
y = [int(y) for y in raw_y[2:].split("..")]


def fire(v, u, x, y):
    i = j = 0
    while i <= x[1] and j >= y[0]:
        if i >= x[0] and j <= y[1]:
            return True  # HIT
        i += v
        j += u
        if v > 0:
            v -= 1
        u -= 1
    return False  # MISS


def part1(x, y):
    assert y[1] < 0, "This approach will not work when target above start"
    x_min = 0
    for i in range(x[0]):
        if (t := sum(range(i))) >= x[0]:
            x_min = i
            break
    for u in range(abs(y[0]), -1, -1):
        for v in range(x_min, x[1]):
            if fire(v, u, x, y):
                return sum(range(u + 1))


def part2(x, y):
    assert y[1] < 0, "This approach will not work when target above start"
    x_min = 0
    count = 0
    for i in range(x[0]):
        if sum(range(i + 1)) >= x[0]:
            x_min = i
            break
    for u in range(abs(y[0]), -1 * abs(y[0]) - 1, -1):
        for v in range(x_min, x[1] + 1):
            if fire(v, u, x, y):
                count += 1
    return count


print(part1(x, y))
print(part2(x, y))
