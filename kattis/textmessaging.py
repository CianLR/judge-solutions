from sys import stdin

def get_min_presses(K, presses):
    cost = 0
    for i, p in enumerate(sorted(presses, reverse=True)):
        cost += ((i / K) + 1) * p
    return cost

def main():
    T = int(stdin.readline())
    for t in xrange(1, T + 1):
        P, K, L = (int(x) for x in stdin.readline().split())
        presses = [int(x) for x in stdin.readline().split()]
        print "Case #{}: {}".format(t, get_min_presses(K, presses))

if __name__ == '__main__':
    main()

