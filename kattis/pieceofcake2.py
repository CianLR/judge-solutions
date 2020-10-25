

def main():
    n, h, v = [int(x) for x in input().split()]
    sizes = [
        h       * v       * 4,
        (n - h) * v       * 4,
        h       * (n - v) * 4,
        (n - h) * (n - v) * 4,
    ]
    print(max(sizes))


if __name__ == '__main__':
    main()

