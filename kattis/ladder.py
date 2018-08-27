from math import sin, pi, ceil

O, A = map(int, input().split())
rA = A * (pi/180)
print(ceil(O/sin(rA)))

