from tqdm import tqdm
from itertools import product

f = open("input24.txt")
raw = f.read()
commands = raw.split("inp")[1:]
for i, com in enumerate(commands):
    commands[i] = ("inp" + com).split("\n")[:-1]


def fast_step(com, n, z):
    c1 = int(com[4][6:])
    c2 = int(com[5][6:])
    c3 = int(com[15][6:])
    if (z % 26) + c2 == n:
        return z // c1
    else:
        return n + (26) * (z // c1) + c3


def fast_MONAD(commands, model):
    z = 0
    valid = ""
    for com, n in zip(commands, model):
        if n == "@":
            n = (z % 26) + int(com[5][6:])
            if n <= 0 or n >= 10:
                return [-1]
        else:
            n = int(n)
        valid += str(n)
        z = fast_step(com, n, z)
    return (z, valid)


def part1and2(commands):
    free = []
    small = None
    big = None
    model = ["@" for _ in range(14)]
    for i, com in enumerate(commands):
        if com[4][6:] != "26":
            free.append(i)
    start = 10 ** len(free)
    end = 10 ** (len(free) + 1)
    for n in tqdm(product("123456789", repeat=len(free))):
        for i in range(len(free)):
            model[free[i]] = n[i]
        if (valid := fast_MONAD(commands, model))[0] == 0:
            if small == None:
                small = valid[1]
            else:
                big = valid[1]
    return f"Part 1: {big}\nPart 2: {small}"


print(part1and2(commands))
