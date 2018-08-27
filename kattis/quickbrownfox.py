N = int(input())
alpha = set('abcdefghijklmnopqrstuvwxyz')
for _ in range(N):
    s = set(input().lower())
    missing = alpha - s
    if missing:
        print('missing', ''.join(sorted(missing)))
    else:
        print('pangram')
