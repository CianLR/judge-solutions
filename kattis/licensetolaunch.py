

def main():
    N = int(input())
    junk = [int(x) for x in input().split()]
    min_day = -1
    min_junk = 1000000000000000
    for d, j in enumerate(junk):
        if j < min_junk:
            min_day = d
            min_junk = j
    print(min_day)

if __name__ == '__main__':
    main()
