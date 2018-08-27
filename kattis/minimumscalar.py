
def scalar_prod(v1, v2):
    prod = 0
    for a, b in zip(v1, v2):
        prod += a * b
    return prod


def main():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        v1 = [int(x) for x in input().split()]
        v2 = [int(x) for x in input().split()]
        v1 = sorted(v1)
        v2 = sorted(v2, reverse=True)
        print("Case #{}: {}".format(t, scalar_prod(v1, v2)))

if __name__ == '__main__':
    main()

