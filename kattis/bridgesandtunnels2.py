from heapq import heappush, heappop


def dijkstra(adj, start, end):
    seen = set()
    # Time outside, total time, vertex
    pq = [(0, 0, start)]
    while pq:
        to, tt, u = heappop(pq)
        if u == end:
            return "{} {}".format(to, tt)
        elif u in seen:
            continue
        seen.add(u)
        for v, t, o in adj[u]:
            if v in seen:
                continue
            heappush(pq, (to + (t if o else 0), tt + t, v))
    return 'IMPOSSIBLE'


def main():
    N, M, P = [int(x) for x in input().split()]
    adj = [[] for _ in range(N)]
    for _ in range(M):
        u, v, t, io = input().split()
        u, v, t = int(u), int(v), int(t)
        adj[u].append((v, t, io == 'O'))
        adj[v].append((u, t, io == 'O'))
    for _ in range(P):
        start, end = [int(x) for x in input().split()]
        print(dijkstra(adj, start, end))

if __name__ == '__main__':
    main()
