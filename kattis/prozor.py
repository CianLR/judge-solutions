
def get_summed_grid(R, S, grid):
    summed = [[0] * S for _ in range(R)]
    summed[0][0] = int(grid[0][0])
    for i in range(1, R):
        summed[i][0] = summed[i - 1][0] + grid[i][0]
    for j in range(1, S):
        summed[0][j] = summed[0][j - 1] + grid[0][j]
    for i in range(1, R):
        for j in range(1, S):
            summed[i][j] = (grid[i][j] +
                            summed[i - 1][j] +
                            summed[i][j - 1] -
                            summed[i - 1][j - 1])
    return summed

def get_max(R, S, K, grid):
    throw = K - 2
    maxp = (-1, -1, -1)
    for i in range(R - throw - 1):
        for j in range(S - throw - 1):
            flies = (grid[i + throw][j + throw] -
                     grid[i + throw][j] -
                     grid[i][j + throw] +
                     grid[i][j])
            maxp = max(maxp, (flies, i, j))
    return maxp

def draw_racket(R, S, K, grid, I, J):
    strgrid = [[''] * S for _ in range(R)]
    for i in range(R):
        for j in range(S):
            vert = I <= i < I + K and (j == J or j == J + K - 1)
            horz = J <= j < J + K and (i == I or i == I + K - 1)
            if horz and vert:
                strgrid[i][j] = '+'
            elif horz:
                strgrid[i][j] = '-'
            elif vert:
                strgrid[i][j] = '|'
            else:
                strgrid[i][j] = '*' if grid[i][j] else '.'
    return strgrid

def main():
    R, S, K = map(int, input().split())
    grid = [
        [c == '*' for c in input()] for _ in range(R)
    ]
    summed = get_summed_grid(R, S, grid)
    m, i, j = get_max(R, S, K, summed)
    strgrid = draw_racket(R, S, K, grid, i, j)
    print(m)
    print('\n'.join(''.join(l) for l in strgrid))

if __name__ == '__main__':
    main()

