
TURTLE_MOVES = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
]

def pt_sum(a, b):
    return a[0] + b[0], a[1] + b[1]

def turn_left(angle):
    return (angle - 1) % 4

def turn_right(angle):
    return (angle + 1) % 4

def get_next(loc, angle):
    return pt_sum(loc, TURTLE_MOVES[angle])

def on_board(point):
    return 0 <= point[0] < 8 and 0 <= point[1] < 8

def simulate(board, prog):
    turtle_loc = (7, 0)
    turtle_dir = 0
    for command in prog:
        if command == 'R':
            turtle_dir = turn_right(turtle_dir)
        elif command == 'L':
            turtle_dir = turn_left(turtle_dir)
        elif command == 'X':
            laser_loc = get_next(turtle_loc, turtle_dir)
            if not on_board(laser_loc):
                return False
            if board[laser_loc[0]][laser_loc[1]] != 'I':
                return False
            board[laser_loc[0]][laser_loc[1]] = '.'
        elif command == 'F':
            nxt = get_next(turtle_loc, turtle_dir)
            if not on_board(nxt):
                return False
            if board[nxt[0]][nxt[1]] not in '.D':
                return False
            turtle_loc = nxt
        else:
            return False
    return board[turtle_loc[0]][turtle_loc[1]] == 'D'


def main():
    # grid[h][w]
    grid = [list(input()) for _ in range(8)]
    grid[7][0] = '.'
    prog = input()
    print("Diamond!" if simulate(grid, prog) else "Bug!")

if __name__ == '__main__':
    main()

