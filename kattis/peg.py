
board = [input() for _ in range(7)]

def is_on_board(r, c):
    if 2 <= c <= 4:
        return 0 <= r <= 6
    elif 0 <= c <= 6:
        return 2 <= r <= 4
    return False

valid_moves = 0
for i in range(7):
    for j in range(7):
        if board[i][j] != 'o':
            continue
        if is_on_board(i + 2, j):
            valid_moves += board[i+1][j] == 'o' and board[i+2][j] == '.'
        if is_on_board(i - 2, j):
            valid_moves += board[i-1][j] == 'o' and board[i-2][j] == '.'
        if is_on_board(i, j + 2):
            valid_moves += board[i][j+1] == 'o' and board[i][j+2] == '.'
        if is_on_board(i, j - 2):
            valid_moves += board[i][j-1] == 'o' and board[i][j-2] == '.'

print(valid_moves)
