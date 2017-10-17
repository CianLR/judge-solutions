
def main():
    N = int(input())
    for _ in range(N):
        r, e, c = map(int, input().split())
        diff = r - (e - c)
        if diff < 0:
            print("advertise")
        elif diff == 0:
            print("does not matter")
        else:
            print("do not advertise")



if __name__ == '__main__':
    main()

