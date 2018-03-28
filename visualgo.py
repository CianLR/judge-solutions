import heapq
from math import inf

def dijkstra_count_paths(V, adj, s, t):
    shortest_paths = [0] * V
    dists = [inf] * V
    shortest_paths[s] = 1
    dists[s] = 0
    q = [(0, s)]
    while q:
        d, u = heapq.heappop(q)
        if dists[u] < d:
            continue
        if u == t:
            break
        for v, w in adj[u]:
            if dists[v] < d + w:
                continue
            elif dists[v] == d + w:
                shortest_paths[v] += shortest_paths[u]
                continue
            else:
                shortest_paths[v] = shortest_paths[u]
            dists[v] = d + w
            heapq.heappush(q, (d + w, v))
    return shortest_paths[t]


def main():
    V, E = [int(x) for x in input().split()]
    adj = [[] for _ in range(V)]
    for _ in range(E):
        u, v, w = input().split()
        adj[int(u)].append((int(v), int(w)))
    s, t = [int(x) for x in input().split()]
    print(dijkstra_count_paths(V, adj, s, t))

if __name__ == '__main__':
    main()

