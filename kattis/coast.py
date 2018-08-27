from collections import deque

def adj(r, c, R, C):
    if r + 1 < R:
        yield r + 1, c
    if r - 1 >= 0:
        yield r - 1, c
    if c + 1 < C:
        yield r, c + 1
    if c - 1 >= 0:
        yield r, c - 1

def get_coast(R, C, grid):
    coast = 0
    visited = set()
    q = deque([(0, 0)])
    while q:
        r, c = q.pop()
        for nr, nc in adj(r, c, R, C):
            if grid[nr][nc]:
                coast += 1
                continue
            if (nr, nc) in visited:
                continue
            visited.add((nr, nc))
            q.append((nr, nc))
    return coast

def main():
    R, C = map(int, input().split())
    grid = (
        [[False] * (C + 2)] +
        [
            [False] + [c == '1' for c in input()] + [False] for _ in range(R)
        ] +
        [[False] * (C + 2)]
    )
    print(get_coast(R + 2, C + 2, grid))

if __name__ == '__main__':
    main()
