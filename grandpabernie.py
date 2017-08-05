from collections import defaultdict

N = int(input())

countries = defaultdict(list)
for _ in range(N):
    c, y = input().split()
    countries[c].append(int(y))

for cn in countries:
    countries[cn] = sorted(countries[cn])

K = int(input())
for _ in range(K):
    c, time = input().split()
    print(countries[c][int(time) - 1])

