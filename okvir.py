M, N = map(int, input().split())
U, L, R, D = map(int, input().split())

rows = [input() for _ in range(M)]

overall_width = N + L + R

for i in range(U):
    if i % 2 == 0:
        print('#.'*(overall_width // 2) + '#'*(overall_width % 2))
    else:
        print('.#'*(overall_width // 2) + '.'*(overall_width % 2))

for i in range(U, M + U):
    if i % 2 == 0:
        for j in range(L):
            if j % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print(rows[i - U], end='')
        for j in range(L + N, L + N + R):
            if j % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
    else:
        for j in range(L):
            if j % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
        print(rows[i - U], end='')
        for j in range(L + N, L + N + R):
            if j % 2 == 0:
                print('.', end='')
            else:
                print('#', end='')
    print()

for i in range(U + M, U + M + D):
    if i % 2 == 0:
        print('#.'*(overall_width // 2) + '#'*(overall_width % 2))
    else:
        print('.#'*(overall_width // 2) + '.'*(overall_width % 2))

