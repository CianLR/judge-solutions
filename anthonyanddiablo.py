from math import pi

A, N = [float(x) for x in input().split()]

r = N / (2 * pi)
a = pi * (r ** 2)

if A <= a:
    print("Diablo is happy!")
else:
    print("Need more materials!")
