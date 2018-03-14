from math import radians, cos, sin

def rotation_vector(v):
    r = radians(-v)
    return complex(cos(r), sin(r))

def direction(a, b, c):
    return (((a.imag - c.imag) * (a.real - b.real)) -
            ((a.imag - b.imag) * (a.real - c.real)))

def convex_hull(points):
    points = sorted(points, key=lambda p: (p.real, p.imag))
    upper = []
    lower = []
    for p in points:
        while len(upper) > 1 and direction(upper[-2], upper[-1], p) >= 0:
            upper.pop()
        upper.append(p)
        while len(lower) > 1 and direction(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    return lower + upper[1:-1][::-1]

def triangle_area(a, b, c):
    b -= a
    c -= a
    return abs((b.real * c.imag) - (c.real * b.imag)) / 2

def convex_area(points):
    a, *pts = points
    area = 0
    for b, c in zip(points, points[1:]):
        area += triangle_area(a, b, c)
    return area

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        board_area = 0
        points = []
        for _ in range(N):
            x, y, w, h, v = [float(x) for x in input().split()]
            board_area += w * h
            center = complex(x, y)
            rotation = rotation_vector(v)
            height = (complex(0, h) * rotation) / 2
            width  = (complex(w, 0) * rotation) / 2
            for m in [height + width, height - width, -height + width, -height - width]:
                points.append(center + m)
            
        hull = convex_hull(points)
        hull_area = convex_area(hull)
        print('{:.1f} %'.format((board_area * 100) / hull_area))


if __name__ == '__main__':
    main()

