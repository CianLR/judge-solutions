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

def best_min(guard):
    return max((x, i) for i, x in enumerate(guard))

def main():
    events = sorted(map(parse_event, sys.stdin.readlines()))
    guard_sleep = defaultdict(lambda: [0] * 60)
    cur_guard = None
    sleep_min = None
    for e in events:
        if e.type == E.CHANGE:
            cur_guard = e.var
        elif e.type == E.ASLEEP:
            sleep_min = e.time[-1]
        elif e.type == E.WAKE:
            for m in range(sleep_min, e.time[-1]):
                guard_sleep[cur_guard][m] += 1
    
    (_, minute), g = max((best_min(guard_sleep[g]), g) for g in guard_sleep)
    print(g * minute)

if __name__ == '__main__':
    main()

