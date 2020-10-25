

def calc_days(D):
    return D + ((D + 1) * D) // 2


def main():
    N = int(input())
    for t in range(N):
        _, D = [int(x) for x in input().split()]
        print(t + 1, calc_days(D))


if __name__ == '__main__':
    main()
