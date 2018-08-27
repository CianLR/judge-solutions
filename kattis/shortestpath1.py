import heapq

def dijkstra(adj, start):
    q = [(0, start)]
    dists = {}
    while q:
        d, u = heapq.heappop(q)
        if u in dists:
            continue
        dists[u] = d
        for v, w in adj[u]:
            if v not in dists:
                heapq.heappush(q, (d + w, v))
    return dists

def main():
    N, M, Q, S = [int(x) for x in input().split()]
    while N or M or Q or S:
        adj = [[] for _ in range(N)]
        for _ in range(M):
            u, v, w = input().split()
            adj[int(u)].append((int(v), int(w)))
        dists = dijkstra(adj, S)
        for _ in range(Q):
            q = int(input())
            print(dists[q] if q in dists else "Impossible")
        print()
        N, M, Q, S = [int(x) for x in input().split()]

if __name__ == '__main__':
    main()
