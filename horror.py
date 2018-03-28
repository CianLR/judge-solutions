from math import inf
from collections import deque

def bfs(N, adj, starts):
    dists = [inf] * N
    q = deque((0, s) for s in starts)
    for s in starts:
        dists[s] = 0
    while q:
        d, u = q.pop()
        for v in adj[u]:
            if dists[v] <= d + 1:
                continue
            dists[v] = d + 1
            q.appendleft((d + 1, v))
    return dists
            

def main():
    N, H, L = (int(x) for x in input().split())
    horror = [int(x) for x in input().split()]
    adj = [[] for _ in range(N)]
    for _ in range(L):
        a, b = (int(x) for x in input().split())
        adj[a].append(b)
        adj[b].append(a)
    dists = bfs(N, adj, horror)
    best = 0
    for i in range(1, len(dists)):
        if dists[i] > dists[best]:
            best = i
    print(best)

if __name__ == '__main__':
    main()

