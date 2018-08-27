from math import sin, cos, pi

N = int(input())

for _ in range(N):
    v, the, x, h1, h2 = map(float, input().split())
    t = x / (v * cos(the * pi / 180))
    y = (v * t * sin(the * pi / 180)) - (0.5 * 9.81 * (t ** 2))
    if h1 + 1 <= y <= h2 - 1:
        print("Safe")
    else:
        print("Not Safe")
