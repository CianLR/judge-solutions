import heapq
from math import ceil, inf

class Edge:
    def __init__(self, fr, to, start_time, interval, cost):
        self.fr = fr
        self.to = to
        self.start_time = start_time
        self.interval = interval
        self.cost = cost

    def next_available(self, t):
        if t <= self.start_time:
            return self.start_time - t
        if self.interval == 0:
            return None
        period = ceil((t - self.start_time) / self.interval)
        return ((period * self.interval) + self.start_time) - t

def dijkstra(N, adj, S):
    q = [(0, S)]
    dists = [inf] * N
    dists[S] = 0
    while q:
        t, u = heapq.heappop(q)
        if dists[u] < t:
            continue
        for e in adj[u]:
            wait = e.next_available(t)
            if wait is None:
                continue
            next_t = t + wait + e.cost
            if dists[e.to] <= next_t:
                continue
            dists[e.to] = next_t
            heapq.heappush(q, (next_t, e.to))
    return dists


def main():
    N, M, Q, S = [int(x) for x in input().split()]
    while N or M or Q or S:
        adj = [[] for _ in range(N)]
        for _ in range(M):
            u, v, t, p, d = [int(x) for x in input().split()]
            adj[u].append(Edge(u, v, t, p, d))
        dists = dijkstra(N, adj, S)
        for _ in range(Q):
            q = int(input())
            if dists[q] < inf:
                print(dists[q])
            else:
                print("Impossible")
        print()

        N, M, Q, S = [int(x) for x in input().split()]

if __name__ == '__main__':
    main()

