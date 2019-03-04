
def main():
    N = int(input())
    for _ in range(N):
        k, b, d = [int(x) for x in input().split()]
        ssd = 0
        while d > 0:
            ssd += (d % b) ** 2
            d //= b
        print(k, ssd)

if __name__ == '__main__':
    main()

