R, C, zR, zC = map(int, input().split())
grid = [input() for _ in range(R)]

for line in grid:
    for _ in range(zR):
        for c in line:
            print(c*zC, end='')
        print()
