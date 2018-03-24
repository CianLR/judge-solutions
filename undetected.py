
class UF(object):
    
    __slots__ = ('parent', 'weight')
    
    def __init__(self, N):
        self.parent = range(N)
        self.weight = [1] * N

    def get_root(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def join(self, a, b):
        aroot = self.get_root(a)
        broot = self.get_root(b)
        if aroot == broot:
            return
        if self.weight[aroot] > self.weight[broot]:
            self.parent[broot] = aroot
            self.weight[aroot] += self.weight[broot]
        else:
            self.parent[aroot] = broot
            self.weight[broot] += self.weight[aroot]

    def connected(self, a, b):
        return self.get_root(a) == self.get_root(b)


def circle_intersect(ax, ay, ar, bx, by, br):
    center_dist = ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5
    return center_dist <= ar + br

def main():
    N = int(raw_input())
    uf =  UF(N + 2)
    circles = []
    for i in xrange(N):
        x, y, r = [int(x) for x in raw_input().split()]
        for ci, (cx, cy, cr) in enumerate(circles):
            if circle_intersect(x, y, r, cx, cy, cr):
                uf.join(i + 2, ci + 2)
        circles.append((x, y, r))
        if circle_intersect(x, y, r, 0, y, 0):
            uf.join(i + 2, 0)
        if circle_intersect(x, y, r, 200, y, 0):
            uf.join(i + 2, 1)
        # Check if path
        if uf.connected(0, 1):
            print i
            break

if __name__ == '__main__':
    main()

