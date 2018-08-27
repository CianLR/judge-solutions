
N = int(input())
seq = [int(x) for x in input().split()]

gis = [seq[0]]
for g in seq[1:]:
    if g > gis[-1]:
        gis.append(g)

print(len(gis))
print(*gis)

