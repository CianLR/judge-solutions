import sys

class Node:
    def __init__(self, n):
        self.sum = n
        self.size = 1

class AlmostUF:
    def __init__(self):
        self.parent = {}
        self.nodes = {}

    def get_root(self, a):
        if a not in self.nodes:
            n = Node(a)
            self.nodes[a] = n
            self.parent[n] = None
            return n
        n = self.nodes[a]
        while self.parent[n]:
            n = self.parent[n]
        return n

    def join(self, a, b):
        aroot = self.get_root(a)
        broot = self.get_root(b)
        if aroot == broot:
            return
        if aroot.size > broot.size:
            self.parent[broot] = aroot
            aroot.size += broot.size
            aroot.sum += broot.sum
        else:
            self.parent[aroot] = broot
            broot.size += aroot.size
            broot.sum += aroot.sum

    def move(self, a, b):
        aroot = self.get_root(a)
        broot = self.get_root(b)
        if broot == aroot:
            return
        n = Node(a)
        self.nodes[a] = n
        self.parent[n] = broot
        broot.size += 1
        aroot.size -= 1
        broot.sum += a
        aroot.sum -= a

    def info(self, a):
        aroot = self.get_root(a)
        return aroot.size, aroot.sum


def main():
    while True:
        try:
            N, M = [int(x) for x in input().split()]
        except:
            break
        uf = AlmostUF()
        for _ in range(M):
            cmd, *args = [int(x) for x in input().split()]
            if cmd == 1:
                uf.join(*args)
            elif cmd == 2:
                uf.move(*args)
            else:
                print(*uf.info(*args))


if __name__ == '__main__':
    main()

