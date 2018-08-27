needed = [1, 1, 2, 2, 2, 8]
have = map(int, input().split())
mod = [str(n - h) for n, h in zip(needed, have)]
print(' '.join(mod))