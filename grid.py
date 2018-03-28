from collections import deque

class Node:
    def __init__(self):
        self.adj = []

def bfs(start, end):
    q = deque([(0, start)])
    seen = set([start])
    while q:
        d, u = q.pop()
        for v in u.adj:
            if v in seen:
                continue
            if v == end:
                return d + 1
            seen.add(v)
            q.appendleft((d + 1, v))
    return -1

def main():
    R, C = [int(x) for x in input().split()]
    grid = [[Node() for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c, x in enumerate(map(int, input())):
            for nr, nc in ((r + x, c), (r - x, c), (r, c + x), (r, c - x)):
                if 0 <= nr < R and 0 <= nc < C:
                    grid[r][c].adj.append(grid[nr][nc])
    print(bfs(grid[0][0], grid[-1][-1]))

if __name__ == '__main__':
    main()

