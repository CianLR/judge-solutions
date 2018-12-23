
def get_power(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level = (power_level / 100) % 10
    power_level -= 5
    return power_level

def main():
    SERIAL = 1718
    grid = [[get_power(x, y, SERIAL) for y in xrange(1, 301)] for x in xrange(1, 301)]
    mx_power = -100000000000
    mx_cord = (None, None)
    for x in xrange(0, 298):
        for y in xrange(0, 298):
            p = 0
            for x2 in xrange(x, x + 3):
                for y2 in xrange(y, y + 3):
                    p += grid[x2][y2]
            if p > mx_power:
                mx_power = p
                mx_cord = (x + 1, y + 1)
    print '{},{}'.format(*mx_cord)

if __name__ == '__main__':
    main()

