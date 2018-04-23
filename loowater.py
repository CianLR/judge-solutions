from sys import stdin

def main():
    N, M = (int(x) for x in stdin.readline().split())
    while N or M:
        heads = sorted([int(stdin.readline()) for _ in xrange(N)])
        knights = sorted([int(stdin.readline()) for _ in xrange(M)])
        hi = ki = cost = 0
        while hi < N and ki < M:
            if heads[hi] <= knights[ki]:
                cost += knights[ki]
                hi += 1
            ki += 1
        if hi == N:
            print cost
        else:
            print "Loowater is doomed!"

        N, M = (int(x) for x in stdin.readline().split())

if __name__ == '__main__':
    main()

