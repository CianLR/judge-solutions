R, N = map(int, input().split())
taken = {int(input()) for _ in range(N)}
for r in range(1, R + 1):
    if r not in taken:
        print(r)
        break
else:
    print("too late")
