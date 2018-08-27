from itertools import permutations

n = int(input())
smallest = None
for p in permutations(str(n)):
    p = int(''.join(p))
    if p > n:
        if smallest is None:
            smallest = p
        smallest = min(smallest, p)

print(smallest if smallest is not None else 0)
