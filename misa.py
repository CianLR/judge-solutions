R, C = map(int, input().split())

def get_num_neighbours(grid, r, c, top_and_left_only=False):
    count = 0
    if r > 0 and c > 0:
        count += grid[r - 1][c - 1]
    if r > 0:
        count += grid[r - 1][c]
    if c > 0:
        count += grid[r][c - 1]
    if r > 0 and c < C - 1:
        count += grid[r - 1][c + 1]

    if top_and_left_only:
        return count

    if r < R - 1 and c > 0:
        count += grid[r + 1][c - 1]
    if r < R - 1 and c < C - 1:
        count += grid[r + 1][c + 1]
    if r < R - 1:
        count += grid[r + 1][c]
    if c < C - 1:
        count += grid[r][c + 1]
    return count


# grid[r][c]
grid = [[False]*C for _ in range(R)]
for r in range(R):
    for c, p in enumerate(input()):
        grid[r][c] = p == 'o'

max_neigh = -1
max_r = max_c = -1
for r in range(R):
    for c in range(C):
        if grid[r][c]:
            continue
        nbrs = get_num_neighbours(grid, r, c)
        if nbrs > max_neigh:
            max_neigh = nbrs
            max_r, max_c = r, c

if max_neigh > 0:
    grid[max_r][max_c] = True

handshakes = 0
for r in range(R):
    for c in range(C):
        if not grid[r][c]:
            continue
        handshakes += get_num_neighbours(
            grid, r, c, top_and_left_only=True)

print(handshakes)
