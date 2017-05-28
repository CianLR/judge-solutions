import sys

for line in sys.stdin.readlines():
    n = int(line)
    print(n + max(0, n - 2))
