class Point:
    def __init__(self, i, x, y):
        self.i = i
        self.x = x
        self.y = y

    def dist_to(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5

N = int(input())
points = []
for i in range(N):
    x, y = map(float, input().split())
    points.append(Point(i, x, y))

used = set()
tour = [points[0]]
for _ in range(N - 1):
    curr_node = tour[-1]
    used.add(curr_node)

    unused = [p for p in points if p not in used]
    best = min(unused, key=lambda p: p.dist_to(curr_node))

    tour.append(best)

for p in tour:
    print(p.i)
