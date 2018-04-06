
def tup_sub(a, b):
    return tuple(x - y for x, y in zip(a, b))

def cross_product(a, b):
    return (
            (a[1] * b[2]) - (a[2] * b[1]),
            (a[2] * b[0]) - (a[0] * b[2]),
            (a[0] * b[1]) - (a[1] * b[0]))

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def tetrahedron_area(a, b, c, d):
    a = tup_sub(a, d)
    b = tup_sub(b, d)
    c = tup_sub(c, d)
    return abs(dot_product(a, cross_product(b, c))) / 6

class Polygon:
    def __init__(self, v, verts):
        self.v = v
        self.verts = list(zip(verts[::3], verts[1::3], verts[2::3]))
        self.center = (sum(verts[::3]) / v,
                       sum(verts[1::3]) / v,
                       sum(verts[2::3]) / v)
    
    def wedge_area(self, peak):
        area = 0
        a = self.verts[0]
        for b, c in zip(self.verts[1:], self.verts[2:]):
            area += tetrahedron_area(a, b, c, peak)
        return area

def get_center(polygons):
    return tuple(sum(c) / len(polygons) for c in zip(*(p.center for p in polygons)))

def main():
    N = int(input())
    area = 0
    for _ in range(N):
        F = int(input())
        polygons = []
        for _ in range(F):
            V, *verts = (float(x) for x in input().split())
            polygons.append(Polygon(int(V), verts))
        
        center = get_center(polygons)
        area += sum(p.wedge_area(center) for p in polygons)
    print("{:.2f}".format(area))

if __name__ == '__main__':
    main()

