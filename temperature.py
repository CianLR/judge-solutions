P, M = map(int, input().split())
if M == 1 and P == 0:
    print("ALL GOOD")
elif M == 1:
    print("IMPOSSIBLE")
else:
    print(P/-(M - 1))
