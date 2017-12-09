
N = int(input())
unis = set()
for i in range(N):
    u, t = input().split()
    if u not in unis:
        print(u, t)
        unis.add(u)

    if len(unis) == 12:
        break

