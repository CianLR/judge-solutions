
def find_player(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'P':
                return r, c

def has_draft(grid, r, c):
    if (grid[r-1][c] == 'T' or
        grid[r+1][c] == 'T' or
        grid[r][c-1] == 'T' or
        grid[r][c+1] == 'T'):
        return True
    return False

C, R = [int(x) for x in input().split()]
grid = [input() for _ in range(R)]
# grid[row][col]

P = find_player(grid)
stack = [P]
seen = set()
gold = 0
while stack:
    r, c = stack.pop()
    if (r, c) in seen:
        continue
    seen.add((r, c))
    if grid[r][c] == 'G':
        gold += 1
    if has_draft(grid, r, c):
        continue
    # Add adjacent
    for r_mod, c_mod in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nr, nc = r + r_mod, c + c_mod
        if (nr, nc) in seen or grid[nr][nc] == '#':
            continue
        stack.append((nr, nc))

print(gold)


