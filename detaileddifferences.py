N = int(input())
for _ in range(N):
    A = input()
    B = input()
    print(A)
    print(B)
    for a, b in zip(A, B):
        if a == b:
            print(".", end='')
        else:
            print("*", end='')
    print('\n')
