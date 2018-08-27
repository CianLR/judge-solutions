import heapq
from collections import Counter

def pack(N, bags):
    pbags = [[] for _ in xrange(max(Counter(bags).values()))]
    b = 0
    for i in bags:
        pbags[b].append(i)
        b = (b + 1) % len(pbags)
    return pbags

def main():
    N = int(raw_input())
    while N != 0:
        bags = sorted((int(x) for x in raw_input().split()), reverse=True)
        packed = pack(N, bags)
        print len(packed)
        for b in packed:
            print ' '.join(map(str, b))
        N = int(raw_input())

if __name__ == '__main__':
    main()

