K = int(input())

largest_pow = 1
while largest_pow < K:
    largest_pow *= 2

constit_pows = set()
div = largest_pow
k = K
while k > 0:
    if div > k:
        div //= 2
    else:
        constit_pows.add(div)
        k -= div

breaks = 0
pieces = set([largest_pow])
while not constit_pows.issubset(pieces):
    small = min(pieces)
    pieces.add(small)
    pieces.add(small//2)
    breaks += 1

print(largest_pow, breaks)
