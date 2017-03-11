from math import pi

r, m, c = map(float, input().split())
while r or m or c:
    true_area = pi * r ** 2
    expr_area = (c / m) * ((r * 2) ** 2)
    print(true_area, expr_area)

    r, m, c = map(float, input().split())
