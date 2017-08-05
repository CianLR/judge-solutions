import sys

for line in sys.stdin.readlines():
    a, b = map(int, line.split())
    print(abs(a - b))

