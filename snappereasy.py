
def main():
    T = int(input())
    for case in range(1, T + 1):
        print("Case #{}: ".format(case), end='')
        N, K = map(int, input().split())
        if K % (2 ** N) == (2 ** N) - 1:
            print("ON")
        else:
            print("OFF")

if __name__ == '__main__':
    main()

