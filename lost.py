from collections import defaultdict
import heapq

def dijkstra(edges):
    cost = 0
    seen = set()
    pq = [(0, 0, 'English', None)]
    while pq:
        l, c, u, p = heapq.heappop(pq)
        if u in seen:
            continue
        seen.add(u)
        cost += c
        for v in edges[u]:
            if v in seen:
                continue
            heapq.heappush(pq, (l + 1, edges[u][v], v, u))
    return cost, len(seen)

def main():
    N, M = [int(x) for x in input().split()]
    targets = input().split()
    edges = defaultdict(dict)
    for _ in range(M):
        u, v, c = input().split()
        edges[u][v] = int(c)
        edges[v][u] = int(c)

    cost, visited = dijkstra(edges)
    if visited != len(targets) + 1:
        print("Impossible")
    else:
        print(cost)

if __name__ == '__main__':
    main()

