
def main():
    L, X = [int(x) for x in input().split()]
    curr = 0
    turned_away = 0
    for _ in range(X):
        e, v = input().split()
        if e == 'leave':
            curr -= int(v)
        else:
            if L - curr < int(v):
                turned_away += 1
            else:
                curr += int(v)
    print(turned_away)


if __name__ == '__main__':
    main()

