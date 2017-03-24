N = int(input())
for _ in range(N):
    D, C, H, M = input().split()
    C, H, M = int(C), int(H), int(M)

    if D == 'B':
        C *= -1

    h_diff, m = divmod(M + C, 60)
    h = (H + h_diff) % 24

    print(h, m)
