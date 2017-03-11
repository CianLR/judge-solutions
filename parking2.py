from math import ceil, floor

T = int(input())
for _ in range(T):
    S = int(input())
    shops = [int(x) for x in input().split()]
    spread = max(shops) - min(shops)
    print(spread * 2)
