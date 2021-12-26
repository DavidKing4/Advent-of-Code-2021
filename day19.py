from copy import deepcopy
import numpy as np
from typing import List, Tuple, TypeVar, Generic, Optional

f = open("input19.txt")
raw_scanners = f.read()[:-1].split("\n\n")
scanners = [(x.split("\n")[1:]) for x in raw_scanners]

for i in range(len(scanners)):
    for j in range(len(scanners[i])):
        scanners[i][j] = [int(x) for x in scanners[i][j].split(",")]


Beacon = List[int]
SC = TypeVar("SC")


class Scanner(Generic[SC]):
    id: int
    beacons: List[Beacon]
    loc: List[int]
    links: List[SC]

    def __init__(self, id: int, beacons: List[Beacon]) -> None:
        self.id = id
        self.beacons = beacons
        self.loc = None
        self.links = []

    def find_link(self, s2: SC, tol: int = 12) -> Optional[bool]:
        max_overlap = 0
        for b1 in self.beacons:
            for b2 in s2.beacons:

                diff = [x1 - x2 for x1, x2 in zip(b1, b2)]
                overlap = []
                for b3 in self.beacons:
                    if b1 != b3:
                        trans = [x3 - x4 for x3, x4 in zip(b3, diff)]
                        if trans in s2.beacons:
                            overlap.append(trans)
                if len(overlap) == tol - 1:
                    self.join(s2, diff)
                    self.links.append(s2)
                    s2.links.append(self)
                    return True
                if len(overlap) > max_overlap:
                    max_overlap = len(overlap)

    def join(self, s2: SC, diff: Beacon) -> None:
        if self.loc is None and s2.loc is None:
            self.loc = [0 for _ in range(len(diff))]
            s2.loc = diff
            s2.update_beacons(diff)
        elif self.loc is not None and s2.loc is None:
            s2.loc = diff
            s2.update_beacons(diff)
        else:
            raise ValueError("One should not linke in this fasion")

    def update_beacons(self, diff):
        for i in range(len(self.beacons)):
            self.beacons[i] = [x + d for x, d in zip(self.beacons[i], diff)]


def all_rotations_multiple(beacons: List[Beacon]) -> List[List[Beacon]]:
    rot_x = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
    rot_z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    rot_y = np.array([[0, 0, -1], [0, 1, 0], [1, 0, 0]])
    rotated = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                new_beacons = []
                for b in beacons:
                    b_new = [x for x in b]
                    for _ in range(i):
                        b_new = list(np.matmul(rot_x, b_new))
                    for _ in range(j):
                        b_new = list(np.matmul(rot_y, b_new))
                    for _ in range(k):
                        b_new = list(np.matmul(rot_z, b_new))
                    new_beacons.append(b_new)
                rotated.append(new_beacons)
    return rotated


def part1and2(raw_scanners: Tuple[Tuple[Tuple[int]]]) -> List[SC]:
    rotations: List[List[SC]] = []
    linked: List[SC] = []
    unchecked: List[SC] = []

    for i, s in enumerate(raw_scanners):
        rotations.append([])
        for r in all_rotations_multiple(s):
            rotations[i].append(Scanner(i, deepcopy(r)))
    linked.append(rotations[0][0])
    unchecked.append(rotations[0][0])
    rotations.pop(0)

    while unchecked:
        print(f"unchecked :{len(unchecked)}\trotations: {len(rotations)}    ")
        to_check = unchecked.pop(0)
        n = 0
        while True:
            for n in range(n, len(rotations)):
                for r in range(len(rotations[n])):
                    if to_check.find_link(rotations[n][r]):
                        print(f"link created: {to_check.id} {rotations[n][r].id}")
                        unchecked.append(rotations[n][r])
                        linked.append(rotations[n][r])
                        rotations.pop(n)
                        break
                else:
                    continue
                break
            else:
                break

    all_becons = set()
    for s in linked:
        for b in s.beacons:
            all_becons.add(tuple(b))

    suli_mute = 0
    for s1 in linked:
        for s2 in linked:
            if s1 != s2:
                d = sum([abs(x1 - x2) for x1, x2 in zip(s1.loc, s2.loc)])
                if d > suli_mute:
                    suli_mute = d

    return f"Part 1: {len(all_becons)}\nPart 2: {suli_mute}"


print(part1and2(scanners))
