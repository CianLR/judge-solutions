T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]

    # flip_grid = [[None]*C for _ in range(R)]
    print("Test", t)
    for r in range(R):
        for c in range(C):
            print(grid[-r-1][-c-1], end='')
        print()



