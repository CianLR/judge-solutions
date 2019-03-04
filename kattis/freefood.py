
def main():
    N = int(input())
    free = set()
    for _ in range(N):
        s, t = [int(x) for x in input().split()]
        for d in range(s, t + 1):
            free.add(d)
    print(len(free))

if __name__ == '__main__':
    main()

