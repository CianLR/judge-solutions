from math import log

K = int(input())

largest_pow = 1
while largest_pow < K:
    largest_pow *= 2

constit_pows = set()
div = largest_pow
k = K
while k > 0:
    if div <= k:
        constit_pows.add(div)
        k -= div
    div //= 2

breaks = int(log(largest_pow, 2) - log(min(constit_pows), 2))
print(largest_pow, breaks)
