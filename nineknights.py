

kmove = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

def check_ok(board, x, y):
    for a, b in [(x + a, y + b) for a, b in kmove]:
        if 0 <= a < 5 and 0 <= b < 5 and board[a][b] == 'k':
            return False
    return True


def main():
    board = [input() for _ in range(5)]
    ks = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] != 'k':
                continue
            ks += 1
            if not check_ok(board, i, j):
                print("invalid")
                return
    print("valid" if ks == 9 else "invalid")

if __name__ == '__main__':
    main()

