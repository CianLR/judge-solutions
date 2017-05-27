from collections import defaultdict

M, N = map(int, input().split())

x_to_y = defaultdict(list)
for _ in range(M):
    a, b = input().split()
    x_to_y[a].append(b)


def a_find_b(a, b, _seen=None):
    if not _seen:
        _seen = set()

    # print("Checking", a, "->", b)
    _seen.add(a)
    if a == b:
        return True
    for c in x_to_y[a]:
        if c not in _seen and a_find_b(c, b, _seen):
            return True
    return False

for _ in range(N):
    A, B = input().split()
    if len(A) != len(B):
        print('no')
        continue
    for a, b in zip(A, B):
        if not a_find_b(a, b):
            print('no')
            break
    else:
        print('yes')
