from sys import stdin
from math import pi

def intergrate(poly):
    inter = [0]
    for i, p in enumerate(poly):
        inter.append(p / (i + 1))
    return inter

def square(poly):
    newpoly = [0] * (len(poly) * 2)
    for i, p in enumerate(poly):
        for j, q in enumerate(poly):
            newpoly[i + j] += p * q
    return newpoly

def mul(poly, c):
    return [p * c for p in poly]

def f(poly, x):
    a = 0
    for i, p in enumerate(poly):
        a += p * (x ** i)
    return a

def binsearch(poly, lo, hi, target, tol=0.001):
    bottom = lo
    v = float('infinity')
    mid = None
    while abs(v - target) > tol:
        mid = (hi + lo) / 2
        v = f(poly, mid) - f(poly, bottom)
        if v > target:
            hi = mid
        else:
            lo = mid
    return mid

def get_inc_heights(poly, top, bottom, inc):
    inter = intergrate(mul(square(poly), pi))
    volume = f(inter, top) - f(inter, bottom)
    target = inc
    heights = []
    while target < volume and len(heights) < 8:
        heights.append(binsearch(inter, bottom, top, target) - bottom)
        target += inc
    return volume, heights

def main():
    N = stdin.readline()
    case = 1
    while N.strip():
        N = int(N) + 1
        poly = [float(x) for x in stdin.readline().split()]
        bottom, top, inc = (float(x) for x in stdin.readline().split())
        
        vol, heights = get_inc_heights(poly, top, bottom, inc)
        print("Case {}: {:.2f}".format(case, vol))
        if heights:
            print(' '.join(map('{:.2f}'.format, heights)))
        else:
            print("insufficient volume")

        

        case += 1
        N = stdin.readline()


if __name__ == '__main__':
    main()

