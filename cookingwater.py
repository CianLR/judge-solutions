
def main():
    N = int(raw_input())
    possible = set(xrange(1001))
    for _ in xrange(N):
        a, b = (int(x) for x in raw_input().split())
        possible &= set(xrange(a, b + 1))
    if possible:
        print "gunilla has a point"
    else:
        print "edward is right"

if __name__ == '__main__':
    main()

