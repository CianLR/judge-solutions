from collections import deque
from sys import stdin
import heapq

class LIFO:
    
    TYPE = 'stack'

    def __init__(self):
        self.q = deque()

    def add(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.pop() if self.q else None

class FIFO:

    TYPE = 'queue'

    def __init__(self):
        self.q = deque()

    def add(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.popleft() if self.q else None

class PQ:

    TYPE = 'priority queue'

    def __init__(self):
        self.q = []

    def add(self, x):
        heapq.heappush(self.q, -x)

    def pop(self):
        return -heapq.heappop(self.q) if self.q else None

def guess_ds(N, cmds):
    ds = [LIFO(), FIFO(), PQ()]
    for t, x in cmds:
        for i in range(len(ds) - 1, -1, -1):
            if t == 1:
                ds[i].add(x)
            else:
                if ds[i].pop() != x:
                    del ds[i]
    if len(ds) == 0:
        return 'impossible'
    elif len(ds) == 1:
        return ds[0].TYPE
    return 'not sure'

def main():
    N = stdin.readline()
    while N.strip():
        N = int(N)
        cmds = [tuple(int(x) for x in stdin.readline().split()) for _ in range(N)]
        print(guess_ds(N, cmds))
        N = stdin.readline()

if __name__ == '__main__':
    main()
