
def main():
    N = int(input())
    a = [int(x) for x in input().split()]
    mx = -1
    max_left = [None] * N
    for i in range(N):
        if a[i] > mx:
            mx = a[i]
        max_left[i] = mx
    mn = mx
    possible = 0
    for i in range(N - 1, -1, -1):
        if a[i] < mn:
            mn = a[i]
        if mn == max_left[i]:
            possible += 1
    print(possible)

if __name__ == '__main__':
    main()

