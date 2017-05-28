from math import floor

def get_r_c(size):
    r = floor(size ** 0.5)
    while size % r != 0:
        r -= 1
    return r, size // r


mess = input()
R, C = get_r_c(len(mess))
mess_it = iter(mess)
grid = [['']*C for _ in range(R)]
for c in range(C):
    for r in range(R):
        grid[r][c] = next(mess_it)

for r in range(R):
    for c in range(C):
        print(grid[r][c], end='')
print()
