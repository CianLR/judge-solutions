import sys
import operator

sys.setrecursionlimit(10000)

def dfs(adj, r, l, seen, u):
    seen[u] = True
    for v in adj[u]:
        if l[v] == -1 or (not seen[l[v]] and dfs(adj, r, l, seen, l[v])):
            r[u] = v
            l[v] = u
            return True
    return False

def hopcroft_karp(N, M, adj):
    r, l = [-1] * N, [-1] * M
    for u in range(N):
        if r[u] == -1 and not dfs(adj, r, l, [False] * N, u):
            return
    return r

OPS = [operator.add, operator.mul, operator.sub]

def get_op(a, b, r):
    if a - b == r:
        return '-'
    elif a + b == r:
        return '+'
    return '*'

def main():
    N = int(input())
    right, left, left_lookup = [], [], {}
    adj = [[] for _ in range(N)]
    for i in range(N):
        a, b = (int(x) for x in input().split())
        right.append((a, b))
        res = {op(a, b) for op in OPS}
        for r in res:
            if r not in left:
                left_lookup[r] = len(left)
                left.append(r)
            adj[i].append(left_lookup[r])
    matching = hopcroft_karp(N, len(left), adj)
    if matching is None:
        print("impossible")
        return
    for u, v in enumerate(matching):
        print("{} {} {} = {}".format(
            right[u][0], get_op(*right[u], left[v]), right[u][1], left[v]))

if __name__ == '__main__':
    main()
