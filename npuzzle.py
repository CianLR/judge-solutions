
# Returns row, col
def get_proper_loc(c):
    o = ord(c) - 65
    return o // 4, o % 4

def dist(a, b, c, d):
    return abs(a - c) + abs(b - d)

grid = [list(input()) for _ in range(4)]
scatter = 0
for r in range(4):
    for c in range(4):
        if grid[r][c] == '.':
            continue
        scatter += dist(r, c, *get_proper_loc(grid[r][c]))
print(scatter)

