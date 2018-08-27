import sys
from cmath import polar

def diverges(point, iters):
    p = 0j
    for _ in range(iters):
        p = (p ** 2) + point
        if polar(p)[0] > 2:
            return True
    return False

def main():
    for i, line in enumerate(sys.stdin.readlines()):
        x, y, r = line.split()
        print("Case {}:".format(i + 1),
              "OUT" if diverges(complex(float(x), float(y)), int(r)) else "IN")

if __name__ == '__main__':
    main()
