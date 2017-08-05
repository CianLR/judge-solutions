from math import sin, cos, pi

N = int(input())
for _ in range(N):
    velo, theta, x1, h1, h2 = map(float, input().split())
    theta_rad = theta * (pi / 180)
    time = x1 / (velo * cos(theta_rad))
    y1 = (velo * time * sin(theta_rad)) - (0.5 * 9.81 * (time ** 2))
    if y1 - h1 >= 1 and h2 - y1 >= 1:
        print("Safe")
    else:
        print("Not Safe")


