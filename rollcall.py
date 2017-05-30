import sys
from collections import defaultdict

first_name_count = defaultdict(int)
names_l_f = []
for line in sys.stdin.readlines():
    f, l = line.split()
    first_name_count[f] += 1
    names_l_f.append((l, f))

for l, f in sorted(names_l_f):
    if first_name_count[f] > 1:
        print(f, l)
    else:
        print(f)

