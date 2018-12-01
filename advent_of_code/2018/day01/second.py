import sys

diffs = [int(x.strip()) for x in sys.stdin.readlines()]
point = 0
i = 0
seen = set()
while point not in seen:
    seen.add(point)
    point += diffs[i]
    i = (i + 1) % len(diffs)
print(point)

