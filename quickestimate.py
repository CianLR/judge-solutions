from math import log, floor

N = int(input())
for _ in range(N):
    e = int(input())
    if e == 0:
        print(1)
        continue
    l = floor(log(e, 10) + 1)
    print(int(l))
