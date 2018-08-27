N = int(input())

grid = [[int(x) for x in input().split()] for _ in range(N)]
outs = []
for i in range(N):
    ands = [a for j, a in enumerate(grid[i]) if j != i]
    val = 0
    for v2 in ands:
        val |= v2
    outs.append(val)

print(*outs)
