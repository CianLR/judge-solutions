LEFT = 0
RIGHT = 1

P = int(input())
for _ in range(P):
    K, frac = input().split()
    p, q = map(int, frac.split('/'))

    path = []
    while p != 1 or q != 1:
        if p/q > 1:
            p = p - q
            path.append(RIGHT)
        else:
            q = q - p
            path.append(LEFT)

    line_start = 2**len(path)
    line_end = 2*line_start - 1
    for direc in path[::-1]:
        mid = (line_start + line_end) // 2
        if direc == LEFT:
            line_end = mid
        else:
            line_start = mid

    print(K, line_end)
