T = int(input())
for _ in range(T):
    s = input()

    sq = 1
    while sq**2 < len(s):
        sq += 1
    M = sq ** 2

    # grid[row][column]
    grid = [['*']*sq for _ in range(sq)]
    for i, c in enumerate(s):
        row = i // sq
        col = i % sq
        grid[row][col] = c

    flipped = zip(*grid[::-1])
    for l in flipped:
        for c in l:
            if c != '*':
                print(c, end='')
    print()
