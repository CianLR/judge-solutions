from math import ceil

B, K, G = map(int, input().split())
print(ceil((B - 1) / (K // G)))

