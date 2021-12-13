f = open("input13.txt")
points, raw_folds = [line for line in f.read().split("\n\n")]

suli_mute = max([int(y) for x in points.split("\n") for y in x.split(",")]) + 1
paper = [[False] * suli_mute for _ in range(suli_mute)]

for p in points.split("\n"):
    y, x = [int(n) for n in p.split(",")]
    paper[x][y] = True


def display(paper):
    for line in paper:
        print("".join(["#" if x else "." for x in line]))


def fold(paper, axis, loc):
    if axis == "y":
        new_paper = paper[:loc]
        for j in range(1, len(new_paper) + 1):
            new_paper[loc - j] = [
                new_paper[loc - j][i] or paper[loc + j][i] for i in range(len(paper[0]))
            ]
    elif axis == "x":
        new_paper = [line[:loc] for line in paper]
        for j in range(len(paper)):
            for i in range(1, len(new_paper[0]) + 1):
                new_paper[j][loc - i] = new_paper[j][loc - i] or paper[j][loc + i]
    return new_paper


def count_dots(paper):
    count = 0
    for line in paper:
        for d in line:
            if d:
                count += 1
    return count


folds = [["", 0] for _ in range(len(raw_folds.split("\n")[:-1]))]
for i, f in enumerate(raw_folds.split("\n")[:-1]):
    folds[i] = [f[11], int(f[13:])]

print(count_dots(fold(paper, *folds[0])))

for f in folds:
    paper = fold(paper, *f)

display(paper)
