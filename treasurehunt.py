R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]
dirs = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

def get_new_dir(r, c, d):
    return r + dirs[d][0], c + dirs[d][1]

def trace_path():
    visited = set()
    r = c = 0
    steps = 0
    while 0 <= r < R and 0 <= c < C:
        if (r, c) in visited:
            return 'Lost'
        visited.add((r, c))
        if grid[r][c] == 'T':
            return steps
        r, c = get_new_dir(r, c, grid[r][c])
        steps += 1
    return 'Out'

print(trace_path())

