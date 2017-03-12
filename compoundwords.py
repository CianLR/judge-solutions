import sys
from itertools import permutations

words = []
for l in sys.stdin.readlines():
    words.extend(l.split())

unique_perms = set(''.join(w) for w in permutations(words, 2))
for w in sorted(unique_perms):
    print(w)
