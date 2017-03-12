from queue import Queue
from itertools import combinations
from collections import defaultdict

class Node:
    def __init__(self, i, connects):
        self.i = i
        self.colour = None
        self.connects = connects

    def inject_intersections(self, inter):
        self.inter = inter

    def get_neigh_colours(self):
        cols = set()
        for c in self.connects:
            if self.inter[c].colour is not None:
                cols.add(self.inter[c].colour)
        return cols

    def has_neighbour(self, seen):
        for c in self.connects:
            if c in seen:
                return True
        return False

    def set_colour(self):
        negh = self.get_neigh_colours()
        i = 0
        while i in negh:
            i += 1
        self.colour = i

K = int(input())
N = int(input())

intersections = []
for i in range(N):
    _, *conected_to = map(lambda x: int(x) - 1, input().split())
    intersections.append(Node(i, conected_to))

for inter in intersections:
    inter.inject_intersections(intersections)


def one_or_pairs_of_neighbours(node_i, taken):
    available = []
    for nbr in intersections[node_i].connects:
        if not intersections[nbr].has_neighbour(taken):
            available.append(nbr)
    for a, b in combinations(available, 2):
        if not intersections[a].has_neighbour((b,)):
            yield a, b
    yield from [(x,) for x in available]


def get_n_indep(target, taken=()):
    # print([x + 1 for x in taken])
    if target == 0:
        return True

    # Get next vertex to look at
    nxt = 0
    while nxt in taken or intersections[nxt].has_neighbour(taken):
        nxt += 1
        if nxt == N:
            return False  

    if get_n_indep(target - 1, taken + (nxt,)):
        return True
    for ns in one_or_pairs_of_neighbours(nxt, taken):
        if get_n_indep(target - len(ns), taken + ns):
            return True
    return False

print('possible' if get_n_indep(K) else 'impossible')



# to_visit = Queue()
# seen = set()
# subgraph_colour_counts = []
# while len(seen) != N:
#     # Get first unseen
#     unseen = None
#     for i in range(N):
#         if i not in seen:
#             unseen = i
#             break
#     subgraph_colour_counts.append(defaultdict(int))
#     to_visit.put(intersections[unseen])
#     while not to_visit.empty():
#         inter = to_visit.get()
#         if inter.i in seen:
#             continue
#         seen.add(inter.i)
#         inter.set_colour()
#         subgraph_colour_counts[-1][inter.colour] += 1
#         for neigh in inter.connects:
#             if neigh not in seen:
#                 to_visit.put(intersections[neigh])

# print("Num different graphs:", len(subgraph_colour_counts))
# for inter in intersections:
#     print('    ', inter.i + 1, ' color:', inter.colour)
# max_drones = sum([max(sg.values()) for sg in subgraph_colour_counts])
# print("Max drones:", max_drones)
# print('impossible' if max_drones < K else 'possible')
