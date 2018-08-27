from collections import defaultdict
from math import factorial
import sys

for line in sys.stdin.read().split('\n'):
    if not line:
        continue
    char_count = defaultdict(int)
    for c in line:
        char_count[c] += 1

    total_perms = factorial(len(line))
    repititions = 1
    for c in char_count:
        repititions *= factorial(char_count[c])
    print(total_perms // repititions)

