import sys

*hs, t1, t2 = [int(i) for i in input().split()]

tower1 = None

for i, h1 in enumerate(hs):
    for j, h2 in enumerate(hs[i+1:]):
        h3 = t1 - h1 - h2
        if h3 == h1 or h3 == h2:
            continue
        if h3 in hs:
            tower1 = [h1, h2, h3]
            break
    if tower1:
        break

print(
    *sorted(tower1, reverse=True),
    *sorted([x for x in hs if x not in tower1], reverse=True))
        
