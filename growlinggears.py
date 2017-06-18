
def get_differ(a, b):
    # dy/dx = 0 = -2aR + b
    # R = b/2a
    return b / (2 * a)


def get_y(a, b, c, R):
    return (-a * (R ** 2)) + (b * R) + c


T = int(input())
for _ in range(T):
    G = int(input())
    max_torque = -1
    max_i = -1
    for i in range(1, G + 1):
        a, b, c, = map(int, input().split())
        dif = get_differ(a, b)
        tq = get_y(a, b, c, dif)
        if tq > max_torque:
            max_torque, max_i = tq, i
    print(max_i)
