from collections import defaultdict

class UF:
    def __init__(self, N):
        self.parent = range(N)
        self.size = [1] * N
        self.sets = N

    def root(self, a):
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def join(self, a, b):
        a, b = self.root(a), self.root(b)
        if a == b:
            return
        if self.size[b] > self.size[a]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.sets -= 1

def prime_mults(p, lo, N):
    grid = [True] * (N + 1)
    mults = defaultdict(list)
    for i in xrange(2, N + 1):
        if not grid[i]:
            continue
        for j in xrange(i, N + 1, i):
            grid[j] = False
            if i >= p and j >= lo:
                mults[i].append(j)
        grid[i] = True
    return mults

def main():
    T = int(raw_input())
    for c in xrange(1, T + 1):
        lo, hi, p = [int(x) for x in raw_input().split()]
        mults = prime_mults(p, lo, hi)
        uf = UF((hi - lo) + 1)
        for pr in mults:
            first, rest = mults[pr][0], mults[pr][1:]
            for r in rest:
                uf.join(first - lo, r - lo)
        print "Case #{}:".format(c), uf.sets

if __name__ == '__main__':
    main()

