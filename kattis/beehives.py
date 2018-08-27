def dist_within_n(n, p1, p2):
    return n >= ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

D, N = input().split()
while D != '0.0' or N != '0':
    D, N = float(D), int(N)
    hives = []
    for _ in range(N):
        x, y = map(float, input().split())
        hives.append((x, y))

    sour = [False for _  in range(N)]
    for i in range(N):
        for j in range(i):
            if dist_within_n(D, hives[i], hives[j]):
                sour[i] = sour[j] = True

    tot_sour = sour.count(True)
    print(tot_sour, "sour,", N - tot_sour, "sweet")

    D, N = input().split()

