import numpy as np

f = open("input7.txt")
crab = np.array([int(x) for x in f.read().strip().split(",")])

costs = [x for x in range(1, max(crab))]
ans1 = sum(crab)
ans2 = sum([sum(costs[0:x]) for x in crab])
for x in range(min(crab), max(crab)):
    if (t1 := sum(abs(crab - x))) < ans1:
        ans1 = t1
    if (t2 := sum([sum(costs[0:x]) for x in abs(crab - x)])) < ans2:
        ans2 = t2
    if t1 > ans1 and t2 > ans2:
        break

print(ans1)
print(ans2)
