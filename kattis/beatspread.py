T = int(input())
for _ in range(T):
    S, D = map(int, input().split())

    n = (S - D) / 2
    n2 = n + D

    if n >= 0 and n2 >= 0 and n%1 == 0:
        print(*sorted(map(int, (n, n2)), reverse=True))
    else:
        print("impossible")
