from heapq import *
from collections import defaultdict

N = int(input())

nodes = defaultdict(set)
for _ in range(N):
    n, *to = input().split()
    nodes[n].update(to)
    for oth in to:
        nodes[oth].add(n)
    

start, end = input().split()
prev = {}
seen = set()

heap = [start]
while heap:
    n = heappop(heap)
    if n == end:
        break
    if n in seen:
        continue
    seen.add(n)
    for oth in nodes[n]:
        if oth not in prev:
            prev[oth] = n
            heappush(heap, oth)

if end not in prev:
    print("no route found")
else:
    path = []
    while end != start:
        path.append(end)
        end = prev[end]
    path.append(start)
    print(*reversed(path))

