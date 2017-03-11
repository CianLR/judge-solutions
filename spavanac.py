H, M = map(int, input().split())
print((H - (M < 45))%24, (M - 45)%60)