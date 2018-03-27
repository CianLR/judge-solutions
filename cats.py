from sys import stdin

class UF:
    def __init__(self, N):
        self.root = range(N)
        self.size = [1] * N
        self.clusters = N

    def _get_root(self, a):
        while self.root[a] != a:
            self.root[a] = self.root[self.root[a]]
            a = self.root[a]
        return a

    def join(self, a, b):
        ar, br = self._get_root(a), self._get_root(b)
        if ar == br:
            return
        if self.size[br] > self.size[ar]:
            ar, br = br, ar
        self.root[br] = ar
        self.size[ar] += self.size[br]
        self.clusters -= 1

    def connected(self, a, b):
        return self._get_root(a) == self._get_root(b)


def kruskals(N, edges):
    edges = sorted(edges)
    edges_i = 0
    mst_weight = 0
    uf = UF(N)
    while uf.clusters > 1 and edges_i < len(edges):
        d, i, j = edges[edges_i]
        edges_i += 1
        if uf.connected(i, j):
            continue
        uf.join(i, j)
        mst_weight += d
    return mst_weight

def main():
    T = int(stdin.readline())
    for _ in xrange(T):
        M, C = (int(x) for x in stdin.readline().split())
        cat_dists = []
        for _ in xrange((C * (C - 1)) // 2):
            i, j, d = (int(x) for x in stdin.readline().split())
            cat_dists.append((d, i, j))
        mst = kruskals(C, cat_dists)
        print "yes" if mst + C <= M else "no"

if __name__ == '__main__':
    main()

