import sys

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.count -= 1
    
    def set_sizes(self):
        yield from (self.size[i] for i in range(len(self.size)) if self.find(i) == i)


class Point:
    def __init__(self, index, x, y, z):
        self.index = index
        self.x = x
        self.y = y
        self.z = z
    
    def dist(self, p2):
        return (self.x - p2.x) ** 2 + (self.y - p2.y) ** 2 + (self.z - p2.z) ** 2
    
    def __repr__(self):
        return f"Point({self.index}, {self.x}, {self.y}, {self.z})"


def part1(points):
    uf = UnionFind(len(points))
    dists = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dists.append((points[i].dist(points[j]), i, j))
    dists.sort()
    connected = 0
    for _, i, j in dists:
        uf.union(i, j)
        connected += 1
        if connected == (10 if len(points) < 100 else 1000):
            break
    ret = 1
    for s in sorted(uf.set_sizes())[::-1][:3]:
        ret *= s
    return ret


def part2(points):
    uf = UnionFind(len(points))
    dists = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dists.append((points[i].dist(points[j]), i, j))
    dists.sort()
    for _, i, j in dists:
        uf.union(i, j)
        if uf.count == 1:
            return points[i].x * points[j].x
    return -1


def preprocess(lines):
    return [Point(i, *map(int, l.split(','))) for i, l in enumerate(lines)]


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 {sys.argv[0]} <input_file>")
        sys.exit(1)
    with open(sys.argv[1], "r") as f:
        lines = f.read().splitlines()
    lines = preprocess(lines)
    print("Part 1:", part1(lines))
    print("Part 2:", part2(lines))


if __name__ == "__main__":
    main()
