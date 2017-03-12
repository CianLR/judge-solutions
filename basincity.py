from queue import Queue
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


to_visit = Queue()
seen = set()
colour_counts = defaultdict(int)
while len(seen) != N:
    # Get first unseen
    unseen = None
    for i in range(N):
        if i not in seen:
            unseen = i
            break
    to_visit.put(intersections[unseen])
    while not to_visit.empty():
        inter = to_visit.get()
        if inter.i in seen:
            continue
        seen.add(inter.i)
        inter.set_colour()
        colour_counts[inter.colour] += 1
        for neigh in inter.connects:
            if neigh not in seen:
                to_visit.put(intersections[neigh])

# print("Max drones:", max(colour_counts.values()))
print('impossible' if max(colour_counts.values()) < K else 'possible')
