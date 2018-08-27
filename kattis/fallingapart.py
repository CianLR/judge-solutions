
def main():
    N = int(input())
    pieces = sorted((int(x) for x in input().split()), reverse=True)
    print(sum(pieces[::2]), sum(pieces[1::2]))


if __name__ == '__main__':
    main()

