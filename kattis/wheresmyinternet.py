
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.tree_size = {}

    def get_root(self, n):
        if n not in self.parent:
            self.parent[n] = None
            self.tree_size[n] = 1
            return n
        while self.parent[n]:
            n = self.parent[n]
        return n
    
    def is_connected(self, a, b):
        return self.get_root(a) == self.get_root(b)

    def connect_pair(self, a, b):
        a_root = self.get_root(a)
        b_root = self.get_root(b)
        if a_root == b_root:
            return self.tree_size[a_root]

        a_sz = self.tree_size[a_root]
        b_sz = self.tree_size[b_root]
        
        large, small = a_root, b_root
        if a_sz < b_sz:
            large, small = small, large

        self.parent[small] = large
        self.tree_size[large] += self.tree_size[small]
        return self.tree_size[large]


def main():
    N, M = [int(x) for x in input().split()]
    uf = UnionFind()
    for _ in range(M):
        uf.connect_pair(*input().split())
    
    found = False
    for i in range(2, N + 1):
        if not uf.is_connected('1', str(i)):
            print(i)
            found = True
    if not found:
        print("Connected")


if __name__ == '__main__':
    main()

