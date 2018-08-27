
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b:
        a, b = b, a % b
    return a

def get_ratio(a, b):
    g = gcd(a, b)
    return '{}/{}'.format(a // g, b // g)


def main():
    N = int(input())
    gears = [int(x) for x in input().split()]
    for i in range(1, len(gears)):
        print(get_ratio(gears[0], gears[i]))


if __name__ == '__main__':
    main()

