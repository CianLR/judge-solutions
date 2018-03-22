
def backtrack(n, holes, col=0, rows_filled=0, diag_filled=0, counter_diag_filled=0):
    if col == n:
        return 1
    count = 0
    for row in range(n):
        if ((row, col) not in holes and
            not rows_filled & (1 << row) and
            not diag_filled & (1 << (row + col)) and
            not counter_diag_filled & (1 << (n + row - col))):
            count += backtrack(n, holes, col + 1,
                               rows_filled | (1 << row),
                               diag_filled | (1 << (row + col)),
                               counter_diag_filled | (1 << (n + row - col)))
    return count

def main():
    N, M = [int(x) for x in raw_input().split()]
    while N or M:
        holes = set()
        for _ in range(M):
            x, y = raw_input().split()
            holes.add((int(x), int(y)))
        print backtrack(N, holes)

        N, M = [int(x) for x in raw_input().split()]

if __name__ == '__main__':
    main()
