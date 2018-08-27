import heapq
from collections import deque

EVENT_LEAVE  = 0
EVENT_ARRIVE = 1
EVENT_LOCK   = 2

def count_unlocks(N, M, times):
    events = [(t, EVENT_ARRIVE, s) for t, s in times]
    heapq.heapify(events)
    usage_end = []
    computers_locked = deque()
    computers_free = deque()
    unlocks = 0
    while events:
        t, e, x = heapq.heappop(events)
        if e == EVENT_LEAVE:
            computers_free.append(x)
            heapq.heappush(events, (t + M, EVENT_LOCK, x))
        elif e == EVENT_ARRIVE:
            if not computers_free and not computers_locked:
                computers_locked.append(len(usage_end))
                usage_end.append(-M)
            if not computers_free:
                computers_free.append(computers_locked.pop())
                unlocks += 1
            c = computers_free.popleft()
            usage_end[c] = t + x
            heapq.heappush(events, (t + x, EVENT_LEAVE, c))
        else:  # EVENT_LOCK
            if usage_end[x] == t - M:
                computers_locked.append(x)
                assert computers_free.popleft() == x
    return N - unlocks


def main():
    N, M = (int(x) for x in input().split())
    times = [tuple(int(x) for x in input().split()) for _ in range(N)]
    print(count_unlocks(N, M, times))

if __name__ == '__main__':
    main()

