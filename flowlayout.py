M = int(input())
while M:
    rects = []
    w, h = map(int, input().split())
    while w > 0 and h > 0:
        rects.append((w, h))
        w, h = map(int, input().split())

    max_w = [0]
    tot_h = 0
    max_h = 0
    for w, h in rects:
        if max_w[-1] + w > M:
            max_w.append(0)
            tot_h += max_h
            max_h = 0
        max_w[-1] += w
        max_h = max(max_h, h)
    tot_h += max_h
    print(max(max_w), 'x', tot_h)

    M = int(input())
