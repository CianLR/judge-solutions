from collections import defaultdict, deque

class Node:
    def __init__(self):
        self.adj = []
        self.adj_rev = []

def dfs(u, adj_getter, visited, stack):
    visited.add(u)
    for v in adj_getter(u):
        if v in visited:
            continue
        dfs(v, adj_getter, visited, stack)
    stack.append(u)

def kosaraju(nodes):
    # First dfs pass
    visited = set()
    stack = deque()
    for n in nodes:
        if n in visited:
            continue
        dfs(n, (lambda u: u.adj), visited, stack)
    # Reverse dfs pass
    sccs = []
    visited.clear()
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        scc = []
        dfs(u, (lambda u: u.adj_rev), visited, scc)
        sccs.append(scc)
    return sccs

def main():
    N = int(input())
    understands = defaultdict(list)
    chars = []
    nodes = [Node() for _ in range(N)]
    for i in range(N):
        name, speak, *under = input().split()
        chars.append((name, speak))
        understands[speak].append(nodes[i])
        for u in under:
            understands[u].append(nodes[i])

    for i, (name, speak) in enumerate(chars):
        for v in understands[speak]:
            if nodes[i] == v:
                continue
            nodes[i].adj.append(v)
            v.adj_rev.append(nodes[i])

    sccs = kosaraju(nodes)
    print(N - max(len(scc) for scc in sccs))

if __name__ == '__main__':
    main()

