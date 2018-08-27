
T = int(input())
for _ in range(T):
    X, Y = [int(x) for x in input().split()]
    first = (X + Y) / 6
    second = ((X**2 + Y**2 - X*Y) ** 0.5) / 6
    h = first + second
    if not 0 < h < min(X, Y) / 2:
        h = first - second
    print(h * (X - 2*h) * (Y - 2*h))

