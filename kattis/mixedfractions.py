N, D = map(int, input().split())
while N and D:
    whole = N // D
    numer = N % D

    print(whole, numer, '/', D)

    N, D = map(int, input().split())
