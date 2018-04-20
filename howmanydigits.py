from math import log, floor
from sys import stdin

MAX = 1000001

def gen_fac_lens(N):
    last = 1
    lens = [None] * N
    lens[0] = 1
    for i in xrange(1, N):
        last += log(i, 10)
        lens[i] = int(floor(last))
    return lens

def main():
    fac_lens = gen_fac_lens(MAX)
    for line in stdin.readlines():
        f = int(line)
        print fac_lens[f]

if __name__ == '__main__':
    main()


