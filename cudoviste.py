
R, C = map(int, input().split())
grid = [None]*R
for r in range(R):
    grid[r] = list(input())

squashed = [0] * 6
for r in range(R - 1):
    for c in range(C - 1):
        n_squash = 0
        for r_mod, c_mod in ((0, 0), (0, 1), (1, 0), (1, 1)):
            if grid[r + r_mod][c + c_mod] == '#':
                n_squash = -1
                break
            elif grid[r + r_mod][c + c_mod] == 'X':
                n_squash += 1
        squashed[n_squash] += 1

for s in squashed[:-1]:
    print(s)
