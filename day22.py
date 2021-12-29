from copy import deepcopy
from typing import List

f = open("input22.txt")
lines = f.read().split("\n")[:-1]


def part1(lines):
    com_val = {"on": True, "off": False}
    core = [[[False] * 101 for _ in range(101)] for _ in range(101)]
    for l in lines:
        com = l.split()[0]
        x_raw, y_raw, z_raw = l.split(",")
        x = [int(x) for x in x_raw.split(" ")[1][2:].split("..")]
        y = [int(y) for y in y_raw[2:].split("..")]
        z = [int(z) for z in z_raw[2:].split("..")]
        if x[0] > 50 or x[0] < -50:
            return sum([x for z in core for y in z for x in y])
        for i in range(x[0] + 50, x[1] + 51):
            for j in range(y[0] + 50, y[1] + 51):
                for k in range(z[0] + 50, z[1] + 51):
                    core[i][j][k] = com_val[com]


class Cube:
    dim: List[List[int]]
    value: bool
    area: int

    def __init__(self, x: int, y: int, z: int, value: bool) -> None:
        self.dim = [x, y, z]
        self.value = value
        area = 1
        for d in self.dim:
            area *= abs(d[1] - d[0]) + 1
        self.area = area

    def intersecting(self, cube):
        for d0, d1 in zip(self.dim, cube.dim):
            if d0[1] < d1[0]:
                return False
            elif d0[0] > d1[1]:
                return False
        return True

    def segment(self, cube):
        to_segment = cube.dim
        segments = []
        for i in range(3):
            if cube.dim[i][0] < self.dim[i][0]:
                seg_dim = deepcopy(to_segment)
                seg_dim[i][1] = self.dim[i][0] - 1
                segments.append(Cube(*seg_dim, cube.value))
            if cube.dim[i][1] > self.dim[i][1]:
                seg_dim = deepcopy(to_segment)
                seg_dim[i][0] = self.dim[i][1] + 1
                segments.append(Cube(*seg_dim, cube.value))
            if cube.dim[i][0] < self.dim[i][0]:
                to_segment[i][0] = self.dim[i][0]
            if cube.dim[i][1] > self.dim[i][1]:
                to_segment[i][1] = self.dim[i][1]

        a = 0
        for x in segments:
            a += x.area
        assert a + self.overlap(cube).area == cube.area
        return segments

    def overlap(self, cube):
        new_dim = [[0] * 2 for _ in range(3)]
        for d in range(3):
            new_dim[d][0] = max(self.dim[d][0], cube.dim[d][0])
            new_dim[d][1] = min(self.dim[d][1], cube.dim[d][1])
        value = self.value != cube.value
        return Cube(*new_dim, value)


def part2(data):
    cubes = []
    com_val = {"on": True, "off": False}
    for line in data:
        value = com_val[line.split()[0]]
        x_raw, y_raw, z_raw = line.split(",")
        x = [int(x) for x in x_raw.split(" ")[1][2:].split("..")]
        y = [int(y) for y in y_raw[2:].split("..")]
        z = [int(z) for z in z_raw[2:].split("..")]
        c1 = Cube(x, y, z, value)

        new_cubes = []
        if value:
            new_cubes.append(c1)
            for c2 in cubes:
                if c1.intersecting(c2):
                    overlap = c1.overlap(c2)
                    if overlap.dim != c2.dim:
                        new_cubes.append(overlap)
                        new_cubes.append(c2)
                else:
                    new_cubes.append(c2)
        else:
            for c2 in cubes:
                if c1.intersecting(c2):
                    new_cubes.extend(c1.segment(c2))
                else:
                    new_cubes.append(c2)
        cubes = new_cubes

    total_area = 0
    for c in cubes:
        if c.value:
            total_area += c.area
        else:
            total_area -= c.area
    return total_area


print(part1(lines))
print(part2(lines))
