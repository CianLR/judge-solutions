from itertools import combinations

dvs = [int(input()) for _ in range(9)]
for selects in combinations(dvs, 7):
    if sum(selects) == 100:
        print('\n'.join([str(x) for x in selects]))
        break
