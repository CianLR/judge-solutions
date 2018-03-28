import heapq

def prims(N, adj, pre_connected):
    used_nodes = 0
    mst_cost = 0
    in_tree = [False] * N
    best_edge = [1000000] * N
    q = []
    for u in pre_connected:
        in_tree[u] = True
        used_nodes += 1
        for v, w in adj[u]:
            heapq.heappush(q, (w, v))
    while used_nodes < N:
        w, u = heapq.heappop(q)
        if in_tree[u]:
            continue
        in_tree[u] = True
        mst_cost += w
        used_nodes += 1
        for v, w2 in adj[u]:
            if in_tree[v] or w2 > best_edge[v]:
                continue
            best_edge[v] = w2
            heapq.heappush(q, (w2, v))
    return mst_cost

def main():
    T = int(raw_input())
    for _ in xrange(T):
        N, M, L, S = [int(x) for x in raw_input().split()]
        pre_connected = [int(x) - 1 for x in raw_input().split()]
        adj = [[] for _ in xrange(N)]
        for _ in xrange(M):
            u, v, w = [int(x) for x in raw_input().split()]
            adj[u - 1].append((v - 1, w))
            adj[v - 1].append((u - 1, w))

        mst = prims(N, adj, pre_connected)
        print mst + (L * (N - S))

if __name__ == '__main__':
    main()

