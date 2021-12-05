f = open("input5.txt")
all_data = [x for x in f.read().split("\n")[:-1]]
vents = [[0] * 4 for _ in range(len(all_data))]

for i, line in enumerate(all_data):
    s, f = line.split("->")
    vents[i][0], vents[i][1] = [int(x) for x in s.split(",")]
    vents[i][2], vents[i][3] = [int(x) for x in f.split(",")]

suli_mute = max([y for x in vents for y in x]) + 1
seafloor1 = [[0] * suli_mute for _ in range(suli_mute)]
seafloor2 = [[0] * suli_mute for _ in range(suli_mute)]

for v in vents:
    if v[1] == v[3]:
        orient = 1 if v[2] >= v[0] else -1
        for x in range(v[0], v[2] + orient, orient):
            seafloor1[v[1]][x] += 1
            seafloor2[v[1]][x] += 1
    elif v[0] == v[2]:
        orient = 1 if v[3] >= v[1] else -1
        for y in range(v[1], v[3] + orient, orient):
            seafloor1[y][v[0]] += 1
            seafloor2[y][v[0]] += 1
    else:
        o_x = 1 if v[1] <= v[3] else -1
        o_y = 1 if v[0] <= v[2] else -1
        space = zip(range(v[1], v[3] + o_x, o_x), range(v[0], v[2] + o_y, o_y))
        for y, x in space:
            seafloor2[y][x] += 1

ans1 = sum([j > 1 for i in seafloor1 for j in i])
ans2 = sum([j > 1 for i in seafloor2 for j in i])
print(ans1)
print(ans2)
