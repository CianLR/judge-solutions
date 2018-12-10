import sys
from collections import defaultdict

class E:
    
    CHANGE = 0
    ASLEEP = 1
    WAKE = 2

    def __init__(self, time, line):
        self.time = time
        self.var = None
        if line.startswith('Guard'):
            self.type = self.CHANGE
            self.var = int(line.split()[1][1:])
        elif line.startswith('falls'):
            self.type = self.ASLEEP
        else:
            self.type = self.WAKE

    def __lt__(self, other):
        return self.time < other.time

def parse_event(line):
    y, t, rest = line.split(' ', 2)
    d = y[1:].split('-') + t[:-1].split(':')
    return E(tuple(map(int, d)), rest)

def main():
    events = sorted(map(parse_event, sys.stdin.readlines()))
    guard_sleep = defaultdict(int)
    guard_intervals = defaultdict(list)
    cur_guard = None
    sleep_min = None
    for e in events:
        if e.type == E.CHANGE:
            cur_guard = e.var
        elif e.type == E.ASLEEP:
            sleep_min = e.time[-1]
        elif e.type == E.WAKE:
            guard_sleep[cur_guard] += e.time[-1] - sleep_min
            guard_intervals[cur_guard].append((sleep_min, e.time[-1]))
    sleep_g = max(guard_sleep, key=lambda g: guard_sleep[g])
    mins = [0] * 60
    for s, e in guard_intervals[sleep_g]:
        for m in range(s, e):
            mins[m] += 1
    best_min = max(range(60), key=lambda m: mins[m])
    print(sleep_g * best_min)

if __name__ == '__main__':
    main()

