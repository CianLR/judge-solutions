R, C = map(int, input().split())
while R and C:
    grid = ['' for _ in range(C)]
    for _ in range(R):
        for i, c in enumerate(input()):
            grid[i] += c

    for comb in zip(*sorted(grid, key=lambda c: c.lower())):
        print(''.join(comb))
    print()

    R, C = map(int, input().split())
