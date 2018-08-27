T = int(input())
for _ in range(T):
    K, N = map(int, input().split())

    n_even = N * (N + 1)
    n_pos = n_even // 2
    n_odd = n_even - N

    print(K, n_pos, n_odd, n_even)
