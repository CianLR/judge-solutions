from math import ceil

N = int(input())

s = ceil(N ** (1 / 9))
while s != 1:
    if N % (s ** 9) == 0:
        break
    s -= 1
print(s)

