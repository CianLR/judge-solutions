from heapq import *

class UF:
    def __init__(self):
        self.parent = {}
        self.size = {}
    
    def root(self, a):
        if a not in self.parent:
            self.parent[a] = a
            self.size[a] = 1
            return a
        prev = None
        while self.parent[a] != a:
            a = self.parent[a]
            self.parent[prev] = self.parent[a]
            prev = a
        return a

    def is_union(self, a, b):
        return self.root(a) == self.root(b)

    def join(self, a, b):
        ar = self.root(a)
        br = self.root(b)
        if ar == br:
            return
        if self.size[ar] > self.size[br]:
            self.parent[br] = ar
            self.size[ar] += self.size[br]
        else:
            self.parent[ar] = br
            self.size[br] += self.size[ar]

def mst(N, M, edge_q):
    cost = 0
    edges_in_tree = []
    uf = UF()
    while edge_q and len(edges_in_tree) < N - 1:
        w, u, v = heappop(edge_q)
        if uf.is_union(u, v):
            continue
        cost += w
        uf.join(u, v)
        edges_in_tree.append((u, v))
    
    if len(edges_in_tree) != N - 1:
        print "Impossible"
    else:
        print cost
        for u, v in sorted(edges_in_tree):
            print u, v


def main():
    N, M = map(int, raw_input().split())
    while N or M:
        edge_q = []
        for _ in xrange(M):
            u, v, w = raw_input().split()
            u, v = int(u), int(v)
            heappush(edge_q, (int(w), min(u, v), max(v, u)))
        mst(N, M, edge_q)
        N, M = map(int, raw_input().split())



if __name__ == '__main__':
    main()


