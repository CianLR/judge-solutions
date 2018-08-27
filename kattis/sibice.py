N, W, H = map(int, input().split())

m = (W**2 + H**2)**0.5
for _ in range(N):
    if int(input()) <= m:
        print("DA")
    else:
        print("NE")
