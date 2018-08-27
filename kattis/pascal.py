
def main():
    N = int(raw_input())
    for i in xrange(2, int(N ** 0.5) + 1):
        if N % i == 0:
            o = N / i
            print N - o
            return
    print N - 1

if __name__ == '__main__':
    main()

