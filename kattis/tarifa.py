X = int(input())
N = int(input())

print(X * (N + 1) - sum(int(input()) for _ in range(N)))
