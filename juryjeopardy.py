# ESWN

forwards = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

N = int(input())
print(N)
for _ in range(N):
    instrs = input()
    visited = {(0, 0)}
    cur_x = cur_y = 0
    direction = 0
    for ins in instrs:
        if ins == 'L':
            direction = (direction - 1) % 4
        elif ins == 'R':
            direction = (direction + 1) % 4
        elif ins == 'B':
            direction = (direction + 2) % 4

        cur_x += forwards[direction][0]
        cur_y += forwards[direction][1]
        visited.add((cur_x, cur_y))

    max_x = max(visited, key=lambda t: t[0])[0]
    min_x = min(visited, key=lambda t: t[0])[0]
    max_y = max(visited, key=lambda t: t[1])[1]
    min_y = min(visited, key=lambda t: t[1])[1]
    W, H = max_x - min_x + 2, max_y - min_y + 3
    print(H, W)

    offset_x = 0#1 - min_x
    offset_y = 1 - min_y
    grid = [['#'] * W for _ in range(H)]
    for x, y in visited:
        grid[y + offset_y][x + offset_x] = '.'

    for line in grid:
        print(''.join(line))
