
def convert_cords(c):
    return ord(c[0]) - ord('A'), int(c[1]) - 1

def can_move(a, b):
    return (a[0] % 2) ^ (a[1] % 2) == (b[0] % 2) ^ (b[1] % 2)

def can_reach(u):
    for xadd, yadd in ((-1, -1), (1, -1), (-1, 1), (1, 1)):
        x, y = u[0] + xadd, u[1] + yadd
        while 0 <= x < 8 and 0 <= y < 8:
            yield x, y
            x, y = x + xadd, y + yadd

def path(u, v):
    if u == v:
        return [u]
    nxt = list(can_reach(u))
    if v in nxt:
        return [u, v]
    for n in nxt:
        nnxt = list(can_reach(n))
        if v in nnxt:
            return [u, n, v]
    return []

def convert_back(a):
    return chr(a[0] + ord('A')) + ' ' + str(a[1] + 1)

def main():
    T = int(raw_input())
    for _ in xrange(T):
        a, b, c, d = raw_input().split()
        u, v = map(convert_cords, ((a, b), (c, d)))
        if not can_move(u, v):
            print "Impossible"
        else:
            p = [convert_back(k) for k in path(u, v)]
            print len(p) - 1, ' '.join(p)

if __name__ == '__main__':
    main()

