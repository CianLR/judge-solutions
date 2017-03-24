turns = {
    '/': {
        'U': 'R',
        'D': 'L',
        'R': 'U',
        'L': 'D'
    },
    '\\': {
        'U': 'L',
        'D': 'R',
        'R': 'D',
        'L': 'U'
    }
}

case_no = 0
C, R = map(int, input().split())
while C or R:
    case_no += 1
    print("HOUSE", case_no)

    entrance = None
    direct = None
    grid = []
    for r in range(R):
        l = input()
        if '*' in l:
            entrance = (r, l.find('*'))
            if r == 0:
                direct = 'D'
            elif r + 1 == R:
                direct = 'U'
            elif entrance[1] == 0:
                direct = 'R'
            else:
                direct = 'L'
        grid.append(l)

    r, c = entrance
    while grid[r][c] != 'x':
        if direct == 'R':
            c += 1
        elif direct == 'L':
            c -= 1
        elif direct == 'U':
            r -= 1
        else:
            r += 1
        if grid[r][c] in turns:
            direct = turns[grid[r][c]][direct]

    for i in range(R):
        for j in range(C):
            if i == r and j == c:
                print('&', end='')
            else:
                print(grid[i][j], end='')
        print()


    C, R = map(int, input().split())
