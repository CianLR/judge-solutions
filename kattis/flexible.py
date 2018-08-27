
def main():
    W, P = map(int, input().split())
    parts = [0] + [int(x) for x in input().split()] + [W]
    poss = set()
    for i, start in enumerate(parts):
        for end in parts[i + 1:]:
            poss.add(end - start)
    print(*sorted(poss))

if __name__ == '__main__':
    main()

