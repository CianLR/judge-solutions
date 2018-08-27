from random import randint

class Line:
    def __init__(self, p1, p2):
        self.a, self.b, self.c = self.abc_from_points(p1, p2)
        self.x_bound = (min(p1[0], p2[0]), max(p1[0], p2[0]))
        self.y_bound = (min(p1[1], p2[1]), max(p1[1], p2[1]))

    def __repr__(self):
        return "<a: {}, b: {}, c: {}>".format(self.a, self.b, self.c)

    def on_line(self, point):
        x, y = point
        return abs((self.a * x) + (self.b * y) - self.c) < 1e-9

    def intersects(self, other):
        det = (self.a * other.b) - (other.a * self.b)
        if det == 0:
            return False
        x = ((other.b * self.c) - (self.b * other.c)) / det
        y = ((self.a * other.c) - (other.a * self.c)) / det
        return (self.x_bound[0] <= x <= self.x_bound[1] and
                self.y_bound[0] <= y <= self.y_bound[1] and
                other.x_bound[0] <= x <= other.x_bound[1] and
                other.y_bound[0] <= y <= other.y_bound[1])

    @staticmethod
    def abc_from_points(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        a = y2 - y1
        b = x1 - x2
        return a, b, (a * x1) + (b * y1)

def generate_lines(poly):
    lines = []
    for p1, p2 in zip(poly, poly[1:] + [poly[0]]):
        lines.append(Line(p1, p2))
    return lines

def check_contains(lines, point):
    intersections = 0
    test_line = Line(point, (randint(30000, 90000),
                             randint(30000, 90000)))
    for l in lines:
        if test_line.intersects(l):
            if l.on_line(point):
                return "on"
            intersections += 1
    return "in" if intersections % 2 else "out"

def main():
    N = int(input())
    while N > 0:
        poly = [tuple(int(x) for x in input().split()) for _ in range(N)]
        lines = generate_lines(poly)
        M = int(input())
        for _ in range(M):
            x, y = input().split()
            print(check_contains(lines, (int(x), int(y))))
        N = int(input())


if __name__ == '__main__':
    main()
