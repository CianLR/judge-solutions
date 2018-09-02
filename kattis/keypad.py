

def litgrid_to_rc(R, C, grid):
    rows = [False] * R
    cols = [False] * C
    for r in xrange(R):
        for c in xrange(C):
            if grid[r][c] == '1':
                cols[c] = rows[r] = True
    return rows, cols

def is_impossible(R, C, grid, rows, cols):
    newgrid = [['0'] * C for _ in xrange(R)]
    for r in xrange(R):
        if not rows[r]:
            continue
        for c in xrange(C):
            if cols[c]:
                newgrid[r][c] = '1'
    return newgrid != grid

def get_prob_grid(R, C, grid, rows, cols):
    out_grid = [['N'] * C for _ in xrange(R)]
    for r in xrange(R):
        for c in xrange(C):
            if grid[r][c] != '1':
                continue
            grid[r][c] = '0'
            if litgrid_to_rc(R, C, grid) == (rows, cols):
                out_grid[r][c] = 'I'
            else:
                out_grid[r][c] = 'P'
            grid[r][c] = '1'
    return '\n'.join(map(''.join, out_grid))

def main():
    T = int(raw_input())
    for _ in xrange(T):
        R, C = [int(x) for x in raw_input().split()]
        grid = [list(raw_input()) for _ in xrange(R)]
        rows, cols = litgrid_to_rc(R, C, grid)
        if is_impossible(R, C, grid, rows, cols):
            print "impossible"
        else:
            print get_prob_grid(R, C, grid, rows, cols)
        print "-" * 10

if __name__ == '__main__':
    main()

