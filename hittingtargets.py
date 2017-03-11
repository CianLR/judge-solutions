class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_hit(self, x, y):
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def is_hit(self, x, y):
        dist = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return dist <= self.r

shapes = {
    'circle': Circle,
    'rectangle': Rect,
}

M = int(input())
targets = []
for _ in range(M):
    t, *params = input().split()
    targets.append(
        shapes[t](*map(int, params))
    )

N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    hits = 0
    for t in targets:
        if t.is_hit(x, y):
            hits += 1
    print(hits)
