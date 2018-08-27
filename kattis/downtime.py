from heapq import *
from math import ceil

N, K = [int(x) for x in input().split()]

pq = []
for _ in range(N):
    time_in = int(input())
    heappush(pq, (time_in, 1))
    heappush(pq, (time_in + 1000, -1))

max_count = 0
cur_count = 0
while pq:
    _, mod = heappop(pq)
    cur_count += mod
    max_count = max(max_count, cur_count)

print(ceil(max_count / K))

