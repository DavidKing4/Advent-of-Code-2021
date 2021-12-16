import heapq
from math import inf

f = open("input15.txt")
data = [line for line in f.read().split("\n")[:-1]]
chitons = [[0] * len(data[0]) for _ in range(len(data))]

for i in range(len(data)):
    for j in range(len(data[0])):
        chitons[i][j] = int(data[i][j])


class Node:
    def __init__(self, x, y, danger, t_dist) -> None:
        self.x = x
        self.y = y
        self.danger = danger
        self.t_dist = t_dist

    def __gt__(self, other):
        return self.t_dist > other.t_dist


def Dijkstra(danger, start, end):
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    shortest = [[inf] * len(danger[0]) for _ in range(len(danger))]
    shortest[start[0]][start[1]] = 0

    loc_to_node = dict()
    n0 = Node(start[1], start[0], 0, 0)
    loc_to_node.update({(start[0], start[1]): n0})

    nodes = []
    heapq.heappush(nodes, n0)
    unvisited = set()

    for y in range(len(danger)):
        for x in range(len(danger[0])):
            if not (y == start[0] and x == start[1]):
                n = Node(x, y, danger[y][x], inf)
                loc_to_node[(y, x)] = n
                unvisited.add((y, x))

    while len(nodes):
        n = heapq.heappop(nodes)
        for d in direction:
            y1 = n.y + d[0]
            x1 = n.x + d[1]
            if 0 <= y1 and y1 < len(danger) and 0 <= x1 and x1 < len(danger[0]):
                if (y1, x1) in unvisited:
                    adj = loc_to_node[(y1, x1)]
                    t_dang = adj.danger + n.t_dist
                    if t_dang < adj.t_dist:
                        shortest[y1][x1] = t_dang
                        adj.t_dist = t_dang
                        heapq.heappush(nodes, adj)

        shortest[n.y][n.x] = n.t_dist
        unvisited -= set([(n.y, n.x)])
    return shortest


def part1(chitons):
    h, w = len(chitons), len(chitons[0])
    return Dijkstra(chitons, [0, 0], [h - 1, w - 1])[h - 1][w - 1]


def part2(chitons):
    h, w = len(chitons), len(chitons[0])
    big_map = [[0] * (h * 5) for _ in range(w * 5)]
    for i in range(5):
        for j in range(5):
            for x in range(w):
                for y in range(h):
                    danger = (chitons[y][x] + i + j) % 9
                    big_map[y + h * j][x + w * i] = danger if danger else 9
    shortest = Dijkstra(big_map, [0, 0], [(h * j) - 1, (w * i) - 1])
    return shortest[(h * 5) - 1][(w * 5) - 1]


print(part1(chitons))
print(part2(chitons))
