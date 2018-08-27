
DIRS = {
    'up': (0, 1),
    'down': (0, -1),
    'left': (-1, 0),
    'right': (1, 0),
}

def step(p, d):
    return p[0] + d[0], p[1] + d[1]

def unstep(p, d):
    return p[0] - d[0], p[1] - d[1]

def new_board():
    board = {
        (i % 5, i // 5): l for i, l in enumerate('UVWXYPQRSTKLMNOFGHIJABCDE')
    }
    lookup = {l: p for p, l in board.items()}
    return board, lookup

def mutate_board(bl, instrs):
    board, lookup = bl
    for letter, direc in instrs:
        start = p = lookup[letter]
        while p in board:
            p = step(p, direc)
        while p != start:
            nxt = unstep(p, direc)
            board[p] = board[nxt]
            lookup[board[p]] = p
            p = nxt
        del board[p]
    return board, lookup

def print_board(bl):
    board = bl[0]
    min_x = min(p[0] for p in board)
    max_x = max(p[0] for p in board)
    min_y = min(p[1] for p in board)
    max_y = max(p[1] for p in board)
    for y in range(max_y, min_y - 1, -1):
        out = ''
        for x in range(min_x, max_x + 1):
            if (x, y) in board:
                out += board[(x, y)]
            else:
                out += ' '
        print(out.rstrip())
    print()

def main():
    N = int(input())
    while N != -1:
        instrs = []
        for _ in range(N):
            l, d = input().split()
            instrs.append((l, DIRS[d]))
        print_board(mutate_board(new_board(), instrs))
        N = int(input())

if __name__ == '__main__':
    main()

