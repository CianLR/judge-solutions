import sys
from collections import defaultdict

def get_squares(tx, ty, w, h):
    for x in range(tx, tx + w):
        for y in range(ty, ty + h):
            yield x, y

def main():
    seen = defaultdict(int)
    squares = {}
    for line in sys.stdin.readlines():
        claim, _, t, d = line.split()
        tx, ty = t[:-1].split(',')
        w, h = d.split('x')
        squares[claim] = (int(tx), int(ty), int(w), int(h))
    for sq in squares.values():
        for p in get_squares(*sq):
            seen[p] += 1
    print(sum(1 for p in seen if seen[p] > 1))

if __name__ == '__main__':
    main()

