from math import sin, cos, pi

def handle_fd(x, y, a, val):
    nx = x + (val * cos(a))
    ny = y + (val * sin(a))
    return nx, ny, a

def handle_bk(x, y, a, val):
    return handle_fd(x, y, a, -val)

def handle_lt(x, y, a, val):
    return x, y, (a + (val * pi / 180)) % (pi * 2)

def handle_rt(x, y, a, val):
    return handle_lt(x, y, a, -val)

handle = {
    'fd': handle_fd,
    'bk': handle_bk,
    'lt': handle_lt,
    'rt': handle_rt,
}

def get_dist(x, y):
    return ((x ** 2) + (y ** 2)) ** 0.5

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        x, y, ang = 0, 0, 0
        for _ in range(N):
            cmd, val = input().split()
            x, y, ang = handle[cmd](x, y, ang, int(val))
        print(round(get_dist(x, y)))

if __name__ == '__main__':
    main()

