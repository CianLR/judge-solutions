
class Node:
    def __init__(self):
        self.ds = None
        self.connects = []

    def add_connect(self, con_node):
        self.connects.append(con_node)

    def get_dists(self):
        if self.ds is not None:
            return self.ds
        self.ds = set()
        for n in self.connects:
            for d in n.get_dists():
                self.ds.add(d + 1)
        return self.ds


def main():
    N1, N2, M1, M2 = map(int, raw_input().split())
    g1 = [Node() for _ in range(N1)]
    g1[-1].ds = {0}
    g2 = [Node() for _ in range(N2)]
    g2[-1].ds = {0}

    for _ in range(M1):
        u, v = [int(x) for x in raw_input().split()]
        g1[u - 1].add_connect(g1[v - 1])
    for _ in range(M2):
        u, v = [int(x) for x in raw_input().split()]
        g2[u - 1].add_connect(g2[v - 1])
    
    g1_ds = g1[0].get_dists()
    g2_ds = g2[0].get_dists()
    
    combs = set()
    for a in g1_ds:
        for b in g2_ds:
            combs.add(a + b)

    Q = int(raw_input())
    for _ in range(Q):
        q = int(raw_input())
        if q in combs:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()

