
def direc(p, q, r):
    return (((q.imag - p.imag) * (r.real - p.real)) -
            ((q.real - p.real) * (r.imag - p.imag)))

def get_hulls(points):
    pts = sorted(points, key=lambda p: (p.real, p.imag))
    upper = []
    lower = []
    for p in pts:
        while len(upper) > 1 and direc(upper[-2], upper[-1], p) < 0:
            upper.pop()
        while len(lower) > 1 and direc(lower[-2], lower[-1], p) > 0:
            lower.pop()
        lower.append(p)
        upper.append(p)
    return upper, lower

def main():
    N = int(input())
    points = []
    for i in range(N):
        x, y, h = input().split()
        if h == 'Y':
            points.append(complex(int(x), int(y)))
    upper, lower = get_hulls(points)
    
    assert len(points) == len(upper) + len(lower) - 2

    print(len(upper) + len(lower) - 2)
    for p in lower + upper[1:-1][::-1]:
        print(int(p.real), int(p.imag))

if __name__ == '__main__':
    main()

