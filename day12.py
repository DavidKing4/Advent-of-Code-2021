from copy import deepcopy
from typing import Generic, List, TypeVar

f = open("input12.txt")
connections = [line for line in f.read().split("\n")[:-1]]

N = TypeVar("N")


class Node(Generic[N]):
    connections: List[N]
    name: str
    big: bool
    visited: bool

    def __init__(self, name, big):
        self.name = name
        self.big = big
        self.connections = list()
        self.visited = False

    def add_con(self, con):
        self.connections.append(con)

    def visit(self):
        if self.big:
            return
        self.visited = True

    def all_ways_to_end(self, twice, trace):
        if self.name == "end":
            trace.append("end")
            t = set()
            t.add(tuple(trace))
            return t
        routes = set()
        if twice and self.name != "start" and not self.big:
            for cave in self.connections:
                if cave.big or not cave.visited:
                    t = deepcopy(trace)
                    t.append(self.name)
                    routes = routes.union(deepcopy(cave).all_ways_to_end(False, t))

        self.visited = True
        for cave in self.connections:
            if cave.big or not cave.visited:
                t = deepcopy(trace)
                t.append(self.name)
                routes = routes.union(deepcopy(cave).all_ways_to_end(twice, t))
        return routes

    def num_ways_to_end(self, twice, trace):
        x = self.all_ways_to_end(twice, trace)
        return len(x)


all_caves = dict()
for line in connections:
    a, b = line.split("-")
    if a not in all_caves:
        A = Node(a, a.isupper())
    else:
        A = all_caves[a]
    if b not in all_caves:
        B = Node(b, b.isupper())
    else:
        B = all_caves[b]
    A.add_con(B)
    B.add_con(A)
    all_caves.update({a: A, b: B})

print(all_caves["start"].num_ways_to_end(False, list()))
print(all_caves["start"].num_ways_to_end(True, list()))
