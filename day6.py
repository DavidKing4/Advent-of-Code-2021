from typing import List

f = open("input6.txt")
fish = [int(x) for x in f.read().strip().split(",")]
fish_counts = [0] * 6
for i, f in enumerate(fish):
    fish_counts[f] += 1


def go_forth_and_multiply(days: int) -> List[int]:
    timers = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    popu = [1]
    for _ in range(days):
        if timers[0] > 0:
            mama_baby_pairs = timers.pop(0)
            timers.append(mama_baby_pairs)
            timers[6] += mama_baby_pairs
            popu.append(sum(timers))
        else:
            timers.pop(0)
            timers.append(0)
            popu.append(sum(timers))
    return list(reversed(popu[-6:]))


def fish_factory(counts: List[int], days: int = 80) -> int:
    mult_factor = go_forth_and_multiply(days)
    resulting_pop = [x * y for x, y in zip(mult_factor, counts)]
    return sum(resulting_pop)


print(fish_factory(fish_counts))
print(fish_factory(fish_counts, days=256))
