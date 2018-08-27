import sys

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oth):
        return Point(self.x + oth.x, self.y + oth.y)

    def __sub__(self, oth):
        return Point(self.x - oth.x, self.y - oth.y)


dirs = {
    'down': Point(0, 1),
    'up': Point(0, -1),
    'left': Point(-1, 0),
    'right': Point(1, 0),
}

curr = Point(0, 0)
visited = [curr]
for line in sys.stdin.readlines():
    curr = curr + dirs[line.strip()]
    visited.append(curr)

min_x = min([p.x for p in visited])
min_y = min([p.y for p in visited])

# Point to move so nothing < 1
mod = Point(min_x - 1, min_y - 1)
for i in range(len(visited)):
    visited[i] = visited[i] - mod

max_x = max([p.x for p in visited])
max_y = max([p.y for p in visited])

grid = [[' '] * (max_y + 2) for _ in range(max_x + 2)]
for i in range(len(grid)):
    grid[i][0] = '#'
    grid[i][-1] = '#'

for i in range(len(grid[0])):
    grid[0][i] = '#'
    grid[-1][i] = '#'

for p in visited:
    grid[p.x][p.y] = '*'

grid[visited[0].x][visited[0].y] = 'S'
grid[visited[-1].x][visited[-1].y] = 'E'

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='')
    print()

