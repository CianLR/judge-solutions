

def is_valid(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            x_dif = queens[i][0] - queens[j][0]
            y_dif = queens[i][1] - queens[j][1]
            if abs(x_dif) == abs(y_dif) or not x_dif or not y_dif:
                return False
    return True


def main():
    N = int(input())
    queens = []
    for _ in range(N):
        x, y = map(int, input().split())
        queens.append((x, y))

    print('CORRECT' if is_valid(queens) else 'INCORRECT')


if __name__ == '__main__':
    main()
