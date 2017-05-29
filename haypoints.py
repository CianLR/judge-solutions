M, N = map(int, input().split())

points = {}
for _ in range(M):
    w, p = input().split()
    points[w] = int(p)

for _ in range(N):
    desc_toks = []
    line = input()
    while line != '.':
        desc_toks += line.split()
        line = input()

    total_points = 0
    for tk in desc_toks:
        if tk in points:
            total_points += points[tk]

    print(total_points)
