from queue import Queue
from copy import deepcopy

# Board indicies
# 0 1 2
# 3 4 5
# 6 7 8
#
# x,y
# 0,0 1,0 2,0
# 0,1 1,1 2,1
# 0,2 1,2 2,2

class Board:
    def __init__(self):
        self.grid = [[False]*3 for _ in range(3)]

    def _on_b(self, x, y):
        return 0 <= x <= 2 and 0 <= y <= 2

    def flip(self, x, y):
        muts = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
        for n_x, n_y in [(x + n[0], y + n[1]) for n in muts]:
            if self._on_b(n_x, n_y):
                self.grid[n_x][n_y] = not self.grid[n_x][n_y]

    def copy(self):
        b = Board()
        b.grid = deepcopy(self.grid)
        return b

    def serialise(self):
        on = []
        for y in range(3):
            for x in range(3):
                if self.grid[x][y]:
                    on.append((x, y))
        return tuple(on)

q = Queue()
q.put((Board(), 0))
dists = {Board().serialise(): 0}
while not q.empty():
    b, dist = q.get()
    for x in range(3):
        for y in range(3):
            b.flip(x, y)
            s = b.serialise()
            if not s in dists:
                dists[s] = dist + 1
                q.put((b.copy(), dist + 1))
            b.flip(x, y)

P = int(input())
for _ in range(P):
    on = []
    for y in range(3):
        for x, c in enumerate(input()):
            if c == '*':
                on.append((x, y))
    print(dists[tuple(on)])
