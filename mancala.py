
def get_boards(n):
    boards = [()]
    b = []
    for _ in range(n):
        z = -1
        if 0 in b:
            z = b.index(0)
        else:
            z = len(b)
            b.append(0)
        b[z] = z + 1
        for i in range(z):
            b[i] -= 1
        boards.append(tuple(b))
    return boards

BOARDS = get_boards(2001)

def print_board(b):
    for i in range((len(b) // 10) + 1):
        print(*b[(i * 10):((i + 1) * 10)])

def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        board = BOARDS[N]
        print(K, len(board))
        print_board(board)

if __name__ == '__main__':
    main()

