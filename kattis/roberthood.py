
def dist(p, q):
    c = p - q
    return ((c * c.conjugate()) ** 0.5).real

def weird_magic(u1, u2, l1, l2):
    return ((u2.imag - u1.imag) * (l1.real - l2.real) >
            (u2.real - u1.real) * (l1.imag - l2.imag))

def direc(p, q, r):
    return (((q.imag - p.imag) * (r.real - p.real)) -
            ((q.real - p.real) * (r.imag - p.imag)))

def get_hulls(points):
    pts = sorted(points, key=lambda p: (p.real, p.imag))
    upper = []
    lower = []
    for p in pts:
        while len(upper) > 1 and direc(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        while len(lower) > 1 and direc(lower[-2], lower[-1], p) >= 0:
            lower.pop()
        lower.append(p)
        upper.append(p)
    return upper, lower

def main():
    N = int(input())
    points = [None] * N
    for i in range(N):
        x, y = input().split()
        points[i] = complex(int(x), int(y))
    upper, lower = get_hulls(points)
    
    max_dist = 0
    up = 0
    lo = len(lower) - 1
    while up < len(upper) - 1 or lo > 0:
        max_dist = max(max_dist, dist(upper[up], lower[lo]))
        if up == len(upper) - 1:
            lo -= 1
        elif lo == 0:
            up += 1
        elif weird_magic(upper[up], upper[up + 1], lower[lo], lower[lo - 1]):
            up += 1
        else:
            lo -= 1
    print(max_dist)

if __name__ == '__main__':
    main()

