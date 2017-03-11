l = input()
while l != '0':
    x1, y1, x2, y2, p = map(float, l.split())
    print((abs(x1 - x2)**p + abs(y1 - y2)**p)**(1/p))
    l = input()
