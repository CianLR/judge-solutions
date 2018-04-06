from math import ceil

inf = float('infinity')

MEMO = {0: 0, 1: 0}
def opt_print(lines, r, p):
    if lines in MEMO:
        return MEMO[lines]
    best_time = inf
    for k in xrange(1, lines):
        t = (p * k) + opt_print(int(ceil(lines / (k + 1.0))), r, p)
        if t < best_time:
            best_time = t
    MEMO[lines] = best_time + r
    return best_time + r

def main():
    N, R, P = (int(x) for x in raw_input().split())
    print opt_print(N, R, P)

if __name__ == '__main__':
    main()

