from copy import copy
import re

f = open("input14.txt")
poly, raw_rules = [line for line in f.read().split("\n\n")]
rules = dict()

for r in raw_rules.split("\n")[:-1]:
    pair, element = r.split(" -> ")
    rules.update({pair: element})


def step(poly, rules):
    match_iter = list(re.finditer("(?=" + "|".join(rules.keys()) + ")", poly))
    match_iter.reverse()
    for match in match_iter:
        s = match.start()
        poly = poly[: s + 1] + rules[poly[s : s + 2]] + poly[s + 1 :]
    return poly


def expand(poly, rules, steps):
    for _ in range(steps):
        poly = step(poly, rules)
    return poly


def part1(poly, rules):
    poly = expand(poly, rules, 10)
    cs = [poly.count(x) for x in "".join(set(poly))]
    return max(cs) - min(cs)


def part2(poly, rules):
    product = {}
    counts = {}
    for par, child in rules.items():
        product[par] = (par[0] + child, child + par[1])
        counts[par] = 0
    count_reset = copy(counts)
    for n in range(len(poly) - 1):
        counts[poly[n : n + 2]] += 1
    parents = list(product.keys())
    for _ in range(40):
        new_count = copy(count_reset)
        for par in parents:
            for prod in product[par]:
                new_count[prod] += counts[par]
        counts = copy(new_count)

    final_count = {}
    for k, v in counts.items():
        for i in range(2):
            if k[i] in final_count:
                final_count[k[i]] += v
            else:
                final_count[k[i]] = v

    final_count[poly[0]] -= 1
    final_count[poly[-1]] -= 1
    xs = [x for x in final_count.values()]
    return int((max(xs) / 2) - (min(xs) / 2) + 1)


print(part1(poly, rules))
print(part2(poly, rules))
