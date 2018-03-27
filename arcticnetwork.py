import cmath

class UF:
    def __init__(self, N):
        self.root = list(range(N))
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

def complex_dist(a, b):
    return cmath.polar(a - b)[0]

def kruskals(N, points, clusters):
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            edges.append((complex_dist(points[i], points[j]), i, j))
    edges = sorted(edges)
    edge_i = 0
    d = None
    uf = UF(N)
    while uf.clusters > clusters and edge_i < len(edges):
        d, i, j = edges[edge_i]
        edge_i += 1
        if uf.connected(i, j):
            continue
        uf.join(i, j)
    return d

def main():
    N = int(input())
    for _ in range(N):
        S, P = (int(x) for x in input().split())
        points = []
        for _ in range(P):
            x, y = input().split()
            points.append(complex(int(x), int(y)))
        print('{:.2f}'.format(kruskals(P, points, S)))

if __name__ == '__main__':
    main()

