f = open("input10.txt")
data = [line for line in f.read().strip().split("\n")]
opening = "[{(<"
matching = {"[": "]", "(": ")", "<": ">", "{": "}"}
checker_scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
completion_scoring = {"(": 1, "[": 2, "{": 3, "<": 4}
completion_scores = []
ans1 = 0

for i, line in enumerate(data):
    subcount = 0
    stack = list()
    for x in line:
        if x in opening:
            stack.append(x)
        else:
            t = stack.pop()
            if not matching[t] == x:
                ans1 += checker_scoring[x]
                break
    else:
        for x in stack[::-1]:
            subcount *= 5
            subcount += completion_scoring[x]
        completion_scores.append(subcount)

completion_scores.sort()
ans2 = completion_scores[len(completion_scores) // 2]

print(ans1)
print(ans2)
