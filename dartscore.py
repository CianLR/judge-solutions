from math import ceil

T = int(input())
for _ in range(T):
    N = int(input())
    points = 0
    for _ in range(N):
        x, y = map(int, input().split())
        dist = (x**2 + y**2)**0.5
        ring = ceil(dist / 20)
        if ring == 0:
            ring = 1
        points += max(0, 11 - ring)
    print(points)
