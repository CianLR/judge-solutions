
inf = float('infinity')

def bellman_ford(N, edges, start):
    dist = [inf] * N
    dist[start] = 0
    for _ in xrange(N - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    neg = [False] * N
    changes = True
    while changes:
        changes = False
        for u, v, w in edges:
            if not neg[v] and (neg[u] or dist[u] + w < dist[v]):
                neg[v] = changes = True
    return dist, neg

def main():
    N, M, Q, S = (int(x) for x in raw_input().split())
    while N or M or Q or S:
        edges = [tuple(int(x) for x in raw_input().split()) for _ in xrange(M)]
        dist, neg = bellman_ford(N, edges, S)
        for _ in xrange(Q):
            q = int(raw_input())
            if neg[q]:
                print "-Infinity"
            else:
                print dist[q] if dist[q] != inf else "Impossible"
        print
        N, M, Q, S = (int(x) for x in raw_input().split())

if __name__ == '__main__':
    main()


