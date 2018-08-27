
def adj_sq(m, n, grid, i, j, seen):
    for im, jm in [(1, 0), (1, 1), (0, 1), (-1, 1),
                   (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if (0 <= i + im < m and
            0 <= j + jm < n and
            grid[i + im][j + jm] and
            (i + im, j + jm) not in seen):
            yield i + im, j + jm

def dfs(m, n, grid, start, seen):
    stack = [start]
    while stack:
        i, j = stack.pop()
        if (i, j) in seen:
            continue
        seen.add((i, j))
        for ni, nj in adj_sq(m, n, grid, i, j, seen):
            stack.append((ni, nj))

def flood_fill(m, n, grid):
    seen = set()
    colours = 0
    for i in range(m):
        for j in range(n):
            if (i, j) in seen or not grid[i][j]:
                continue
            colours += 1
            dfs(m, n, grid, (i, j), seen)
    return colours

def main():
    m, n = [int(x) for x in input().split()]
    grid = [
        [c == '#' for c in input()] for _ in range(m)
    ]
    print(flood_fill(m, n, grid))

if __name__ == '__main__':
    main()


