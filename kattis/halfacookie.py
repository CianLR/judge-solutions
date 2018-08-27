import sys
from math import acos, pi

for line in sys.stdin.readlines():
    r, x, y = map(float, line.split())

    h = (x**2 + y**2)**0.5
    if h >= r:
        print("miss")
    else:
        print("Radius", r)
        print("Seg height", h)
        seg_area = (r**2)*acos((r - h) / r) - (r - h)*((2*r*h - h**2)**0.5)
        overall_area = pi * r**2
        print(overall_area - seg_area, seg_area)
