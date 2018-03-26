from sys import stdin
from collections import deque

class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))
        self.size = [1] * N
        self.total_sets = N

    def get_root(self, a):
        while self.root[a] != a:
            self.root[a] = self.root[self.root[a]]
            a = self.root[a]
        return a

    def join(self, a, b):
        aroot, broot = self.get_root(a), self.get_root(b)
        if aroot == broot:
            return
        if self.size[aroot] < self.size[broot]:
            aroot, broot = broot, aroot
        self.size[aroot] += self.size[broot]
        self.root[broot] = aroot
        self.total_sets -= 1

def flood_fill(island_map, h, w, lookup, i_id):
    lookup[(h, w)] = i_id
    q = deque([(h, w)])
    while q:
        h, w = q.pop()
        for hm, wm in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            hn, wn = h + hm, w + wm
            if ((hn, wn) in lookup or
                hn < 0 or hn >= len(island_map) or
                wn < 0 or wn >= len(island_map[hn]) or
                island_map[hn][wn] not in {'X', '#'}):
                continue
            lookup[(hn, wn)] = i_id
            q.appendleft((hn, wn))

def connect_map(island_map):
    island_id = 0
    island_lookup = {}
    # Find all islands
    for h in range(len(island_map)):
        for w in range(len(island_map[h])):
            if (h, w) in island_lookup or island_map[h][w] not in {'X', '#'}:
                continue
            flood_fill(island_map, h, w, island_lookup, island_id)
            island_id += 1
    # Find all bridges
    bridges = 0
    uf = UnionFind(island_id)
    for h in range(len(island_map)):
        for w in range(len(island_map[h])):
            if island_map[h][w] != 'X':
                continue
            if h + 1 < len(island_map) and island_map[h + 1][w] == 'B':
                for h2 in range(h + 2, len(island_map)):
                    if island_map[h2][w] == 'X':
                        bridges += 1
                        uf.join(island_lookup[(h, w)], island_lookup[(h2, w)])
                        break
                    elif island_map[h2][w] != 'B':
                        break
            if w + 2 < len(island_map[h]) and island_map[h][w + 1] == 'B':
                for w2 in range(w + 2, len(island_map[h])):
                    if island_map[h][w2] == 'X':
                        bridges += 1
                        uf.join(island_lookup[(h, w)], island_lookup[(h, w2)])
                        break
                    elif island_map[h][w2] != 'B':
                        break

    return island_id, bridges, uf.total_sets

def main():
    l = stdin.readline()
    case = 1
    while l:
        print("Map", case)
        island_map = []
        while l.strip():
            island_map.append(l.strip())
            l = stdin.readline()

        islands, bridges, buses = connect_map(island_map)
        print("islands:", islands)
        print("bridges:", bridges)
        print("buses needed:", buses)
        print()

        case += 1
        l = stdin.readline()

if __name__ == '__main__':
    main()

