T = int(input())

for _ in range(T):
    Is = [int(p) for p in input().split()]
    points = [(Is[i], Is[i+1]) for i in range(1, (Is[0] * 2) + 1, 2)]
    
    area = 0
    anch_x, anch_y = points[0]
    for p1, p2 in zip(points[1:], points[2:]):
        a, b, c, d = p1[0] - anch_x, p1[1] - anch_y, p2[0] - anch_x, p2[1] - anch_y
        area += abs(a*d - b*c) / 2
    print(area)
