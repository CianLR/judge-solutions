import sys
from collections import Counter

boxes = [Counter(x.strip()) for x in sys.stdin.readlines()]
twos = 0
threes = 0
for c in boxes:
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1

print(twos * threes)

