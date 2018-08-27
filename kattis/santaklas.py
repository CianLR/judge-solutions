from math import floor, sin, pi

H, A = [int(x) for x in input().split()]
if A <= 180:
    print("safe")
else:
    print(floor(H / sin((A - 180) * pi / 180)))

