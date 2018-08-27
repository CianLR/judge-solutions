from math import pi, sin, cos

T = int(input())
for _ in range(T):
    M = int(input())
    ang, x, y = pi/2, 0, 0
    for _ in range(M):
        angle, dist = map(float, input().split())
        ang += angle * pi/180
        x += cos(ang) * dist
        y += sin(ang) * dist
    print(x, y)
