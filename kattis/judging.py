from collections import defaultdict

N = int(input())

dom = defaultdict(int)
for _ in range(N):
    dom[input()] += 1

kattis = defaultdict(int)
for _ in range(N):
    kattis[input()] += 1

crossover = 0
for res in min([kattis, dom], key=len):
    crossover += min(kattis[res], dom[res])

print(crossover)

