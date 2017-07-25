
def point_dist_sq(a, b):
    return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)

def point_add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def point_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))
c = tuple(map(int, input().split()))
pts = [a, b, c]

p = c1 = c2 = None
for i in range(3):
    p = pts[i]
    c1, c2 = pts[:i] + pts[i + 1:]
    if point_dist_sq(p, c1) == point_dist_sq(p, c2):
        break

print(*point_add(point_add(point_sub(c1, p), point_sub(c2,p)), p))

