from sys import stdin
from collections import deque

def dfs(u, adj, visited, s):
    visited.add(u)
    for v in adj[u]:
        if v not in visited:
            dfs(v, adj, visited, s)
    s.append(u)

def kosaraju(N, adj, rev_adj):
    stack = deque()
    visited = set()
    for u in range(N):
        if u not in visited:
            dfs(u, adj, visited, stack)
    visited.clear()
    sccs = []
    while stack:
        u = stack.pop()
        if u not in visited:
            sccs.append([])
            dfs(u, rev_adj, visited, sccs[-1])
    return sccs

def build_scc_graph(adj, sccs):
    scc_id = [None] * len(adj)
    for i in range(len(sccs)):
        for u in sccs[i]:
            scc_id[u] = i
    scc_adj = [[] for _ in range(len(sccs))]
    rev_scc_adj = [[] for _ in range(len(sccs))]
    for i in range(len(sccs)):
        for u in sccs[i]:
            for v in adj[u]:
                if i == scc_id[v]:
                    continue
                scc_adj[i].append((scc_id[v], (u, v)))
                rev_scc_adj[scc_id[v]].append((i, (u, v)))
    return scc_adj, rev_scc_adj

def check_valid(scc_adj, rev_scc_adj, read_order):
    if len(scc_adj) == 1:
        return "valid"
    no_outs = {i for i in range(len(scc_adj)) if not scc_adj[i]}
    no_ins = {i for i in range(len(rev_scc_adj)) if not rev_scc_adj[i]}
    if len(no_ins) != 1 or len(no_outs) != 1:
        return "invalid"
    no_in, no_out = no_ins.pop(), no_outs.pop()
    if (sum(v == no_out for v, _ in scc_adj[no_in]) < 2 and
        (len(set(v for v, _ in scc_adj[no_in])) < 2 or
         len(set(v for v, _ in rev_scc_adj[no_out])) < 2)):
        return "invalid"
    rev_edges = []
    for v, e in scc_adj[no_in]:
        if v == no_out:
            rev_edges.append(e)
    if not rev_edges:
        return "invalid"
    return "{} {}".format(*min(rev_edges, key=lambda e: read_order[e]))

def main():
    nm = stdin.readline().strip()
    case = 1
    while nm:
        N, M = map(int, nm.split())
        adj = [[] for _ in range(N)]
        rev_adj = [[] for _ in range(N)]
        read_order = {}
        for i in range(M):
            a, b = (int(x) for x in stdin.readline().split())
            read_order[(a, b)] = i
            adj[a].append(b)
            rev_adj[b].append(a)
        
        sccs = kosaraju(N, adj, rev_adj)
        scc_adj, rev_scc_adj = build_scc_graph(adj, sccs)
        print("Case {}:".format(case),
              check_valid(scc_adj, rev_scc_adj, read_order))
        
        case += 1
        nm = stdin.readline().strip()

if __name__ == '__main__':
    main()

