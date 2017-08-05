N, K = map(int, input().split())
tree = [0] * (N + 1)
is_set = [False] * (N + 1)

def lsb(x):
    return x & -x

def flip(i):
    mod = -1 if is_set[i] else 1
    is_set[i] = not is_set[i]
    while i <= N:
        tree[i] += mod
        i += lsb(i)

def sum_to_i(i):
    tot = 0
    while i > 0:
        tot += tree[i]
        i -= lsb(i)
    return tot

def range_sum(i, j):
    return sum_to_i(j) - sum_to_i(i - 1)

for _ in range(K):
    t, *args = input().split()
    if t == 'F':
        flip(int(args[0]))
    else:
        print(range_sum(int(args[0]), int(args[1])))

