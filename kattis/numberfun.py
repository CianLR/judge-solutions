import operator

OPS = [
    operator.add,
    operator.sub,
    operator.mul,
    operator.truediv,
]


def possible(a, b, c):
    for op in OPS:
        if op(a, b) == c or op(b, a) == c:
            return True
    return False


def main():
    T = int(input())
    for _ in range(T):
        a, b, c = map(int, input().split())
        print("Possible" if possible(a, b, c) else "Impossible")


if __name__ == '__main__':
    main()

