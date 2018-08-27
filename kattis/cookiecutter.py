
def segments(pts):
    return zip(pts, pts[1:] + pts[:1])


def area(pts):
    return 0.5 * abs(sum((x[0] * y[1]) - (x[1] * y[0]) for x, y in segments(pts)))


def point_mul(p1, c):
    return p1[0] * c, p1[1] * c


def normalise(points):
    minx = min(x for x, y in points)
    miny = min(y for x, y in points)
    return [(x - minx, y - miny) for x, y in points]


def scale_polygon(points, scale):
    start_a = area(points)
    factor = scale / start_a
    scaled = [point_mul(p, factor ** 0.5) for p in points]
    return normalise(scaled)


def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(float, input().split())
        points.append((x, y))
    scale = int(input())
    for x, y in scale_polygon(points, scale):
        print(x, y)

if __name__ == '__main__':
    main()

