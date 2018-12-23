
def get_power(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level = (power_level / 100) % 10
    power_level -= 5
    return power_level


def make_summed_grid(grid):
    g2 = [[None] * len(x) for x in grid]
    for x in xrange(len(grid)):
        for y in xrange(len(grid[0])):
            g2[x][y] = grid[x][y]
            if x - 1 >= 0:
                g2[x][y] += g2[x - 1][y]
            if y - 1 >= 0:
                g2[x][y] += g2[x][y - 1]
            if x - 1 >= 0 and y - 1 >= 0:
                g2[x][y] -= g2[x - 1][y - 1]
    return g2

def grid_sum(grid, x, y, s):
    r = grid[x + s][y + s]
    if x - 1 >= 0:
        r -= grid[x - 1][y + s]
    if y - 1 >= 0:
        r -= grid[x + s][y - 1]
    if x - 1 >= 0 and y - 1 >= 0:
        r += grid[x - 1][y - 1]
    return r

def main():
    SERIAL = 1718
    grid = [[get_power(x, y, SERIAL) for y in xrange(1, 301)] for x in xrange(1, 301)]
    summed = make_summed_grid(grid)
    mx_power = -100000000000
    mx_cord = (None, None, None)
    for s in xrange(300):
        for x in xrange(300 - s):
            for y in xrange(300 - s):
                p = grid_sum(summed, x, y, s)
                if p > mx_power:
                    mx_power = p
                    mx_cord = (x + 1, y + 1, s + 1)
    print '{},{},{}'.format(*mx_cord)

if __name__ == '__main__':
    main()

