T = int(input())
for _  in range(T):
    s = input()
    width = int(len(s)**0.5)
    # grid[col][row]
    grid = [['']* width for _ in range(width)]
    for i, c in enumerate(s):
        row = i // width
        col = i % width
        grid[col][row] = c

    rot_grid = ''.join([''.join(col) for col in grid[::-1]])
    print(rot_grid)
