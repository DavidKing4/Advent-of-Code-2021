f = open("input21.txt")
p1, p2 = [int(x[27:]) for x in f.read().split("\n")[:-1]]


class deterministic_dice:
    roll: int
    total: int

    def __init__(self, start: int = 0) -> None:
        self.roll = start
        self.total = 0

    def next(self):
        self.total += 1
        result = self.roll + 1
        self.roll = result % 100
        return result


def part1(p1, p2):
    dice = deterministic_dice()
    s1 = s2 = 0
    while True:
        p1 += dice.next() + dice.next() + dice.next()
        p1 %= 10
        p1 = 10 if p1 == 0 else p1
        s1 += p1
        if s1 >= 1000:
            return dice.total * s2
        p2 += dice.next() + dice.next() + dice.next()
        p2 %= 10
        p2 = 10 if p2 == 0 else p2
        s2 += p2
        if s2 >= 1000:
            return dice.total * s1


def game_step(pos, score, turn, lookup):
    winners = [0, 0]
    freq = [1, 3, 6, 7, 6, 3, 1]
    if score[(turn + 1) % 2] >= 21:
        winners[(turn + 1) % 2] += 1
        return winners
    for roll, f in zip(range(3, 10), freq):
        new_pos = pos[:]
        new_pos[turn] = lookup[(pos[turn], roll)]
        new_score = score[:]
        new_score[turn] += lookup[(pos[turn], roll)]
        futures = game_step(new_pos, new_score, (turn + 1) % 2, lookup)
        winners = [(x + y * f) for x, y in zip(winners, futures)]
    return winners


def part2(p1, p2):
    lookup = dict()
    for n in range(1, 11):
        for d in range(3, 10):
            t = n + d
            t %= 10
            t = 10 if t == 0 else t
            lookup[(n, d)] = t
    return game_step([p1, p2], [0, 0], 0, lookup)


print(part1(p1, p2))
print(part2(p1, p2))
