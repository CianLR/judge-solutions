
def main():
    N = int(raw_input())
    needed = [int(x) for x in raw_input().split()]
    bac = 1
    for b in needed:
        bac *= 2
        bac -= b
        if bac < 0:
            print "error"
            return
    print bac % 1000000007

if __name__ == '__main__':
    main()

