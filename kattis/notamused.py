import sys
from collections import defaultdict

day = 0
total_mins = defaultdict(int)
entered_park = {}
for line in sys.stdin.readlines():
    line = line.strip()
    if line == 'OPEN':
        day += 1
        total_mins = defaultdict(int)
        entered_park = {}
        continue
    elif line == 'CLOSE':
        print("Day", day)
        for person in sorted(total_mins):
            print(person, "${:.2f}".format(total_mins[person] * 0.1))
        print()
        continue

    direc, person, time = line.split()
    if direc == 'ENTER':
        entered_park[person] = int(time)
    else:
        total_mins[person] += int(time) - entered_park[person]



