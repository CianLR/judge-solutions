from collections import deque

def get_start_and_end(L, R, C, grid):
    start = end = None
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if grid[l][r][c] == 'S':
                    start = (l, r, c)
                    if end:
                        return start, end
                elif grid[l][r][c] == 'E':
                    end = (l, r, c)
                    if start:
                        return start, end

DIRS = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))

def adj(L, R, C, grid, u):
    l, r, c = u
    for ld, rd, cd in DIRS:
        nl, nr, nc = l + ld, r + rd, c + cd
        if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and grid[nl][nr][nc] != '#':
            yield nl, nr, nc

def bfs(L, R, C, grid, start, end):
    q = deque([(0, start)])
    seen = {start}
    while q:
        d, u = q.pop()
        for v in adj(L, R, C, grid, u):
            if v in seen:
                continue
            if v == end:
                return d + 1
            q.appendleft((d + 1, v))
            seen.add(v)
    return None

def main():
    L, R, C = [int(x) for x in input().split()]
    while L or R or C:
        grid = []
        for _ in range(L):
            grid.append([input() for _ in range(R)])
            input()
        start, end = get_start_and_end(L, R, C, grid)
        dist = bfs(L, R, C, grid, start, end)
        print("Trapped!" if dist is None else "Escaped in {} minute(s).".format(dist))
        
        L, R, C = [int(x) for x in input().split()]

if __name__ == '__main__':
    main()

